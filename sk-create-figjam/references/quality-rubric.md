---
title: "FigJam Diagram Quality Rubric"
description: "The taste gate a FigJam model passes before the write gate, translated from sk-design-diagram's success criteria: type fit, the remove test, signal, the check, the board and the reply."
contextType: implementation
importance_tier: important
trigger_phrases:
  - "figjam quality rubric"
  - "diagram taste gate"
  - "remove test"
  - "figjam review checklist"
version: 1.0.0.0
---

# FigJam Diagram Quality Rubric

The script checks what a script can see. This rubric is the rest: whether the diagram should exist, whether every node earns its place and whether the reader can trust what lands on the board. Walk it after the check passes and before the write gate.

**Loading Condition:** CONDITIONAL, on every Flow route before the write gate
**Purpose:** The judgement pass between the pre-write check and the gate
**Scope:** The model, the provenance table, the planned extensions and, after the write, the board and the reply

---

## 1. TYPE FIT

- [ ] The type answers the reader's question, as `references/flow-mode.md` Section 3 maps it
- [ ] A table, a list or a paragraph would not do the same job. If it would, say so and offer that instead
- [ ] The type's reference in `references/types/` was loaded and its judged-by-hand rules were applied
- [ ] A request for a kind the generator does not draw was answered with the nearest kind it does draw, or a plain no

---

## 2. THE REMOVE TEST

sk-design-diagram's highest-quality move is usually deletion. A diagram is done when nothing can be removed.

The remove test runs on the outline before the first Mermaid block, because a step cut from a list of steps costs a sentence and the same step cut from a drawn diagram costs a redraw. This section is the third rung of the challenge ladder in `references/flow-mode.md` Section 3, so the two rungs above it are asked first: what the board must not do, and whether a list, a table or a paragraph would serve the reader better.

- [ ] The `userIntent` sentence was agreed in the sparring and is the first line of the outline, rather than composed at the write call
- [ ] The remove test ran on the outline, one line per node and edge, before any layout was judged
- [ ] An unanswered sparring proposal is marked assumed and named in the playback before the gate
- [ ] No node can be removed without the reader losing a step they need
- [ ] Every node serves the `userIntent` sentence, or it is cut and named under `Left out:`
- [ ] No two nodes always travel together. If they do, they are one node
- [ ] No connector restates what the layout already shows
- [ ] No label repeats what the shape already says
- [ ] No diagram carries the same label on four or more connectors. Cut them all, or keep one where the label says something the shape cannot. Decision exits and sequence messages are exempt, and an architecture renames each edge instead, as its type reference sets out
- [ ] The remove test ran on the outline before the first Mermaid block, so no node was drawn only to be cut
- [ ] The diagram sits inside its budget, or was split, and every cut is named under `Left out:`

---

## 3. SIGNAL

The accent is chosen against a target written down first. A board judged only against itself cannot catch a second focal object, such as a title that repeats the claim the accent was meant to carry. Three lines are written before the first Mermaid block:

1. **First glance.** The one claim, decision or object that should win within two seconds
2. **Second glance.** The evidence or relationship that advances it
3. **Last glance.** The risk, the metadata or the appendix that stays available without competing

Those three lines travel into the gate, so the accent has a node to land on and the reply can say what should win.

- [ ] At most one accent, on the node a reader would keep if they could keep only one, never the node that comes first. The happy path, the riskiest decision, the costliest handoff and the error state are the candidates. Two that tie mean the diagram splits
- [ ] The three glance lines were written before the model and named in the gate
- [ ] The accent sits on the node the first glance names, which is the claim the reader came for rather than the node the flow reaches first, and nothing the second or last glance owns competes with it
- [ ] No title repeats the focal claim, so one idea carries one focal object. Where the title already states the claim, the accent carries the evidence, the consequence or the next move
- [ ] Shape and label carry the meaning on their own, so the diagram reads in greyscale
- [ ] A board carrying three or more kinds of mark carries a key, and the key names every shape, tint and dash the board uses and nothing else
- [ ] Each tint in the key shows both of its channels, the light fill and the dash, so a reader in greyscale still reads which nodes belong together
- [ ] Every label uses the product's or the source's own words. Proper nouns are never renamed
- [ ] The naming fits the audience: exact component names for engineers, plain verbs for a mixed team, capabilities and outcomes for leadership
- [ ] Nothing was invented to fill a lane, a slot or a gap. A missing step is asked about or named, never guessed

---

## 4. PROVENANCE

- [ ] Every node has a row in the provenance table naming its source and its source class
- [ ] Nothing marked proposal or unknown is drawn as current behavior. Its status sits in its label, or it is left out
- [ ] Every causal edge is stated by its sources from both ends. An edge one source states and another contradicts is a finding, not a connector
- [ ] A contradicted item leaves a trace the reader can see. It sits in the reply's `Left out:` line with both sources and the reason, or the one question that asks which source governs settled it. Nothing is removed in silence and no extra line is invented for it

---

## 5. THE CHECK AND THE GATE

- [ ] `scripts/flow_check.py` printed `PASSED` for the model file, with the type each diagram was read as
- [ ] The measures printed beside the counts were read: the widest rank, the longest path, the connectors per step, the average label length and the crossing pairs, against the budgets `scripts/figjam_checks/layout.py` sets
- [ ] A measure out of band was fixed in the model rather than on the board and the check rerun after the change, because the generator owns the layout and a tangled shape cannot be rearranged after the write
- [ ] The gate message names the plan, the file, what will be written, any planned extensions and the rollback
- [ ] An architecture call carries `useArchitectureLayoutCode`, and no other type carries it

---

## 6. THE BOARD

After the write, before the reply:

- [ ] The read-back counts match the model, as the type's reference sets them out
- [ ] Each provenance row whose class is not current behavior or whose edge is inferred was re-read against its source before the gate, and the row records the reason. A row that quotes a source line was not re-read
- [ ] The screenshot comes from `get_figjam`, which returns the outline with a screenshot of each node
- [ ] A node that needs its own view is read with `get_screenshot` and a node id from that read, because the tool fails without one
- [ ] Two screenshots of the board were taken for this pass: one of the whole board in a single frame and one at 100% zoom. Composition is judged on the overview, because a crossing and a crowded label are invisible at reading size
- [ ] The overview reads in the order the model plans, and that order was written down before the first screenshot
- [ ] The overview shows no connector crossing another, no two edges sharing a trunk the model draws apart and no two labels touching
- [ ] One screenshot of the diagram shows no stretched shape, no label cut off and no overlap with existing board content
- [ ] Every gap falls in one of the three bands `references/style-guide.md` Section 7 states, and two unrelated groups sit no closer than the text blocks inside a card
- [ ] Each tint leaves a margin wider than the gap inside its group and narrower than the gap to the next group, and none spans two groups
- [ ] The same screenshot shows no connector crossing and no edge that reads as joining the wrong node. Each edge is followed by eye from end to end, because a connector count does not prove that a route is clear
- [ ] The screenshot shows the one accent where Section 3 places it, and the board answers the `userIntent` sentence without the model beside it
- [ ] The accent node reads first, and no other node competes with it
- [ ] A screenshot finding is reported, and it is fixed only by reshaping the model and regenerating after a yes, inside the two-attempt bound `references/flow-mode.md` Section 9 sets
- [ ] Each extension landed where planned and covers no generated node's label
- [ ] The key that landed names every mark the board shows, and each tint swatch there carries its dash
- [ ] Nothing was moved, resized or restyled after generation
- [ ] Every finding below full marks names the label it sits on, where it sits in the frame, and one fix, which is a model change regenerated after a yes or a named generator limit the writer cannot move

---

## 7. THE REPLY

- [ ] The board URL first, then the `Read-back:` line, then any `Extensions:` and `Left out:` lines, then the `HVR self-scan:` line
- [ ] A mismatch is reported as measured, and the board is never called done on one
- [ ] No file was written to `export/`, and no Mermaid, HTML, SVG or PNG file was left behind
