"""Static configuration for the Product Listing Generator demo."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_DATA_DIR = PROJECT_ROOT / "sample-data"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
LOG_DIR = PROJECT_ROOT / "logs"

INPUT_MODE = "csv"
INPUT_PATH = PROJECT_ROOT / "sample-data/products.csv"
ITEM_ID_FIELD = "product_name"
LABEL_FIELD = "product_name"

OUTPUT_CSV = OUTPUT_DIR / "generated_listings.csv"
OUTPUT_MARKDOWN = OUTPUT_DIR / "qa_report.md"
LOG_JSONL = None
MARKDOWN_TITLE = "Listing QA Report"
