"""Static configuration for the Webhook Debugger Starter Kit demo."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_DATA_DIR = PROJECT_ROOT / "sample-data"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
LOG_DIR = PROJECT_ROOT / "logs"

INPUT_MODE = "json_dir"
INPUT_PATH = PROJECT_ROOT / "sample-data/payloads"
ITEM_ID_FIELD = "event_id"
LABEL_FIELD = "event_type"

OUTPUT_CSV = OUTPUT_DIR / "webhook_validation_report.csv"
OUTPUT_MARKDOWN = OUTPUT_DIR / "debug_report.md"
LOG_JSONL = LOG_DIR / "event_log.jsonl"
MARKDOWN_TITLE = "Webhook Debug Report"
