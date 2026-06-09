# Workflow Diagram

        ```mermaid
flowchart LR
    A["Workflow CSV"]
    B["failure detection"]
    A --> B
    C["latency check"]
    B --> C
    D["health report"]
    C --> D
    E["retry checklist"]
    D --> E
```

        The demo is intentionally local-only. In a client project, each step can become a node in n8n, Make, Zapier, or a small Python/API service after owner approval.
