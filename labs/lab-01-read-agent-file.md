# Lab 01: Read a Custom Agent File

## Difficulty

Beginner.

## Estimated Time

10-15 minutes.

## Scenario

You are reviewing a custom executor profile before allowing it to run a controlled repository task. The file declares a high-risk role with command execution capability, so the operator must confirm that its boundaries and required outputs are clear.

## Artifacts to Inspect

- `.github/agents/executor.agent.md`
- `.github/agents/reviewer.agent.md`
- `docs/guardrails-and-accountability.md`

## What You Are Looking For

Look for the declared role, tool list, approval language, high-risk warnings, and output requirements. Compare the executor profile with a lower-risk reviewer profile to see how role-specific tool scope should change.

## Questions

1. Why is the executor profile higher risk than the reviewer profile?
2. Which tool creates the largest safety concern?
3. What approval should be required before executor use?
4. What evidence should the executor produce after an action?
5. What should happen if artifacts are missing or stale?

## Expected Reasoning Path

A safe operator starts with the front matter because tool access is a governance declaration. The `execute` tool changes the risk level because it can run commands and change repository or environment state. The body of the file should then be checked for explicit approval requirements, boundaries, and required output fields that preserve accountability.

## Answer Key

1. The executor is higher risk because it includes `execute`, while reviewer-style work should not need command execution.
2. `execute` is the largest safety concern.
3. Explicit human approval tied to a specific command or action should be required.
4. The executor should produce a command or action summary, approval reference, run context, output location, error status, and rollback notes.
5. The action should stop until the artifacts are refreshed or verified.

## Common Wrong Answers

- Treating the agent description as enough evidence that execution is safe.
- Assuming all custom agents need the same tools.
- Approving execution without a command-specific approval reference.
- Ignoring stale artifacts because the agent profile looks correct.

## Safe Operator Decision

Escalate for explicit human approval before use. Allow executor activity only for the approved action, then require an auditable action summary and rollback notes.

## Portfolio Signal

This lab demonstrates least-privilege review of agent profiles and the ability to connect tool scope, approval gates, and audit evidence in a GitHub-native control plane.
