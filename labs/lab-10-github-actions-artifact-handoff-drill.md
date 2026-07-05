# Lab 10: GitHub Actions Artifact Handoff Drill

## Difficulty

Intermediate.

## Estimated Time

25-30 minutes.

## Scenario

A downstream Builder job starts after the Planner job reports success. The GitHub Actions check is green, the uploaded artifact name exists, and `needs: planner` was satisfied. A shallow review would conclude that the handoff worked.

The deeper problem is that workflow success is not agentic success. A green GitHub Actions check only proves the runner completed its configured steps. It does not prove that the upstream agent runtime completed, all background work was awaited, files were fully written, or the downstream agent consumed the correct artifact.

A green GitHub Actions check only proves the workflow completed. It does not prove that the downstream agent consumed the correct, complete, current, non-empty, schema-valid, semantically valid artifact from the correct run, branch, commit SHA, and producing job.

## Artifacts to Inspect

- `.github/workflows/multi-agent-artifact-handoff.yml`
- `.github/workflows/consolidated-operator-report.yml`
- `artifacts/planner-output.json`
- `artifacts/builder-diff-summary.json`
- `artifacts/pipeline-execution-checkpoint.json`
- `artifacts/artifact-transaction-report.json`
- `artifacts/artifact-provenance-manifest.json`
- `schemas/pipeline-execution-checkpoint.schema.json`
- `schemas/artifact-transaction-report.schema.json`
- `schemas/artifact-provenance-manifest.schema.json`
- `docs/artifact-transaction-governance.md`
- `docs/workflow-validation-guide.md`
- `docs/state-serializability.md`
- `docs/schema-semantic-validation-governance.md`
- `docs/advanced-agentic-failure-modes.md`
- `docs/guardrails-and-accountability.md`

## What You Are Looking For

Trace `needs`, job outputs, `$GITHUB_OUTPUT`, artifact upload/download naming, downstream gating, runtime checkpoints, transaction readiness, and provenance binding. The safe operator should verify both the logical dependency chain and the actual artifact consumed by the downstream agent.

Look for:

- workflow success versus agentic success
- runner exit code versus internal agent runtime status
- asynchronous completion mismatch
- background task leakage
- partial artifact truncation
- artifact upload racing file generation
- file existence versus file completeness
- parseable but incomplete artifacts
- schema-valid but semantically incomplete artifacts
- artifact name collision
- stale artifact download
- run ID, branch, and commit SHA binding
- matrix job or multi-job artifact confusion
- `needs` ordering versus artifact integrity
- downstream processing zero or fewer-than-expected records
- provenance manifest validation
- fail-closed downstream gates

## Questions

1. Why does a green GitHub Actions check not prove that an agent handoff artifact is complete?
2. How can a runner step exit successfully while an internal agent runtime still failed to produce a valid output?
3. What is the risk if artifact upload starts while the producing process is still writing the file?
4. Why is file existence insufficient as an artifact validation check?
5. What is the difference between a parseable artifact and a complete artifact?
6. Why is `needs` necessary but insufficient for multi-agent artifact governance?
7. What evidence proves that a downstream job consumed the correct artifact from the correct run, branch, commit SHA, workflow, and producing job?
8. What should happen if the downstream Builder Agent processes zero records or fewer records than expected?
9. How can artifact name collisions or retention behavior cause a downstream job to use stale state?
10. What should the upload gate verify before allowing downstream jobs to boot?

## Expected Reasoning Path

Start with `needs` to identify dependency order. Follow the job output back to the step that writes to `$GITHUB_OUTPUT`. Compare the uploaded artifact name with the downloaded artifact name. Then stop before concluding that the handoff is valid.

Next inspect `artifacts/pipeline-execution-checkpoint.json`. This artifact separates runner step status from internal agent runtime status. A runner step can be `success` while the agent runtime is `incomplete`, background tasks remain unfinished, and `upload_ready` is false.

Then inspect `artifacts/artifact-transaction-report.json`. Verify file existence, size, parse status, schema status, semantic status, expected versus actual record count, fake digest, atomic write status, upload gate status, and downstream gate status. File existence is only the weakest signal.

Finally inspect `artifacts/artifact-provenance-manifest.json`. The consumed artifact must be bound to run ID, run attempt, branch, commit SHA, workflow, producing job, producing agent, artifact name, fake digest, upload timestamp, and consuming job. If any of those do not match, the downstream agent should not boot from that artifact.

## Answer Key

1. Runner success means the configured step completed. It does not prove all internal agent state was valid, complete, flushed, or current.
2. Async calls, background tasks, or partial state writers can finish after the process reports success or fail without being reflected in the step exit code.
3. The downstream job can receive an empty, truncated, partial, or semantically incomplete file and treat it as operational truth.
4. File existence does not prove size, parseability, schema validity, semantic completeness, expected record count, provenance, or freshness.
5. A parseable artifact is syntactically readable. A complete artifact contains all expected records, passes schema and semantic checks, and is bound to the correct run and producer.
6. `needs` controls job ordering. It does not validate artifact correctness, completeness, provenance, or semantic readiness.
7. Evidence includes run ID, run attempt, branch, commit SHA, workflow name, producing job, consuming job, producing agent, artifact name, fake digest, upload timestamp, and validation status.
8. Treat zero or fewer-than-expected records as silent failure. Block final reporting, preserve evidence, and regenerate the artifact.
9. Reused artifact names, retention windows, fallback downloads, or matrix outputs can make a downstream job consume previous-run state that looks current by name alone.
10. The upload gate should verify runtime completion, background task completion, expected outputs, file size, record count, parse/schema/semantic validation, fake digest capture, and provenance manifest generation.

## Common Wrong Answers

- Changing the downstream job without checking the producer.
- Confusing artifact file paths with uploaded artifact names.
- Removing gating to make the workflow pass.
- Assuming `needs` transfers artifacts automatically.
- Assuming a green check means the agent runtime completed correctly.
- Treating file existence as proof of artifact integrity.
- Letting a downstream agent continue after processing zero records.
- Trusting artifact name alone without run, branch, commit, job, and digest evidence.
- Ignoring semantic validation because parse and schema checks passed.

## Safe Operator Decision

Block downstream consumption until the producing agent runtime is complete, background tasks are resolved, expected files are fully written, transaction checks pass, provenance is bound to the current run/branch/commit/job, and the downstream gate revalidates the artifact before invoking the next agent.

## Agentic Nuance

A foundational friction point in Agentic SDLC is the mismatch between cloud-native runner state and agent runtime state. GitHub Actions sees jobs, steps, exit codes, and uploaded artifacts. An agent framework may contain internal planning loops, asynchronous calls, background tasks, partial state files, and dynamic execution branches that do not map cleanly to those runner steps.

That means a workflow can be green while the agentic state machine is broken. The runner may mark the Planner job successful because the process exited cleanly, while the planner artifact is empty, partial, stale, or missing required semantic content. The downstream Builder job may boot because `needs` was satisfied, not because the artifact is trustworthy.

This creates transaction risk. A partially written artifact can become operational truth if upload occurs before the file is complete, or if the downstream job only checks file existence. In multi-agent systems, that corrupted handoff can shape the next agent's plan, review, and final operator report.

The safe control is artifact transaction governance: explicit runtime checkpoints, file completeness checks, parse/schema/semantic validation, provenance manifests, content digests, and fail-closed downstream gates before any agent consumes the handoff.

## Portfolio Signal

This lab demonstrates production-grade thinking about CI/CD artifact integrity for agentic workflows. It shows the ability to reason beyond green workflow status and inspect whether agent state, artifact completeness, provenance, and downstream consumption are actually valid.

A reviewer should come away understanding that the engineer can ask the production-grade question: "Did the downstream agent consume the correct, complete, current, validated artifact from the correct producing job and run?"
