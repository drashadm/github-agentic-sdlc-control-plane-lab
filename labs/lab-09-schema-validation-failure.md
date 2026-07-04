# Lab 09: Schema Validation Failure

## Difficulty

Intermediate.

## Estimated Time

15-20 minutes.

## Scenario

A planner artifact is missing required success criteria, or a consolidated operator report omits unresolved security findings. The operator must decide whether schema validation is enough to proceed.

## Artifacts to Inspect

- `artifacts/planner-output.json`
- `artifacts/consolidated-operator-report.json`
- `schemas/planner-output.schema.json`
- `schemas/consolidated-operator-report.schema.json`
- `docs/artifact-schema-map.md`

## What You Are Looking For

Check required fields, artifact purpose, and the difference between artifact shape and artifact truth. A schema can prove that required fields exist, but it cannot prove that the agent made a correct decision or preserved every important risk.

## Questions

1. Which planner field proves the artifact lists reviewable outcomes?
2. Which consolidated report field should preserve remaining risk?
3. What does schema validation prove?
4. What does schema validation not prove?
5. What should happen when a required field is missing?

## Expected Reasoning Path

Start with the schema required fields and compare them to the artifact. If a required field is missing, the handoff is incomplete and downstream review should stop. If the artifact passes schema validation, continue reviewing content quality, source alignment, and whether unresolved risks were accurately carried forward.

## Answer Key

1. `success_criteria`.
2. `unresolved_risks`.
3. It proves the artifact has the minimum expected shape and required fields.
4. It does not prove the agent was correct, truthful, complete in substance, or aligned with source evidence.
5. Block the review path, regenerate the artifact, and validate again before downstream use.

## Common Wrong Answers

- Treating schema success as approval to ship.
- Ignoring missing fields because the prose looks clear.
- Assuming a valid final report cannot omit important findings.
- Fixing the schema to fit a bad artifact instead of regenerating the artifact.

## Safe Operator Decision

Block downstream review on schema failure. If validation passes, continue evidence review because schema validation proves artifact shape, not truth.

## Portfolio Signal

This lab demonstrates schema-aware governance: using contracts to catch incomplete handoffs while preserving human review for correctness and risk judgment.
