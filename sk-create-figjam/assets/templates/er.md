---
title: "FigJam ER Templates"
description: "ER patterns that pass the pre-write check: a one-to-many core, a many-to-many junction and an aliased entity."
contextType: general
importance_tier: important
trigger_phrases:
  - "er templates"
  - "figjam er pattern"
version: 1.0.0.0
---

# FigJam ER Templates

Copy/apply patterns for an ER model. Each pattern passes `scripts/flow_check.py`, and `references/types/er.md` holds the rules.

**Loading Condition:** CONDITIONAL, with `references/types/er.md`
**Purpose:** Starting points for an ER diagram
**Scope:** Three patterns. The provenance table and the reply shape are in `assets/flow-templates.md`

---

## 1. USAGE

- Get the relationships and their cardinality right first, then add the 5 to 10 columns a reader needs
- Mark every `PK` and `FK`
- An alias goes on the entity block only, and relationships use the plain id

---

## 2. PATTERNS

### One-to-many core

```mermaid
erDiagram
    Account ||--o{ Project : owns
    Project ||--|{ Task : contains
    Account {
        uuid id PK
        string name
    }
    Project {
        uuid id PK
        uuid accountId FK
        string title
    }
    Task {
        uuid id PK
        uuid projectId FK
        string status "open | done"
    }
```

### Many-to-many through a junction

```mermaid
erDiagram
    Member ||--o{ Membership : holds
    Team ||--o{ Membership : includes
    Member {
        uuid id PK
        string email UK
    }
    Team {
        uuid id PK
        string name
    }
    Membership {
        uuid memberId PK, FK
        uuid teamId PK, FK
        string role
    }
```

### Aliased entity and a loose link

```mermaid
erDiagram
    Order ||--|{ OrderLine : contains
    Order }o..o| PromoCode : "applied with"
    OrderLine["Order Line"] {
        uuid id PK
        uuid orderId FK
        int quantity
    }
    Order {
        uuid id PK
        decimal total
    }
    PromoCode["Promo Code"] {
        string code PK
        decimal discount
    }
```
