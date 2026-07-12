# Weak-Area Scorecard

Use this scorecard to measure readiness before the cram sprint and exam. Score from evidence you can inspect and explain, not from familiarity alone.

| Skill Area | Self-Score 1-5 | Evidence I Can Explain | Files to Revisit | Notes |
| --- | --- | --- | --- | --- |
| Agent profiles and role boundaries |  |  | `.github/agents/`, `labs/lab-01-read-agent-file.md` |  |
| MCP tool authority |  |  | `mcp/`, `labs/lab-03-identify-mcp-risk.md` |  |
| GitHub Actions workflow gates |  |  | `.github/workflows/`, `labs/lab-02-debug-workflow-output.md` |  |
| Artifact provenance |  |  | `artifacts/artifact-provenance-manifest.json`, `labs/lab-10-github-actions-artifact-handoff-drill.md` |  |
| Schema versus semantic validation |  |  | `schemas/`, `labs/lab-09-schema-validation-failure.md` |  |
| Memory governance |  |  | `memory/`, `labs/lab-06-memory-drift.md` |  |
| Session continuity |  |  | `logs/copilot-cli-session-resumed.log`, `labs/lab-04-analyze-session-log.md` |  |
| Hook enforcement |  |  | `.github/hooks/`, `labs/lab-05-hook-permission-decision.md` |  |
| Output serialization |  |  | `logs/reviewer-scratchpad.json`, `labs/lab-08-reviewer-note-leakage.md` |  |
| Multi-agent consolidation |  |  | `artifacts/consolidation-fidelity-report.json`, `labs/lab-07-multi-agent-handoff.md` |  |
| Cost/retry/context controls |  |  | `artifacts/billing-and-token-telemetry.json`, `docs/cost-and-retry-control.md` |  |
| Zombie Pipeline diagnosis |  |  | `artifacts/zombie-pipeline-failure-report.json`, `labs/lab-11-advanced-agent-handoff-failure.md` |  |
| Repo validation harness |  |  | `scripts/validate_repo.py`, `docs/repo-validation-governance.md` |  |

## Scoring Guidance

- **1:** I recognize the term.
- **2:** I can define it.
- **3:** I can inspect repo artifacts for it.
- **4:** I can diagnose a failure scenario.
- **5:** I can explain the control pattern clearly under pressure.

## Pass-Ready Threshold

Use this practical target rather than treating the score as a certification guarantee:

- No skill area below 3.
- At least 8 areas at 4 or higher.
- Able to explain Labs 01, 03, 05, 07, 09, and 11 without notes.
