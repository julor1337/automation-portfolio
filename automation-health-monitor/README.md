# Automation Health Monitor

Reads workflow run logs, detects failures and slow runs, then creates health reports and retry priorities.

## What The Workflow Demonstrates
- Structured intake from local sample data
- Validation and scoring rules
- Human review before real-world action
- Report generation for an operations queue
- A clean path to n8n, Make, Zapier, Google Sheets, APIs, or CRM integrations

## Project Structure
```text
src/config.py
src/models.py
src/rules.py
src/pipeline.py
src/report_writer.py
src/run_demo.py
tests/test_pipeline.py
docs/architecture.md
docs/example-output.md
docs/extension-ideas.md
sample-data/
```

## How To Run
```bash
python src/run_demo.py
```

## How To Run Tests
```bash
python -m unittest discover -s tests
```

## Demo Data
All files in `sample-data/` are synthetic. They are designed to show happy paths, review cases, and edge cases without using client data.

## Security Note
This demo does not call external APIs, send messages, publish listings, place orders, or trigger webhooks. `.env.example` contains placeholders only. Real credentials and client data should never be committed.

## Automation Mapping
Workflow run export -> failure detector -> latency check -> retry priority -> operations report.
