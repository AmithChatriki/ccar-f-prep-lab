from gates import SessionState, check_call, record_result

s = SessionState()

# 1. Skip path: order lookup before verification must be blocked
assert check_call("lookup_order", {"order_id": "A1"}, s)["blocked"]
assert check_call("process_refund", {"amount": 20}, s)["blocked"]

# 2. Multiple matches must NOT verify
record_result("get_customer", {"matches": [{"customer_id": "C1"}, {"customer_id": "C2"}]}, s)
assert s.verified_customer_id is None

# 3. Single match verifies; gated tools now allowed
record_result("get_customer", {"matches": [{"customer_id": "C1"}]}, s)
assert check_call("lookup_order", {"order_id": "A1"}, s) is None

# 4. Boundary behavior around the $500 limit
assert check_call("process_refund", {"amount": 499}, s) is None
assert check_call("process_refund", {"amount": 500}, s) is None
assert check_call("process_refund", {"amount": 501}, s)["blocked"]

print("all gate tests passed")