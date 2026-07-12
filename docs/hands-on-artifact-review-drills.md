# Hands-On Artifact Review Drills

These drills are repo-based practice scenarios, not official exam questions. They are designed to strengthen artifact literacy, control-plane reasoning, and scenario diagnosis.

## How to Use These Drills

Set a timer, inspect the listed artifacts, and answer the task before reading the expected answer. Explain the control failure out loud, then identify the deterministic control that should fail closed. Repeat any drill that you cannot explain without relying on the answer key.

## Drill Format

Each drill supplies a timebox, scenario, artifacts to inspect, task, expected answer, control pattern, and a short statement to practice out loud.

## Drill 1: Agent Profile Grants Unclear Authority

**Timebox:** 6 minutes

**Scenario:** An executor profile can edit and execute, but the profile does not make the approval boundary obvious.

**Artifacts to inspect:** `.github/agents/executor.agent.md`, `.github/agents/planner.agent.md`, `artifacts/agent-profile-review-report.json`, and `labs/lab-01-read-agent-file.md`.

**Task:** Identify the ambiguous authority and the evidence required before execution.

**Expected answer:** A descriptive role is not authorization. High-impact execution requires an explicit, current approval bound to the reviewed plan and repository state.

**Control pattern:** A workflow or pre-execution gate validates role, scope, approval, and current commit before granting execution.

**What to say out loud:** "The profile describes capability; a deterministic gate grants authority for this specific action."

## Drill 2: Workflow Output Key Drift

**Timebox:** 7 minutes

**Scenario:** A producer writes one output key while a downstream job reads a different key, yet the workflow remains visually green.

**Artifacts to inspect:** `.github/workflows/agent-plan-review.yml`, `artifacts/workflow-validation-report.json`, and `labs/lab-02-debug-workflow-output.md`.

**Task:** Find the producer-consumer contract and explain why status alone is insufficient.

**Expected answer:** The handoff fails when the consumer reads a key the producer never emitted. A green job only proves step completion, not that the expected value arrived.

**Control pattern:** Validate required output keys and non-empty values at the handoff boundary; fail before downstream work begins.

**What to say out loud:** "Workflow success must include contract-valid outputs, not only successful process exit codes."

## Drill 3: MCP Wildcard Tool Expansion

**Timebox:** 6 minutes

**Scenario:** An MCP server configuration permits wildcard tool access, allowing future tools to become available without a new review.

**Artifacts to inspect:** `mcp/broad-server-wildcard-risk.yml`, `mcp/server-manifest-snapshot.json`, `artifacts/mcp-boundary-review-report.json`, and `labs/lab-03-identify-mcp-risk.md`.

**Task:** Explain how reviewed authority can drift after the configuration is approved.

**Expected answer:** The wildcard delegates authority to the server's evolving tool inventory. A newly exposed tool can silently widen the agent's effective permissions.

**Control pattern:** Pin an explicit tool allowlist and compare the current server manifest with the approved snapshot before use.

**What to say out loud:** "MCP is externalized authority, so tool inventory changes are permission changes."

## Drill 4: Resumed Session with Stale Commit SHA

**Timebox:** 7 minutes

**Scenario:** A resumed session relies on context captured from an older commit.

**Artifacts to inspect:** `logs/copilot-cli-session-resumed.log`, `artifacts/session-continuity-report.json`, `artifacts/git-state-snapshot.json`, and `labs/lab-04-analyze-session-log.md`.

**Task:** Determine whether the session may continue and name the required freshness check.

**Expected answer:** The session must not act until its stored commit and branch are reconciled with the current repository state. Stale reasoning may describe files or approvals that no longer apply.

**Control pattern:** Bind resumable state to branch and commit, then invalidate or re-review it on mismatch.

**What to say out loud:** "Session continuity is valid only when its state is current and provenance-bound."

## Drill 5: Hook Logs but Does Not Block

**Timebox:** 6 minutes

**Scenario:** A pre-tool hook records a denied execution request but allows the tool call to continue.

**Artifacts to inspect:** `.github/hooks/preToolUse-deny-execute.example.json`, `artifacts/hook-enforcement-report.json`, `logs/workflow-permission-denied.log`, and `labs/lab-05-hook-permission-decision.md`.

**Task:** Distinguish observability from enforcement.

**Expected answer:** Logging creates evidence but does not prevent harm. A deny decision must stop the tool before execution and return a machine-verifiable failure.

**Control pattern:** Pre-tool interception with explicit deny semantics, non-bypassable failure, and approval binding.

**What to say out loud:** "A control that only records a violation is telemetry, not prevention."

## Drill 6: Memory Fact Conflicts with Agent Profile

**Timebox:** 7 minutes

**Scenario:** Repository memory says an agent may publish, while the current agent profile limits it to review.

**Artifacts to inspect:** `memory/repository-facts-example.json`, `.github/agents/reviewer.agent.md`, `artifacts/memory-authority-review-report.json`, and `labs/lab-06-memory-drift.md`.

**Task:** Decide which source governs and how the conflict should be handled.

**Expected answer:** Memory is context, not authority. The current reviewed profile and workflow policy govern; conflicting memory must be quarantined or refreshed.

**Control pattern:** Validate memory against authoritative current configuration before injecting it into an agent session.

**What to say out loud:** "Memory can inform a decision, but it cannot grant a permission."

## Drill 7: Consolidator Drops Dissent

**Timebox:** 8 minutes

**Scenario:** A consolidated report shows consensus but omits a reviewer's conditional rejection.

**Artifacts to inspect:** `artifacts/multi-agent-manifest.json`, `artifacts/consolidated-operator-report.json`, `artifacts/consolidation-fidelity-report.json`, and `labs/lab-07-multi-agent-handoff.md`.

**Task:** Identify the lost decision signal and its effect on approval.

**Expected answer:** The consolidation is not faithful because unresolved dissent and conditions are decision-relevant evidence. Approval must remain blocked until they are preserved and resolved.

**Control pattern:** Reconcile every source finding by stable identifier and fail when findings are omitted, weakened, or unresolved.

**What to say out loud:** "A consolidator may summarize wording, but it must preserve dissent and decision impact."

## Drill 8: Reviewer Scratchpad Leaks into Docs

**Timebox:** 6 minutes

**Scenario:** Internal reviewer notes are serialized into a public documentation artifact.

**Artifacts to inspect:** `logs/reviewer-scratchpad.json`, `artifacts/reviewer-note-leakage-report.json`, `artifacts/publication-readiness-report.json`, and `labs/lab-08-reviewer-note-leakage.md`.

**Task:** Explain why the content boundary failed even if the notes contain no secret.

**Expected answer:** Internal reasoning and scratch state are not approved publication inputs. Leakage can expose unsupported claims, provisional judgments, or irrelevant internal context.

**Control pattern:** Serialize only an explicit public output contract and require a promotion review before publication.

**What to say out loud:** "Public artifacts come from approved fields, not from the agent's entire working context."

## Drill 9: Schema-Valid Artifact Contains Semantic Nulls

**Timebox:** 8 minutes

**Scenario:** An artifact parses and satisfies required field types, but decision-critical fields contain null-like or placeholder meaning.

**Artifacts to inspect:** `schemas/schema-semantic-validation-report.schema.json`, `artifacts/schema-semantic-validation-report.json`, `artifacts/agent-handoff-valid-v2.json`, and `labs/lab-09-schema-validation-failure.md`.

**Task:** Separate structural validity from semantic readiness.

**Expected answer:** Schema validity proves shape, not truth, completeness, freshness, or usefulness. Decision-critical values require domain checks and evidence.

**Control pattern:** Run semantic invariants after schema validation and fail closed on absent, placeholder, contradictory, or stale values.

**What to say out loud:** "A valid envelope can still carry an unusable handoff."

## Drill 10: Green Workflow Consumes Wrong Artifact

**Timebox:** 8 minutes

**Scenario:** A downstream job successfully downloads an artifact from the wrong run or commit.

**Artifacts to inspect:** `.github/workflows/multi-agent-artifact-handoff.yml`, `artifacts/artifact-provenance-manifest.json`, `artifacts/artifact-transaction-report.json`, and `labs/lab-10-github-actions-artifact-handoff-drill.md`.

**Task:** Identify the provenance mismatch and explain why the successful download must be rejected.

**Expected answer:** Availability is not authenticity. The artifact must match the expected run, branch, commit, job, producer, and digest before consumption.

**Control pattern:** Verify provenance and integrity as one atomic artifact transaction before deserialization or use.

**What to say out loud:** "A green download proves transport; provenance proves that this is the intended artifact."

## Drill 11: Zombie Pipeline with Zero Processed Items

**Timebox:** 9 minutes

**Scenario:** Jobs keep succeeding and retrying while the processed-item count remains zero.

**Artifacts to inspect:** `artifacts/zombie-pipeline-failure-report.json`, `artifacts/pipeline-execution-checkpoint.json`, `artifacts/billing-and-token-telemetry.json`, and `labs/lab-11-advanced-agent-handoff-failure.md`.

**Task:** Diagnose the gap between visible activity and semantic progress.

**Expected answer:** The pipeline is alive operationally but dead semantically. Repeated success without progress wastes budget and can conceal a broken handoff or empty input.

**Control pattern:** Track semantic progress, enforce retry and token budgets, and fail closed when progress remains zero.

**What to say out loud:** "Activity is not progress; zero processed items is a terminal control signal."

## Drill 12: Validation Harness Catches Broken Repo Reference

**Timebox:** 5 minutes

**Scenario:** A documentation edit points to a local file that does not exist.

**Artifacts to inspect:** `scripts/validate_repo.py`, `docs/repo-validation-governance.md`, `.github/workflows/validate-repo.yml`, and `scripts/README.md`.

**Task:** Predict the validation result and describe the narrow repair.

**Expected answer:** The local Markdown reference check should fail and identify the source reference. Repair the link or add the intentionally referenced artifact, then rerun validation.

**Control pattern:** Run deterministic repository validation locally and on pull requests; block promotion on broken references.

**What to say out loud:** "Documentation references are repository contracts, so the validation gate should reject broken local paths."
