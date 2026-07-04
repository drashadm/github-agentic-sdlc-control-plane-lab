# Lab 02: Debug Workflow Output Handoff

## Difficulty

Intermediate.

## Estimated Time

15-20 minutes.

## Scenario

A Builder Agent cannot find the planner artifact it expects. In a normal CI workflow, this might look like a wiring bug. In a multi-agent workflow, it is an unhandled exception in a distributed state machine: the Planner Agent failed to serialize state deterministically, and the Builder Agent may continue with empty input, stale cached context, malformed state, or hallucinated assumptions.

## Artifacts to Inspect

- `.github/workflows/multi-agent-artifact-handoff.yml`
- `.github/workflows/consolidated-operator-report.yml`
- `artifacts/planner-output.json`
- `artifacts/builder-diff-summary.json`
- `artifacts/planner-state-manifest.json`
- `artifacts/stale-agent-state-cache-example.json`
- `docs/cost-and-retry-control.md`
- `docs/advanced-agentic-failure-modes.md`

## What You Are Looking For

Trace the producing job, step output, job output, `needs` dependency, upload artifact name, download artifact name, and planner state manifest. Confirm that the artifact name is deterministic, normalized, schema-backed, bound to the current run/branch/commit, and configured to block downstream execution if missing.

Also look for stale-cache risk: if the current planner state is missing, the Builder Agent must not fall back to a previous run's artifact unless that fallback is explicitly approved, labeled, and reviewed.

## Questions

1. Which workflow job produces `plan_artifact_name`, and which job consumes it?
2. If the builder job receives an empty string for `plan_artifact_name`, what should happen before the Builder Agent is invoked?
3. Why is a missing workflow output more dangerous in an agentic workflow than in a normal CI workflow?
4. If the Planner Agent writes `plan_artifact_name=" planner-output "` with unexpected whitespace, why can the artifact download fail even though the workflow syntax is valid?
5. What is the risk if the Builder Agent falls back to a cached planner artifact from a previous run?
6. How does schema validation reduce the chance that a downstream agent hallucinates missing state?
7. What evidence proves the Builder Agent consumed the correct planner output for the current branch, run ID, and commit SHA?
8. Why should retry loops have explicit stop conditions and cost/rate-limit controls?

## Expected Reasoning Path

Start with the `planner` job and find its `outputs` block. Follow `plan_artifact_name` to the step with `id: plan`, then compare the value written to `$GITHUB_OUTPUT` with the uploaded artifact name. Next, inspect the `builder` job and confirm it uses `needs: planner` and downloads the exact artifact name produced by the planner.

Then move from workflow wiring to state integrity. Inspect `artifacts/planner-state-manifest.json` and verify the expected artifact name, normalized artifact name, output key, run ID, run attempt, commit SHA, source branch, `state_status`, and `downstream_blocked_if_missing`. Compare that with `artifacts/stale-agent-state-cache-example.json` to understand why previous-run fallback context is dangerous. A safe operator treats empty, null, stale, or schema-invalid state as a blocking condition before any Builder Agent invocation.

## Answer Key

1. The `planner` job produces `plan_artifact_name`; the `builder` job consumes it through `needs.planner.outputs.plan_artifact_name`.
2. The workflow should fail closed before invoking the Builder Agent. Empty state should be marked invalid and preserved as evidence.
3. A downstream agent may guess, reuse stale context, retry repeatedly, or produce a plausible report without real planner state.
4. Artifact names are exact strings. Unexpected whitespace changes the name, so `actions/download-artifact` may look for an artifact that was never uploaded.
5. The Builder Agent may reason, plan, or build against stale instructions from a previous run, branch, or commit.
6. Schema validation makes missing or malformed required state visible before the downstream agent has a chance to infer or hallucinate it.
7. Evidence includes the planner state manifest fields: `run_id`, `run_attempt`, `commit_sha`, `source_branch`, `expected_artifact_name`, `normalized_artifact_name`, `output_key`, and `state_status`.
8. Missing artifacts can trigger repeated downloads, LLM regenerations, or tool calls. Stop conditions, backoff, explicit failure state, and cost/rate-limit annotations prevent waste and hide less of the root cause.

## Common Wrong Answers

- Treating workflow output values as harmless strings instead of state contracts.
- Assuming a passed workflow means the Builder Agent consumed valid planner state.
- Allowing fallback to a cached planner artifact without labeling it stale.
- Trimming or renaming artifact names downstream without fixing the producing contract.
- Retrying indefinitely instead of surfacing the missing or invalid state.

## Safe Operator Decision

Block downstream execution until planner state is present, deterministic, schema-valid, and bound to the current run ID, branch, and commit SHA. Reject empty output strings, malformed artifact names, and unapproved stale-cache fallback. Preserve the failed handoff evidence and regenerate the planner state manifest before rerunning the Builder Agent.

## Agentic Nuance

A broken workflow output in a multi-agent system is not merely a CI wiring bug; it is an unhandled exception in a distributed state machine. When an upstream Planner Agent fails to register its output name deterministically, it creates an execution vacuum.

Autonomous downstream agents can behave unpredictably when inputs resolve to null, empty strings, or stale artifact names. Instead of failing immediately, they may fall back to default prompts, use stale context from a previous run, retry the same missing download repeatedly, or infer a plausible plan that was never produced.

That creates silent data corruption inside the agentic delivery pipeline. The workflow may look successful while the Builder Agent actually processed no valid planner state.

The safe boundary is strong state serializability: handoffs must be deterministic, schema-validated, bound to the current run ID, branch, and commit SHA, and engineered to fail closed before any downstream agent is invoked.

## Portfolio Signal

This lab demonstrates advanced state-management thinking for multi-agent CI/CD environments. It shows the ability to trace loose data contracts across decoupled agent steps, detect silent handoff failures, prevent stale context ingestion, and design deterministic gates that preserve state continuity inside GitHub Actions.

A reviewer should come away understanding that the engineer can reason beyond "did the workflow pass?" and ask the more important question: "Did the downstream agent consume the correct validated state for this exact run?"
