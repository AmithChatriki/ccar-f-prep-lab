"""
CCAR-F Day 1 — Anti-pattern: parsing natural language for completion signals.
Exam framing: fragile, phrasing-dependent, and unrelated to the actual
mechanism (stop_reason) that indicates completion.
"""

import json
from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

TOOLS = [
    {
        "name": "get_weather",
        "description": "Get the current weather for a given city.",
        "input_schema": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"],
        },
    }
]


def execute_tool(name, tool_input):
    if name == "get_weather":
        return json.dumps({"city": tool_input["city"], "condition": "clear", "temp_c": 21})
    return json.dumps({"error": "unknown tool"})


def looks_done(text: str) -> bool:
    """BROKEN heuristic: guesses completion from phrasing."""
    markers = ["done", "finished", "that's all", "here is the answer", "in summary"]
    return any(m in text.lower() for m in markers)


def run_broken_loop(user_message: str):
    messages = [{"role": "user", "content": user_message}]
    iteration = 0

    while iteration < 6:
        iteration += 1
        print(f"\n--- Iteration {iteration} ---")
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            tools=TOOLS,
            messages=messages,
        )
        print(f"actual stop_reason (ignored by this broken logic): {response.stop_reason}")

        text_so_far = ""
        for block in response.content:
            if block.type == "text":
                text_so_far += block.text
                print(f"  [text]: {block.text}")
            elif block.type == "tool_use":
                print(f"  [tool_use]: {block.name}({block.input})")

        messages.append({"role": "assistant", "content": response.content})

        # BROKEN: branching on text content instead of stop_reason
        if looks_done(text_so_far):
            print(f"\n>>> BROKEN LOGIC DECIDED 'done' BASED ON PHRASING: {text_so_far!r}")
            print(f">>> But real stop_reason was: {response.stop_reason}")
            if response.stop_reason == "tool_use":
                print(">>> This is a FALSE POSITIVE — tool calls are still pending and will NEVER execute.")
            return

        if response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    result = execute_tool(block.name, block.input)
                    tool_results.append(
                        {"type": "tool_result", "tool_use_id": block.id, "content": result}
                    )
            messages.append({"role": "user", "content": tool_results})
        else:
            print(">>> Reached end_turn without ever matching a phrasing marker (also broken — false negative).")
            return


if __name__ == "__main__":
    # Ask something where Claude is likely to say "Let me check" (containing no marker)
    # or occasionally phrase things in a way that trips the false-positive heuristic.
    run_broken_loop("Can you check the weather in Paris for me? Give me a one-line summary when done.")