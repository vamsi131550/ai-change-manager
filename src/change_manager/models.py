from enum import Enum
from pydantic import BaseModel, Field


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ChangeRequest(BaseModel):
    change_id: str
    requester: str
    description: str
    repository: str
    environment: str = "sandbox"
    requested_action: str


class RiskAssessment(BaseModel):
    score: int = Field(ge=0, le=100)
    level: RiskLevel
    reasons: list[str]


class Approval(BaseModel):
    approval_id: str
    change_id: str
    status: str = "PENDING"
    reason: str


class AuditEvent(BaseModel):
    event_id: str
    change_id: str
    actor: str
    actor_type: str
    action: str
    policy_decision: str
