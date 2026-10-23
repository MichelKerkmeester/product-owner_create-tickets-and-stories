# Product Owner - Assets - Flow Templates - ER

Copy/apply patterns for an ER model. Each pattern passes the rules, and Templates - Flow Type - ER holds the rules.

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
