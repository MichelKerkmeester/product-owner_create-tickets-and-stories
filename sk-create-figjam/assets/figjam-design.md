---
title: "FigJam Board Design"
description: "The design every composed FigJam board is drawn in, as one json block a team edits: what each colour means, the first-glance accent, the type sizes, the lines, the zone tints and the words on the key."
contextType: implementation
importance_tier: important
trigger_phrases:
  - "figjam design"
  - "figjam board design"
  - "restyle figjam boards"
  - "figjam design tokens"
  - "figjam board theme"
version: 1.0.0.0
---

# FigJam Board Design

> FigJam's own palette with one meaning per colour, one pink first glance and Inter at seven sizes. Flat, light and drawn on an 8 pixel grid.

This file is the style every board `assets/compose-board.js` draws. Change a token in the json block in Section 8 and every board composed after it follows. Nothing else needs editing. `scripts/compose_board.py` reads the block, sends the composer only the tokens that differ from its built-in design and names every token it could not use.

---

## 1. OVERVIEW

A board is drawn from FigJam's own palette, so anyone on it can recolour a node from FigJam's picker later. A design never adds a colour. It chooses which FigJam pair carries which meaning.

Three layers carry a colour from this file to a node:

- **Swatches** are FigJam's own pairs, each a fill, a stroke and a text colour, and its light section tints. The block lists them as reference, and they stay as FigJam ships them
- **Roles** say what a colour means, such as `goal` or `decision`, and each names one swatch. This is the layer a team restyles
- **Kinds** are what a model draws, such as a decision or a data store. Each kind names one role and the words its key entry shows, and its shape stays the composer's

So `"goal": "lightTeal"` turns every goal on every board teal and the key says so, while the shapes, the layout and the routing stay as they are. The board is flat: no shadow, no gradient and no fill on the board itself beyond white.

---

## 2. COLOUR ROLES

| Role | Swatch | What it marks | Drawn by |
|---|---|---|---|
| `entry` | Light blue | Where a reader starts | A flow's start, a state diagram's first state |
| `neutral` | White | An ordinary step | Screens, steps, states, services, sub-processes, entities, participants and planned bars |
| `goal` | Light green | The outcome the flow exists for | A flow's goal |
| `exit` | Light orange | A way out of the flow | An exit end |
| `error` | Light red | An error or a block | An error end, a critical gantt bar |
| `decision` | Light yellow | A choice, or a point a plan reaches | Decisions, state choices, milestones |
| `store` | Light violet | Data at rest | Data stores |
| `io` | Light teal | Input or output | Input and output steps |
| `client` | Light teal | An app or a client | Architecture clients |
| `gateway` | Light blue | The edge of a system | Architecture gateways |
| `queue` | Light orange | A queue or a stream | Architecture queues |
| `external` | Light gray | A system outside the board's scope | Architecture outside systems |
| `inProgress` | Light blue | Work under way | Gantt bars in progress |
| `done` | Light gray | Work finished | Gantt done bars, a state diagram's final states |
| `pseudo` | Charcoal | A state machine's own marks | Start and end dots, fork and join bars |
| `junction` | Dark gray | Paths that join | A flow's merge dot |
| `marker` | Violet | A numbered pin | A sequence's step numbers |

Light blue serves three roles but never two on one board. A flow and a state diagram start in it, an architecture marks its gateways in it and a gantt chart its work in progress, and the key names the one a board uses. Light teal, light orange and light gray split the same way, by diagram type.

---

## 3. THE ACCENT

The accent marks the one node, message or task a reader should see first. It is a pair no role draws, light pink by default, drawn as an `accent.node` outline of 8 pixels around a node or bar and an `accent.message` line of 4 pixels along a sequence message. A user flow or a process names it with a `style` line and the other types with `%% focus:`, as `references/style-guide.md` Section 3 sets out.

It keeps first place by three measures, which Section 7 holds every edit to:

- Its stroke clears 3:1 on white
- Its hue sits 45 degrees or more from every role a kind draws, every tint in the zone cycle and every line colour and the key's tint
- Its outline outweighs every other mark: heavier than the 6 pixel ring of an end state on a node, and heavier than the lines on a message

---

## 4. KINDS AND THE KEY

Each kind in the `kind` group names its role and its key words. `focus` names no role, because it draws the accent's own pair. The key shows one sample per kind, line and arrow the board draws, the kinds in the composer's own order, which reordering the `kind` group does not change, then the lines, the arrows, the step pin and the focus last. It is as wide as the diagram, and an entry that would run past that edge starts a new row.

The `key` group holds the key's own words: its title, the step pin's entry and one entry per line style and sequence arrow. Its `tint` is the section tint the key sits on.

---

## 5. TYPE

| Token | Default | Weight | Where it is used |
|---|---|---|---|
| `title` | 64 | Bold | The board's title |
| `subtitle` | 28 | Regular | The line under the title, wrapped between 960 and 1440 pixels into even lines |
| `zone` | 24 | Semi Bold | Zone names and the key's title |
| `node` | 20 | Medium | Node labels and entity names |
| `label` | 18 | Medium on a connector, Regular elsewhere | Edge labels, key entries, gantt axis and task names, the source line |
| `field` | 16 | Regular | Entity fields |
| `small` | 14 | Medium | Gantt bar lengths and step pins |

`family` names the face. The board loads its Medium, Regular, Semi Bold and Bold styles, taking Semi Bold under either name FigJam gives it, `Semi Bold` or `SemiBold`. When a style will not load, the board is set in Inter and the composer's warnings say so, so pick a family that carries all four.

---

## 6. LINES AND ZONES

| Token | Default | Draws |
|---|---|---|
| `line.color` | `#757575` | Every connector, and a sequence's requests and replies |
| `line.async` | `#3DADFF` | A sequence's async messages and replies |
| `line.lifeline` | `#B3B3B3` | A sequence's lifelines |
| `line.weight` | 2 | Every line but the accent's |

A line colour is one of the colours the swatch block holds, any fill, stroke or text, so it stays on FigJam's palette.

`zone.cycle` lists the section tints zones and gantt sections take in turn. Each takes the first tint along the cycle that no node inside it draws and that no zone beside it took, within two zone gaps on any side. An orange exit never sits in an orange zone and two neighbouring zones never read as one, however the layout placed them. When no tint keeps both rules, a zone keeps the neighbour rule, repeats a member's hue and the composer's warnings say so. Pink stays out of the cycle, because it is the accent's hue, and gray is left for the key.

Spacing stays the composer's: the gaps between ranks and zones, the zone margins and the board's margin. The router measures every clearance against that spacing, so a board that reads cramped is fixed in the model, as `references/style-guide.md` Section 7 sets out.

---

## 7. FLOORS

A token that misses a floor falls back to its built-in value and the rest of the design stands. When the file changed two tokens that miss a floor together, one falls back at a time and the floors are measured again, so the other stands once the floor holds.

| Floor | Measure |
|---|---|
| Text on a fill | Each role's text colour on its fill at 4.5:1 or more |
| The accent's own pair | No role names the accent's pair |
| The accent's hue | 45 degrees or more from every saturated role stroke, zone tint, line colour and the key's tint on the board |
| The accent's contrast | Its stroke at 3:1 or more on white |
| The accent's weight | A node outline over 6 and up to 16 pixels, a message line heavier than the lines and up to 8 |
| Lines | 1 to 4 pixels, `line.color` at 3:1 or more on white and `line.async` and `line.lifeline` at 2:1 or more, because an open head also marks an async message and a lifeline is a guide |
| Dots | A start, an end, a merge and a fork carry no label, so the fill of the role each draws measures 3:1 or more on white |
| Kinds apart | No two kinds one type draws share a shape, a pair and an outline |
| Type | `small` 14 or more, `label` and `field` from `small` up to `node`, `node` 16 to 24, `zone` from `node` up to 24, the largest zone name the router keeps a zone's head clear for, `subtitle` from `zone` up to `title`, `title` from twice `node` up to 128 |
| Names | A role or the accent names a swatch, a kind names a role, the cycle and the key's tint name section tints, the cycle holds two or more tints once each and never the key's tint |
| Words | Key words and `meta.name` on one line of 40 characters or fewer, every character of them text |

Three more rules keep a bad edit from passing silently:

- A group or a token the composer does not read is left out, and a value of the wrong type falls back
- An edit to a swatch or a tint is ignored, because those are FigJam's own colours
- A file with no json block, two blocks, a block that does not parse or another `schemaVersion` falls back whole to the built-in design, and so does one the reader cannot handle for any other reason, so an edit never stops a board

Do pick a role's swatch for what it means on every board, and keep the accent the only pink. Do not give two kinds of one type the same swatch and shape, and do not reach for a colour outside FigJam's pairs, because a custom colour drops out of FigJam's picker.

---

## 8. TOKENS

```json
{
  "meta": {"name": "FigJam default", "schemaVersion": 1},
  "role": {
    "entry": "lightBlue",
    "neutral": "white",
    "goal": "lightGreen",
    "exit": "lightOrange",
    "error": "lightRed",
    "decision": "lightYellow",
    "store": "lightViolet",
    "io": "lightTeal",
    "client": "lightTeal",
    "gateway": "lightBlue",
    "queue": "lightOrange",
    "external": "lightGray",
    "inProgress": "lightBlue",
    "done": "lightGray",
    "pseudo": "black",
    "junction": "darkGray",
    "marker": "violet"
  },
  "accent": {"pair": "lightPink", "node": 8, "message": 4},
  "kind": {
    "initial": {"role": "pseudo", "key": "Start"},
    "start": {"role": "entry", "key": "Where it starts"},
    "firstState": {"role": "entry", "key": "First state"},
    "client": {"role": "client", "key": "App or client"},
    "gateway": {"role": "gateway", "key": "Edge or gateway"},
    "participant": {"role": "neutral", "key": "Participant"},
    "screen": {"role": "neutral", "key": "Screen or step"},
    "step": {"role": "neutral", "key": "Step"},
    "state": {"role": "neutral", "key": "State"},
    "service": {"role": "neutral", "key": "Service"},
    "subprocess": {"role": "neutral", "key": "Sub-process"},
    "io": {"role": "io", "key": "Input or output"},
    "entity": {"role": "neutral", "key": "Entity"},
    "queue": {"role": "queue", "key": "Queue or stream"},
    "decision": {"role": "decision", "key": "Decision"},
    "choice": {"role": "decision", "key": "Choice"},
    "fork": {"role": "pseudo", "key": "Fork or join"},
    "merge": {"role": "junction", "key": "Paths join"},
    "success": {"role": "goal", "key": "Goal reached"},
    "exit": {"role": "exit", "key": "Leaves the flow"},
    "error": {"role": "error", "key": "Error or blocked"},
    "finalState": {"role": "done", "key": "Final state"},
    "final": {"role": "pseudo", "key": "End"},
    "datastore": {"role": "store", "key": "Data store"},
    "external": {"role": "external", "key": "Outside system"},
    "done": {"role": "done", "key": "Done"},
    "active": {"role": "inProgress", "key": "In progress"},
    "planned": {"role": "neutral", "key": "Planned"},
    "crit": {"role": "error", "key": "Critical, heavy outline"},
    "milestone": {"role": "decision", "key": "Milestone"},
    "focus": {"key": "In focus"}
  },
  "type": {"family": "Inter", "title": 64, "subtitle": 28, "zone": 24, "node": 20, "label": 18, "field": 16, "small": 14},
  "line": {"color": "#757575", "async": "#3DADFF", "lifeline": "#B3B3B3", "weight": 2},
  "zone": {"cycle": ["blue", "orange", "teal", "yellow", "violet"]},
  "key": {
    "title": "Key",
    "tint": "gray",
    "pin": "Step number",
    "dashedOptional": "Optional or proposed",
    "dashedAsync": "Async or outside call",
    "identifying": "Identifying",
    "nonIdentifying": "Non-identifying",
    "twoWay": "Both ways",
    "request": "Request",
    "reply": "Reply",
    "async": "Async message",
    "asyncReply": "Async reply"
  },
  "swatch": {
    "white": ["#FFFFFF", "#B3B3B3", "#1E1E1E"],
    "black": ["#1E1E1E", "#B3B3B3", "#FFFFFF"],
    "darkGray": ["#757575", "#5E5E5E", "#FFFFFF"],
    "violet": ["#874FFF", "#5427B4", "#FFFFFF"],
    "lightBlue": ["#C2E5FF", "#3DADFF", "#1E1E1E"],
    "lightGreen": ["#CDF4D3", "#66D575", "#1E1E1E"],
    "lightYellow": ["#FFECBD", "#FFC943", "#1E1E1E"],
    "lightOrange": ["#FFE0C2", "#FF9E42", "#1E1E1E"],
    "lightRed": ["#FFCDC2", "#FF7556", "#1E1E1E"],
    "lightViolet": ["#DCCCFF", "#874FFF", "#1E1E1E"],
    "lightPink": ["#FFC2EC", "#F849C1", "#1E1E1E"],
    "lightTeal": ["#C6FAF6", "#5AD8CC", "#1E1E1E"],
    "lightGray": ["#D9D9D9", "#B3B3B3", "#1E1E1E"]
  },
  "tint": {"gray": "#F9F9F9", "green": "#EBFFEE", "teal": "#F1FEFD", "blue": "#F5FBFF", "violet": "#F8F5FF", "pink": "#FFF0FA", "red": "#FFF5F5", "orange": "#FFF7F0", "yellow": "#FFFBF0"}
}
```

---

## 9. CHANGING THE DESIGN

1. Edit a value in the block above. A role or the accent names a swatch, the zone cycle and the key's tint name section tints and a line colour is a hex from the swatch block
2. Run `python3 sk-create-figjam/scripts/compose_board.py --design-check`. It prints the design's name, each token that differs from the built-in design, each role's measured contrast, the accent's nearest hue, the `THEME` it sends and the room left for the model. It exits 1 on any design warning
3. Compose as usual. Each design warning prints a `DESIGN` line, the `COMPOSED` line counts them and the Flow reply carries a `Finding:` line for each
4. Rename `meta.name` for a team design. The name and a short hash travel with the theme and go into the board's tag, so a later revision knows which design drew it

A claude.ai Project mirrors this file as Knowledge `Assets - Flow Board Design`, and its composer takes the `THEME` line that `--design-check` prints.

The composer keeps the same values built in, as `const D` in `assets/compose-board.js`, so a board drawn with an empty theme matches this file as shipped. A change to a built-in value changes this block with it, and `--design-check` lists every token where the two differ.
