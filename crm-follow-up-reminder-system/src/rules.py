"""CRM follow-up rules."""

from __future__ import annotations

from datetime import date, datetime
from typing import Any

from models import Evaluation


TODAY = date(2026, 6, 9)


def evaluate(record: dict[str, Any]) -> Evaluation:
    due = datetime.strptime(str(record.get("due_date")), "%Y-%m-%d").date()
    value = int(float(str(record.get("value") or 0)))
    status_raw = str(record.get("status", "")).lower()
    days_overdue = max((TODAY - due).days, 0)
    flags: list[str] = []
    actions = ["owner approval before sending any reminder"]
    score = 20

    if due <= TODAY:
        flags.append("followup_due")
        actions.append("draft reminder")
        score += 35
    if days_overdue >= 2:
        flags.append("overdue")
        actions.append("prioritize today")
        score += 20
    if value >= 2500:
        flags.append("high_value_opportunity")
        score += 25
    if status_raw == "warm":
        flags.append("warm_lead")
        score += 15
    if status_raw == "cold":
        flags.append("low_priority")
        score -= 10

    status = "due_now" if score >= 65 else "monitor"
    summary = f"{record.get('company')} next step: {record.get('next_step')}."
    return Evaluation(score=max(0, min(score, 100)), status=status, summary=summary, flags=flags, actions=actions)
