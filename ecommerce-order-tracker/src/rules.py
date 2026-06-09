"""Fulfillment risk rules for e-commerce orders."""

from __future__ import annotations

from datetime import date, datetime
from typing import Any

from models import Evaluation


TODAY = date(2026, 6, 9)


def _date(value: Any) -> date | None:
    return datetime.strptime(str(value), "%Y-%m-%d").date() if value else None


def evaluate(record: dict[str, Any]) -> Evaluation:
    status = str(record.get("status", "")).lower()
    promised = _date(record.get("promised_ship_date"))
    shipped = _date(record.get("ship_date"))
    total = float(record.get("total") or 0)
    days_late = 0 if shipped or not promised else max((TODAY - promised).days, 0)
    flags: list[str] = []
    actions = ["owner reviews before any customer message"]
    score = 20

    if status == "exception":
        flags.append("fulfillment_exception")
        actions.append("inspect order manually")
        score += 60
    if days_late > 0:
        flags.append(f"{days_late}_days_late")
        actions.append("draft customer update")
        score += min(days_late * 20, 50)
    if status == "paid" and not shipped:
        flags.append("unshipped_paid_order")
        actions.append("confirm fulfillment queue")
        score += 20
    if total >= 200:
        flags.append("high_value_order")
        actions.append("prioritize review")
        score += 10

    review_status = "urgent_review" if score >= 70 else "monitor"
    summary = f"Order {record.get('order_id')} on {record.get('channel')} is {status}."
    return Evaluation(score=min(score, 100), status=review_status, summary=summary, flags=flags, actions=actions)
