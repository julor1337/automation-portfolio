"""Static configuration for the E-commerce Order Tracker demo."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_DATA_DIR = PROJECT_ROOT / "sample-data"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
LOG_DIR = PROJECT_ROOT / "logs"

INPUT_MODE = "csv"
INPUT_PATH = PROJECT_ROOT / "sample-data/orders.csv"
ITEM_ID_FIELD = "order_id"
LABEL_FIELD = "customer"

OUTPUT_CSV = OUTPUT_DIR / "order_status_report.csv"
OUTPUT_MARKDOWN = OUTPUT_DIR / "alerts.md"
LOG_JSONL = None
MARKDOWN_TITLE = "Operations Alerts"
