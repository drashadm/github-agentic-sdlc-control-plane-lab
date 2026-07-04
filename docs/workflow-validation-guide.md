# Workflow Validation Guide

## Why Workflow Validation Matters

Workflows are where agent intent becomes enforceable process. If the workflow is weak, agents can appear governed while still bypassing meaningful controls. In agentic SDLC systems, the risky failure is often not a failed job. It is a job that passes while a downstream agent receives stale, malformed, incomplete, or unverified context.

## What to Inspect

Inspect:

* trigger scope
* permissions blocks
* branch and PR scope
* `needs` dependencies
* `$GITHUB_OUTPUT`
* artifact upload/download naming
* concurrency and `cancel-in-progress`
* gate conditions
* environment or reviewer gates
* artifact retention
* final report dependencies

## Workflow Files in This Lab

| Workflow File | Purpose | Primary Artifact Skill |
| ------------- | ------- | ---------------------- |
| `.github/workflows/agent-plan-review.yml` | Validate and preserve a planner artifact before review | Plan artifact existence and review handoff |
| `.github/workflows/multi-agent-artifact-handoff.yml` | Demonstrate staged artifact handoffs across planner, builder, and reviewer jobs | `needs`, job outputs, and artifact naming |
| `.github/workflows/security-gate.yml` | Inspect active agent and workflow risk patterns while preserving educational examples | Distinguishing active config risk from inert lab examples |
| `.github/workflows/consolidated-operator-report.yml` | Collect evidence before publishing a final operator report | Evidence gating and final report dependencies |

## Common Workflow Failure Modes

Common failures include:

* downstream job runs without required upstream artifact
* workflow succeeds even though agent processed zero files
* permissions block is broader than required
* artifact name mismatch
* stale artifact consumed
* branch scope mismatch
* educational risky example treated as active production config

## Safe Operator Response Checklist

* Confirm the trigger scope matches the intended branch or PR path.
* Verify permissions are least privilege.
* Trace each `needs` dependency before trusting downstream jobs.
* Compare `$GITHUB_OUTPUT` names to downstream references.
* Match artifact upload and download names exactly.
* Confirm gates fail closed when evidence is missing or invalid.
* Validate required artifacts against schemas before agent consumption.
* Preserve logs and artifacts that explain failures.
* Require human approval for workflow permission changes and high-risk execution.
