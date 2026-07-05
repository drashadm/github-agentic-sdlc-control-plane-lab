# Lab Nuance Upgrade Playbook

## Purpose

The remaining labs should not be surface-level artifact checks. Each upgraded lab should connect the visible file issue to a deeper agentic SDLC failure mode: how an autonomous or semi-autonomous agent could continue incorrectly, what control-plane boundary should stop it, and what a safe human operator should decide.

## Quality Bar

Every upgraded lab should answer four questions:

1. Surface issue: What broke in the visible artifact?
2. Agentic issue: How could an autonomous or semi-autonomous agent continue incorrectly?
3. Control-plane issue: What deterministic GitHub/MCP/workflow control should prevent it?
4. Operator decision: Should the human approve, block, escalate, regenerate, narrow permissions, or preserve evidence?

## Lab 01 and Lab 02 as Reference Models

The first two upgraded labs establish the pattern:

* Lab 01 upgraded `.agent.md` files from passive config examples into prompt-and-capability control surfaces.
* Lab 02 upgraded workflow output mismatch from a CI wiring bug into a state serializability and stale-context risk.

## Required Sections for Each Upgraded Lab

Every upgraded lab should have strong versions of:

* Scenario
* Artifacts to Inspect
* What You Are Looking For
* Questions
* Expected Reasoning Path
* Answer Key
* Common Wrong Answers
* Safe Operator Decision
* Agentic Nuance
* Portfolio Signal

## Safe Content Rules

* No real secrets
* No malicious domains
* No runnable exploit payloads
* No destructive shell commands
* Use safe placeholders for risky examples
* Keep examples educational and inert
* Do not frame the repo as an exploit lab

## Desired Tone

Professional, practical, enterprise-aware, security-minded, and public-portfolio appropriate.
