# Lab 05: Hook Permission Decision

## Scenario

A hook receives a request to execute:

```bash
rm -rf artifacts/
```

## Artifact to Inspect

`.github/hooks/preToolUse-deny-execute.example.json`

## Questions

1. Which event is this?
2. Which tool was requested?
3. What decision did the hook make?
4. Why is fail-closed appropriate?

## Expected Reasoning Path

This is a `preToolUse` event. The requested tool is `execute`. The hook decision is `deny` because the command is destructive and lacks approval.

## Safe Operator Response

Block the command, preserve the hook event, and require explicit human approval for any destructive operation.
