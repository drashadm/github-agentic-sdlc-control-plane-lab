# Lab 03: Identify MCP Tool Access Risk

## Difficulty

Intermediate.

## Estimated Time

10-15 minutes.

## Scenario

An agent configuration includes broad MCP tool access. The example is intentionally risky for artifact-reading practice and should not be copied into production without review.

## Artifacts to Inspect

- `mcp/broad-server-wildcard-risk.yml`
- `mcp/local-stdio-risky-example.yml`
- `mcp/local-stdio-safe-example.yml`
- `mcp/mcp-allowlist-limitations.md`
- `docs/risk-to-github-mitigation-map.md`

## What You Are Looking For

Look for wildcard tool access, local process boundaries, server trust assumptions, and whether safer examples use explicit tool names. Also check whether the file clearly labels the example as risky and educational.

## Questions

1. Why is `governance-api/*` risky?
2. What safer pattern appears in the same risk example?
3. Why is an MCP allowlist not a complete security boundary?
4. What extra risk does local stdio introduce?
5. What review should be required before expanding MCP access?

## Expected Reasoning Path

A safe operator treats MCP access as capability expansion. Wildcards can grant access to tools that were not reviewed when the agent was approved. Local stdio servers may expose process or environment context, so the operator should prefer explicit allowlists, trusted servers, documented trust boundaries, and security review for new tools.

## Answer Key

1. It can include every current and future tool under that server namespace.
2. The safer pattern is a narrow list such as `governance-api/read-policy` and `governance-api/read-audit-summary`.
3. Allowlists narrow tool names but do not solve identity, network, runtime, logging, or secret-handling risks.
4. Local stdio can connect the agent to local process execution and local environment context.
5. Security review and explicit operator approval should be required before adding broad or remote MCP capability.

## Common Wrong Answers

- Treating `server/*` as safe because it is still an allowlist.
- Ignoring future tools that may appear under the wildcard.
- Assuming local MCP servers are safer than remote servers by default.
- Removing the educational risky example instead of labeling and constraining it.

## Safe Operator Decision

Narrow permissions to explicit tool names, document the trust boundary, and escalate broad MCP expansion for security review.

## Agentic Nuance

MCP expands agency beyond repository reading and editing. Wildcard access can turn a narrow reviewer or planner into a tool-using actor with unreviewed reach. The deeper failure is not only that a tool exists, but that the server trust boundary and future tool surface become invisible to normal code review.

## Portfolio Signal

This lab demonstrates practical MCP governance: reading tool boundaries, identifying overbroad access, and translating risk into least-privilege controls.
