# ccar-f-prep-lab

Notes and small labs from my preparation for the Claude Certified Architect
exams: Foundations (CCAR-F) and Professional (CCAR-P).

> Independent study repository. Not affiliated with or endorsed by Anthropic.
> It contains no exam questions or exam content. Scripts are learning exercises,
> not production code.

## Status

- **CCAR-F:** preparation closed (10 days recorded; Day 10 closed by my own
  decision). The official exam has not been taken.
- **CCAR-P:** in progress since 2026-11-01 on an 8-day plan. Days 1 to 7 are
  complete. Preparation is chat-based with multiple-choice checks, so no scripts
  are added to this repository for it.

Day-by-day progress, objective coverage, weak spots, and unverified items are
tracked in `ccar-p-progress.md` (CCAR-P) and `ccar-f-progress.md` (CCAR-F).

## What was built (CCAR-F)

| Folder | What it demonstrates | Task statements |
|---|---|---|
| `day1/` | Raw-API agentic loop (`stop_reason` handling) and three anti-pattern variants | 1.1 |
| `day2/` | Coordinator with two subagents via `AgentDefinition` | 1.2, 1.3, 1.6 |
| `day3/` | Hooks, prerequisite gate, refund limit, handoff builder, session resume and fork | 1.4, 1.5, 1.7 |

Days 4 to 10 had no lab built because API spend is capped. Known gaps in the Day 3
lab: the verification gate never fired live, `PostToolUse` normalization was not
built live, and the final customer message wrongly said a blocked refund was
processed (enforcement in code does not guarantee the model's wording).

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install anthropic claude-agent-sdk python-dotenv
cp .env.example .env      # fill in ANTHROPIC_API_KEY and CLAUDE_MODEL
```