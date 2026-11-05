# ccar-f-prep-lab

Labs and notes from my preparation for the Claude Certified Architect – Foundations
(CCAR-F) exam. Where a build was done, each day has one small, cheap script that
demonstrates the concept, including the anti-patterns the exam tests.

> Independent study repository. Not affiliated with or endorsed by Anthropic.
> It contains no exam questions or exam content. Scripts are learning exercises,
> not production code.

## Status

Foundations preparation is closed: all 10 days are recorded, with Day 10 closed by my own
decision rather than by completing every planned step. The official CCAR-F exam has not
been taken.

I am now preparing for the Claude Certified Architect – Professional (CCAR-P) exam.
Preparation started on 2026-11-01. Days 1 (RAG and retrieval), 2 (models, prompting,
caching, context), and 3 (evaluation and optimization) are complete as concepts only.
See the CCAR-P section below.

## Structure

| Folder | Focus | Task statements |
|---|---|---|
| `day1/` | Raw-API agentic loop and its anti-patterns | 1.1 |
| `day2/` | Coordinator with subagents via the Agent SDK | 1.2, 1.3, 1.6 |
| `day3/` | Enforcement hooks, prerequisite gates, handoffs, session resume/fork | 1.4, 1.5, 1.7 |
| (none) | Day 4: tool design and MCP (concepts only) | 2.1 to 2.4 |
| (none) | Day 5: built-in tools and escalation (concepts only) | 2.5, 5.2 |
| (none) | Day 6: Claude Code configuration (concepts only) | 3.1 to 3.4 |
| (none) | Day 7: CI/CD and review architectures (concepts only) | 3.5, 3.6, 4.1, 4.6 |
| (none) | Day 8: structured output and extraction (concepts only so far) | 4.2 to 4.5 |
| (none) | Day 9: context management and reliability (concepts only) | 5.1, 5.3 to 5.6 |
| (none) | Day 10: mock exam and consolidation (closed by decision) | all |

Foundations preparation is closed, so no further days will be added.

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

**Days 4 to 7.** Concepts only, no lab built (API spend is capped). Day 6 notes: the
exact frontmatter format for `paths`, `allowed-tools`, and skill keys should be checked
against current Claude Code docs before use in a real repo. Day 7 notes: the CI review
pipeline (`claude -p` with `--output-format json` and `--json-schema`) was not built; the
`--json-schema` value format (inline vs file) and where the schema-conforming result sits
in the JSON output should be checked against current CLI docs before scripting against it.

**Day 8.** Concepts only so far; the extraction pipeline lab (Exercise 3) has not been
built. Worked through in notes and questions: extraction tools with JSON schemas,
`tool_choice` (`auto` vs `any` vs forced), nullable/`unclear`/`other` schema design,
validation-retry with specific error feedback, `calculated_total` vs `stated_total` and
`conflict_detected`, few-shot examples for varied layouts, and Message Batches strategy
(`custom_id`, chunked resubmission, SLA arithmetic). Notes: check the current API docs
for the exact `tool_choice` request shape, the strict tool use setting, and the Message
Batches request and result format before scripting against them.

**Day 9.** Concepts only, no lab built (API spend is capped). Not built: the case-facts
block and trimmed order lookups for the support agent, the research pipeline remainder
(structured error propagation from a simulated subagent timeout, conflict annotation with
dates, claim-source mappings, coverage-gap notes, crash-recovery manifest), a scratchpad
and `/compact` exploration session, and the extraction pipeline's field-level confidence,
calibrated routing, accuracy by document type and field, and stratified sampling. Worked
through in notes and questions: progressive summarization loss, lost-in-the-middle
placement, structured error context vs generic status, valid empty results vs access
failures, claim-source mappings with publication dates, and why aggregate accuracy can
mislead.

**Day 10.** No lab built. One full timed mock exam from an unofficial third-party source
was completed in a single sitting without notes, and it produced no misses to classify.
Closed by my own decision: the 30-task-statement one-or-two-sentence self-check, a second
full mock from a different source, and the drill of weakest domains were skipped. The
official CCAR-F exam has not been taken. Mock exams from third parties are unofficial and
their scores are not comparable to the official scaled score.

## CCAR-P (Professional) preparation

An 8-day provisional plan against the official CCAR-P exam guide (v1.0, July 2026). I
chose to skip the hands-on builds for CCAR-P, so preparation is chat-based with
multiple-choice and multiple-select checks, and no scripts are added to this repository
for it.

| Day | Focus | Status |
|---|---|---|
| 1 | RAG and retrieval (chunking, indexing, retrieval strategy, diagnosis) | Done (concepts only, build skipped by decision) |
| 2 | Models, prompting, caching, context | Done (concepts only, build skipped by decision) |
| 3 | Evaluation and optimization | Done (concepts only, build skipped by decision) |
| 4 | Governance, safety, compliance | Not started |
| 5 | Integration protocols, auth, observability | Not started |
| 6 | Stakeholder communication and lifecycle | Not started |
| 7 | Refresh of carried-over content | Not started |
| 8 | Mock exams and consolidation | Not started |

**Day 1.** Worked through in notes and questions: chunk boundaries aligned to document
structure, parent-section retrieval and overlap, table header repetition, metadata for
refresh, filtering and access control, the same embedding model across documents and
queries, BM25 vs dense vs hybrid retrieval, reranking as a two-stage fix, contextual
retrieval for chunks that lose identity, and stage-by-stage diagnosis of wrong answers.
Notes: Anthropic's contextual retrieval benchmark figures are its own published results
and are directional; check the current docs for the embedding provider lineup before
building anything on it.

**Day 2.** Worked through in notes and questions: model selection by task, stage, and
segment (small tier for narrow high-volume work, capable tier for multi-step reasoning,
batch for latency-tolerant work, effort as a per-task cost and latency setting), prompt
caching (`cache_control` breakpoints, stable prefix first, what invalidates the cache,
checking `cache_read_input_tokens`), modular prompts, Skills and progressive disclosure,
context and token budgeting (trimming tool results, retrieval instead of stuffing, facts
carried forward verbatim), system prompts, templates, and layered guardrails, and the
zero-shot, few-shot, and chain-of-thought trade-offs. Not built: a cached vs uncached
comparison with timestamp-in-prefix and breakpoint-on-varying-block variants. Notes: the
model lineup, prices, and cache minimums change, so check the current docs (models
overview, prompt caching, pricing) before relying on any figure; the Skills API request
shape, token counting, context editing, compaction, and tool search were not verified, so
read their docs before building on them.

**Day 3.** Worked through in notes and questions: evaluation metrics tied to business
requirements (accuracy by segment, p95 and p99 latency, cost per successful task, safety
metrics paired with an over-refusal guardrail, security metrics such as injection success
rate), evaluation dataset design (production-shaped distribution, over-represented edge
and adversarial cases, segment tags, a held-out set, refresh from production), mixed
grading (code checks for deterministic fields, a rubric-based LLM grader validated
against human labels, humans on a sampled slice and the highest-risk segment), A/B
testing (same fixed set, one variable at a time, pre-set decision rule and guardrails,
staged rollout with rollback), diagnosis by stage (retrieval vs prompt or grounding vs
hallucination vs model mismatch, including upstream defects such as truncated stage
output), matching the cost or latency lever to the failing metric (caching, streaming,
batch, per-segment model tier, effort, output length), and layered monitoring (provider
usage and cost data, per-stage request logs with a trace ID, sampled production quality
grading, governed logs). Not built: a 30 to 40 case eval set with segment tags and a
held-out portion, a harness mixing code checks with an LLM grader that reports by
segment, an A/B of two prompt versions, and structured per-request logging. Notes: the
latency guidance and the Usage and Cost Admin API were checked in current docs; the
Evaluation Tool mechanics, tracing and OpenTelemetry specifics, and exact effort level
names were not verified, so read their docs before building on them.

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
- In CI, run `claude -p` (non-interactive) and pair `--output-format json` with
  `--json-schema`: the envelope alone is valid JSON around prose, the schema is what makes
  findings machine-parseable. Project context for CI runs comes from CLAUDE.md.
- On re-review, pass prior findings in explicitly and report only new or unaddressed
  issues; for test generation, put existing tests in context to avoid duplicates.
- Reduce false positives with explicit categorical criteria and concrete severity
  examples, not "be conservative" or confidence thresholds. Disable a noisy category
  temporarily while rewriting it, since it erodes trust in the accurate ones.
- Review with an independent instance, not the session that generated the code. Split
  large reviews into per-file passes plus a cross-file integration pass; a larger context
  window or majority voting across repeated passes does not fix attention dilution.
- Fix inconsistent prose interpretation with 2-3 concrete input/output examples or
  test-first iteration; use the interview pattern for unfamiliar domains; send interacting
  issues in one message and independent issues sequentially.
- Tool use with a JSON schema removes syntax errors, not semantic ones. Use
  `tool_choice` `any` when the document type is unknown and several schemas exist, forced
  selection when one extraction must run first, and never `auto` when a tool call must be
  guaranteed.
- Make fields nullable (and add `unclear` or `other` plus a detail string) when the source
  may not contain the value; required fields invite fabrication.
- Retry with the original document, the failed extraction, and the specific validation
  error. Retry fixes format and structural errors; it cannot recover information that is
  absent from the source, so use null or route to review instead.
- Make semantic errors observable: `calculated_total` next to `stated_total`,
  `conflict_detected` for inconsistent sources, `detected_pattern` for dismissed findings.
- Systematic misses on a specific input shape call for 2 to 4 targeted few-shot examples
  with reasoning, not more prose, more examples, or blind retries.
- Batch only latency-tolerant, non-blocking work; it has no latency SLA and no multi-turn
  tool calling. Keep the submission interval at or below SLA minus 24 hours (with margin),
  match results by `custom_id`, resubmit only failures with the fix that addresses the
  cause, and refine the prompt on a sample before the full run.
- An aggregate pass rate can hide a failing document type or field; measure accuracy by
  segment before reducing human review.
- Facts that must survive a long session (amounts, dates, order IDs, statuses) live in a
  persistent case-facts block outside summarized history, not in a summarizer instruction.
  Trim tool output to the relevant fields before it enters context. A larger context
  window does not fix summarization loss, position effects, or exploration degradation.
- Put key findings at the start of aggregated input under explicit section headers, and
  have upstream agents return structured data (facts, citations, dates, locations) rather
  than verbose prose when a downstream agent has a limited context budget.
- Subagents recover locally from transient failures, then propagate structured error
  context (failure type, attempted query, partial results, alternatives). The coordinator
  proceeds with partial results and annotates coverage gaps. Silent suppression, generic
  status, and whole-workflow termination are all anti-patterns; a clean zero-match query
  is a valid empty result, not a failure.
- Preserve claim-source mappings with publication or collection dates through synthesis.
  Annotate conflicting values with their sources instead of selecting, averaging, or
  dropping one, and separate well-established findings from contested ones.
- Counter exploration degradation with scratchpad files, subagent delegation for verbose
  discovery, phase summaries injected into the next phase, `/compact`, and manifests of
  exported agent state for crash recovery.
- Calibrate before automating: field-level confidence thresholds checked against a labeled
  validation set, accuracy by document type and field, and ongoing stratified random
  sampling of high-confidence extractions to catch novel errors. Uncalibrated or
  document-level confidence and same-session self-review are not grounds to skip review.

## Design patterns from CCAR-P Day 1 (RAG and retrieval)

- When the right chunk is retrieved but the answer is incomplete, fix chunk boundaries
  (keep a rule with its exceptions, repeat table headers, return the parent section), not
  top-k, the model, or the prompt.
- Match the retrieval method to the query pattern: BM25 or hybrid for exact identifiers,
  dense for paraphrase, metadata filters for structured attributes, reranking when the
  right chunk is a candidate but ranked too low.
- Freshness bugs get a data-layer fix: delete by a stable source key, filter on a version
  or current flag, and keep one embedding model across the whole corpus. Temperature,
  top-k, and prompt instructions do not remove stale data.
- Access control and tenant separation are filters inside the retrieval query, not prompt
  instructions or after-the-fact logging.
- Diagnose by stage: check whether the correct chunk was retrieved and at what rank, then
  whether the model used it, before swapping the model.
- Report retrieval metrics by query segment; a good aggregate can hide a failing segment.

## Design patterns from CCAR-P Day 2 (models, prompting, caching, context)

- Choose the model per stage and per segment from your own labeled evaluation, not one
  model everywhere and not public benchmarks: a small tier for narrow high-volume work, a
  capable tier for multi-step reasoning, batch for latency-tolerant bulk work. An overall
  accuracy figure can hide a failing segment, so evaluate each routed segment.
- Caching makes a repeated prefix cheaper, Skills make the context smaller, and modular
  prompts make the prompt maintainable. Match the mechanism to the symptom.
- Put stable content first and the cache breakpoint on the last block that is identical
  across the requests sharing the cache. Never put it on a block that varies (timestamp,
  retrieved passages, user message). Confirm with `cache_read_input_tokens` above 0; both
  cache fields at 0 means the prompt was not cached (a varying prefix, a prefix under the
  model's minimum, or an expired TTL).
- Changing tool definitions, `tool_choice`, images, or the thinking and effort settings
  invalidates part or all of the cache, so keep them consistent across requests that
  should share it.
- A larger context window is capacity, not a strategy. Trim tool results to the needed
  fields at the source, retrieve the relevant passages instead of stuffing the corpus, and
  carry critical facts in a structured block passed forward verbatim.
- Treat untrusted content (documents, tool output, user input) as data delimited from the
  instructions. When the harm depends on a capability the role does not need, remove the
  capability first; stronger prompt wording is soft and logging is detective.
- Put the rules that must always hold in the tool layer, query filters, or approval gates,
  not in capitals, repetition, or a self-check line in the prompt.
- Match the prompting technique to the gap: a few diverse few-shot examples for a specific
  boundary or input-shape gap, more reasoning only for multi-step reasoning failures, and
  never maximum effort or the top tier by default.

## Design patterns from CCAR-P Day 3 (evaluation and optimization)

- Fix the metric, the pass threshold, and the guardrail metrics before testing. Pair every
  safety metric with an over-refusal or task-completion guardrail, and report p95 or p99
  latency and cost per successful task, not means or per-call cost.
- Build the eval set from production-shaped traffic, over-represent edge, adversarial, and
  ambiguous cases, tag segments, keep a held-out set that is never tuned against, and
  refresh it from production failures. More cases of the same clean type add confidence
  in the wrong distribution.
- Mix grading methods: code checks for deterministic fields, a specific rubric for the
  LLM grader validated against human labels, and humans on a sampled slice and the
  highest-risk segment. Do not use one unvalidated judge for everything or humans for
  everything.
- A/B test on the same fixed set, one variable at a time, with a pre-set decision rule,
  segment report, and enough cases to beat noise; roll out in stages with a rollback path.
  Never use different data per arm or declare a winner from a marginal aggregate gap.
- Diagnose with evidence by stage: correct source absent from context points to retrieval
  or indexing; correct source present but contradicted points to prompt or grounding
  (quoted support, an abstain path) and only then a model tier change for that stage. Fix
  an upstream defect (for example truncated stage output) before changing a downstream
  prompt or model.
- Match the cost or latency lever to the failing metric: caching for a repeated prefix,
  streaming for perceived latency (it does not cut cost), batch only for latency-tolerant
  work, a smaller tier per validated segment, lower effort only where the eval holds.
  Truncating needed context is never the answer.
- Monitoring is layered: provider-level usage and cost data cannot judge answer quality;
  per-stage request logs with a trace ID localize failures; sampled quality grading
  (stratified, including confident-looking outputs) catches silent drift when errors,
  latency, and token usage all look flat.
- Treat logs as governed data: redact or reference sensitive content by ID, control
  access, and set a retention period.