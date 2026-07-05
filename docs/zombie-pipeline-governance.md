# Zombie Pipeline Governance

## What Is a Zombie Pipeline?

A Zombie Pipeline is a workflow that continues executing and reporting success after the agentic state chain has already collapsed.

It can look healthy because:

- runner exit codes are zero
- JSON parses
- schema validation passes
- downstream agents process empty data
- final reports render successfully
- dashboards show green status

## Why Agents Continue Instead of Crashing

LLM-driven agents often try to be helpful under ambiguity. When schema drift, missing fields, or malformed context appears, they may:

- process zero items
- fill missing fields with generic content
- retry with larger context
- invent a plausible bridge
- pass a success message upward
- allow consolidators to flatten risk

## Unexpected-Field Context Injection

Schema drift can create an injection surface when unexpected keys are not rejected. A downstream agent must not treat unknown fields from upstream JSON as raw prompt context.

Safe controls include:

- reject unknown fields
- use `additionalProperties: false` where appropriate
- maintain allowlisted keys
- validate against versioned schemas
- quarantine malformed or unexpected fields
- never inject unknown fields directly into agent prompts

## Semantic Void Detection

`processed_files_count: 0` or `processed_items_actual: 0` should not be treated as harmless success when work was expected. Zero-work success is a control-plane signal.

## Cost and Retry Budget Controls

Silent failures can trigger repeated LLM calls, bigger context windows, and compounding token spend. Safe controls include:

- max retries
- max token budget
- max cost budget
- context-window cap
- backoff
- explicit stop conditions
- fail-closed state when semantic progress is zero

This repository uses fake educational token and cost values only. Billing kill-switches and live token metering may be useful as optional production controls, but they are not implemented here.

## Provenance and Handoff Integrity

Artifacts should be bound to:

- run ID
- branch
- commit SHA
- workflow
- producing job
- producing agent
- digest/checksum
- upload timestamp
- schema version

The hashes in this repository are fake educational values. Signed attestations are optional higher-assurance production controls, not implemented features.

## Capstone Chain-of-Trust Review

Advanced handoff review asks:

- Did the schema match?
- Did semantics match?
- Did the artifact come from the expected source?
- Did memory agree with current repository state?
- Did tool authority remain bounded?
- Did hooks enforce before execution?
- Did retries stay within budget?
- Did the final consolidator preserve risk?
- Was human approval based on complete evidence?

## Safe Operator Checklist

- Did any agent process zero items when work was expected?
- Did schema validation pass but semantic validation fail?
- Were unexpected keys rejected?
- Were retry and token budgets enforced?
- Was artifact provenance valid?
- Did the final report preserve all blocking findings?
- Was human approval based on complete evidence?
- Did the system fail closed before authority crossed the boundary?
