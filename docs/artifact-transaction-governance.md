# Artifact Transaction Governance

## Workflow Success Is Not Agentic Success

GitHub Actions job success is based on configured step and process outcomes. It does not prove that an internal agent loop completed, all async work was awaited, all output files were flushed, or the correct artifact was consumed downstream.

A green workflow is useful evidence, but it is not the same as a valid agent handoff.

## Runner State vs. Agent Runtime State

Runner state and agent runtime state can diverge:

- runner step exited 0
- internal agent task may still be incomplete
- background work may not have written all state
- artifact upload may race file generation
- downstream job may run because `needs` passed, not because the artifact is valid

## Partial Artifact and Atomicity Risk

A handoff artifact can be:

- empty
- truncated
- partially written
- parseable but incomplete
- schema-valid but semantically incomplete
- uploaded before all records are present

This repository models atomicity and digest evidence with safe educational artifacts only. It does not implement real fsync enforcement or production transactional storage.

## Provenance Binding

Artifact identity should include:

- run ID
- run attempt
- branch
- commit SHA
- workflow
- producing job
- producing agent
- artifact name
- digest or checksum
- upload timestamp
- consuming job

The digests in this lab are fake educational values. Signed attestations may be useful as optional higher-assurance production controls, but this repository does not implement real cryptographic signing or attestation verification.

## `needs` Is Necessary But Not Sufficient

`needs` enforces job ordering, but not artifact integrity. A downstream job still needs artifact validation before invoking a downstream agent.

The builder can wait for the planner job and still receive an empty, stale, partial, wrong-run, or semantically invalid artifact.

## Transaction Gate Pattern

A safer pattern is:

- agent runtime completes
- expected outputs are checked
- file size and record count are checked
- JSON parse passes
- schema validation passes
- semantic validation passes
- digest is recorded
- provenance manifest is generated
- upload gate approves
- downstream gate revalidates before consumption

## Safe Operator Checklist

- Did the runner step succeed?
- Did the internal agent runtime complete?
- Were background tasks awaited or marked complete?
- Does the artifact exist and have expected size?
- Does the artifact parse?
- Does it pass schema validation?
- Does it pass semantic validation?
- Does the digest match the manifest?
- Is the artifact bound to the expected run, branch, commit, workflow, and job?
- Did the downstream job process the expected number of records?
- Should downstream automation be blocked?
