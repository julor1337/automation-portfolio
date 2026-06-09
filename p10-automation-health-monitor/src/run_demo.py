from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "sample-data" / "workflow_runs.csv"
OUT = ROOT / "outputs"
SLOW_SECONDS = 120


def main() -> None:
    OUT.mkdir(exist_ok=True)
    rows = list(csv.DictReader(DATA.open(newline="", encoding="utf-8")))
    status_counts = Counter(row["status"] for row in rows)
    workflow_counts: dict[str, int] = defaultdict(int)
    retry_rows: list[dict[str, str]] = []

    for row in rows:
        workflow_counts[row["workflow"]] += 1
        duration = int(row["duration_seconds"])
        if row["status"] != "success" or duration > SLOW_SECONDS:
            retry_rows.append({
                "workflow": row["workflow"],
                "run_id": row["run_id"],
                "reason": row["error"] or f"slow run: {duration}s",
                "priority": "high" if row["status"] == "failed" else "medium",
                "owner_review_required": "yes",
            })

    report = [
        "# Automation Health Report",
        "",
        f"Total runs: {len(rows)}",
        f"Successful runs: {status_counts['success']}",
        f"Failed runs: {status_counts['failed']}",
        "",
        "## Runs by workflow",
        *[f"- {workflow}: {count}" for workflow, count in sorted(workflow_counts.items())],
        "",
        "## Attention needed",
        *[f"- {row['workflow']} / {row['run_id']}: {row['reason']} ({row['priority']})" for row in retry_rows],
        "",
    ]
    (OUT / "health_report.md").write_text("\n".join(report), encoding="utf-8")
    with (OUT / "retry_checklist.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["workflow", "run_id", "reason", "priority", "owner_review_required"])
        writer.writeheader()
        writer.writerows(retry_rows)
    print("Wrote health_report.md and retry_checklist.csv")


if __name__ == "__main__":
    main()
