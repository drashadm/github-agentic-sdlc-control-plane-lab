# Lab 09: Schema Validation Failure

## Difficulty

Intermediate.

## Estimated Time

25-30 minutes.

## Scenario

A planner artifact passes JSON parsing and satisfies its JSON Schema. The required fields exist, `success_criteria` is an array, and the consolidated operator report has an `unresolved_risks` field. A shallow workflow gate would allow downstream automation to continue.

The deeper problem is that shape is not truth. A schema-valid artifact can still contain generic filler, hallucinated content, stale decisions, downgraded risk language, type-coerced values, semantic nulls, or omissions that mislead downstream agents and human operators.

Passing schema validation only proves that the artifact has the expected shape. It does not prove that the content is true, current, complete, specific, safe, or decision-ready.

## Artifacts to Inspect

- `artifacts/planner-output.json`
- `artifacts/reviewer-findings.json`
- `artifacts/consolidated-operator-report.json`
- `artifacts/schema-semantic-validation-report.json`
- `artifacts/validation-telemetry.log`
- `schemas/planner-output.schema.json`
- `schemas/reviewer-findings.schema.json`
- `schemas/consolidated-operator-report.schema.json`
- `schemas/schema-semantic-validation-report.schema.json`
- `docs/artifact-schema-map.md`
- `docs/schema-semantic-validation-governance.md`
- `docs/multi-agent-coordination-governance.md`
- `docs/advanced-agentic-failure-modes.md`
- `docs/workflow-validation-guide.md`
- `docs/guardrails-and-accountability.md`

## What You Are Looking For

Check required fields, artifact purpose, and the difference between structural validation and semantic validation. A schema can prove that required fields exist, but it cannot prove that the agent made a correct decision, preserved every important risk, or produced specific engineering evidence.

Look for:

- structural validation versus semantic validation
- schema-compliant confabulation
- semantic nulls
- generic filler inside valid fields
- schema-induced omission
- strict JSON mode prioritizing structural compliance over analytical completeness
- type coercion into strings
- consolidated reports saying "None" while upstream artifacts contain risks
- required fields that are present but misleading
- risk values downgraded while still schema-valid
- downstream over-trust
- cross-artifact consistency checks
- schema version drift if producer and consumer expectations diverge
- deterministic escalation when schema-valid content conflicts with upstream evidence

## Questions

1. Why does passing JSON Schema validation not prove an artifact is true, complete, or safe to act on?
2. What is schema-compliant confabulation?
3. If `success_criteria` exists and is an array, why might it still fail semantic validation?
4. What is a semantic null, and why can it pass structural validation?
5. If `consolidated-operator-report.json` says `unresolved_risks: ["None"]` while an upstream report contains an unresolved risk, what validation layer should catch the conflict?
6. How can strict JSON schemas cause an agent to omit complex or conditional findings?
7. Why is type coercion dangerous when downstream agents treat schema-valid values as verified truth?
8. What should happen before downstream automation consumes an artifact that is structurally valid but semantically weak?

## Expected Reasoning Path

Start with the schema required fields and compare them to the artifact. If a required field is missing, the handoff is incomplete and downstream review should stop. If the artifact passes schema validation, do not treat that as approval. Treat it as the first gate.

Next inspect `artifacts/schema-semantic-validation-report.json` and `artifacts/validation-telemetry.log`. These artifacts show how structural checks can pass while content checks still require review: generic success criteria, semantic nulls such as `"None"`, type-coerced summaries, and cross-artifact conflicts.

Then compare the planner and consolidated operator report with upstream evidence. If an upstream artifact records unresolved risk but the final report compresses that risk into `"None"` or "looks good," the pipeline should fail closed or require human review. Downstream agents should not consume the artifact until semantic specificity, provenance, and cross-artifact consistency checks pass.

## Answer Key

1. Structural schema validation proves parseability, required fields, allowed types, and minimum shape. It does not prove truth, freshness, completeness, source alignment, or safety.
2. Schema-compliant confabulation happens when an agent satisfies the schema with generic, hallucinated, stale, or low-value content that looks valid to the parser but is not reliable evidence.
3. A required array can contain useless filler such as "Make sure it works" or "Looks good." The type is correct, but the content is not specific or actionable.
4. A semantic null is a structurally valid value that carries no useful engineering meaning, such as `"None"` in a risk field despite upstream findings.
5. Cross-artifact consistency checks should catch the conflict. If upstream risk exists but the final report says no risk, the pipeline should fail closed or require human review.
6. Strict schemas can become compression points. If there is no field for conditional approvals, rare caveats, or multidimensional risks, the agent may truncate or omit them to satisfy the structure.
7. Type coercion can turn complex error objects, caveats, or evidence into vague strings. Downstream agents may over-trust the value because validation passed.
8. Block downstream automation, preserve validation telemetry, regenerate or enrich the artifact, and require semantic and provenance checks before use.

## Common Wrong Answers

- Treating schema success as approval to ship.
- Ignoring missing fields because the prose looks clear.
- Assuming a valid final report cannot omit important findings.
- Fixing the schema to fit a bad artifact instead of regenerating the artifact.
- Accepting phrases like "No issues found," "None," or "Looks good" as engineering evidence without source comparison.
- Letting downstream agents consume a schema-valid artifact before semantic and provenance checks pass.
- Treating semantic scanners or LLM graders as replacements for deterministic cross-artifact checks.

## Safe Operator Decision

Block downstream automation on schema failure. If validation passes but semantic checks flag generic filler, semantic nulls, downgraded risk, missing provenance, or cross-artifact conflicts, require human review and regenerate the artifact from current evidence before downstream use.

## Agentic Nuance

Schema validation in an Agentic SDLC establishes structural integrity, not semantic truth. When agents are forced into strict JSON mode or tool-calling schemas, they may optimize for structural compliance: every required field exists, every type matches, and the artifact passes the gate.

That does not mean the artifact is useful or safe. A model can produce schema-valid JSON filled with generic filler, hallucinated reasoning, stale decisions, downgraded risk language, or semantic nulls. The validator passes because the shape is correct, while downstream agents inherit a false sense of certainty.

Schemas can also become compression points. If a complex security caveat, conditional approval, or architectural trade-off does not fit neatly into a primitive string or array, the agent may truncate or omit it to satisfy the schema.

The safe control is layered validation. JSON parsing and schema validation should be treated as the first gate, not the final decision. Production-grade agentic pipelines need semantic specificity checks, cross-artifact consistency checks, provenance validation, deterministic escalation rules, and human review when structurally valid content conflicts with upstream evidence.

## Portfolio Signal

This lab demonstrates production-grade thinking about programmatic quality controls for LLM-generated artifacts. It shows the ability to separate structural serialization from content integrity, detect schema-compliant hallucination, identify semantic nulls, and prevent downstream agents from over-trusting valid but misleading artifacts.

A reviewer should come away understanding that the engineer can reason beyond "did the JSON validate?" and ask the more important question: "Is the schema-valid content specific, current, consistent, and safe to use?"
