# Lab 07: Multi-Agent Handoff

## Difficulty

Advanced.

## Estimated Time

15-20 minutes.

## Scenario

A planner, builder, reviewer, and security auditor all produce artifacts. A consolidator prepares the final operator report, and the operator must decide whether the report preserved the important findings.

## Artifacts to Inspect

- `artifacts/planner-output.json`
- `artifacts/builder-diff-summary.json`
- `artifacts/reviewer-findings.json`
- `artifacts/security-audit-report.json`
- `artifacts/consolidated-operator-report.json`
- `.github/workflows/consolidated-operator-report.yml`

## What You Are Looking For

Check whether every required upstream artifact is present, whether the consolidated report lists consumed artifacts, whether unresolved risks are preserved, and whether workflow gating prevents publication when evidence is missing.

## Questions

1. Which artifacts did the consolidator consume?
2. Did the final report preserve unresolved risks?
3. Did the reviewer approve fully or with conditions?
4. Which workflow job checks required artifacts?
5. What would make the final report unsafe?

## Expected Reasoning Path

Start with the consolidated operator report and compare `artifacts_consumed` against the expected planner, builder, reviewer, and security artifacts. Then inspect reviewer and security outputs to confirm the final report did not hide unresolved findings. Finally, check workflow gating to see whether missing evidence blocks publication.

## Answer Key

1. It consumed `planner-output.json`, `builder-diff-summary.json`, `reviewer-findings.json`, and `security-audit-report.json`.
2. Yes. It preserves the risk that examples should not be mistaken for production-safe configuration.
3. The reviewer recommends `approve_after_security_review`, so approval is conditional.
4. The `collect-evidence` job checks required artifacts.
5. The report is unsafe if it omits required artifacts, hides reviewer/security findings, uses stale inputs, or publishes despite missing evidence.

## Common Wrong Answers

- Treating the final report as authoritative without comparing upstream artifacts.
- Ignoring conditional approval language.
- Assuming a report is safe because it has a `decision` field.
- Forgetting that missing evidence should block downstream publication.

## Safe Operator Decision

Block final approval if any required artifact is missing, stale, contradicted, or omitted from the consolidated report. Regenerate the report from current artifacts.

## Agentic Nuance

More agents create more handoff contracts and more chances for contradiction. A consolidator can accidentally hide disagreement, drop security findings, or turn conditional approval into a clean-looking final decision. The final report is evidence only if it preserves upstream conflict.

## Portfolio Signal

This lab demonstrates cross-artifact review, a core skill for governing multi-agent delivery systems where no single artifact should be trusted in isolation.
