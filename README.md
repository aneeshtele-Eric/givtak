# GIVTAK - Autonomous Agentic Mobility & Civic Telematics Protocol

**Live Cloud Run Service:** [https://givtak-589359892281.asia-south1.run.app](https://givtak-589359892281.asia-south1.run.app)  
**Built by:** Team Agent RASAR  
**Repository:** [https://github.com/aneeshtele-Eric/givtak](https://github.com/aneeshtele-Eric/givtak)

---

## 🏛️ Architecture Overview
GIVTAK is built on Google's official GenAI SDK (`google-genai`) with Function Calling (Tools), implementing the Agentic Orchestration pattern:  
> **"Gemini reasons. Deterministic tools decide."**

- **Agent Reasoning:** Google Gemini (`gemini-3.5-flash` with dynamic fallback cascade to `gemini-3.6-flash`, etc.)
- **Agent Tools:** 6 deterministic mathematical Python tools registered directly into the Gemini tool-calling engine:
  1. `calculate_haversine_pooling` — Anonymized corridor clustering (max 4.2 km detours, 4 riders/cab).
  2. `allocate_bus_hubs` — 32-seater EV shuttle consolidation along ORR/Whitefield hubs.
  3. `score_flood_risk` — Rainfall elevation gradient hazard matrix (Western Ghats / EcoShield).
  4. `census_tourist_geofence` — Zero-PII telecom antenna density estimation.
  5. `calculate_relief_supplies` — Disaster logistics staging (potable water, ration kits, medical crates).
  6. `correlate_corridor_traffic` — Live bottleneck mitigation and surge rerouting.
- **Server & APIs:** FastAPI with defensive security headers, HSTS, and CORS isolation.
- **State & Database:** Google Cloud Firestore (`asia-south1`) with in-memory resilient fallback.
- **Privacy & Governance:** Zero-PII SHA-256 worker tokenization with Human-in-the-Loop (HITL) approval gates.

---

## 🚀 Quickstart & Local Setup

### 1. Prerequisites
- Python 3.10+
- Google Gemini API key (optional for local testing; deterministic tool fallback activates if key is absent)

### 2. Installation
```bash
git clone https://github.com/aneeshtele-Eric/givtak.git
cd givtak
pip install -r requirements.txt
```

### 3. Run Locally
```bash
# Optional: set Gemini API Key
export GEMINI_API_KEY="your-gemini-api-key"
export GEMINI_MODEL="gemini-3.5-flash"

# Start the server
uvicorn server.py:app --host 0.0.0.0 --port 8080 --reload
```
Open [http://localhost:8080](http://localhost:8080) in your browser.

---

## 🧪 Automated Testing
Run the automated test suite with pytest:
```bash
pytest test_app.py -v
```

---

## 📡 Key API Endpoints
| Endpoint | Method | Purpose |
|---|---|---|
| `/` | `GET` | Serves the GIVTAK Mission Control dashboard |
| `/api/ask` | `POST` | Agentic Gemini reasoning & tool execution dispatcher |
| `/api/health` | `GET` | Health diagnostics & active Gemini model telemetry |
| `/api/runs` | `GET` | Live audit trail of model reasoning & tool executions |
| `/api/approve` | `POST` | Human-in-the-Loop (HITL) operator sign-off audit log |
| `/api/optin` | `POST` | Zero-PII employee corridor opt-in endpoint |
| `/api/fleet/submit`| `POST` | Enterprise fleet consolidation submission |
