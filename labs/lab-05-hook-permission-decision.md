# Lab 05: Hook Permission Decision

## Difficulty

Beginner.

## Estimated Time

10-15 minutes.

## Scenario

A pre-tool hook receives a request for a destructive execute action against repository artifacts. The hook must decide whether to allow, deny, or require approval.

## Artifacts to Inspect

- `.github/hooks/preToolUse-deny-execute.example.json`
- `.github/hooks/permissionRequest-cli-only.example.json`
- `docs/guardrails-and-accountability.md`

## What You Are Looking For

Inspect the event type, requested tool, command summary, policy rule, matched status, decision, and reason. Focus on whether the hook fails closed when approval is missing.

## Questions

1. Which hook event is represented?
2. Which tool was requested?
3. What permission decision did the hook make?
4. Why is fail-closed appropriate here?
5. What evidence should be preserved?

## Expected Reasoning Path

A safe operator starts with `event` and `toolName`, then checks the policy block and final `permissionDecision`. If the action is destructive and approval is absent, fail-closed behavior should deny the request and preserve the hook event for audit.

## Answer Key

1. The event is `preToolUse`.
2. The requested tool is `execute`.
3. The decision is `deny`.
4. Fail-closed is appropriate because the action is destructive and lacks explicit human approval.
5. Preserve the hook event, policy match, requested tool, reason, and session context.

## Common Wrong Answers

- Treating a hook warning as equivalent to an enforced deny.
- Allowing the action because the path is only an example artifact path.
- Ignoring the `matched` policy field.
- Escalating without a specific command/action approval.

## Safe Operator Decision

Block the action, preserve the hook evidence, and require explicit human approval before any destructive operation is reconsidered.

## Agentic Nuance

Hooks are control points only if they are enforced and audited. If a hook warning is treated as advisory, or if deny/ask behavior differs by runtime, an agent can continue through a fail-open path. The hook decision itself is an artifact that must be preserved as evidence.

## Portfolio Signal

This lab demonstrates how to read hook artifacts as enforcement records and how to explain fail-closed behavior in agentic SDLC governance.
