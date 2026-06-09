"""Static configuration for the Content Pipeline Automation demo."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_DATA_DIR = PROJECT_ROOT / "sample-data"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
LOG_DIR = PROJECT_ROOT / "logs"

INPUT_MODE = "csv"
INPUT_PATH = PROJECT_ROOT / "sample-data/content_ideas.csv"
ITEM_ID_FIELD = "idea"
LABEL_FIELD = "idea"

OUTPUT_CSV = OUTPUT_DIR / "content_calendar.csv"
OUTPUT_MARKDOWN = OUTPUT_DIR / "drafts.md"
LOG_JSONL = None
MARKDOWN_TITLE = "Content Draft Queue"
