# ccar-f-prep-lab

Labs and notes from my preparation for the Claude Certified Architect – Foundations
(CCAR-F) exam. Where a build was done, each day has one small, cheap script that
demonstrates the concept, including the anti-patterns the exam tests.

> Independent study repository. Not affiliated with or endorsed by Anthropic.
> It contains no exam questions or exam content. Scripts are learning exercises,
> not production code.

## Structure

| Folder | Focus | Task statements |
|---|---|---|
| `day1/` | Raw-API agentic loop and its anti-patterns | 1.1 |
| `day2/` | Coordinator with subagents via the Agent SDK | 1.2, 1.3, 1.6 |
| `day3/` | Enforcement hooks, prerequisite gates, handoffs, session resume/fork | 1.4, 1.5, 1.7 |
| (none) | Day 4: tool design and MCP (concepts only) | 2.1 to 2.4 |
| (none) | Day 5: built-in tools and escalation (concepts only) | 2.5, 5.2 |
| (none) | Day 6: Claude Code configuration (concepts only) | 3.1 to 3.4 |

Later days will be added as I complete them.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install anthropic claude-agent-sdk python-dotenv
cp .env.example .env      # then fill in ANTHROPIC_API_KEY and CLAUDE_MODEL
```

Day 3 session experiments also need the Claude Code CLI (`claude -p`) on your PATH.
API spend is kept low with a small model and local-only tests.

## What was built

**Day 1.** Agentic loop: continue on `stop_reason == "tool_use"`, append tool results,
stop on `"end_turn"`. Variants reproduce three anti-patterns: iteration cap as the main
stop, parsing text for "done", and treating text presence as completion.

**Day 2.** A coordinator delegates to two subagents defined with `AgentDefinition`.
Observed: independent delegations emitted together, subagents needing full context in
their prompts, a loose `source_name` field producing filenames instead of sources, and a
delegation prompt overriding a subagent's word limit.

**Day 3.**
- Local tests: prerequisite gate, refund limit at the boundary (499, 500, 501), data
  normalizer, handoff builder that rejects missing fields.
- Live run: a `PreToolUse` denial of a $750 refund overrode a prompt that allowed any
  amount, and the model then escalated.
- Sessions via `claude -p`: named sessions, stale resume vs resume with changed-file
  notes, and `--fork-session` branches with no leakage.
- Gaps: the verification gate never fired live, `PostToolUse` normalization was not built
  live, and the final customer message wrongly said the blocked refund was processed.
  Enforcement in code does not guarantee the model's wording.

**Days 4 to 6.** Concepts only, no lab built (API spend is capped). Day 6 notes: the
exact frontmatter format for `paths`, `allowed-tools`, and skill keys should be checked
against current Claude Code docs before use in a real repo.

## Design patterns I keep applying

- Rules that must always hold belong in code (hooks, gates), not prompts.
- Pick the proportionate fix for the root cause before adding infrastructure.
- Subagents inherit no context: pass it explicitly, in structured form, via the coordinator.
- Fix thin tool descriptions before adding examples, routers, or consolidation.
- Use `tool_choice` when a tool call must be guaranteed.
- Return structured tool errors (category, retryable flag, reason); keep valid empty
  results separate from failures.
- Least privilege: scope each agent's tools, and restrict skills with `allowed-tools`.
- Scope follows location: team-shared config (CLAUDE.md, commands, skills, `.mcp.json`)
  lives in the repo, personal config under `~`. Secrets go in `${VAR}`, never committed.
  When behavior differs between developers, check what loaded with `/memory`.
- Match mechanism to when content applies: CLAUDE.md for always-on standards, path-scoped
  rules for file-type conventions, skills for deliberate workflows.
- Match the built-in tool to the job: Grep for contents, Glob for paths, Read plus Write
  when Edit has no unique anchor.
- Escalate on explicit requests, policy gaps, or no progress, not on sentiment or
  self-reported confidence. Multiple customer matches mean asking for another identifier.
- Plan mode for decisions and large surfaces; direct execution for well-scoped changes.