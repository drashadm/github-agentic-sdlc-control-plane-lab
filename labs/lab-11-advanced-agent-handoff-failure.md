# Lab 11: Advanced Agent Handoff Failure

## Difficulty

Advanced.

## Estimated Time

30-40 minutes.

## Scenario

A Planner Agent produces parseable JSON, but it no longer matches the expected handoff schema. The Builder Agent accepts the file, processes zero files, retries with growing context, and reports success. The Consolidator later produces a polished final report that hides the broken state chain.

This is not one bug. It is a compound failure across schema drift, semantic voids, unexpected fields, stale memory, artifact provenance, tool authority, hook enforcement, retry budgets, context-window growth, consolidator fidelity, and final human approval.

A mature agentic SDLC control plane does not ask only, "Which artifact failed?" It asks, "Which chain of trust broke, and did the system fail closed before authority crossed the boundary?"

## Artifacts to Inspect

* `artifacts/agent-handoff-valid-v2.json`
* `artifacts/planner-context-raw-malformed.json`
* `artifacts/billing-and-token-telemetry.json`
* `artifacts/zombie-pipeline-failure-report.json`
* `artifacts/compound-handoff-failure-report.json`
* `schemas/agent-handoff-v2.schema.json`
* `schemas/billing-and-token-telemetry.schema.json`
* `schemas/zombie-pipeline-failure-report.schema.json`
* `schemas/compound-handoff-failure-report.schema.json`
* `docs/advanced-agentic-failure-modes.md`
* `docs/context-window-gating.md`
* `docs/cost-and-retry-control.md`
* `docs/schema-semantic-validation-governance.md`
* `docs/artifact-transaction-governance.md`
* `docs/memory-governance.md`
* `docs/multi-agent-coordination-governance.md`
* `docs/guardrails-and-accountability.md`
* `docs/zombie-pipeline-governance.md`

## What You Are Looking For

Look for the full chain of trust, not only the first invalid field.

Focus on:

* silent cascading failure
* Zombie Pipeline behavior
* runner success versus agentic state collapse
* `processed_items_actual: 0` or `processed_files_count: 0` when work was expected
* schema drift with structural pass
* schema-valid but semantically void data
* unexpected-field context injection risk
* unknown properties not rejected
* stale memory entering context
* artifact provenance mismatch
* consolidator flattening total failure into success
* token/cost retry loop
* context-window bloat
* human approval based on incomplete evidence
* compound chain-of-trust break

## Questions

1. Why can a traditional CI/CD monitor that checks only exit codes miss a Zombie Pipeline failure?
2. Why is `processed_items_actual: 0` a blocking signal when work was expected?
3. How can an artifact pass schema validation while still representing semantic collapse?
4. What is unexpected-field context injection, and why should unknown schema keys be rejected instead of passed into downstream prompts?
5. Why can silent schema drift cause compounding token and cost growth?
6. What evidence should prove that retry loops stayed within budget and stopped on zero semantic progress?
7. What provenance fields should be checked before a downstream agent trusts an upstream handoff?
8. How can a final consolidator turn a total state-chain collapse into a polished success report?
9. What deterministic assert should block the pipeline if a downstream agent processes zero files or zero records?
10. What should the operator do when schema validation passes, semantic validation fails, token budget is exceeded, and artifact provenance is incomplete?

## Expected Reasoning Path

Start with the handoff pair. `artifacts/agent-handoff-valid-v2.json` shows the expected contract, while `artifacts/planner-context-raw-malformed.json` is parseable JSON with drifted fields such as `target_files` and `code_changes`. A downstream agent must not treat unknown fields as prompt-ready context or infer missing fields.

Then inspect the Zombie Pipeline evidence. `artifacts/zombie-pipeline-failure-report.json` shows visible pipeline success while agentic state has collapsed and processed items are zero. `artifacts/billing-and-token-telemetry.json` shows repeated attempts, context growth, and budget status moving to blocked. `artifacts/compound-handoff-failure-report.json` ties the layers together.

Finally reason across controls. The safe review checks schema, semantic assertions, processed-item counts, provenance, memory freshness, MCP/tool authority, hook enforcement, retry budgets, context-window caps, consolidator fidelity, and human approval evidence. If any required layer cannot prove continuity, authority transfer must fail closed.

## Answer Key

1. Exit code success is not agentic success. It can miss zero-work processing, semantic voids, stale memory, wrong provenance, and lossy final consolidation.
2. Zero-work success is a failure when work was expected. The pipeline should assert `processed_items_actual > 0` or an explicitly approved no-op reason before proceeding.
3. Schema validation checks shape. Semantic collapse can still occur when required fields contain placeholders, generic success, stale claims, or no meaningful processed records.
4. Unexpected-field context injection happens when unknown upstream JSON keys are passed directly into a downstream prompt. Unknown fields should be rejected or quarantined, not injected into prompts.
5. Silent schema drift can cause repeated regeneration, larger context windows, and more prior-failure material in each attempt without making semantic progress.
6. Evidence should include retry attempts, token usage, fake estimated cost, context-window growth, stop conditions, budget status, anomaly detection, and safe next action.
7. Provenance must bind artifacts to run ID, branch, commit SHA, workflow, producing job, producing agent, schema version, digest/checksum, and upload timestamp.
8. A consolidator can summarize file existence, parse success, or agent messages into a clean report while omitting that zero items were processed and semantic validation failed.
9. A deterministic assertion should block when expected processed items are nonzero and actual processed items are zero, unless a reviewed exception is present.
10. Block, preserve evidence, reset or regenerate from known-good state, quarantine malformed artifacts, and require human escalation before authority moves to the next agent or approval gate.

## Common Wrong Answers

* "The JSON parsed, so it is safe."
* "The downstream agent can infer missing fields."
* "CI passed, so the report is trustworthy."
* "The final report is enough evidence."
* "Zero processed files is harmless if the final status is green."
* "Unknown fields can be included as extra helpful context."
* "Retrying with more context will eventually fix schema drift."
* "Human approval is valid because the report is well formatted."
* "One failed layer can be ignored because other gates passed."

## Safe Operator Decision

Block downstream execution and final approval. Preserve the malformed handoff, Zombie Pipeline report, billing/token telemetry, and compound failure report as evidence. Quarantine unexpected fields and stale memory, reset or regenerate from known-good state, enforce retry and context limits, and require human escalation before authority crosses to the next agent or approval gate.

## Agentic Nuance

Lab 11 exposes the capstone failure mode of multi-agent engineering: the Zombie Pipeline. A Zombie Pipeline is a workflow that continues executing and reporting success after the agentic state chain has already collapsed.

LLM-driven agents often try to resolve ambiguity instead of crashing. When an upstream schema drifts, a downstream agent may ingest the payload, find zero matching items, process nothing, and still return a success message. The final consolidator can then render a polished operator report that hides total functional failure behind clean structure.

This failure is dangerous because it combines several risks at once: schema-valid but semantically void artifacts, stale memory, unexpected-field context injection, wrong or partial artifact provenance, unbounded retries, context-window bloat, and final-report overconfidence.

The safe control is a chain-of-trust review. Each boundary must fail closed: schema validation, semantic assertions, processed-item counts, provenance checks, memory freshness, MCP/tool authority, hook enforcement, retry budget, and consolidator fidelity. If any required layer cannot prove continuity, the system should block authority transfer and escalate to a human operator.

## Portfolio Signal

This capstone lab demonstrates production-grade thinking about compound failure in distributed AI engineering systems. It shows the ability to detect silent cascading failures, enforce semantic progress checks, control retry/token budgets, validate artifact provenance, reject unexpected context, and prevent polished final reports from masking a broken agentic state chain.

A reviewer should come away understanding that the engineer can reason beyond "which step passed?" and ask the more important question: "Did the entire chain of trust remain valid before authority moved to the next agent or human approval gate?"
