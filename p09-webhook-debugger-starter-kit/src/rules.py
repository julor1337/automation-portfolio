"""Webhook schema validation and event routing rules."""

from __future__ import annotations

from typing import Any

from models import Evaluation


REQUIRED = {"event_id", "event_type", "source", "payload"}
SUPPORTED = {"order.created", "lead.created", "refund.created"}


def evaluate(record: dict[str, Any]) -> Evaluation:
    flags: list[str] = []
    actions = ["do not expose public webhook URLs in demos"]
    score = 40

    missing = sorted(REQUIRED - set(record))
    for field in missing:
        flags.append(f"missing_{field}")
        actions.append(f"add {field}")
        score -= 20

    event_type = str(record.get("event_type", ""))
    if event_type in SUPPORTED:
        flags.append("supported_event")
        actions.append(f"route to {event_type.replace('.', '_')} handler")
        score += 35
    else:
        flags.append("unsupported_event")
        actions.append("create or reject route")
        score -= 10

    payload = record.get("payload")
    if isinstance(payload, dict) and payload:
        flags.append("payload_present")
        score += 15
    else:
        flags.append("empty_payload")
        actions.append("inspect payload schema")

    status = "accepted_for_local_route" if score >= 70 and not missing else "rejected_for_review"
    summary = f"{event_type or 'missing event'} from {record.get('source', 'unknown source')}."
    return Evaluation(score=max(0, min(score, 100)), status=status, summary=summary, flags=flags, actions=actions)
