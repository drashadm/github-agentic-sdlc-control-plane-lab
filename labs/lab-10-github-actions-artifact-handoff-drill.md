# Lab 10: GitHub Actions Artifact Handoff Drill

## Difficulty

Intermediate.

## Estimated Time

15-20 minutes.

## Scenario

A downstream job expects an artifact or output that was not produced under the expected name. The operator must trace the GitHub Actions handoff and decide where the chain broke.

## Artifacts to Inspect

- `.github/workflows/multi-agent-artifact-handoff.yml`
- `.github/workflows/consolidated-operator-report.yml`
- `artifacts/planner-output.json`
- `artifacts/builder-diff-summary.json`

## What You Are Looking For

Trace `needs`, job outputs, `$GITHUB_OUTPUT`, artifact upload/download naming, and downstream gating. The safe operator should verify both the logical dependency chain and the exact strings used for artifact names.

## Questions

1. Which workflow keyword makes the builder wait for planner output?
2. Where does the planner write the artifact name?
3. Which action uploads the planner artifact?
4. Which action downloads the planner artifact?
5. How does the consolidated report workflow gate publication?
6. What is the safest first fix when names do not match?

## Expected Reasoning Path

Start with `needs` to identify dependency order. Follow the job output back to the step that writes to `$GITHUB_OUTPUT`. Compare the uploaded artifact name with the downloaded artifact name. Then inspect the consolidated report workflow to confirm downstream publishing depends on complete evidence.

## Answer Key

1. `needs: planner`.
2. The planner step with `id: plan` writes `plan_artifact_name=planner-output` to `$GITHUB_OUTPUT`.
3. `actions/upload-artifact@v4`.
4. `actions/download-artifact@v4`.
5. `publish-report` runs only when `needs.collect-evidence.outputs.evidence_status == 'complete'`.
6. Fix the producing output and upload name so the downstream download references the produced artifact exactly, then rerun the workflow.

## Common Wrong Answers

- Changing the downstream job without checking the producer.
- Confusing artifact file paths with uploaded artifact names.
- Removing gating to make the workflow pass.
- Assuming `needs` transfers artifacts automatically.

## Safe Operator Decision

Rerun the workflow only after matching job outputs and artifact names. Keep downstream gating in place and block publication when required evidence is missing.

## Agentic Nuance

Workflow success is not the same as agentic success. A job can pass while the downstream agent uses the wrong artifact, an old artifact, or an artifact that caused zero files to be processed. The gate should verify meaningful handoff content, not only job completion.

## Portfolio Signal

This lab demonstrates operational GitHub Actions literacy for agentic systems: tracing evidence handoffs across jobs without weakening governance controls.
