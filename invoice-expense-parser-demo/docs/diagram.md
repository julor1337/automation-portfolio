# Workflow Diagram

        ```mermaid
flowchart LR
    A["Invoice text files"]
    B["regex extraction"]
    A --> B
    C["category totals"]
    B --> C
    D["monthly summary"]
    C --> D
```

        The demo is intentionally local-only. In a client project, each step can become a node in n8n, Make, Zapier, or a small Python/API service after owner approval.
