# Support Ticket Triage Bot

## Problem
Support teams waste time reading every ticket from zero and deciding category, urgency, and first response.

## Solution
A local triage demo that classifies fake tickets, estimates priority, and drafts safe responses.

## Workflow
`Ticket CSV -> keyword classification -> priority -> draft response -> escalation flag`

## Tech Stack
- Python 3 standard library only
- CSV, JSON, text, and Markdown files
- Local demo data in `sample-data/`
- Generated output in `outputs/`

## How to Run Locally
```bash
python src/run_demo.py
```

Run `python src/run_demo.py` to create `triage_report.csv` and `response_drafts.md`.

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
