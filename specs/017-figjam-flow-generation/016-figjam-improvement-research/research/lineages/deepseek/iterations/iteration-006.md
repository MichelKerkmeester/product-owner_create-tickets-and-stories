# Iteration 6: Design-system diagram house style, independent architecture lanes, and a publish manifest

## Focus

Read the diagram-quality and design-system projects — `adobe__spectrum-design-data` (the `spectrum-diagrams` skill and its house style), `figma__architecture-diagram-components`, `hferello__ai` (arch-flow FigJam references) and `ompug__diagram-codebase` (plan, manifest, thresholds) — for layout, colour, density and delivery rules bearing on Q2, and for architecture modelling the packet's lane table may not cover. Builds on iteration 5 finding 3 (edge trace, not counts) and iteration 3 finding 8 (lane table versus real board contents).

## Actions Taken

1. Read `adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md` (workflow, recolor pass, export and embed, guardrails).
2. Read its `references/diagram-house-style.md` (accent discipline, precedence, connectors, layout, one message, review loop).
3. Read `hferello__ai/arch-flow/SKILL.md` and `references/figjam-architecture.md` (doc-first workflow, six-lane rules, allowed edges, link-back).
4. Read `ompug__diagram-codebase/docs/DESIGN.md` (output directory, plan schema, thresholds, witness loop) and the feature and output sections of its README.
5. Read `figma__architecture-diagram-components/README.md` (manual component library).

## Findings

1. Adobe's house style gives the packet a selection procedure its rubric lacks: blue is reserved for "the one node the diagram exists to explain", never assigned by habit or position, at most one per diagram, and if two nodes feel equally important the diagram should be split [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:20], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:22]. The packet's rubric offers a menu of candidates — happy path, riskiest decision, costliest handoff, error state — without a test for choosing one [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:47].
2. Adobe encodes ordering without hue: increasing precedence is shown as a light-to-dark neutral step, not a distinct colour per stage [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:36]. The packet has no equivalent rule for a gantt phase or a process lane that needs ordering, only the one-accent rule [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:31].
3. Adobe says connectors recede: always a dark neutral, never coloured to match an adjacent node, and repetitive edge labels should be dropped — four or more identical labels should become zero or one [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:44], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:50]. The packet allows the accent on happy-path connectors [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:83] and does not check redundant labels, so a process diagram can repeat one edge label on every connector and still pass.
4. Adobe's layout discipline adds three rules the packet has no counterpart for: a header label once per column rather than the phase name repeated in every node, consistent node size and corner radius inside one diagram, and parallel chains sharing alignment so they read as restatements of one pattern [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:56]. The packet's process lanes name work handlers but have no column-header rule [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/process.md:58].
5. Adobe requires one message per diagram and a one-sentence figure caption, and anything that does not serve that sentence is cut, including "for completeness" nodes [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:69]. The packet asks for the reader's question before drawing [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:75], but never asks for the caption or uses it as a cut test in the reply.
6. Adobe enforces cross-diagram consistency on a shared board — same corner radius, type treatment, connector weight and accent discipline — so a reader does not notice that diagram 5 differs from diagram 2 [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:76]. The packet supports several diagrams on one board through fileKey reuse [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:183], but its rubric and reply are per-diagram only.
7. Adobe closes the loop the packet leaves open after the write: a bounded `diagram-critic` pass on the Mermaid source plus a screenshot, checking clutter, hierarchy, accent misuse, redundant labels and whether the caption matches the canvas, applied in one batch and then stopped [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:82]. The packet's post-write check is a read-back count, with no critic pass [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:228].
8. Adobe adds a delivery target the packet forbids: export a high-resolution screenshot, compute each diagram's bounding box from board coordinates, crop per diagram, normalize the near-white FigJam canvas to white, and embed the image with real alt text in a published article [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md:98], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md:113], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md:117]. The packet forbids rendering the diagram as an image or leaving any file behind [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:203], so a Doc that needs an inline figure has no route.
9. `hferello__ai` independently corroborates the packet's architecture lane table: only `flowchart LR`, every node inside one of `client`, `gateway`, `service`, `datastore`, `external`, `async`, dotted edges for async and external, never connecting to a subgraph id, and one independently deployable unit per node [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/arch-flow/references/figjam-architecture.md:8], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/arch-flow/references/figjam-architecture.md:10], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/arch-flow/references/figjam-architecture.md:12], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/arch-flow/references/figjam-architecture.md:16], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/arch-flow/references/figjam-architecture.md:41]. The packet's checker goes further by machine-checking the same table, lane count and cycles [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:47], [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:266], [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:319].
10. `hferello__ai` supplies the Doc integration pattern Q4 needs: the markdown `arch-flow.md` is the source of truth, the diagram is optional and never blocks the doc, node labels must match the ASCII boxes and pseudocode, the returned board link is written back under a `## Visual diagram` heading, and a missing MCP tool means finish the doc and tell the user [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/arch-flow/SKILL.md:153], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/arch-flow/SKILL.md:166], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/arch-flow/SKILL.md:168], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/arch-flow/SKILL.md:170], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/arch-flow/SKILL.md:173]. The packet's only product is the board; it has no doc-side link-back [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:221].
11. `diagram-codebase` runs the packet's gate as a durable artifact: a plan with a purpose sentence per diagram and a content hash [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/docs/DESIGN.md:157], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/docs/DESIGN.md:175], a `publish/review.md` listing exactly what will leave the machine [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/docs/DESIGN.md:59], and a `manifest.json` with phases, per-diagram status, Figma ids and the pending action [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/docs/DESIGN.md:60]. The packet's gate is a spoken message and its reply has no run manifest, so a resumed session cannot tell which nodes it wrote.
12. `diagram-codebase` documents readable thresholds between the packet and Figma: 25 nodes and 30 edges per diagram, a master diagram of 12–20, nesting at most two, and oversized diagrams split with every omission listed in the diagram's notes rather than truncated silently [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/docs/DESIGN.md:192], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/docs/DESIGN.md:193]. The packet's 9-node cap is the strictest of the three sources, and its `Left out:` line is the only omission record [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:77].
13. `figma__architecture-diagram-components` is a manual community component library, not generated guidance: it offers owned-versus-external service variants and icon overlays that `generate_diagram` cannot express [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__architecture-diagram-components/README.md:23]. It marks the boundary of what a generated architecture can show, and the packet should not promise ownership variants it cannot draw.

## Questions Answered

- Q2: Which layout, colour, density and board-quality measurement practices in the corpus exceed the packet's style guide, quality rubric and manual-testing scorecard?

  Answer: layout — a 4px board grid, paired type roles, one direction, column headers instead of repeated phase labels, parallel-chain alignment, and cross-diagram consistency on a shared board; colour — a selection test for the single accent, neutral light-to-dark for ordering, connectors that recede, and a redundant-edge-label rule; density — independent thresholds of about 20–25 nodes and 25–30 edges with split-with-notes, against the packet's 9; measurement — a bounded post-write critic pass, a publish review artifact and a run manifest, while the packet's seven-dimension 0–2 scorecard remains the only scored instrument in the corpus.

## Questions Remaining

- Q3: read-back, revision, fileKey reuse, failure/retry, delivery (delivery now has corpus evidence; revision and retry still need the routing and execution surfaces).
- Q4: request routing and artifact handoff.
- Q5: claude.ai kernel without a Figma connector, and ClickUp.

## Ruled Out

- Adopting Adobe's full export-and-embed pipeline inside Flow Mode: it conflicts with the packet's no-file rule and needs a site build; it belongs to a Doc or publication route, not to the board reply.
- Treating the architecture component library as a rule source: it is a manual asset library, and its variants cannot be generated.

## Dead Ends

- No dead end. The component library was thin on rules but useful as a capability boundary.

## Edge Cases

- Contradictory evidence: the packet allows the accent on connectors, Adobe says connectors always recede to a dark neutral. The conflict is recorded; the packet's version is defensible for a happy-path emphasis, but its redundant-label gap is not.
- Ambiguous input: none.
- Missing dependencies: none.
- Partial success: none.

## Sources Consulted

- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/arch-flow/SKILL.md
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/arch-flow/references/figjam-architecture.md
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/docs/DESIGN.md
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/README.md
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__architecture-diagram-components/README.md

## Assessment

- New information ratio: 0.88
- Questions addressed: Q2, Q3, Q4
- Questions answered: Q2

## Reflection

- What worked and why: reading Adobe's house style and `diagram-codebase`'s design doc together produced the strongest single improvement of the run so far: the packet verifies counts but never traces edges, and both sources independently insist on clarity over counts. hferello's lane file then corroborated the packet's best machine-checked rule instead of adding a competitor.
- What did not work and why: the component library had almost no textual rules; it cost one read to establish that the generated path cannot express ownership variants.
- What I would do differently: read `diagram-codebase`'s DESIGN before its README, because the schema and thresholds are the transferable part and the feature list only advertises them.

## Recommended Next Focus

Iteration 7: read the integration surfaces — `AI Systems/Product Owner/SKILL.md`, `ROUTER.md`, `hub-router.json`, `mode-registry.json`, `AGENTS.md`, and `sk-product-owner/SKILL.md` with `references/router-contract.md`, `interactive-mode.md` and `task-mode.md` — and trace how a Flow request reaches the packet and hands back to a Story, Epic, Doc, Task or Bug. Builds on iteration 6 finding 10 (doc-first visual diagram link-back) and iteration 5 finding 10 (board-to-Mermaid reverse conversion).
