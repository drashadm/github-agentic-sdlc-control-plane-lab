# Lab 06: Memory Drift

## Difficulty

Intermediate.

## Estimated Time

15-20 minutes.

## Scenario

Stored memory says the Builder Agent should run tests, but the current repository agent profile shows the Builder has only `read`, `search`, and `edit` tools. The operator must decide whether memory can authorize the action.

Memory is useful context, not runtime authority. If memory says the Builder Agent should perform work that requires execution, but the Builder profile lacks execution authority, the memory is wrong for execution purposes. The agent must not self-remediate by inventing a proxy path, modifying workflows, editing helper scripts, or rewriting its own memory. Runtime authorization must come from source-controlled agent profiles, workflow permissions, MCP/tool policy, and human-approved control-plane state.

## Artifacts to Inspect

- `memory/stale-memory-drift-scenario.md`
- `memory/repository-facts-example.json`
- `memory/memory-vector-index.lock.json`
- `.github/agents/builder.agent.md`
- `.github/agents/executor.agent.md`
- `artifacts/memory-validation-report.json`
- `artifacts/memory-authority-review-report.json`
- `schemas/memory-validation-report.schema.json`
- `schemas/memory-authority-review-report.schema.json`
- `docs/memory-governance.md`
- `docs/session-continuity-governance.md`
- `docs/state-serializability.md`
- `docs/advanced-agentic-failure-modes.md`
- `docs/guardrails-and-accountability.md`

## What You Are Looking For

Look for:

- Memory as non-authoritative cache
- Stale memory facts
- Missing `source_commit_sha`
- Missing `validated_at`
- Memory TTL or expiration policy
- Vector index and flat JSON sync divergence
- Out-of-band repository mutations
- Belief versus authorization separation
- Read/write asymmetry for memory
- Agent self-remediation risk
- Memory fact conflicts with `.agent.md` permissions
- Repository evidence overriding memory
- Memory quarantine before context injection
- Human review for memory writes

## Questions

1. Why must memory be treated as untrusted input rather than runtime authority?
2. If the Builder Agent reads a memory fact saying it must run tests, but its profile lacks execution authority, what should happen?
3. Why is it unsafe for the Builder Agent to use its edit authority to create a workaround for a missing execution tool?
4. If a memory fact lacks `source_commit_sha`, why should the runtime treat it as untrusted until verified?
5. How can a vector index drift away from flat JSON repository facts after a human hotfix or parallel PR merge?
6. What is the risk if an agent can write to its own long-term memory without review?
7. Which source wins when memory conflicts with current repository files or `.agent.md` permissions?
8. What artifact should prove that memory facts were validated before entering the agent context window?
9. What should happen to stale or unpinned memory before privileged execution?
10. Which control-plane sources can grant runtime authority?

## Expected Reasoning Path

Start with `memory/stale-memory-drift-scenario.md`. The remembered fact claims that the Builder Agent may execute test commands after planning, but `.github/agents/builder.agent.md` grants only `read`, `search`, and `edit`. Then compare `.github/agents/executor.agent.md`, which is the profile that has `execute` authority and requires explicit human approval.

Next inspect `memory/repository-facts-example.json`. Some facts are valid and source-bound, while others are stale, missing source commit metadata, or conflict with current agent profile authority. The operator should not treat all facts equally just because they live in the memory directory.

Then inspect `memory/memory-vector-index.lock.json`. It shows a mock vector index generated from an older commit that no longer matches current head. That means long-term memory and flat JSON facts may be out of sync with the repository.

Finally, inspect `artifacts/memory-validation-report.json` and `artifacts/memory-authority-review-report.json`. The first proves which memory facts were checked, allowed, or quarantined before context injection. The second separates what the agent believes from what the runtime authorizes. A safe operator blocks execution through the Builder, quarantines stale memory, and routes any approved execution through the authorized Executor path.

## Answer Key

1. Memory is retrieved context. It can be stale, unpinned, generated from old files, or inconsistent with current repository authority.
2. The Builder must not execute. The task should be handed off to an authorized Executor Agent, or a human-approved control-plane change should be requested.
3. That would turn edit authority into an indirect execution path and bypass the source-controlled role boundary.
4. Without a source commit, the runtime cannot prove which repository state produced the memory or whether it still matches current head.
5. A vector index can remain built from old files while JSON facts or repository files change after a human hotfix, parallel PR merge, regenerated artifact, or policy update.
6. The agent can create self-reinforcing false state: it may rewrite memory to match its plan and future runs may inherit that false authority.
7. Current repository evidence wins: `.agent.md` files, workflow permissions, MCP/tool policy, and explicit human-approved control-plane state outrank memory.
8. `artifacts/memory-validation-report.json` should prove validation before memory enters the context window.
9. Quarantine it, exclude it from context, regenerate or re-index it, and require review before using it for privileged decisions.
10. Source-controlled agent profiles, workflow permissions, MCP/tool policy, and human approval gates grant runtime authority.

## Common Wrong Answers

- Trusting memory because it sounds operationally useful.
- Editing the Builder profile, workflow, or helper file to match stale memory.
- Treating memory as an approval record.
- Letting the agent rewrite its own memory without review.
- Loading stale or unpinned memory into context because it is already stored in the repository.
- Ignoring vector index drift because flat JSON facts look current.

## Safe Operator Decision

Block execution through the Builder Agent. Treat memory as untrusted context until it is source-bound, commit-aware, freshness-checked, and compared with current repository authority. Quarantine stale, unpinned, or authority-conflicting memory before context injection. Route execution through the Executor Agent with explicit approval, or request a reviewed control-plane change.

## Agentic Nuance

Memory is a soft state plane. It can help an agent preserve context, but it should never grant authority. Repository files, agent profiles, workflow permissions, MCP policies, and human approval gates are the hard governance plane.

When memory and governance diverge, the agent may not fail like a traditional program. It may try to reconcile the conflict by inventing a plausible path forward. A Builder Agent that remembers it should run tests may attempt to create helper files, modify workflow behavior, or rewrite its own task context even though its profile does not authorize execution.

That is the core risk: memory can shape belief, but belief must not become permission.

Memory also drifts structurally. Flat JSON facts, vector indexes, and session summaries can fall out of sync when the repository changes through a human hotfix, parallel PR merge, or policy update. Once stale memory enters the context window, it can steer the agent toward confident but incorrect execution.

The safe control is deterministic memory validation before context injection. Memory facts should be source-bound, commit-aware, freshness-checked, compared against current repository evidence, and quarantined when stale, unpinned, or authority-conflicting. Agents may read memory as context, but memory writes and authority-affecting updates require review.

## Portfolio Signal

This lab demonstrates production-grade thinking about memory governance in multi-agent SDLC systems. It shows the ability to separate agent belief from runtime authorization, detect stale or unpinned memory, validate memory against source-controlled evidence, and prevent non-deterministic agents from rewriting their own authority model.

A reviewer should come away understanding that the engineer can reason beyond "does the agent remember?" and ask the more important question: "Is this memory valid, current, source-bound, and allowed to influence execution?"
