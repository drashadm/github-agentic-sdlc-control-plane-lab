# Custom Agent Repository Policy

## Purpose

Custom agents are governed SDLC assets. They must be reviewed, versioned, and retired like other platform components.

## Required Metadata

Every agent must define:

- name
- description
- owner
- intended use
- allowed tools
- denied actions
- approval requirements
- audit expectations

## Review Requirements

Security review is required when an agent:

- uses `execute`
- uses MCP tools
- changes workflow files
- expands permissions
- reaches remote systems
- performs external write actions

## Retirement

Retired agents must preserve historical artifacts and audit references.
