"""Static configuration for the CRM Follow-up Reminder System demo."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_DATA_DIR = PROJECT_ROOT / "sample-data"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
LOG_DIR = PROJECT_ROOT / "logs"

INPUT_MODE = "csv"
INPUT_PATH = PROJECT_ROOT / "sample-data/crm_contacts.csv"
ITEM_ID_FIELD = "company"
LABEL_FIELD = "company"

OUTPUT_CSV = OUTPUT_DIR / "followups_due.csv"
OUTPUT_MARKDOWN = OUTPUT_DIR / "reminder_drafts.md"
LOG_JSONL = None
MARKDOWN_TITLE = "CRM Follow-up Review"
