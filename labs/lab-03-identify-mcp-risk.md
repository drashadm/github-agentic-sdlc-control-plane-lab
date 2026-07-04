# Lab 03: Identify MCP Tool Access Risk

## Difficulty

Intermediate.

## Estimated Time

10-15 minutes.

## Scenario

An agent configuration includes broad MCP tool access. This is not just a configuration smell: MCP is externalized agent authority. A tool allowlist defines what the agent can reach, read, call, mutate, or trust outside its core prompt context. Overbroad MCP access can turn a constrained agent into an overprivileged operator.

## Artifacts to Inspect

- `mcp/local-stdio-safe-example.yml`
- `mcp/local-stdio-risky-example.yml`
- `mcp/remote-http-example.yml`
- `mcp/broad-server-wildcard-risk.yml`
- `mcp/broad-server-wildcard-risk.json`
- `mcp/local-stdio-risky-example.json`
- `mcp/local-stdio-safe-example.json`
- `mcp/server-manifest-snapshot.json`
- `mcp/mcp-allowlist-limitations.md`
- `.github/agents/security-auditor.agent.md`
- `.github/agents/executor.agent.md`
- `docs/agentic-threat-model-map.md`
- `docs/risk-to-github-mitigation-map.md`
- `docs/guardrails-and-accountability.md`
- `docs/mcp-tool-boundary-governance.md`

## What You Are Looking For

Look for:

- Narrow MCP tool allowlists versus broad wildcard access
- Local stdio server risk versus remote HTTP server trust boundary
- MCP allowlists as capability controls, not complete security boundaries
- Tool-output trust: downstream agents may treat MCP results as authoritative even when they need validation
- Server identity drift: a server name may stay the same while implementation or available tools change
- Capability creep: wildcard access may silently grant future tools
- Confused deputy risk: an agent may call a tool that acts with broader authority than the agent should have
- Data egress risk when remote tools receive repository or task context
- Dynamic tool-list changes through server-declared `listChanged` behavior, where supported
- Strict argument schemas and provenance evidence for tool calls
- Why stdio is a host subprocess boundary that requires isolation and trusted configuration
- Why MCP config changes should require review like workflow permission or IAM policy changes

## Questions

1. Why is `server/*` materially different from an explicit allowlist such as `server/read-policy`?
2. What new trust boundary is created when an agent uses a remote HTTP MCP server instead of a local read-only tool?
3. Why is an MCP allowlist not equivalent to a firewall, sandbox, or secret-management policy?
4. How could wildcard MCP access create capability creep if the server owner adds new tools later?
5. How can server-declared dynamic tool-list changes affect an existing wildcard approval?
6. Why should MCP tools use strict argument schemas?
7. If an MCP tool returns a policy summary, why should the downstream agent not automatically treat that summary as verified truth?
8. What evidence should an operator preserve to prove which MCP server, tool name, run ID, branch, and agent profile were involved?
9. Which files should require human review when MCP access changes?
10. What should happen if an agent profile requests a new MCP tool that is not already reviewed and documented?

## Expected Reasoning Path

Start by comparing explicit tool lists with wildcard access. A narrow allowlist such as `governance-api/read-policy` limits the agent to a named capability, while `governance-api/*` delegates future authority to the server namespace. Then compare transport boundaries: a local stdio server is a host subprocess boundary that requires isolation and trusted configuration; it does not automatically mean arbitrary code execution, but it does require host-level review. A remote HTTP server adds data egress, server identity, authentication, and logging questions.

Next, inspect the server manifest snapshot. MCP can support dynamic tool-list changes through server-declared `listChanged` behavior, so an operator should preserve evidence of the tool list discovered at runtime. Do not assume every MCP server mutates tools mid-session, but do verify which tools were actually available for the run. Finally, treat MCP output as evidence that still needs validation, not as ground truth.

## Answer Key

1. `server/*` grants every current and future tool under that server namespace; `server/read-policy` grants one reviewed capability.
2. A remote HTTP server introduces network, identity, ownership, data egress, authentication, logging, and availability boundaries outside the local repository.
3. An allowlist controls named tool access, but it does not replace network controls, process isolation, secret handling, server identity validation, runtime monitoring, or human approval.
4. If the server later adds tools, wildcard access can grant those tools without changing the agent profile.
5. If a server supports dynamic tool-list changes through `listChanged`, the runtime tool surface can change after an earlier review. Wildcard approvals should be revalidated against discovered tools.
6. Strict argument schemas reduce ambiguous calls, unexpected parameters, and model-inferred tool usage that the operator did not review.
7. Tool output can be stale, incomplete, malformed, biased, or influenced by upstream data. Downstream agents should validate source, timestamp, schema, and provenance.
8. Preserve server name, server version, transport, discovered tool list, tool name, run ID, branch, commit SHA, agent profile, arguments where safe, output artifact, and review decision.
9. MCP configs, agent profiles, workflow files that bind tools, hook policies, and any server manifest or review artifact should require human review.
10. Block or escalate the change until the tool purpose, owner, trust boundary, allowed action, schema, logging, and removal path are reviewed and documented.

## Common Wrong Answers

- Treating `server/*` as safe because it is still an allowlist.
- Assuming local stdio automatically means arbitrary code execution, or assuming it is safe without subprocess isolation review.
- Assuming every MCP server mutates tools mid-session instead of checking runtime capabilities and `listChanged` behavior where supported.
- Trusting MCP output as verified truth because it came from a tool.
- Reviewing MCP changes with less rigor than workflow permissions or IAM-style policy.

## Safe Operator Decision

Narrow MCP access to explicit, reviewed tools. Block wildcard access unless it has documented justification, ownership, logging, runtime discovery evidence, and human approval. Require review for new MCP tools, remote servers, local stdio subprocess boundaries, agent profiles that bind MCP tools, and any workflow or hook that changes MCP authority.

## Agentic Nuance

MCP configuration is not just integration plumbing. It is the boundary where an agent's reasoning loop becomes external authority. A model that was previously limited to reading repository context can suddenly query tools, retrieve external state, or trigger actions through an MCP server.

That creates several agent-specific risks:

1. **Capability creep**
   Wildcard access such as `server/*` can silently expand the agent's authority when the server later adds new tools. The agent profile may not change, but the effective capability surface does.

2. **Server identity drift**
   A stable server name does not guarantee stable behavior. The implementation, transport, authentication, or available tools can change behind the same logical MCP name.

3. **Tool-output poisoning**
   Agents may over-trust tool responses. If a tool returns stale, incomplete, or adversarially influenced content, the downstream agent may treat that output as grounded truth unless the workflow requires validation and provenance.

4. **Confused deputy behavior**
   A low-authority agent can become dangerous if it calls a tool that acts with higher authority than the agent should possess.

5. **Remote trust boundary expansion**
   Remote MCP tools may receive repository context, prompts, summaries, or artifacts. That creates data egress and auditability concerns beyond simple local config review.

The safe control is explicit, reviewed, least-privilege MCP access. Every MCP tool should have a clear purpose, owner, trust boundary, allowed action, logging expectation, and removal path. Wildcards should be treated as high-risk exceptions, not defaults.

## Portfolio Signal

This lab demonstrates the ability to audit MCP as an agent authority boundary rather than treating it as ordinary configuration. It shows production-grade thinking about least-privilege tool access, server trust boundaries, tool-output validation, and the operational risks created when LLM agents gain external capability through MCP.

A reviewer should come away understanding that the engineer can reason beyond "is the MCP server configured?" and ask the more important question: "What authority does this tool grant once an agent can call it?"
