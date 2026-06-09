# Lead Intake AI Router

## Problem
Small B2B teams often receive leads from forms, spreadsheets, and webhooks, then manually decide which ones deserve fast follow-up.

## Solution
A local workflow that validates fake leads, scores them, creates an AI-style summary, and drafts follow-up text for human review.

## Workflow
`CSV lead intake -> validation -> scoring -> summary -> human-reviewed draft`

## Tech Stack
- Python 3 standard library only
- CSV, JSON, text, and Markdown files
- Local demo data in `sample-data/`
- Generated output in `outputs/`

## How to Run Locally
```bash
python src/run_demo.py
```

Run `python src/run_demo.py` to create `outputs/scored_leads_report.csv` and `outputs/followup_drafts.md`.

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
