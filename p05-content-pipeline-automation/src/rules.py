"""Content planning and approval rules."""

from __future__ import annotations

from typing import Any

from models import Evaluation


def evaluate(record: dict[str, Any]) -> Evaluation:
    priority = str(record.get("priority", "")).lower()
    effort = str(record.get("effort", "")).lower()
    platform = str(record.get("platform", ""))
    flags: list[str] = [f"platform_{platform.lower()}"]
    actions = ["owner approval before publishing"]
    score = 35

    if priority == "high":
        score += 35
        flags.append("high_priority")
    elif priority == "medium":
        score += 20
    if effort == "low":
        score += 20
        flags.append("quick_win")
    elif effort == "high":
        actions.append("prepare longer outline")
    if str(record.get("goal", "")).lower() in {"authority", "trust"}:
        score += 15
        flags.append("trust_building")

    status = "draft_ready" if score >= 65 else "needs_outline"
    actions.append("create hook and repurpose checklist")
    summary = f"{record.get('idea')} targets {record.get('audience')} on {platform}."
    return Evaluation(score=min(score, 100), status=status, summary=summary, flags=flags, actions=actions)
