---
title: "FigJam Diagram Style Guide"
description: "The colour every composed FigJam board draws by kind, the type scale and the 8 pixel grid, the palette pairs the check accepts with their measured contrast, and the spacing bands, translated from sk-design-diagram's style guide and derivation record."
contextType: implementation
importance_tier: important
trigger_phrases:
  - "figjam style guide"
  - "figjam palette"
  - "figjam colour by kind"
  - "figjam type scale"
  - "palette derivation record"
  - "figjam contrast"
version: 1.0.1.0
---

# FigJam Diagram Style Guide

The one source for colour, type and spacing on a FigJam board. The composer in `assets/compose-board.js` draws every board from the tables below, and every hex a model or a note extension uses comes from them. `scripts/flow_check.py` refuses any other.

**Loading Condition:** CONDITIONAL, before the gate on every Flow route, and when a model or a note extension uses colour
**Purpose:** Names the colour each kind draws in, the type scale, the grid, the palette pairs the check accepts and the measured contrast record
**Scope:** The composed board, Mermaid `style`, `classDef` and `linkStyle` colours, sticky and pin colours for notes, and the contrast record the self-test re-measures

---

## 1. OVERVIEW

sk-design-diagram owns a skinnable palette with semantic roles and a record of where each value comes from. A FigJam board already has a palette of its own, and a colour the board recognises as a palette swatch can be recoloured from FigJam's colour picker by anyone on the board. So this guide does not skin the board. It picks FigJam's own pairs, gives each kind of node one of them and records what each pair measures.

Three rules carry the board:

- **Colour by meaning.** A kind fixes a node's shape and colour together, so a goal is light green and a decision light yellow on every board, whichever type draws them. A colour never marks a position in the layout and is never picked for looks
- **The key names every colour.** The composer draws one key under the diagram, with a sample of every kind, line and arrow the board uses and nothing else, so a reader never meets a colour the board does not explain
- **Colour never carries meaning alone.** Most kinds also differ by shape, such as a diamond for a decision or a cylinder for a data store. Where two kinds share a shape and differ only by colour, such as a goal and an exit, the label names the outcome and the key names both, so a reader who cannot tell the fills apart still reads the board

The board carries one accent, a heavy pink outline on the node, message or task the first glance names. A user flow or a process marks it with a `style` line and the check refuses a model that has none. The other five types may name it with a `%% focus:` line. A `style` line does not colour a node for the board. It tells the composer what the node means, as Section 3 sets out.

---

## 2. KINDS

The composer reads each node's kind from the model: its shape, its place in the flow, its lane, its stereotype or its `style` line. The kind fixes the shape and the pair, and the key names it in the words below.

### Flows and processes

| Kind | Shape | Colour | Key | Read from |
|---|---|---|---|---|
| Start | Rounded rectangle | Light blue | Where it starts | A stadium node no edge enters |
| Screen or step | Rounded rectangle | White | Screen or step, or Step on a process | A plain node |
| Decision | Diamond | Light yellow | Decision | A rhombus |
| Goal | Rounded rectangle | Light green | Goal reached | A styled end, or the end the longest path reaches when none is styled |
| Exit | Rounded rectangle | Light orange | Leaves the flow | Every other unstyled end |
| Error | Rounded rectangle | Light red | Error or blocked | An end styled with the light red pair |
| Focus | Rounded rectangle | Light pink, 8 pixel outline | In focus | A styled step that is none of the kinds above |
| Merge | 24 pixel dot | Dark gray | Paths join | A circle |
| Data store | Cylinder | Light violet | Data store | A cylinder |
| Sub-process | Predefined process | White | Sub-process | A subroutine |
| Input or output | Parallelogram | Light teal | Input or output | A parallelogram |

An exit and an error sit beside the main line rather than on it, so the longest route to the goal stays one straight line.

The accent is not a kind. A styled goal, error, decision or any other node keeps the kind and fill it has and takes the pink outline on top, so a goal stays green and reads first. Only a styled step has no kind of its own to keep, so it is drawn light pink. The key adds `In focus` whenever the board carries an accent, and its sample is drawn as the marked node is, its own kind under the pink outline, so a goal in focus shows a green sample and a styled step a light pink one.

### Architecture

The lane a part sits in fixes its kind: a client is light teal, an edge or gateway light blue, a service white, a queue or stream an orange queue shape, a data store a violet cylinder and an outside system light gray.

### State, ER, sequence and gantt

| Kind | Shape | Colour | Key |
|---|---|---|---|
| Initial and final pseudo-state | 32 pixel dot, the final one ringed | Charcoal | Start, End |
| First state, a state, final state | Rounded rectangle | Light blue, white, light gray | First state, State, Final state |
| Choice | 56 pixel diamond | Light yellow | Choice |
| Fork or join | 16 by 96 pixel bar | Charcoal | Fork or join |
| Entity | Card with its fields | White | Entity |
| Participant | Rounded rectangle, drawn again at the foot of its lifeline | Light blue | Participant |
| Planned, in progress, done, critical | Bar, the critical one with a heavier outline and `, critical` after its length | White, light blue, light gray, light red | Planned, In progress, Done, Critical, heavy outline |
| Milestone | 32 pixel diamond | Light yellow | Milestone |

A sequence numbers every message with a violet pin at the left edge, and its key names the pin `Step number`.

### Lines and zones

| Element | Colour | Notes |
|---|---|---|
| Connector | Gray `#757575`, 2 pixels | Dashed for an optional or proposed edge, and for an async or outside call on an architecture |
| Request, reply | Charcoal solid and gray dashed, both with a closed head | Sequence |
| Async message, async reply | Blue `#3DADFF`, solid or dashed, with an open head | Sequence |
| Lifeline | Light gray `#B3B3B3`, dashed | Sequence |
| Accent | Pink `#F849C1`, 8 pixels around a node or bar and 4 pixels along a sequence message | The only pink and the only heavy line on a board |
| Relationship | Gray, solid when identifying and dashed when not, no arrow | ER, with the cardinality in the label |
| Zone | A section in a light tint, named in 24 pixel type | Tints cycle blue, orange, teal, yellow, violet and pink, so two neighbouring zones never read as one |
| Key | A light gray section under the diagram | One sample per mark the board uses |
| Board | A white section around everything | Named after the title |

---

## 3. PALETTE

### Accent and lane pairs

The check accepts exactly the pairs in this record. Each fill takes only the stroke FigJam pairs it with, and a connector takes either the stroke or nothing. The lane pair is Figma's own suggestion for a diagram's one container, and it never counts as the accent. The composer draws every kind from the same pairs, with white, charcoal and dark gray for the pseudo-states, the merge dot and the pins. The light pink pair is the accent's and no kind draws it.

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

### What a `style` line means

A user flow or a process may carry one `style` line, or several on nodes that share one pair. The composer reads it as meaning, not as paint:

| Where it sits | Pair | What the board shows |
|---|---|---|
| On an end | Light red | An error, in light red, with the pink outline |
| On an end | Any other pair | The goal, in light green, with the pink outline, and the spine runs to it |
| On a decision | Any pair | The decision keeps its light yellow diamond and takes the pink outline |
| On a step | Any pair | That step in focus, in light pink |

Pick the node the board exists to explain first, then the line that says what it is. A user flow and a process each need one such line, because the board has no other way to say what the first glance is, and the check refuses a model without one. With no end styled, the end the longest path reaches is still the goal and the others leave the flow, but the goal then carries no outline. A `linkStyle` line passes the check and changes nothing on a composed board, because a connector's colour belongs to its kind, and it never counts as the accent. An architecture, a sequence, a state diagram, an ER diagram and a gantt chart take no `style` line, because their kinds already carry their colour, and the check refuses styling on an architecture.

### The accent

The first glance is the one node, message or task a reader should see within two seconds, and the accent is how the board says so. Three measures keep it first:

- **A hue no kind uses.** The light pink pair belongs to the accent alone and every kind draws another pair. The nearest kind hues, light red at 52 degrees and light violet at 60, sit well clear of the accent's 319
- **Weight as well as colour.** A marked node or bar takes an 8 pixel outline against 2 for every other node and 4 for a critical bar, and a marked message takes 4 pixels against 2. On a greyscale copy pink and light blue are both just grey, so the line is what tells them apart. Weight times contrast on white puts 25.0 on the accent against 4.9 on the start pill and 12.6 on the heaviest other mark, the ring of an end state
- **The mark gate.** The pink stroke measures 3.13:1 on white, which only violet also clears, so it is the one outline on the board that holds at overview zoom

The start pill keeps its light blue, because at those weights it cannot outweigh the accent in colour or in greyscale. What carries the accent depends on the type:

| Type | What carries the accent | How the model says so |
|---|---|---|
| User flow, process | A node: a step, a decision, the goal or an error end | A `style` line, which the check requires |
| Architecture, state, ER | A node | `%% focus: <id>`, optional |
| Sequence | A message | `%% focus: <number>`, the message's place in the order, optional |
| Gantt | A task or a milestone | `%% focus: <id or name>`, optional |

A `%% focus:` line is a comment, so the Mermaid stays plain. It names one thing, and a second line, a name that matches nothing or a line on a user flow or a process is refused. Where a type carries no focus line the first glance is whatever the layout shows first, and the gate says so. A planned first glance is one thing, never a group such as the end states, and when the layout would show another first, the model names it with a focus line rather than promise a glance the board does not give.

### Note palettes

The composer and a note extension both set colour through the Plugin API, where FigJam recognises a colour as a palette swatch only when each channel is written as `hex/255`. A rounded decimal makes it a custom colour that the colour picker no longer offers.

| Node | Palette |
|---|---|
| Sticky | White `#FFFFFF`, gray `#E6E6E6`, green `#B3EFBD`, teal `#B3F4EF`, blue `#A8DAFF`, violet `#D3BDFF`, pink `#FFA8DB`, red `#FFB8A8`, orange `#FFD3A8`, yellow `#FFE299` |
| Section | White `#FFFFFF`, light gray `#F9F9F9`, light green `#EBFFEE`, light teal `#F1FEFD`, light blue `#F5FBFF`, light violet `#F8F5FF`, light pink `#FFF0FA`, light red `#FFF5F5`, light orange `#FFF7F0`, light yellow `#FFFBF0` |
| Label | Violet fill `#874FFF`, stroke `#5427B4`, white text, the one preset for numbered pins |

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

## 5. TYPE AND GRID

sk-design-diagram's type ramp and grid carry over, because the composer sets the font itself. Every board uses Inter at one scale:

| Text | Size | Weight |
|---|---|---|
| Title | 64 | Bold |
| Subtitle | 28 | Regular, wrapped at the diagram's width between 960 and 1440 pixels |
| Zone and key names | 24 | Semi Bold |
| Node label | 20 | Medium |
| Edge label, key entry, source line | 16 | Medium on a connector, Regular elsewhere |
| Entity field, gantt bar length, step pin | 14 to 16 | Regular or Medium |

Every position and size sits on an 8 pixel grid. A shape grows from its kind's base size until its label fits inside it, with a 32 pixel inset in a round shape whose text FigJam clips to the inscribed box, and every shape of one kind on a board takes the size of the largest, so a rank reads as one row.

The scale is tuned for a laptop at overview zoom. Reading distance does not change it, as `references/flow-mode.md` Section 4 sets out, and buys fewer nodes and shorter labels instead.

Skins and brand onboarding still stay behind. A board is shared and recoloured in FigJam, so a brand palette would turn every swatch into a custom colour. A brand colour asked for by name is a hand edit after the write, and the reply says it is off-palette.

---

## 6. WHAT HOLDS THE RECORD

- `scripts/figjam_checks/common.py` holds the pairs the check accepts
- `assets/compose-board.js` holds the kinds, the tints and the type scale the composer draws, and `scripts/compose_board.py --self-test` measures the accent's hue, weight and ink on every board it composes
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

The composer spaces the diagram on fixed steps: 80 pixels between two nodes in one rank, 136 between ranks, widened so an edge label fits its gap, a 48 pixel zone margin under a 96 pixel zone heading, 48 pixels between two zones, 80 pixels of board margin and 64 pixels above the key. Those steps are the composer's, and a board that reads cramped is fixed in the model rather than by changing them. The composer also routes every edge clear of the zones: no run lies along a zone's border, within 16 pixels outside it or 40 inside, so a line in the 48 pixel gap between two zones keeps to its middle, and no edge runs through a zone it neither starts nor ends in. An architecture therefore stands its lanes in the order client, gateway, service, async, datastore, external, so a queue sits beside the service that writes to it and an edge into it does not cross the stores. A node has four magnets, so each edge leaves from its own while one is free. Edges that only arrive may share a magnet once the others are taken, and then lie together for no more than 200 pixels, so a fourth client merges into the gateway near the target instead of looping across its zone to a free magnet. Any other two runs lie at least 56 pixels apart or share no more than a 56 pixel stub, so two edges never read as near-parallel lines, and a label keeps 8 pixels of air from every other line. A bend that lands on another edge counts as a crossing however short the jog after it, so two edges touch only where they merge into one magnet. The bands govern what a person or a note places: the legend column 200 pixels clear of the diagram, a sticky beside its node and the 400 pixels between two boards of one piece of work.

Stickies stand on FigJam's own grid, a gap of 64 pixels from the sticky beside them, aligned to the top left of the space they fill. A column of stickies keeps that grid, which is why its rows read as one list rather than as separate notes.
