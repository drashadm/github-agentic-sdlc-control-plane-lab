#!/usr/bin/env python3
"""Dependency-free repository validation harness.

This script is intentionally lightweight. It is not a full JSON Schema Draft
2020-12 implementation. It validates JSON parsing, top-level required fields,
and simple top-level enum/const constraints for matching artifact/schema pairs.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]

JSON_ROOTS = [
    "artifacts",
    "memory",
    ".github/hooks",
    "schemas",
    "mcp",
    "logs",
]

SCHEMA_ARTIFACT_ROOTS = [
    "artifacts",
    "logs",
    "memory",
    "mcp",
]

SCHEMA_ARTIFACT_ALIASES = {
    "agent-handoff-v2.schema.json": ["artifacts/agent-handoff-valid-v2.json"],
}

SECRET_SCAN_ROOTS = [
    "README.md",
    "docs",
    "labs",
    "artifacts",
    "memory",
    ".github",
    "schemas",
    "mcp",
    "logs",
]

MARKDOWN_ROOTS = [
    "README.md",
    "docs",
    "labs",
]

SECRET_PATTERNS = [
    "api_key",
    "token",
    "secret",
    "password",
    "credential",
    "private_key",
    "BEGIN PRIVATE KEY",
    "sk-",
]

HIGH_RISK_PATTERNS = [
    re.compile(r"BEGIN PRIVATE KEY", re.IGNORECASE),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    re.compile(
        r"\b(?:password|api_key|token)\s*=\s*(?![\"']?(?:placeholder|example|changeme|dummy|fake|redacted|null|none|<[^>]+>)[\"']?\b)[\"']?[^\"'\s]+",
        re.IGNORECASE,
    ),
]

LOCAL_REF_RE = re.compile(
    r"(?<![A-Za-z0-9_.-])"
    r"((?:\.github|docs|labs|artifacts|schemas|memory|mcp|logs)/"
    r"[A-Za-z0-9_./#?=-]+?\.(?:md|json|ya?ml|log))",
    re.IGNORECASE,
)


@dataclass
class ValidationResult:
    json_files_checked: int = 0
    json_parse_failures: list[str] = field(default_factory=list)
    schema_pairs_checked: int = 0
    schema_failures: list[str] = field(default_factory=list)
    secret_findings: list[str] = field(default_factory=list)
    high_risk_secret_findings: list[str] = field(default_factory=list)
    markdown_refs_checked: int = 0
    missing_markdown_refs: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def failures(self) -> list[str]:
        return (
            self.json_parse_failures
            + self.schema_failures
            + self.high_risk_secret_findings
            + self.missing_markdown_refs
        )


def iter_files(paths: list[str], suffixes: tuple[str, ...] | None = None) -> list[Path]:
    files: list[Path] = []
    for raw_path in paths:
        path = REPO_ROOT / raw_path
        if not path.exists():
            continue
        if path.is_file():
            if suffixes is None or path.name.lower().endswith(suffixes):
                files.append(path)
            continue
        for child in path.rglob("*"):
            if child.is_file() and (suffixes is None or child.name.lower().endswith(suffixes)):
                files.append(child)
    return sorted(set(files))


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_json_parse(result: ValidationResult) -> None:
    for path in iter_files(JSON_ROOTS, (".json",)):
        result.json_files_checked += 1
        try:
            load_json(path)
        except Exception as exc:  # noqa: BLE001 - report parser detail.
            result.json_parse_failures.append(f"{rel(path)}: {exc}")


def artifact_candidates(schema_path: Path) -> list[Path]:
    aliases = SCHEMA_ARTIFACT_ALIASES.get(schema_path.name, [])
    candidates = [REPO_ROOT / alias for alias in aliases if (REPO_ROOT / alias).is_file()]
    base_name = schema_path.name.removesuffix(".schema.json")
    expected_names = {
        f"{base_name}.json",
        f"{base_name}.lock.json",
    }
    for root in SCHEMA_ARTIFACT_ROOTS:
        root_path = REPO_ROOT / root
        if not root_path.exists():
            continue
        for path in root_path.rglob("*.json"):
            if path.name in expected_names:
                candidates.append(path)
    return sorted(candidates)


def validate_schema_contracts(result: ValidationResult) -> None:
    for schema_path in sorted((REPO_ROOT / "schemas").glob("*.schema.json")):
        try:
            schema = load_json(schema_path)
        except Exception as exc:  # noqa: BLE001 - JSON parse phase reports this too.
            result.schema_failures.append(f"{rel(schema_path)} could not be loaded: {exc}")
            continue

        candidates = artifact_candidates(schema_path)
        if not candidates:
            result.warnings.append(f"No matching artifact found for {rel(schema_path)}")
            continue

        for artifact_path in candidates:
            result.schema_pairs_checked += 1
            try:
                artifact = load_json(artifact_path)
            except Exception as exc:  # noqa: BLE001
                result.schema_failures.append(f"{rel(artifact_path)} could not be loaded: {exc}")
                continue

            if not isinstance(artifact, dict):
                result.schema_failures.append(f"{rel(artifact_path)} is not a JSON object")
                continue

            required = schema.get("required", [])
            for field_name in required:
                if field_name not in artifact:
                    result.schema_failures.append(
                        f"{rel(artifact_path)} missing required field '{field_name}' from {rel(schema_path)}"
                    )

            properties = schema.get("properties", {})
            for field_name, field_schema in properties.items():
                if field_name not in artifact or not isinstance(field_schema, dict):
                    continue
                value = artifact[field_name]
                if "const" in field_schema and value != field_schema["const"]:
                    result.schema_failures.append(
                        f"{rel(artifact_path)} field '{field_name}' expected const {field_schema['const']!r}, found {value!r}"
                    )
                if "enum" in field_schema and value not in field_schema["enum"]:
                    result.schema_failures.append(
                        f"{rel(artifact_path)} field '{field_name}' value {value!r} not in enum {field_schema['enum']!r}"
                    )


def is_text_file(path: Path) -> bool:
    return path.suffix.lower() in {
        ".md",
        ".json",
        ".yml",
        ".yaml",
        ".log",
        ".txt",
        ".gitignore",
    } or path.name in {"README.md"}


def validate_secret_posture(result: ValidationResult) -> None:
    pattern_re = re.compile("|".join(re.escape(pattern) for pattern in SECRET_PATTERNS), re.IGNORECASE)
    for path in iter_files(SECRET_SCAN_ROOTS):
        if not is_text_file(path):
            continue
        try:
            lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        except OSError as exc:
            result.warnings.append(f"Could not read {rel(path)} for secret scan: {exc}")
            continue
        for line_number, line in enumerate(lines, start=1):
            if pattern_re.search(line):
                finding = f"{rel(path)}:{line_number}: {line.strip()}"
                result.secret_findings.append(finding)
                if any(pattern.search(line) for pattern in HIGH_RISK_PATTERNS):
                    result.high_risk_secret_findings.append(finding)


def normalize_ref(raw_ref: str) -> str:
    ref = raw_ref.split("#", 1)[0].split("?", 1)[0]
    return ref.rstrip(".,;:)]}'\"")


def validate_markdown_refs(result: ValidationResult) -> None:
    for path in iter_files(MARKDOWN_ROOTS, (".md",)):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in LOCAL_REF_RE.finditer(text):
            reference = normalize_ref(match.group(1))
            if not reference:
                continue
            result.markdown_refs_checked += 1
            if not (REPO_ROOT / reference).is_file():
                result.missing_markdown_refs.append(
                    f"{rel(path)} references missing local file {reference}"
                )


def print_section(title: str, lines: list[str], max_lines: int = 40) -> None:
    print(f"\n{title}")
    if not lines:
        print("  none")
        return
    for line in lines[:max_lines]:
        print(f"  - {line}")
    if len(lines) > max_lines:
        print(f"  ... {len(lines) - max_lines} more")


def main() -> int:
    result = ValidationResult()

    validate_json_parse(result)
    validate_schema_contracts(result)
    validate_secret_posture(result)
    validate_markdown_refs(result)

    print("Repository validation summary")
    print("=============================")
    print(f"JSON files checked: {result.json_files_checked}")
    print(f"Schema contract pairs checked: {result.schema_pairs_checked}")
    print(f"Secret scan findings: {len(result.secret_findings)}")
    print(f"Markdown references checked: {result.markdown_refs_checked}")
    print(f"Warnings: {len(result.warnings)}")
    print(f"Failures: {len(result.failures)}")

    print_section("JSON parse failures", result.json_parse_failures)
    print_section("Schema contract failures", result.schema_failures)
    print_section("High-risk secret findings", result.high_risk_secret_findings)
    print_section("Missing local Markdown references", result.missing_markdown_refs)
    print_section("Warnings", result.warnings)

    if result.secret_findings:
        print_section("Secret scan findings (reported, not automatically failing unless high-risk)", result.secret_findings)

    if result.failures:
        print("\nFinal status: FAIL")
        return 1

    print("\nFinal status: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
