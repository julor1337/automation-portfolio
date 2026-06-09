"""Static configuration for the Automation Health Monitor demo."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_DATA_DIR = PROJECT_ROOT / "sample-data"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
LOG_DIR = PROJECT_ROOT / "logs"

INPUT_MODE = "csv"
INPUT_PATH = PROJECT_ROOT / "sample-data/workflow_runs.csv"
ITEM_ID_FIELD = "run_id"
LABEL_FIELD = "workflow"

OUTPUT_CSV = OUTPUT_DIR / "retry_checklist.csv"
OUTPUT_MARKDOWN = OUTPUT_DIR / "health_report.md"
LOG_JSONL = None
MARKDOWN_TITLE = "Automation Health Report"
