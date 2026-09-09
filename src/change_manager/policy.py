from change_manager.models import RiskAssessment, RiskLevel


class RiskEngine:
    def assess(self, change) -> RiskAssessment:
        text = f"{change.description} {change.requested_action}".lower()
        score = 10
        reasons = ["sandbox operation"]

        if "production" in text:
            score += 45
            reasons.append("production environment requested")
        if "database" in text or "migration" in text:
            score += 25
            reasons.append("database change")
        if "authentication" in text or "authorization" in text:
            score += 30
            reasons.append("security-sensitive change")
        if "delete" in text or "destroy" in text:
            score = 100
            reasons.append("destructive operation")

        if score >= 80:
            level = RiskLevel.CRITICAL
        elif score >= 60:
            level = RiskLevel.HIGH
        elif score >= 30:
            level = RiskLevel.MEDIUM
        else:
            level = RiskLevel.LOW

        return RiskAssessment(score=score, level=level, reasons=reasons)


class PolicyEngine:
    def authorize(self, assessment: RiskAssessment) -> dict:
        if assessment.level == RiskLevel.CRITICAL:
            return {"allowed": False, "approval_required": False, "reason": "critical action denied"}
        if assessment.level == RiskLevel.HIGH:
            return {"allowed": True, "approval_required": True, "reason": "human approval required"}
        return {"allowed": True, "approval_required": False, "reason": "within autonomous policy"}
