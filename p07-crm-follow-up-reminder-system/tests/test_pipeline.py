"""Regression tests for the local workflow demo."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC = PROJECT_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from config import OUTPUT_CSV, OUTPUT_MARKDOWN
from pipeline import load_records, process_records, run_pipeline


class WorkflowTests(unittest.TestCase):
    def test_load_records(self) -> None:
        records = load_records()
        self.assertGreaterEqual(len(records), 3)

    def test_process_records(self) -> None:
        items = process_records(load_records())
        self.assertTrue(all(item.item_id for item in items))
        self.assertTrue(all(0 <= item.evaluation.score <= 100 for item in items))
        self.assertTrue(any(item.evaluation.actions for item in items))

    def test_run_pipeline_writes_outputs(self) -> None:
        run_pipeline()
        self.assertTrue(OUTPUT_CSV.exists())
        self.assertTrue(OUTPUT_MARKDOWN.exists())


if __name__ == "__main__":
    unittest.main()
