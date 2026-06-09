"""Invoice validation and categorization rules."""

from __future__ import annotations

from typing import Any

from models import Evaluation


def _amount(value: Any) -> float:
    try:
        return float(str(value or 0).replace("$", ""))
    except ValueError:
        return 0.0


def evaluate(record: dict[str, Any]) -> Evaluation:
    flags: list[str] = []
    actions = ["owner reviews extracted fields before bookkeeping import"]
    amount = _amount(record.get("amount"))
    category = str(record.get("category", "")).lower()
    score = 50

    for field in ("vendor", "date", "category"):
        if not record.get(field):
            flags.append(f"missing_{field}")
            actions.append(f"confirm {field}")
            score -= 15
    if amount <= 0:
        flags.append("missing_or_invalid_amount")
        actions.append("confirm invoice amount")
        score -= 25
    elif amount >= 100:
        flags.append("high_value_expense")
        actions.append("review approval threshold")
        score += 20
    if category in {"software", "shipping", "marketing"}:
        flags.append(f"category_{category}")
        score += 15

    status = "ready_for_review" if score >= 60 and "missing_or_invalid_amount" not in flags else "needs_manual_check"
    summary = f"{record.get('vendor', 'Unknown vendor')} expense in {record.get('category', 'uncategorized')}."
    return Evaluation(score=max(0, min(score, 100)), status=status, summary=summary, flags=flags, actions=actions)
