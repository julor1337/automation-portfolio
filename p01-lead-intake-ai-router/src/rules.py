"""Lead validation, scoring, and routing rules."""

from __future__ import annotations

import re
from typing import Any

from models import Evaluation


EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def _number(value: Any) -> int:
    try:
        return int(float(str(value or 0)))
    except ValueError:
        return 0


def evaluate(record: dict[str, Any]) -> Evaluation:
    flags: list[str] = []
    actions: list[str] = ["owner review before sending any message"]
    score = 0

    if not EMAIL_RE.match(str(record.get("email", ""))):
        flags.append("invalid_email")
        actions.append("confirm contact details")

    budget = _number(record.get("budget"))
    employees = _number(record.get("employees"))
    source = str(record.get("source", "")).lower()

    if budget >= 15000:
        score += 45
        flags.append("large_budget")
    elif budget >= 5000:
        score += 25
        flags.append("medium_budget")
    else:
        flags.append("small_budget")

    if employees >= 50:
        score += 30
        flags.append("established_team")
    if source in {"referral", "partner"}:
        score += 20
        flags.append("warm_source")
    elif source in {"website", "linkedin"}:
        score += 10
        flags.append("direct_inbound")

    status = "ready_for_review" if score >= 60 and "invalid_email" not in flags else "needs_review"
    if status == "ready_for_review":
        actions.append("prepare scoped follow-up draft")
    else:
        actions.append("qualify manually before prioritizing")

    summary = f"{record.get('company', 'Unknown company')} needs {record.get('need', 'automation support')}."
    return Evaluation(score=min(score, 100), status=status, summary=summary, flags=flags, actions=actions)
