# Repository Validation Governance

## Why Validation Matters

Artifact-first repositories need repeatable validation so humans and agents can trust that files are parseable, references resolve, and examples remain public-safe. A lab about governed agentic delivery should be able to inspect its own evidence files before asking reviewers to trust them.

Validation also protects the public portfolio shape of the repository. It helps catch broken JSON, stale documentation links, missing required artifact fields, and unsafe-looking secret patterns before they reach a review branch.

## What This Harness Checks

- JSON parse validity
- lightweight schema required-field contracts
- enum and const checks where simple
- no-secrets posture
- local documentation references

## What This Harness Does Not Claim

- It is not a full JSON Schema validator.
- It does not prove semantic truth.
- It does not replace human review.
- It does not implement production security scanning.

## How It Supports the Lab Doctrine

```text
Agents propose.
GitHub records.
Workflows enforce.
Artifacts prove.
Hooks constrain.
Humans approve high-risk action.
```

The validation harness turns that doctrine into a repo-quality habit. Agents and humans can propose changes, GitHub can record them, workflows can run the harness, artifacts can remain parseable, and humans can review high-risk authority transfer with better evidence.
