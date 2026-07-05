# Lab 08: Reviewer Note Leakage

## Difficulty

Beginner / Intermediate.

## Estimated Time

20-30 minutes.

## Scenario

A final documentation artifact contains an internal editorial note: "I would recommend mentioning this earlier in the intro." The sentence is not user-facing content. The learner must classify the failure and choose a safe operator response before publication.

In an agentic workflow, this is more than an editing miss. The agent may have produced draft text, reviewer critique, simulated scratchpad state, internal metadata, and final public output in the same run. If the orchestration layer writes the raw response buffer or the wrong structured field into a public Markdown file, draft residue can cross the publication boundary.

A final artifact is not final because it exists. It is final only if it passed a promotion gate that strips or blocks draft residue, reviewer notes, unresolved comments, private scratchpad state, internal-only context, and hidden instruction fragments.

## Artifacts to Inspect

- `docs/artifact-reading-guide.md`
- `logs/reviewer-scratchpad.json`
- `artifacts/reviewer-note-leakage-report.json`
- `artifacts/publication-readiness-report.json`
- `schemas/reviewer-scratchpad.schema.json`
- `schemas/reviewer-note-leakage-report.schema.json`
- `schemas/publication-readiness-report.schema.json`
- `.github/workflows/publish-docs.yml`
- `docs/output-serialization-governance.md`
- `docs/failure-analysis-playbook.md`
- `docs/risk-to-github-mitigation-map.md`
- `docs/guardrails-and-accountability.md`
- `docs/workflow-validation-guide.md`
- `docs/advanced-agentic-failure-modes.md`

## What You Are Looking For

Look for signs that draft review notes, reviewer comments, internal editing guidance, simulated scratchpad state, or private context placeholders leaked into final documentation. The operator should distinguish useful review feedback from publishable content and verify that publication depends on a deterministic promotion gate, not mere file existence.

Focus on:

- scratchpad state leakage
- reviewer note leakage
- draft/final boundary failure
- raw LLM buffer written directly to a public file
- structured field extraction error
- `final_output` vs `internal_notes` separation
- hidden instruction fragment placeholder detection
- private context reference placeholder detection
- unresolved comments in a public artifact
- publication gate vs file existence
- semantic scanner limitations
- deterministic promotion gates
- artifact promotion evidence tied to run ID, branch, and commit SHA

## Questions

1. Why is reviewer note leakage an output serialization failure rather than just an editing mistake?
2. What is the risk of writing a raw LLM response buffer directly into a public Markdown file?
3. If `reviewer-scratchpad.json` contains both `simulated_internal_notes` and `final_output`, which field is allowed to populate public documentation?
4. What API or orchestration mistake can cause internal scratchpad fields to blend into public-facing Markdown?
5. Why would a normal Markdown syntax check fail to detect hidden instruction fragments or private context references?
6. What should happen if the publication gate detects unresolved comments, reviewer notes, or internal placeholders?
7. Why should publication readiness be tied to run ID, branch, commit SHA, and structured output validation?
8. How could internal corporate context leak if an agent uses private sources during review and the runner writes the wrong output field?

## Expected Reasoning Path

A safe operator treats internal notes in published artifacts as a state-boundary and output serialization failure. The issue may look like unpolished prose, but the deeper failure is that the system could not prove only approved public payload fields reached the final artifact.

The operator should inspect the simulated scratchpad, leakage report, publication readiness report, schemas, and workflow gate. The safe path is to block publication, regenerate the public artifact from `final_output` or another approved public payload field, validate the structured output, run leakage checks, preserve run/branch/commit evidence, and require human review before any override.

## Answer Key

1. Reviewer note leakage is an output serialization failure because internal state crossed into a public artifact. The defect is not only the sentence; it is the broken boundary between draft/review fields and approved public output.
2. A raw LLM response buffer can contain mixed draft text, critique, metadata, placeholder markers, unresolved comments, and public content. Writing it directly to documentation collapses those states into one publishable blob.
3. Only `final_output` or another explicitly approved public payload field may populate public documentation. `simulated_internal_notes` is internal-only evidence.
4. The runner may concatenate fields, read the wrong JSON key, ignore the schema contract, stream intermediate text into a file, or treat the full API response as final Markdown.
5. Markdown syntax checks validate formatting, not semantic state boundaries. A hidden instruction placeholder or private context reference can be syntactically valid prose while still being unsafe to publish.
6. The gate should block or require review, preserve evidence, and regenerate the artifact from approved public fields before publication.
7. Run ID, branch, commit SHA, and schema validation prove which artifact was reviewed, which repository state produced it, and whether the payload shape matched the expected contract.
8. If private sources inform review and the runner writes internal notes or private context reference fields into public output, the public artifact can disclose internal assumptions or source references that were never approved for release.

## Common Wrong Answers

- Publishing anyway because the note is harmless.
- Deleting evidence of the issue without recording the cleanup.
- Treating Markdown syntax validity as publication readiness.
- Fixing only the sentence without adding a serialization or promotion gate.
- Trusting a semantic scanner alone without deterministic field selection and schema validation.
- Assuming a file is final because it exists in the `docs/` directory.

## Safe Operator Decision

Block publication or merge, preserve the leakage evidence, regenerate the public artifact only from `final_output` or another approved public payload field, validate the structured output, rerun leakage checks, and require human review before override.

## Agentic Nuance

Reviewer note leakage in an Agentic SDLC is a state-boundary failure. Agents often generate multiple classes of text during a workflow: drafts, critiques, reviewer notes, metadata, simulated scratchpad state, and final public output. If the orchestration layer treats the raw model response as a single blob, these states can collapse into the same public artifact.

The danger is not limited to unpolished prose. A leaked internal note can reveal private context, hidden instruction fragments, unresolved risk, proprietary review assumptions, or implementation details that were never meant to leave the agent runtime.

The safe control is strict output serialization. Public files should be generated only from approved public fields such as `final_output` or `user_payload`. Internal fields must be excluded by schema, leakage scans, and deterministic promotion gates before publication.

A final artifact is not final because it was written to disk. It is final only when it has passed a promotion gate that proves draft residue, reviewer notes, hidden instruction fragments, unresolved comments, and private context references were excluded.

## Portfolio Signal

This lab demonstrates production-grade thinking about output serialization, draft/final separation, and public artifact promotion in agentic workflows. It shows the ability to prevent internal reviewer notes, simulated scratchpad state, private context references, and hidden instruction fragments from crossing into public-facing deliverables.

A reviewer should come away understanding that the engineer can reason beyond "did the agent generate the document?" and ask the more important question: "Did the system prove that only approved public payload fields reached the final artifact?"
