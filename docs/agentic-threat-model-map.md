# Agentic Threat Model Map

This document maps existing lab artifacts to agentic AI threat families without adding runnable exploit payloads. The examples are safe, non-executable, and intended for artifact-reading practice.

| Lab Artifact | Threat Family | What Could Go Wrong | GitHub/MCP Control | Safe Operator Response |
| --- | --- | --- | --- | --- |
| `mcp/broad-server-wildcard-risk.yml` | Excessive agency / overprivileged tool access | A broad wildcard grants more tool access than the agent role needs, including future tools that have not been reviewed. | Explicit MCP tool allowlists, security review, least privilege | Replace broad wildcards with named tools, document the justification, and require review before expanding access. |
| `mcp/local-stdio-risky-example.yml` | Local process execution risk / untrusted tool supply chain | A local tool server could expose unsafe capabilities or run with more local context than the operator intended. | Trusted servers, pinned versions, sandboxing, no unreviewed shell execution | Treat local stdio servers as high risk, review the server source and configuration, and require approval before enabling execution-like tools. |
| `.github/agents/executor.agent.md` | Indirect prompt injection / agent instruction tampering | A change to the executor profile could weaken approval requirements or steer the agent toward unsafe execution. | CODEOWNERS, required review for agent profile changes, signed/trusted changes where applicable | Review agent profile diffs like code, verify approval language remains intact, and block execution if instructions drift. |
| `.github/hooks/preToolUse-deny-execute.example.json` | Guardrail tampering / fail-open control risk | A hook decision could be weakened, removed, or interpreted as advisory instead of enforcing a block. | Protected hook files, required review, fail-closed policy, audit logging | Keep high-risk hook changes review-gated, verify denied actions remain blocked, and preserve hook decision logs. |

Threat labels are educational mappings, not authoritative legal or compliance classifications. Exact OWASP naming and numbering may change across versions.
