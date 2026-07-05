# Multi-Agent Coordination Governance

## Coordination Is Not Consensus

Multiple agent outputs agreeing with each other does not prove correctness. Agents can inherit assumptions, summarize each other, or miss the same blind spot.

## Semantic Compression Loss

Consolidator agents can flatten nuanced findings into clean summaries. Conditional approval, rare edge cases, unresolved risk, and minority dissent must survive consolidation.

## Consensus Illusion and Groupthink Loops

Sequential agents may treat upstream assumptions as facts:

- Planner assumes
- Builder builds from the assumption
- Reviewer reviews only the Builder's summary
- Security auditor sees the same narrowed context
- Consolidator reports consensus

The safe pattern is adversarial independence where downstream agents inspect raw evidence when needed.

## State Squashing and Chain of Custody

Merging many JSON or Markdown outputs into a final report can drop metadata:

- Timestamps
- Run IDs
- Branch names
- Commit SHAs
- Source artifact names
- Agent role boundaries
- Conditional approval codes
- Unresolved findings
- Provenance hashes or evidence references

This repository uses fake hashes and provenance metadata only. It does not implement real cryptographic signing. Signatures may be useful as an optional higher-assurance production control.

## Deterministic Merge Rules

Some top-level decisions should be computed deterministically instead of summarized by an LLM.

Examples:

- If any upstream artifact has `critical` risk, final status cannot be `approved`.
- If any upstream artifact has unresolved findings, final status must be `review_required` or `human_escalation_required`.
- If security approval is conditional, final status must preserve that condition.
- If dissent exists, final report must include it.

## Safe Operator Checklist

- Did the consolidator preserve dissent?
- Did it preserve conditional approvals?
- Did it independently verify raw evidence when required?
- Did it avoid downgrading risk language?
- Did it preserve run ID, branch, commit SHA, and source artifact references?
- Did it use deterministic rules for global status?
- Did existence checks get confused with structural or semantic validation?
- Does the final report prove what was lost, preserved, or escalated?
