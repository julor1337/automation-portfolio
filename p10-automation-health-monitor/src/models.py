"""Shared data objects for this automation demo."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Evaluation:
    """Decision output produced by the workflow rules."""

    score: int
    status: str
    summary: str
    flags: list[str] = field(default_factory=list)
    actions: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class WorkflowItem:
    """A raw input record plus the workflow evaluation."""

    item_id: str
    label: str
    raw: dict[str, Any]
    evaluation: Evaluation

    def to_report_row(self) -> dict[str, str]:
        """Flatten the item into a CSV-safe report row."""

        return {
            "item_id": self.item_id,
            "label": self.label,
            "score": str(self.evaluation.score),
            "status": self.evaluation.status,
            "flags": "; ".join(self.evaluation.flags),
            "actions": "; ".join(self.evaluation.actions),
            "summary": self.evaluation.summary,
            "source_file": str(self.raw.get("_source_file", "")),
        }


def safe_text(value: Any) -> str:
    """Convert nested values into compact text for reports."""

    if isinstance(value, (dict, list)):
        return json.dumps(value, sort_keys=True)
    return str(value)
