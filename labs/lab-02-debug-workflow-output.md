# Lab 02: Debug Workflow Output Handoff

## Scenario

A downstream job cannot find the planner artifact name.

## Artifact to Inspect

`.github/workflows/multi-agent-artifact-handoff.yml`

Look for:

- `outputs`
- `$GITHUB_OUTPUT`
- `needs.planner.outputs.plan_artifact_name`
- `actions/upload-artifact`
- `actions/download-artifact`

## Questions

1. Which job produces the output?
2. Which job consumes the output?
3. What happens if the output key name changes?
4. What should the safe operator inspect first?

## Expected Reasoning Path

The planner job writes `plan_artifact_name` to `$GITHUB_OUTPUT`. The builder job consumes it through `needs.planner.outputs.plan_artifact_name`.

## Safe Operator Response

Inspect producing job logs first, verify output key, then verify artifact upload name matches download name.
