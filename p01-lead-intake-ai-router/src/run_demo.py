from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "sample-data" / "leads.csv"
OUT = ROOT / "outputs"
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def score_lead(row: dict[str, str]) -> tuple[int, list[str]]:
    reasons: list[str] = []
    score = 0
    budget = int(row.get("budget") or 0)
    employees = int(row.get("employees") or 0)
    source = row.get("source", "").lower()
    if budget >= 15000:
        score += 45
        reasons.append("large budget")
    elif budget >= 5000:
        score += 25
        reasons.append("medium budget")
    if employees >= 50:
        score += 30
        reasons.append("established team")
    if source in {"referral", "partner"}:
        score += 20
        reasons.append("warm source")
    elif source == "website":
        score += 10
        reasons.append("direct inbound")
    return min(score, 100), reasons


def main() -> None:
    OUT.mkdir(exist_ok=True)
    rows = list(csv.DictReader(DATA.open(newline="", encoding="utf-8")))
    report_rows: list[dict[str, str]] = []
    drafts: list[str] = ["# Follow-up Drafts", ""]

    for row in rows:
        valid_email = bool(EMAIL_RE.match(row.get("email", "")))
        score, reasons = score_lead(row)
        status = "ready_for_review" if valid_email and score >= 60 else "needs_review"
        summary = f"{row['company']} wants help with {row['need']}."
        report_rows.append({
            **row,
            "valid_email": str(valid_email),
            "score": str(score),
            "status": status,
            "summary": summary,
            "score_reasons": "; ".join(reasons),
        })
        if status == "ready_for_review":
            drafts.extend([
                f"## {row['company']}",
                f"Hi {row['name'].split()[0]},",
                "",
                f"Thanks for reaching out about {row['need'].lower()}. I can map the current intake flow, identify the fastest automation win, and prepare a small proof of concept before anything is sent or connected.",
                "",
                "Best,",
                "Automation demo owner",
                "",
            ])

    report_path = OUT / "scored_leads_report.csv"
    with report_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(report_rows[0].keys()))
        writer.writeheader()
        writer.writerows(report_rows)
    (OUT / "followup_drafts.md").write_text("\n".join(drafts), encoding="utf-8")
    print(f"Wrote {report_path}")
    print(f"Wrote {OUT / 'followup_drafts.md'}")


if __name__ == "__main__":
    main()
