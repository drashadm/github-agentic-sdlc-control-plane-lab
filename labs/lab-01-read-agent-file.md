# Lab 01: Read a Custom Agent File

## Difficulty

Beginner.

## Estimated Time

10-15 minutes.

## Scenario

You are reviewing a custom executor profile before allowing an agent runner to bind tools from it. The executor profile is not passive documentation: when an orchestrator, IDE agent, or CI workflow reads it, the profile can shape model behavior, define role boundaries, and grant execution authority. Your task is to decide whether the executor role is isolated behind deterministic controls or whether a markdown change could become a real capability change.

## Artifacts to Inspect

- `.github/agents/executor.agent.md`
- `.github/agents/reviewer.agent.md`
- `docs/guardrails-and-accountability.md`
- `.github/workflows/agent-runner-educational.yml`

## What You Are Looking For

Look for:

- Tool authority differences between reviewer and executor
- Whether `execute` access is isolated behind approval
- Whether natural-language safety rules are backed by deterministic controls
- Whether untrusted repository content, PR comments, issue text, or generated artifacts could contaminate the executor context
- Whether role transitions are explicit and enforced by workflow policy
- Whether agent profile changes should require human review
- Whether agent profile changes should be treated like source code, IAM policy, or workflow permission changes

## Questions

1. Why is the executor profile a prompt-and-capability control surface rather than passive documentation?
2. If a malicious pull request includes untrusted text that attempts to override the agent's instructions, what boundary in `executor.agent.md` prevents the executor from treating that content as higher authority than its own operating profile?
3. How does the educational workflow prevent a reviewer agent from dynamically becoming an executor agent during the same run?
4. Why is a policy written only in `docs/guardrails-and-accountability.md` insufficient to stop misuse of the `execute` tool?
5. What deterministic control should exist outside the LLM's natural-language reasoning before any high-risk tool call is allowed?
6. If an executor profile says "only run safe commands," why is that weaker than an allowlist of approved command IDs or function calls?
7. Which files should require human review if they change: agent profiles, workflow files, hook policies, MCP configs, or all of them?

## Expected Reasoning Path

A safe operator starts with the `.agent.md` front matter because tool access is a governance declaration. The reviewer profile has read/search authority, while the executor profile includes `execute`, which can change repository or environment state if an agent runner binds that tool. Next, inspect the profile body to see whether it requires explicit approval and stops on missing or stale artifacts.

Then look beyond the profile. Natural-language instructions are advisory unless a deterministic control enforces them. The educational runner workflow models the control-plane review that should happen before privileged agent execution: detect changes to agent profiles, workflows, hooks, and MCP configuration; flag executor/tool access changes; and preserve a review artifact. The safe conclusion is that profile changes, role transitions, and privileged tool calls need workflow, hook, or approval enforcement outside the model's own reasoning.

## Answer Key

1. It can be loaded into an LLM operating context and paired with tool permissions by an agent runner, so a markdown change can influence both behavior and authority.
2. The executor profile says it performs approved execution tasks only after human authorization, must not execute without explicit approval, and must stop if artifacts are missing or stale. That boundary should outrank untrusted PR or artifact text.
3. The educational workflow does not run a real agent or dynamically bind tools. It models review of changed control-plane files and flags executor/tool access changes before any high-risk invocation would occur.
4. Documentation alone cannot enforce behavior. Without a workflow, hook, allowlist, approval gate, or runner-side policy, the model could ignore or misinterpret advisory prose.
5. A deterministic approval gate, hook policy, command/function allowlist, or runner-side permission check should occur before high-risk tool calls.
6. "Only run safe commands" is subjective natural language. An allowlist of approved command IDs or function calls is explicit, auditable, and enforceable.
7. All of them should require review: agent profiles, workflow files, hook policies, and MCP configs are control-plane assets.

## Common Wrong Answers

- Treating `.agent.md` files as harmless documentation because they are markdown.
- Assuming the LLM will always follow the safest interpretation of natural-language boundaries.
- Letting a reviewer role become an executor role because the model says execution is now needed.
- Treating docs-only policy as equivalent to a deterministic approval gate.
- Reviewing tool access changes with less scrutiny than workflow permissions or IAM-style policy.

## Safe Operator Decision

Block unreviewed executor profile changes and require human review for agent profiles, workflow files, hook policies, and MCP configs. Do not allow high-risk tool calls until a deterministic control confirms approval, role boundaries, and allowed command/function scope. Preserve the agent profile review report as evidence.

## Agentic Nuance

Custom agent markdown profiles are not passive documentation. They are prompt-and-capability control surfaces that can be loaded into an LLM's operating context and paired with tool permissions by an orchestrator, IDE agent, or CI workflow.

That creates a different risk profile than ordinary configuration drift.

1. **Persona hijacking**
   Natural-language rules are probabilistic, not deterministic. An agent told to "execute safely" may still be influenced by malicious repository content, PR text, issue comments, or generated artifacts that attempt to override the intended operating boundary.

2. **Tool authority expansion**
   If the orchestration layer dynamically registers tools from an agent profile, a small change to a markdown file can become a real capability change. A reviewer who treats `.agent.md` as harmless text may accidentally approve a path from read-only review into edit or execute authority.

3. **State transition abuse**
   A safe agentic workflow should not allow an agent to promote itself from a low-privilege reviewer role into a high-privilege executor role during the same run. Role transitions should be deterministic, explicit, and enforced by workflow policy rather than inferred from model reasoning.

4. **Context contamination**
   High-risk agents should not consume untrusted PR comments, forked content, issue text, or arbitrary repository files immediately before using privileged tools unless those inputs are clearly classified, sanitized, and bounded.

The key lesson: agent profiles should be reviewed like production control-plane assets. A change to tool access, execution authority, MCP configuration, or role boundaries should receive the same scrutiny as source code, IAM policy, or GitHub Actions permission changes.

## Portfolio Signal

This lab demonstrates the ability to audit the intersection of LLM instruction surfaces, tool permissions, and CI/CD execution boundaries. It shows production-grade thinking about prompt security, agent role separation, deterministic guardrails, and the difference between advisory policy and enforceable controls.

A reviewer should come away understanding that the engineer can reason beyond "does the config file exist?" and ask the more important question: "What authority does this file grant once an agent runner interprets it?"
