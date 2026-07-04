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
  workflows/       GitHub Actions governance patterns
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
5. Inspect the agent profiles under `.github/agents/` and note how tool access is scoped.
6. Review MCP server examples under `mcp/`.
7. Review workflow governance patterns under `.github/workflows/`.
8. Complete the labs under `labs/` by reading the artifacts and explaining what is safe, risky, broken, or missing.

Use `labs/README.md` for the recommended lab order, difficulty levels, and answer-key guidance.

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

---

## Public Proof Intent

This repository exists to demonstrate practical, hands on fluency with agentic SDLC governance. It is intentionally artifact heavy because real production agent operations are governed through files, logs, workflows, approvals, and evidence. Not through conversation histories that disappear.

The skills this lab builds are the ones that matter when coding agents move from assisted development into governed, auditable software delivery at scale.
