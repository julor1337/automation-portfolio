"""Workflow pipeline for Client Onboarding Automation."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from config import (
    INPUT_MODE,
    INPUT_PATH,
    ITEM_ID_FIELD,
    LABEL_FIELD,
    LOG_JSONL,
    MARKDOWN_TITLE,
    OUTPUT_CSV,
    OUTPUT_MARKDOWN,
)
from models import WorkflowItem
from report_writer import write_csv, write_jsonl, write_markdown
from rules import evaluate


def _parse_key_value_text(path: Path) -> dict[str, Any]:
    record: dict[str, Any] = {"_source_file": path.name}
    for line in path.read_text(encoding="utf-8").splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        normalized = key.strip().lower().replace(" ", "_")
        record[normalized] = value.strip()
    return record


def load_records() -> list[dict[str, Any]]:
    """Load sample records from CSV, JSON files, or key-value text files."""

    if INPUT_MODE == "csv":
        with INPUT_PATH.open(newline="", encoding="utf-8") as handle:
            records = list(csv.DictReader(handle))
        for record in records:
            record["_source_file"] = INPUT_PATH.name
        return records

    if INPUT_MODE == "json_dir":
        records = []
        for path in sorted(INPUT_PATH.glob("*.json")):
            record = json.loads(path.read_text(encoding="utf-8"))
            record["_source_file"] = path.name
            records.append(record)
        return records

    if INPUT_MODE == "text_dir":
        return [_parse_key_value_text(path) for path in sorted(INPUT_PATH.glob("*.txt"))]

    raise ValueError(f"Unsupported INPUT_MODE: {INPUT_MODE}")


def _field(record: dict[str, Any], name: str, fallback: str = "") -> str:
    value = record.get(name)
    if value is None:
        return fallback
    return str(value)


def process_records(records: list[dict[str, Any]]) -> list[WorkflowItem]:
    """Evaluate raw records and return report-ready workflow items."""

    items: list[WorkflowItem] = []
    for index, record in enumerate(records, start=1):
        item_id = _field(record, ITEM_ID_FIELD, f"item-{index:03d}")
        label = _field(record, LABEL_FIELD, item_id)
        items.append(WorkflowItem(item_id=item_id, label=label, raw=record, evaluation=evaluate(record)))
    return items


def run_pipeline() -> list[WorkflowItem]:
    """Run the full local workflow and write output files."""

    items = process_records(load_records())
    write_csv(OUTPUT_CSV, items)
    write_markdown(OUTPUT_MARKDOWN, MARKDOWN_TITLE, items)
    if LOG_JSONL is not None:
        write_jsonl(LOG_JSONL, items)
    print(f"Wrote {OUTPUT_CSV}")
    print(f"Wrote {OUTPUT_MARKDOWN}")
    if LOG_JSONL is not None:
        print(f"Wrote {LOG_JSONL}")
    return items
