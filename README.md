# ccar-f-prep-lab

Hands-on labs and notes from my preparation for the Claude Certified Architect –
Foundations (CCAR-F) exam. Each day maps to task statements in the public exam guide
and, where a build was done, has one small, cheap script that demonstrates the concept,
including the anti-patterns the exam tests.

> Independent study repository. Not affiliated with or endorsed by Anthropic.
> It contains no exam questions or exam content. Scripts are learning exercises,
> not production code.

## Structure

| Folder | Focus | Task statements |
|---|---|---|
| `day1/` | Raw-API agentic loop and its anti-patterns | 1.1 |
| `day2/` | Coordinator with subagents via the Agent SDK | 1.2, 1.3, 1.6 |
| `day3/` | Enforcement hooks, prerequisite gates, handoffs, and session resume/fork | 1.4, 1.5, 1.7 |
| (no folder) | Day 4: tool design and MCP. Studied as concepts and exam-style questions; no lab built | 2.1, 2.2, 2.3, 2.4 |
| (no folder) | Day 5: built-in tools and escalation. Studied as concepts and exam-style questions; no lab built | 2.5, 5.2 |

Further days (Claude Code configuration, CI/CD review, structured extraction, context
management) will be added as I complete them.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install anthropic claude-agent-sdk python-dotenv
cp .env.example .env      # then fill in your values
```

`.env` variables:

```
ANTHROPIC_API_KEY=
CLAUDE_MODEL=
```

Day 3 session experiments also use the Claude Code CLI (`claude -p`), so it needs to be
installed and on your PATH. API spend is kept low by using a small model and local-only
tests wherever possible.

## What each day demonstrates

**Day 1: agentic loop.** Continue on `stop_reason == "tool_use"`, append tool
results, stop on `"end_turn"`. Variants reproduce the three anti-patterns: an
iteration cap as the main stop, parsing text for a "done" marker, and treating
text presence as completion.

**Day 2: orchestration.** A coordinator delegates to `doc_analysis_agent` and
`synthesis_agent` defined with `AgentDefinition`. Observations from real runs:
independent delegations were emitted together, then a dependent synthesis call
followed; each subagent received its full context in its prompt; a loosely
defined `source_name` field produced filenames instead of document sources; and a
word limit in the subagent definition was overridden by the delegation prompt.

**Day 3: enforcement, hooks, and sessions.**
- Local unit tests cover a prerequisite gate (multiple customer matches do not count
  as verified), a refund limit interception at the boundary (499, 500, 501), a
  normalizer for epoch and ISO timestamps and numeric status codes (unknown codes
  preserved), and a handoff builder that rejects missing fields.
- A live Agent SDK run showed a `PreToolUse` denial of a $750 refund overriding a
  system prompt that said any amount was allowed. The model then escalated with all
  four handoff fields, and no `PostToolUse` event fired for the denied call.
- Session experiments with `claude -p`: named sessions, a duplicate name forcing a
  resume by session ID, a stale resume answering from old tool results, resume with an
  explicit note about changed files correcting the answer, and `--fork-session`
  producing two independent branches with no leakage.
- Known gaps: the verification gate never fired live (the model verified on its own),
  live `PostToolUse` normalization was not built, and the final customer message
  wrongly claimed the refund had been processed even though it was blocked. That last
  one is a reminder that enforcement in code does not guarantee the model's wording.

**Day 4: tool design and MCP (concepts only).** No lab was built. Topics covered:
tool descriptions as the main selection mechanism, structured MCP errors
(`isError`, error category, retryability, valid empty result vs access failure),
tool distribution and `tool_choice` (`auto`, `any`, forced), and MCP scoping
(`.mcp.json` vs `~/.claude.json`, `${VAR}` expansion, resources vs tools).

**Day 5: built-in tools and escalation (concepts only).** No lab was built (API spend
is capped and the Day 4 MCP server was never built). Topics covered:
- Built-in tools: Grep searches file contents, Glob matches file paths, Read and Write
  operate on whole files, and Edit makes targeted changes by matching unique text.
  When Edit fails on a non-unique anchor, the reliable fallback is Read the full file,
  modify it, then Write it back. Codebase exploration is incremental (Grep for entry
  points, then Read to follow imports) rather than reading everything upfront, and
  wrapper modules are traced by listing their exported names first and then searching
  for each name.
- Escalation: valid triggers are an explicit request for a human (honored immediately,
  without investigating first), a policy that is silent or ambiguous on the request,
  and an inability to make progress. Frustration alone is not a request for a human, so
  the agent acknowledges it and offers resolution when the issue is in scope. Multiple
  customer matches call for an additional identifier, never a heuristic pick. Complexity
  alone is not a trigger, and a multi-issue message is decomposed and investigated per
  issue using shared verified context.

## Design patterns I keep applying

- Rules that must always hold belong in code (hooks, prerequisite gates), not prompts.
- Pick the proportionate fix for the root cause before adding infrastructure.
- Subagents inherit no context: pass what they need explicitly and in structured form.
- Route inter-agent communication through the coordinator for observability.
- Tool selection starts with the tool description; fix thin or overlapping descriptions
  before adding examples, routers, or consolidation. Check the system prompt for
  keyword-triggered instructions if misrouting persists.
- Use `tool_choice` rather than prompt wording when a tool call or a first step must be guaranteed.
- Return structured tool errors (category, retryable flag, readable reason) so the agent
  can retry, explain, or escalate correctly, and keep valid empty results separate from failures.
- Give each agent only the tools its role needs; put shared config in project scope and
  secrets in environment variables, never in committed files.
- Match the built-in tool to the operation: Grep for contents, Glob for paths, and Read
  plus Write when Edit cannot find a unique anchor. Write has a larger blast radius than
  Edit, so keep it for full rewrites and the fallback case.
- Calibrate escalation with explicit criteria and few-shot examples in the system prompt.
  Do not use sentiment or self-reported confidence as triggers; they are poor proxies
  for case complexity.
- When a customer lookup returns several matches, ask for another identifier rather than
  guessing, and do not treat the result as a verified customer.