# Lab 04: Analyze a Session Log

## Difficulty

Beginner.

## Estimated Time

10-15 minutes.

## Scenario

An agent resumed a previous session and made a repository change. The operator must decide whether the resumed context was still valid.

## Artifacts to Inspect

- `logs/copilot-cli-session-resumed.log`
- `logs/copilot-cli-session-new.log`
- `memory/repository-facts-example.json`
- `artifacts/planner-output.json`

## What You Are Looking For

Look for session state, branch or workspace context, referenced artifacts, validated memory facts, tool activity, and final status. The important distinction is whether a resumed session verified current repository reality before acting.

## Questions

1. Is the inspected session new or resumed?
2. Which previous artifact was found?
3. Which memory fact was validated?
4. Which file did the builder edit?
5. What could make the resumed session unsafe?

## Expected Reasoning Path

Start by identifying whether the log says the session is new or resumed. Then trace the artifacts and memory facts the agent used to justify continuing. A safe operator compares those references against current files and branch state before accepting the result.

## Answer Key

1. The log shows a resumed session.
2. It finds `artifacts/planner-output.json`.
3. It validates `repo_fact_001`.
4. It edits `mcp/broad-server-wildcard-risk.yml`.
5. The session becomes unsafe if the branch, plan artifact, or memory fact is stale or conflicts with current repository state.

## Common Wrong Answers

- Assuming resumed sessions are automatically safe because they preserve context.
- Reading only the final status and ignoring branch or artifact references.
- Trusting memory without checking its validation timestamp or source.
- Treating repeated work as harmless.

## Safe Operator Decision

Request clarification or regenerate artifacts if the resumed context is stale. Accept the session only after current branch state, plan artifact, and memory references are verified.

## Portfolio Signal

This lab demonstrates trace-based reasoning over agent sessions and shows that continuity is useful only when validated against current repository evidence.
