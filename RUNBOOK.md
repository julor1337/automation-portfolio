# Portfolio Runbook

## What is here
This folder contains 10 GitHub-safe automation portfolio projects. Each project has its own folder, README, sample data, Python demo, security checklist, and placeholder `.env.example`.

## Project folders
- `p01-lead-intake-ai-router`
- `p02-client-onboarding-automation`
- `p03-ecommerce-order-tracker`
- `p04-invoice-expense-parser-demo`
- `p05-content-pipeline-automation`
- `p06-support-ticket-triage-bot`
- `p07-crm-follow-up-reminder-system`
- `p08-product-listing-generator`
- `p09-webhook-debugger-starter-kit`
- `p10-automation-health-monitor`

## Agent prompts
Prompts for the Hermes Portfolio Team are stored in:

`/home/julor/projects/ai-business/agent-prompts/portfolio-team`

## Verification
The verifier runs every demo, checks required files, scans for common secret patterns, and confirms ASCII text:

```bash
python3 "/mnt/c/Users/julor/Documents/New project/verify_portfolio_projects.py"
```

Expected result:

`All portfolio projects passed structure, demo, secret, and ASCII checks.`

## Hermes note
The safe non-interactive command format is:

```bash
/home/julor/.local/bin/hermes -p portfolio chat -Q -q "your prompt"
```

A local Cerebras compatibility patch removes unsupported `reasoning_content` replay fields. If a run stops with `Tokens per minute limit exceeded`, wait a few minutes and retry one project at a time.

## GitHub safety
Before publishing, run the verifier again. Do not commit real `.env` files, API keys, client data, private webhook URLs, cookies, or credentials.
