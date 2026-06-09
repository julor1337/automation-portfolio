# Workflow Diagram

        ```mermaid
flowchart LR
    A["Client CSV"]
    B["checklist"]
    A --> B
    C["task CSV"]
    B --> C
    D["folder plan"]
    C --> D
    E["welcome draft"]
    D --> E
```

        The demo is intentionally local-only. In a client project, each step can become a node in n8n, Make, Zapier, or a small Python/API service after owner approval.
