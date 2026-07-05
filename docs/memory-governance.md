# Memory Governance

## Memory Is Not Authority

Memory is retrieved context, not permission. Runtime authority must come from source-controlled agent profiles, workflow permissions, MCP/tool policy, and human approval gates.

## Belief vs. Authorization

An agent may believe it should perform an action because a memory says so, but that does not mean it is authorized to perform that action.

An agent's belief about its task must never expand its runtime authority.

## Context Conflict and Confident Wrong Execution

When memory conflicts with current repository state or current agent permissions, the model may try to reconcile the conflict by inventing a plausible bridge. In an SDLC setting, that can look like:

- Rewriting a workflow it is allowed to edit
- Creating an ad-hoc helper file
- Modifying memory to match its plan
- Escalating to a tool it should not use
- Continuing confidently from stale assumptions

These are governance failures even when they look like helpful problem solving.

## Git-Pinned Memory Binding

Memory facts should include source metadata where possible:

- Source path
- Source commit SHA
- Source branch
- `generated_at`
- `validated_at`
- TTL or expiration policy
- Owner or producing workflow
- Confidence/source type

If a memory fact lacks a source commit or validation timestamp, the runtime should treat it as untrusted until verified.

## Vector Index and JSON Sync Drift

Long-term memory can drift when:

- A human hotfix lands
- A parallel PR merges
- Repository files change out of band
- Embeddings are not regenerated
- Memory compaction runs on stale files
- Flat JSON facts diverge from vector memory

## Read/Write Asymmetry

An agent may read memory as context, but writing to memory is a governance action. Agents should not be able to mutate their own long-term memory without review, because that can create self-reinforcing false beliefs.

## Memory Invalidation Lifecycle

Safe memory handling includes:

- Validate before context injection
- Compare memory source commit to current head
- Compare memory claims to agent profile permissions
- Quarantine stale or unpinned memory
- Schedule re-indexing
- Preserve validation evidence
- Require human review for memory writes affecting authority, scope, or policy

## Safe Operator Checklist

- Does this memory fact have a source?
- Is it bound to a commit SHA?
- Does it match current branch/head?
- Does it conflict with agent profile authority?
- Does it conflict with repository evidence?
- Is it stale or expired?
- Can the agent write back to this memory?
- Should the memory be allowed, quarantined, regenerated, or deleted after review?
