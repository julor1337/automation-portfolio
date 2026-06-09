"""Product listing generation and QA rules."""

from __future__ import annotations

from typing import Any

from models import Evaluation


def _tags(record: dict[str, Any]) -> list[str]:
    source = " ".join(
        str(record.get(field, ""))
        for field in ("product_name", "category", "style", "audience")
    )
    words = [word.strip(" ,;").lower() for word in source.replace("-", " ").split()]
    return list(dict.fromkeys(word for word in words if len(word) > 2))[:13]


def evaluate(record: dict[str, Any]) -> Evaluation:
    tags = _tags(record)
    price = float(record.get("price") or 0)
    title = f"{record.get('style', '').title()} {record.get('product_name')} for {record.get('audience', '').title()}"
    flags: list[str] = []
    actions = ["owner review before publishing listing"]
    score = 40

    if len(title) <= 140:
        flags.append("title_length_ok")
        score += 20
    else:
        flags.append("title_too_long")
        actions.append("shorten title")
    if len(tags) >= 6:
        flags.append("tags_ready")
        score += 20
    if price > 0:
        flags.append("price_present")
        score += 10
    if "instant download" in str(record.get("features", "")).lower():
        flags.append("digital_delivery_clear")
        score += 10

    status = "ready_for_marketplace_review" if score >= 75 else "needs_qa"
    summary = f"Draft listing: {title}. Tags: {', '.join(tags)}."
    return Evaluation(score=min(score, 100), status=status, summary=summary, flags=flags, actions=actions)
