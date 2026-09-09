from fastapi import FastAPI
from change_manager.models import ChangeRequest
from change_manager.policy import RiskEngine, PolicyEngine

app = FastAPI(title="AI Change Manager")

risk_engine = RiskEngine()
policy_engine = PolicyEngine()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/assess")
def assess(change: ChangeRequest):
    assessment = risk_engine.assess(change)
    decision = policy_engine.authorize(assessment)
    return {"assessment": assessment.model_dump(), "policy": decision}
