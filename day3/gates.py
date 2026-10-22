from dataclasses import dataclass

REFUND_LIMIT = 500  # policy: above $500 needs a human
GATED_TOOLS = {"lookup_order", "process_refund"}


@dataclass
class SessionState:
    verified_customer_id: str | None = None


def check_call(name: str, args: dict, state: SessionState) -> dict | None:
    """Return None to allow the call, or a tool-result dict to block it."""
    if name in GATED_TOOLS and state.verified_customer_id is None:
        return {
            "blocked": True,
            "reason": "Customer not verified. Call get_customer first and "
                      "use the verified customer ID.",
        }
    if name == "process_refund" and args.get("amount", 0) > REFUND_LIMIT:
        return {
            "blocked": True,
            "reason": f"Refund exceeds the ${REFUND_LIMIT} automated limit. "
                      "Call escalate_to_human with a structured summary.",
        }
    return None


def record_result(name: str, result: dict, state: SessionState) -> None:
    """Update state from tool results (only a single match counts as verified)."""
    if name == "get_customer":
        matches = result.get("matches", [])
        if len(matches) == 1:
            state.verified_customer_id = matches[0]["customer_id"]