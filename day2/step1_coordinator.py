import asyncio
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
# Force foreground subagents (the CLI subprocess inherits this).
os.environ["CLAUDE_CODE_DISABLE_BACKGROUND_TASKS"] = "1"

from claude_agent_sdk import (
    query, ClaudeAgentOptions, AgentDefinition,
    AssistantMessage, ResultMessage, TextBlock, ToolUseBlock,
)

MODEL = os.getenv("CLAUDE_MODEL")
assert os.getenv("ANTHROPIC_API_KEY") and MODEL, "Check .env"

DELEGATE = {"Task", "Agent"}              # your CLI reports the spawn tool as "Agent"
USE_TASK = "--no-task" not in sys.argv    # optional: python day2/step1_coordinator.py --no-task
TIMEOUT_S = 120                           # safety net only, not the stop condition
DOCS = Path(__file__).resolve().parent / "docs"
SOURCES = ["Synthetic Design Council Report", "Synthetic Industry Brief A",
           "Synthetic Film Guild Memo", "Synthetic Authors Survey"]

COORD_PROMPT = f"""You are a coordinator. You never read files or analyze content yourself.
You delegate to subagents, then give the final answer.
Docs in {DOCS}: visual_arts.txt, music.txt, film.txt, writing.txt
Goal: a short briefing on AI's impact on creative industries covering every doc,
each claim with document name and date.
Subagents start with NO context: each delegation prompt must contain everything
that subagent needs.
Step 1: call doc_analysis_agent once per document. Emit all four calls together in a
single response.
Step 2: pass those findings, pasted in full, to synthesis_agent to write the briefing.
Paste the four JSON lists into the synthesis_agent prompt unmodified.
Wait for results in this session. Never schedule wakeups or run work in the background."""

doc_analysis_agent = AgentDefinition(
    description="Reads ONE local txt document and extracts its findings as structured JSON.",
    prompt="Read only the document you are told to read. Return ONLY a JSON list, 2-3 items, "
           'each {"claim": str, "evidence_excerpt": str (max 15 words), '
           '"source_name": str, "date": str}. Max 80 words total.',
    tools=["Read"],
)
synthesis_agent = AgentDefinition(
    description="Writes a short briefing from structured claim lists supplied in its prompt. No tools.",
    prompt="Input is JSON claim lists. Use ONLY those claims. Every sentence must end with "
           "(source_name, date). If two claims conflict, state both with their sources; "
           "never merge them. Max 120 words.",
    tools=[],
)


async def main() -> None:
    options = ClaudeAgentOptions(
        model=MODEL,
        system_prompt=COORD_PROMPT,
        allowed_tools=["Read"] + (["Task"] if USE_TASK else []),
        disallowed_tools=["ListAgents", "SendMessage", "ScheduleWakeup"],
        agents={"doc_analysis_agent": doc_analysis_agent,
                "synthesis_agent": synthesis_agent},
        max_turns=15,
    )
    final = ""
    sub_calls = 0      # subagent tool calls seen so far
    delegations = 0
    try:
        async with asyncio.timeout(TIMEOUT_S):
            async for m in query(prompt="Write the briefing.", options=options):
                if isinstance(m, AssistantMessage):
                    coord = m.parent_tool_use_id is None
                    for b in m.content:
                        if isinstance(b, ToolUseBlock):
                            if b.name in DELEGATE:
                                delegations += 1
                                p = b.input.get("prompt", "")
                                print(f"[COORD] delegation #{delegations} -> "
                                      f"{b.input.get('subagent_type')} | prompt {len(p)} chars | "
                                      f"subagent tool calls so far: {sub_calls}")
                                print(f"        {p[:120]!r}")
                            elif coord:
                                print(f"[COORD] tool: {b.name}  <-- coordinator doing work itself")
                            else:
                                sub_calls += 1
                                print(f"  [SUB] tool: {b.name}")
                        elif isinstance(b, TextBlock) and coord:
                            final = b.text
                elif isinstance(m, ResultMessage):
                    print(f"[RESULT] error={m.is_error} cost_usd={m.total_cost_usd}")
                    if m.result and not m.is_error:
                        final = m.result
    except TimeoutError:
        print(f"[TIMEOUT] stopped waiting after {TIMEOUT_S}s")
    except Exception as e:
        print(f"[ERROR] {type(e).__name__}: {e}")
    finally:
        print("\n--- FINAL ---\n" + final[:800])
        print()
        for name in SOURCES:
            print(f"cited {name!r}: {name in final}")


if __name__ == "__main__":
    asyncio.run(main())