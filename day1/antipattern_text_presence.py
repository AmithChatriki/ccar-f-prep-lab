"""
CCAR-F Day 1 — Anti-pattern: treating "there is a text block" as "task is complete."
Exam framing: Claude can emit text AND tool_use in the same response. This causes
premature exit while stop_reason is still 'tool_use'.
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
        return json.dumps({"city": tool_input["city"], "condition": "cloudy", "temp_c": 15})
    return json.dumps({"error": "unknown tool"})


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

        has_text = any(block.type == "text" for block in response.content)
        has_tool_use = any(block.type == "tool_use" for block in response.content)

        print(f"stop_reason: {response.stop_reason} | has_text: {has_text} | has_tool_use: {has_tool_use}")
        for block in response.content:
            if block.type == "text":
                print(f"  [text]: {block.text}")
            elif block.type == "tool_use":
                print(f"  [tool_use]: {block.name}({block.input})  <-- THIS WILL NEVER RUN")

        # BROKEN: any text block present == "the model answered" == stop
        if has_text:
            print("\n>>> BROKEN LOGIC: saw a text block, decided the task is complete.")
            if response.stop_reason == "tool_use":
                print(">>> WRONG: stop_reason is 'tool_use'. A pending tool call was abandoned.")
                print(">>> The user gets a half-finished response and the tool_use_id is now orphaned.")
            return

        # unreachable in most real cases but kept for completeness
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


if __name__ == "__main__":
    run_broken_loop("What's the weather in Berlin? Let me know what you're doing before you check.")