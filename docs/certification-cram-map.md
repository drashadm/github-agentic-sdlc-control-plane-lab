# Certification Cram Map

This document is a repo-based study map, not an official exam guide. It maps practical repository artifacts to agentic SDLC skills the operator should be able to explain, inspect, and reason about.

## How to Use This Cram Map

Review the repository artifacts, not just the prose. Inspect workflows, schemas, logs, MCP examples, hooks, validation output, and lab answer keys.

For each topic, practice explaining what can go wrong, which artifact proves it, and what deterministic control prevents it. Focus on artifact literacy and control-plane reasoning: agents may propose or summarize, but GitHub workflows, schemas, hooks, reviews, and preserved artifacts are the inspectable evidence.

## 7-Day Cram Sprint

### Day 1: Repo Orientation and Validation

Files to read:
- `README.md`
- `docs/vulnerability-to-defense-matrix.md`
- `labs/README.md`
- `docs/repo-validation-governance.md`
- `scripts/README.md`

Artifacts to inspect:
- `scripts/validate_repo.py`
- `.github/workflows/validate-repo.yml`
- `docs/artifact-schema-map.md`

Questions to answer:
- What is the repository thesis?
- Why is this an artifact-first lab rather than an app?
- What does the validation harness prove, and what does it not prove?

Output to produce:
- A one-page orientation note explaining the doctrine, lab sequence, and validation harness.

### Day 2: Agent Authority Boundaries

Files to read:
- `.github/agents/planner.agent.md`
- `.github/agents/executor.agent.md`
- `.github/agents/reviewer.agent.md`
- `docs/mcp-tool-boundary-governance.md`
- `docs/hook-enforcement-governance.md`

Artifacts to inspect:
- `mcp/broad-server-wildcard-risk.yml`
- `mcp/local-stdio-risky-example.yml`
- `.github/hooks/preToolUse-deny-execute.example.json`
- `artifacts/mcp-boundary-review-report.json`
- `artifacts/hook-enforcement-report.json`

Questions to answer:
- Why are agent profiles control-plane assets?
- Why is MCP access externalized authority?
- What makes a hook advisory versus enforceable?

Output to produce:
- A role-boundary review comparing planner, executor, reviewer, MCP, and hook controls.

### Day 3: Workflow Handoffs and Provenance

Files to read:
- `docs/state-serializability.md`
- `docs/artifact-transaction-governance.md`
- `docs/workflow-validation-guide.md`
- `docs/workflow-dry-run-checklist.md`

Artifacts to inspect:
- `.github/workflows/multi-agent-artifact-handoff.yml`
- `.github/workflows/agent-plan-review.yml`
- `artifacts/planner-state-manifest.json`
- `artifacts/artifact-transaction-report.json`
- `artifacts/artifact-provenance-manifest.json`

Questions to answer:
- Why is a green workflow not enough evidence?
- Which fields bind an artifact to a run, branch, commit, workflow, and job?
- What should fail closed before downstream invocation?

Output to produce:
- A handoff checklist for validating workflow outputs and artifact provenance.

### Day 4: Memory, Session Continuity, and Context

Files to read:
- `docs/memory-governance.md`
- `docs/session-continuity-governance.md`
- `docs/context-window-gating.md`
- `labs/lab-04-analyze-session-log.md`
- `labs/lab-06-memory-drift.md`

Artifacts to inspect:
- `memory/repository-facts-example.json`
- `memory/memory-vector-index.lock.json`
- `artifacts/session-continuity-report.json`
- `artifacts/memory-validation-report.json`
- `artifacts/git-state-snapshot.json`

Questions to answer:
- Why is memory an untrusted cache?
- What evidence proves a resumed session is still current?
- How can context growth make a failure worse?

Output to produce:
- A stale-state triage note listing memory, branch, commit, run, and approval checks.

### Day 5: Schemas, Semantics, and Publication Gates

Files to read:
- `docs/schema-semantic-validation-governance.md`
- `docs/output-serialization-governance.md`
- `labs/lab-08-reviewer-note-leakage.md`
- `labs/lab-09-schema-validation-failure.md`

Artifacts to inspect:
- `schemas/schema-semantic-validation-report.schema.json`
- `artifacts/schema-semantic-validation-report.json`
- `logs/reviewer-scratchpad.json`
- `artifacts/publication-readiness-report.json`
- `artifacts/reviewer-note-leakage-report.json`

Questions to answer:
- Why does schema validation prove shape, not truth?
- What is a semantic null?
- What should be excluded from public artifacts?

Output to produce:
- A short review explaining structural validity, semantic validity, and output promotion.

### Day 6: Multi-Agent Failure and Retry Controls

Files to read:
- `docs/multi-agent-coordination-governance.md`
- `docs/cost-and-retry-control.md`
- `docs/zombie-pipeline-governance.md`
- `docs/advanced-agentic-failure-modes.md`
- `labs/lab-07-multi-agent-handoff.md`
- `labs/lab-11-advanced-agent-handoff-failure.md`

Artifacts to inspect:
- `artifacts/multi-agent-manifest.json`
- `artifacts/consolidation-fidelity-report.json`
- `artifacts/billing-and-token-telemetry.json`
- `artifacts/zombie-pipeline-failure-report.json`
- `artifacts/compound-handoff-failure-report.json`

Questions to answer:
- Why must a consolidator preserve dissent?
- How can retry loops create cost and context risk?
- What is a Zombie Pipeline?

Output to produce:
- A compound-failure explanation that traces one failure across state, schema, memory, artifact, retry, and final approval boundaries.

### Day 7: Mock Review

Files to read:
- `docs/exam-style-practice-questions.md`
- `docs/oral-defense-prompts.md`
- `docs/v0.5-capstone-review.md`
- `docs/repo-validation-governance.md`

Artifacts to inspect:
- Six labs of your choice, including Labs 01, 02, 05, 07, 09, and 11
- `scripts/validate_repo.py`
- The latest output from `python scripts/validate_repo.py`

Questions to answer:
- Can you explain six labs out loud without reading?
- Can you identify the deterministic control for each failure?
- Can you explain what the repository does not claim?

Output to produce:
- A mock defense transcript and a weak-area list for final review.

## Skill-to-Artifact Map

| Skill Area | What to Know | Repo Artifacts to Inspect | Labs |
| --- | --- | --- | --- |
| Custom agent profiles and role boundaries | Agent profiles shape role, authority, tool scope, and review obligations. | `.github/agents/planner.agent.md`, `.github/agents/executor.agent.md`, `.github/agents/reviewer.agent.md`, `artifacts/agent-profile-review-report.json` | Lab 01 |
| MCP tool access and external authority | MCP tools can expand runtime capability beyond reviewed intent. | `mcp/broad-server-wildcard-risk.yml`, `mcp/local-stdio-risky-example.yml`, `docs/mcp-tool-boundary-governance.md`, `artifacts/mcp-boundary-review-report.json` | Lab 03 |
| GitHub Actions workflow gates | Workflows can record evidence, enforce checks, and block unsafe handoffs. | `.github/workflows/agent-plan-review.yml`, `.github/workflows/multi-agent-artifact-handoff.yml`, `.github/workflows/validate-repo.yml`, `docs/workflow-validation-guide.md` | Labs 02, 10 |
| Artifact handoff and provenance | Downstream agents need current, complete, provenance-bound artifacts. | `artifacts/artifact-provenance-manifest.json`, `artifacts/artifact-transaction-report.json`, `artifacts/planner-state-manifest.json` | Labs 02, 10, 11 |
| JSON schemas and validation limits | Schema checks validate shape and required fields, not semantic truth. | `schemas/`, `artifacts/schema-semantic-validation-report.json`, `scripts/validate_repo.py`, `docs/schema-semantic-validation-governance.md` | Lab 09 |
| Memory/state/session continuity | Memory and resumed sessions must be checked against current repository state. | `memory/repository-facts-example.json`, `artifacts/session-continuity-report.json`, `artifacts/memory-validation-report.json` | Labs 04, 06 |
| Hooks and pre-tool enforcement | Hooks are strongest when they mediate actions before execution and fail closed. | `.github/hooks/preToolUse-deny-execute.example.json`, `artifacts/intent-analysis-payload.json`, `artifacts/hook-enforcement-report.json` | Lab 05 |
| Multi-agent coordination and consolidator risks | Consolidators must preserve dissent, conditional approvals, and unresolved findings. | `artifacts/multi-agent-manifest.json`, `artifacts/consolidation-fidelity-report.json`, `docs/multi-agent-coordination-governance.md` | Lab 07 |
| Output serialization and public artifact promotion | Draft notes and internal state must not leak into public outputs. | `logs/reviewer-scratchpad.json`, `artifacts/reviewer-note-leakage-report.json`, `artifacts/publication-readiness-report.json` | Lab 08 |
| Cost/retry/context-window controls | Retry loops need budgets, stop conditions, and context-window limits. | `artifacts/billing-and-token-telemetry.json`, `docs/cost-and-retry-control.md`, `docs/context-window-gating.md` | Labs 04, 11 |
| Zombie Pipeline and compound failure review | Visible success can hide collapsed agentic state and zero semantic progress. | `artifacts/zombie-pipeline-failure-report.json`, `artifacts/compound-handoff-failure-report.json`, `docs/zombie-pipeline-governance.md` | Lab 11 |
| Repository validation and public-safety hygiene | Public artifact labs need repeatable checks for parseability, references, and high-risk patterns. | `scripts/validate_repo.py`, `scripts/README.md`, `docs/repo-validation-governance.md`, `.github/workflows/validate-repo.yml` | All labs |
