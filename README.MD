# ccar-f-prep-lab

Hands-on labs and notes from my preparation for the Claude Certified Architect –
Foundations (CCAR-F) exam. Each day maps to task statements in the public exam guide
and has one small, cheap script that demonstrates the concept, including the
anti-patterns the exam tests.

> Independent study repository. Not affiliated with or endorsed by Anthropic.
> It contains no exam questions or exam content. Scripts are learning exercises,
> not production code.

## Structure

| Folder | Focus | Task statements |
|---|---|---|
| `day1/` | Raw-API agentic loop and its anti-patterns | 1.1 |
| `day2/` | Coordinator with subagents via the Agent SDK | 1.2, 1.3, 1.6 |

Further days (hooks and sessions, tool design and MCP, Claude Code configuration,
CI/CD review, structured extraction, context management) will be added as I
complete them.

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

## Design patterns I keep applying

- Rules that must always hold belong in code (hooks, prerequisite gates), not prompts.
- Pick the proportionate fix for the root cause before adding infrastructure.
- Subagents inherit no context: pass what they need explicitly and in structured form.
- Route inter-agent communication through the coordinator for observability.

## Notes

- The Claude Code CLI I run reports the subagent spawn tool as `Agent`; the exam
  guide and SDK docs call it `Task`.
- `.env` and the exam guide PDF are intentionally not committed.