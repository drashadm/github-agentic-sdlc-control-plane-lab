# Lab 02: Debug Workflow Output Handoff

## Difficulty

Intermediate.

## Estimated Time

15-20 minutes.

## Scenario

A builder job cannot find the planner artifact it expects. The workflow is meant to pass an artifact name from a planner job to a builder job through GitHub Actions outputs.

## Artifacts to Inspect

- `.github/workflows/multi-agent-artifact-handoff.yml`
- `artifacts/planner-output.json`
- `artifacts/builder-diff-summary.json`

## What You Are Looking For

Trace the producing job, step output, job output, `needs` dependency, upload artifact name, and download artifact name. The key question is whether the name written to `$GITHUB_OUTPUT` matches the name later used by `actions/download-artifact`.

## Questions

1. Which job produces `plan_artifact_name`?
2. Which job consumes `needs.planner.outputs.plan_artifact_name`?
3. Where is the planner artifact name written?
4. What breaks if the output key or artifact name changes?
5. What should the operator inspect first?

## Expected Reasoning Path

Start with the `planner` job and find its `outputs` block. Follow that output to the step with `id: plan`, then verify the line that writes to `$GITHUB_OUTPUT`. Next, inspect the `builder` job, confirm it declares `needs: planner`, and verify the download name uses the planner output. Finally, compare the uploaded artifact name with the downloaded artifact name.

## Answer Key

1. The `planner` job produces `plan_artifact_name`.
2. The `builder` job consumes it through `needs.planner.outputs.plan_artifact_name`.
3. The `Produce plan artifact marker` step writes `plan_artifact_name=planner-output` to `$GITHUB_OUTPUT`.
4. The downstream download can fail because the builder job asks for a name that was never produced or exposed.
5. Inspect the producing job logs and workflow YAML before changing downstream logic.

## Common Wrong Answers

- Debugging the builder code before checking the planner output.
- Assuming artifact file paths and artifact names are interchangeable.
- Removing `needs` instead of fixing the handoff.
- Treating a successful checkout as proof that the artifact exists.

## Safe Operator Decision

Block or rerun the workflow after verifying the output key and artifact upload/download names. Do not approve the downstream result until the handoff is traceable.

## Agentic Nuance

A missing workflow output is not just a CI wiring bug. In an agentic handoff, the downstream agent may guess what the planner meant, reuse stale context, or summarize an empty handoff as if it were complete. The control should block silent continuation, not merely make the workflow logs cleaner.

## Portfolio Signal

This lab shows the ability to debug GitHub Actions as an evidence pipeline, where outputs, dependencies, and artifacts form reviewable agent handoffs.
