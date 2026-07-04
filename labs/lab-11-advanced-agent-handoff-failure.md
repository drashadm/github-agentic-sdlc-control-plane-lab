# Lab 11: Advanced Agent Handoff Failure

## Difficulty

Advanced.

## Estimated Time

20 minutes.

## Scenario

A Planner Agent produces valid JSON, but it no longer matches the expected handoff schema. The Builder Agent accepts the file, processes zero files, and reports success. The Consolidator later produces a final report that looks complete but is missing the real implementation context.

## Artifacts to Inspect

* `artifacts/agent-handoff-valid-v2.json`
* `artifacts/planner-context-raw-malformed.json`
* `schemas/agent-handoff-v2.schema.json`
* `docs/advanced-agentic-failure-modes.md`
* `docs/context-window-gating.md`
* `docs/cost-and-retry-control.md`

## What You Are Looking For

Look for schema drift, silent success, `processed_files_count: 0`, missing `validation_status`, `output_files` vs `target_files` mismatch, oversized or unsafe context risk, and downstream hallucination risk.

## Questions

1. Why is valid JSON not enough?
2. Which fields show schema drift?
3. Why is `processed_files_count: 0` dangerous if the workflow still reports success?
4. What should happen before the Builder Agent is invoked?
5. How should the workflow protect the downstream agent's context window?
6. What controls reduce retry/cost loops?
7. What evidence would prove the artifact came from the expected upstream job?

## Expected Reasoning Path

The artifact must be validated against the expected schema before downstream invocation. A parseable file is not the same as a valid handoff. If schema validation fails or required fields are missing, the safe response is to block, regenerate, or escalate. The operator should also check provenance fields, context budget, and whether the downstream agent had enough verified input to act.

## Answer Key

1. Valid JSON only proves the file parses. It does not prove the file matches the expected handoff schema or contains useful context.
2. `target_files` replaces expected `output_files`, and `code_changes` replaces expected `handoff_summary`.
3. It means the downstream agent may have completed without processing any meaningful implementation input.
4. The handoff should be validated against `schemas/agent-handoff-v2.schema.json`; failures should block invocation.
5. Enforce max artifact size, require summaries with source links, reject oversized raw logs, preserve unresolved risks, and chunk only with traceable references.
6. Max retry count, backoff, explicit failure state, cost/rate-limit annotations, and a stop condition.
7. Provenance evidence such as source job, run ID, commit SHA, source branch, timestamp, checksum or attestation, and reviewer approval.

## Common Wrong Answers

* "The JSON parsed, so it is safe."
* "The downstream agent can infer missing fields."
* "CI passed, so the report is trustworthy."
* "The final report is enough evidence."

## Safe Operator Decision

Block downstream execution. Mark the artifact invalid. Regenerate the planner handoff using the required schema. Preserve the malformed artifact as evidence. Do not let the Builder or Consolidator guess missing context.

## Portfolio Signal

This lab demonstrates production-grade thinking about agentic handoffs, schema drift, context-window governance, and silent failure prevention.
