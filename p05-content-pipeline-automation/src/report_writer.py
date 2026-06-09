"""Report writing helpers for local demo outputs."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Iterable

from models import WorkflowItem


def write_csv(path: Path, items: list[WorkflowItem]) -> None:
    """Write the evaluated workflow items to a CSV report."""

    path.parent.mkdir(parents=True, exist_ok=True)
    rows = [item.to_report_row() for item in items]
    fieldnames = ["item_id", "label", "score", "status", "flags", "actions", "summary", "source_file"]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path: Path, title: str, items: Iterable[WorkflowItem]) -> None:
    """Write a human-readable review report."""

    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"# {title}", "", "Nothing is sent or published by this demo.", ""]
    for item in items:
        lines.extend(
            [
                f"## {item.label}",
                f"- ID: {item.item_id}",
                f"- Status: {item.evaluation.status}",
                f"- Score: {item.evaluation.score}",
                f"- Summary: {item.evaluation.summary}",
                f"- Flags: {', '.join(item.evaluation.flags) if item.evaluation.flags else 'none'}",
                f"- Human actions: {', '.join(item.evaluation.actions) if item.evaluation.actions else 'none'}",
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def write_jsonl(path: Path, items: Iterable[WorkflowItem]) -> None:
    """Write a replay/debug log as JSON lines."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for item in items:
            handle.write(
                json.dumps(
                    {
                        "item_id": item.item_id,
                        "label": item.label,
                        "status": item.evaluation.status,
                        "score": item.evaluation.score,
                        "flags": item.evaluation.flags,
                        "actions": item.evaluation.actions,
                    },
                    sort_keys=True,
                )
                + "\n"
            )
