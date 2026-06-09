from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "sample-data" / "invoices"
OUT = ROOT / "outputs"
FIELD_RE = re.compile(r"^(Vendor|Date|Amount|Category|Description):\s*(.+)$", re.MULTILINE)


def parse_invoice(path: Path) -> dict[str, str]:
    values = {key.lower(): value.strip() for key, value in FIELD_RE.findall(path.read_text(encoding="utf-8"))}
    values["file"] = path.name
    return values


def main() -> None:
    OUT.mkdir(exist_ok=True)
    rows = [parse_invoice(path) for path in sorted(DATA.glob("*.txt"))]
    totals: dict[str, float] = defaultdict(float)
    monthly: dict[str, float] = defaultdict(float)
    for row in rows:
        amount = float(row["amount"])
        totals[row["category"]] += amount
        monthly[row["date"][:7]] += amount

    with (OUT / "expenses_summary.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["file", "vendor", "date", "amount", "category", "description"])
        writer.writeheader()
        writer.writerows(rows)

    lines = ["# Monthly Summary", "", "## By month"]
    lines.extend(f"- {month}: ${amount:.2f}" for month, amount in sorted(monthly.items()))
    lines.extend(["", "## By category"])
    lines.extend(f"- {category}: ${amount:.2f}" for category, amount in sorted(totals.items()))
    (OUT / "monthly_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Wrote expenses_summary.csv and monthly_summary.md")


if __name__ == "__main__":
    main()
