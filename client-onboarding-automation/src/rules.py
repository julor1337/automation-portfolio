"""Onboarding packet and risk rules."""

from __future__ import annotations

from typing import Any

from models import Evaluation


def _number(value: Any) -> int:
    try:
        return int(float(str(value or 0)))
    except ValueError:
        return 0


def evaluate(record: dict[str, Any]) -> Evaluation:
    tools = str(record.get("tools", ""))
    timeline = _number(record.get("timeline_days"))
    flags: list[str] = []
    actions = [
        "create kickoff checklist",
        "prepare folder plan",
        "owner approves requirements before live connection",
    ]
    score = 40

    tool_count = len([tool for tool in tools.split(";") if tool.strip()])
    score += min(tool_count * 10, 30)
    if tool_count >= 3:
        flags.append("multi_tool_workflow")
        actions.append("map integration dependencies")
    if timeline <= 5:
        flags.append("tight_timeline")
        actions.append("confirm reduced scope")
        score -= 10
    if "n8n" in tools.lower() or "zapier" in tools.lower():
        flags.append("automation_platform_ready")
        score += 15

    status = "ready_for_kickoff" if score >= 60 and "tight_timeline" not in flags else "needs_scope_review"
    summary = f"{record.get('client_name')} needs {record.get('service')} for {record.get('goal')}."
    return Evaluation(score=max(0, min(score, 100)), status=status, summary=summary, flags=flags, actions=actions)
