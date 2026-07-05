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
| `artifacts/mcp-boundary-review-report.json` | `schemas/mcp-boundary-review-report.schema.json` | Preserves evidence from reviewing MCP tool boundaries and agent authority expansion. |
| `artifacts/git-state-snapshot.json` | `schemas/git-state-snapshot.schema.json` | Preserves mocked branch and commit continuity evidence for resumed session review. |
| `artifacts/session-continuity-report.json` | `schemas/session-continuity-report.schema.json` | Preserves evidence that resumed session state, memory, permissions, prior errors, and approval status were reviewed. |
| `artifacts/intent-analysis-payload.json` | `schemas/intent-analysis-payload.schema.json` | Preserves pre-tool semantic intent analysis evidence before hook-mediated execution. |
| `artifacts/hook-enforcement-report.json` | `schemas/hook-enforcement-report.schema.json` | Preserves evidence that hook decisions enforced, rewrote, advised, or blocked tool calls. |
| `artifacts/hook-approval-binding-report.json` | `schemas/hook-approval-binding-report.schema.json` | Preserves evidence that human approval was bound to an exact operation, payload hash, run, branch, and commit. |
| `memory/memory-vector-index.lock.json` | N/A | Preserves mocked memory index freshness evidence and whether long-term memory matches current repository head. |
| `artifacts/memory-validation-report.json` | `schemas/memory-validation-report.schema.json` | Preserves evidence that memory facts were source-checked, freshness-checked, allowed, or quarantined before context injection. |
| `artifacts/memory-authority-review-report.json` | `schemas/memory-authority-review-report.schema.json` | Preserves evidence separating agent belief from runtime authorization. |
| `artifacts/multi-agent-manifest.json` | `schemas/multi-agent-manifest.schema.json` | Preserves multi-agent provenance, role boundaries, dissent, conditional approvals, and deterministic global-status state. |
| `artifacts/consolidation-fidelity-report.json` | `schemas/consolidation-fidelity-report.schema.json` | Preserves evidence that final consolidation retained upstream findings, dissent, conditional risk, and semantic fidelity. |
| `artifacts/planner-state-manifest.json` | `schemas/planner-state-manifest.schema.json` | Teaches state serializability and deterministic planner-to-builder handoffs. |
| `artifacts/stale-agent-state-cache-example.json` | `schemas/stale-agent-state-cache-example.schema.json` | Demonstrates stale context risk when downstream agents fall back to previous-run state. |
| `logs/reviewer-scratchpad.json` | `schemas/reviewer-scratchpad.schema.json` | Demonstrates separation between simulated internal reviewer scratchpad state and approved public output fields. |
| `artifacts/reviewer-note-leakage-report.json` | `schemas/reviewer-note-leakage-report.schema.json` | Preserves evidence that reviewer notes, draft residue, hidden instruction placeholders, and private context references were checked before publication. |
| `artifacts/publication-readiness-report.json` | `schemas/publication-readiness-report.schema.json` | Records whether a public artifact passed output serialization, internal-field exclusion, leakage, and promotion-readiness checks. |
| `artifacts/schema-semantic-validation-report.json` | `schemas/schema-semantic-validation-report.schema.json` | Preserves evidence for structural validation, semantic validation, generic filler detection, semantic null detection, and cross-artifact consistency checks. |
| `schemas/schema-semantic-validation-report.schema.json` | N/A | Defines the educational contract for schema-versus-semantic validation reports. |
| `artifacts/validation-telemetry.log` | N/A | Shows a safe validation trace where JSON parsing and schema checks pass while semantic and cross-artifact gates block downstream automation. |
| `artifacts/pipeline-execution-checkpoint.json` | `schemas/pipeline-execution-checkpoint.schema.json` | Preserves evidence comparing GitHub Actions runner success with internal agent runtime completion before upload. |
| `schemas/pipeline-execution-checkpoint.schema.json` | N/A | Defines the educational contract for runner-state versus agent-runtime checkpoints. |
| `artifacts/artifact-transaction-report.json` | `schemas/artifact-transaction-report.schema.json` | Preserves artifact transaction readiness evidence, including file size, parse/schema/semantic status, record counts, fake digest, and gate decisions. |
| `schemas/artifact-transaction-report.schema.json` | N/A | Defines the educational contract for artifact completeness and transaction-readiness reports. |
| `artifacts/artifact-provenance-manifest.json` | `schemas/artifact-provenance-manifest.schema.json` | Preserves provenance-bound downstream consumption evidence for run, branch, commit, workflow, job, producing agent, artifact name, and fake digest. |
| `schemas/artifact-provenance-manifest.schema.json` | N/A | Defines the educational contract for provenance manifests used in agent handoff review. |
| `artifacts/billing-and-token-telemetry.json` | `schemas/billing-and-token-telemetry.schema.json` | Preserves fake retry, token, cost, context-growth, and stop-condition evidence for silent failure loops. |
| `schemas/billing-and-token-telemetry.schema.json` | N/A | Defines the educational contract for retry and token budget accountability artifacts. |
| `artifacts/zombie-pipeline-failure-report.json` | `schemas/zombie-pipeline-failure-report.schema.json` | Preserves evidence that visible pipeline success hid collapsed agentic state and zero-work processing. |
| `schemas/zombie-pipeline-failure-report.schema.json` | N/A | Defines the educational contract for Zombie Pipeline detection reports. |
| `artifacts/compound-handoff-failure-report.json` | `schemas/compound-handoff-failure-report.schema.json` | Preserves capstone chain-of-trust review evidence across schema, semantic, memory, artifact, tool, hook, retry, consolidation, and human approval layers. |
| `schemas/compound-handoff-failure-report.schema.json` | N/A | Defines the educational contract for compound handoff failure reports. |
