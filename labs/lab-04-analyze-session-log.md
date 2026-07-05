# Lab 04: Analyze a Session Log

## Difficulty

Intermediate.

## Estimated Time

15-20 minutes.

## Scenario

An agent resumed a previous session and made a repository change. The log shows continuity, but a resumed session is not proof of safe continuity. It only proves that prior context was carried forward.

In an agentic SDLC workflow, old session context can preserve useful progress, but it can also carry stale assumptions, outdated branch state, old memory facts, previous error traces, obsolete plans, or invalid permissions into a new run. The safe operator question is not "Did the session resume?" The safe operator question is: "Did the resumed session prove it still matches the current branch, commit SHA, run ID, memory state, tool permissions, approval state, and expected artifacts?"

## Artifacts to Inspect

- `logs/copilot-cli-session-new.log`
- `logs/copilot-cli-session-resumed.log`
- `logs/cloud-agent-stuck-session.log`
- `logs/workflow-permission-denied.log`
- `memory/repository-facts-example.json`
- `memory/stale-memory-drift-scenario.md`
- `artifacts/planner-output.json`
- `artifacts/git-state-snapshot.json`
- `artifacts/session-continuity-report.json`
- `schemas/git-state-snapshot.schema.json`
- `schemas/session-continuity-report.schema.json`
- `docs/session-continuity-governance.md`
- `docs/state-serializability.md`
- `docs/advanced-agentic-failure-modes.md`
- `docs/guardrails-and-accountability.md`

## What You Are Looking For

Look for:

- New session versus resumed session
- Temporal drift between the original run and the resumed run
- Anchor bias from old session context, prior plans, or previous failures
- Branch drift and commit SHA mismatch
- Stale memory facts, memory TTL, or missing validation timestamp
- Stale artifact references that no longer match the current run
- Previous run failure, stall, or permission denial
- Previous error footprint replay into current execution
- Out-of-band repository changes such as a human hotfix or parallel PR merge
- Tool permission changes between runs
- Unresolved risk carried forward, dropped, or incorrectly marked complete
- Whether resumed-session evidence is strong enough to permit privileged action
- False continuity: logs may look continuous while branch, commit, artifact, memory, permission, or approval state no longer matches reality

## Questions

1. What evidence proves that a resumed session is continuing the correct task rather than carrying stale context?
2. Why is matching session ID alone insufficient to approve continued execution?
3. If the current commit SHA differs from the commit SHA recorded when the session was created, what should happen before the agent continues?
4. How can stale memory cause a resumed agent to make a wrong decision even if the log says the session resumed successfully?
5. How can old session history anchor the agent to an obsolete plan or obsolete error state?
6. What is the risk if a previous run stalled or crashed but the resumed session treats it as completed?
7. What should happen if tool permissions changed between the original and resumed session?
8. What control detects whether a human hotfix or parallel PR merge changed the repository while the agent was suspended?
9. Which artifact should prove that memory facts, branch state, tool permissions, prior error traces, and approval state were checked before privileged execution?
10. When should the operator allow a resumed session to continue, reset it, or escalate it for human review?

## Expected Reasoning Path

Start with the session logs. Compare `logs/copilot-cli-session-new.log` with `logs/copilot-cli-session-resumed.log` and confirm that the same session ID appears in both. Then resist the easy conclusion. A matching session ID only proves that prior context was rehydrated; it does not prove that the repository, memory, approval, or tool boundary still matches the original world state.

Next, inspect `artifacts/git-state-snapshot.json`. The mocked snapshot shows the resumed session still expects the same branch, but the commit SHA no longer matches. That means an out-of-band change may have landed while the agent was suspended. A safe workflow should block privileged execution until the current branch and commit are compared with the session's expected state.

Then inspect memory and error evidence. `memory/repository-facts-example.json` contains validated repository facts, while `memory/stale-memory-drift-scenario.md` shows how an older memory fact can conflict with current agent permissions. `logs/cloud-agent-stuck-session.log` and `logs/workflow-permission-denied.log` show previous failure footprints that should be treated as evidence, not as instructions to replay blindly.

Finally, inspect `artifacts/session-continuity-report.json`. A safe resumed session should preserve session ID, previous and current run IDs, branch, commit SHA, artifact provenance, memory checks, tool permission changes, approval state, stale-context findings, previous error footprints, and a safe next action. If that evidence is missing or marked `review_required`, the operator should block privileged work until continuity is verified.

## Answer Key

1. Evidence should include session ID, previous and current run IDs, previous and current branch, previous and current commit SHA, artifact references, memory validation, tool permission status, approval state, unresolved risks, and safe next action.
2. A session ID only shows that prior context was carried forward. It does not prove the current branch, commit, artifact set, memory state, permissions, or approval boundary still matches the original run.
3. Privileged execution should stop. The operator should inspect the diff or mocked git state snapshot, determine whether the change was expected, regenerate stale artifacts if needed, and reapprove only after continuity is verified.
4. Stale memory can preserve an old permission rule, outdated file fact, or obsolete policy. The agent may trust that memory over current repository evidence unless memory is revalidated against the current branch and commit.
5. Old history can make the agent interpret current files through a previous plan or failure. It may keep fixing a problem that no longer exists or repeat a plan that was superseded by a human hotfix or merged PR.
6. The agent may skip required recovery, mark incomplete work as done, or continue from a corrupted intermediate state.
7. Treat the permission change as a control-plane change. Block high-risk actions until the new permission boundary is reviewed, documented, and approved.
8. A git state snapshot or equivalent workflow evidence comparing previous and current branch, commit SHA, run ID, and artifact provenance detects out-of-band changes.
9. `artifacts/session-continuity-report.json` should prove those continuity checks happened before privileged execution.
10. Allow resume only when branch, commit, artifacts, memory, permissions, prior errors, unresolved risks, and approval state are current and valid. Reset if context is stale or contaminated. Escalate if privileged actions, permission changes, failed runs, or unresolved drift are involved.

## Common Wrong Answers

- Assuming a resumed session is safe because it has the same session ID.
- Reading only the final status and ignoring branch, commit, run ID, memory, and approval evidence.
- Treating memory validation from an old run as valid for the current run.
- Replaying a previous error trace without checking whether the underlying issue still exists.
- Allowing tool use because the previous run had approval, even though permissions or repository state changed.
- Treating a stalled or crashed prior run as completed because the resumed session continued smoothly.

## Safe Operator Decision

Block privileged execution until deterministic continuity evidence proves the resumed session still matches the current branch, commit SHA, run ID, artifact provenance, memory state, tool permissions, approval state, and prior error relevance. If commit drift, stale memory, permission changes, unresolved failures, or missing artifacts are present, reset or re-scope the session and preserve the continuity report for review.

## Agentic Nuance

Session resumption introduces the risk of temporal drift and context anchoring. When an agent state is rehydrated from logs, memory, or a previous conversation, the model may treat that history as the foundation for its current world model.

That is useful when the world has not changed. It is dangerous when the repository has changed underneath the agent.

A resumed agent can run smoothly, consume tokens, update files, and report success while operating from obsolete assumptions. It may reapply an old plan, revive a stale error trace, ignore a human hotfix, or overwrite work from a parallel PR because its internal context no longer matches the external repository state.

This is efficient regression: the agent appears productive while corrupting state that had already moved forward.

The safe control is deterministic continuity validation. A resumed session should not perform privileged work until branch, commit SHA, run ID, artifact provenance, memory freshness, tool permissions, prior error relevance, and approval state are verified. Continuity without real-time state revalidation is automated state corruption.

## Portfolio Signal

This lab demonstrates production-grade thinking about forensic agent log analysis, temporal drift, resumed-state validation, and stale-context governance. It shows the ability to inspect logs as control-plane evidence, not just debugging output.

A reviewer should come away understanding that the engineer can reason beyond "did the session resume?" and ask the more important question: "Did the resumed agent prove it is still operating on the correct branch, commit, memory, artifact, permission, and approval boundary?"
