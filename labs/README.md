# Labs

This directory contains safe, inert artifact-reading labs for GitHub-native agentic SDLC governance. The sequence starts with individual artifacts, then moves into workflow handoffs, memory validation, schema checks, and multi-agent consolidation.

## Recommended Order

Work through the labs in numeric order. Labs 01-03 build basic artifact literacy, Labs 04-07 connect artifacts across sessions and agents, Labs 08-10 add publication quality, schema validation, and GitHub Actions handoff drills, and Lab 11 covers advanced agentic handoff failure.

## Skill Focus

Use each answer key after attempting the questions yourself. The answer keys are designed to teach operator reasoning, not to replace inspection of the source artifacts.

These labs are educational and safe/inert. They do not include runnable exploit payloads, real secrets, or production integrations.

Advanced labs focus on agent-specific risks that may not appear in normal CI/CD troubleshooting, such as schema drift, silent success, context-window overload, state poisoning, and retry/cost loops.

| Lab | Title | Difficulty | Primary Skill |
| --- | ----- | ---------- | ------------- |
| Lab 01 | Read a Custom Agent File | Beginner | Agent profile and least-privilege review |
| Lab 02 | Debug Workflow Output Handoff | Intermediate | State serializability and deterministic handoff validation |
| Lab 03 | Identify MCP Tool Access Risk | Intermediate | MCP allowlist and trust-boundary review |
| Lab 04 | Analyze a Session Log | Beginner | Session continuity and log inspection |
| Lab 05 | Hook Permission Decision | Beginner | Fail-closed hook decision review |
| Lab 06 | Memory Drift | Intermediate | Memory validation against repository state |
| Lab 07 | Multi-Agent Handoff | Advanced | Cross-artifact consolidation review |
| Lab 08 | Reviewer Note Leakage | Beginner / Intermediate | Final artifact cleanup and publish readiness |
| Lab 09 | Schema Validation Failure | Intermediate | Schema-aware artifact governance |
| Lab 10 | GitHub Actions Artifact Handoff Drill | Intermediate | Workflow dependency and evidence gating |
| Lab 11 | Advanced Agent Handoff Failure | Advanced | Schema drift, context-window governance, and silent failure prevention |

## How to Use the Answer Keys

Read the artifact first, write your answer, then compare against the answer key. If your answer differs, identify whether the difference comes from a missed field, stale assumption, or a reasonable alternate operator judgment.

## Agentic Nuance Checklist

* Did the agent receive the correct artifact?
* Did the artifact match the expected schema?
* Was the artifact current for this branch and run?
* Could the downstream agent guess missing context instead of failing?
* Was memory validated against current repository state?
* Was tool access scoped to the role?
* Was MCP access explicit and reviewed?
* Did the workflow preserve evidence?
* Did the final report include unresolved risks?
* Did a human approval gate exist for high-risk action?

## Lab Nuance Pattern

Use this pattern when moving from surface artifact inspection to production-grade agentic review:

* Surface issue: What broke in the visible artifact?
* Agentic issue: How could an autonomous agent continue incorrectly?
* Control-plane issue: What deterministic GitHub/MCP/workflow control should prevent it?
* Operator decision: Should the human approve, block, escalate, regenerate, narrow permissions, or preserve evidence?

Lab 01 now models this deeper review pattern for the remaining labs by treating agent profiles as prompt-and-capability control surfaces, not passive documentation.

Lab 02 extends the pattern by treating workflow outputs and artifact names as serialized state contracts. It shows why downstream agents must receive deterministic, schema-valid state for the current run instead of guessing or using stale cache context.

The v0.5 upgrade effort uses `docs/lab-nuance-upgrade-playbook.md` and `docs/v0.5-lab-upgrade-plan.md` as the quality bar for Labs 03-11.
