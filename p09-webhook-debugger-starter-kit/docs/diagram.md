# Workflow Diagram

        ```mermaid
flowchart LR
    A["Sample payload JSON"]
    B["schema validation"]
    A --> B
    C["route handler"]
    B --> C
    D["JSONL log"]
    C --> D
    E["debug report"]
    D --> E
```

        The demo is intentionally local-only. In a client project, each step can become a node in n8n, Make, Zapier, or a small Python/API service after owner approval.
