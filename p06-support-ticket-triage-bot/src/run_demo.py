from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "sample-data" / "tickets.csv"
OUT = ROOT / "outputs"


def classify(message: str) -> tuple[str, str, str]:
    text = message.lower()
    if "api" in text or "webhook" in text or "500" in text:
        return "technical", "high", "yes"
    if "failed" in text or "stuck" in text:
        return "order_issue", "high", "yes"
    if "billing" in text:
        return "account", "medium", "no"
    return "general", "low", "no"


def sentiment(message: str) -> str:
    text = message.lower()
    if "thanks" in text or "fast fix" in text:
        return "positive"
    if "failed" in text or "stuck" in text or "500" in text:
        return "frustrated"
    return "neutral"


def main() -> None:
    OUT.mkdir(exist_ok=True)
    tickets = list(csv.DictReader(DATA.open(newline="", encoding="utf-8")))
    report: list[dict[str, str]] = []
    drafts = ["# Response Drafts", ""]

    for ticket in tickets:
        category, priority, escalate = classify(ticket["message"])
        mood = sentiment(ticket["message"])
        report.append({**ticket, "category": category, "priority": priority, "sentiment": mood, "escalate": escalate})
        drafts.extend([
            f"## {ticket['ticket_id']} - {ticket['customer']}",
            f"Priority: {priority}; category: {category}; human escalation: {escalate}",
            f"Draft: Hi {ticket['customer'].split()[0]}, thanks for the details. I am reviewing this as a {category.replace('_', ' ')} case and will confirm the next step before making changes to your account.",
            "",
        ])

    with (OUT / "triage_report.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(report[0].keys()))
        writer.writeheader()
        writer.writerows(report)
    (OUT / "response_drafts.md").write_text("\n".join(drafts), encoding="utf-8")
    print("Wrote triage_report.csv and response_drafts.md")


if __name__ == "__main__":
    main()
