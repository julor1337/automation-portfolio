from __future__ import annotations

import csv
from datetime import date, datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
DATA = ROOT / "sample-data" / "orders.csv"
DEMO_TODAY = date(2026, 6, 9)


def parse_date(value: str) -> date | None:
    return datetime.strptime(value, "%Y-%m-%d").date() if value else None


def main() -> None:
    OUT.mkdir(exist_ok=True)
    orders = list(csv.DictReader(DATA.open(newline="", encoding="utf-8")))
    report: list[dict[str, str]] = []
    alerts = ["# Order Alerts", ""]

    for order in orders:
        promised = parse_date(order["promised_ship_date"])
        shipped = parse_date(order["ship_date"])
        days_late = 0 if shipped or not promised else max((DEMO_TODAY - promised).days, 0)
        risk = "low"
        action = "monitor"
        if order["status"] == "exception":
            risk = "high"
            action = "manual review required"
        elif days_late > 0:
            risk = "high" if days_late >= 2 else "medium"
            action = "prepare customer update draft"
        elif order["status"] == "paid":
            risk = "medium"
            action = "confirm fulfillment queue"
        report.append({**order, "days_late": str(days_late), "risk": risk, "next_action": action})
        if risk in {"high", "medium"}:
            alerts.append(f"- {order['order_id']} ({order['channel']}): {risk} risk, {action}.")

    with (OUT / "order_status_report.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(report[0].keys()))
        writer.writeheader()
        writer.writerows(report)
    (OUT / "alerts.md").write_text("\n".join(alerts) + "\n", encoding="utf-8")
    print("Wrote order_status_report.csv and alerts.md")


if __name__ == "__main__":
    main()
