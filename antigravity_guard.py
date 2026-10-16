"""
Antigravity Policy & Evaluation Guard for SHARE Prototype
Enforces zero-trust privacy boundaries and multi-firm governance.
"""
from typing import List, Dict, Any

class AntigravityPolicyViolation(Exception):
    pass

class AntigravitySecurityGuard:
    def __init__(self, max_allowed_time_delta_mins: int = 15):
        self.max_time_delta = max_allowed_time_delta_mins

    def intercept_cab_candidates(self, candidates: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Policy Rule 1: Zero Data Leakage for Non-Consenting Commuters.
        Drops any commuter record whose consent is not 'full' or 'anonymous'.
        """
        sanitized = []
        for c in candidates:
            consent = c.get("consent", "none").lower()
            if consent in ["full", "anonymous"]:
                sanitized.append(c)
            else:
                print(f"[ANTIGRAVITY GUARD] Blocked commuter {c.get('emp_id')}: Consent missing or denied.")
        return sanitized

    def validate_time_window(self, time_str_1: str, time_str_2: str) -> bool:
        """
        Policy Rule 2: Strict Shift Tolerance Window (<= 15 minutes).
        """
        def to_minutes(t_str: str) -> int:
            h, m = map(int, t_str.strip().split(":"))
            return h * 60 + m

        delta = abs(to_minutes(time_str_1) - to_minutes(time_str_2))
        return delta <= self.max_time_delta

# Global singleton guard instance
security_guard = AntigravitySecurityGuard()