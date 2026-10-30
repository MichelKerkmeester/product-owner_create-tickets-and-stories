---
title: "FigJam Type - User Flow"
description: "A person's path through a product composed as a FigJam board: four shapes, labelled exits, colour by kind, optional zones and a nine-node budget."
contextType: implementation
importance_tier: important
trigger_phrases:
  - "figjam user flow"
  - "user flow rules"
  - "screen flow figjam"
  - "merge dot"
version: 1.0.5.0
---

# FigJam Type - User Flow

A user flow is the screens and choices one person passes through to reach a goal. It is the default Flow type and the strictest, because it is drawn from screenshots and frames a reader will compare node by node.

**Loading Condition:** CONDITIONAL, when the Flow route draws a user flow
**Purpose:** The grammar, rules, budget and read-back for a user flow
**Pairs With:** `assets/flow-templates.md`

---

## 1. WHEN TO USE

**The reader's question:** which screens does a person pass through, and where do they choose?

- A flow drawn from screenshots, from Figma frames or from a product doc that walks one person through the product
- A platform split, such as desktop and mobile, that rejoins on a later screen
- A journey, which Flow Mode does not draw as such, redrawn as the screens it visits

Use another type when several people or teams hand work to each other (a process), when the subject is services and stores (an architecture) or when time order between systems is the point (a sequence).

---

## 2. WHAT THE BOARD DRAWS

`flowchart LR` or `flowchart TD`, composed into a board as Section 6 sets out. No `%% type:` line is needed, because a flowchart with none is a user flow.

| Shape | Mermaid | Means |
|---|---|---|
| Stadium | `id([Label])` | The flow starts or ends here |
| Rectangle | `id[Label]` | A screen or an action |
| Rhombus | `id{Label?}` | A choice, written as a question |
| Circle | `id((.))` | A merge dot, where branches rejoin, with no words |

Every connector is a solid one-way arrow, `-->`, with an optional label: `a -->|Yes| b`.

On the board the first screen takes the `entry` role, every other screen the `neutral` role, a decision a diamond in the `decision` role, the goal the `goal` role and every other end the `exit` role, beside the main line rather than on it, and `assets/figjam-design.md` names the swatch each role draws. The main route from the first screen to the goal runs on one straight line, and `%% zone:` lines group the screens into named stages, as `assets/flow-templates.md` Section 1 sets out.

Every move carries an actor in the model, one of a person, a system or a timer. A system step is marked automatic and a timer step is fired by time, so neither is ever counted as a missing user action.

---

## 3. RULES

The check enforces:

- **Four shapes only.** No other shape, no subgraph and never a colour per type. A `%% zone:` line does the grouping instead
- **A decision has 1 to 3 exits, each labelled.** A fourth outcome means the decision is two decisions
- **Every node connected, every step with a way in and a way out.** Only a stadium starts or ends the flow, and a stadium never sits mid-flow. The first node may take a loop back to it
- **A merge dot carries no words**
- **Solid one-way arrows only.** A dotted, thick, headless or two-way connector would carry a second meaning. A proposal's status goes in its label, and a `%% goal:` line names the goal
- **Left to right or top to bottom,** the same way for every diagram of one flow. Left to right is the default, because the composer keeps the main route on one straight line across a board that reads wider than tall and sets each branch beside it. Top to bottom suits a short flow
- **Labels of at most 40 characters on one line,** in double quotes when they hold a parenthesis, a colon or a slash
- **camelCase ids,** never an underscore or a reserved word such as `end`
- **No emoji, markup or literal `\n`** anywhere in the block but a `%%` comment
- **At most 9 nodes,** and exactly one `style` line from `references/style-guide.md`

Judged by hand:

- **No node returns to itself.** A connector from a node back onto the same node draws no loop a reader can follow, so a retry goes into a label or through the node it returns through, and `scripts/flow_check.py` refuses one
- **Labels name the screen or the action in the product's own words,** one to four words where those words allow
- **A decision label is a question and each exit one of its answers**
- **Exits read the same way across the flow,** such as Yes to the right and No below, so a reader learns the pattern once
- **The shape carries the type, so the label does not repeat it.** Write `valid{Card valid?}`, never `valid{Decision: card valid?}`
- **A state is a screen in another condition, and no fifth shape carries it.** A state earns its own node only when a different action reaches it or a reader can be trapped in it, and otherwise the condition goes in the screen's label and under `Left out:`

---

## 4. BUDGET AND SPLITTING

Nine nodes is sk-design-diagram's general budget and matches what a hand-drawn user flow uses. A longer flow splits into diagrams that hand off through a named end and a start with the same label, all in one file. When the user asked in so many words for one board, cut the lowest-priority part instead, name it under `Left out:` and offer the split as the alternative in the playback. Every source step lands in one diagram or under `Left out:`, never dropped silently. At `Meeting screen` distance labels drop to 32 characters. At `Wall` distance the budget drops to 6 nodes, with labels at 25 characters, as the reading distance dial in `references/flow-mode.md` Section 4 sets out.

---

## 5. COLOUR, ZONES AND NOTES

The composer colours every screen by its kind. A user flow and a process each carry exactly one `style` line, which marks the first glance. A styled failing end or decision keeps its kind and takes the accent's outline. The goal is named by a `%% goal:` line rather than styled. A styled step is drawn in the accent's pair. The line marks meaning: on an end, in the light red pair, it marks a failure, and on a screen it puts that screen in focus, as `references/style-guide.md` Section 3 sets out. Zones are `%% zone:` lines in flow order, and once a flow has zones every screen sits in one. Each zone takes a `%% about:` line with up to three notes under its title, `Starts:`, `Ends:` and `Good to know:` where the source holds them, so the reader learns where the stage begins and ends without tracing it. The styled screen or decision takes `%% focus: <id> because <reason>`, which the key draws as `In focus: <reason>`. At `Balanced` and `Faithful` a screen may carry a body of up to 4 or 10 lines, `%% detail: <id> | <line> | <line>`, for what the source says the screen holds, such as the reasons a picker offers. A note on a screen, such as a drop-off rate, goes on through the pins and legend recipe in `references/hybrid-workflow.md`.

---

## 6. WRITING THE BOARD

`scripts/compose_board.py` composes the model and one `use_figma` call draws the board, as `references/flow-mode.md` Section 6 sets out. On the generated fallback, `generate_diagram` takes `name`, `mermaidSyntax` and `userIntent`, with `name` set to the flow and its hand-off and no `useArchitectureLayoutCode`. The `fj` route can also draw a user flow when neither hosted tool is connected.

---

## 7. READ-BACK

Count on the board, against the model: nodes, connectors, decision exits labelled, every node label, and for each model connector a board connector joining the same two nodes in the same direction with the same label, following a routed edge through its legs as `references/flow-mode.md` Section 7 sets out. When the flow has zones, each screen sits in its zone.

```text
Read-back: 8 of 8 nodes, 8 of 8 connectors, 2 of 2 decision exits labelled
```

---

## 8. PATTERNS AND EXAMPLE

- `assets/flow-templates.md` holds five user-flow patterns that pass the check
- `assets/examples/user-flow-fernhouse-return.md` walks one flow from screenshots to the reply
