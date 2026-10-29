---
title: "FigJam Type - Process"
description: "A business process or decision flow drawn as a FigJam flowchart, with optional actor lanes, a status lane, detail cards, stores and data in or out, held to sk-design-diagram's process budget."
contextType: implementation
importance_tier: important
trigger_phrases:
  - "figjam process flow"
  - "decision flowchart figjam"
  - "figjam swimlane"
  - "process lanes"
  - "approval flow figjam"
version: 1.0.7.0
---

# FigJam Type - Process

A process is work that moves through steps, decisions and often several people or teams: a refund, an approval, a release, an onboarding checklist, a decision tree. It is a flowchart marked `%% type: process`, so the check holds it to process rules rather than user-flow rules.

**Loading Condition:** CONDITIONAL, when the Flow route draws a process or decision flowchart
**Purpose:** The grammar, rules, budget and read-back for a process
**Pairs With:** `assets/templates/process.md`

---

## 1. WHEN TO USE

**The reader's question:** who does what, in which order, and where does the work change hands?

- A process across teams or roles, drawn with one lane per actor
- A decision tree or a pipeline with no actors, drawn without lanes
- A process that reads from or writes to a store, or takes data in and hands data out

Use a user flow when the subject is one person's screens, a state diagram when one thing moves between named states, and a sequence when the order of messages between systems is the point.

---

## 2. WHAT THE BOARD DRAWS

```text
%% type: process
flowchart LR
```

The first line of the block names the type for the check, and the composer reads it too. A process runs `LR` or `TD`.

| Shape | Mermaid | Means |
|---|---|---|
| Stadium | `id([Label])` | Start or end |
| Rectangle | `id[Label]` | A step |
| Rhombus | `id{Label?}` | A decision |
| Circle | `id((.))` | A merge dot |
| Cylinder | `id[(Label)]` | A store, such as a database or a log table steps read and write |
| Subroutine | `id[[Label]]` | A step that is a process of its own, drawn elsewhere |
| Parallelogram | `id[/Label/]` | Data entering or leaving, such as a form or a report |

The last three come from Figma's list of shapes that render as distinct FigJam shapes, and translate sk-design-diagram's input and output chips. Every other Mermaid shape falls back to a plain rectangle or adds a meaning the reader has to learn.

A lane is a subgraph with a readable label, `subgraph agent ["CS agent"]`, holding the steps that actor performs.

**Status lane.** When the parties move one shared record through named statuses, such as an order or a commission, a laned process may give those statuses a lane of their own. `%% status: <lane id>` names it. The lane is declared first, so the board draws it on top, and holds each status as a plain node `id[Label]`, joined in order by `-->` from the first status to the last. A step that moves the record to a status draws a dotted `-.->` into that status. The status lane is never an actor lane: no work happens in it, a status never leads to a step, and its states and connectors count toward the budget.

```text
%% status: status
subgraph status ["Order status"]
    placed[Placed]
    shipped[Shipped]
end
placed --> shipped
ship -.-> shipped
```

**Detail cards.** At the `Faithful` detail level a step may carry a body under its one-line label, as `references/flow-mode.md` Section 4 sets out: `%% level: faithful` once, then one `%% detail: <step id> | <line> | <line>` line per step.

Connectors are `-->` for the flow and `-.->` for an optional or proposed step. A log write that runs today is drawn solid. A source that says every decision or every step is logged names those nodes as its writers, so the log store is drawn with one solid edge from the decision the reader most needs and the source line says the others write it too.

On the board the status lane draws each status as a white chevron, joined by the status line, and each move as a dotted gray line the key names `Moves the status`. A step with a body is a card: its label in Bold on one line, a spacer and the body left-aligned under it. On the board each lane is a band in a light tint, named after its label, stacked in the order the model declares them, and every step sits inside its lane's band. The kinds take their shapes from `references/style-guide.md` Section 2 and their colour roles from `assets/figjam-design.md`: a store is a cylinder in the `store` role, data entering or leaving a parallelogram in the `io` role and a sub-process a predefined-process shape in the `neutral` role. A process without lanes may group its steps into stages with `%% zone:` lines.

---

## 3. RULES

The check enforces:

- **The seven shapes above only**
- **Decisions have 1 to 3 labelled exits,** and a merge dot carries no words
- **Every step has a way in and a way out,** a stadium only starts or ends, and a store or a data shape needs one connector
- **`-->` or `-.->` only.** A thick connector competes with the marked step, and a headless or two-way one hides the direction work moves in
- **Lanes, when used, number 2 to 6,** never nest, each hold a step, and every step sits in one. A connector joins steps, never a lane
- **A lane takes the neutral pair** `fill:#F5F5F5,stroke:#B3B3B3` or no style at all, and never counts as the accent. The composer tints lanes itself, so a lane style changes nothing on the board
- **Without lanes, at most 9 nodes and 12 connectors. With lanes, at most 12 and 16,** sk-design-diagram's process budget and its balanced detail level. **A laned process at `Faithful` with detail cards reads at 18 and 24**, because a step's body carries what would otherwise be cut
- **A status lane, when used, is one lane,** named by one `%% status:` line, declared first, holding two or more statuses as plain `[Label]` nodes in a single `-->` chain. A step moves a status with `-.->` only, and no status leads to a step. A status move is no way out of a step, so an end may move the last status and stay an end. Every status after the first is reached by a step's move, and a status never takes the accent
- **A body only at `Faithful`.** A `%% detail:` line needs `%% level: faithful`, names a plain step `[Label]` that is no status, and holds 1 to 10 lines of 44 characters or fewer
- The shared rules: labels, quoting, ids, no emoji or markup, exactly one `style` line from `references/style-guide.md`, one direction for every process diagram in the file

Judged by hand:

- **No node returns to itself.** A connector from a node back onto the same node draws no loop a reader can follow, so a retry goes into a label or through the node it returns through, and `scripts/flow_check.py` refuses one
- **A handoff is the edge that matters most.** When the process has lanes, a connector that crosses lanes is a handoff, and the step in focus is the sending step of the handoff that adds the most delay or risk
- **One owner per step.** A step two teams share is two steps or a handoff
- **Every non-rectangle shape earns its place.** A store that only one step touches may be a label on that step instead
- **A queue between two lanes is the handoff.** A queue that only carries work from one lane to the next adds nothing the crossing connector's label cannot say, so it fails the remove test and is drawn as that label, such as `Claim queued`. It is a store only when the source treats it as a place steps read and write on their own, such as a ticket tool
- **Lanes follow the order work first reaches them,** top to bottom or left to right
- **No diagram carries the same label on four or more connectors.** Cut them all, or keep one where the label says something the shape cannot. A decision's exits are the exception, because they read the same way through the process

---

## 4. BUDGET AND SPLITTING

Over budget, cut in sk-design-diagram's degrade order and stop as soon as the diagram fits: notes and decoration first, then exact duplicates merged into one step, then steps that change nothing a reader decides, then cross-cutting steps such as logging. Still over, split into an overview, with each phase as one subroutine step, and one detail diagram per phase. When the user asked in so many words for one board, cut the next item in that order instead, name it under `Left out:` and offer the split as the alternative in the playback. Everything cut is named under `Left out:`. At `Meeting screen` distance labels drop to 32 characters. At `Wall` distance the budget drops to 6 nodes and 8 connectors, or 8 nodes and 11 connectors with lanes, with labels at 25 characters, as the reading distance dial in `references/flow-mode.md` Section 4 sets out.

---

## 5. COLOUR, ZONES AND NOTES

The composer colours every step by its kind. A user flow and a process each carry exactly one `style` line, which marks the first glance. A styled failing end or decision keeps its kind and takes the accent's outline. The goal is named by a `%% goal:` line rather than styled. A styled step is drawn in the accent's pair. The line marks meaning: on an end, in light red, it marks a failure, and on a step it puts that step in focus. Figma's guidance gives every subgraph a different tint, and sk-design-diagram keeps containers neutral so the marked step stays the strongest signal. The composer takes both: each lane gets its own tint by the zone rule in `references/style-guide.md` Section 2, pale enough that a lane reads as a container and never as a mark. Notes on a step, such as a service level or a failure rate, go on through `references/hybrid-workflow.md`.

---

## 6. WRITING THE BOARD

`scripts/compose_board.py` composes the model and one `use_figma` call draws the board, as `references/flow-mode.md` Section 6 sets out. On the generated fallback, `generate_diagram` takes `name`, `mermaidSyntax` and `userIntent`, and no `useArchitectureLayoutCode`. The `fj` route draws a process only when it has no lanes and uses only the four user-flow shapes, because `fj` has no container verb and its shape types for a store, a sub-process or data were never confirmed. Any other process needs a hosted route.

---

## 7. READ-BACK

Count nodes, connectors, labelled decision exits and lanes, and check that each step sits inside its lane's section on the board.

The lane order is compared as well, because the check counts the lanes and never reads their order. Walk the lanes in the order work first reaches them, top to bottom on `TD` and left to right on `LR`, and compare that walk with the order the model declares. A lane out of order is a mismatch, reported as measured like any other, and the order the lanes are declared in the model is what fixes it.

```text
Read-back: 11 of 11 nodes, 12 of 12 connectors, 2 of 2 decision exits labelled, 3 of 3 lanes
```

A status lane counts as a lane, and its statuses as nodes. Its order is read too: the status lane sits first, and its statuses run in the order the chain joins them. A detail card counts as one node, and its body is compared line by line with the model's `%% detail:` line.

---

## 8. PATTERNS AND EXAMPLE

- `assets/templates/process.md` holds a decision tree, a laned process and a pipeline with a store
- `assets/examples/process-fernhouse-refund.md` walks a laned refund process from a support runbook to the reply
- `assets/examples/process-fernhouse-commission.md` walks a laned process with a status lane and detail cards, a client and a maker moving one commission through its statuses
