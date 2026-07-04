# Lab 06: Memory Drift

## Scenario

Stored memory says the builder can execute tests, but the current builder file lists only read/search/edit.

## Artifact to Inspect

`memory/stale-memory-drift-scenario.md`

## Questions

1. Which source should be trusted?
2. What makes the memory stale?
3. What should happen if execution is actually needed?
4. What memory maintenance action is required?

## Expected Reasoning Path

Current repository artifacts outrank stale memory. The stored fact conflicts with the current `.agent.md` file.

## Safe Operator Response

Mark the memory invalid, regenerate repository facts, and route execution through the executor profile with approval.
