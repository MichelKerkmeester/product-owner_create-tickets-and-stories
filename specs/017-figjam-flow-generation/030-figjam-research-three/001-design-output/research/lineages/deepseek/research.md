---
title: "Deep Research — FigJam boards that look and read better (deepseek lineage)"
description: "How sk-create-figjam can produce FigJam diagrams that look and read better, layer by layer, with ten ranked changes and a better way to measure board quality. Fan-out lineage synthesis: deepseek."
trigger_phrases:
  - "figjam board legibility"
  - "sk-create-figjam diagram design"
  - "figjam board quality measurement"
  - "figjam multi-diagram board composition"
importance_tier: important
contextType: research
version: 1.0.0.0
---

# FigJam Boards That Look and Read Better

Fan-out lineage `deepseek`, session `fanout-deepseek-1792563734045-6evjmk`. Five iterations, 61 findings, synthesised from `iterations/iteration-001.md` through `iteration-005.md` and their deltas.

The subject is the finished board as a reader meets it: what lands first, what groups with what, how far apart things sit, and whether the reader can tell where to start. The packet under study is `AI Systems/Product Owner/sk-create-figjam/`. The work is a design and output comparison, not an implementation.

---

## 1. Summary

The packet is unusually disciplined where content is concerned and unusually silent where composition is concerned. It refuses to invent a step, caps a decision at three labelled exits, enforces a 40-character label, holds a measured colour record with a self-test, and forbids moving a node the generator drew. Those are real strengths and this research touches none of them.

What it does not have is a vocabulary for the board. It states no gap between two diagrams, no title contract, no glance order, no legend rule for its own shape vocabulary, no density target, and no way to judge whether a board that passes every count has a beginning. The generator owns geometry and the model owns almost nothing geometric, so the packet has concluded — correctly — that layout cannot be redesigned. The missing step is that layout *can be constrained*, and the published sources that build boards for a living say exactly how: fixed spacing bands, a named first glance, a title at a stated size, sections as the grouping and navigation layer, and a two-zoom review that judges the overview before the detail.

Eleven changes are stated below as findings against the packet's own files, and ten are ranked. Three corrections to the packet's stated facts emerged along the way, and one of this lineage's own early findings had to be withdrawn after it collided with prior research.

---

## 2. What the Packet Already Does Better

Named so that nothing good is removed.

- **It says who owns what.** The generator owns layout, the model is how a bad layout is fixed, and the extension layer only ever adds beside or behind. That triad is stated plainly and it holds for every type. [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:164]
- **It refuses to invent.** "A diagram of a real, partial system beats a polished one of an imagined system." A missing step is asked about or named as a gap, never guessed. [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:144]
- **It makes cuts visible.** The `Left out:` line and the provenance table mean a reader can tell what the board omits and why. [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:59]
- **Its colour record is measured, not asserted.** Every palette pair carries a measured text-on-fill and stroke-on-canvas ratio, the departures are recorded with their numbers, and the self-test re-measures both columns and fails on drift. [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:58]
- **It is stricter than Figma's own published guidance on content.** A 40-character label cap where Figma caps nothing, a node budget per type where Figma states none, and a named shape vocabulary where Figma's fallback archetype only asks for distinct fills. [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:160] [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-generate-diagram/SKILL.md:49]
- **Its read-back verifies more about an edge than most tools ever do.** Two endpoint ids, two end caps, a label, and a named "dangling" failure for an edge pinned to the canvas. [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:223]
- **It has two dials set before modelling.** Detail level and audience change the node count and the wording, and they are decided before any writing. [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:148]

---

## 3. Who Owns Each Quality

Iteration 001's inventory, restated as the map every change below uses.

| Quality | Owner today | Steerable by the model? | Notes |
|---|---|---|---|
| Layout direction | The model | Yes, per type | `TD`/`LR` for user flow and process; `LR` only for architecture; `LR`/`TB` for state; generator picks the gantt axis unit [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:38] [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/architecture.md:78] |
| Node size, node gap, font size | `generate_diagram` | No | "The generator sets FigJam's font, and the tool cannot change it afterwards" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:128] |
| Grouping | The model, per type | Partly | Architecture lanes, 2-6 process lanes, gantt sections; no subgraph in a user flow [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/process.md:72] |
| Colour | Model for two types, extension for four | Partly | Architecture takes no colour; sequence, state and ER lose Mermaid styling [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:48] |
| Title | Extension, optional | No | A text node 64px above the diagram, only when the gate named an extension [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:150] |
| Legend, pins, stickies, tints | Extension | No | Four recipes, all additive [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:62] |
| Board composition | Nobody | No | No rule for gaps, headings or order between diagrams |

The one thing Figma's own diagram skill adds to this map is confirmation: "If the diagram looks cramped or tangled, the fix is better Mermaid, not manual repositioning via `use_figma`." [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-generate-diagram/references/workflow.md:148]

---

## 4. Layout Direction and Spacing

**Direction is already well handled, and the comparators agree with the packet.** Mermaid's own guidance assigns `LR` to "processes, workflows, timelines" and `TD`/`TB` to "hierarchies, org charts, decision trees", and adds that "Direction has a bigger impact on readability than most people expect." [SOURCE: https://mermaid.ai/docs/build-and-edit/write-diagram-syntax] The packet goes further than that, because it varies direction by type and enforces one direction family across every diagram of one flow. [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:60]

**Spacing is the packet's largest unowned surface.** Every measurement it states belongs to the extension layer: 40px of sticky clearance, 32px of section padding, 64px of title clearance, a 250px legend gutter, a 24px tint expansion. [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:101] [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:114] [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:118]

The two comparators use two different spacing languages, and both are needed:

- **Diagram-side (macro/grid):** a minimum gap between nodes of 24 (standard), 40 (presentation) or 24 (print), a 40px outer margin and a 60px legend strip. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/foundations/output-spec.md:79] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/foundations/output-spec.md:65]
- **Board-side (relationship):** 60-92px means the same thought, 200-400px means a different topic, 1000px+ means a different part of the board. [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-use-figjam/references/plan-board-content.md:42] And within a composed board: 16-32px inside a text stack, 32-48px of card padding, 60-92px between peers, 160-240px between distinct groups, with the rule that "Unrelated groups should never be closer than the text blocks inside a card." [SOURCE: research/corpus/prasantloki__figjam-builder/references/composition-grammar.md:25]

A published design source names why both exist: whitespace is either macro or micro, and the balance between positive and negative space is "essential to create a functional and esthetic diagram", where micro whitespace is "small pieces of space between shapes, lines, titles, icons". [SOURCE: https://learning.dell.com/content/dam/dell-emc/documents/en-us/2015KS_Pantyukhin-Principles_of_Design_Diagramming.pdf]

So the packet can never measure a node gap, and it can state, today, the board-side bands and the relationship rule that make a grouping legible.

---

## 5. Grouping and Sections

**Grouping is currently a type property rather than a design decision.** It exists as architecture lanes (six fixed lanes), process lanes (`subgraph`, 2 to 6, never nested) and gantt sections; a user flow forbids `subgraph` outright. [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/architecture.md:42] [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/process.md:72] [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:55]

**The section clause is right for the wrong reason, and the reason matters.** The packet says "A section never wraps a generated node, because adding a node to a section moves it." [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:148] Figma's own generation block shows the deeper problem: wrapping a generated diagram in a section means collecting every page-level node and deleting and recreating each connector. [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-use-figjam/references/position-figjam-nodes.md:85] That would replace the very connectors the read-back verifies, so the prohibition is protecting the verification contract, not just the coordinates.

This is where this lineage corrected itself. Iteration 004 argued that Figma's "Create section from selection" affordance lets a finished diagram be grouped with no node moving. That affordance is a **human UI action**; the plugin API route still reparents, and the earlier `016` research had already rejected section-wrapping for exactly the connector reason. [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/research.md:216] The withdrawal is recorded in Section 13.

What survives is narrower and still useful: a section is Figma's documented grouping, hiding, deep-linking and screen-reader navigation structure, and a **section title is a first-class label** that can name a diagram without touching the diagram. [SOURCE: https://help.figma.com/hc/en-us/articles/4939765379351-Organize-your-FigJam-board-with-sections] [SOURCE: https://help.figma.com/hc/en-us/articles/14477101678359-Create-accessible-FigJam-boards]

---

## 6. Hierarchy and the First Glance

The packet's one-accent rule is the strongest hierarchy rule it has: at most one accent, on "the node a reader would keep if they could keep only one", and "Shape and label carry the meaning on their own, so the diagram reads in greyscale". [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:49]

It is scoped to a diagram and it only half-exists, because the rule says what to emphasise and nothing about what to quieten. The comparator's formulation is complete: "Deliberately de-emphasize secondary and tertiary content. Do not amplify the primary." [SOURCE: .skilled/skills/sk-design/sk-design-fundamentals/references/diagnosis-table.md:47] And the board-level version is a focus budget: "One primary focal object per section. Two or three secondary objects may support it. Everything else should be quieter through smaller scale, lower contrast, simpler containers, or later position", with "position and visual mass first, typography second, and color as reinforcement". [SOURCE: research/corpus/prasantloki__figjam-builder/references/composition-grammar.md:17]

The glance order is the concept the packet lacks entirely, and it is cheap: "First glance: the one claim, decision, or object that should win within two seconds. Second glance: the evidence or relationship that advances the argument. Last glance: risks, metadata, appendix…". The same source names the failure mode a title recipe invites: "Repeating the primary sentence in both a board title and a hero card creates two focal objects for one idea." [SOURCE: research/corpus/prasantloki__figjam-builder/references/composition-grammar.md:5]

---

## 7. Colour Roles, Palette and Contrast

The palette work needs no change and should be cited as the model to copy: light fills with charcoal text measure 11.21:1 to 14.61:1, seven strokes are recorded as sitting under the 3.0:1 mark gate, and each departure carries its number. [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:66] [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:115]

Two gaps remain.

1. **The status tint has one channel where it needs two.** The recipe paints a rounded rectangle behind a group in the accent pair's colours. [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:118] Public accessibility guidance is explicit: colour should be used "in combination with labels or line styles so that any difference can be accessible to all users". [SOURCE: https://www.ibm.com/design/language/infographics/technical-diagrams/design/] The dash vocabulary the comparator already uses for optional and security nodes is available and unused. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/foundations/style-guide.md:143]
2. **Four of seven types cannot carry hierarchy in colour or shape at all.** Architecture assigns colour by lane and refuses model styling; sequence, state and ER strip it. [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:48] The packet should say so per type, because the reader's next question — "then where does the emphasis come from?" — is answered only by the extension layer.

---

## 8. The Shape Vocabulary

The user flow is the packet's best-designed type: four shapes, each meaning exactly one thing, a decision with 1 to 3 labelled exits, and a merge dot that carries no words. [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:40] That is a stronger vocabulary than most published diagram guidance, which stops at "distinct fills per node type". [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-use-figjam/references/plan-board-content.md:339]

The gap is coverage, not quality: sequence, ER, state and gantt draw every node of a kind identically, so a reader gets no shape signal. The packet never says which types are in that position, which means an operator cannot tell whether a flat board is a defect or the only thing the type allows.

---

## 9. Connector Routing and Labels

The comparator's five mandatory connector rules are orthogonal elbows, a 6-10px label gap with an opaque mask, no shared stroke paths, fanned attach points at least 12px apart, and no route behind a non-endpoint box. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:291] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:294] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:295] The packet has one proxy: the scorecard counts crossings. [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md:81]

Because the generator routes, four of the five are not steerable. Three model-side causes remain available and unstated:

- **Long connector labels inside a dense rank** — the label collides before the route does.
- **Two edges between the same pair of nodes** — a shared trunk by construction.
- **Declaration order that forces a long reach** — node order influences placement but is "subservient to the line crossing objective". [SOURCE: https://line9.ai/mermaid/layout]

The corpus adds the judgment rule the scorecard needs: "Judge connector crossings from the rendered screenshot; a connector bounding box does not describe its path", and "Avoid shared trunks when they make edge ownership ambiguous". [SOURCE: research/corpus/prasantloki__figjam-builder/references/composition-grammar.md:98]

---

## 10. Density, Titles, Legends and Text

**Density is a node count, not a density.** The packet caps at 9 nodes and 12 connectors generally, 9 nodes for a user flow, 12 tasks with 5 parallel bars in a gantt section. [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:162] The comparator carries a target as well as a ceiling — "density at target 4/10 — enough to be technically complete, not so dense it needs a guide" — so 2/10 and 9/10 currently pass the same check. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:264]

**Titles.** Figma requires an entry point: "Board title (60-96px) at top-left, clearly visible at overview zoom." [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-use-figjam/references/plan-board-content.md:82] The packet's title node matches the position and neither the scale nor the default, and Figma's own diagram skill treats a title block as ordinary extension work that needs no inspection. [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-generate-diagram/references/workflow.md:70]

**Legends.** The comparator requires "Legend covers every type used — and nothing extra". [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:358] The packet's legend covers annotations only, and its sticky column runs at a 32px gap where Figma's own sticky grid uses 64px between fixed 240×240 stickies. [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:103] [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-use-figjam/references/plan-board-content.md:254]

**Text.** Size is fixed by the generator; the only levers are the 40-character cap and the two extension type sizes (the pin digit, the title node). The transferable rule is that a rendered size is a function of viewing distance: "Viewing distance overrides the nominal preset", and the reviewed overview is normalised to 1200px with rendered targets of 44-56px for a board title and 13-18px for body text. [SOURCE: research/corpus/prasantloki__figjam-builder/references/typography-grammar.md:24] [SOURCE: research/corpus/prasantloki__figjam-builder/references/typography-grammar.md:38]

**Several diagrams on one board.** The packet reuses the `fileKey` so the work stays on one board and tags each node with the diagram's name for a later session. [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:187] It states nothing about where the second diagram lands, how far from the first, what it is called, or which one a reader meets first. Figma's board skill supplies all of it by construction: one outer board section, one zone section per diagram, `siblingGapH: 92`, `siblingGapV: 120`. [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-use-figjam/references/plan-board-content.md:117]

**One factual correction.** The packet says "A FigJam file has one page and no write can add another". The second half is true — `figma.createPage()` throws in FigJam. The first half is not: "FigJam files can contain multiple pages… There is no limit to the amount of pages you can create in FigJam", recommended for separate work streams, recurring meetings, divider pages and smaller board sizes. [SOURCE: https://help.figma.com/hc/en-us/articles/24005082123159-Create-and-manage-pages-in-FigJam] [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:65]

---

## 11. Ranked Changes

Ten changes, ranked by effect on how a board reads per unit of change risk. Each names the Product Owner file it changes and the source it comes from. None re-proposes an implemented change from `009-figjam-skill-research` or `016-figjam-improvement-research`.

### Rank 1 — Put a title and a written glance order on every write

- **Files:** `references/hybrid-workflow.md` (Section 3), `references/flow-mode.md` (Section 2 step 7 gate and Section 8 delivery), `references/quality-rubric.md`.
- **Change:** a title is emitted with every diagram, not on request, at the board skill's 60-96px scale rather than a default text node, and it is the same string as the generator's `name`. Before modelling, three lines are written — first, second, last glance — and carried into the gate, so the accent decision has a target and the reply can state what should win. The title carries the claim only if the diagram does not already; the two never repeat each other.
- **Comes from:** [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-use-figjam/references/plan-board-content.md:82] [SOURCE: research/corpus/prasantloki__figjam-builder/references/composition-grammar.md:5] [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-generate-diagram/references/workflow.md:70] Also iteration 001 finding 4 and iteration 002 finding 8.
- **Why first:** it is two sentences and one call argument, it touches every diagram of every type, and it gives every later change a target to measure against.
- **Effort:** small.

### Rank 2 — Give the board a spacing scale and a relationship rule

- **Files:** `references/hybrid-workflow.md` (spacing constants for every recipe), `references/style-guide.md` (new spacing section), `references/quality-rubric.md`.
- **Change:** state the board-side bands once — 60-92px inside one thought, 200-400px between topics, 1000px+ between parts of the board — and the operative rule that unrelated groups are never closer than the text blocks inside a card. Put the legend column on the sticky 64px grid instead of a 32px stack, and replace the fixed 24px tint expansion with the "larger than the group's own internal gap" relationship.
- **Comes from:** [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-use-figjam/references/plan-board-content.md:42] [SOURCE: research/corpus/prasantloki__figjam-builder/references/composition-grammar.md:25] [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-use-figjam/references/plan-board-content.md:254] [SOURCE: .skilled/skills/sk-design/sk-design-fundamentals/references/diagnosis-table.md:50] Also iteration 003 findings 2, 9 and 13 and iteration 004 finding 11.
- **Why second:** "cramped" and "ambiguous grouping" are the two complaints this packet can currently neither diagnose nor answer, and both are spacing relationships it already chooses numbers for.
- **Effort:** small.

### Rank 3 — Compose a multi-diagram board instead of appending to it

- **Files:** `references/hybrid-workflow.md` (new recipe), `references/flow-mode.md` (Section 6 write routes and Section 8 delivery), `AGENTS.md` (delivery).
- **Change:** for a board holding more than one diagram, name the composition: one board-level heading, one zone per diagram placed on the 92px/120px sibling gaps, each zone titled with an ordinal and the diagram's name ("1 · Booking states"), a fixed reading order across the board (context, evidence, asks, appendix), and the relevant zone link in the reply. State plainly that a generated diagram is never reparented into a section, and why: reparenting recreates every connector and breaks the read-back. Offer the wrap-in-a-section hand edit in the reply for a user who wants containment.
- **Comes from:** [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-use-figjam/references/plan-board-content.md:92] [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-use-figjam/references/plan-board-content.md:117] [SOURCE: https://help.figma.com/hc/en-us/articles/4939765379351-Organize-your-FigJam-board-with-sections] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/research.md:216] Also iteration 004 findings 2, 3, 6 and 7.
- **Why third:** it is the only change that answers "how should several diagrams sit on one board", which today has no answer at all, and it reuses gaps Figma already publishes.
- **Effort:** medium.

### Rank 4 — Write down what "better Mermaid" is

- **Files:** `references/flow-mode.md` (Section 5 shared rules) plus a new `references/layout-levers.md`.
- **Change:** replace the general instruction to reshape the model with a lever table: direction; node declaration order (which orders nodes inside a rank, subordinate to crossing minimisation); the edge set (fewer edges per pair, no duplicate edges); and subgraph presence (lanes only, 2 to 6, never nested). State the limits that stop an operator wasting a write: `&` does not group, invisible links are unpredictable, extra-dash length hints are not implemented in ELK, a subgraph direction is ignored when its nodes link outside, and **sibling subgraphs render in reverse declaration order** — so declare lanes in reverse of the intended reading order or verify the order on read-back.
- **Comes from:** [SOURCE: https://line9.ai/mermaid/layout] [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:38] [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/process.md:72] [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-generate-diagram/references/workflow.md:148] Also iteration 004 findings 8, 9 and 10.
- **Why fourth:** the generator leaves exactly one route to a better board, the packet already tells operators to take it, and today nobody can say what taking it means. The lane-reversal note prevents a silent meaning error the read-back cannot catch.
- **Effort:** small.

### Rank 5 — Give the legend a rule, and give tints a second channel

- **Files:** `references/hybrid-workflow.md` (legend and tint recipes), `references/style-guide.md` (line-style channel), `references/quality-rubric.md`.
- **Change:** a legend enumerates the shape vocabulary and any tint or dash encoding the board actually uses, appears by default once a board uses three or more shape kinds, and is laid out as a grid on the sticky rhythm. Group tints encode membership in the stroke dash pattern as well as the fill, so the grouping survives greyscale and colour-blind reading.
- **Comes from:** [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:358] [SOURCE: https://www.ibm.com/design/language/infographics/technical-diagrams/design/] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/foundations/style-guide.md:143] Also iteration 002 finding 7 and iteration 004 finding 12.
- **Why fifth:** it closes the gap between the packet's own vocabulary and its own explanation of that vocabulary, and the dash channel is free because the palette already carries it.
- **Effort:** medium.

### Rank 6 — Add reading distance as the third dial

- **Files:** `references/flow-mode.md` (Section 4, the two dials), `references/types/*.md` (budgets).
- **Change:** keep detail level and audience, and add reading distance: compute the review scale from the board's own width or height, then let it set node count and label length, so a board meant for a wall gets fewer nodes rather than type the reader cannot resolve. State that this is the only route to the comparator's reading-distance rule, because the generator's font cannot be changed afterwards.
- **Comes from:** [SOURCE: research/corpus/prasantloki__figjam-builder/references/typography-grammar.md:24] [SOURCE: research/corpus/prasantloki__figjam-builder/references/typography-grammar.md:38] [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/foundations/output-spec.md:81] Also iteration 002 finding 10 and iteration 003 finding 10.
- **Why sixth:** it turns a dial the packet believes it does not have into one it can compute, but it only bites on boards read at distance, so it ranks below the universal changes.
- **Effort:** medium.

### Rank 7 — Measure the graph before the write, not after

- **Files:** `scripts/flow_check.py`, a new `scripts/figjam_checks/layout.py`, `references/quality-rubric.md`.
- **Change:** report, beside the existing node and connector counts, the numbers that predict a poor layout: rank width (the widest level), fan-out per node, edges per node, longest path, total label characters against the 40-character cap, and an estimate of edge pairs that must cross. Split or re-rank in the model when a number is out of band, instead of discovering the problem from a screenshot after a write has been spent.
- **Comes from:** [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:100] [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/common.py:21] [SOURCE: https://github.com/openai/plugins/blob/main/plugins/build-web-data-visualization/skills/node-link-and-diagram-layout/SKILL.md] Also iteration 002 finding 5 and iteration 004 finding 13.
- **Why seventh:** it is the only change that makes density judgeable rather than capped, but it needs script work and a rule set, so it ranks below the text changes.
- **Effort:** medium to large.

### Rank 8 — Rebuild the scorecard around what a reader experiences

- **Files:** `manual-testing-playbook/manual-testing-playbook.md` (Section 3), `manual-testing-playbook/board-quality/*.md`, `references/quality-rubric.md`.
- **Change:** add a Composition dimension; replace Clarity's three content questions with a planned-versus-actual glance-order test ("what wins first, second, last?" scored against the Rank 1 plan); split Hygiene into its four atomic invariants so one failure cannot hide three; score crossings, shared trunks and label collisions separately; and require a location and a fix for every lost point, in the shape the review contract already uses. Keep the existing floor-plus-mandatory-dimensions structure, and make Composition one of the mandatory dimensions.
- **Comes from:** [SOURCE: research/corpus/prasantloki__figjam-builder/references/composition-grammar.md:106] [SOURCE: research/corpus/prasantloki__figjam-builder/references/composition-grammar.md:98] [SOURCE: .skilled/skills/sk-design/sk-design-fundamentals/references/review-checklist.md:17] Also iteration 001 finding 11, iteration 002 finding 9 and iteration 005 findings 1 to 6.
- **Why eighth:** it changes how every other change is judged, which is a large effect, but it only pays off once the packet has something to score (Ranks 1 to 5).
- **Effort:** medium.

### Rank 9 — Correct the page sentence and give the board a size decision

- **Files:** `references/flow-mode.md` (Section 6).
- **Change:** say that a plugin cannot add a page while a person can, so a board that outgrows one canvas is an operator decision — a second page or a second file — rather than something the write path refuses. Keep the rule that a page is never a write target.
- **Comes from:** [SOURCE: https://help.figma.com/hc/en-us/articles/24005082123159-Create-and-manage-pages-in-FigJam] Also iteration 004 finding 1.
- **Why ninth:** it is one sentence and prevents a wrong reason being repeated, but it changes no behaviour.
- **Effort:** small.

### Rank 10 — Keep the score as a series, with a scored reference board

- **Files:** `manual-testing-playbook/manual-testing-playbook.md` (evidence requirements), new `manual-testing-playbook/benchmark-reports/` convention.
- **Change:** record each scored board with a date, the scenario id, the model and its digest, the scorecard with per-dimension reasons and locations, and the screenshots, so a regression is a diff rather than an opinion. Keep one scored reference board per type as the anchor a rendered-size or density judgment is made against.
- **Comes from:** [SOURCE: .skilled/skills/sk-design/sk-design-diagram/benchmark/reports/README.md] [SOURCE: research/corpus/prasantloki__figjam-builder/references/typography-grammar.md:24] Also iteration 005 findings 7 and 9.
- **Why tenth:** it is infrastructure: it makes Ranks 1 to 8 provable over time, but it produces no improvement on its own.
- **Effort:** medium.

---

## Eliminated Alternatives

- **Replacing the generator's layout.** The comparator's rule — "NEVER reproduce a Mermaid renderer layout; automatic spacing and routing are replaced, not copied" — cannot apply here: `generate_diagram` is the only route for architecture, and four types depend on its grid or its lifelines. [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:279] [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/architecture.md:16] The transferable intent, that automatic spacing must respect grouping, survives as Rank 2.
- **Reparenting a generated diagram into a section.** Rejected in prior research for the connector reason and re-confirmed here: reparenting deletes and recreates every connector, which invalidates the read-back the packet relies on. [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/research.md:216] Rank 3 composes boards beside diagrams instead.
- **Re-adding the 4px grid, node-size and type-ramp tokens.** They govern a renderer the packet does not own; the packet records the omission deliberately and calls it "what did not translate". [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:128] Rank 6 replaces their hierarchy role instead.
- **Re-adding the horizontal legend strip and the `viewBox` expansion.** A board has no `viewBox`; the board-native form is a legend group, which Rank 5 sizes.
- **Using `&` or invisible links as grouping syntax.** Mermaid documents that `&` does not group and that invisible links move nodes unpredictably. [SOURCE: https://line9.ai/mermaid/layout]
- **Treating Figma's board-content skill as an alternative to the packet.** It explicitly routes flowcharts, architecture, sequence, state and ER away from itself, so it is the board layer the packet lacks. [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-use-figjam/references/plan-board-content.md:30]
- **A floating-point quality score.** A decimal built from seven judgements reads as precision the evidence cannot support; the existing floor-plus-mandatory-dimensions shape is kept.
- **Adopting the 1200px overview normalisation as a literal constant.** It assumes a wrapper the packet does not own; the method survives in Rank 6, the constant does not.

## Divergence Map

- **Saturated directions:** none. Convergence was switched off (`convergenceMode: off`) and the stop policy was `max-iterations`, so every iteration was run to the cap by design rather than stopped early.
- **Pivots taken:** none. The five iterations widen in a planned order — packet, comparator, corpus, public guidance and board composition, measurement — and each names the earlier iteration it builds on, so the lineage is a chain rather than a set of branches.
- **Pivot failures and audited overrides:** none.
- **Remaining frontier:** three directions were opened and left for a later run. (1) Whether the hosted generator can write inside a locked section, and what it does when the target region is locked — unobserved, so no change is ranked on it. (2) Whether a section placed behind a diagram as a tinted backdrop (without containment) reads as a group to a sighted reader and to a screen reader — the accessibility benefit of a section depends on containment, so the visual and the assistive readings may diverge. (3) Whether the `fj` route can carry a title or a legend at all, since it has no container or table verb and the packet currently gives it no extension layer.

---

## 12. Open Questions

1. **Does the hosted generator respect a locked section?** No source states what `generate_diagram` does when the target region is locked, and the packet forbids claiming an unobserved generator behaviour. Until it is observed, no composition change may depend on it.
2. **Is a non-containing section any use?** A section placed behind a diagram without containing it is just a tinted rectangle; it may help a sighted reader and do nothing for a screen reader. Worth one test before it is recommended.
3. **Can the `fj` route carry a title or a legend?** `fj` has no layout, container or table verb, so Ranks 1, 2 and 5 have no expression on that route today.
4. **What is the right density target for a board versus a diagram?** The comparator's 4/10 is a diagram target; a board holding six diagrams has a second density question nobody has stated.
5. **Does a numbered section title help or clutter a single-diagram board?** Rank 3 assumes ordinals only pay off across diagrams; that is untested.

---

## References

**Product Owner packet**
- `AI Systems/Product Owner/sk-create-figjam/SKILL.md`
- `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md`
- `AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md`
- `AI Systems/Product Owner/sk-create-figjam/references/style-guide.md`
- `AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md`
- `AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md`, `process.md`, `architecture.md`, `state.md`, `gantt.md`
- `AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py`, `scripts/figjam_checks/common.py`
- `AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md` and `board-quality/user-flow-board-quality.md`

**Design comparators**
- `.skilled/skills/sk-design/sk-design-diagram/SKILL.md`, `references/foundations/output-spec.md`, `references/foundations/style-guide.md`, `references/catalog.md`, `benchmark/reports/README.md`
- `.skilled/skills/sk-design/sk-design-fundamentals/references/hierarchy.md`, `color-system.md`, `depth-and-detail.md`, `review-checklist.md`, `diagnosis-table.md`

**Corpus (22 repos; these used)**
- `research/corpus/lightspeedwp__.github/plugins/figma/figma-use-figjam/references/plan-board-content.md`, `position-figjam-nodes.md`
- `research/corpus/lightspeedwp__.github/plugins/figma/figma-generate-diagram/SKILL.md`, `references/workflow.md`
- `research/corpus/prasantloki__figjam-builder/references/composition-grammar.md`, `typography-grammar.md`
- Read and not used (no design claims): `tmcw__figjam-mermaid`, `memi-design__mermaid-jam`, `lauragalera__figjam-erd-plugin`, `rrichardsonv__parse-figjam`, `ecestnrkl__figjam-mcp`

**Public sources**
- https://help.figma.com/hc/en-us/articles/4939765379351-Organize-your-FigJam-board-with-sections
- https://help.figma.com/hc/en-us/articles/24005082123159-Create-and-manage-pages-in-FigJam
- https://help.figma.com/hc/en-us/articles/14477101678359-Create-accessible-FigJam-boards
- https://mermaid.ai/docs/build-and-edit/write-diagram-syntax
- https://line9.ai/mermaid/layout
- https://www.ibm.com/design/language/infographics/technical-diagrams/design/
- https://learning.dell.com/content/dam/dell-emc/documents/en-us/2015KS_Pantyukhin-Principles_of_Design_Diagramming.pdf
- https://www.lasssim.com/wp-content/uploads/2022/06/WeAreDevelopers_Lasselsberger_Simon_220610.pdf
- https://github.com/openai/plugins/blob/main/plugins/build-web-data-visualization/skills/node-link-and-diagram-layout/SKILL.md

**Prior research built on**
- `AI Systems/Product Owner/specs/017-figjam-flow-generation/009-figjam-skill-research/research/research.md`
- `AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/research.md` (sections 1 to 9, including its rejected section-wrapping idea)

---

## Convergence Report

- **Stop reason:** `maxIterationsReached`
- **Total iterations:** 5 of 5 (`stopPolicy: max-iterations`)
- **Questions answered:** 5 of 5 key questions
- **Remaining questions:** 5 carried as Section 12 open questions, all narrow verification items rather than unexamined territory
- **Convergence threshold:** 0.05, `convergenceMode: off` — the ratio is telemetry only for this run
- **New-information ratio by iteration:** 1.00, 0.92, 0.95, 0.93, 0.80
- **Findings by iteration:** 12, 12, 14, 13, 10 = 61
- **Last three iteration summaries:** run 3 — corpus and Figma's own board numbers (0.95); run 4 — board composition, public guidance and one factual correction (0.93); run 5 — measurement, ranked changes (0.80)
- **Divergence summary:** no divergent pivots recorded; the lineage is a widening chain, and the frontier is recorded in the Divergence Map
- **Corrections recorded:** the packet's one-page claim (iteration 004 finding 1), and this lineage's own iteration 004 finding 2 withdrawn after it collided with the prior `016` research's rejected section-wrapping idea
- **Segment transitions, wave scores and checkpoint metrics:** experimental and omitted from the live report
