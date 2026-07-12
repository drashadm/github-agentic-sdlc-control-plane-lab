# Rapid Review Flashcards

Use these concise cards for quick recall during the final certification cram sprint. They are repo-based study aids, not official exam questions.

## Card 1

Q: What does an agent profile establish?

A: The agent's role, scope, tools, constraints, and review obligations.

## Card 2

Q: Does an agent profile alone authorize a high-impact action?

A: No. A current deterministic approval gate must grant that authority.

## Card 3

Q: Why separate planner and executor profiles?

A: Planning can explore broadly; execution needs narrow, approved authority.

## Card 4

Q: What is least privilege for an agent?

A: Only the tools and permissions required for its current role and task.

## Card 5

Q: What should happen when an agent's authority is ambiguous?

A: Fail closed and require explicit scope and approval.

## Card 6

Q: What does MCP externalize?

A: Tool authority beyond the agent's local profile.

## Card 7

Q: Why is an MCP wildcard risky?

A: New server tools can silently expand effective authority.

## Card 8

Q: What is safer than wildcard MCP access?

A: An explicit, reviewed tool allowlist.

## Card 9

Q: What detects MCP tool inventory drift?

A: Comparing the current manifest with an approved snapshot.

## Card 10

Q: What must a remote tool call preserve?

A: Scope, identity, approval, input constraints, and audit evidence.

## Card 11

Q: When should a hook enforce a denial?

A: Before the tool executes.

## Card 12

Q: Is a hook that only logs a violation preventive?

A: No. It provides telemetry, not enforcement.

## Card 13

Q: What should a denied pre-tool hook return?

A: An explicit machine-verifiable failure that stops execution.

## Card 14

Q: What should an approval be bound to?

A: The action, arguments, actor, branch, commit, and validity window.

## Card 15

Q: Why can argument rewriting be risky?

A: The executed action may differ from the action a human reviewed.

## Card 16

Q: What does a green workflow prove?

A: Only that configured steps reported success, not that the handoff was valid.

## Card 17

Q: What is workflow output key drift?

A: A producer and consumer use different names for the same expected value.

## Card 18

Q: How should required workflow outputs be checked?

A: Validate key presence, type, and non-empty semantic value before use.

## Card 19

Q: What should gate a downstream job?

A: Valid inputs, provenance, policy decisions, and required approvals.

## Card 20

Q: Why pin artifact identity across jobs?

A: To prevent a job from consuming a valid-looking artifact from the wrong run.

## Card 21

Q: What is an artifact handoff?

A: A producer-consumer contract carrying state and evidence between stages.

## Card 22

Q: What makes an artifact reviewable?

A: Explicit fields, provenance, integrity, validation results, and ownership.

## Card 23

Q: What should happen to a malformed artifact?

A: Reject it before any downstream decision or action.

## Card 24

Q: What is an artifact promotion gate?

A: A control that approves internal output for a more public or trusted context.

## Card 25

Q: Why keep scratchpads out of public artifacts?

A: They may contain provisional, unsupported, or irrelevant internal reasoning.

## Card 26

Q: What does JSON Schema primarily validate?

A: Structure, types, required fields, and declared constraints.

## Card 27

Q: Why is schema validity not truth?

A: Correct shape does not prove freshness, completeness, evidence, or meaning.

## Card 28

Q: What is semantic validation?

A: Domain checks that determine whether values are meaningful and decision-ready.

## Card 29

Q: Give one semantic-null example.

A: A required string containing "unknown" where a verified commit SHA is needed.

## Card 30

Q: In what order should artifact checks run?

A: Parse, schema, semantic invariants, provenance, then policy gates.

## Card 31

Q: Is memory an authority source?

A: No. Memory provides context and must be checked against current policy.

## Card 32

Q: What is memory drift?

A: Stored context no longer matches current repository facts or controls.

## Card 33

Q: How should conflicting memory be handled?

A: Quarantine or refresh it before agent use.

## Card 34

Q: What should a memory fact include?

A: Source, timestamp, scope, confidence, and freshness evidence.

## Card 35

Q: What wins when memory conflicts with current policy?

A: The authoritative current policy.

## Card 36

Q: What validates a resumed session?

A: Matching branch, commit, state version, approvals, and current artifacts.

## Card 37

Q: What should a stale session do?

A: Stop, refresh context, and obtain review where required.

## Card 38

Q: Why bind state to a commit SHA?

A: To detect when assumptions were formed against a different repository state.

## Card 39

Q: Is conversational continuity enough for execution continuity?

A: No. Execution requires validated technical and approval continuity.

## Card 40

Q: What is a safe session-resumption default?

A: Read-only inspection until freshness checks pass.

## Card 41

Q: What must a consolidator preserve?

A: Findings, dissent, conditions, severity, provenance, and unresolved status.

## Card 42

Q: Why is false consensus dangerous?

A: It can turn a blocked or conditional review into apparent approval.

## Card 43

Q: How can consolidation fidelity be checked?

A: Reconcile each source finding by stable identifier and decision impact.

## Card 44

Q: What is safe output serialization?

A: Emitting only fields allowed by an explicit output contract.

## Card 45

Q: What does provenance bind?

A: An artifact to its run, branch, commit, job, producer, and integrity digest.

## Card 46

Q: What does the repository validation harness check?

A: JSON parsing, lightweight schema contracts, risky secret patterns, and local links.

## Card 47

Q: What does the validation harness not claim?

A: Full JSON Schema validation or proof that artifact content is true.

## Card 48

Q: What is a Zombie Pipeline?

A: An active-looking pipeline that makes no semantic progress.

## Card 49

Q: How should zero semantic progress be controlled?

A: Enforce progress checkpoints, retry budgets, and a fail-closed stop condition.

## Card 50

Q: Where does human approval add the most value?

A: At high-impact, ambiguous, irreversible, or public-promotion boundaries.
