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
