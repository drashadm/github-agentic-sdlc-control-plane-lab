# Multi-Agent Coordination Patterns

## Pattern 1: Planner → Builder → Reviewer → Security Auditor → Consolidator

Use when a change needs structured design, implementation, correctness review, security review, and final operator synthesis.

### Strengths

- clear separation of responsibility
- reviewable handoffs
- strong audit story

### Risks

- slow if every step requires manual review
- downstream jobs can consume stale artifacts
- consolidator may omit dissenting findings

### Required Artifacts

- planner output
- builder diff summary
- reviewer findings
- security audit report
- consolidated operator report

## Pattern 2: Parallel Reviewers with Consolidation

Use when multiple review perspectives are needed.

### Strengths

- catches more failure modes
- allows specialization

### Risks

- contradictory findings
- duplicated effort
- unclear final authority

### Safe Control

The consolidator must explicitly list conflicts and unresolved findings.

## Pattern 3: Human-Gated Executor

Use when an agent proposes an action that changes state.

### Strengths

- allows speed while preserving judgment
- useful for high-risk changes

### Risks

- approval fatigue
- rubber-stamping

### Safe Control

Only high-risk actions require human approval. Low-risk read-only actions should stay fast.
