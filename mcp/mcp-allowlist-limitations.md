# MCP Allowlist Limitations

MCP allowlists are useful capability boundaries, but they are not complete security controls.

## What an MCP Allowlist Can Do

- restrict which named tools an agent may call
- document expected external capability
- make access reviewable in agent files
- reduce accidental tool exposure

## What an MCP Allowlist Cannot Fully Replace

- network firewall controls
- secret management
- server identity validation
- code review of server behavior
- runtime monitoring
- artifact logging
- human approval for high-risk actions

## Key Risk

A narrow allowlist such as:

```yaml
tools:
  - governance-api/read-policy
```

is much safer than:

```yaml
tools:
  - governance-api/*
```

The wildcard may include tools that are added later and never reviewed.

## Safe Operator Checklist

- Is the server local or remote?
- Who owns the server?
- What data leaves the repository?
- Are tools read-only or mutating?
- Are credentials involved?
- Is access narrow and explicit?
- Are calls logged?
- Are results preserved as artifacts?
