---
title: "FigJam State Templates"
description: "State patterns that pass the pre-write check: a lifecycle, a composite with its own entry and a guarded choice."
contextType: general
importance_tier: important
trigger_phrases:
  - "state templates"
  - "figjam state pattern"
version: 1.0.0.0
---

# FigJam State Templates

Copy/apply patterns for a state model. Each pattern passes `scripts/flow_check.py`, and `references/types/state.md` holds the rules.

**Loading Condition:** CONDITIONAL, with `references/types/state.md`
**Purpose:** Starting points for a state diagram
**Scope:** Three patterns. The provenance table and the reply shape are in `assets/flow-templates.md`

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
