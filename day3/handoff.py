REQUIRED = ("customer_id", "root_cause", "refund_amount", "recommended_action")


def build_handoff(**fields) -> dict:
    missing = [f for f in REQUIRED if fields.get(f) in (None, "")]
    if missing:
        raise ValueError(f"handoff missing required fields: {missing}")
    return fields  # extras (order_ids, attempted_steps) pass through