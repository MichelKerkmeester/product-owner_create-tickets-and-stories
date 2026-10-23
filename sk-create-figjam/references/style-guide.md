---
title: "FigJam Diagram Style Guide"
description: "The colour roles, palette pairs, emphasis rules and measured contrast record every FigJam diagram draws from, translated from sk-design-diagram's style guide and derivation record."
contextType: implementation
importance_tier: important
trigger_phrases:
  - "figjam style guide"
  - "figjam palette"
  - "figjam accent colour"
  - "palette derivation record"
  - "figjam contrast"
version: 1.0.0.0
---

# FigJam Diagram Style Guide

The one source for colour and spacing on a FigJam diagram. Every hex a model or a hybrid extension uses comes from the tables below, and `scripts/flow_check.py` refuses any other.

**Loading Condition:** CONDITIONAL, when a model or a hybrid extension uses colour
**Purpose:** Names the colour roles, the palette pairs, the emphasis rules and the measured contrast record
**Scope:** Mermaid `style`, `classDef` and `linkStyle` colours, hybrid sticky, label and section colours, and the contrast record the self-test re-measures

---

## 1. OVERVIEW

sk-design-diagram owns a skinnable palette with semantic roles and a record of where each value comes from. A FigJam board already has a palette of its own, and a colour the board recognises as a palette swatch can be recoloured from FigJam's colour picker by anyone on the board. So this guide does not skin the board. It picks FigJam's own pairs, gives each a role and records what each pair measures.

Three rules carry over from sk-design-diagram unchanged:

- **Restraint first.** Most diagrams need no colour at all. Shape and label carry the meaning, and colour only points at what is focal
- **One accent.** The accent marks the one node the diagram exists to explain, never a category scheme and never a position in the layout. Where two nodes tie for it, the diagram splits. A fill and the darker stroke FigJam pairs with it are one accent
- **Colour never carries meaning alone.** A reader who cannot tell the colours apart still reads the diagram from its shapes and labels, which is why a stroke may sit under the mark gate below

---

## 2. ROLES

| Role | What it marks | Where it is set |
|---|---|---|
| Accent | The one focal element or path | Mermaid `style` or `linkStyle` on a user flow or a process |
| Lane | A process lane, which is a container and never content | Mermaid `style <lane>` on a process |
| Status tint | Terminal, active or error states, or entity domains | Hybrid extension on a state, ER or sequence diagram, where Mermaid styling is stripped. The pair's light fill with a dashed stroke |
| Sticky | One idea a reader added, such as a note on a step | Hybrid extension |
| Label | A numbered pin that points from a node to a legend sticky | Hybrid extension |
| Text | Every label the generator or an extension writes | Charcoal `#1E1E1E`, FigJam's default |

An architecture takes no colour from the model. Its layout colours each lane by itself, and the check refuses styling there.

A fill is one channel and a stroke pattern is the second. A status tint takes the light fill of its pair and a dashed stroke, and never the saturated stroke colour as its own fill, so a group stays lighter than the accent it borrows. A dash already marks a qualifier rather than a category in sk-design-diagram's guide, which dashes its optional and security treatments, so the pattern carries no new meaning here. A swatch in the board's key shows both channels, and a role the board shows by fill alone disappears in greyscale.

---

## 3. PALETTE

### Accent and lane pairs

The check accepts exactly the pairs in this record. Each fill takes only the stroke FigJam pairs it with, and a connector takes either the stroke or nothing. The lane pair is Figma's own suggestion for a diagram's one container, and it never counts as the accent.

The two ratio columns are measured: dark text on the fill against the 4.5:1 text gate, and the stroke on a white canvas against the 3.0:1 mark gate. `scripts/flow_check.py --self-test` re-measures every row and fails when a number or a pair drifts.

<!-- FIGJAM_PALETTE:BEGIN -->
| Role | Fill | Stroke | Text on fill | Stroke on canvas |
|---|---|---|---|---|
| Light green | `#CDF4D3` | `#66D575` | 13.87:1 | 1.85:1 |
| Light teal | `#C6FAF6` | `#5AD8CC` | 14.61:1 | 1.73:1 |
| Light blue | `#C2E5FF` | `#3DADFF` | 12.66:1 | 2.44:1 |
| Light violet | `#DCCCFF` | `#874FFF` | 11.21:1 | 4.57:1 |
| Light pink | `#FFC2EC` | `#F849C1` | 11.26:1 | 3.13:1 |
| Light red | `#FFCDC2` | `#FF7556` | 11.72:1 | 2.65:1 |
| Light orange | `#FFE0C2` | `#FF9E42` | 13.25:1 | 2.05:1 |
| Light yellow | `#FFECBD` | `#FFC943` | 14.28:1 | 1.53:1 |
| Light gray | `#D9D9D9` | `#B3B3B3` | 11.81:1 | 2.1:1 |
| Lane | `#F5F5F5` | `#B3B3B3` | 15.29:1 | 2.1:1 |
<!-- FIGJAM_PALETTE:END -->

### Picking the accent

| Pair | Reads as |
|---|---|
| Light green | Success, the happy path, completed |
| Light blue | Neutral focus, the step this diagram is about |
| Light red | Error, blocked, the failure path |
| Light orange or yellow | Warning, pending, a step under review |
| Light violet | A special case worth a second look |
| Light gray | Muted context, a deprecated step |

Pick the node the diagram exists to explain first, then the pair whose meaning matches it. With no clear meaning, light blue is the neutral default.

### Hybrid palettes

A hybrid extension sets colour through the Plugin API, where FigJam recognises a colour as a palette swatch only when each channel is written as `hex/255`. A rounded decimal makes it a custom colour that the colour picker no longer offers.

| Node | Palette |
|---|---|
| Sticky | White `#FFFFFF`, gray `#E6E6E6`, green `#B3EFBD`, teal `#B3F4EF`, blue `#A8DAFF`, violet `#D3BDFF`, pink `#FFA8DB`, red `#FFB8A8`, orange `#FFD3A8`, yellow `#FFE299` |
| Section | White `#FFFFFF`, light gray `#F9F9F9`, light green `#EBFFEE`, light teal `#F1FEFD`, light blue `#F5FBFF`, light violet `#F8F5FF`, light pink `#FFF0FA`, light red `#FFF5F5`, light orange `#FFF7F0`, light yellow `#FFFBF0` |
| Label | Violet fill `#874FFF`, stroke `#5427B4`, white text, the one preset for numbered pins |
| Status tint | The accent and lane pairs above, set as fill and stroke together |

Sticky colours keep FigJam's usual meanings: blue for discussion, yellow for a question, green for a positive, pink for a concern, red for a blocker and teal for a decision. One sticky colour per legend is the default, because the numbers already tell the stickies apart.

---

## 4. GATES

| Gate | Threshold | Applies to |
|---|---|---|
| Text on fill | 4.5:1 | Charcoal `#1E1E1E` on every fill the check accepts |
| Mark on canvas | 3.0:1 | A stroke that carries meaning, measured on a white canvas |
| Text on mark | 4.5:1 | The white digit on a label pin: 4.57:1 on violet `#874FFF` |

### Recorded departures

| Departure | Measures | Note |
|---|---|---|
| Seven strokes on the canvas | 1.53:1 to 2.65:1 | Every stroke but violet and pink sits under the mark gate. They are FigJam's own pairs, kept so a reader can recolour them from the picker, and the check never lets colour carry meaning alone |
| The lane stroke `#B3B3B3` | 2.1:1 | A lane outline is a container edge, not a mark, and its label names it |
| Figma's blue label example | Not used | Its white digit on `#3DADFF` measures 2.44:1, under the text gate, so the label pin takes the violet preset |
| The saturated fills | Not accepted | FigJam sets white text on a saturated fill, which measures 1.85:1 on `#66D575`. Mermaid cannot set a text colour, and the generator's text colour on a saturated fill was never observed, so the check refuses them |

The canvas is measured as white. FigJam's canvas is near white with a dot grid, and its exact value was not measured, so a stroke reads a little weaker on the board than the column says.

---

## 5. WHAT DID NOT TRANSLATE

sk-design-diagram draws its own SVG, so much of its style guide governs geometry the FigJam generator owns. These parts stay behind, each for a stated reason:

- **Fonts and the type ramp.** The generator sets FigJam's font, and the tool cannot change it afterwards
- **The 4px grid, node sizes and connector routing.** The generator lays the diagram out, and moving a generated node breaks its connectors
- **The bottom legend strip.** A legend on a board is a column of stickies beside the diagram, as `hybrid-workflow.md` sets out
- **Skins and brand onboarding.** A board is shared and recoloured in FigJam, so a brand palette would turn every swatch into a custom colour. A brand colour asked for by name is applied in the hybrid pass, and the reply says it is off-palette

---

## 6. WHAT HOLDS THE RECORD

- `scripts/figjam_checks/common.py` holds the pairs the check accepts
- The self-test fails when the record above names a pair the check does not accept, or the check accepts one the record does not name
- The self-test re-measures both ratio columns of every row and fails on any drift

---

## 7. SPACING

Colour tells a reader what belongs together, but space tells them first. A reader groups what sits close before reading a label, so a board that spaces every gap the same reads as one flat field and its own structure disappears.

| Band | Gap | What the gap separates |
|---|---|---|
| One thought | 60 to 92 pixels | Two nodes a reader takes as one step or one idea |
| Same topic | 200 to 400 pixels | Two groups the board discusses one after the other |
| Another part of the board | 1000 pixels or more | Content that answers a different question |

Two rules follow from the bands:

- Two unrelated groups are never closer than the text blocks inside a card, so the gap between groups always reads wider than the gap within one
- A wrapper is larger than the group's own internal gap and smaller than the gap to the next group, so its edge never falls on a neighbour

The generator lays out a Mermaid diagram, so these numbers govern what a person places: the legend column, a sticky beside its node, a tint, a title and the space between two diagrams on one board. They also judge a tint drawn behind generated nodes, because a tint that reaches 200 pixels across to the next group claims the two are one.

Stickies stand on FigJam's own grid, a gap of 64 pixels from the sticky beside them, aligned to the top left of the space they fill. A column of stickies keeps that grid, which is why its rows read as one list rather than as separate notes.
