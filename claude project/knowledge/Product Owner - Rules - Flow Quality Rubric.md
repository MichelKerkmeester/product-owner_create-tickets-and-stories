# Product Owner - Rules - Flow Quality Rubric

The type's rules are checked one by one before the gate. This rubric is the rest: whether the diagram should exist, whether every node earns its place and whether the reader can trust what lands on the board. Walk it after the check passes and before the write gate.

---

## 1. TYPE FIT

- [ ] The type answers the reader's question, as Templates - Flow Mode Section 3 maps it
- [ ] A table, a list or a paragraph would not do the same job. If it would, say so and offer that instead
- [ ] The chosen type's Templates - Flow Type document was read and its judged-by-hand rules were applied
- [ ] A request for a kind Flow Mode does not draw was answered with the nearest type it does draw, or a plain no

---

## 2. THE REMOVE TEST

the house diagram guide's highest-quality move is usually deletion. A diagram is done when nothing can be removed.

The remove test runs on the outline before the first Mermaid block, because a step cut from a list of steps costs a sentence and the same step cut from a drawn diagram costs a redraw. This section is the third rung of the challenge ladder in Templates - Flow Mode Section 3, so the two rungs above it are asked first: what the board must not do, and whether a list, a table or a paragraph would serve the reader better.

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

The marked node is chosen against a target written down first. A board judged only against itself cannot catch a second focal object, such as a title that repeats the claim the marked node was meant to carry. Three lines are written before the first Mermaid block:

1. **First glance.** The one claim, decision or object that should win within two seconds
2. **Second glance.** The evidence or relationship that advances it
3. **Last glance.** The risk, the metadata or the appendix that stays available without competing

Those three lines travel into the gate, so the marked node is chosen from them and the reply can say what should win. After the first glance, filled shapes and their keyed fills outweigh connector labels and text in the overview, so the lines name a filled group such as the gray end states before the labels between them. Every node the board draws sits in one of the three lines, because a part the lines leave out still reads early and takes the second glance. Lanes and zones read as part of the frame, like the title block, so the lines plan the nodes inside them and never the lane or zone itself. On a user flow or a process a reader takes the main row after the accent, in path order whatever its fills. The main row is the longest path from the light blue entry to the goal, which the composer draws as one row, or across the lanes on a laned process, so a detour on that path is part of it. The second glance names the main row in path order, the entry included and the accented node left out, and the last glance names every node off it, such as an error, an exit, a branch, a loop back or a data store, in path order. The entry and the goal in one line carry no order between them. On any other type a gateway, an error and a critical bar carry a 4 pixel outline and read right after the accent, so the second glance line plans each one the board draws unless the accent sits on it. A revision that makes a changed end the second glance follows the revision rule below, and a state board takes its order from Templates - Flow Type - State Section 5 instead.

- [ ] One accent on a user flow or a process, on the node a reader would keep if they could keep only one, never the node that comes first. The goal, a failure end, a decision and the one step in focus are the candidates, as Rules - Flow Style Guide Section 3 sets out. Two that tie mean the diagram splits
- [ ] The three glance lines were written before the model and named in the gate
- [ ] On a user flow or a process the first glance is the accented node, marked by the one `style` line the check requires, and the gate names it. On a state board it is the first state, which the layout always shows first, and a `%% focus:` line marks the state the request names where it is drawn, as Templates - Flow Type - State Section 5 sets out. On any other type it is the node, message or task a `%% focus:` line names, or, when the model has none, whatever the layout shows first, and the gate says which. The first glance is one node, message or task, never a group such as the end states, and when the layout would show another first, a `%% focus:` line marks it, so the gate never promises a first glance the board does not show. Except on a state board, it is the claim the reader came for rather than the node the flow reaches first, and nothing the second or last glance owns competes with it
- [ ] On a revision the changed step, decision or failure end is the first glance and takes the accent. When the change is any other end, the accent stays on the goal and the gate and the reply name the changed end alone as the second glance, with the entry, the decisions and the rest of the main row in the last glance line, because a style line on an end makes that end the goal and a second glance shared with the entry hides the change. On an extension that pins several problems, the accent stays on the goal and the pins carry the problems as the second glance
- [ ] When the model gives a reason for the accent as `%% focus: <id> because <reason>`, as Rules - Flow Style Guide Section 3 sets out, the key's `In focus` entry carries that reason, so a reader who asks why one node is marked finds the answer on the board
- [ ] No title repeats the focal claim, so one idea carries one focal object. Where the title already states the claim, the marked node carries the evidence, the consequence or the next move
- [ ] The title names what the reader is looking at. The subtitle says in one sentence who reads it and why. The source line names the sources and what was left out
- [ ] Shape and outline and label carry the meaning without colour, so the diagram reads in greyscale
- [ ] The key the composer draws names every kind, line and arrow the board shows and nothing else, and no note adds a second key beside it
- [ ] Every zone carries a name a reader can see, and zones group what belongs together rather than marking a position
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

- [ ] Every rule in the type's Templates - Flow Type document holds for each diagram, checked one by one
- [ ] The model's shape was read before the gate: the widest rank at most 4 steps, the longest path at most 8 steps, at most 2 connectors per step, labels averaging at most 28 characters and at most 2 connector pairs that swap sides
- [ ] A shape out of band was fixed in the model rather than on the board and read again after the change, because the composer owns the layout and a tangled shape is never rearranged after the write
- [ ] The MODEL for every diagram was written as Assets - Flow Board Composer Section 2 sets out, with the counts the read-back will look for, and the code in its Section 4 was placed whole
- [ ] The gate message names the plan, the file, what will be written, any planned extensions, the calls the write will spend and the rollback
- [ ] On the generated fallback, an architecture call carries `useArchitectureLayoutCode`, and no other type carries it

---

## 6. THE BOARD

After the write, before the reply:

- [ ] The read-back counts match the model, as the type's reference sets them out
- [ ] Each provenance row whose class is not current behavior or whose edge is inferred was re-read against its source before the gate, and the row records the reason. A row that quotes a source line was not re-read
- [ ] The write returned no warning, and its counts match the counts the model expects
- [ ] The overview is the screenshot the composing call returned, and `get_figjam` supplies the outline with a screenshot of each node
- [ ] A node that needs its own view is read with `get_screenshot` and a node id from that read, because the tool fails without one
- [ ] Two screenshots of the board were taken for this pass: one of the whole board in a single frame and one at 100% zoom. Composition is judged on the overview, because a crossing and a crowded label are invisible at reading size
- [ ] The overview reads in the order the model plans, and that order was written down before the first screenshot
- [ ] The overview shows no connector crossing another, no connector or label on a zone title, no two edges sharing a trunk the model draws apart and no two labels touching
- [ ] No edge runs through a zone it neither starts nor ends in. Edges that only arrive may share one magnet and then lie together for no more than 200 pixels
- [ ] One screenshot of the diagram shows no stretched shape, no label cut off and no overlap with existing board content
- [ ] Every gap a note or a person placed falls in one of the three bands Rules - Flow Style Guide Section 7 states, and two unrelated groups sit no closer than the text blocks inside a card
- [ ] Each zone holds its own nodes and no other, and no zone overlaps another
- [ ] The same screenshot shows no connector crossing and no edge that reads as joining the wrong node. Each edge is followed by eye from end to end, because a connector count does not prove that a route is clear
- [ ] Every colour on the board matches its entry in the key. The marked node sits where Section 3 places it. The board answers the `userIntent` sentence without the model beside it
- [ ] Every fill on the board resolves to a role in the active design, as Assets - Flow Board Design holds it, no zone tint shares a hue with a kind inside it or with the accent, and no note added a colour the design does not name
- [ ] The marked node reads first, and no other node competes with it, except on a state board, where it reads where the composer draws it and leads its glance line
- [ ] A screenshot finding is reported, and it is fixed only by reshaping the model and composing again after a yes, inside the two-attempt bound Templates - Flow Mode Section 9 sets
- [ ] Each extension landed where planned and covers no composed node's label
- [ ] Nothing was moved, resized or restyled after the write
- [ ] Every finding below full marks names the label it sits on, where it sits in the frame and one fix, which is a model change composed again after a yes or a named composer limit the writer cannot move

---

## 7. THE DESIGN RUBRIC

The checklists above decide whether a board may ship. The design rubric scores how well it reads, so two boards of the same model, or a board before and after a change, can be compared on something firmer than a glance. Score the overview screenshot on nine criteria, each 0, 1 or 2, for a total out of 18. A criterion scores 2 when it holds everywhere on the board, 1 when it holds with one named exception and 0 when it fails in two places or more.

| Criterion | Scores 2 when |
|---|---|
| Frame and entry | The board is one framed area with a title, a one-sentence subtitle and one obvious place to start reading |
| Reading order | The flow runs in one direction, the main route sits on one straight line and every branch sits beside it rather than across it |
| Colour by meaning | Every colour names a kind the key explains, and nothing is coloured for looks or by position |
| Grouping | Zones, lanes or composite states group what belongs together, each carries a visible name and neighbouring tints differ |
| Legibility | At overview zoom every label reads, no text is cut off or crowded and shapes of one kind share one size |
| Connector clarity | No connector crosses another or runs through a node or a zone title, two edges never lie on one stretch long enough to carry a label, every label sits on its own edge and clear of every other line and every end joins its node cleanly |
| Key and source | The key names every mark and nothing else, and the source line names the sources and what was left out |
| Proportion | The board reads wider than tall or close to square, with no tall strip, no large empty region and margins on the grid |
| Matches the active design | Every kind draws the pair its role names in Assets - Flow Board Design, the title block and type sizes match every other board, the key lists its entries in the design's order with the focus last, every line takes the design's look and no zone tint shares a hue with a kind inside it |

Every score below 2 names the label or the zone it sits on and one fix, in the same shape Section 6 asks of a finding. A comparison between two boards scores both on the same nine criteria and reports both totals, criterion by criterion, so a gain on one criterion never hides a loss on another.

---

## 8. THE REPLY

- [ ] The board URL first, then the `Read-back:` line, then any `Extensions:` and `Left out:` lines, then any `Finding:` lines, then the `HVR self-scan:` line, with no text after it
- [ ] No sentence or key entry ties a colour or a zone tint to a team
- [ ] A mismatch is reported as measured, and the board is never called done on one
- [ ] No HTML, SVG or PNG stand-in was rendered, and a Mermaid block appears only as the checked model a reply with no connector offers
