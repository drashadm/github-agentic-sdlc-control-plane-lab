# Schema and Semantic Validation Governance

## Schema Validity Is Not Truth

JSON Schema validates shape, type, required fields, and structural expectations. It can prove that an artifact is parseable and has the minimum expected contract.

It does not prove content quality, truth, freshness, completeness, specificity, or safety. A schema-valid artifact can still be misleading enough to block downstream agent execution.

## Schema-Compliant Confabulation

An LLM can satisfy required fields with generic, hallucinated, stale, or low-value content. The artifact can be parseable and schema-valid while still being useless or unsafe.

Safe examples include:

- "Make sure it works"
- "No issues found"
- "None"
- "Looks good"

These phrases may be valid strings, but they are weak evidence when a field is supposed to preserve engineering judgment, risk, or review outcome.

## Semantic Nulls

Semantic nulls are valid strings or arrays that carry no actionable engineering evidence.

Examples include:

- success criteria with generic filler
- unresolved risks listed as "None" despite upstream findings
- decision reason that says "approved" without evidence
- summary field that omits the actual condition

## Schema-Induced Omission

Strict schemas can unintentionally encourage agents to drop complex nuance if the structure has no place for it. Conditional approvals, rare edge cases, or multidimensional risks may be compressed into simple strings.

That compression can make the artifact easier to validate but less faithful to the evidence it was supposed to preserve.

## Type Coercion and Downstream Over-Trust

Agents may coerce complex errors, caveats, or objects into strings to satisfy a schema. A downstream agent may then trust the value because validation passed.

This creates a false certainty problem: the artifact is structurally acceptable, but the content no longer carries enough detail for safe automation.

## Dual-Layer Validation

Safer validation layers include:

- JSON parse validation
- JSON Schema validation
- content specificity checks
- disallowed generic phrase checks
- cross-artifact consistency checks
- provenance/current-run checks
- deterministic escalation rules
- human review for conflicting decisions

Production systems may add LLM-based graders or semantic scanners for higher assurance. This repository models deterministic evidence and governance patterns only; it does not implement those scanners.

## Safe Operator Checklist

- Did the artifact parse?
- Did it pass schema validation?
- Are the required fields specific and actionable?
- Are any fields semantic nulls?
- Did any risk language get downgraded?
- Does the artifact conflict with upstream reports?
- Are run ID, branch, and commit SHA preserved?
- Should downstream agents be blocked until semantic validation passes?
