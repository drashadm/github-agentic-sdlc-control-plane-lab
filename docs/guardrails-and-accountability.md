# Guardrails and Accountability

## Control Philosophy

Agents can accelerate software delivery, but acceleration without accountability creates invisible risk. This lab treats GitHub as the control plane where agent intent, capability, execution, evidence, and approval are visible.

```text
Agents propose.
GitHub records.
Workflows enforce.
Artifacts prove.
Hooks constrain.
Humans approve high-risk action.
```

## Autonomy Levels

| Level | Description | Example | Required Control |
|---|---|---|---|
| 0 | Read-only analysis | Summarize repository structure | Logs only |
| 1 | Plan generation | Create implementation plan | Structured artifact |
| 2 | Proposed file changes | Draft PR changes | Review gate |
| 3 | Command execution | Run tests or build commands | Hook + workflow logs |
| 4 | External system action | Call MCP tool or remote system | Allowlist + approval |
| 5 | Irreversible or compliance-sensitive action | Deploy, delete, rotate, publish | Explicit human authorization |

## Planning vs Execution Boundaries

Planning answers:

- What should be done?
- Why should it be done?
- What files or systems might be affected?
- What risks are known?
- What evidence will prove success?

Execution changes state. Execution should be narrower than planning and should be gated by:

- branch scope
- tool scope
- workflow permissions
- review requirements
- audit artifacts

## Least Privilege

Each agent should have the least capability needed.

A reviewer should not need `edit` or `execute`. A planner may need `edit` only to write a plan artifact. An executor with `execute` access should be treated as high risk.

## Scoped Tools

Tool lists are governance declarations. They should be reviewed like code.

Questions to ask:

- Does this role need the listed tool?
- Could this tool mutate state?
- Could this tool reach external systems?
- Is there a narrower alternative?
- Is the expected output inspectable?

## MCP Risk

MCP can extend agent capability. That makes it powerful and risky.

Risk factors:

- broad wildcard access such as `server/*`
- unclear server identity
- remote server transport without trust review
- environment variables or credentials exposed to the process
- tool behavior that is not logged or artifacted
- allowlists treated as complete security boundaries

## Workflow Artifacts as Evidence

A workflow artifact should answer:

- What did the agent intend to do?
- What did it produce?
- Who or what reviewed it?
- What risk was identified?
- What decision was made?
- What remains unresolved?

## Logs as Accountability Records

Logs are not just debugging output. They are accountability records.

Useful logs should include:

- session ID
- job ID or run ID
- branch/ref
- tool name
- tool arguments where safe
- approval state
- artifact path
- error code
- safe next action

## Human-in-the-Loop Gates

Human review should be reserved for actions where judgment materially reduces risk.

Require human approval for:

- production-impacting changes
- workflow/permission changes
- secret or credential handling
- external system writes
- deletion or irreversible actions
- high-risk MCP access expansion

Avoid unnecessary approvals for:

- read-only summarization
- non-mutating repository search
- local plan generation
- low-risk artifact generation

## Fail-Closed Behavior

Sensitive workflows should fail closed.

Fail-open behavior says: “If unsure, proceed.”

Fail-closed behavior says: “If unsure, stop and ask for review.”

In agentic SDLC systems, fail-closed is preferred when:

- permissions are ambiguous
- artifacts are missing
- outputs fail schema validation
- branch scope is wrong
- memory conflicts with current state
- hook decisions are unclear
- security findings are unresolved

## Auditability as a Feature

Auditability should be designed into the system, not added after a failure.

An auditable agent workflow preserves:

- instructions
- agent profile
- tool scope
- MCP configuration
- branch/ref
- workflow run
- logs
- artifacts
- approvals
- final decision
