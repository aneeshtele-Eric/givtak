# GIVTAK - Autonomous Agentic Mobility & Civic Telematics 
 
**Live Cloud Run Deployment:** https://givtak-589359892281.asia-south1.run.app 
 
Built by **Team Agent RASAR** for the Google AI Agent Hackathon. 
 
## Architecture 
GIVTAK is built on Google's Agent Development Kit (ADK) pattern: **"Gemini reasons. Deterministic tools decide."** 
- **LLM Reasoning:** Gemini 3.5 Flash (with automatic fallbacks) 
- **Agent Tools:** 6 Deterministic Python Tools (Haversine pooling, EV bus allocator, flood risk scorer, geofence census, relief calculator, traffic correlator) 
- **Infrastructure:** Google Cloud Run (asia-south1), Artifact Registry, Cloud Build 
- **State & Database:** Google Cloud Firestore 
- **Governance:** Privacy Guard PII tokenization & Human-in-the-Loop (HITL) ops approvals.
