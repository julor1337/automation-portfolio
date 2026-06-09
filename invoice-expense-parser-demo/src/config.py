"""Static configuration for the Invoice Expense Parser Demo demo."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_DATA_DIR = PROJECT_ROOT / "sample-data"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
LOG_DIR = PROJECT_ROOT / "logs"

INPUT_MODE = "text_dir"
INPUT_PATH = PROJECT_ROOT / "sample-data/invoices"
ITEM_ID_FIELD = "vendor"
LABEL_FIELD = "vendor"

OUTPUT_CSV = OUTPUT_DIR / "expenses_summary.csv"
OUTPUT_MARKDOWN = OUTPUT_DIR / "monthly_summary.md"
LOG_JSONL = None
MARKDOWN_TITLE = "Invoice Review Summary"
