# Workflow Diagram

        ```mermaid
flowchart LR
    A["Order CSV"]
    B["status checks"]
    A --> B
    C["risk score"]
    B --> C
    D["alerts"]
    C --> D
```

        The demo is intentionally local-only. In a client project, each step can become a node in n8n, Make, Zapier, or a small Python/API service after owner approval.
