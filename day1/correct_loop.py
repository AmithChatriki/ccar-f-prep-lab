"""
CCAR-F Day 1 — Correct agentic loop implementation.
Branches ONLY on stop_reason. This is the pattern the exam treats as correct.
"""

import json
from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# --- A trivial tool so we can force multi-step tool_use behavior ---
TOOLS = [
    {
        "name": "get_weather",
        "description": "Get the current weather for a given city.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "City name"}
            },
            "required": ["city"],
        },
    },
    {
        "name": "get_time",
        "description": "Get the current local time for a given city.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "City name"}
            },
            "required": ["city"],
        },
    },
]


def execute_tool(name: str, tool_input: dict) -> str:
    """Fake tool execution — returns canned data so we can observe loop behavior."""
    if name == "get_weather":
        return json.dumps({"city": tool_input["city"], "condition": "sunny", "temp_c": 24})
    if name == "get_time":
        return json.dumps({"city": tool_input["city"], "local_time": "14:32"})
    return json.dumps({"error": f"unknown tool {name}"})


def run_agentic_loop(user_message: str, max_iterations: int = 10):
    messages = [{"role": "user", "content": user_message}]
    iteration = 0

    while True:
        iteration += 1
        print(f"\n{'='*60}")
        print(f"ITERATION {iteration}")
        print(f"{'='*60}")

        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            tools=TOOLS,
            messages=messages,
        )

        print(f"stop_reason: {response.stop_reason}")

        # Log every content block so you can see text + tool_use coexisting
        for block in response.content:
            if block.type == "text":
                print(f"  [text block]: {block.text}")
            elif block.type == "tool_use":
                print(f"  [tool_use block]: {block.name}({block.input})")

        # --- THE ONLY BRANCH CONDITION THAT MATTERS ---
        if response.stop_reason == "end_turn":
            print("\n>>> Loop terminated correctly on end_turn.")
            final_text = "".join(
                block.text for block in response.content if block.type == "text"
            )
            print(f">>> Final answer: {final_text}")
            return final_text

        if response.stop_reason == "tool_use":
            # Append the assistant's turn (including tool_use blocks) to history
            messages.append({"role": "assistant", "content": response.content})

            # Execute EVERY tool_use block in this response, build tool_result blocks
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    result = execute_tool(block.name, block.input)
                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result,
                        }
                    )
                    print(f"  [executed]: {block.name} -> {result}")

            # Append tool results as a new user message
            messages.append({"role": "user", "content": tool_results})

            # Safety bound only — NOT the primary stop condition
            if iteration >= max_iterations:
                print(f"\n>>> Safety cap of {max_iterations} hit. Aborting loop.")
                return None
            continue

        # Any other stop_reason (e.g. max_tokens) — handle explicitly, don't guess
        print(f"\n>>> Unhandled stop_reason: {response.stop_reason}")
        return None


if __name__ == "__main__":
    run_agentic_loop(
        "Check the weather and time in Tokyo. Briefly say what you're about to do before calling any tools."
    )