# Validation Scripts

`validate_repo.py` provides a lightweight, dependency-free repository validation harness for this artifact-first lab.

It checks:

- JSON parse validity under `artifacts/`, `memory/`, `.github/hooks/`, `schemas/`, `mcp/`, and `logs/`
- lightweight schema contract checks for required fields
- top-level enum and const checks where simple
- no-secrets posture using conservative educational patterns
- local Markdown references to repo files

It does not check:

- full JSON Schema Draft 2020-12 compliance
- semantic truth of artifact contents
- production-grade secret detection
- external URLs
- runtime behavior of workflows or agents

The script uses only the Python standard library so it can run locally and in GitHub Actions without adding dependencies.

Run:

```bash
python scripts/validate_repo.py
```

Required-field checks are lightweight contract checks, not full JSON Schema validation. The no-secrets scan is educational and conservative: it reports documentation matches, but only fails on simple high-risk key-like patterns. This script exists to support public repo hygiene and v1.0 readiness.
