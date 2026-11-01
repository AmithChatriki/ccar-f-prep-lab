# CCAR-P Progress Tracker

- Exam: Claude Certified Architect – Professional (CCAR-P)
- Exam facts: 63 items, 120 minutes, scaled pass 720/1000, $175, multiple-choice and multiple-response (each item states how many to select)
- Source of truth: Professional Exam Guide v1.0 (July 2026). Objective numbers below (D1.1 etc.) are my own numbering of the guide's bullets, not official.
- Target exam date: (not set)
- Last updated: 2026-11-01
- Current day: 2
- Days completed: 1 / 8 (provisional plan; adjust when the plan is confirmed)

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
| 2 | Models, prompting, caching, context | D2 | Not started | - | - | - |
| 3 | Evaluation and optimization | D4 | Not started | - | - | - |
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
| D2.1 | Select Claude models based on trade-offs | New | 2 | Not started |
| D2.2 | Design system prompts, templates, and guardrails | New | 2 | Not started |
| D2.3 | Apply prompting techniques (zero-shot, few-shot, chain-of-thought) | Partly F (4.2) | 2 | Not started |
| D2.4 | Optimize context windows and manage token usage | Partly F (5.1) | 2 | Not started |
| D2.5 | Implement prompt reuse (caching, modular prompts, Skills) | New (caching), partly F (Skills) | 2 | Not started |
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
| Prompt caching comparison (static prefix first, cached vs uncached) | Day 2 | Not started | - |
| Evaluation set and harness (mixed methods, A/B of two prompts) | Day 3 | Not started | - |
| Logging and observability on the pipeline | Days 3, 5 | Not started | - |
| Guardrail and human-review routing | Day 4 | Not started | - |

## Weak spots
(Claude adds entries here as: objective number, what went wrong, what to revisit. Resolved entries are marked resolved, not deleted.)

- None yet. Day 1 produced no misses on D3.5 or D3.6 (4/4 mid-lesson, 4/4 mastery, 3/3 scenario, including four select-2 questions with the count caught every time).

## Quiz and practice log

| Date | Topic | Score | Missed objectives |
|---|---|---|---|
| 2026-11-01 | Day 1 completion: D3.5, D3.6 (4 mastery checks, 3 scenario questions, plus 4 mid-lesson checks 4/4) | Scenario 3/3; mastery 4/4 | None |

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

## Notes
- Carried over from Foundations: orchestration and decomposition, least privilege and tool bloat, MCP basics, human-in-the-loop, hooks, Claude Code configuration. Foundations tracker is archived in ccar-f-progress.md.
- Foundations scores and mock results do not transfer: they tested Foundations content only.
- Items to verify against current Anthropic docs before relying on them: model lineup and selection guidance, prompt caching mechanics and minimum sizes, and any retrieval or embedding specifics.
- Estimate given on 2026-10-31: about 30 to 45 extra hours beyond Foundations, 8 to 10 day plan shape, not yet confirmed.
- Day 1 (2026-11-01): taught in chat (chunking, indexing, retrieval matched to data shape and query pattern, RAG failure diagnosis; one topic at a time with a mid-lesson MCQ check each, 4/4). Hands-on build skipped by decision. Verified in current docs on 2026-11-01: Anthropic does not offer its own embedding model and names Voyage AI as an embeddings provider; contextual retrieval top-20 failure rates (5.7%, 3.7%, 2.9%, 1.9%) are Anthropic's published benchmark figures. Not verified: the roughly 200,000-token threshold for skipping retrieval in favor of a full-corpus prompt with caching, and the exact current embedding model lineup. Later exercises written to build on the Day 1 pipeline (Days 3, 4, 5) will need a decision on how to handle them given builds are skipped.