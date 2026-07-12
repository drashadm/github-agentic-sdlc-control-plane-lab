# GitHub Agentic SDLC Control Plane Lab

A portfolio grade artifact literacy lab for designing, inspecting, governing, and debugging GitHub native coding agent workflows.

This repository demonstrates how production coding agents can be governed inside a GitHub centered SDLC using custom agent profiles, MCP style tool boundaries, GitHub Actions artifacts, hook controls, memory and state management, execution logs, review gates, and human approval paths.

This is not a certification cram sheet or a production integration. It is a practical lab for developing hands on fluency with agentic software delivery through visible, inspectable artifacts.

---

## Project Status

This is a v0.1 educational scaffold for studying GitHub native agentic SDLC governance. The repository contains illustrative examples, sample artifacts, and practice labs. Some workflows, MCP configurations, hook examples, and logs are intentionally simplified or intentionally risky so they can be inspected, questioned, and improved.

The goal of this version is to establish the control plane structure and artifact literacy foundation. Future polish passes will add schema validation, expanded answer keys, workflow dry run checks, stronger source alignment, and more realistic failure scenarios.

---

## Project Thesis

Modern coding agents should not operate as invisible assistants. They belong inside a governed SDLC control plane where every action, artifact, permission, handoff, and approval path is reviewable.

GitHub already provides that control plane. It offers repositories as the system of record, branches and pull requests as controlled change paths, workflow logs as execution evidence, artifacts as durable handoff records, reviews and approvals as human gates, permissions as enforceable boundaries, and audit trails as accountability records. The infrastructure for governed agentic delivery already exists. This lab is about learning to use it deliberately.

---

## Core Doctrine

```text
Agents propose.
GitHub records.
Workflows enforce.
Artifacts prove.
Hooks constrain.
Humans approve high risk action.
```

---

## Agentic Vulnerability-to-Defense Matrix

The full reviewer matrix lives in `docs/vulnerability-to-defense-matrix.md`. It maps each lab to the agentic failure mode it demonstrates and the deterministic control pattern used to contain it. This is the fastest way for a reviewer to see that the lab is about governed agentic SDLC design, not app code or exploit execution.

| Lab | Core Failure Mode | Control Pattern |
| --- | --- | --- |
| Lab 01 | Agent profile authority is treated as passive prose | Review profiles as protected control-plane assets |
| Lab 02 | Workflow output state drifts or disappears | Validate state manifests and provenance before handoff |
| Lab 03 | MCP tools expand runtime authority | Enforce least-privilege tool allowlists and output checks |
| Lab 04 | Resumed sessions carry stale continuity claims | Revalidate branch, commit, run, memory, and approval state |
| Lab 05 | Hooks advise but do not enforce | Mediate tool use before execution and fail closed |
| Lab 06 | Memory is mistaken for authorization | Treat memory as untrusted cache and verify against repo evidence |
| Lab 07 | Consolidation flattens dissent into consensus | Preserve dissent and deterministic global status |
| Lab 08 | Draft notes leak into public output | Serialize only approved public fields and block leakage |
| Lab 09 | Schema-valid artifacts are semantically void | Layer schema checks with semantic and cross-artifact validation |
| Lab 10 | Green workflow status masks invalid handoff | Require transaction checkpoints and provenance-bound gates |
| Lab 11 | Zombie Pipeline hides compound trust collapse | Review the full chain of trust before authority transfer |

---

## What This Lab Demonstrates

* How to separate planning, building, reviewing, auditing, and consolidation responsibilities across agents
* How to scope tools by role instead of granting every agent every capability
* How to reason about MCP server access, tool allowlists, and transport risks
* How to inspect GitHub Actions workflows, outputs, artifact dependencies, and permission models
* How to diagnose memory and state drift across long-running agent tasks
* How to use hook style controls to constrain risky tool access
* How to treat logs and artifacts as first-class governance evidence
* How to design human-in-the-loop approval gates without destroying delivery velocity

---

## Repository Structure

```text
.github/
  agents/          Custom agent profiles with scoped tool configurations
  workflows/       GitHub Actions governance patterns, including an inert educational agent-runner review workflow
  hooks/           Hook and permission-decision examples
  instructions/    Repository-level agent instructions
  prompts/         Reusable prompts for planning, review, and audit

docs/              Architecture notes, artifact reading guides, domain mapping, failure analysis
mcp/               MCP server definitions and allowlist examples
memory/            Memory and state examples, including drift scenarios
logs/              Sample agent execution and workflow logs
artifacts/         Sample plan, review, audit, and final report artifacts
labs/              Hands-on artifact-reading exercises
org-governance/    Organization-level custom agent governance examples
```

---

## How to Use This Lab

1. Start with `docs/source-ingestion-notes.md` for full context on the lab design.
2. Read `docs/ROADMAP.md` for planned polish and validation milestones.
3. Read `docs/gh-600-domain-map.md` to understand the six major capability areas.
4. Review `docs/artifact-schema-map.md`, `docs/risk-to-github-mitigation-map.md`, and `docs/agentic-threat-model-map.md` for governance maps.
5. Open `docs/vulnerability-to-defense-matrix.md` for the lab-by-lab failure-mode and control-pattern map.
6. Read `docs/advanced-agentic-failure-modes.md`, `docs/context-window-gating.md`, and `docs/cost-and-retry-control.md` for deeper agentic failure patterns.
7. Read `docs/zombie-pipeline-governance.md` to understand compound handoff failure and chain-of-trust review.
8. Read `docs/artifact-transaction-governance.md` to understand workflow success versus agentic success in artifact handoffs.
9. Read `docs/schema-semantic-validation-governance.md` to understand why schema validity proves shape, not content integrity.
10. Use `docs/workflow-validation-guide.md` and `docs/workflow-dry-run-checklist.md` to review workflow gates before trusting downstream agent execution.
11. Read `docs/state-serializability.md` to understand workflow outputs and artifact names as multi-agent state contracts.
12. Read `docs/session-continuity-governance.md` to understand resumed session and stale-state review.
13. Read `docs/hook-enforcement-governance.md` to understand pre-tool guardrails and approval binding.
14. Read `docs/memory-governance.md` to understand memory validation, quarantine, and belief/authorization separation.
15. Read `docs/multi-agent-coordination-governance.md` to understand dissent preservation and consolidation fidelity.
16. Read `docs/output-serialization-governance.md` to understand draft/final separation and public artifact promotion gates.
17. Read `docs/mcp-tool-boundary-governance.md` before reviewing MCP server examples.
18. Use `docs/lab-nuance-upgrade-playbook.md` and `docs/v0.5-lab-upgrade-plan.md` to understand the remaining lab upgrade quality bar.
19. Inspect the agent profiles under `.github/agents/` and note how tool access is scoped.
20. Review MCP server examples under `mcp/`.
21. Review workflow governance patterns under `.github/workflows/`.
22. Complete the labs under `labs/` by reading the artifacts and explaining what is safe, risky, broken, or missing.

Use `labs/README.md` for the recommended lab order, difficulty levels, and answer-key guidance.

---

## Local Validation

Run the dependency-free repository validation harness with:

```bash
python scripts/validate_repo.py
```

The harness checks JSON parsing, lightweight schema contract fields, conservative no-secrets posture, and local documentation references. It uses only the Python standard library and does not claim full JSON Schema validation.

---

## Certification Cram Path

For a repo-based study sprint, use `docs/certification-cram-map.md`, `docs/exam-style-practice-questions.md`, and `docs/oral-defense-prompts.md`. These files map the lab artifacts to practical agentic SDLC skills and interview-style explanations. They are study aids, not official exam guidance or a guarantee of exam coverage.

---

## Hands-On Cram Drills

Practice timed artifact diagnosis with `docs/hands-on-artifact-review-drills.md`, track readiness in `docs/weak-area-scorecard.md`, review `docs/rapid-review-flashcards.md`, and organize the final sprint with `docs/final-48-hour-cram-plan.md`.

---

## Design Principles

**Planning and execution are different responsibilities.**

Planning can be broad, exploratory, and analytical. Execution must be narrow, scoped, observable, and reversible where possible. Conflating them is where agent systems usually break down.

**Agents should receive the least capability needed for their role.**

A reviewer rarely needs edit or execute access. A security auditor should not need broad write capabilities. An executor is high risk by definition and requires stronger gates. Least privilege is not a constraint on agent usefulness; it is a condition for safe autonomy.

**Artifacts are not decoration.**

Plans, diffs, audit findings, logs, and final reports are evidence. They allow humans and downstream workflows to verify what actually happened, not just what an agent claims happened.

**Memory must be validated.**

Stored facts and preferences can be useful, but stale context causes drift, and drift causes dangerous decisions. Durable state must be compared against current repository reality before an agent acts on it.

**Hooks and workflows are control points, not suggestions.**

Agents reason their way toward actions. Control points enforce boundaries regardless of that reasoning. Hooks, protected branches, permission models, review gates, and workflow approvals are what make agent autonomy governable at scale.

---

## Planned Labs

| Lab    | Focus                                    |
| ------ | ---------------------------------------- |
| Lab 01 | Read and interpret a custom agent file   |
| Lab 02 | Debug a workflow output handoff failure  |
| Lab 03 | Identify MCP tool access risk            |
| Lab 04 | Analyze a session execution log          |
| Lab 05 | Evaluate a hook permission decision      |
| Lab 06 | Diagnose memory drift across agent tasks |
| Lab 07 | Review a multi-agent handoff chain       |
| Lab 08 | Detect reviewer note leakage             |
| Lab 09 | Diagnose schema validation failure       |
| Lab 10 | Trace a GitHub Actions artifact handoff  |
| Lab 11 | Advanced agent handoff failure           |

Each lab includes an Agentic Nuance section that connects the surface artifact issue to a deeper production agent failure mode.

---

## Public Proof Intent

This repository exists to demonstrate practical, hands on fluency with agentic SDLC governance. It is intentionally artifact heavy because real production agent operations are governed through files, logs, workflows, approvals, and evidence. Not through conversation histories that disappear.

The skills this lab builds are the ones that matter when coding agents move from assisted development into governed, auditable software delivery at scale.
