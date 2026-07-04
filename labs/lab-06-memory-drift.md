# Lab 06: Memory Drift

## Difficulty

Intermediate.

## Estimated Time

10-15 minutes.

## Scenario

Stored memory says the builder can execute tests, but the current repository agent profile shows the builder has only read, search, and edit tools. The operator must decide which source to trust.

## Artifacts to Inspect

- `memory/stale-memory-drift-scenario.md`
- `memory/repository-facts-example.json`
- `.github/agents/builder.agent.md`
- `.github/agents/executor.agent.md`

## What You Are Looking For

Look for stale validation timestamps, conflicts between memory and current files, and the correct route for execution tasks. Memory is useful context, but current repository artifacts are the stronger source of truth.

## Questions

1. Which source should be trusted when memory conflicts with current repository files?
2. What makes the stored memory stale?
3. Which current profile has execute access?
4. What should happen if execution is actually needed?
5. What memory maintenance action is required?

## Expected Reasoning Path

Compare the remembered fact with the current agent profile. The current `.agent.md` file outranks stale memory because it is the active governance artifact in the repository. If execution is needed, the work should move through the executor profile and approval path rather than expanding the builder based on stale memory.

## Answer Key

1. Trust the current repository artifact.
2. The memory is stale because its stored fact conflicts with the current builder profile and has an old validation timestamp.
3. The executor profile has execute access.
4. Route execution through the executor profile with explicit approval.
5. Mark the stale memory invalid, prune it, or regenerate repository facts.

## Common Wrong Answers

- Trusting memory because it sounds operationally useful.
- Editing the builder profile to match stale memory.
- Running execution through the wrong agent role.
- Ignoring validation timestamps.

## Safe Operator Decision

Block execution through the builder, invalidate the stale memory, regenerate repository facts, and route approved execution through the executor profile.

## Portfolio Signal

This lab demonstrates durable-state governance: validating memory against source-controlled artifacts before allowing an agent to act.
