# Example Output

Running:

```bash
python src/run_demo.py
```

creates:

- `outputs/triage_report.csv`
- `outputs/response_drafts.md`

Each row includes:

- item ID
- label
- score
- status
- flags
- recommended human actions
- short summary

The generated files are ignored by git so the public repository stays clean.
