"""
Antigravity Test Suite: Automated verification of policy hooks & agent tools.
"""
from antigravity_guard import security_guard
from agent_engine import match_company_cabs, match_company_buses

def test_consent_policy():
    print("\n--- TEST 1: Consent Boundary Enforcement ---")
    mock_commuters = [
        {"emp_id": "TEST-01", "consent": "full"},
        {"emp_id": "TEST-02", "consent": "none"},
        {"emp_id": "TEST-03", "consent": "anonymous"}
    ]
    cleared = security_guard.intercept_cab_candidates(mock_commuters)
    assert len(cleared) == 2, "Failed: Guard did not drop non-consented commuter!"
    assert "TEST-02" not in [c["emp_id"] for c in cleared], "Failed: Leaked unconsented profile!"
    print("✓ PASSED: Non-consented commuter TEST-02 was blocked by Antigravity.")

def test_time_window_policy():
    print("\n--- TEST 2: Shift Window Tolerance ---")
    valid_window = security_guard.validate_time_window("08:30", "08:45")  # 15 mins
    invalid_window = security_guard.validate_time_window("08:30", "09:00") # 30 mins
    assert valid_window is True, "Failed: 15-minute gap should be accepted."
    assert invalid_window is False, "Failed: 30-minute gap should be rejected."
    print("✓ PASSED: Time delta limits enforced successfully.")

def test_end_to_end_cab_matcher():
    print("\n--- TEST 3: End-to-End Cab Match Tool ---")
    result = match_company_cabs("Whitefield")
    print(f"Tool Output: {result}")
    assert "Cab Match Success" in result, "Failed: Cab match did not complete."
    print("✓ PASSED: Cab matcher integrated with Antigravity guard.")

if __name__ == "__main__":
    print("================ RUNNING ANTIGRAVITY TEST SUITE ================")
    test_consent_policy()
    test_time_window_policy()
    test_end_to_end_cab_matcher()
    print("\n================ ALL 3 TEST SUITES PASSED ================\n")