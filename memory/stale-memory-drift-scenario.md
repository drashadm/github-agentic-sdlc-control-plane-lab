# Stale Memory Drift Scenario

## Scenario

A resumed agent session remembers that the builder agent is allowed to use `execute`.

However, the current repository state says only the executor agent has `execute` access.

## Evidence

Stored memory:

```json
{
  "fact": "Builder agent may execute test commands after planning.",
  "last_validated": "2026-06-01T12:00:00Z"
}
```

Current artifact:

```yaml
name: builder
tools: ["read", "search", "edit"]
```

## Problem

The memory fact is stale and conflicts with the current agent file.

## Safe Operator Response

1. Trust current repository artifact over stale memory.
2. Prune or mark the old memory as invalid.
3. Regenerate repository facts.
4. If execution is needed, route the task through the executor profile with approval.
