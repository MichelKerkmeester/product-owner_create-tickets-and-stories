# Product Owner - Templates - Flow Hybrid Workflow

A model cannot put a note on a step. The composer draws everything else a model carries: the title, the zones, the colour of every kind, the sequence's step numbers and the key. So the hybrid workflow adds one thing, notes, with `use_figma` inside the board the write returned. Every note is a new node on top of the board. A composed node is never moved, resized or restyled.

---

## 1. WHEN TO EXTEND

Notes cost a second write, a read of the board and a wider rollback, so they are a judgement, not a default.

Extend when:

- The request asks for something the model cannot carry: notes, callouts or the reason behind a step
- The sources hold data that belongs on specific nodes, such as a drop-off rate, an owner or a service level
- The board is for others, such as a team review, and three or more nodes need a note

Do not extend when:

- The request is short and plain, such as "draw the checkout states"
- The diagram has under 8 nodes and a note would be louder than the diagram
- The ask is colour, grouping, a title, numbering or a key. The composer draws each of those from the model, so the fix is a model change, as Templates - Flow Mode Section 5 sets out

Figma ranks the value by type. Annotation helps a flowchart most, and sequence, state and gantt notes are added only when asked for.

---

## 2. THE PATTERN

1. **Compose** the board and keep the `fileKey` and the board id the write returned. Send the URL to the user as soon as it lands, before extending
2. **Pick** the target nodes by their ids in the write's node list, which carries each node's model id and label, or from a `get_figjam` read in a later session
3. **Extend** with one `use_figma` call on the same `fileKey`, following one recipe below, and return every created id with the board's size before the call
4. **Read back** the notes, as Section 6 sets out, and reply

Never create a new file and never call `figma.createPage()`, which throws on a FigJam file. Write `use_figma` code as plain JavaScript with top-level `await` and a `return` of every created id, as Figma's `figma-use` skill requires, and load a node's font before setting its text.

Every node inside a zone has coordinates relative to that zone, so a recipe places a note from the target's `absoluteBoundingBox` minus the board's, never from the `x` and `y` a read reports.

---

## 3. RECIPES

### Numbered pins with a sticky legend

The default for three or more notes. A small numbered circle sits on each annotated node's top-left corner, or on its top vertex when the node is a diamond, and the matching stickies stand in a column inside the board, to the right of the diagram, each starting with its number. The write widens the board to hold the column. The diagram stays clean and ten notes read as easily as three. The column stands 200 pixels clear of the diagram, a same-topic gap, and its stickies keep FigJam's 64 pixel grid between rows, as Rules - Flow Style Guide Section 7 sets the bands.

```javascript
// boardId from the composing write, notes: [{ id, note }] with each id from its node list
const h = (hex) => ({ r: parseInt(hex.slice(1, 3), 16) / 255, g: parseInt(hex.slice(3, 5), 16) / 255, b: parseInt(hex.slice(5, 7), 16) / 255 })
const board = await figma.getNodeByIdAsync(boardId)
const before = { w: board.width, h: board.height }
const origin = board.absoluteBoundingBox
const probe = figma.createSticky()
await Promise.all([figma.loadFontAsync(probe.text.fontName), figma.loadFontAsync({ family: 'Inter', style: 'Medium' })])
probe.remove()
const created = []
const edge = board.width - 80
let top = Infinity
for (let i = 0; i < notes.length; i++) {
  const node = await figma.getNodeByIdAsync(notes[i].id)
  const box = node.absoluteBoundingBox
  const diamond = node.type === 'SHAPE_WITH_TEXT' && node.shapeType === 'DIAMOND'
  const pin = figma.createShapeWithText()
  pin.shapeType = 'ELLIPSE'
  pin.name = `pin:${i + 1}`
  pin.text.fontName = { family: 'Inter', style: 'Medium' }
  pin.text.characters = String(i + 1)
  pin.text.fontSize = 20
  pin.resize(48, 48)
  pin.fills = [{ type: 'SOLID', color: h('#874FFF') }]
  pin.strokes = [{ type: 'SOLID', color: h('#5427B4') }]
  pin.text.fills = [{ type: 'SOLID', color: h('#FFFFFF') }]
  board.appendChild(pin)
  pin.x = box.x - origin.x - 24 + (diamond ? box.width / 2 : 0)
  pin.y = box.y - origin.y - 24
  top = Math.min(top, pin.y)
  created.push(pin.id)
}
let y = top
let right = edge
for (let i = 0; i < notes.length; i++) {
  const sticky = figma.createSticky()
  sticky.name = `note:${i + 1}`
  sticky.text.characters = `${i + 1}. ${notes[i].note}`
  sticky.fills = [{ type: 'SOLID', color: h('#A8DAFF') }]
  board.appendChild(sticky)
  sticky.x = edge + 200
  sticky.y = y
  y += sticky.height + 64
  right = Math.max(right, sticky.x + sticky.width)
  created.push(sticky.id)
}
board.resizeWithoutConstraints(Math.ceil((right + 80) / 8) * 8, Math.max(board.height, Math.ceil((y - 64 + 80) / 8) * 8))
await board.screenshot({ scale: Math.min(1, 1600 / board.width) })
return { createdNodeIds: created, boardBefore: before }
```

- A pin holds one or two characters at a fixed 48 by 48, or 64 by 64 for two
- The violet pin is the one preset whose white digit clears the text gate, as Rules - Flow Style Guide records. A sequence already numbers its messages with smaller pins in the `marker` role, so a note on a sequence names its message number in the sticky rather than adding a second pin beside it
- The pins and stickies are named `pin:<n>` and `note:<n>`, so the read-back counts them by name
- Never annotate every node, never repeat a node's label in its note, and never glue a sticky to its own pin

### A single sticky

For one or two notes, a sticky beside its node is clearer than a legend, so a request for one or two notes gets this form and no pin, no legend column and no sticky parked at the board's far edge away from its node. Place it inside the board 64 pixels clear of its node, which is the gap a sticky keeps from the sticky beside it: to the right first, then below, then above and to the left only when all three are taken and no connector runs between the sticky and its node. A sticky to the right of a node in the last column is allowed, and the board widens to hold it. Name it `note:<n>`, so the read-back counts it by name. Past two notes, switch to pins and a legend. Never mix the two in one diagram.

---

## 4. WHAT AN EXTENSION NEVER DOES

- Moves, resizes, rewires or restyles a composed node. A layout that reads badly is fixed in the model and composed again
- Draws a node, a connector, a zone, a title or a key entry. Each of those belongs in the model, so the composer draws it and the read-back counts it
- Writes outside the board section the write returned or to a file other than the one the gate named, or creates a page
- Uses a colour outside Rules - Flow Style Guide. A brand colour asked for by name is a hand edit, and the reply says it is off-palette
- Adds what nobody asked for. Every unrequested sticky is noise

The notes sit inside the tagged board section, so a later session that finds the board by its tag finds its notes with it, and replacing the board replaces them too.

---

## 5. GATE AND ROLLBACK

The yes before the first write covers the notes only when the gate message named them: what will be added, on which nodes and that the rollback deletes the ids the extension returns. Notes decided after the board landed need their own yes.

The rollback is to delete exactly the ids the extension returned and resize the board to the size the extension returned as `boardBefore`, through `use_figma`, after a yes to the deletion. Stop when an id is gone or belongs to a node that is not a pin or a note inside this board.

---

## 6. READ-BACK

Read the board with `get_figjam` and count the pins and the notes by name against what the extension planned, then check one screenshot for a pin or a sticky that covers a label. The line takes the form the recipe drew, pins with a legend or single stickies.

```text
Extensions: 4 of 4 pins, 4 of 4 legend stickies, 0 overlaps
Extensions: 2 of 2 notes, 0 overlaps
```

The first line is for three or more notes drawn as pins with a legend. The second is for one or two notes drawn as single stickies. The line sits after the board's own `Read-back:` line in the reply.

---

## 7. WHEN AN EXTENSION FAILS

The board already landed and the user already has its URL. Report what landed and what did not, with the error in a few words. When `use_figma` reports `safeToRetryWithoutCanvasRead: true`, fix the error and retry once. Otherwise read the board, find what the failed call left and ask before deleting any of it.

---

## 8. A BOARD OF SEVERAL DIAGRAMS

Work that needs two or more diagrams is planned before the first write, so a reader knows where one ends and the next begins and where to start.

- Each diagram is its own composed board, with its own title, key and tag, in the one file this work writes
- The title carries the diagram's ordinal and then its name, such as `%% title: 2. Workspace setup`, so the boards read as one numbered set
- The composer places each new board 400 pixels to the right of everything already on the page, its top level with the highest node, so the boards read left to right in the order they were written. Write them in reading order, because no later call moves one
- A split flow ends one board on a named hand-off node and starts the next board from the same name, so the reader follows the hand-off from one board to the next
- The reply names the board a reader opens first, by its ordinal and its name, and that first board is the one the reader's question starts in
