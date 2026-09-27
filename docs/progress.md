# CCAR-F Progress Tracker

- Exam: Claude Certified Architect – Foundations (CCAR-F)
- Target exam date: (not set)
- Last updated: 2026-09-27
- Current day: Day 2
- Days completed: 1 / 10

## Status key
- Days: Not started | In progress | Done | Needs review
- Task statements: Not started | Learning | Solid
  - Learning = studied, but mastery check not yet passed
  - Solid = answered the mastery check and exam-style questions correctly

## Day tracker

| Day | Focus | Status | Mastery check | Quiz score | Completed on |
|---|---|---|---|---|---|
| 1 | Baseline and agentic loop | Done | Passed (MCQ format) | 3/3 | 2026-09-27 |
| 2 | Multi-agent orchestration | Not started | - | - | - |
| 3 | Enforcement, hooks, and sessions | Not started | - | - | - |
| 4 | Tool design and MCP | Not started | - | - | - |
| 5 | Built-in tools and escalation | Not started | - | - | - |
| 6 | Claude Code configuration | Not started | - | - | - |
| 7 | CI/CD and review architectures | Not started | - | - | - |
| 8 | Structured output and extraction | Not started | - | - | - |
| 9 | Context management and reliability | Not started | - | - | - |
| 10 | Mock exam and consolidation | Not started | - | - | - |

## Task statement coverage

| TS | Topic | Day | Status |
|---|---|---|---|
| 1.1 | Agentic loops and stop_reason | 1 | Solid |
| 1.2 | Coordinator-subagent orchestration | 2 | Not started |
| 1.3 | Subagent invocation and context passing | 2 | Not started |
| 1.4 | Workflow enforcement and handoff | 3 | Not started |
| 1.5 | Agent SDK hooks | 3 | Not started |
| 1.6 | Task decomposition strategies | 2 | Not started |
| 1.7 | Session resume and fork | 3 | Not started |
| 2.1 | Tool interface design | 4 | Not started |
| 2.2 | Structured MCP error responses | 4 | Not started |
| 2.3 | Tool distribution and tool_choice | 4 | Not started |
| 2.4 | MCP server integration and scoping | 4, 6 | Not started |
| 2.5 | Built-in tools (Read, Write, Edit, Bash, Grep, Glob) | 5 | Not started |
| 3.1 | CLAUDE.md hierarchy and @import | 6 | Not started |
| 3.2 | Slash commands and skills | 6 | Not started |
| 3.3 | Path-specific rules | 6 | Not started |
| 3.4 | Plan mode vs direct execution | 6 | Not started |
| 3.5 | Iterative refinement techniques | 7 | Not started |
| 3.6 | Claude Code in CI/CD | 7 | Not started |
| 4.1 | Explicit criteria and false positives | 7 | Not started |
| 4.2 | Few-shot prompting | 8 | Not started |
| 4.3 | Structured output via tool use and JSON schemas | 8 | Not started |
| 4.4 | Validation, retry, and feedback loops | 8 | Not started |
| 4.5 | Message Batches API strategy | 8 | Not started |
| 4.6 | Multi-instance and multi-pass review | 7 | Not started |
| 5.1 | Preserving context in long interactions | 9 | Not started |
| 5.2 | Escalation and ambiguity resolution | 5 | Not started |
| 5.3 | Error propagation across agents | 9 | Not started |
| 5.4 | Context in large codebase exploration | 9 | Not started |
| 5.5 | Human review and confidence calibration | 9 | Not started |
| 5.6 | Provenance and multi-source synthesis | 9 | Not started |

## Hands-on exercises

| Exercise | Built on | Status | Notes |
|---|---|---|---|
| Raw API agentic loop | Day 1 | Done | Ran correct_loop.py plus all 3 anti-pattern variants; observed text+tool_use coexistence, iteration cap truncation, text-marker false negative, text-presence false positive |
| Ex 4: Multi-agent research pipeline | Days 2, 9 | Not started | - |
| Hooks, gates, and sessions | Day 3 | Not started | - |
| Ex 1: Support agent with escalation | Days 4, 5, 9 | Not started | - |
| Ex 2: Claude Code team configuration | Day 6 | Not started | - |
| CI review pipeline | Day 7 | Not started | - |
| Ex 3: Structured extraction pipeline | Days 8, 9 | Not started | - |

## Governance lens coverage

| Governance idea | Day | Status |
|---|---|---|
| Enforcing policy | 3 | Not started |
| Least privilege | 4, 6 | Not started |
| Human oversight | 5, 9 | Not started |
| Handling secrets | 6 | Not started |
| Configuration scope | 6 | Not started |
| Auditability and traceability | 2, 7, 9 | Not started |
| Quality assurance | 9 | Not started |

## Weak spots
(Claude adds entries here as: TS number, what went wrong, what to revisit. Resolved entries are marked resolved, not deleted.)

- None yet — domain-level signal only so far (D5, D1, D3 below D4/D2 on the quick mock). Will pin to specific task statements as they surface on Days 2, 3, 6, 9.

## Quiz and practice log

| Date | Topic | Score | Missed TS |
|---|---|---|---|
| 2026-09-27 | TS 1.1 (agentic loop, stop_reason, anti-patterns, model-driven vs. decision trees) | 3/3 | None |

## Diagnostic and mock exam results

| Date | Test | Score | Weakest domains |
|---|---|---|---|
| 2026-09-26 | Quick mock (28 Q, claudecertificationguide.com) | 747/1000, 21/28 (75%), passed | D5 (60%), D1 and D3 tied (67% each) |
| - | Full mock exam | - | - |

## Notes
- Formal diagnostic test skipped by decision; quick mock domain breakdown adopted as baseline instead.
- Day 1 mastery check redone in MCQ format after initial free-response drilling was flagged as not reflecting real exam format (see recent memory update). All future mastery checks and quizzes use MCQ/multi-select format matching the actual exam.