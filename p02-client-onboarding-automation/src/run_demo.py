from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
DATA = ROOT / "sample-data" / "clients.csv"


TASK_TEMPLATE = [
    ("Collect source examples", "owner"),
    ("Confirm success metric", "owner"),
    ("Map current manual process", "delivery"),
    ("Build demo workflow", "delivery"),
    ("Review before connecting live accounts", "owner"),
]


def slugify(value: str) -> str:
    return "".join(ch.lower() if ch.isalnum() else "-" for ch in value).strip("-")


def main() -> None:
    OUT.mkdir(exist_ok=True)
    clients = list(csv.DictReader(DATA.open(newline="", encoding="utf-8")))
    packets: list[str] = ["# Onboarding Packets", ""]
    folder_plan: list[str] = ["# Folder Plan", ""]
    task_rows: list[dict[str, str]] = []

    for client in clients:
        slug = slugify(client["client_name"])
        packets.extend([
            f"## {client['client_name']}",
            f"Service: {client['service']}",
            f"Goal: {client['goal']}",
            f"Kickoff date: {client['start_date']}",
            "",
            "Welcome draft:",
            f"Hi, thanks for booking the {client['service']} project. Before I connect anything live, I will build a mock workflow, show the expected output, and ask for approval.",
            "",
        ])
        folder_plan.extend([
            f"## {client['client_name']}",
            f"- clients/{slug}/01-intake",
            f"- clients/{slug}/02-demo-workflow",
            f"- clients/{slug}/03-review",
            f"- clients/{slug}/04-handoff",
            "",
        ])
        for index, (task, owner) in enumerate(TASK_TEMPLATE, start=1):
            task_rows.append({
                "client": client["client_name"],
                "task_id": f"{slug}-{index:02d}",
                "task": task,
                "owner": owner,
                "status": "todo",
            })

    (OUT / "onboarding_packets.md").write_text("\n".join(packets), encoding="utf-8")
    (OUT / "folder_plan.md").write_text("\n".join(folder_plan), encoding="utf-8")
    with (OUT / "task_list.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["client", "task_id", "task", "owner", "status"])
        writer.writeheader()
        writer.writerows(task_rows)
    print("Wrote onboarding packets, folder plan, and task list")


if __name__ == "__main__":
    main()
