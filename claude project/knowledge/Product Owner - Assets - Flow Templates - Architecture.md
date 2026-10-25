# Product Owner - Assets - Flow Templates - Architecture

Copy/apply patterns for an architecture model. Each pattern passes the rules, and Templates - Flow Type - Architecture holds the lanes and the allowed edges.

---

## 1. USAGE

- Keep the `%% type: architecture` line first, before any `%% title:` or other board line. On the generated fallback, pass `useArchitectureLayoutCode` as `"FIGMA_DIAGRAM_2026"` on the call
- Keep the six lane ids exactly and rename only the labels
- Drop a lane the system does not have. An empty lane is never filled with an invented part
- Label every edge from its source's side, and an external edge as `"Service: Purpose"`

---

## 2. PATTERNS

### Request path

```mermaid
%% type: architecture
flowchart LR
    subgraph client ["Apps"]
        app[Mobile App]
    end
    subgraph gateway ["Edge"]
        api[API Gateway]
    end
    subgraph service ["Services"]
        accounts[Account Service]
        search[Search Service]
    end
    subgraph datastore ["Stores"]
        users[Users DB]
        index[Search Index]
    end
    subgraph external ["Outside"]
        idp[Identity Provider]
    end
    app -->|"HTTPS"| api
    api -->|"Routes /me"| accounts
    api -->|"Routes /search"| search
    accounts -->|"Reads Users"| users
    search -->|"Queries"| index
    accounts -.->|"Identity Provider: Verifies"| idp
```

The layout draws `users` and `index` as stores because they sit in the `datastore` lane, so neither needs a cylinder.

### Event-driven path with a backward edge

```mermaid
%% type: architecture
flowchart LR
    subgraph client ["Apps"]
        web[Web App]
    end
    subgraph gateway ["Edge"]
        lb[Load Balancer]
    end
    subgraph service ["Services"]
        orders[Order Service]
        billing[Billing Service]
    end
    subgraph datastore ["Stores"]
        db[Orders DB]
    end
    subgraph async ["Events"]
        stream[Order Events]
    end
    web -->|"HTTPS"| lb
    lb -->|"Routes /orders"| orders
    orders -->|"Writes Orders"| db
    orders -.->|"Produces"| stream
    stream -.->|"Consumes"| billing
    orders <---|"Credit note"| billing
```
