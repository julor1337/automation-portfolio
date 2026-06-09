# Workflow Diagram

        ```mermaid
flowchart LR
    A["CSV lead intake"]
    B["validation"]
    A --> B
    C["scoring"]
    B --> C
    D["summary"]
    C --> D
    E["human-reviewed draft"]
    D --> E
```

        The demo is intentionally local-only. In a client project, each step can become a node in n8n, Make, Zapier, or a small Python/API service after owner approval.
