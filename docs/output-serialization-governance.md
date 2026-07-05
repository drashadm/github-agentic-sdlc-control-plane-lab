# Output Serialization Governance

## Draft State Is Not Public State

Agentic workflows can produce drafts, reviewer notes, critique, metadata, structured outputs, and public payloads during the same run. These states are useful for review, but they are not equally publishable.

Only approved public payload fields should enter public files. A document should not be considered final because it was written to disk. It becomes final only after a promotion gate proves the public artifact was generated from an approved field and excludes draft residue.

## Raw LLM Buffers Are Hazardous

Raw model responses can contain mixed content: draft prose, reviewer critique, metadata, placeholder markers, and public-ready text. A runner should not write a raw response buffer directly to public documentation or release notes.

The safer pattern is to require structured output, extract a known public field, validate the artifact, and preserve evidence that the public artifact came from that field.

## Scratchpad Leakage

Scratchpad leakage happens when simulated internal notes, reviewer comments, or private context placeholders cross into a public artifact. In this lab, scratchpad examples are safe and inert placeholders, not real private reasoning or private instructions.

The common orchestration failure is concatenating internal fields with public fields, parsing the wrong structured output field, or treating the full response object as publishable Markdown.

## Strict Output Serialization

Safer patterns include:

- write only from approved public fields such as `final_output` or `user_payload`
- reject raw LLM buffers as public artifacts
- require schema validation before publication
- block unresolved comments
- block internal note markers
- block hidden instruction placeholders
- block private context references
- preserve leakage scan evidence
- require human review before publication override

## Deterministic Promotion Gates

A publication gate should check artifact source, run ID, branch, commit SHA, schema validity, public payload field, excluded internal fields, unresolved comments, reviewer note leakage, private context references, and approval state.

File existence is not enough. A public artifact must be tied to the run that produced it, the branch and commit under review, the structured output contract, and the gate decision that allowed or blocked promotion.

## Semantic Scanners Are Optional Defense-in-Depth

Production systems may add semantic or LLM-based scanners to detect subtle leakage, ambiguous internal references, or policy-sensitive wording. This repository does not implement those scanners and does not claim to provide semantic scanning.

The lab models the control-plane evidence pattern: structured output, schema validation, deterministic field extraction, leakage artifacts, and human approval paths.

## Safe Operator Checklist

- Confirm the source payload is structured, not a raw model buffer.
- Confirm the public artifact was generated from an approved field such as `final_output` or `user_payload`.
- Confirm internal fields are excluded by schema and promotion logic.
- Scan for reviewer notes, unresolved comments, hidden instruction placeholders, and private context references.
- Tie the promotion decision to run ID, branch, and commit SHA.
- Preserve blocked publication evidence instead of deleting it.
- Require human review before any override.
