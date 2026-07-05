# Lab 05: Hook Permission Decision

## Difficulty

Intermediate.

## Estimated Time

15-20 minutes.

## Scenario

A pre-tool hook receives a request for a high-risk execution action against repository artifacts. The visible event shows a deny decision, but the deeper question is whether the hook actually mediated execution before the tool call reached the execution layer.

In agentic workflows, hooks are not just logging helpers or static string filters. They are deterministic mediation points between probabilistic model intent and system-level tool execution. A strong hook must reason about the requested capability, bind approval to the exact payload or operation, fail closed under ambiguity, and preserve tamper-resistant evidence.

## Artifacts to Inspect

- `.github/hooks/preToolUse-deny-execute.example.json`
- `.github/hooks/preToolUse-rewrite-args.example.json`
- `.github/hooks/postToolUse-add-context.example.json`
- `.github/hooks/permissionRequest-cli-only.example.json`
- `.github/workflows/agent-runner-educational.yml`
- `artifacts/intent-analysis-payload.json`
- `artifacts/hook-enforcement-report.json`
- `artifacts/hook-approval-binding-report.json`
- `schemas/intent-analysis-payload.schema.json`
- `schemas/hook-enforcement-report.schema.json`
- `schemas/hook-approval-binding-report.schema.json`
- `docs/hook-enforcement-governance.md`
- `docs/guardrails-and-accountability.md`
- `docs/workflow-validation-guide.md`
- `docs/agentic-threat-model-map.md`
- `docs/risk-to-github-mitigation-map.md`

## What You Are Looking For

Look for:

- `preToolUse` versus `postToolUse` timing
- Deny, allow, rewrite, escalate, and advisory decisions
- Fail-open versus fail-closed behavior
- Semantic intent mapping from raw request to capability, target, scope, and risk
- String matching limitations
- Approval-to-payload binding
- Time-of-check to time-of-use risk
- Hook tampering or unreviewed hook file changes
- Protected hook files and required review
- CLI-only permission request versus cloud-agent enforcement
- Evidence that a tool call was blocked before execution
- Whether a blocked action still appears as workflow success
- Bypass paths around hooks, including alternate workflows or tool paths
- Whether human override is explicit, scoped, expiring, and auditable

## Questions

1. Why is a `postToolUse` hook insufficient to prevent a dangerous action?
2. What evidence proves that `preToolUse` blocked the tool call before execution?
3. What is the difference between an advisory warning and an enforced deny decision?
4. Why is static string matching weaker than capability-level intent analysis?
5. If a human approves a high-risk tool call, why should the approval be bound to the exact operation, run ID, branch, commit SHA, and payload hash?
6. What is the time-of-check to time-of-use risk if the approved file or payload can change after approval?
7. Why should high-risk tool calls fail closed if the hook policy is missing, unavailable, or ambiguous?
8. How could an agent or contributor weaken the guardrail if hook files are not protected?
9. Why is a CLI-only permission request not automatically equivalent to cloud-agent enforcement?
10. What should happen if the hook blocks a command but the workflow still reports success?

## Expected Reasoning Path

Start with `.github/hooks/preToolUse-deny-execute.example.json`. The event type is `preToolUse`, which means the decision is intended to happen before execution. The requested tool is `execute`, the policy rule matched, and the permission decision is `deny`. Because the command is represented by a safe placeholder, the artifact teaches the control decision without preserving a copy-pasteable dangerous operation.

Next compare this with `.github/hooks/postToolUse-add-context.example.json`. A `postToolUse` event can add context or preserve evidence after a tool call, but it cannot prevent an action that already completed. Then compare `.github/hooks/preToolUse-rewrite-args.example.json`, which models a deterministic rewrite, and `.github/hooks/permissionRequest-cli-only.example.json`, which teaches that a CLI permission pattern is not automatically cloud-agent enforcement.

Then inspect `artifacts/intent-analysis-payload.json`. A strong hook should reason about capability intent, target resource, scope, risk, matched rules, approval requirement, and safe next action rather than only raw strings. Finally, inspect `artifacts/hook-enforcement-report.json` and `artifacts/hook-approval-binding-report.json` to verify enforcement evidence, bypass risks, protected control-plane files, approval scope, payload hash, run ID, branch, commit SHA, and mutation status.

## Answer Key

1. `postToolUse` runs after the tool call, so it can observe, annotate, or report but cannot stop a completed action.
2. Evidence includes the `preToolUse` event, requested tool, interpreted capability, matched policy rule, deny decision, reason, run ID, branch, commit SHA, and an enforcement report showing no execution occurred.
3. An advisory warning informs the agent or operator but may allow the call to proceed. An enforced deny blocks the call before the execution layer receives it.
4. Static strings are brittle. The same unsafe intent can be repackaged as a different summary, helper action, generated script, alternate tool call, or indirect operation. Capability analysis evaluates intent, target, scope, and risk.
5. Binding approval to exact evidence prevents broad approvals from being reused for a different operation. The approval should match the operation summary, run, branch, commit, payload hash, and expiration window.
6. If the payload or target changes after approval, the original human judgment no longer applies. The hook should re-check immediately before execution and block on mismatch.
7. If policy is missing, unavailable, or ambiguous, allowing high-risk execution creates a fail-open path. High-risk tool calls should block until policy can verify the request.
8. If hook files are not protected, an agent or contributor can weaken, remove, or bypass the guardrail through an ordinary repository change.
9. CLI permission requests may guide a local runtime, but they do not prove that a cloud agent, workflow, or alternate execution path enforces the same decision.
10. Treat the workflow result as invalid, fail the run, preserve hook evidence, and fix the workflow so blocked tool calls propagate as blocking status.

## Common Wrong Answers

- Treating a hook warning as equivalent to an enforced deny.
- Assuming `postToolUse` can prevent a completed action.
- Approving a broad class of actions instead of one exact operation.
- Trusting raw string matching while ignoring equivalent capability intent.
- Allowing execution when hook policy is missing or ambiguous.
- Treating CLI-only permission prompts as proof of cloud-agent enforcement.
- Ignoring hook file protection and alternate workflow bypass paths.

## Safe Operator Decision

Block the action unless a pre-execution hook can prove deterministic enforcement for the exact requested capability, target resource, payload, run ID, branch, commit SHA, and approval state. Require protected hook files, fail-closed policy behavior, scoped and expiring human overrides, and durable evidence that blocked tool calls cannot be reported as successful workflow execution.

## Agentic Nuance

Pre-tool hooks are the last deterministic checkpoint before probabilistic agent intent becomes system action. Treating hooks as simple pattern-matching scripts misses the primary failure mode of LLM tool use: the model can repackage the same intent in different surface forms.

A blocked request may reappear as a rewritten command, a generated script, a different tool call, or an apparently harmless helper action with the same risky capability. The control plane should therefore evaluate capability intent, target resource, scope, approval state, and policy, not only raw strings.

Human approval also creates a state-binding problem. An approval that says "allow this kind of action" is weaker than approval bound to one exact operation, run ID, branch, commit SHA, and payload hash. Without that binding, the action can drift between approval and execution.

The safe control is deterministic hook enforcement: fail-closed policy evaluation, protected hook files, scoped human overrides, immutable decision evidence, and execution boundaries that prevent the agent from modifying the guardrail that governs it.

## Portfolio Signal

This lab demonstrates production-grade thinking about runtime guardrails for probabilistic agent behavior. It shows the ability to distinguish advisory policy from enforceable control, reason about semantic intent rather than raw command strings, and design approval mechanisms that bind human judgment to exact execution evidence.

A reviewer should come away understanding that the engineer can reason beyond "does a hook exist?" and ask the more important question: "Did this hook actually mediate the intended capability before the agent could act?"
