# CCAR-P Progress Tracker

- Exam: Claude Certified Architect – Professional (CCAR-P)
- Exam facts: 63 items, 120 minutes, scaled pass 720/1000, $175, multiple-choice and multiple-response (each item states how many to select)
- Source of truth: Professional Exam Guide v1.0 (July 2026). Objective numbers below (D1.1 etc.) are my own numbering of the guide's bullets, not official.
- Target exam date: (not set)
- Last updated: 2026-11-01
- Current day: 3
- Days completed: 2 / 8 (provisional plan; adjust when the plan is confirmed)

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
| 3 | Evaluation and optimization | D4 | In progress | - | - | - |
| 4 | Governance, safety, compliance | D5 | Not started | - | - | - |
| 5 | Integration protocols, auth, observability | D3 | Not started | - | - | - |
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
| D3.1 | Evaluate tool/agent configuration for capability bloat | F (2.3) | 5 | Not started |
| D3.2 | Analyze authentication and authorization requirements to identify security gaps | New | 5 | Not started |
| D3.3 | Evaluate accuracy-latency trade-offs and justify configuration decisions | New | 5 | Not started |
| D3.4 | Analyze observability challenges and select monitoring strategies at scale | New | 5 | Not started |
| D3.5 | Design a RAG pipeline with appropriate chunking and indexing strategies | New | 1 | Solid |
| D3.6 | Apply retrieval strategies matched to data shape and query pattern | New | 1 | Solid |
| D3.7 | Select the integration mechanism (MCP, API/CLI, agent-to-agent) | Partly F (2.4) | 5 | Not started |
| D3.8 | Evaluate progressive discovery vs monolithic context strategy | New | 5 | Not started |
| D4.1 | Define evaluation metrics (accuracy, latency, cost, safety, security) | New | 3 | Not started |
| D4.2 | Design evaluation datasets and test frameworks using mixed methodologies | Partly F (5.5) | 3 | Not started |
| D4.3 | Conduct A/B testing and iterative improvements | New | 3 | Not started |
| D4.4 | Diagnose system issues (prompt failure, hallucinations, model mismatch) | New | 3 | Not started |
| D4.5 | Optimize token usage, latency, and cost-performance trade-offs | New | 3 | Not started |
| D4.6 | Monitor performance using logging and observability tools | New | 3 | Not started |
| D5.1 | Implement guardrails and safety controls | Partly F (1.5) | 4 | Not started |
| D5.2 | Identify risks, limitations, and failure modes of LLM systems | New | 4 | Not started |
| D5.3 | Apply human-in-the-loop validation strategies | F (5.2, 5.5) | 4 | Not started |
| D5.4 | Ensure compliance with regulations (GDPR, HIPAA, FedRAMP) | New | 4 | Not started |
| D5.5 | Address ethical AI considerations (bias, fairness, transparency) | New | 4 | Not started |
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
| Evaluation set and harness (mixed methods, A/B of two prompts) | Day 3 | Not started | Build vs chat-only decision pending at Day 3 start. |
| Logging and observability on the pipeline | Days 3, 5 | Not started | - |
| Guardrail and human-review routing | Day 4 | Not started | - |

## Weak spots
(Claude adds entries here as: objective number, what went wrong, what to revisit. Resolved entries are marked resolved, not deleted.)

- None yet. Day 1 produced no misses on D3.5 or D3.6 (4/4 mid-lesson, 4/4 mastery, 3/3 scenario, including four select-2 questions with the count caught every time).
- D2.5 (2026-11-01, resolved 2026-11-01): On a caching clarification check, put the single breakpoint on the first block (the only block that never changes) instead of the last block that is identical across the requests sharing the cache, so the monthly catalog was reprocessed on every request. Re-check on tools plus system prompt placement answered correctly, then mastery check 2 and scenario 1 correct. Rule to keep: the breakpoint goes on the last block identical across the sharing requests, never on a block that varies.
- D2.2 (2026-11-01, resolved 2026-11-01): On a mastery check about a prompt-injection line inside an uploaded document, chose stronger prompt wording (select 2: delimiting document text as untrusted data was right, but missed removing the unneeded email tool from the role). Scenario 2 re-check (remove the delete and directory-export tools from a summarizer) answered correctly. Rule to keep: when the harm depends on a capability the role does not need, remove the capability first; prompt wording and logging are soft or detective. Refresh on Day 4 guardrails.

## Quiz and practice log

| Date | Topic | Score | Missed objectives |
|---|---|---|---|
| 2026-11-01 | Day 1 completion: D3.5, D3.6 (4 mastery checks, 3 scenario questions, plus 4 mid-lesson checks 4/4) | Scenario 3/3; mastery 4/4 | None |
| 2026-11-01 | Day 2 completion: D2.1 to D2.5 (5 mastery checks, 3 scenario questions, plus 5 topic mid-lesson checks 5/5 and 2 caching clarification checks 1/2) | Scenario 3/3; mastery 4/5 | D2.2 (mastery); D2.5 (clarification check); both resolved 2026-11-01 |

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

## Notes
- Carried over from Foundations: orchestration and decomposition, least privilege and tool bloat, MCP basics, human-in-the-loop, hooks, Claude Code configuration. Foundations tracker is archived in ccar-f-progress.md.
- Foundations scores and mock results do not transfer: they tested Foundations content only.
- Items to verify against current Anthropic docs before relying on them: model lineup and selection guidance, prompt caching mechanics and minimum sizes, and any retrieval or embedding specifics.
- Estimate given on 2026-10-31: about 30 to 45 extra hours beyond Foundations, 8 to 10 day plan shape, not yet confirmed.
- Day 1 (2026-11-01): taught in chat (chunking, indexing, retrieval matched to data shape and query pattern, RAG failure diagnosis; one topic at a time with a mid-lesson MCQ check each, 4/4). Hands-on build skipped by decision. Verified in current docs on 2026-11-01: Anthropic does not offer its own embedding model and names Voyage AI as an embeddings provider; contextual retrieval top-20 failure rates (5.7%, 3.7%, 2.9%, 1.9%) are Anthropic's published benchmark figures. Not verified: the roughly 200,000-token threshold for skipping retrieval in favor of a full-corpus prompt with caching, and the exact current embedding model lineup. Later exercises written to build on the Day 1 pipeline (Days 3, 4, 5) will need a decision on how to handle them given builds are skipped.
- Day 2 start (2026-11-01): verified in current docs. Model lineup: Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5, all 1M context and 128K max output; roles: Fable for demanding reasoning and long-horizon agentic work, Opus for long-running agentic coding and knowledge work (docs' default starting point), Sonnet for the best speed-intelligence balance, Haiku for high-volume latency-sensitive classification, extraction, routing; latency Slower/Moderate/Fast/Fastest; Batch API 50% off; adaptive thinking steered by effort. Prompt caching: cache_control top-level (automatic) or on blocks (explicit, up to 4 breakpoints); prefix order tools, system, messages; 5-minute default TTL refreshed on use, 1-hour TTL at higher write cost; 5-minute writes 1.25x, 1-hour writes 2x, reads 0.1x base with lower multipliers on some current models; minimum cacheable prefix 512 tokens for the current lineup (differs on older models), silently skipped below it; breakpoint belongs on the last block identical across requests; tool definition changes invalidate everything, tool_choice, images, thinking and effort changes invalidate messages; verify via cache_creation_input_tokens and cache_read_input_tokens. Exam guide names no models, so selection logic matters more than names or prices. Not verified yet: Skills mechanics and the choosing-a-model page. Day 2 build skipped by decision (chat-only), consistent with Day 1.
- Day 2 completion (2026-11-01): taught in chat (D2.1 model selection, D2.5 caching, modular prompts and Skills, D2.4 context budgeting, D2.2 system prompts, templates and guardrails, D2.3 zero-shot, few-shot, chain-of-thought; one topic at a time with a mid-lesson MCQ check each). The user asked for simple worked examples of caching, modular prompts, and Skills, then for a plain explanation of stable block and breakpoint; both were explained with a code-review assistant example and block diagrams. Skills mechanics verified in current docs: SKILL.md with YAML frontmatter (name, description), three loading levels (metadata always loaded at roughly 100 tokens per Skill, SKILL.md body under about 5k tokens when triggered, bundled files and scripts as needed with script contents not loaded into context), API use via skill_id in the container parameter with the code execution tool, custom Skills shared workspace-wide, sandbox with no network access and no runtime package installation. Not verified: the exact Skills API request shape, token counting, context editing, compaction, tool search, and the choosing-a-model page (named in docs navigation only), and Anthropic's current prompting best-practices guidance (XML tag conventions not asserted). The Haiku 5.5 pricing in the docs is tiered by prompt length (lower input rate up to 100,000 tokens); check the pricing page before assuming linear cost. Day 3 hands-on exercises (evaluation harness, logging) will need a decision on builds, consistent with the chat-only approach so far.
- Day 3 start (2026-11-01): checked current docs. Success criteria should be specific, measurable, and multidimensional; eval design principles: mirror the real task distribution, include edge cases, automate grading; grading families: code-based, LLM-graded, human; evaluation should be ongoing with offline evals refreshed from production data. Docs navigation lists an Evaluation Tool, Reducing latency, and Reduce hallucinations pages. Not verified: Evaluation Tool mechanics, latency page contents, and any specific logging or usage-reporting features; check at D4.5 and D4.6. Teaching order planned: D4.1, D4.2, D4.4, D4.3, D4.5, D4.6. Build vs chat-only decision for Day 3 pending.