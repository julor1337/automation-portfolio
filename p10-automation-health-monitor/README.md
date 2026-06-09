# Automation Health Monitor

## Problem
No-code and API workflows can fail quietly unless someone reviews run logs and retry priorities.

## Solution
A health monitor that reads fake workflow runs, detects failures or slowness, and builds a retry checklist.

## Workflow
`Workflow CSV -> failure detection -> latency check -> health report -> retry checklist`

## Tech Stack
- Python 3 standard library only
- CSV, JSON, text, and Markdown files
- Local demo data in `sample-data/`
- Generated output in `outputs/`

## How to Run Locally
```bash
python src/run_demo.py
```

Run `python src/run_demo.py` to create `health_report.md` and `retry_checklist.csv`.

## Demo Data Explanation
All files in `sample-data/` are synthetic examples. They are designed to show how the automation behaves before connecting any real account, store, CRM, sheet, API, or webhook.

## Security Note
This repository uses mock data only. It contains no real API keys, tokens, client records, private webhook URLs, cookies, or credentials. Use `.env.example` as a placeholder reference and keep real `.env` files local.

## What This Demonstrates for Automation Clients
- A clear end-to-end automation workflow
- Human approval before real-world actions
- Public-safe project structure for GitHub
- Practical thinking for Fiverr automation services
- Easy handoff from demo logic to n8n, Make, Zapier, Google Sheets, or API integrations
