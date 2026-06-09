# Workflow Diagram

        ```mermaid
flowchart LR
    A["CRM CSV"]
    B["due-date check"]
    A --> B
    C["value sort"]
    B --> C
    D["reminder drafts"]
    C --> D
    E["weekly report"]
    D --> E
```

        The demo is intentionally local-only. In a client project, each step can become a node in n8n, Make, Zapier, or a small Python/API service after owner approval.
