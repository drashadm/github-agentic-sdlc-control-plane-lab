# Cost and Retry Control

Agent retry loops happen when a workflow repeatedly retries a failed artifact download, tool call, schema validation, or generation step without a clear stop condition. In normal automation this may create noisy logs. In agentic workflows it can also burn API/tool credits, trigger rate limits, and hide the original failure behind repeated attempts.

Retries need explicit stop conditions. A downstream agent should not keep guessing after missing context, and a regeneration loop should not continue when the schema mismatch is deterministic.

Cost controls are part of governance because agentic workflows can spend money while producing misleading confidence. A safe control plane records retries, failure state, rate-limit signals, and when a human operator must intervene.

| Failure Pattern | Agentic Risk | Control |
| --------------- | ------------ | ------- |
| repeated artifact download failure | Agent keeps retrying or uses stale fallback context | Limit retries, require explicit missing-artifact failure, and block downstream agents |
| repeated schema validation failure | Agent regenerates similar invalid artifacts without fixing the contract | Stop after a small retry count and route to schema review |
| repeated MCP tool timeout | Agent burns tool calls while obscuring service or permission failure | Use backoff, timeout budgets, and operator-visible failure state |
| repeated LLM regeneration loop | Agent spends tokens producing variations that do not satisfy the handoff | Add validation gates, cost annotations, and a stop condition |
| downstream agent keeps guessing after missing context | Final report sounds complete despite incomplete evidence | Fail closed when required context is absent |

## Retry Loops Caused by Broken State Handoffs

Missing artifacts or empty workflow outputs can trigger repeated download attempts, LLM regeneration loops, or repeated tool calls. These loops can burn credits while making the original state handoff failure harder to see.

State handoff retries should have:

* max retry count
* backoff
* explicit failed state
* cost/rate-limit annotation
* no fallback to stale context unless explicitly approved and labeled

## Denial of Wallet and Silent Retry Loops

Silent schema drift can cause repeated LLM attempts. Each retry may include more context, logs, artifacts, and prior failures, so cost growth can compound while semantic progress remains zero.

Retries must have explicit stop conditions. Budget breaches should block downstream automation, and zero semantic progress should stop the agent chain rather than triggering another larger retry.

This lab uses generic educational token and cost values only. It does not implement vendor billing enforcement, live token metering, or billing kill-switches.
