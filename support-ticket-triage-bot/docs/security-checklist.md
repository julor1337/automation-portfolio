# Security Checklist

- [x] Uses synthetic sample data only.
- [x] Does not call external APIs.
- [x] Does not send emails, messages, orders, listings, or webhooks.
- [x] Stores no real API keys, tokens, cookies, credentials, or client data.
- [x] Includes `.env.example` with placeholders only.
- [x] Ignores local `.env`, credentials, generated outputs, and logs.
- [x] Keeps human approval in the workflow before any real-world action.
