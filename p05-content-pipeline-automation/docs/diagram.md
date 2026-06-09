# Workflow Diagram

        ```mermaid
flowchart LR
    A["Idea CSV"]
    B["priority sort"]
    A --> B
    C["calendar"]
    B --> C
    D["draft outline"]
    C --> D
    E["reuse checklist"]
    D --> E
```

        The demo is intentionally local-only. In a client project, each step can become a node in n8n, Make, Zapier, or a small Python/API service after owner approval.
