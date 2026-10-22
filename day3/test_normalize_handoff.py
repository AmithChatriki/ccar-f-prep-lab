from normalize import normalize_result
from handoff import build_handoff

ship = normalize_result("get_shipment", {"delivered_at": 1760000000, "status": 3})
inv = normalize_result("get_invoice", {"issued_at": "2025-10-09T08:00:00Z", "status": "paid"})
print(ship, inv, sep="\n")

assert ship["delivered_at"].endswith("+00:00") and inv["issued_at"].endswith("+00:00")
assert ship["status"] == "delivered"

odd = normalize_result("get_shipment", {"delivered_at": None, "status": 99})
assert odd["status"] == "unknown" and odd["status_raw"] == 99

h = build_handoff(customer_id="C1", root_cause="Duplicate charge on order A1",
                  refund_amount=750, recommended_action="Approve refund of 750",
                  order_ids=["A1"], attempted_steps=["verified customer", "confirmed duplicate"])
try:
    build_handoff(customer_id="C1", root_cause="x")
except ValueError as e:
    print("rejected:", e)

print("normalize + handoff tests passed")