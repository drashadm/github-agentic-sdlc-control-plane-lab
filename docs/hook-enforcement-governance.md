# Hook Enforcement Governance

## Why Hooks Matter

Hooks sit between model intent and tool execution. They are where probabilistic intent can be constrained by deterministic policy before a requested action reaches the execution layer.

## Advisory Controls vs. Enforced Controls

Different controls have different strength:

- A warning tells the operator or agent about risk.
- A log event preserves evidence.
- A model instruction asks the model to behave safely.
- An ask or approval request pauses for human judgment.
- A deterministic deny blocks the tool call.
- A deterministic rewrite changes the request before it reaches the tool.
- A deterministic escalation routes the request to a stronger review path.

Only enforced controls can reliably stop a tool call before execution.

## Semantic Intent Beats String Matching

Agents may repackage the same unsafe intent in different forms. A guardrail should evaluate the requested capability, target resource, scope, and risk rather than relying only on brittle string matching. For example, a request summarized as `[blocked destructive command]`, `[obfuscated destructive file operation]`, or `[blocked file deletion intent]` should map to the same high-risk capability if the target and effect are equivalent.

## Approval-to-Payload Binding

Human approval should be bound to a specific operation or payload summary, not a vague capability. In higher-assurance systems, approval may be tied to a payload hash, run ID, branch, commit SHA, and expiration window. This lab uses fake educational values only.

## Time-of-Check to Time-of-Use Risk

A request can change between validation and execution if the approved payload, script, artifact, or target file is mutable. The safe control is to bind approval to immutable evidence and re-check immediately before execution.

## Fail-Open vs. Fail-Closed

Fail-open means the tool call proceeds when policy is missing, unclear, crashed, or unavailable. Fail-closed means the tool call is blocked until policy can verify it. High-risk tool calls should fail closed.

## Hook Tampering and Bypass Risk

Hook files and runner policy files are control-plane assets. If an agent or contributor can modify them without review, the guardrail can be weakened or removed.

Safe examples of bypass risk include:

- Hook file changed without CODEOWNERS review
- Alternate workflow path bypasses the hook layer
- `postToolUse` logs context but cannot prevent a completed action
- CLI-only permission request is mistaken for cloud enforcement

## Enforcement Plane Isolation

Stronger systems may run policy evaluation outside the agent's mutable runtime. The concept is to prevent the agent from changing the policy that governs it. Production environments may use higher-assurance runtime controls such as security sidecars or operating-system enforcement layers, but this repository does not implement kernel enforcement, eBPF, seccomp, or a real security sidecar.

## Decision Evidence

Hook decisions should produce evidence:

- Session ID
- Tool name
- Requested operation summary
- Interpreted capability
- Decision
- Reason
- Policy rule
- Run ID
- Branch
- Commit SHA
- Approval state
- Payload hash or immutable evidence reference where applicable

## Safe Operator Checklist

- Did the hook enforce or only advise?
- Did it evaluate capability intent, not only strings?
- Did it fail closed?
- Was approval bound to the exact operation?
- Was the hook file protected?
- Was the decision logged?
- Was the tool call blocked before execution?
- Could another path bypass the hook?
- Is human approval required for high-risk override?
