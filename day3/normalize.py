from datetime import datetime, timezone

# Shipment system uses numeric codes; invoice system uses text.
SHIPMENT_STATUS = {1: "pending", 2: "shipped", 3: "delivered"}


def to_iso(value) -> str | None:
    """Unix epoch (int/float) or ISO 8601 string -> ISO 8601 UTC string."""
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return datetime.fromtimestamp(value, tz=timezone.utc).isoformat()
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)  # assumption: naive means UTC
    return dt.astimezone(timezone.utc).isoformat()


def normalize_result(tool_name: str, result: dict) -> dict:
    out = dict(result)
    for key in ("delivered_at", "issued_at"):
        if key in out:
            out[key] = to_iso(out[key])
    if tool_name == "get_shipment" and "status" in out:
        raw = out["status"]
        out["status"] = SHIPMENT_STATUS.get(raw, "unknown")
        if out["status"] == "unknown":
            out["status_raw"] = raw  # keep the original, never guess
    return out