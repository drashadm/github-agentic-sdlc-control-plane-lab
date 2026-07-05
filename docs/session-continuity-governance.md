# Session Continuity Governance

## Why Resumed Sessions Are Risky

Resumed sessions can preserve useful task progress, but they can also preserve stale assumptions, old branch state, previous error traces, outdated tool permissions, and invalid memory. A resumed conversation or agent session is continuity of context, not proof that the context still matches the repository.

## Temporal Drift and Anchor Bias

Old session history can anchor the model to obsolete assumptions. In operational terms, stale context may dominate current execution unless it is revalidated. The agent may interpret fresh repository state through a prior plan, prior failure, or prior policy version even when the repository has moved on.

## Memory Invalidation

Repository facts, vector memory, and flat JSON memory can become toxic when repository state changes out of band. Out-of-band changes include:

- Human hotfixes
- Parallel PR merges
- Emergency GitHub UI edits
- Policy changes
- Workflow permission changes
- Regenerated artifacts

Memory should be treated as a cache that must be validated against current repository evidence before it influences privileged work.

## Previous Error Footprints

Resuming from a failed or crashed session can reintroduce old error traces into the current prompt context. The agent may try to fix a problem that no longer exists, repeat a stale workaround, or skip recovery because it assumes the prior run already completed.

## Continuity Evidence

A safe resumed session should verify:

- Session ID
- Previous and current run ID
- Previous and current commit SHA
- Previous and current branch
- Artifact references
- Memory facts checked
- Memory validation timestamp
- Tool permissions
- Policy version
- Approval state
- Safe next action

## False Continuity

A resumed session may appear continuous while the underlying state is no longer continuous. False continuity can happen when:

- Branch changed
- Commit changed
- Required artifact regenerated
- Tool permissions changed
- Memory fact expired
- Policy changed
- Previous run failed or stalled
- Old failure trace is no longer relevant

## Safe Resume Checklist

- Verify branch and commit
- Verify run ID and artifact provenance
- Validate memory against current repository state
- Confirm tool permissions have not expanded
- Confirm unresolved risks are still present
- Confirm previous error traces are still relevant
- Block privileged actions until continuity is verified

## Operator Decision

Allow resume when branch, commit, run ID, artifacts, memory facts, tool permissions, policy version, approval state, and prior error relevance have been verified for the current repository state. Reset the session when old context conflicts with current evidence or contains stale memory that would contaminate execution. Escalate when privileged actions, permission changes, failed prior runs, regenerated artifacts, or unresolved drift are involved.
