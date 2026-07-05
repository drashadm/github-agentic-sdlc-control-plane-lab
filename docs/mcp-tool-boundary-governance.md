# MCP Tool Boundary Governance

## Why MCP Changes the Agent Risk Model

MCP extends agent capability beyond the prompt and repository. It can introduce external state, remote services, local processes, tool calls, and mutating actions. That means MCP configuration is part of the agentic SDLC control plane, not ordinary convenience wiring.

## MCP Review Questions

* Is the server local or remote?
* Who owns the server?
* What transport is used?
* What tools are exposed?
* Are tools read-only or mutating?
* Is wildcard access used?
* What data leaves the repository?
* Are tool outputs validated?
* Are calls logged?
* Is there a removal or disable path?

## Narrow vs. Broad Access

| Access Pattern | Risk | Safer Control |
| -------------- | ---- | ------------- |
| explicit read-only tool | Limited but still needs output validation | Keep allowlist narrow and preserve provenance |
| explicit mutating tool | Agent may change external or repository state | Require human approval and audit logging |
| wildcard server access | Future tools may become automatically available | Treat as high-risk exception with security review |
| remote server with unclear owner | Data egress and server identity are ambiguous | Require owner, transport, auth, and logging review |
| local stdio server with broad process access | Host subprocess boundary may expose local context or unsafe behavior | Use trusted configuration, isolation, and explicit tools |

## Tool Output Is Not Ground Truth

MCP output can be stale, incomplete, biased, malformed, or adversarially influenced. Downstream agents should validate tool output against expected schema, source, timestamp, and provenance before acting. A tool response is evidence, not automatic truth.

## Safe Operator Checklist

* Confirm server owner and transport.
* Prefer explicit tools over wildcards.
* Review whether tools are read-only or mutating.
* Validate argument schemas and output schemas.
* Record run ID, branch, commit SHA, server version, and tool name.
* Document what data leaves the repository.
* Require approval for new tools, wildcard access, remote servers, and local subprocess boundaries.
* Preserve MCP review artifacts and removal paths.
