# Oral Defense Prompts

## 60-Second Repo Explanation

This repository is an artifact-first lab for GitHub-native agentic SDLC governance. It shows how coding agents can be managed through visible control-plane assets: custom agent profiles, MCP tool boundaries, GitHub Actions workflows, schemas, logs, memory examples, hooks, review gates, and durable artifacts. The central doctrine is simple: agents propose, GitHub records, workflows enforce, artifacts prove, hooks constrain, and humans approve high-risk action. The labs teach how to inspect failures before trusting an agent handoff or final report.

## 5-Minute Technical Walkthrough

Thesis:
Modern coding agents should not operate as invisible assistants. They should operate inside a governed SDLC where permissions, state, artifacts, and approvals are reviewable.

Doctrine:
Agents propose. GitHub records. Workflows enforce. Artifacts prove. Hooks constrain. Humans approve high-risk action.

Architecture:
The repo organizes governance assets across `.github/agents/`, `.github/workflows/`, `.github/hooks/`, `mcp/`, `memory/`, `logs/`, `artifacts/`, `schemas/`, `docs/`, and `labs/`.

Labs:
The lab sequence starts with agent profiles and workflow outputs, then moves through MCP authority, sessions, hooks, memory, multi-agent handoffs, output serialization, schema versus semantic validation, artifact transactions, and Zombie Pipeline failure.

Validation harness:
`scripts/validate_repo.py` gives the repo a dependency-free hygiene check for JSON parsing, lightweight schema contracts, public-safety scanning, and local Markdown references. It supports v1.0 readiness without claiming full JSON Schema compliance or production security scanning.

Why this matters:
Agentic SDLC risk often appears as broken state, stale memory, overbroad tool access, false consensus, or polished reports that hide failure. This repo teaches the operator to inspect evidence and identify deterministic controls.

## Explain These Concepts Out Loud

- Why agents propose but workflows enforce
- Why MCP is externalized authority
- Why memory is not authority
- Why schema validation is not truth
- Why a green workflow is not agentic success
- Why a consolidator must preserve dissent
- What a Zombie Pipeline is
- How hooks convert policy into enforcement

## Recruiter-Friendly Explanation

This project is a portfolio lab showing how I think about safe AI-assisted software delivery. Instead of building another demo app, it focuses on the governance layer around coding agents: who can do what, what evidence gets produced, how handoffs are validated, and when a human must approve. It includes realistic labs, sample artifacts, GitHub workflow patterns, schemas, and a validation harness so the repository can be reviewed like a real control-plane exercise.

## Engineering-Leader Explanation

This repo models GitHub as the control plane for agentic software delivery. It treats agent profiles, MCP permissions, workflow outputs, schemas, memory, logs, hooks, artifacts, and final reports as state boundaries that need deterministic validation. The labs demonstrate common operational failures such as authority expansion, stale session state, schema-valid but semantically weak artifacts, lossy consolidation, and Zombie Pipelines. The goal is not to claim a production security platform, but to show practical governance reasoning and reviewable evidence patterns for adopting coding agents safely.
