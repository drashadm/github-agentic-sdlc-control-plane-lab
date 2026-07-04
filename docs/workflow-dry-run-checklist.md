# Workflow Dry-Run Checklist

## Pre-run Checks

* Confirm the workflow is educational or production-intended.
* Confirm the triggering branch, PR, and path filters are expected.
* Confirm referenced artifacts exist in the repository or producing job.

## Permission Checks

* Verify `permissions` are explicitly declared.
* Confirm no job uses broader write access than needed.
* Require review for workflow permission changes.

## Artifact Checks

* Match upload and download artifact names.
* Confirm required artifacts are produced by the expected job.
* Confirm stale artifacts cannot satisfy current-run requirements.

## Branch/ref Checks

* Confirm the workflow runs on the intended branch or PR ref.
* Confirm resumed agent context matches the current branch.
* Record the commit SHA used for artifact generation.

## Schema Validation Checks

* Validate structured artifacts before downstream agent use.
* Block missing required fields.
* Treat parseable JSON as insufficient without schema fit.

## Context-window Checks

* Reject oversized raw logs or diffs.
* Require summaries that link back to source evidence.
* Preserve unresolved risks in compressed context.

## Failure Behavior Checks

* Confirm missing artifacts fail closed.
* Confirm zero processed files is not reported as success.
* Confirm retry loops have a stop condition.

## Human Approval Checks

* Require human approval for destructive execution.
* Require approval for workflow permission expansion.
* Require review for new MCP tools or remote servers.

## Post-run Evidence Checks

* Preserve run logs and uploaded artifacts.
* Confirm final reports list consumed artifacts.
* Confirm unresolved risks are carried forward.
