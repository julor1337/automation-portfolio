"""Static configuration for the Lead Intake AI Router demo."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_DATA_DIR = PROJECT_ROOT / "sample-data"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
LOG_DIR = PROJECT_ROOT / "logs"

INPUT_MODE = "csv"
INPUT_PATH = PROJECT_ROOT / "sample-data/leads.csv"
ITEM_ID_FIELD = "email"
LABEL_FIELD = "company"

OUTPUT_CSV = OUTPUT_DIR / "scored_leads_report.csv"
OUTPUT_MARKDOWN = OUTPUT_DIR / "followup_drafts.md"
LOG_JSONL = None
MARKDOWN_TITLE = "Lead Review Queue"
