"""Support ticket classification rules."""

from __future__ import annotations

from typing import Any

from models import Evaluation


def evaluate(record: dict[str, Any]) -> Evaluation:
    message = str(record.get("message", "")).lower()
    plan = str(record.get("plan", "")).lower()
    flags: list[str] = []
    actions = ["human approves response before sending"]
    score = 20

    if any(term in message for term in ("api", "webhook", "500")):
        flags.append("technical_issue")
        actions.append("escalate to technical review")
        score += 45
    if any(term in message for term in ("failed", "stuck", "blocked", "cannot log in")):
        flags.append("customer_blocked")
        actions.append("prioritize first response")
        score += 35
    if "billing" in message:
        flags.append("account_billing")
        score += 20
    if plan == "enterprise":
        flags.append("enterprise_account")
        score += 15
    if "thanks" in message:
        flags.append("positive_sentiment")
        score -= 10

    status = "escalate" if score >= 70 else "standard_reply"
    summary = f"Ticket {record.get('ticket_id')} from {record.get('customer')} needs {status}."
    return Evaluation(score=max(0, min(score, 100)), status=status, summary=summary, flags=flags, actions=actions)
