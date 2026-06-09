"""Static configuration for the Support Ticket Triage Bot demo."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_DATA_DIR = PROJECT_ROOT / "sample-data"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
LOG_DIR = PROJECT_ROOT / "logs"

INPUT_MODE = "csv"
INPUT_PATH = PROJECT_ROOT / "sample-data/tickets.csv"
ITEM_ID_FIELD = "ticket_id"
LABEL_FIELD = "customer"

OUTPUT_CSV = OUTPUT_DIR / "triage_report.csv"
OUTPUT_MARKDOWN = OUTPUT_DIR / "response_drafts.md"
LOG_JSONL = None
MARKDOWN_TITLE = "Support Triage Queue"
