# Exam-Style Practice Questions

These are repo-grounded practice questions, not official exam questions. They are designed to help the operator reason through agentic SDLC scenarios using this repository's artifacts.

## Question 1

Scenario:
A reviewer treats `.github/agents/executor.agent.md` as ordinary documentation because it is a Markdown file.

Question:
What is the best control-plane interpretation?

Choices:
A. It is harmless prose unless a workflow imports it.
B. It is a control-plane asset because it shapes role, authority, and tool expectations.
C. It is only relevant to human onboarding.
D. It should be ignored during security review.

Correct Answer:
B.

Why:
Agent profiles influence behavior and authority boundaries, so they should be reviewed like governance artifacts.

## Question 2

Scenario:
An MCP config uses broad wildcard tool access for a local server.

Question:
What is the primary risk?

Choices:
A. The YAML file may render poorly.
B. The agent may gain runtime capabilities beyond reviewed intent.
C. The workflow will automatically fail.
D. The server cannot be documented.

Correct Answer:
B.

Why:
MCP access externalizes authority; broad tools expand what an agent can do at runtime.

## Question 3

Scenario:
A downstream workflow receives an empty output variable but the upstream job exits successfully.

Question:
What should happen before invoking the next agent?

Choices:
A. Continue because the job was green.
B. Ask the next agent to infer missing context.
C. Validate the handoff state and fail closed if required fields are missing.
D. Retry indefinitely with more context.

Correct Answer:
C.

Why:
Workflow success is runner evidence, not proof that valid agentic state was handed off.

## Question 4

Scenario:
An artifact has the expected filename but its commit SHA does not match the current branch head.

Question:
What control is most relevant?

Choices:
A. Artifact provenance validation.
B. Markdown linting.
C. Human memory.
D. A larger context window.

Correct Answer:
A.

Why:
Provenance binds artifacts to run ID, branch, commit SHA, workflow, and producing job.

## Question 5

Scenario:
A JSON artifact validates against a schema but contains generic filler in required fields.

Question:
What is the missing control?

Choices:
A. Semantic validation.
B. A second file extension.
C. More YAML comments.
D. Fewer required fields.

Correct Answer:
A.

Why:
Schema validation checks shape; semantic validation checks whether content is meaningful and specific.

## Question 6

Scenario:
A resumed session uses a stale assumption from a previous branch.

Question:
What should be checked first?

Choices:
A. Whether the agent sounds confident.
B. Branch, commit SHA, run ID, artifacts, memory, permissions, and approval state.
C. The number of Markdown files.
D. Whether the final report is polished.

Correct Answer:
B.

Why:
Session continuity is a claim that must be proven against current repository state.

## Question 7

Scenario:
Memory says an agent is allowed to execute deployment steps, but the current profile does not grant that role.

Question:
What is the safest conclusion?

Choices:
A. Memory overrides profile authority.
B. The agent should proceed if the memory is old.
C. Memory is an untrusted cache and must not grant authority.
D. The deployment should be hidden from review.

Correct Answer:
C.

Why:
Memory may inform context, but runtime authority must come from current policy and reviewed artifacts.

## Question 8

Scenario:
A hook logs that a command is risky but allows it to run anyway.

Question:
What weakness does this show?

Choices:
A. Advisory control mistaken for enforcement.
B. Too many schema files.
C. A missing README section.
D. A harmless logging preference.

Correct Answer:
A.

Why:
Pre-tool controls are strongest when they mediate execution before action and fail closed when needed.

## Question 9

Scenario:
A final consolidator removes a security auditor's conditional approval from the operator report.

Question:
What failure mode is present?

Choices:
A. Semantic compression loss.
B. JSON parse failure.
C. External URL validation.
D. Workflow dispatch failure.

Correct Answer:
A.

Why:
Consolidators can flatten dissent and conditional findings into false consensus.

## Question 10

Scenario:
Internal reviewer notes appear in a public report artifact.

Question:
Which control pattern applies?

Choices:
A. Strict output serialization and publication readiness gates.
B. More permissive MCP access.
C. Larger token budgets.
D. Ignoring draft state.

Correct Answer:
A.

Why:
Public artifacts should contain only approved fields and should block leakage of draft or internal content.

## Question 11

Scenario:
An agent retries a failed handoff four times, each time adding more logs and prior failures to context.

Question:
What should control this?

Choices:
A. Retry, token, cost, context-window, and semantic-progress limits.
B. A longer final report.
C. A hidden approval.
D. A broad wildcard.

Correct Answer:
A.

Why:
Retry loops can compound cost and context drift without improving semantic progress.

## Question 12

Scenario:
A workflow reports success, but `processed_items_actual` is zero when work was expected.

Question:
What is the best interpretation?

Choices:
A. A successful no-op by default.
B. A blocking semantic-progress failure unless explicitly approved.
C. A formatting issue.
D. A reason to skip provenance checks.

Correct Answer:
B.

Why:
Zero-work success is a control-plane signal that the pipeline may be continuing incorrectly.

## Question 13

Scenario:
A schema has `required` fields and simple top-level enums.

Question:
What does `scripts/validate_repo.py` claim to validate?

Choices:
A. Full JSON Schema Draft 2020-12 behavior.
B. Parse checks and lightweight required-field, enum, and const contracts.
C. Runtime agent behavior.
D. Official exam coverage.

Correct Answer:
B.

Why:
The harness is intentionally dependency-free and honest about its limited scope.

## Question 14

Scenario:
The secret scanner finds the word "token" in `docs/cost-and-retry-control.md`.

Question:
Why does the harness report but not fail this by default?

Choices:
A. Documentation-only matches are expected in this educational repo.
B. Tokens are never risky.
C. The scanner is disabled.
D. Markdown files are ignored.

Correct Answer:
A.

Why:
The repo intentionally discusses token budgets; only simple high-risk key-like patterns should fail.

## Question 15

Scenario:
A Markdown reference points to a local guide that does not exist in the repository.

Question:
How should the validation harness treat it?

Choices:
A. Ignore all local references.
B. Report a missing local reference failure.
C. Try to open a web browser.
D. Replace it with an external URL.

Correct Answer:
B.

Why:
Public repo hygiene depends on local documentation references resolving.

## Question 16

Scenario:
An artifact includes unknown upstream JSON keys and the downstream prompt ingests them as raw context.

Question:
What is the risk?

Choices:
A. Unexpected-field context injection.
B. Better schema compliance.
C. Stronger provenance.
D. Improved validation speed.

Correct Answer:
A.

Why:
Unknown fields should be rejected or quarantined, not treated as trusted prompt context.

## Question 17

Scenario:
A reviewer sees `.github/workflows/validate-repo.yml` running on pull requests.

Question:
What is its purpose?

Choices:
A. Deploy the project.
B. Run the dependency-free validation harness.
C. Rotate credentials.
D. Claim production security scanning.

Correct Answer:
B.

Why:
The workflow is an educational PR gate that runs `python scripts/validate_repo.py`.

## Question 18

Scenario:
A planner output artifact is parseable JSON but uses `target_files` where the schema expects another field.

Question:
What should the downstream agent do?

Choices:
A. Infer the intended field.
B. Treat parseability as enough.
C. Block or quarantine the malformed handoff.
D. Copy unknown fields into its prompt.

Correct Answer:
C.

Why:
Parseable JSON is not necessarily a valid handoff contract.

## Question 19

Scenario:
A report claims all agents agreed, but the manifest shows one conditional approval.

Question:
What should the operator inspect?

Choices:
A. Consolidation fidelity evidence.
B. Only the final paragraph.
C. The repository icon.
D. External billing logs.

Correct Answer:
A.

Why:
The operator must verify whether final consolidation preserved upstream dissent and conditions.

## Question 20

Scenario:
A hook decision approves a command without binding approval to payload, branch, and commit.

Question:
What is the weakness?

Choices:
A. The approval may be reused or misapplied.
B. The Markdown is too short.
C. The command becomes safer.
D. The workflow cannot run.

Correct Answer:
A.

Why:
Approval should be scoped to the exact reviewed operation and repository state.

## Question 21

Scenario:
A memory artifact contains useful facts but no source commit or freshness evidence.

Question:
What should happen before context injection?

Choices:
A. Inject it because it is useful.
B. Validate or quarantine it.
C. Treat it as authorization.
D. Publish it as final output.

Correct Answer:
B.

Why:
Memory must be checked against current repository evidence before it influences an agent.

## Question 22

Scenario:
A workflow uses artifacts as handoff records between jobs.

Question:
Why are artifacts important?

Choices:
A. They are durable evidence that can be reviewed and versioned.
B. They replace all human approval.
C. They guarantee semantic correctness.
D. They remove the need for schemas.

Correct Answer:
A.

Why:
Artifacts preserve inspectable evidence of intent, scope, review, and state.

## Question 23

Scenario:
A green check appears on a workflow, but the uploaded artifact is from a prior run.

Question:
What control catches this?

Choices:
A. Provenance-bound artifact consumption.
B. Ignoring run IDs.
C. More prose in the README.
D. Larger outputs.

Correct Answer:
A.

Why:
Consumers should verify run ID, branch, commit SHA, workflow, job, and artifact identity.

## Question 24

Scenario:
A public report includes placeholders that were meant to be internal reviewer notes.

Question:
Which lab topic does this best match?

Choices:
A. Reviewer note leakage.
B. MCP server identity.
C. Cost control.
D. Git branch naming.

Correct Answer:
A.

Why:
Draft/final boundary failures can leak internal state into public artifacts.

## Question 25

Scenario:
An operator wants to explain why the repo is not an app.

Question:
Which answer is strongest?

Choices:
A. It models an artifact-first governance control plane for agentic SDLC.
B. It forgot to include a frontend.
C. It cannot run any checks.
D. It is an official exam simulator.

Correct Answer:
A.

Why:
The repository demonstrates governance through inspectable files, workflows, schemas, logs, and labs.

## Question 26

Scenario:
An agent asks for all tools because it can decide responsibly at runtime.

Question:
What principle counters this?

Choices:
A. Least privilege by role.
B. More autonomy always improves safety.
C. Reviews should happen only after execution.
D. Tool access does not matter.

Correct Answer:
A.

Why:
Agents should receive only the capabilities needed for their reviewed role and task.

## Question 27

Scenario:
An artifact has a fake digest in this educational repo.

Question:
How should the operator describe it?

Choices:
A. A modeled evidence pattern, not real cryptographic signing.
B. A production attestation.
C. A secret key.
D. Proof that the artifact cannot be stale.

Correct Answer:
A.

Why:
The lab uses fake educational values to teach provenance patterns without claiming production attestation.

## Question 28

Scenario:
A candidate says the repo guarantees certification success.

Question:
What correction is accurate?

Choices:
A. It is a practical repo-based study guide, not an official exam guide or guarantee.
B. It covers every official objective.
C. It replaces hands-on practice.
D. It contains official exam questions.

Correct Answer:
A.

Why:
The cram docs support practical review but do not claim official coverage or outcomes.

## Question 29

Scenario:
A downstream agent receives a valid artifact but the context window also includes stale prior-failure traces.

Question:
What risk should be considered?

Choices:
A. Context-window pollution or drift.
B. Better determinism.
C. Automatic approval.
D. Schema deletion.

Correct Answer:
A.

Why:
More context can amplify stale assumptions and confuse downstream reasoning.

## Question 30

Scenario:
A pipeline continues after schema drift, zero processed items, retry budget exhaustion, and a polished final report.

Question:
What failure mode best describes this?

Choices:
A. Zombie Pipeline.
B. Simple typo.
C. Successful deployment.
D. External URL failure.

Correct Answer:
A.

Why:
A Zombie Pipeline reports success after the agentic state chain has already collapsed.
