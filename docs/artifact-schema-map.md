# Artifact Schema Map

Governed agent systems should produce structured artifacts because artifacts are the durable record of intent, scope, review, risk, and operator decision-making. Conversation history can disappear or become detached from the repository. Structured files can be reviewed, versioned, linked from workflows, and compared over time.

Schemas make those artifacts inspectable contracts. They define the minimum shape a downstream reviewer or workflow can expect before trusting an artifact enough to read it. Schema validation helps detect missing fields, stale handoffs, incomplete reports, and hidden risk that would otherwise be buried in prose or omitted entirely.

Schema validation does not prove an agent was correct. It proves the artifact is complete enough to review and that downstream jobs can rely on its shape before applying human judgment to its contents.

| Artifact | Schema | Purpose |
| -------- | ------ | ------- |
| `artifacts/planner-output.json` | `schemas/planner-output.schema.json` | Captures request scope, affected files, success criteria, risks, and whether execution needs approval. |
| `artifacts/builder-diff-summary.json` | `schemas/builder-diff-summary.schema.json` | Records what changed, which plan it followed, assumptions made, and known gaps left open. |
| `artifacts/reviewer-findings.json` | `schemas/reviewer-findings.schema.json` | Preserves review outcome, plan alignment, findings, and approval recommendation. |
| `artifacts/security-audit-report.json` | `schemas/security-audit-report.schema.json` | Captures permission, MCP, approval, and audit evidence status for security review. |
| `artifacts/consolidated-operator-report.json` | `schemas/consolidated-operator-report.schema.json` | Combines consumed artifacts, final decision, unresolved risks, and the next safe action. |
| `artifacts/agent-handoff-valid-v2.json` | `schemas/agent-handoff-v2.schema.json` | Demonstrates a valid advanced agent handoff with provenance, output files, risk flags, context budget, and validation status. |
| `artifacts/planner-context-raw-malformed.json` | `schemas/agent-handoff-v2.schema.json` | Intentionally malformed artifact for teaching schema drift and silent-success risk; it should parse as JSON but fail the expected handoff schema. |
| `artifacts/workflow-validation-report.json` | `schemas/workflow-validation-report.schema.json` | Preserves workflow review evidence before downstream agent execution. |
| `artifacts/agent-profile-review-report.json` | `schemas/agent-profile-review-report.schema.json` | Preserves evidence from reviewing agent profile and control-plane file changes. |
