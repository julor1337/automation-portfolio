from __future__ import annotations

import csv
from datetime import date, datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "sample-data" / "crm_contacts.csv"
OUT = ROOT / "outputs"
TODAY = date(2026, 6, 9)


def main() -> None:
    OUT.mkdir(exist_ok=True)
    contacts = list(csv.DictReader(DATA.open(newline="", encoding="utf-8")))
    due: list[dict[str, str]] = []
    drafts = ["# Reminder Drafts", "", "These are drafts only. Nothing is sent automatically.", ""]

    for contact in contacts:
        due_date = datetime.strptime(contact["due_date"], "%Y-%m-%d").date()
        if due_date <= TODAY and contact["status"] in {"warm", "pending"}:
            days_overdue = (TODAY - due_date).days
            row = {**contact, "days_overdue": str(days_overdue), "review_required": "yes"}
            due.append(row)
            drafts.extend([
                f"## {contact['company']}",
                f"Contact: {contact['contact']}",
                f"Draft: Hi {contact['contact']}, quick follow-up on {contact['next_step'].lower()}. I can prepare a small mock workflow first so you can review it before anything goes live.",
                "",
            ])

    due.sort(key=lambda row: int(row["value"]), reverse=True)
    with (OUT / "followups_due.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["contact", "company", "last_contact", "next_step", "due_date", "value", "status", "days_overdue", "review_required"])
        writer.writeheader()
        writer.writerows(due)
    (OUT / "reminder_drafts.md").write_text("\n".join(drafts), encoding="utf-8")
    print("Wrote followups_due.csv and reminder_drafts.md")


if __name__ == "__main__":
    main()
