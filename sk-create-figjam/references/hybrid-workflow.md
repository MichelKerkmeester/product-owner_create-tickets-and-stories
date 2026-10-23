---
title: "FigJam Hybrid Workflow"
description: "How to add what Mermaid cannot say to a generated FigJam diagram: numbered pins with a sticky legend, a single sticky, a status tint behind a group and a legend section, each additive, gated and reversible, plus the title every diagram carries."
contextType: implementation
importance_tier: important
trigger_phrases:
  - "figjam hybrid workflow"
  - "annotate figjam diagram"
  - "sticky legend"
  - "colour code figjam"
  - "use_figma extension"
version: 1.0.0.0
---

# FigJam Hybrid Workflow

Mermaid cannot put a note on a step, colour a state, number a message or group entities by domain. The hybrid workflow generates the diagram first, then adds those pieces with `use_figma` in the same file. Every addition is a new node beside or behind the diagram. A generated node is never moved, resized or restyled. A tag on a created node is metadata, so it is not a move, a resize or a restyle.

**Loading Condition:** ON_DEMAND, when the request asks for notes, callouts, numbering, highlighting or colour the model cannot carry
**Purpose:** When to extend a generated diagram, the four recipes, their gate and their rollback
**Scope:** Additions through `use_figma` on the hosted route. The `fj` route adds nothing beyond the diagram

---

## 1. WHEN TO EXTEND

Extending costs a second tool call, a read of the board and a wider rollback, so it is a judgement, not a default.

Extend when:

- The request asks for something the model cannot carry: notes, callouts, numbers, highlighted phases, colour-coded states or domains
- The sources hold data that belongs on specific nodes, such as a drop-off rate, an owner or a service level
- The board is for others, such as a team review, and three or more nodes need a note

Do not extend when:

- The request is short and plain, such as "draw the checkout states"
- The diagram has under 8 nodes and a note would be louder than the diagram
- The only extension would be colour on a user flow or a process, which the model already carries as its one accent

Figma ranks the value by type. Annotation helps a flowchart most, colour by domain helps an ER diagram most, and sequence, state and gantt extensions are added only when asked for.

A title never waits on this judgement. It is written with the diagram rather than added to it, so it costs one write call and no extra read, and Figma treats a title block as needing no inspection. Section 3 sets its string and its scale.

---

## 2. THE PATTERN

1. **Generate** the diagram and keep the `fileKey` from the returned URL. Send the URL to the user as soon as it lands, before extending
2. **Read** the diagram with `get_figjam` to find each target node's id and bounds
3. **Extend** with one `use_figma` call on the same `fileKey`, following one or more recipes below, and return every created id
4. **Read back** the extension, as Section 6 sets out, and reply

Never create a new file and never call `figma.createPage()`, which throws on a FigJam file. Write `use_figma` code as plain JavaScript with top-level `await` and a `return` of every created id, as Figma's `figma-use` skill requires. Load a node's font before setting its text.

Every recipe starts from the same helper, which writes a colour as `hex/255` so FigJam keeps it a palette swatch:

```javascript
const h = (hex) => ({ r: parseInt(hex.slice(1, 3), 16) / 255, g: parseInt(hex.slice(3, 5), 16) / 255, b: parseInt(hex.slice(5, 7), 16) / 255 })
```

---

## 3. RECIPES

### The legend is the board's key

A legend that lists only the notes leaves the board's own vocabulary unexplained. The numbered pins below explain a set of notes, and a legend has a second job: it names every shape, tint and dash the board uses. It appears once the board carries three or more kinds of mark, counting a tint as a kind, and it holds one entry for every kind the board uses and nothing else. A board under three kinds explains itself and carries no key.

Each entry is a small swatch of the mark itself beside the word for it, so a reader matches what they see to what it means without asking. A swatch shows the fill and the stroke the board uses, and a tint's swatch shows the dash as well, because a swatch with one channel teaches half the meaning. The key stands in the column the notes use, to the right of the diagram, so a board holding both keeps one column rather than two. Its entries are written as stickies, so the section recipe below applies once the key holds more than five.

### Numbered pins with a sticky legend

The default for three or more notes. A small numbered circle sits on each annotated node's top-left corner, and the matching stickies stand in a column to the right of the diagram, each starting with its number. The diagram stays clean and ten notes read as easily as three. The column is one group, so its stickies keep FigJam's 64 pixel grid gap between rows and the whole column stands one topic gap from the diagram, as `style-guide.md` Section 7 sets the bands.

```javascript
// targets: [{ id, x, y, width, height }] from get_figjam, notes: ["Drop-off: 42% last quarter", ...]
const pins = [], stickies = []
const probePin = figma.createShapeWithText()
const probeSticky = figma.createSticky()
await Promise.all([figma.loadFontAsync(probePin.text.fontName), figma.loadFontAsync(probeSticky.text.fontName)])
probePin.remove()
probeSticky.remove()
for (let i = 0; i < targets.length; i++) {
  const pin = figma.createShapeWithText()
  pin.shapeType = 'ELLIPSE'
  pin.text.characters = String(i + 1)
  pin.resize(48, 48)
  pin.text.fontSize = 20
  pin.fills = [{ type: 'SOLID', color: h('#874FFF') }]
  pin.strokes = [{ type: 'SOLID', color: h('#5427B4') }]
  pin.text.fills = [{ type: 'SOLID', color: h('#FFFFFF') }]
  pin.x = targets[i].x - 24
  pin.y = targets[i].y - 24
  pins.push(pin)
  const sticky = figma.createSticky()
  sticky.text.characters = `${i + 1}. ${notes[i]}`
  sticky.fills = [{ type: 'SOLID', color: h('#A8DAFF') }]
  stickies.push(sticky)
}
const right = Math.max(...targets.map((t) => t.x + t.width))
const top = Math.min(...targets.map((t) => t.y))
const bottom = Math.max(...targets.map((t) => t.y + t.height))
const clear = figma.currentPage.children
  .filter((n) => !pins.includes(n) && !stickies.includes(n) && n.y < bottom + 250 && n.y + n.height > top)
  .reduce((max, n) => Math.max(max, n.x + n.width), right)
let y = top
for (const sticky of stickies) {
  sticky.x = clear + 200
  sticky.y = y
  y += sticky.height + 64
}
return { createdNodeIds: [...pins, ...stickies].map((n) => n.id) }
```

- A pin holds one or two characters at a fixed 48 by 48, or 64 by 64 for two
- The violet pin is the one preset whose white digit clears the text gate, as `style-guide.md` records
- Never annotate every node, never repeat a node's label in its note, and never glue a sticky to its own pin

### A single sticky

For one or two notes, a sticky beside its node is clearer than a legend. Place it to the right of the node, or above or below when the right is taken, 64 pixels clear, which is the gap a sticky keeps from the sticky beside it. Past two notes, switch to pins and a legend. Never mix the two in one diagram.

### A status tint behind a group

Colour for a state, ER or sequence diagram, where Mermaid styling is stripped. Rather than restyle the generated nodes, draw a tinted rounded rectangle behind each group and send it to the back so the nodes sit on top of it. The margin is wider than the gap the group keeps inside itself and narrower than the gap to the nearest group, as `style-guide.md` Section 7 sets out, so the tint reads as one group rather than as a loose rectangle around two.

```javascript
// groups: [{ name, fill, stroke, nodes: [{ x, y, width, height }] }] from get_figjam and style-guide.md
const created = []
// wider than the gap inside a group and narrower than the gap to the next one
const pad = 40
for (const group of groups) {
  const left = Math.min(...group.nodes.map((n) => n.x)) - pad
  const top = Math.min(...group.nodes.map((n) => n.y)) - pad
  const right = Math.max(...group.nodes.map((n) => n.x + n.width)) + pad
  const bottom = Math.max(...group.nodes.map((n) => n.y + n.height)) + pad
  const tint = figma.createShapeWithText()
  tint.shapeType = 'ROUNDED_RECTANGLE'
  tint.resize(right - left, bottom - top)
  tint.x = left
  tint.y = top
  tint.fills = [{ type: 'SOLID', color: h(group.fill) }]
  tint.strokes = [{ type: 'SOLID', color: h(group.stroke) }]
  tint.dashPattern = [8, 6]
  tint.name = group.name
  figma.currentPage.insertChild(0, tint)
  created.push(tint.id)
}
return { createdNodeIds: created }
```

- Tint groups, never single nodes one by one, and pick each pair from the accent table in `style-guide.md`
- The tint takes the light side of the pair as its fill and a dashed stroke, never the saturated stroke colour as its fill, so the group stays lighter than the accent it borrows
- The dash is the second channel, so a reader who cannot tell two fills apart still reads which nodes belong together
- Two to four groups is the useful range. A tint per node carries no meaning
- Every group the board tints is an entry in the key, because the group's layer name is not text a reader can see
- A board whose stroke will not take a pattern keeps the light fill, and the reply says the tint carries one channel

### A legend section and a title

A section holds the legend stickies when there are more than five, named with a short word such as `Notes`. Create the section, then `appendChild` each sticky this write created and place it in section coordinates, then resize the section to its stickies plus 32 pixels on every side. A section never wraps a generated node, because adding a node to a section moves it.

A title is a text node above the diagram, 64 pixels clear of its top edge, in charcoal `#1E1E1E`, naming what the reader is looking at.

Every diagram carries one, whether or not the request asked for a title, and its string is the one the generator was given as its `name`. Its text size is 60 to 96 pixels, so it reads at overview zoom, the zoom a reader arrives at, and the board has an entry point before any node is read. No read comes before it, because a title block needs no inspection to place.

---

## 4. WHAT AN EXTENSION NEVER DOES

- Moves, resizes, rewires or restyles a generated node. A layout that reads badly is fixed in the model and regenerated
- Builds the diagram by hand when `generate_diagram` can draw it
- Writes to a file other than the one the gate named, or creates a page
- Uses a colour outside `style-guide.md`. A brand colour asked for by name is applied here and the reply says it is off-palette
- Adds what nobody asked for. Every unrequested sticky is noise

Tagging a created node with metadata is allowed, because the tag changes nothing a reader sees. The tag is shared plugin data written with `setSharedPluginData` under a fixed namespace of `productowner`, keyed by the diagram's name so a later session can rebuild the key. It is written only after the read-back and only when the gate named the write. `references/flow-mode.md` Section 6 sets out the value and the set of nodes to tag. Every read and every write is wrapped so a refusal leaves the board as it was.

---

## 5. GATE AND ROLLBACK

The yes before the first write covers the extension only when the gate message named it: what will be added, where, and that the rollback deletes the ids the extension returns. An extension decided after the diagram landed needs its own yes. The gate also says whether the created nodes will be tagged, because a later session reads the tags before it deletes or regenerates anything.

The rollback is to delete exactly the ids the extension returned, through `use_figma`, after a yes to the deletion. Read the board and its tags first, and treat a node that carries this work's tag as one this write created. Stop when an id is gone or belongs to a node with no returned id and no tag.

---

## 6. READ-BACK

Read the board with `get_figjam` and count what the extension added against what it planned, then check one screenshot for overlap with the diagram.

```text
Extensions: 4 of 4 pins, 4 of 4 legend stickies, 0 overlaps
```

The line sits after the diagram's own `Read-back:` line in the reply.

---

## 7. WHEN AN EXTENSION FAILS

The diagram already landed and the user already has its URL. Report what landed and what did not, with the error in a few words. When `use_figma` reports `safeToRetryWithoutCanvasRead: true`, fix the error and retry once. Otherwise read the board, find what the failed call left, and ask before deleting any of it.

---

## 8. COMPOSING A BOARD

A board that holds two or more diagrams is a composition, and it is planned before the first write. Two diagrams placed beside each other with no plan leave the reader to work out where one ends and the next begins, and no later call may move either one.

- Zones read left to right along a row and wrap to a new row below, so no diagram lands above or to the left of the one that comes before it. One direction holds for every board and it is never chosen per request
- Each zone carries a heading above its diagram that reads as an ordinal and then the diagram's name, such as `2. Workspace setup`. The heading is the title Section 3 places above a diagram, so a board of zones carries one heading per diagram and never two
- 92 pixels separate two zones in one row and 120 pixels separate two rows, measured between the nearest edges of the two diagrams
- A zone is a heading and a gap, never a section. The diagram is never reparented into a section and no section is resized around it, because adding a node to a section moves it
- The reply names the zone a reader opens first, by its ordinal and its name, and that first zone is the one the board's question starts in
