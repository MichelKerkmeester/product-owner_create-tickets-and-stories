---
title: "FigJam Type - State"
description: "The states of one thing and the events that move it, drawn as a FigJam state diagram with no notes or styling, labelled transitions, one level of composites and a nine-state budget."
contextType: implementation
importance_tier: important
trigger_phrases:
  - "figjam state diagram"
  - "state machine figjam"
  - "lifecycle diagram"
  - "order status flow"
version: 1.0.1.0
---

# FigJam Type - State

A state diagram shows the states one thing can be in and what moves it between them: an order, a booking, a subscription, a review. It answers the questions a Product Owner gets asked most about status fields.

**Loading Condition:** CONDITIONAL, when the Flow route draws a state diagram
**Purpose:** The grammar, rules, budget and read-back for a state diagram
**Pairs With:** `assets/templates/state.md`

---

## 1. WHEN TO USE

**The reader's question:** which states exist, what moves the thing between them, and what guards each move?

- A lifecycle such as draft, review, published and archived
- A status field whose values and allowed changes need agreeing before a story is written
- A protocol or session with explicit states

Use a process when people and steps are the subject, and a sequence when several parties exchange messages.

---

## 2. WHAT THE BOARD DRAWS

```text
stateDiagram-v2
    direction LR
    [*] --> Draft
    Draft --> Review: submit
    Review --> Draft: reject
    Review --> Published: approve
    Published --> [*]
```

- `[*]` starts and ends the machine, by the arrow's direction
- A state is a word id, or an id with a description: `Pending: Waiting for payment`, or `state "Waiting for payment" as Pending`
- A composite groups substates: `state Active { ... }`, with its own `[*]` entry and exit inside
- `state Gate <<choice>>` branches on a condition, and `<<fork>>` and `<<join>>` split and rejoin parallel paths
- `--` inside a composite splits it into regions that run at the same time

On the board the first state is light blue, a state the machine ends from light gray and every other state white. The start and end are charcoal dots, a choice is a small light yellow diamond and a fork or join a charcoal bar. Each composite is a tinted section named after it, around its substates.

---

## 3. RULES

The check enforces:

- **`stateDiagram-v2`,** never the legacy `stateDiagram`, running `LR` or `TB`, where `TD` is another name for `TB`
- **No note and no styling.** The generated fallback reads the text inside a note and the names inside a style line as new states, so its board grows phantom boxes. The composer colours states by role itself, and notes are hybrid extensions
- **Transitions written `-->`,** and the machine entered from `[*]`
- **Every transition between two states carries a label,** the event that triggers it. A move into or out of `[*]`, a fork or a join may go without
- **A choice has 2 or 3 exits,** each with a guard label
- **Composites one level deep.** A composite inside a composite is its own diagram
- **Transitions stay within their level.** Mermaid forbids a move into another composite's substate, so the move goes to or from the composite itself
- **Every state has a transition,** and state ids are camelCase or PascalCase
- **At most 9 states and 12 transitions,** and never more than twice as many moves between states as states, the `[*]` entry and exit arrows aside, which sk-design-diagram reads as two machines drawn as one
- The shared rules: labels of at most 40 characters, no emoji, markup or literal `\n`

Judged by hand:

- **States are nouns or adjectives,** such as `Confirmed`. Actions are transition labels, such as `pay`
- **Labels follow `event [guard] / action`,** dropping the parts a move does not need, in one to three words where possible
- **A move from any state, such as a timeout, is one transition from a composite,** never one from every state
- **Mark terminal states with `--> [*]`** only when the thing really ends

---

## 4. BUDGET AND SPLITTING

Over budget, split by phase, such as booking and stay, or by entity. A coarse machine with one composite per phase plus one diagram per composite reads better than one deep machine. At `Meeting screen` distance transition labels drop to 32 characters. At `Wall` distance the budget drops to 6 states and 8 transitions, with labels at 25 characters, as the reading distance dial in `references/flow-mode.md` Section 4 sets out.

---

## 5. COLOUR, ZONES AND NOTES

None in the model. The composer colours the first and final states and the pseudo-states by role, and composites are the zones. A grouping the model does not hold, such as every error state, is a composite when the states share a way out, and otherwise a note. A self-transition can render tight against its state, so tell the user they can drag its loop in FigJam if it crowds. A `%% focus: <id>` line may name the one node the first glance lands on. It is a comment, so the model stays styleless.

---

## 6. WRITING THE BOARD

`scripts/compose_board.py` composes the model and one `use_figma` call draws the board, as `references/flow-mode.md` Section 6 sets out. On the generated fallback, `generate_diagram` takes `name`, `mermaidSyntax` and `userIntent`, and no `useArchitectureLayoutCode`. The `fj` route cannot draw a state diagram.

---

## 7. READ-BACK

Count states, transitions and labelled transitions, and check every guard on a choice. A composite draws as the section around its substates, so it counts as a state by its section name.

```text
Read-back: 6 of 6 states, 8 of 8 transitions, 6 of 6 transitions labelled
```

---

## 8. PATTERNS AND EXAMPLE

- `assets/templates/state.md` holds a lifecycle, a composite and a choice
- `assets/examples/state-roamstay-booking.md` draws a booking's status field from a product doc
