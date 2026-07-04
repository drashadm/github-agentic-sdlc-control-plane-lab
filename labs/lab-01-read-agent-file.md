# Lab 01: Read a Custom Agent File

## Scenario

You are reviewing `.github/agents/executor.agent.md`.

## Artifact to Inspect

```yaml
name: executor
description: High-risk executor profile for controlled command execution after explicit approval.
tools: ["read", "edit", "execute"]
```

## Questions

1. Why is this agent higher risk than the reviewer?
2. Which tool creates the largest safety concern?
3. What approval should be required before use?
4. What artifact should prove the action was authorized?

## Expected Reasoning Path

- `execute` can run commands and change state indirectly.
- This role should be isolated from planning and review.
- Human approval should be explicit and tied to a specific command/action.
- Logs and action summaries should be preserved.

## Safe Operator Response

Allow executor use only for approved actions. Require command summary, approval reference, output location, and rollback notes.
