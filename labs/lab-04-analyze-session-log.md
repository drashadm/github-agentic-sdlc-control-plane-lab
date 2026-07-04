# Lab 04: Analyze a Session Log

## Scenario

An agent resumed a previous session and made changes.

## Artifact to Inspect

`logs/copilot-cli-session-resumed.log`

## Questions

1. Is the session new or resumed?
2. Which previous artifact was found?
3. Which memory fact was validated?
4. What file did the builder edit?

## Expected Reasoning Path

The log shows `state=resumed`, finds `artifacts/planner-output.json`, validates `repo_fact_001`, and edits `mcp/broad-server-wildcard-risk.yml`.

## Safe Operator Response

Confirm the resumed context matches the current branch and that the plan artifact is still valid.
