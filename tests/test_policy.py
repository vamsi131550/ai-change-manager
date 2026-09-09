from change_manager.models import ChangeRequest, RiskLevel
from change_manager.policy import RiskEngine, PolicyEngine


def make_change(description, action="change"):
    return ChangeRequest(
        change_id="c-1",
        requester="demo",
        description=description,
        repository="sample-service",
        requested_action=action,
    )


def test_low_risk_is_autonomous():
    a = RiskEngine().assess(make_change("update documentation"))
    assert a.level == RiskLevel.LOW
    assert not PolicyEngine().authorize(a)["approval_required"]


def test_production_requires_approval():
    a = RiskEngine().assess(make_change("deploy to production"))
    assert a.level in {RiskLevel.HIGH, RiskLevel.CRITICAL}
    decision = PolicyEngine().authorize(a)
    assert decision["allowed"]


def test_destructive_operation_denied():
    a = RiskEngine().assess(make_change("delete production database"))
    assert a.level == RiskLevel.CRITICAL
    assert not PolicyEngine().authorize(a)["allowed"]
