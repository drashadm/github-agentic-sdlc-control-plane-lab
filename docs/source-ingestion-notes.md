# Source Ingestion Notes

This lab is based on public GitHub and Microsoft documentation concepts around GitHub-native agentic development workflows.

## Concept Areas Covered

### GH-600 Capability Areas

The lab maps to six practical capability areas:

1. Prepare agent architecture and SDLC processes
2. Implement tool use and environment interaction
3. Manage memory, state, and execution
4. Perform evaluation, error analysis, and tuning
5. Orchestrate multi-agent coordination
6. Implement guardrails and accountability

## Custom Agent Governance

Organizations should treat custom agents as governed SDLC assets. A reusable agent should have:

- a clear purpose
- scoped tools
- explicit boundaries
- documented risks
- review and approval expectations
- ownership
- update and retirement procedures

## Custom Agent File Structure

Custom agent profiles are represented as markdown files with YAML frontmatter followed by operating instructions.

Common fields include:

- `name`
- `description`
- `tools`
- `mcp-servers`

The frontmatter declares capability and configuration. The markdown body explains behavior, boundaries, and output expectations.

## Tool Scoping

Tool scoping is a primary safety mechanism.

Examples:

- `read`: inspect files and context
- `search`: search repository/code context
- `edit`: propose or make file changes
- `execute`: run commands, higher risk
- `agent`: call or coordinate another agent
- `web`: access external web context where allowed
- `todo`: manage structured task lists

A safe control plane avoids giving every agent every tool.

## MCP Configuration

MCP-style configuration can expose external tools to agents. This lab distinguishes:

- local stdio/local process servers
- remote HTTP-style servers
- narrow allowlists such as `server/tool`
- broad wildcard allowlists such as `server/*`

## MCP Allowlist Limitations

MCP allowlists are capability boundaries, not complete network firewall controls. Server identity, configuration integrity, environment restrictions, and review gates still matter.

## Copilot Memory

Memory can help agents remember repository facts, conventions, or user preferences. Memory can also create risk when facts are stale, unverified, or conflict with current repository state.

This lab treats memory as evidence that must be validated, not as unquestioned truth.

## Hooks and Permission Decisions

Hooks can provide control points before and after tool use.

Typical hook ideas:

- block risky tool use
- rewrite unsafe arguments
- add context after execution
- escalate high-risk actions to a human

The key distinction is whether the control applies to local CLI-style execution, cloud-agent execution, or both.

## GitHub Actions Artifacts

Workflow artifacts serve as durable handoffs between jobs and reviewers. A plan artifact can be consumed by a builder job. A builder summary can be consumed by a reviewer. Review and security audit artifacts can be consolidated into an operator report.

## Multi-Agent Orchestration

Multi-agent workflows require isolation, handoffs, conflict detection, and auditability. Parallel work can accelerate delivery, but only if the control plane can detect duplication, contradictory outputs, or overlapping changes.

## Guardrails and Accountability

Guardrails should right-size human intervention. Low-risk read-only actions can move quickly. Irreversible, security-sensitive, compliance-sensitive, or production-impacting actions should require explicit authorization.
