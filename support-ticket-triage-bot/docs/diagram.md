# Workflow Diagram

        ```mermaid
flowchart LR
    A["Ticket CSV"]
    B["keyword classification"]
    A --> B
    C["priority"]
    B --> C
    D["draft response"]
    C --> D
    E["escalation flag"]
    D --> E
```

        The demo is intentionally local-only. In a client project, each step can become a node in n8n, Make, Zapier, or a small Python/API service after owner approval.
