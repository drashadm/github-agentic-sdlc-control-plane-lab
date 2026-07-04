# Failure Analysis Playbook

| # | Symptom | Likely Cause | Artifact to Inspect | Risk Level | Safe Operator Response |
|---:|---|---|---|---|---|
| 1 | Agent changed workflow file and stalled | Approval gate required for workflow changes | PR timeline, session log | High | Pause merge, request human approval, inspect changed workflow diff |
| 2 | Downstream job cannot find expected output | `$GITHUB_OUTPUT` name mismatch or missing job output | Workflow logs, workflow YAML | Medium | Fix output key, rerun workflow, verify producing job artifact |
| 3 | MCP tool unavailable | Tool not listed or server config mismatch | Agent file, MCP config | Medium | Confirm server name/tool name, narrow allowlist, retry after review |
| 4 | Broad MCP access appears in agent profile | Wildcard allowlist such as `server/*` | `.agent.md`, MCP config | High | Replace wildcard with explicit tools, require security review |
| 5 | Agent resumed stale session | Session state older than branch changes | Session log, memory file | Medium | Reset or re-scope session, validate current branch state |
| 6 | Reviewer and builder disagree on output | Conflicting task interpretation or stale artifact | Reviewer findings, builder summary | Medium | Consolidate conflicts, require planner clarification |
| 7 | Artifact deleted before audit review | Retention or manual deletion issue | Audit log, workflow artifacts | High | Block final approval, regenerate artifact, preserve deletion record |
| 8 | Hook blocked execute access | Pre-tool policy denied command execution | Hook event log | Medium | Confirm deny was expected, escalate only if execution is approved |
| 9 | Memory fact conflicts with current repo | Stale repository fact or invalid citation | Memory files, current code | Medium | Prune stale memory, regenerate validated repository facts |
| 10 | Security gate failed due to permissions | Workflow lacks required permission or has unsafe permission | Security gate logs, workflow YAML | High | Correct permissions, rerun gate, avoid broad permissions unless justified |
| 11 | Branch scope mismatch | Agent ran on default branch or wrong PR branch | Workflow context, session log | High | Stop action, re-run on correct branch/ref, verify no unintended writes |
| 12 | Human approval skipped for high-risk action | Missing approval condition or weak workflow gate | PR timeline, workflow YAML | Critical | Revert if needed, add explicit approval gate, conduct audit |
| 13 | Final report omits security finding | Consolidator consumed wrong or stale artifact | Consolidated report, audit artifact | High | Block final decision, regenerate report from current inputs |
| 14 | Matrix job hides partial failure | One axis failed but final job ignored status | Workflow logs, matrix strategy | Medium | Add explicit needs/status checks and artifact validation |
| 15 | Agent repeats previously completed work | Missing durable state or failed resume detection | Session log, planner artifact | Low/Medium | Reconcile state, update progress artifact, resume from last verified step |
| 16 | Remote MCP endpoint used without trust notes | External tool boundary undocumented | MCP config, governance review | High | Require trust review, document data flow, narrow or disable access |
