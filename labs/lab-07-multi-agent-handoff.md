# Lab 07: Multi-Agent Handoff

## Scenario

A planner, builder, reviewer, and security auditor all produce artifacts. A consolidator prepares the final report.

## Artifacts to Inspect

- `artifacts/planner-output.json`
- `artifacts/builder-diff-summary.json`
- `artifacts/reviewer-findings.json`
- `artifacts/security-audit-report.json`
- `artifacts/consolidated-operator-report.json`

## Questions

1. Which artifacts did the consolidator consume?
2. Did the final report preserve unresolved risks?
3. Did the reviewer approve fully or with conditions?
4. What would make the final report unsafe?

## Expected Reasoning Path

The final report must not hide unresolved security or reviewer findings.

## Safe Operator Response

Block final approval if any required artifact is missing, stale, or contradicted by another artifact.
