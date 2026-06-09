# Example Output

Running:

```bash
python src/run_demo.py
```

creates:

- `outputs/scored_leads_report.csv`
- `outputs/followup_drafts.md`

Each row includes:

- item ID
- label
- score
- status
- flags
- recommended human actions
- short summary

The generated files are ignored by git so the public repository stays clean.
