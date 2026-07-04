# Lab 03: Identify MCP Risk

## Scenario

A custom agent includes:

```yaml
tools:
  - "governance-api/*"
```

## Questions

1. Why is this risky?
2. What safer alternative exists?
3. Is an MCP allowlist equivalent to a firewall?
4. What review should be required?

## Expected Reasoning Path

Wildcard tool access may include future tools that were not reviewed. MCP allowlists narrow tool names but do not replace identity, network, secret, or runtime controls.

## Safe Operator Response

Replace wildcard access with explicit tools and require security review for remote MCP access.
