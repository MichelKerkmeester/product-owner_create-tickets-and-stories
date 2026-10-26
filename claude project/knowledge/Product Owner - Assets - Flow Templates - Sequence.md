# Product Owner - Assets - Flow Templates - Sequence

Copy/apply patterns for a sequence model. Each pattern passes the rules, and Templates - Flow Type - Sequence holds the subset the board draws.

---

## 1. USAGE

- The participant id is what the board shows, so write `AuthServer`, never `a` with an alias
- Declare every participant in the order the board should show them
- `->>` for a request and `-->>` for its return. `-)` and `--)` only when the message really is fire-and-forget, such as telling another system an event happened, which the caller does not wait on
- A failure path is a second diagram, because `alt` renders flat

---

## 2. PATTERNS

### Request and response chain

```mermaid
sequenceDiagram
    title Sign in
    participant WebApp
    participant AuthServer
    participant UserStore
    WebApp->>AuthServer: POST /sessions
    AuthServer->>UserStore: Find user by email
    UserStore-->>AuthServer: User record
    AuthServer-->>WebApp: 201 with session token
```

### Event handoff

```mermaid
sequenceDiagram
    title Order shipped
    participant Warehouse
    participant OrderService
    participant EventBus
    participant Notifier
    Warehouse->>OrderService: Mark shipped
    OrderService-)EventBus: OrderShipped
    EventBus-)Notifier: OrderShipped
    Notifier--)OrderService: Customer notified
    OrderService-->>Warehouse: 200 OK
```
