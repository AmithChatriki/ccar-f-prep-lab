# CCAR-P Progress Tracker

- Exam: Claude Certified Architect – Professional (CCAR-P)
- Exam facts: 63 items, 120 minutes, scaled pass 720/1000, $175, multiple-choice and multiple-response (each item states how many to select)
- Source of truth: Professional Exam Guide v1.0 (July 2026). Objective numbers below (D1.1 etc.) are my own numbering of the guide's bullets, not official.
- Target exam date: (not set)
- Last updated: 2026-11-08
- Current day: 6
- Days completed: 5 / 8 (provisional plan; adjust when the plan is confirmed)

## Status key
- Days: Not started | In progress | Done | Needs review
- Objectives: Not started | Learning | Solid
  - Learning = studied, but mastery check not yet passed
  - Solid = answered the mastery check and exam-style questions correctly

## Domain weights

| Domain | Topic | Weight | Items (approx of 63) |
|---|---|---|---|
| D1 | Solution Design & Architecture | 17% | 11 |
| D2 | Claude Models, Prompting & Context Engineering | 13% | 8 |
| D3 | Integration | 19% | 12 |
| D4 | Evaluation, Testing & Optimization | 16% | 10 |
| D5 | Governance, Safety & Risk Management | 14% | 9 |
| D6 | Stakeholder Communication & Lifecycle Management | 14% | 9 |
| D7 | Developer Productivity & Operational Enablement | 7% | 4 |

## Day tracker (provisional)

| Day | Focus | Domains | Status | Mastery check | Quiz score | Completed on |
|---|---|---|---|---|---|---|
| 1 | RAG and retrieval | D3 | Done | Passed (MCQ format, 4/4) | 3/3 | 2026-11-01 |
| 2 | Models, prompting, caching, context | D2 | Done | Passed (MCQ format, 4/5; missed the capability-removal option on the D2.2 injection question, re-check in scenario 2 correct) | 3/3 | 2026-11-01 |
| 3 | Evaluation and optimization | D4 | Done | Passed (MCQ format, 5/5) | 3/3 | 2026-11-05 |
| 4 | Governance, safety, compliance | D5 | Done | Passed (MCQ format, 5/5) | 3/3 | 2026-11-07 |
| 5 | Integration protocols, auth, observability | D3 | Done | Passed (MCQ format, 6/6) | 3/3 | 2026-11-08 |
| 6 | Stakeholder communication and lifecycle | D6 | Not started | - | - | - |
| 7 | Refresh of carried-over content | D1, D7 | Not started | - | - | - |
| 8 | Mock exams and consolidation | All | Not started | - | - | - |

## Objective coverage

| Obj | Objective | Origin | Day | Status |
|---|---|---|---|---|
| D1.1 | Translate business problems into Claude-based AI solutions | New | 7 | Not started |
| D1.2 | Design end-to-end architectures (input, processing, output, feedback loops) | Partly F | 7 | Not started |
| D1.3 | Select architectural patterns (workflow, agentic, augmented LLM) | Partly F | 7 | Not started |
| D1.4 | Design multi-agent systems and orchestration strategies | F (1.2, 1.3) | 7 | Not started |
| D1.5 | Apply decomposition techniques for complex problem solving | F (1.6) | 7 | Not started |
| D1.6 | Align solutions to business value pillars (efficiency, transformation, productivity, cost, performance SLAs) | New | 6 | Not started |
| D2.1 | Select Claude models based on trade-offs | New | 2 | Solid |
| D2.2 | Design system prompts, templates, and guardrails | New | 2 | Solid |
| D2.3 | Apply prompting techniques (zero-shot, few-shot, chain-of-thought) | Partly F (4.2) | 2 | Solid |
| D2.4 | Optimize context windows and manage token usage | Partly F (5.1) | 2 | Solid |
| D2.5 | Implement prompt reuse (caching, modular prompts, Skills) | New (caching), partly F (Skills) | 2 | Solid |
| D3.1 | Evaluate tool/agent configuration for capability bloat | F (2.3) | 5 | Solid |
| D3.2 | Analyze authentication and authorization requirements to identify security gaps | New | 5 | Solid |
| D3.3 | Evaluate accuracy-latency trade-offs and justify configuration decisions | New | 5 | Solid |
| D3.4 | Analyze observability challenges and select monitoring strategies at scale | New | 5 | Solid |
| D3.5 | Design a RAG pipeline with appropriate chunking and indexing strategies | New | 1 | Solid |
| D3.6 | Apply retrieval strategies matched to data shape and query pattern | New | 1 | Solid |
| D3.7 | Select the integration mechanism (MCP, API/CLI, agent-to-agent) | Partly F (2.4) | 5 | Solid |
| D3.8 | Evaluate progressive discovery vs monolithic context strategy | New | 5 | Solid |
| D4.1 | Define evaluation metrics (accuracy, latency, cost, safety, security) | New | 3 | Solid |
| D4.2 | Design evaluation datasets and test frameworks using mixed methodologies | Partly F (5.5) | 3 | Solid |
| D4.3 | Conduct A/B testing and iterative improvements | New | 3 | Solid |
| D4.4 | Diagnose system issues (prompt failure, hallucinations, model mismatch) | New | 3 | Solid |
| D4.5 | Optimize token usage, latency, and cost-performance trade-offs | New | 3 | Solid |
| D4.6 | Monitor performance using logging and observability tools | New | 3 | Solid |
| D5.1 | Implement guardrails and safety controls | Partly F (1.5) | 4 | Solid |
| D5.2 | Identify risks, limitations, and failure modes of LLM systems | New | 4 | Solid |
| D5.3 | Apply human-in-the-loop validation strategies | F (5.2, 5.5) | 4 | Solid |
| D5.4 | Ensure compliance with regulations (GDPR, HIPAA, FedRAMP) | New | 4 | Solid |
| D5.5 | Address ethical AI considerations (bias, fairness, transparency) | New | 4 | Solid |
| D6.1 | Conduct structured discovery and requirement gathering | New | 6 | Not started |
| D6.2 | Communicate architectural decisions and trade-offs | New | 6 | Not started |
| D6.3 | Manage stakeholder feedback loops and expectation alignment (including SLAs) | New | 6 | Not started |
| D6.4 | Document architectures and provide implementation guidance | New | 6 | Not started |
| D6.5 | Support lifecycle phases (discovery, design, handoff, monitoring, iteration) | New | 6 | Not started |
| D7.1 | Configure Claude tools and environments for teams (e.g., Claude Code) | F (3.1 to 3.4) | 7 | Not started |
| D7.2 | Improve developer workflows using AI-assisted tooling | F (3.5, 3.6) | 7 | Not started |
| D7.3 | Support debugging and operational issue resolution | Partly F | 7 | Not started |

## Hands-on exercises

The guide recommends building and operating at least one end-to-end Claude solution including RAG, evaluation, and observability. API spend is capped, so keep builds small, local, and on a cheap model.

| Exercise | Built on | Status | Notes |
|---|---|---|---|
| Small RAG pipeline (chunking, index, retrieval) | Day 1 | Skipped by decision | Skipped by decision (stated at Day 1 start; teaching is chat-only with MCQ checks). Not built: corpus and labeled test set with identifier, paraphrase, and context-dependent segments; fixed-size vs structure-aware chunkers; BM25 vs dense retrieval (optional hybrid); hit@k by segment; stale-chunk refresh simulation with doc_id and version fix. Judgment content covered in chat and through questions. |
| Prompt caching comparison (static prefix first, cached vs uncached) | Day 2 | Skipped by decision | Skipped by decision (stated at Day 2 start; chat-only). Not built: static prefix above the minimum cacheable length with cache_control on the last static block; two back-to-back calls comparing usage fields and latency; timestamp-in-prefix variant (expect no read); breakpoint-on-varying-block variant (expect a write every time). Judgment content covered in chat and through questions; worked code examples of caching, modular prompt assembly, and a SKILL.md shown in chat only. |
| Evaluation set and harness (mixed methods, A/B of two prompts) | Day 3 | Skipped by decision | Skipped by decision (Day 3 started chat-only, consistent with Days 1 and 2; no objection raised). Not built: 30 to 40 case JSONL eval set with segment tags (typical, edge, adversarial, ambiguous) and a held-out portion; harness mixing exact-match or code checks with a rubric-based LLM grader, reporting accuracy by segment; A/B of two prompt versions on the same set with per-segment deltas. Judgment content covered in chat and through questions. |
| Logging and observability on the pipeline | Days 3, 5 | Skipped by decision | Day 3 part (structured per-request logs with trace ID, prompt version, model, token and cache usage, latency) skipped by decision; Day 5 tracing part (trace ID and per-stage spans on the Day 3 harness) skipped by decision (stated at Day 5 start as chat-only by default; no builds reported at completion, no objection raised). Judgment content for D4.6 and D3.4 covered in chat and through questions. |
| Guardrail and human-review routing | Day 4 | Skipped by decision | Skipped by decision (confirmed chat-only at Day 4 start, consistent with Days 1 to 3). Not built: input classifier with structured verdict and benign, direct-injection, and indirect-injection cases; per-role tool allowlist; review routing on ambiguity, policy gap, and high-impact cases with reason codes; block and over-refusal rates by segment. Judgment content covered in chat and through questions. |
| Progressive vs monolithic context comparison | Day 5 | Skipped by decision | Skipped by decision (stated at Day 5 start as chat-only by default; no builds reported at completion, no objection raised). Not built: a monolithic tool list vs a deferred list with a tool-search tool, comparing tokens in context and tool-selection accuracy. Judgment content covered in chat and through questions. |

## Weak spots
(Claude adds entries here as: objective number, what went wrong, what to revisit. Resolved entries are marked resolved, not deleted.)

- None yet. Day 1 produced no misses on D3.5 or D3.6 (4/4 mid-lesson, 4/4 mastery, 3/3 scenario, including four select-2 questions with the count caught every time).
- Day 3 produced no misses on D4.1 to D4.6 (6/6 mid-lesson, 5/5 mastery, 3/3 scenario, including nine select-2 questions with the count caught every time).
- Day 4 produced no misses on D5.1 to D5.5 (5/5 mid-lesson, 5/5 mastery, 3/3 scenario, including six select-2 questions with the count caught every time). The D2.2 capability-removal refresh (indirect injection through a fetched page, remove the unneeded send_email tool plus untrusted-data handling) was answered correctly in mastery check 1.
- Day 5 produced no misses on D3.1, D3.2, D3.3, D3.4, D3.7, D3.8 (6/6 mid-lesson, 6/6 mastery, 3/3 scenario, including seven select-2 questions with the count caught every time). The capability-removal pattern held again (allowlist plus narrow tool replacing a general shell tool; credential moved out of the model context with scoped rights and unneeded tools removed).
- D2.5 (2026-11-01, resolved 2026-11-01): On a caching clarification check, put the single breakpoint on the first block (the only block that never changes) instead of the last block that is identical across the requests sharing the cache, so the monthly catalog was reprocessed on every request. Re-check on tools plus system prompt placement answered correctly, then mastery check 2 and scenario 1 correct. Rule to keep: the breakpoint goes on the last block identical across the sharing requests, never on a block that varies.
- D2.2 (2026-11-01, resolved 2026-11-01): On a mastery check about a prompt-injection line inside an uploaded document, chose stronger prompt wording (select 2: delimiting document text as untrusted data was right, but missed removing the unneeded email tool from the role). Scenario 2 re-check (remove the delete and directory-export tools from a summarizer) answered correctly. Rule to keep: when the harm depends on a capability the role does not need, remove the capability first; prompt wording and logging are soft or detective. Refresh on Day 4 guardrails (done 2026-11-07, answered correctly); refreshed again on Day 5 (mastery check 1 and scenario 1, answered correctly).

## Quiz and practice log

| Date | Topic | Score | Missed objectives |
|---|---|---|---|
| 2026-11-01 | Day 1 completion: D3.5, D3.6 (4 mastery checks, 3 scenario questions, plus 4 mid-lesson checks 4/4) | Scenario 3/3; mastery 4/4 | None |
| 2026-11-01 | Day 2 completion: D2.1 to D2.5 (5 mastery checks, 3 scenario questions, plus 5 topic mid-lesson checks 5/5 and 2 caching clarification checks 1/2) | Scenario 3/3; mastery 4/5 | D2.2 (mastery); D2.5 (clarification check); both resolved 2026-11-01 |
| 2026-11-05 | Day 3 completion: D4.1 to D4.6 (5 mastery checks, 3 scenario questions, plus 6 mid-lesson checks 6/6) | Scenario 3/3; mastery 5/5 | None |
| 2026-11-07 | Day 4 completion: D5.1 to D5.5 (5 mastery checks, 3 scenario questions, plus 5 mid-lesson checks 5/5) | Scenario 3/3; mastery 5/5 | None |
| 2026-11-08 | Day 5 completion: D3.1, D3.2, D3.3, D3.4, D3.7, D3.8 (6 mastery checks, 3 scenario questions, plus 6 mid-lesson checks 6/6) | Scenario 3/3; mastery 6/6 | None |

## Diagnostic and mock exam results

| Date | Test | Score | Weakest domains |
|---|---|---|---|
| - | Full mock exam | - | - |

## Recurring answer patterns (carry over and extend)
- Remove capabilities the role does not need (least privilege) rather than only logging or confirming; prevention beats detection.
- Choose the proportionate fix for the root cause before adding infrastructure.
- Rules that must always hold go in code, not prompts.
- Stable content first, then prompt caching, for repeated prefixes.
- Confident but wrong answers after a data change point to retrieval and indexing first.
- Incomplete answers with the right chunk retrieved point to chunk boundaries: align to document structure, keep rules with exceptions, return the parent section; not top-k, model, or prompt changes.
- Match the retrieval method to the query pattern: BM25 or hybrid for exact identifiers, semantic for paraphrase, metadata filters for structured attributes, reranking when the right chunk is a candidate but ranked too low.
- Freshness bugs get a data-layer fix: delete by a stable source key, version or is_current filter, one embedding model across the corpus; never temperature, top-k, or a prompt instruction.
- Access control and tenant separation are filters inside the retrieval query, not prompt instructions or after-the-fact logging.
- Diagnose by stage: check whether the correct chunk was retrieved and at what rank, then whether the model used it; do not swap the model first.
- A good aggregate metric can hide a failing query segment; report by segment.
- Cache breakpoint goes on the last block identical across the requests sharing the cache, never on a block that varies (timestamp, retrieved passages, user message); verify with cache_read_input_tokens above 0.
- Caching makes a repeated prefix cheaper; Skills make the context smaller; modular prompts make the prompt maintainable; match the mechanism to the symptom.
- Pick the model per stage and per segment from your own labeled evaluation (small tier for narrow high-volume work, capable tier for multi-step reasoning, batch for latency-tolerant work), not one model everywhere and not public benchmarks.
- A bigger context window is capacity, not a strategy: trim tool results at the source, retrieve instead of stuffing, and carry critical facts in a structured block passed forward verbatim.
- Untrusted content (documents, tool output, user input) is data, delimited from instructions; when harm depends on a capability the role does not need, remove the capability.
- Match the prompting technique to the gap: few-shot examples for a specific boundary or input-shape gap, more reasoning only for multi-step reasoning failures, never maximum effort or the top tier by default.
- Metrics: fix the metric, threshold, and guardrail metrics before testing; pair every safety metric with an over-refusal or task-completion guardrail; report p95 or p99 for latency and cost per successful task, not means or per-call cost.
- Evaluation design: mirror production traffic, over-represent edge, adversarial, and ambiguous cases, tag segments, keep a held-out set, and refresh from production. Code checks for deterministic fields, a specific rubric for the LLM grader, validated against human labels, with humans on a sampled slice and the highest-risk segment.
- A/B testing: same fixed set, one variable at a time, pre-set decision rule and guardrails, segment report, enough cases to beat noise, staged rollout with rollback; never different data per arm or a winner from a marginal aggregate gap.
- Diagnose by stage with evidence: correct source absent from context means retrieval or indexing; correct source present but contradicted means prompt or grounding (quoted support, abstain path), and only then a model tier change for that stage; a defect in an upstream stage is fixed before changing a downstream prompt.
- Match the cost or latency lever to the failing metric: caching for a repeated prefix, streaming for perceived latency (not cost), batch only for latency-tolerant work, a smaller tier per validated segment, lower effort only where the eval holds; truncating needed context is never the answer.
- Monitoring is layered: provider-level usage and cost data cannot judge answer quality; per-request stage logs with a trace ID localize failures; sampled quality grading catches silent drift when errors, latency, and token usage all look flat. Logs are governed data: redact or reference by ID, control access, set retention.
- Name the failure mode before choosing the control: hallucination with retrieval verified calls for an abstain path and quote-first grounding (plus human review for high stakes), not temperature 0, higher top-k, a bigger window, or a bigger model; fabricated but checkable output (citations, IDs, amounts) is verified in code.
- Guardrails are layered, and strength must match the risk: capability removal and code-enforced action gates for rules that must always hold; screens (input or output classifiers) are probabilistic, cost latency and tokens, fail closed on high-risk paths, and are never the only barrier on an irreversible action; use cheap deterministic checks first.
- Every blocking control has a false-positive cost: report block and over-refusal rates by segment alongside the safety metric, tune against both, and send borderline verdicts to a secondary check rather than an automatic block.
- Human review triggers are impact, ambiguity, and policy gaps (plus calibrated, measured confidence), not stated confidence or sentiment; give reviewers evidence and a reason code; guard against rubber-stamping with override rate, time per item, and planted known-bad items; sample auto-approved work by segment and feed confirmed errors into the evaluation set.
- Compliance changes the architecture: minimize or pseudonymize before data reaches prompts, index stores and logs by a stable subject ID so erasure works, set retention per store, enforce access in the retrieval or tool layer, redact logs; a BAA covers supported features only, and retention terms can constrain model choice; never a prompt rule, a disclaimer, or output-only redaction.
- Fairness is measured by group with counterfactual (paired) tests on a labeled set; removing a protected attribute does not remove proxies; consequential decisions about people keep a human, with criteria, cited evidence, disclosure of AI involvement, and a way to contest; a model's written reasoning is not proof of how it decided; never "be fair" in a prompt or an aggregate metric as evidence.
- Capability bloat is audited, not just trimmed: map tasks to the minimum tools, remove what no task needs through a per-role allowlist (not a prompt line, a confirmation, or logging), merge or sharpen overlapping tools to fix wrong-tool selection, and replace a general tool (a shell) with a narrow, constrained one.
- Progressive discovery versus monolithic: keep the hot tools loaded and defer the rare ones behind a tool-search tool with clear names and descriptions, and evaluate discovery recall; removal is for tools the role does not need, deferral for tools it needs rarely; caching and a bigger window do not fix selection accuracy or capacity; discovery is efficiency, not access control.
- Choose the integration mechanism from the shape of the need: MCP for a capability shared by several consumers with authentication and permitted operations in one place, a direct API or CLI tool for one narrow fixed integration, agent-to-agent for open-ended work owned by an independent agent; never MCP everywhere, and never an agent for a deterministic lookup.
- Authentication and authorization gaps: identity comes from the verified session in code, never from a model-generated argument; permissions are enforced at the tool, MCP server, or data layer with the user's own authority (per-user or on-behalf-of token), not a shared broad service account; credentials stay out of the model context and are scoped and short-lived; the acting person is recorded in the audit trail; never a stronger prompt, rotation alone, or logging alone.
- Accuracy-latency trade-offs: start from the requirement (p95 budget, accuracy bar), segment the traffic, route only the failing segment to the more capable configuration, validate it on the labeled set by segment, and check the latency budget on that path; offline work can spend latency on accuracy and use batch; streaming helps perceived latency only; never the biggest model everywhere, the smallest everywhere, or truncating needed context.
- Observability at scale: propagate a trace ID through every hop with per-stage spans (model, tokens, cache use, tool, latency, outcome; large inputs by reference), tag requests by team, workflow, and prompt version for spend and failure attribution, add sampled quality grading by segment and compare cost per successful task around changes, keep full detail for flagged runs plus a random sample, and govern logs; instrument your boundary for third-party MCP servers; organization-level totals cannot attribute spend or judge quality.

## Notes
- Carried over from Foundations: orchestration and decomposition, least privilege and tool bloat, MCP basics, human-in-the-loop, hooks, Claude Code configuration. Foundations tracker is archived in ccar-f-progress.md.
- Foundations scores and mock results do not transfer: they tested Foundations content only.
- Items to verify against current Anthropic docs before relying on them: model lineup and selection guidance, prompt caching mechanics and minimum sizes, and any retrieval or embedding specifics.
- Estimate given on 2026-10-31: about 30 to 45 extra hours beyond Foundations, 8 to 10 day plan shape, not yet confirmed.
- Day 1 (2026-11-01): taught in chat (chunking, indexing, retrieval matched to data shape and query pattern, RAG failure diagnosis; one topic at a time with a mid-lesson MCQ check each, 4/4). Hands-on build skipped by decision. Verified in current docs on 2026-11-01: Anthropic does not offer its own embedding model and names Voyage AI as an embeddings provider; contextual retrieval top-20 failure rates (5.7%, 3.7%, 2.9%, 1.9%) are Anthropic's published benchmark figures. Not verified: the roughly 200,000-token threshold for skipping retrieval in favor of a full-corpus prompt with caching, and the exact current embedding model lineup. Later exercises written to build on the Day 1 pipeline (Days 3, 4, 5) will need a decision on how to handle them given builds are skipped.
- Day 2 start (2026-11-01): verified in current docs. Model lineup: Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5, all 1M context and 128K max output; roles: Fable for demanding reasoning and long-horizon agentic work, Opus for long-running agentic coding and knowledge work (docs' default starting point), Sonnet for the best speed-intelligence balance, Haiku for high-volume latency-sensitive classification, extraction, routing; latency Slower/Moderate/Fast/Fastest; Batch API 50% off; adaptive thinking steered by effort. Prompt caching: cache_control top-level (automatic) or on blocks (explicit, up to 4 breakpoints); prefix order tools, system, messages; 5-minute default TTL refreshed on use, 1-hour TTL at higher write cost; 5-minute writes 1.25x, 1-hour writes 2x, reads 0.1x base with lower multipliers on some current models; minimum cacheable prefix 512 tokens for the current lineup (differs on older models), silently skipped below it; breakpoint belongs on the last block identical across requests; tool definition changes invalidate everything, tool_choice, images, thinking and effort changes invalidate messages; verify via cache_creation_input_tokens and cache_read_input_tokens. Exam guide names no models, so selection logic matters more than names or prices. Not verified yet: Skills mechanics and the choosing-a-model page. Day 2 build skipped by decision (chat-only), consistent with Day 1.
- Day 2 completion (2026-11-01): taught in chat (D2.1 model selection, D2.5 caching, modular prompts and Skills, D2.4 context budgeting, D2.2 system prompts, templates and guardrails, D2.3 zero-shot, few-shot, chain-of-thought; one topic at a time with a mid-lesson MCQ check each). The user asked for simple worked examples of caching, modular prompts, and Skills, then for a plain explanation of stable block and breakpoint; both were explained with a code-review assistant example and block diagrams. Skills mechanics verified in current docs: SKILL.md with YAML frontmatter (name, description), three loading levels (metadata always loaded at roughly 100 tokens per Skill, SKILL.md body under about 5k tokens when triggered, bundled files and scripts as needed with script contents not loaded into context), API use via skill_id in the container parameter with the code execution tool, custom Skills shared workspace-wide, sandbox with no network access and no runtime package installation. Not verified: the exact Skills API request shape, token counting, context editing, compaction, tool search, and the choosing-a-model page (named in docs navigation only), and Anthropic's current prompting best-practices guidance (XML tag conventions not asserted). The Haiku 5.5 pricing in the docs is tiered by prompt length (lower input rate up to 100,000 tokens); check the pricing page before assuming linear cost. Day 3 hands-on exercises (evaluation harness, logging) will need a decision on builds, consistent with the chat-only approach so far.
- Day 3 start (2026-11-05): checked current docs. Success criteria should be specific, measurable, and multidimensional; eval design principles: mirror the real task distribution, include edge cases, automate grading; grading families: code-based, LLM-graded, human; evaluation should be ongoing with offline evals refreshed from production data. Latency page: three levers (choose the right model, trim prompt and output length, stream), latency measured as baseline latency and time to first token, build a working prompt before optimizing latency, effort described as the main speed and cost control, max_tokens is a blunt cutoff that truncates. Usage and Cost Admin API: organization-level historical usage and cost, requires Admin API credentials, groupable by dimensions such as model, API key, and workspace, data typically within about five minutes, partner observability and FinOps integrations listed. Not verified: Evaluation Tool mechanics, tracing and OpenTelemetry specifics, exact effort level names. Day 3 build decision: chat-only (no objection raised).
- Day 3 completion (2026-11-05): taught in chat (D4.1, D4.2, D4.4, D4.3, D4.5, D4.6, one topic at a time with a mid-lesson MCQ check each, 6/6). The user asked what a stage is in stage-level logging (explained with a five-stage RAG and tool pipeline and a per-stage log example), what p95 and p99 mean (explained with a 100-request worked example where the mean hides a slow tail), and what "p95 latency is flat" means (a flat trend over time, one of several clues that the system looked healthy while quality drifted silently). Standing preference stated on Day 3: any question with two correct answers is written with 5 options, not 4. Mastery check 1 (written before the preference) had 4 options. Recurring Day 3 patterns are in the answer-patterns list above.
- Day 4 start (2026-11-07): checked current docs. Guardrails page: two threat models (jailbreaks and direct injection, where the user is the adversary; indirect injection, where the user is trusted but third-party content such as web pages, emails, documents, and tool results carries adversarial instructions); mitigations are layered: input screening with a classifier returning a structured verdict the application branches on, a system-prompt policy that tool and document content is untrusted data, continuous monitoring, throttling or banning repeat offenders, chained safeguards; Anthropic runs extra injection classifiers for the computer use tool. Data retention page: ZDR and HIPAA readiness are two separate arrangements; ZDR is an agreement per organization, not a toggle; HIPAA-ready API access needs a signed BAA plus a HIPAA-enabled organization, and some features (for example code_execution) are blocked for HIPAA organizations without ZDR; Claude Code is covered only with ZDR enabled; on Amazon Bedrock and Google Cloud (Google managed) the cloud provider is the data processor; Fable 5.1, Mythos 5.1, Fable 5, and Mythos 5 require 30-day retention and are not available under ZDR unless Anthropic expressly authorizes it. Not verified: current FedRAMP status (community sources conflict: one says in progress as of March 2026, another says FedRAMP High via Bedrock GovCloud and Palantir FedStart; the exam guide names FedRAMP generically), EU data residency claims (community source only), and GDPR specifics (taught as general architectural implications, not legal advice). Build decision: chat-only confirmed.
- Day 4 completion (2026-11-07): taught in chat (D5.2, D5.1, D5.3, D5.4, D5.5, one topic at a time with a mid-lesson MCQ check each, 5/5). Hallucination page verified in current docs on 2026-11-07: give Claude an explicit out to say it does not know, extract word-for-word quotes first for long documents and answer only from them, require evidence for claims with a defined fallback statement; the docs say these techniques reduce but do not eliminate hallucinations and critical information in high-stakes decisions should still be validated. The user asked what "screening" means (an extra check on input or output before or after the main model call; model-based screens add a call, so they add tokens, and an input screen adds latency in series; worked example of about 400 ms and a few hundred tokens per request) and what rubber-stamping is (a reviewer approving items without real evaluation because of volume and missing evidence; signs: approval near 100%, very low time per item, near-zero override rate, planted known-bad items approved; fixes: route only judgment cases, show evidence and a reason code, plant test cases, size the queue to capacity). Not verified: the prompt-leak page, GDPR legal specifics, current FedRAMP status. Recurring Day 4 patterns are in the answer-patterns list above.
- Day 5 start (2026-11-08): checked current docs. Tool search: a tool-search tool (regex and BM25 variants, dated type strings in the tools list) plus defer_loading: true on tools that should not load up front; Claude initially sees only the search tool and non-deferred tools; defer_loading controls what enters the context window, not what is sent in the request (the API needs all definitions server-side to run the search); both variants search tool names, descriptions, argument names, and argument descriptions; a third-party page (LiteLLM) recommends keeping the 3 to 5 most-used tools non-deferred (not confirmed on Anthropic's own page). MCP connector: Messages API connects to remote MCP servers without a separate MCP client via an mcp_servers array (url must be https, name, optional authorization_token) and an mcp_toolset entry in tools (per-server tool enablement with allowlist or denylist configuration); the API consumer runs the OAuth flow, obtains the access token, and refreshes it; not available on Amazon Bedrock or Google Cloud, and on Microsoft Foundry it needs a Hosted-on-Anthropic deployment. Not verified: the beta header and exact model support for tool search (sources conflict or are outdated), any Anthropic documentation on agent-to-agent protocols (the guide names it generically, so taught as a selection criterion), and tracing or OpenTelemetry specifics. Build decision: chat-only by default, no objection raised.
- Day 5 completion (2026-11-08): taught in chat (D3.1, D3.8, D3.7, D3.2, D3.3, D3.4, one topic at a time with a mid-lesson MCQ check each, 6/6). No user questions or builds reported at completion; both Day 5 builds recorded as skipped by decision. Seven select-2 questions across the day, count caught every time. Recurring Day 5 patterns are in the answer-patterns list above. Not verified: agent-to-agent as a named protocol (taught as the delegation pattern), tool search beta header and model support, tracing and OpenTelemetry specifics.