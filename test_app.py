import unittest
from fastapi.testclient import TestClient
from server import (
    app,
    calculate_haversine_pooling,
    allocate_bus_hubs,
    score_flood_risk,
    calculate_relief_supplies,
    haversine_distance
)

client = TestClient(app)

class TestGivtakPlatform(unittest.TestCase):

    def test_01_health_endpoint(self):
        """Verify system diagnostics and health endpoint."""
        response = client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "healthy")
        self.assertEqual(data["service"], "givtak")
        self.assertIn("active_gemini_model", data)
        self.assertIn("model_fallbacks", data)
        self.assertIn("uptime_seconds", data)

    def test_02_serve_index(self):
        """Verify that the frontend dashboard loads successfully."""
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("GIVTAK", response.text)

    def test_03_haversine_math(self):
        """Verify accurate distance calculations between coordinates."""
        # Bengaluru Whitefield to Marathahalli (~6.5 km)
        dist = haversine_distance(12.9716, 77.7500, 12.9562, 77.7019)
        self.assertTrue(5.0 <= dist <= 8.0)

    def test_04_deterministic_cab_pooling_tool(self):
        """Verify zero-PII cab pooling optimizer forms valid clusters."""
        result = calculate_haversine_pooling()
        self.assertIn("clusters_formed", result)
        self.assertIn("total_riders_pooled", result)
        self.assertIn("co2_avoided_kg", result)
        self.assertGreater(result["clusters_formed"], 0)
        self.assertGreater(result["total_riders_pooled"], 0)
        self.assertGreater(result["co2_avoided_kg"], 0)

    def test_05_deterministic_bus_hub_tool(self):
        """Verify EV shuttle hub consolidation operates within corridor bounds."""
        result = allocate_bus_hubs()
        self.assertIn("hub", result)
        self.assertIn("passengers_assigned", result)
        self.assertIn("co2_saved_kg", result)
        self.assertGreaterEqual(result["passengers_assigned"], 1)

    def test_06_deterministic_relief_supplies_tool(self):
        """Verify disaster relief supply staging scales correctly."""
        result = calculate_relief_supplies(location="Chikmagalur", rain_rate=114.0, stranded_count=1200)
        self.assertEqual(result["location"], "Chikmagalur")
        self.assertEqual(result["potable_water_liters_24h"], 1200 * 3)
        self.assertEqual(result["meal_packets_24h"], 1200 * 2)
        self.assertEqual(result["stranded_population"], 1200)

    def test_07_agent_query_dispatch(self):
        """Verify agent query endpoint dispatches successfully without throwing."""
        response = client.post("/api/ask", json={"query": "Optimize cab pool for Whitefield tech parks"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("response", data)
        self.assertIn("model", data)
        self.assertIn("tools", data)
        self.assertTrue(len(data["model"]) > 0)

    def test_08_input_validation_limits(self):
        """Verify Pydantic input constraints enforce safety limits (rider count <= 500)."""
        invalid_fleet = {
            "company_name": "Nimbus Tech",
            "shift_time": "09:00",
            "employee_count": 9999,  # exceeds max 500 limit
            "fleet_partner": "Routematic"
        }
        response = client.post("/api/onboard-fleet", json=invalid_fleet)
        self.assertEqual(response.status_code, 422)

    def test_09_human_in_the_loop_approval(self):
        """Verify operations lead HITL sign-off gets audited."""
        payload = {
            "action": "Approve EV shuttle re-routing via Marathahalli Hub",
            "operator_role": "Corridor Operations Lead",
            "notes": "Verified traffic reduction on Outer Ring Road"
        }
        response = client.post("/api/approve", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertIn("audit_record", data)
        self.assertIn("approval_id", data["audit_record"])

if __name__ == "__main__":
    unittest.main()
