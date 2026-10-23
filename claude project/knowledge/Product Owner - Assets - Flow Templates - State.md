# Product Owner - Assets - Flow Templates - State

Copy/apply patterns for a state model. Each pattern passes the rules, and Templates - Flow Type - State holds the rules.

---

## 1. USAGE

- States are nouns or adjectives and labels are the events that move between them
- A long state name goes in a description, `Pending: Waiting for payment`, so the id stays one word
- No note and no style line, which would grow phantom states on the board

---

## 2. PATTERNS

### Lifecycle

```mermaid
stateDiagram-v2
    direction LR
    [*] --> Draft
    Draft --> InReview: submit
    InReview --> Draft: request changes
    InReview --> Published: approve
    Published --> Archived: archive
    Archived --> [*]
```

### Composite with its own entry

```mermaid
stateDiagram-v2
    direction LR
    [*] --> Trial
    Trial --> Active: subscribe
    state Active {
        [*] --> Paid
        Paid --> PastDue: payment fails
        PastDue --> Paid: payment succeeds
    }
    Active --> Cancelled: cancel
    Trial --> Cancelled: trial ends
    Cancelled --> [*]
```

### Guarded choice

```mermaid
stateDiagram-v2
    direction TB
    [*] --> Submitted
    state Screen <<choice>>
    Submitted --> Screen: screen
    Screen --> Approved: score above 80
    Screen --> ManualReview: score 50 to 80
    Screen --> Rejected: score below 50
    ManualReview --> Approved: approve
    ManualReview --> Rejected: reject
    Approved --> [*]
    Rejected --> [*]
```
