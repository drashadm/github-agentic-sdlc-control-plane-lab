# Artifact Reading Guide

This guide teaches how to inspect the artifacts that govern agentic SDLC workflows.

## Custom Agent Files

### What It Is

A custom agent file declares an agent's purpose, tool access, configuration, and behavioral instructions.

### Why It Matters

The file defines what the agent is supposed to do and what it is allowed to access.

### Inspect

- `name`
- `description`
- `tools`
- `mcp-servers`
- role-specific boundaries
- output format requirements
- approval requirements

### Common Failure Indicators

- broad `tools: ["*"]`
- execute access for a non-executor role
- unclear output format
- no warning for high-risk actions
- MCP tools included without rationale

### Safe Operator Response

Narrow the tools, clarify the role, require structured output, and add approval gates for risky actions.

## MCP Configuration

### What It Is

Configuration that exposes external or local tools to an agent.

### Why It Matters

MCP expands agent capability beyond repository reasoning.

### Inspect

- server name
- local command vs remote URL
- arguments
- environment variables
- tool allowlist
- wildcard use
- transport type

### Common Failure Indicators

- broad `server/*`
- unclear server identity
- exposed credentials
- remote server without trust notes
- allowlist treated as complete security control

### Safe Operator Response

Prefer narrow tool access, document trust boundaries, verify environment handling, and require approval for expanded access.

## GitHub Actions Workflows

### What It Is

A YAML workflow that executes jobs, sets permissions, passes outputs, and stores artifacts.

### Why It Matters

Workflows enforce the delivery path and preserve evidence.

### Inspect

- `on`
- `permissions`
- `concurrency`
- `jobs`
- `needs`
- job outputs
- `$GITHUB_OUTPUT`
- artifact upload/download
- branch/ref conditions

### Common Failure Indicators

- missing `permissions`
- missing `needs`
- output name mismatch
- artifact name mismatch
- downstream job runs despite failed gate
- overly broad write permissions

### Safe Operator Response

Fix output names, add explicit dependencies, scope permissions, enforce gates, and preserve artifacts.

## Hooks

### What It Is

A control point before or after tool use.

### Why It Matters

Hooks can block, transform, or add context around tool calls.

### Inspect

- event type
- tool name
- tool arguments
- decision field
- allow/deny/ask behavior
- CLI-only vs cloud-agent applicability

### Common Failure Indicators

- hook logs a warning but does not block
- `ask` assumed to work in a context where it denies
- execute access allowed without approval
- post-tool context hides a failure

### Safe Operator Response

Clarify enforcement behavior, test the hook path, and ensure blocked actions fail closed.

## Copilot-like Session Logs

### What It Is

A log showing how an agent session started, resumed, used tools, encountered errors, and produced outputs.

### Why It Matters

Session logs reveal continuity, context drift, and execution trace.

### Inspect

- session ID
- resumed vs new session
- branch/ref
- tool calls
- approval state
- errors
- artifact paths
- final status

### Common Failure Indicators

- resumed session uses stale branch
- repeated work without recognizing prior artifact
- tool denied but task marked successful
- approval state missing

### Safe Operator Response

Reset or re-scope the session, validate current repository state, and require artifact regeneration.

## Workflow Artifacts

### What It Is

Files produced by workflows or agents for downstream review.

### Why It Matters

Artifacts are durable evidence and handoff contracts.

### Inspect

- artifact name
- producing job
- consuming job
- schema
- timestamp
- decision fields
- unresolved findings

### Common Failure Indicators

- stale timestamp
- schema mismatch
- missing required field
- final report omits reviewer/security findings
- artifact deleted before review

### Safe Operator Response

Regenerate the artifact, block downstream jobs, and preserve the audit trail.

## PR Timelines and Audit Trails

### What It Is

Chronological evidence of assignments, comments, reviews, approvals, workflow runs, and changes.

### Why It Matters

PR timelines connect human and agent actions.

### Inspect

- who assigned the agent
- which branch changed
- review requests
- approval gates
- workflow run links
- artifact deletion events
- merge decision

### Common Failure Indicators

- agent unassigned/reassigned without explanation
- approval skipped
- workflow file changed without required review
- audit artifact removed early

### Safe Operator Response

Pause merge, reconstruct the timeline, request review, and preserve evidence.

## Memory and State Files

### What It Is

Stored facts, preferences, decisions, and task progress used to maintain continuity.

### Why It Matters

Memory improves continuity but can cause drift if stale.

### Inspect

- source
- last validated timestamp
- branch/ref citation
- expiration
- scope
- conflicts with current files

### Common Failure Indicators

- old architecture decision reused
- preference applied outside scope
- memory has no citation
- conflict with current repository state

### Safe Operator Response

Validate against current repository files, prune stale facts, and regenerate state artifacts.

## Schema Validation as Artifact Governance

Structured artifacts are easier to inspect because important fields have predictable names and locations. Schemas make missing fields visible before a downstream workflow, reviewer, or operator relies on an incomplete handoff.

Schemas help downstream jobs trust artifact shape, not artifact truth. Validation can show that a planner output includes success criteria, risks, affected files, and approval state, but it does not prove the agent made the right plan. It proves the artifact is complete enough to review.

Use `docs/artifact-schema-map.md` to understand which sample artifacts map to which schemas, and inspect `schemas/` for the minimum required fields.
