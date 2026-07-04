# GH-600 Domain Map

This document maps the lab to six practical agentic SDLC capability areas.

## 1. Prepare Agent Architecture and SDLC Processes

### Practical Meaning

Define how agents participate in the software development lifecycle. Separate planning, reasoning, execution, review, and approval.

### Repo Artifacts

- `.github/agents/planner.agent.md`
- `.github/agents/builder.agent.md`
- `.github/agents/reviewer.agent.md`
- `.github/workflows/agent-plan-review.yml`
- `artifacts/planner-output.json`

### Artifact-Reading Skills

- identify what an agent is allowed to do
- distinguish planning output from executable change
- verify inputs, outputs, and success criteria
- detect missing approval gates

### Example Failure Modes

- an agent moves from planning to execution without review
- success criteria are vague
- output is not structured enough for downstream review
- the wrong branch or repository scope is used

## 2. Implement Tool Use and Environment Interaction

### Practical Meaning

Select tools, configure permissions, integrate MCP servers, and control how agents interact with repositories, branches, CI, and external systems.

### Repo Artifacts

- `.github/agents/*.agent.md`
- `mcp/local-stdio-safe-example.yml`
- `mcp/remote-http-example.yml`
- `mcp/broad-server-wildcard-risk.yml`
- `.github/workflows/security-gate.yml`

### Artifact-Reading Skills

- inspect tool lists
- distinguish narrow tool access from wildcard access
- identify local vs remote server configuration
- spot tool/environment mismatches

### Example Failure Modes

- broad `server/*` MCP access
- execute access granted to a reviewer
- remote MCP server used without a clear trust boundary
- CI job lacks required permissions

## 3. Manage Memory, State, and Execution

### Practical Meaning

Maintain task continuity without allowing stale context or conflicting facts to drive the agent.

### Repo Artifacts

- `memory/repository-facts-example.json`
- `memory/user-preferences-example.json`
- `memory/stale-memory-drift-scenario.md`
- `logs/copilot-cli-session-resumed.log`

### Artifact-Reading Skills

- determine whether a session is new or resumed
- detect stale facts
- compare memory against current repository evidence
- identify context drift

### Example Failure Modes

- resumed session ignores a newer decision
- repository memory conflicts with current files
- agent repeats prior work
- stale branch state causes bad recommendations

## 4. Perform Evaluation, Error Analysis, and Tuning

### Practical Meaning

Define success criteria, inspect outputs, classify root causes, and tune instructions/tools/workflows based on evidence.

### Repo Artifacts

- `docs/failure-analysis-playbook.md`
- `artifacts/reviewer-findings.json`
- `artifacts/security-audit-report.json`
- `logs/workflow-permission-denied.log`

### Artifact-Reading Skills

- classify failures as reasoning, tool, environment, or context issues
- locate the artifact that proves the failure
- decide whether to retry, rollback, escalate, or update instructions

### Example Failure Modes

- output artifact missing expected schema
- workflow failed due to insufficient permission
- agent made a correct plan but used the wrong tool
- reviewer flagged incomplete tests but no tuning occurred

## 5. Orchestrate Multi-Agent Coordination

### Practical Meaning

Coordinate planner, builder, reviewer, security auditor, and consolidator roles through artifacts and workflows.

### Repo Artifacts

- `.github/workflows/multi-agent-artifact-handoff.yml`
- `.github/agents/consolidator.agent.md`
- `artifacts/consolidated-operator-report.json`
- `labs/lab-07-multi-agent-handoff.md`

### Artifact-Reading Skills

- trace handoffs from one job/agent to another
- verify that downstream jobs consume the correct artifacts
- detect conflicting outputs
- evaluate isolation boundaries for parallel work

### Example Failure Modes

- two agents edit the same file in incompatible ways
- downstream reviewer consumes stale builder artifact
- consolidator omits a security finding
- one failed agent is hidden by a successful final job

## 6. Implement Guardrails and Accountability

### Practical Meaning

Classify risk, enforce least privilege, block unsafe actions, require approvals, and preserve audit evidence.

### Repo Artifacts

- `.github/hooks/preToolUse-deny-execute.example.json`
- `.github/hooks/postToolUse-add-context.example.json`
- `.github/workflows/security-gate.yml`
- `docs/guardrails-and-accountability.md`
- `org-governance/agent-release-checklist.md`

### Artifact-Reading Skills

- determine whether an action required human approval
- inspect hook decisions
- verify audit evidence exists
- evaluate whether permissions match risk

### Example Failure Modes

- high-risk action lacks explicit approval
- artifact deleted before review
- hook denies a tool but workflow continues as if successful
- permissions are broader than the job requires
