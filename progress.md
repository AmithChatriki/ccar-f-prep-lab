# CCAR-F Progress Tracker

- Exam: Claude Certified Architect – Foundations (CCAR-F)
- Target exam date: (not set)
- Last updated: 2026-10-31
- Current day: Day 9
- Days completed: 8 / 10

## Status key
- Days: Not started | In progress | Done | Needs review
- Task statements: Not started | Learning | Solid
  - Learning = studied, but mastery check not yet passed
  - Solid = answered the mastery check and exam-style questions correctly

## Day tracker

| Day | Focus | Status | Mastery check | Quiz score | Completed on |
|---|---|---|---|---|---|
| 1 | Baseline and agentic loop | Done | Passed (MCQ format) | 3/3 | 2026-09-27 |
| 2 | Multi-agent orchestration | Done | Partial (missed refinement loop option on a select-2 question; re-check on that concept passed 2026-10-21) | 3/3 | 2026-10-21 |
| 3 | Enforcement, hooks, and sessions | Done | Passed (MCQ format, 5/5) | 3/3 | 2026-10-22 |
| 4 | Tool design and MCP | Done | Passed (MCQ format, 4/4) | 3/3 | 2026-10-27 |
| 5 | Built-in tools and escalation | Done | Passed (MCQ format, 4/4) | 3/3 | 2026-10-27 |
| 6 | Claude Code configuration | Done | Passed (MCQ format, 4/4) | 3/3 | 2026-10-29 |
| 7 | CI/CD and review architectures | Done | Passed (MCQ format, 4/4) | 3/3 | 2026-10-30 |
| 8 | Structured output and extraction | Done | Passed (MCQ format, 4/4) | 3/3 | 2026-10-31 |
| 9 | Context management and reliability | In progress | - | - | - |
| 10 | Mock exam and consolidation | Not started | - | - | - |

## Task statement coverage

| TS | Topic | Day | Status |
|---|---|---|---|
| 1.1 | Agentic loops and stop_reason | 1 | Solid |
| 1.2 | Coordinator-subagent orchestration | 2 | Solid |
| 1.3 | Subagent invocation and context passing | 2 | Solid |
| 1.4 | Workflow enforcement and handoff | 3 | Solid |
| 1.5 | Agent SDK hooks | 3 | Solid |
| 1.6 | Task decomposition strategies | 2 | Solid |
| 1.7 | Session resume and fork | 3 | Solid |
| 2.1 | Tool interface design | 4 | Solid |
| 2.2 | Structured MCP error responses | 4 | Solid |
| 2.3 | Tool distribution and tool_choice | 4 | Solid |
| 2.4 | MCP server integration and scoping | 4, 6 | Solid |
| 2.5 | Built-in tools (Read, Write, Edit, Bash, Grep, Glob) | 5 | Solid |
| 3.1 | CLAUDE.md hierarchy and @import | 6 | Solid |
| 3.2 | Slash commands and skills | 6 | Solid |
| 3.3 | Path-specific rules | 6 | Solid |
| 3.4 | Plan mode vs direct execution | 6 | Solid |
| 3.5 | Iterative refinement techniques | 7 | Solid |
| 3.6 | Claude Code in CI/CD | 7 | Solid |
| 4.1 | Explicit criteria and false positives | 7 | Solid |
| 4.2 | Few-shot prompting | 8 | Solid |
| 4.3 | Structured output via tool use and JSON schemas | 8 | Solid |
| 4.4 | Validation, retry, and feedback loops | 8 | Solid |
| 4.5 | Message Batches API strategy | 8 | Solid |
| 4.6 | Multi-instance and multi-pass review | 7 | Solid |
| 5.1 | Preserving context in long interactions | 9 | Not started |
| 5.2 | Escalation and ambiguity resolution | 5 | Solid |
| 5.3 | Error propagation across agents | 9 | Not started |
| 5.4 | Context in large codebase exploration | 9 | Not started |
| 5.5 | Human review and confidence calibration | 9 | Not started |
| 5.6 | Provenance and multi-source synthesis | 9 | Not started |

## Hands-on exercises

| Exercise | Built on | Status | Notes |
|---|---|---|---|
| Raw API agentic loop | Day 1 | Done | Ran correct_loop.py plus all 3 anti-pattern variants; observed text+tool_use coexistence, iteration cap truncation, text-marker false negative, text-presence false positive |
| Ex 4: Multi-agent research pipeline | Days 2, 9 | In progress | Day 2 part done on local docs only (cost-conscious): coordinator plus doc_analysis_agent and synthesis_agent via AgentDefinition; observed 4 independent delegations emitted together then dependent synthesis call; explicit context passing; structured claim/source JSON (source_name field ambiguity caused filename vs document-source mismatch); subagent word cap not honored when delegation prompt asked for more. Not built: refinement loop, chain vs dynamic comparison, error propagation, conflict handling (Day 9) |
| Hooks, gates, and sessions | Day 3 | Done | Local unit tests: prerequisite gate (multiple matches do not verify), $500 interception boundary (499/500/501), normalizer (epoch/ISO, status codes, unknown code preserved), handoff builder rejecting missing fields. Live Agent SDK run (Haiku, about $0.04): PreToolUse deny on a $750 refund overrode a system prompt saying any amount is allowed; model then escalated with all four handoff fields; no PostToolUse event for the denied call; tool_response arrived as a list. Sessions via claude -p: -n naming, duplicate name forced resume by session ID, stale resume answered 500 when file was 300, resume-and-inform corrected to 300 and flagged cross-file mismatch, --fork-session produced two independent branches with no leakage. Gaps: verification gate never fired live (model verified on its own); live PostToolUse normalization with updatedToolOutput not built; final customer message falsely said refund was processed with a 1-2 day timeline |
| Ex 1: Support agent with escalation | Days 4, 5, 9 | In progress | Day 4 build skipped by decision (user already has hands-on MCP experience): local MCP server with four tools, structured error tests, minimal vs detailed description comparison, tool_choice experiments, and resource catalog not built. Resource catalog covered with a worked example in chat only. Day 5 build skipped by decision (cost cap; Day 4 MCP server never built): escalation criteria with few-shot prompt, five escalation test cases, and the Grep/Glob/Read/Edit-failure repo exercise not built; TS 2.5 and TS 5.2 taught in chat with 4 mid-lesson checks (4/4) and covered by exam-style questions instead. Remaining: context handling (Day 9) |
| Ex 2: Claude Code team configuration | Day 6 | Skipped by decision | Day 6 build skipped by decision (no build requested; judgment content covered through questions). Not built: CLAUDE.md at user/project/subdirectory levels with @import and /memory check, .claude/rules/ paths: files, .claude/commands/ command, skill with context: fork / allowed-tools / argument-hint plus personal variant, .mcp.json with ${VAR} alongside ~/.claude.json, plan mode vs direct execution on three tasks, Explore subagent. Worked examples of a command and a skill were shown in chat only. Exact frontmatter format (paths, allowed-tools, name, description) to be verified in current docs before real use |
| CI review pipeline | Day 7 | Skipped by decision | Day 7 build skipped by decision (cost cap, consistent with Days 4 to 6; judgment content covered through questions). Not built: claude -p with --output-format json and --json-schema producing findings, explicit report/skip criteria with severity examples, per-file passes plus cross-file integration pass, independent reviewer instance, re-review with prior findings, iterative refinement drills. Worked examples shown in chat only (findings schema and JSON output, per-file plus integration pass on a three-file order module, with-and-without --json-schema comparison). Exact --json-schema value format (inline vs file) and the envelope location of the schema-conforming result to be verified in current CLI docs before real use |
| Ex 3: Structured extraction pipeline | Days 8, 9 | In progress | Day 8 build not reported by user at completion; no build recorded (not confirmed as skipped by decision). Judgment content covered in chat and through questions; worked examples in chat only (SLA arithmetic with 4/6/12-hour intervals, custom_id audit trail with chunked resubmission). Not built: nullable/unclear/other schema with absent-field tests, Pydantic validation-retry loop with retry-fixes vs cannot-fix log, calculated_total vs stated_total and conflict_detected, few-shot comparison on varied formats, Batches job with custom_id and failure resubmission, tool_choice auto/any/forced experiments. Remaining: Day 9 human review routing, field-level confidence, accuracy by document type and field. Exact tool_choice request shape, strict tool use setting, and Message Batches request/result format to be verified in current API docs before real use |

## Governance lens coverage

| Governance idea | Day | Status |
|---|---|---|
| Enforcing policy | 3 | Done (Day 3: prerequisite gate and PreToolUse refund limit enforced in code, verified live over a contradicting prompt) |
| Least privilege | 4, 6 | Done (Day 4 covered: scoped subagent toolsets, constrained tools such as load_document, scoped verify_fact, user-scoped experimental MCP servers; Day 5 touched: Bash as the broadest built-in, Write vs Edit blast radius; Day 6 covered: skill allowed-tools excluding Bash as a capability-level control vs CLAUDE.md instructions) |
| Human oversight | 5, 9 | In progress (Day 5 covered: explicit escalation criteria with few-shot examples, honoring explicit requests for a human, policy gaps as triggers, structured handoff for agents without transcript access, clarification over heuristic selection; Day 6 touched: plan mode as a review checkpoint; Day 7 touched: test-first iteration and the interview pattern as human checkpoints on design and acceptance criteria; Day 8 touched: errors retry cannot fix (absent information, conflicting source data) route to review via null and conflict_detected rather than looping, keeping human review until accuracy is measured by segment; Day 9 to add confidence-based routing to human review) |
| Handling secrets | 6 | Done (Day 6: ${VAR} expansion in .mcp.json keeps tokens out of version control; hardcoded tokens are the anti-pattern) |
| Configuration scope | 6 | Done (Day 6: project vs user CLAUDE.md, commands, skills, and MCP servers; /memory as the diagnostic for what loaded) |
| Auditability and traceability | 2, 7, 9 | In progress (Day 2 covered: coordinator routing as the single observation point; Day 3 touched: hook logging of allowed and denied attempts; Day 4 touched: categorized structured errors as an audit record; Day 7 covered: schema-constrained findings as a storable record, detected_pattern for analyzing dismissed findings, prior-findings context across commits, per-pass traceability of which pass raised or missed a finding; Day 8 covered: custom_id as a per-document record of submission, failure, and modified resubmission, conflict_detected and logged retry error categories; Day 9 to add claim-source mappings and coverage gaps) |
| Quality assurance | 8, 9 | In progress (Day 7 touched: independent review instance as a quality control, per-file plus integration passes, false-positive rate as a trust metric; Day 8 covered: schema validation as the syntax layer, calculated_total vs stated_total as the semantic layer, sample-first prompt refinement before batch volume, 96% aggregate pass rate masking a failing document type and field; Day 9 to add stratified sampling and accuracy by segment) |

## Weak spots
(Claude adds entries here as: TS number, what went wrong, what to revisit. Resolved entries are marked resolved, not deleted.)

- None yet — domain-level signal only so far (D5, D1, D3 below D4/D2 on the quick mock). Will pin to specific task statements as they surface on Days 2, 3, 6, 9. Days 6, 7, and 8 produced no misses on D3 task statements 3.1 to 3.6 or on TS 4.1 to 4.6.
- TS 1.2 (2026-10-21, resolved 2026-10-21): On a select-2 question about narrow decomposition, chose only the upstream decomposition fix and missed the iterative refinement loop (coordinator evaluates synthesis for gaps, re-delegates targeted queries, re-invokes synthesis until coverage is sufficient). User reported knowing the refinement option was correct but not noticing the select-2 count; re-check question on the refinement loop answered correctly (A and B). Habit to keep: find the "select N" count before reading the options.

## Quiz and practice log

| Date | Topic | Score | Missed TS |
|---|---|---|---|
| 2026-09-27 | TS 1.1 (agentic loop, stop_reason, anti-patterns, model-driven vs. decision trees) | 3/3 | None |
| 2026-10-21 | Day 2 completion: TS 1.2, 1.3, 1.6 (3 mastery checks, 3 scenario questions, plus 2 mid-lesson checks 2/2) | Scenario 3/3; mastery 2 full + 1 partial | 1.2 |
| 2026-10-21 | TS 1.2 re-check (iterative refinement loop, select-2) | 1/1 | None |
| 2026-10-22 | Day 3 completion: TS 1.4, 1.5, 1.7 (5 mastery checks, 3 scenario questions, plus 6 mid-lesson checks 6/6) | Scenario 3/3; mastery 5/5 | None |
| 2026-10-27 | Day 4 completion: TS 2.1, 2.2, 2.3, 2.4 (4 mastery checks, 3 scenario questions, plus 5 mid-lesson checks 5/5) | Scenario 3/3; mastery 4/4 | None |
| 2026-10-27 | Day 5 completion: TS 2.5, 5.2 (4 mastery checks, 3 scenario questions including the TS 1.4 multi-issue carryover, plus 4 mid-lesson checks 4/4) | Scenario 3/3; mastery 4/4 | None |
| 2026-10-29 | Day 6 completion: TS 3.1, 3.2, 3.3, 3.4 plus TS 2.4 scope/secrets angle (4 mastery checks, 3 scenario questions, plus 5 mid-lesson checks 5/5) | Scenario 3/3; mastery 4/4 | None |
| 2026-10-30 | Day 7 completion: TS 3.5, 3.6, 4.1, 4.6 (4 mastery checks, 3 scenario questions, plus 4 mid-lesson checks 4/4) | Scenario 3/3; mastery 4/4 | None |
| 2026-10-31 | Day 8 completion: TS 4.2, 4.3, 4.4, 4.5 (4 mastery checks, 3 scenario questions, plus 4 mid-lesson checks 4/4) | Scenario 3/3; mastery 4/4 | None |

## Diagnostic and mock exam results

| Date | Test | Score | Weakest domains |
|---|---|---|---|
| 2026-09-26 | Quick mock (28 Q, claudecertificationguide.com) | 747/1000, 21/28 (75%), passed | D5 (60%), D1 and D3 tied (67% each) |
| - | Full mock exam | - | - |

## Notes
- Formal diagnostic test skipped by decision; quick mock domain breakdown adopted as baseline instead.
- Day 1 mastery check redone in MCQ format after initial free-response drilling was flagged as not reflecting real exam format (see recent memory update). All future mastery checks and quizzes use MCQ/multi-select format matching the actual exam.
- Hands-on tasks are kept short and low-cost (API spend is capped); prefer local-only builds and cheaper models for build days, and cover judgment-only topics with questions instead of paid runs.
- The installed Claude Code CLI reports the subagent spawn tool as "Agent"; the exam guide and SDK docs call it "Task". Use "Task" for exam answers.
- Day 3 onward: the user does not watch the YouTube prep video; all topics are taught in chat, one topic at a time with a mid-lesson MCQ check.
- Spelling differences to remember: the CLI flag is --fork-session while the guide and SDK use fork_session; the interception hook event is PreToolUse (the guide describes it without naming the event).
- Shell setup: load the project-root .env with set -a; source .env; set +a (values are quoted, so cut leaves literal quotes and causes an invalid API key error).
- Day 4: the user skipped the build by choice (prior hands-on MCP experience); judgment content was covered through questions instead. MCP resources (catalog vs tool, resources/list and resources/read, @ mentions in Claude Code) were explained with a worked example.
- Day 5: the user skipped the build by choice; TS 2.5 and TS 5.2 were taught in chat (wrapper tracing, Edit failure fallback to Read plus Write, escalation triggers, policy gaps, multiple matches). The multi-issue message case (TS 1.4 carryover, not taught on Day 5) was covered in scenario question 1 and answered correctly. The select-N counting habit held on all select-2 questions.
- Day 6: taught in chat (TS 3.1 to 3.4, plus TS 2.4 scope/secrets and a light pass on permission modes without asserting exact mode names). The user asked whether ~/.claude/commands supports version control (it does not; scope follows location) and requested worked examples of a command and a skill. The select-N counting habit held on all select-2 questions. Permission mode names, skill frontmatter format, and path-rule syntax were not verified against current docs; verify before real use.
- Day 7: taught in chat (TS 3.6, 4.1, 4.6, 3.5, one topic at a time with a mid-lesson check each, 4/4). The user asked for worked examples of --output-format json with --json-schema, of --output-format json without --json-schema (valid JSON envelope with a prose payload, so findings still need the schema), and of per-file plus cross-file integration passes. The select-N counting habit held on all select-2 questions. --json-schema value format and envelope layout not verified against current docs; verify before real use.
- Day 8: taught in chat (TS 4.3, 4.4, 4.2, 4.5, one topic at a time with a mid-lesson check each, 4/4). The user asked what an SLA is and for a simple custom_id audit example; both were explained with worked examples (30-hour SLA with 24-hour batches: interval <= SLA - 24, so 4 hours gives 28-hour worst case; custom_id trail with chunked resubmission). The select-N counting habit held on all select-2 questions. Recurring Day 8 patterns: schema validity is not correctness; retry works only when the information is present in the source; systematic misses on an input shape call for 2 to 4 targeted few-shot examples; batch fits only latency-tolerant work and cannot do multi-turn tool calling; aggregate pass rates can hide failing document types and fields. Day 8 build not reported at completion. The tool_choice request shape (guide shows bare "auto" and "any" strings), strict tool use setting, and Message Batches request/result format not verified against current docs; verify before real use.