import asyncio, json, os
from dotenv import load_dotenv
from pathlib import Path
from claude_agent_sdk import (
    ClaudeSDKClient, ClaudeAgentOptions, HookMatcher,
    tool, create_sdk_mcp_server, AssistantMessage, ResultMessage,
)
from gates import SessionState, check_call

env_path = Path(__file__).resolve().parent.parent / ".env"  # project root, independent of cwd
assert env_path.exists(), f"missing {env_path}"
load_dotenv(env_path)
state = SessionState()


def text(obj):
    return {"content": [{"type": "text", "text": json.dumps(obj)}]}


@tool("get_customer", "Look up a customer by name or email.", {"query": str})
async def get_customer(args):
    return text({"matches": [{"customer_id": "C1", "name": "Jane"}]})

@tool("lookup_order", "Get order details by order ID.", {"order_id": str})
async def lookup_order(args):
    return text({"order_id": args["order_id"], "total": 750, "status": "delivered"})

@tool("process_refund", "Refund an order. amount is in dollars.",
      {"order_id": str, "amount": float})
async def process_refund(args):
    return text({"refunded": args["amount"]})

@tool("escalate_to_human", "Escalate with a structured summary.",
      {"customer_id": str, "root_cause": str, "refund_amount": float,
       "recommended_action": str})
async def escalate_to_human(args):
    print("ESCALATED:", args)
    return text({"escalated": True})


async def pre_hook(input_data, tool_use_id, context):
    name = input_data["tool_name"].split("__")[-1]
    block = check_call(name, input_data["tool_input"], state)
    print(f"[PRE] {name} {input_data['tool_input']} -> {'DENY' if block else 'allow'}")
    if block:
        return {"hookSpecificOutput": {
            "hookEventName": input_data["hook_event_name"],
            "permissionDecision": "deny",
            "permissionDecisionReason": block["reason"]}}
    return {}


async def post_hook(input_data, tool_use_id, context):
    name = input_data["tool_name"].split("__")[-1]
    print("[POST]", name, "response shape:", type(input_data.get("tool_response")))
    if name == "get_customer":
        state.verified_customer_id = "C1"  # stub always returns one match
    return {}


async def main():
    server = create_sdk_mcp_server(name="support", version="1.0.0",
        tools=[get_customer, lookup_order, process_refund, escalate_to_human])
    options = ClaudeAgentOptions(
        model=os.environ["CLAUDE_MODEL"],
        max_turns=8,
        system_prompt="You are a support agent. Refunds of any amount are allowed.",
        mcp_servers={"support": server},
        allowed_tools=[f"mcp__support__{t}" for t in
                       ("get_customer", "lookup_order", "process_refund", "escalate_to_human")],
        hooks={
            "PreToolUse": [HookMatcher(matcher="^mcp__support__", hooks=[pre_hook])],
            "PostToolUse": [HookMatcher(matcher="^mcp__support__", hooks=[post_hook])],
        },
    )
    async with ClaudeSDKClient(options=options) as client:
        await client.query("I'm Jane. Refund my full $750 order A1, it arrived broken.")
        async for m in client.receive_response():
            if isinstance(m, (AssistantMessage, ResultMessage)):
                print(m)

asyncio.run(main())