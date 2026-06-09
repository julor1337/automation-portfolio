from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "sample-data" / "payloads"
OUT = ROOT / "outputs"
LOGS = ROOT / "logs"
REQUIRED = {"event_id", "event_type", "source", "payload"}


def validate(event: dict) -> list[str]:
    errors = [f"missing {field}" for field in sorted(REQUIRED - set(event))]
    if event.get("event_type") not in {"order.created", "lead.created"}:
        errors.append("unsupported event_type")
    if not isinstance(event.get("payload", {}), dict):
        errors.append("payload must be an object")
    return errors


def main() -> None:
    OUT.mkdir(exist_ok=True)
    LOGS.mkdir(exist_ok=True)
    log_path = LOGS / "event_log.jsonl"
    report = ["# Debug Report", ""]
    with log_path.open("w", encoding="utf-8") as log:
        for path in sorted(DATA.glob("*.json")):
            event = json.loads(path.read_text(encoding="utf-8"))
            errors = validate(event)
            status = "accepted" if not errors else "rejected"
            entry = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "file": path.name,
                "status": status,
                "event_type": event.get("event_type", "missing"),
                "errors": errors,
            }
            log.write(json.dumps(entry, sort_keys=True) + "\n")
            report.append(f"- {path.name}: {status}" + (f" ({'; '.join(errors)})" if errors else ""))
    (OUT / "debug_report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print("Wrote logs/event_log.jsonl and outputs/debug_report.md")


if __name__ == "__main__":
    main()
