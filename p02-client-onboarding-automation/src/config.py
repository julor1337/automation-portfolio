"""Static configuration for the Client Onboarding Automation demo."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_DATA_DIR = PROJECT_ROOT / "sample-data"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
LOG_DIR = PROJECT_ROOT / "logs"

INPUT_MODE = "csv"
INPUT_PATH = PROJECT_ROOT / "sample-data/clients.csv"
ITEM_ID_FIELD = "client_name"
LABEL_FIELD = "client_name"

OUTPUT_CSV = OUTPUT_DIR / "onboarding_report.csv"
OUTPUT_MARKDOWN = OUTPUT_DIR / "onboarding_packets.md"
LOG_JSONL = None
MARKDOWN_TITLE = "Client Onboarding Packets"
