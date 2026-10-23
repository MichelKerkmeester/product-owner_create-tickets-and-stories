# Product Owner - Templates - Flow Type - User Flow

A user flow is the screens and choices one person passes through to reach a goal. It is the default Flow type and the strictest, because it is drawn from screenshots and frames a reader will compare node by node.

---

## 1. WHEN TO USE

**The reader's question:** which screens does a person pass through, and where do they choose?

- A flow drawn from screenshots, from Figma frames or from a product doc that walks one person through the product
- A platform split, such as desktop and mobile, that rejoins on a later screen
- A journey Figma's generator cannot draw as a journey, redrawn as the screens it visits

Use another type when several people or teams hand work to each other (a process), when the subject is services and stores (an architecture) or when time order between systems is the point (a sequence).

---

## 2. WHAT THE BOARD DRAWS

`flowchart TD` or `flowchart LR`, laid out by the generator's ELK engine. No `%% type:` line is needed, because a flowchart with none is a user flow.

| Shape | Mermaid | Means |
|---|---|---|
| Stadium | `id([Label])` | The flow starts or ends here |
| Rectangle | `id[Label]` | A screen or an action |
| Rhombus | `id{Label?}` | A choice, written as a question |
| Circle | `id((.))` | A merge dot, where branches rejoin, with no words |

Every connector is a solid one-way arrow, `-->`, with an optional label: `a -->|Yes| b`.

Every move carries an actor in the model, one of a person, a system or a timer. A system step is marked automatic and a timer step is fired by time, so neither is ever counted as a missing user action.

---

## 3. RULES

Check these rule by rule before the gate:

- **Four shapes only.** No other shape, no subgraph and never a colour per type
- **A decision has 1 to 3 exits, each labelled.** A fourth outcome means the decision is two decisions
- **Every node connected, every step with a way in and a way out.** Only a stadium starts or ends the flow, and a stadium never sits mid-flow. The first node may take a loop back to it
- **A merge dot carries no words**
- **Solid one-way arrows only.** A dotted, thick, headless or two-way connector would carry a second meaning. A proposal's status goes in its label, and the accent marks the happy path
- **Top to bottom or left to right,** the same way for every diagram of one flow. Top to bottom is the default, because a user flow fans out at its decisions and platform splits. Left to right suits a short sequential flow
- **Labels of at most 40 characters on one line,** in double quotes when they hold a parenthesis, a colon or a slash
- **camelCase ids,** never an underscore or a reserved word such as `end`
- **No emoji, markup or literal `\n`** anywhere in the block but a `%%` comment
- **At most 9 nodes,** and at most one accent from Rules - Flow Style Guide

Judged by hand:

- **Labels name the screen or the action in the product's own words,** one to four words where those words allow
- **A decision label is a question and each exit one of its answers**
- **Exits read the same way across the flow,** such as Yes to the right and No below, so a reader learns the pattern once
- **The shape carries the type, so the label does not repeat it.** Write `valid{Card valid?}`, never `valid{Decision: card valid?}`
- **A state is a screen in another condition, and no fifth shape carries it.** A state earns its own node only when a different action reaches it or a reader can be trapped in it, and otherwise the condition goes in the screen's label and under `Left out:`

---

## 4. BUDGET AND SPLITTING

Nine nodes is the house diagram guide's general budget and matches what a hand-drawn user flow uses. A longer flow splits into diagrams that hand off through a named end and a start with the same label, all in one file. Every source step lands in one diagram or under `Left out:`, never dropped silently. At `Meeting screen` distance labels drop to 32 characters. At `Wall` distance the budget drops to 6 nodes, with labels at 25 characters, as the reading distance dial in Templates - Flow Mode Section 4 sets out.

---

## 5. COLOUR AND THE HYBRID PASS

One accent at most, set in the model: a fill with its paired stroke on the focal node, or the paired stroke on the happy-path connectors. A note on a screen, such as a drop-off rate, goes on through the label and legend recipe in Templates - Flow Hybrid Workflow.

---

## 6. CALLING THE TOOL

`generate_diagram` with `name` set to the flow and its hand-off, `mermaidSyntax` set to the block and `userIntent` set to one sentence on the reader's question. No `useArchitectureLayoutCode`.

---

## 7. READ-BACK

Count on the board, against the model: nodes, connectors, decision exits labelled, every node label, and for each model connector a board connector joining the same two nodes in the same direction with the same label.

```text
Read-back: 8 of 8 nodes, 8 of 8 connectors, 2 of 2 decision exits labelled
```

---

## 8. PATTERNS AND EXAMPLE

- Assets - Flow Templates holds five user-flow patterns that pass these rules
- Examples - Flow - User Flow walks one flow from screenshots to the reply
