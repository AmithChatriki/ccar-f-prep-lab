"""
CCAR-F Day 1 — Anti-pattern: iteration cap as PRIMARY stop mechanism.
Exam framing: this truncates legitimate multi-step tasks because it ignores
stop_reason entirely and just counts turns.
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
    },
    {
        "name": "get_time",
        "description": "Get the current local time for a given city.",
        "input_schema": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"],
        },
    },
]


def execute_tool(name, tool_input):
    if name == "get_weather":
        return json.dumps({"city": tool_input["city"], "condition": "rainy", "temp_c": 18})
    if name == "get_time":
        return json.dumps({"city": tool_input["city"], "local_time": "09:10"})
    return json.dumps({"error": "unknown tool"})


def run_broken_loop(user_message: str, hard_cap: int = 1):
    """
    BROKEN: stops after `hard_cap` iterations NO MATTER WHAT stop_reason says.
    Set hard_cap=1 to force a mid-task truncation with a 2-tool request.
    """
    messages = [{"role": "user", "content": user_message}]

    for iteration in range(1, hard_cap + 1):
        print(f"\n--- Iteration {iteration} (hard cap = {hard_cap}) ---")
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            tools=TOOLS,
            messages=messages,
        )
        print(f"stop_reason: {response.stop_reason}")

        for block in response.content:
            if block.type == "text":
                print(f"  [text]: {block.text}")
            elif block.type == "tool_use":
                print(f"  [tool_use]: {block.name}({block.input})")

        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    result = execute_tool(block.name, block.input)
                    tool_results.append(
                        {"type": "tool_result", "tool_use_id": block.id, "content": result}
                    )
            messages.append({"role": "user", "content": tool_results})

    print("\n>>> BROKEN LOOP EXITED PURELY BECAUSE THE FOR-LOOP RAN OUT.")
    print(">>> stop_reason may still be 'tool_use' — task is INCOMPLETE.")
    print(">>> The user never gets a final synthesized answer.")


if __name__ == "__main__":
    run_broken_loop(
        "What's the weather and local time in Tokyo? Use both tools, then summarize.",
        hard_cap=1,
    )