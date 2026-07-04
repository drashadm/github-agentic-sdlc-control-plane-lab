# Context Window Gating

Agent artifacts should not be blindly pasted into an LLM context window. Large logs, raw diffs, repeated stack traces, or broad artifact bundles can crowd out important instructions, unresolved risks, and source evidence. When that happens, a downstream agent may appear to reason over the full handoff while actually missing the parts that matter.

Summaries should link to source artifacts instead of replacing them. A summary helps fit the task into context, but source links preserve auditability and let a reviewer verify the underlying evidence.

Define max artifact size before handoff. If an artifact is too large, mark it as blocked or require chunking and summarization before a downstream agent consumes it. Oversized raw logs should be rejected rather than silently compressed into an unverifiable summary.

Context compression can hide risk if it is not traceable. Any compressed summary should preserve unresolved findings, cite the source artifact, and state what was omitted.

# Context Window Gate Checklist

* Is the artifact task-relevant?
* Is it too large?
* Does it have a summary?
* Does the summary link back to source evidence?
* Are unresolved risks preserved?
* Is the artifact safe to pass to a downstream agent?
