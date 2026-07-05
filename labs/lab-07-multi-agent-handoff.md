# Lab 07: Multi-Agent Handoff

## Difficulty

Advanced.

## Estimated Time

20-25 minutes.

## Scenario

A Planner, Builder, Reviewer, Security Auditor, and Consolidator all produce artifacts. The final operator report compiles successfully, but the operator must decide whether it preserved the important upstream findings or flattened them into a clean but misleading status.

Multi-agent coordination is not just agents passing files. It is authority routing, dissent preservation, conflict resolution, provenance tracking, and final-decision governance. A final operator report is valid only if it preserves high-fidelity evidence from upstream agents, surfaces internal disagreement, retains conditional approvals, and proves that the consolidator did not compress nuanced findings into a false approval.

## Artifacts to Inspect

- `artifacts/planner-output.json`
- `artifacts/builder-diff-summary.json`
- `artifacts/reviewer-findings.json`
- `artifacts/security-audit-report.json`
- `artifacts/consolidated-operator-report.json`
- `artifacts/multi-agent-manifest.json`
- `artifacts/consolidation-fidelity-report.json`
- `.github/workflows/consolidated-operator-report.yml`
- `schemas/planner-output.schema.json`
- `schemas/builder-diff-summary.schema.json`
- `schemas/reviewer-findings.schema.json`
- `schemas/security-audit-report.schema.json`
- `schemas/consolidated-operator-report.schema.json`
- `schemas/multi-agent-manifest.schema.json`
- `schemas/consolidation-fidelity-report.schema.json`
- `docs/multi-agent-coordination-governance.md`
- `docs/state-serializability.md`
- `docs/workflow-validation-guide.md`
- `docs/advanced-agentic-failure-modes.md`
- `docs/guardrails-and-accountability.md`

## What You Are Looking For

Look for:

- Semantic compression loss
- Lossy consolidation
- Conditional approvals flattened into binary status
- Dissent erased during summary
- Reviewer concerns summarized away
- Security findings downgraded
- Multi-agent consensus mistaken for correctness
- Sequential blind spots
- Reviewer relying on Builder summary instead of raw diff or primary evidence
- State squashing when JSON outputs are merged
- File existence checks versus schema validation versus semantic fidelity
- Provenance metadata preservation
- Deterministic global-status merge rules
- Final report as evidence, not just a dashboard

## Questions

1. Why is a final consolidated report not automatically trustworthy just because all upstream artifact files exist?
2. What is semantic compression loss, and why is it dangerous in a Consolidator Agent?
3. If a security artifact says "approve only after out-of-band validation," why is it unsafe for the final report to summarize this as "approved with mild warnings"?
4. How can a reviewer be misled if it reviews only the Builder Agent's summary instead of raw diffs or primary evidence?
5. What is the difference between structural schema validation and semantic fidelity validation?
6. Which metadata must survive consolidation to preserve chain of custody across agents?
7. Why should dissent or conditional approval force `human_escalation_required` or `review_required` instead of `approved`?
8. What deterministic merge rule should override the consolidator if any upstream artifact contains critical risk, unresolved findings, or conditional approval?
9. Which artifact should show whether the final report preserved or omitted important upstream findings?
10. What should the operator do if the final report is structurally valid but semantically lossy?

## Expected Reasoning Path

Start with `artifacts/consolidated-operator-report.json` and verify the final report lists upstream artifacts and unresolved risks. Then do not stop there. File presence and a valid top-level schema only prove that a report exists and has a reviewable shape; they do not prove it faithfully preserved upstream meaning.

Next compare upstream evidence. `artifacts/reviewer-findings.json` contains `approve_after_security_review`, which is conditional approval. `artifacts/security-audit-report.json` contains human approval requirements for executor execution, broad MCP expansion, and workflow permission changes. A safe consolidator must preserve those conditions rather than compressing them into a clean approval.

Then inspect `artifacts/multi-agent-manifest.json`. It records agent roles, upstream artifact status, dissent items, conditional approvals, unresolved findings, and deterministic consolidation rules. If any upstream artifact contains conditional approval, unresolved findings, critical risk, or missing provenance, the global status cannot be plain `approved`.

Finally inspect `artifacts/consolidation-fidelity-report.json`. This artifact checks whether findings were preserved, omitted, downgraded, or reduced to file-existence checks. If semantic fidelity is `review_required` or `blocked`, the final operator report should not be treated as a trustworthy approval artifact.

## Answer Key

1. Existence only proves files are present. It does not prove they are current, schema-valid, provenance-bound, or semantically preserved.
2. Semantic compression loss happens when detailed findings are summarized so aggressively that conditions, dissent, severity, provenance, or unresolved risks disappear.
3. Conditional approval is not approval. Compressing it into mild warnings erases the required validation step and can let unsafe work proceed.
4. The Builder summary may omit assumptions, raw diffs, or edge cases. A Reviewer who only reviews the summary may inherit the Builder's blind spots.
5. Structural schema validation checks required fields and types. Semantic fidelity validation checks whether the meaning, risk, dissent, and conditions survived consolidation.
6. Run ID, branch, commit SHA, timestamps, source artifact names, agent roles, source evidence references, conditional approval codes, unresolved findings, and provenance hashes or fake evidence references should survive.
7. Dissent and conditional approval mean the system has not reached clean approval. The safe global status is `review_required` or `human_escalation_required`.
8. If any upstream artifact has critical risk, unresolved findings, conditional approval, or missing provenance, final status must block full approval and escalate to human review.
9. `artifacts/consolidation-fidelity-report.json` should show preserved findings, omitted findings, downgrades, dissent preservation, and semantic fidelity status.
10. Block final approval, preserve the lossy report as evidence, regenerate from current upstream artifacts, and require human review of omitted or downgraded findings.

## Common Wrong Answers

- Treating a final report as authoritative because it has a `decision` field.
- Equating file existence with artifact integrity.
- Treating schema validity as proof that risk was preserved.
- Ignoring conditional approval language.
- Assuming multiple agents agreeing proves correctness.
- Letting the Consolidator downgrade security findings for readability.
- Dropping run ID, branch, commit SHA, or source artifact references during merge.

## Safe Operator Decision

Block final approval unless the consolidated report preserves dissent, conditional approvals, unresolved findings, provenance metadata, and deterministic global-status rules. If the final report omits or downgrades upstream risk, require human escalation and regenerate the report from current artifacts.

## Agentic Nuance

Multi-agent systems are vulnerable to semantic compression loss and consensus illusion. A final Consolidator Agent may ingest detailed Planner, Builder, Reviewer, and Security outputs, then compress nuanced findings into a clean dashboard status. Conditional approvals, rare edge cases, unresolved risks, and dissent can disappear because the summarizer optimizes for brevity.

Sequential agent pipelines can also create groupthink loops. If the Planner makes an unverified assumption, the Builder may treat it as the task baseline, the Reviewer may inspect only the Builder's summary, and the Consolidator may report structural agreement. The system appears coordinated even though no agent independently challenged the original premise.

State squashing makes this worse. When multiple artifacts are merged into one report, source metadata, run IDs, branch names, commit SHAs, timestamps, role boundaries, and conditional approval codes can be dropped. Once that chain of custody is lost, the final report becomes a polished narrative rather than reliable governance evidence.

The safe control is high-fidelity consolidation. The workflow should preserve dissent, conditional findings, provenance metadata, and unresolved risks. Global approval status should be computed by deterministic rules: any critical risk, unresolved finding, missing provenance, or conditional approval must block full approval or escalate to human review.

## Portfolio Signal

This lab demonstrates production-grade thinking about governing decoupled multi-agent architectures. It shows the ability to detect semantic loss, consensus illusion, lossy JSON merging, and final-report overreach.

A reviewer should come away understanding that the engineer can reason beyond "did the agents agree?" and ask the more important question: "Did the final report preserve dissent, provenance, and conditional risk accurately enough for a human operator to trust it?"
