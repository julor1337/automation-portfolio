from __future__ import annotations

import csv
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "sample-data" / "content_ideas.csv"
OUT = ROOT / "outputs"
START = date(2026, 6, 10)


def main() -> None:
    OUT.mkdir(exist_ok=True)
    ideas = list(csv.DictReader(DATA.open(newline="", encoding="utf-8")))
    ideas.sort(key=lambda row: 0 if row["priority"] == "high" else 1)
    calendar_rows: list[dict[str, str]] = []
    drafts = ["# Draft Outlines", ""]

    for index, idea in enumerate(ideas):
        publish_date = START + timedelta(days=index * 2)
        hook = f"Most people overcomplicate {idea['idea'].lower()}."
        outline = [
            "Hook",
            "Show the manual pain",
            "Show the automation step",
            "End with a human approval reminder",
        ]
        calendar_rows.append({
            "publish_date": publish_date.isoformat(),
            "platform": idea["platform"],
            "idea": idea["idea"],
            "goal": idea["goal"],
            "status": "draft_ready",
        })
        drafts.extend([
            f"## {idea['idea']}",
            f"Audience: {idea['audience']}",
            f"Hook: {hook}",
            "Outline:",
            *[f"- {item}" for item in outline],
            "Repurpose: short post, checklist, Fiverr portfolio note",
            "",
        ])

    with (OUT / "content_calendar.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["publish_date", "platform", "idea", "goal", "status"])
        writer.writeheader()
        writer.writerows(calendar_rows)
    (OUT / "drafts.md").write_text("\n".join(drafts), encoding="utf-8")
    print("Wrote content_calendar.csv and drafts.md")


if __name__ == "__main__":
    main()
