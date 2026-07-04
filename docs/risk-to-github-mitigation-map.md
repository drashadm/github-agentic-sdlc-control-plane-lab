# Risk to GitHub Mitigation Map

This document maps common agentic SDLC risks to observable GitHub symptoms and practical GitHub-native mitigations.

| Risk / Anti-Pattern | What It Looks Like in GitHub | Mitigation Using GitHub Controls |
| ------------------- | ---------------------------- | -------------------------------- |
| Planless execution | PR has a diff but no plan, rationale, scope, or success criteria | Require a plan section in the PR template; require review before merge |
| Over-permissioned agents | Workflows can write to the repository or access secrets broadly | Use least-privilege GITHUB_TOKEN permissions; use environments with required reviewers; restrict who can trigger workflows |
| Hidden reasoning | No assumptions, scope, decision trail, or artifact handoff | Require a plan artifact; link workflow runs; record key decisions in PR comments or review artifacts |
| Blind trust in automation | "CI passed, ship it" mindset without human judgment | Combine checks with CODEOWNERS, required reviews, and risk-based approvals |
| Stale memory or context drift | Agent resumes old assumptions that conflict with current repository state | Validate memory against current files, branch, and PR context before execution |
| Risky MCP expansion | Agent has broad tool access such as `server/*` without justification | Use explicit MCP tool allowlists; require security review for new tools or remote servers |
| Workflow permission creep | Workflow permissions expand from read-only to write-all without clear need | Review permissions blocks in workflow files; require approval for permission changes |
| Reviewer-note leakage | Internal review comment appears in final published docs or PR output | Add final-render review; require artifact cleanup checks before publish or merge |
| Missing audit evidence | Final report exists but does not link plan, review, logs, or security findings | Require consolidated operator report to list consumed artifacts and unresolved risks |
| Approval bypass | High-risk change merges without human review | Use branch protection, required reviewers, environments, and CODEOWNERS |
