"""Workflow health and retry priority rules."""

from __future__ import annotations

from typing import Any

from models import Evaluation


SLOW_SECONDS = 120


def evaluate(record: dict[str, Any]) -> Evaluation:
    duration = int(float(str(record.get("duration_seconds") or 0)))
    status_raw = str(record.get("status", "")).lower()
    error = str(record.get("error", "")).strip()
    flags: list[str] = []
    actions = ["owner reviews retry before rerunning live automation"]
    score = 20

    if status_raw == "failed":
        flags.append("failed_run")
        actions.append("investigate error")
        score += 55
    if duration > SLOW_SECONDS:
        flags.append("slow_run")
        actions.append("inspect bottleneck")
        score += 30
    if "approval" in error.lower():
        flags.append("approval_gate_issue")
        actions.append("check human approval flag")
        score += 10
    if not error and status_raw == "success":
        flags.append("healthy")
        score -= 10

    status = "retry_or_review" if score >= 60 else "healthy"
    summary = f"{record.get('workflow')} run {record.get('run_id')} finished as {status_raw} in {duration}s."
    return Evaluation(score=max(0, min(score, 100)), status=status, summary=summary, flags=flags, actions=actions)
