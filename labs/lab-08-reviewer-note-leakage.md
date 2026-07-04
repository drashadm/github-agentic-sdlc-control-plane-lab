# Lab 08: Reviewer Note Leakage

## Difficulty

Beginner / Intermediate.

## Estimated Time

10-15 minutes.

## Scenario

A final documentation artifact contains an internal editorial note: "I would recommend mentioning this earlier in the intro." The sentence is not user-facing content. The learner must classify the failure and choose a safe operator response before publication.

## Artifacts to Inspect

- `docs/artifact-reading-guide.md`
- `docs/failure-analysis-playbook.md`
- `docs/risk-to-github-mitigation-map.md`

## What You Are Looking For

Look for signs that draft review notes, reviewer comments, or internal editing guidance leaked into final documentation. The operator should distinguish useful review feedback from publishable content.

## Questions

1. Why is the quoted sentence not appropriate for final documentation?
2. What kind of failure does this represent?
3. Which mitigation in the risk map helps prevent recurrence?
4. What evidence should be preserved?
5. What checklist item should be added?

## Expected Reasoning Path

A safe operator treats internal notes in published artifacts as a review hygiene and artifact cleanup failure. The issue may not be a security vulnerability, but it can reduce trust, expose process noise, and show that final-render review did not happen. The response should clean the artifact while preserving enough evidence to prevent recurrence.

## Answer Key

1. It is editorial guidance, not reader-facing documentation.
2. It is reviewer-note leakage or final artifact cleanup failure.
3. The risk map recommends final-render review and artifact cleanup checks before publish or merge.
4. Preserve the affected artifact version, review comment context, and cleanup decision.
5. Add a checklist item to scan final docs and PR output for internal notes before publication.

## Common Wrong Answers

- Publishing anyway because the note is harmless.
- Deleting evidence of the issue without recording the cleanup.
- Treating all reviewer notes as security incidents.
- Fixing only the sentence without adding a recurrence check.

## Safe Operator Decision

Block publish or merge, remove editorial notes, run final-render review, preserve evidence of the issue, and add a checklist item to prevent recurrence.

## Portfolio Signal

This lab demonstrates publication readiness judgment: catching non-code artifact quality failures that can erode trust in an agent-assisted SDLC.
