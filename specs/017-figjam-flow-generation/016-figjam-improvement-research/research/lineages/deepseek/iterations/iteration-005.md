# Iteration 5: FigJam builders and converters — board-quality grammars, extra diagram kinds, and the reverse round trip

## Focus

Read the FigJam builders and converters — `prasantloki__figjam-builder`, `tmcw__figjam-mermaid`, `memi-design__mermaid-jam`, `lauragalera__figjam-erd-plugin` and `bluescaban__blueprints` — and compare their build, parse and round-trip models with the packet's model-first, write-once flow. Builds on iteration 4's read-back and diff findings and on iteration 3's type coverage.

## Actions Taken

1. Read `prasantloki__figjam-builder/SKILL.md` in full (design principles, palette tiers, construction rules, audit pass, large-board reading ladder, diagram guidance).
2. Read `memi-design__mermaid-jam/README.md` (supported inputs, controls, update behaviour) and listed its examples.
3. Read `tmcw__figjam-mermaid/README.md` (reverse conversion scope and limits).
4. Listed `lauragalera__figjam-erd-plugin` and `bluescaban__blueprints` surfaces; their detailed rules were not read because the iteration's remaining budget went to the builder grammar.

## Findings

1. `figjam-builder` states the limitation the packet's layout rule assumes but never argues: generative diagram tools optimise for compactness, not breathing room, so "when the flow matters, hand-build it or accept the limitation" [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:46]. The packet answers the same problem by forbidding moves and splitting the model [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:164], but has no hand-built escape hatch for a flow whose spatial relationships carry the argument.
2. `figjam-builder` has a board-quality grammar the packet lacks at diagram scale: eleven design principles, three palette tiers with a job per tier (accent for marks, vibrant for signal, muted for zones), paired type roles rather than a size ramp, and a fourteen-item audit pass [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:26], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:154], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:359]. The packet's one-accent rule is a diagram-specific subset of that system [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:31].
3. The audit pass contains the check that most directly improves the packet's read-back: "trace every required edge source-to-target in the screenshot; neither a connector count nor a collision-free bounding box proves clarity" [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:323], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:371]. The packet's `Read-back:` line is exactly a count plus a connector comparison, so it can pass a board whose arrows route ambiguously [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:224].
4. `figjam-builder` documents a concrete large-board reading ladder: `get_figjam` with images first; if text is illegible or the call times out, read child IDs only, then metadata in batches of about 30, then screenshot 4–6 nodes in parallel, halving the batch on a timeout [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:378], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:382], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:395], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:412]. The packet's rule to read node by node and never whole-board is the opposite first move, and it has no timeout or batch rule [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:68].
5. `figjam-builder` documents a plugin-API trap the packet's extension path will hit if it ever wraps a diagram in a section: a child's `x`/`y` are section-local, so adding `section.x` doubles the offset and pushes content outside the section [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:237], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:248]. It also documents `upload_assets` with a five-per-call limit and ten-minute expiry [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:274].
6. Two independent corpus sources converge on the same board constants — 4px spacing multiples, Inter only, a white wrapper section, tight clusters of 60–92px, loose 200–400px, zone breaks at 1000px+ [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:131], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:135], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills-figquery/figma-use-figjam/references/plan-board-content.md:17]. The packet has none of these numbers because it never places a board wrapper, which is precisely what an extension beside a diagram needs.
7. `mermaid-jam` exposes diagram kinds the packet cannot draw: journey, mindmap, timeline, and markdown user-flow notes, with sequence flattened into interaction cards and explicit diagnostics for pie, gantt, ERD and class [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/memi-design__mermaid-jam/README.md:32], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/memi-design__mermaid-jam/README.md:37], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/memi-design__mermaid-jam/README.md:44]. This is the first corpus evidence that public FigJam work covers more kinds than the hosted generator, so the packet's nearest-type answer is a real capability gap rather than a generator limit [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:93].
8. `mermaid-jam` keeps a revision model the packet lacks: it preserves manually moved node positions during updates when IDs match, and offers a rules-based "Revise" cleanup for rough Mermaid or markdown source [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/memi-design__mermaid-jam/README.md:27], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/memi-design__mermaid-jam/README.md:86]. The packet forbids moving generated nodes at all and has no automated model cleanup beyond "fix or split" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:238].
9. `mermaid-jam` gives line-level diagnostics before generation and always contains its output in a FigJam section [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/memi-design__mermaid-jam/README.md:28], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/memi-design__mermaid-jam/README.md:30]. The packet matches the diagnostics and exceeds them with a rule check, but has no section wrapper, which is why its diagrams cannot be moved as one unit later.
10. `tmcw__figjam-mermaid` runs the reverse direction the packet never runs: stickies and connectors on a board become a Mermaid flowchart, with arrow styles except a filled triangle, and it explicitly does not yet support other element kinds or selection-only export [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/tmcw__figjam-mermaid/README.md:3], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/tmcw__figjam-mermaid/README.md:9]. For the Product Owner, that is the bridge from a board back into a Doc or a Story, and the README's support list names its fidelity limit.
11. The packet's measured contrast gate remains stronger than the corpus palette systems: `figjam-builder` gives hex values and tiers but no contrast measurement, and it permits vibrant fills for signal [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:157], while the packet records a 4.5:1 text gate, a 3.0:1 mark gate and its departures [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:105]. Nothing in the corpus should displace the packet's measurement.

## Questions Answered

- Q1: Which diagram types, diagram kinds and model rules does the public FigJam/Figma corpus expose that the packet's seven types do not cover?

  Answer: the corpus adds no drawable Mermaid kind beyond the packet's five headers, but it does expose three kinds the hosted generator cannot draw and that a FigJam plugin builds natively — journey, mindmap and timeline — plus markdown user-flow notes and a sequence-to-cards flattening, so the packet's nearest-type answer loses real capability rather than merely redirecting an impossible request.

## Questions Remaining

- Q2: layout, colour, density and board-quality measurement.
- Q3: read-back, revision, fileKey reuse, failure/retry, delivery.
- Q4: request routing and artifact handoff.
- Q5: claude.ai kernel without a Figma connector, and ClickUp.

## Ruled Out

- Adopting `figjam-builder`'s vibrant palette tiers for diagram fills: its vibrant tier is for board signal sections and stickies, while the packet's diagram fills are governed by a measured contrast gate that the vibrant values would fail.
- Treating `tmcw__figjam-mermaid` as a full read-back: it reads stickies and connectors only, so it cannot verify shapes, sections, tables or labels.

## Dead Ends

- `lauragalera__figjam-erd-plugin` and `bluescaban__blueprints` were listed but not read; their ERD and flow-export surfaces are candidates for a later iteration, not dead ends. The iteration spent its remaining budget on the builder grammar because it bears directly on Q2.

## Edge Cases

- Ambiguous input: none.
- Contradictory evidence: the packet says read node by node and never whole-board, while two corpus sources say get_figjam first and escalate. Both are recorded; the corpus rule fits a small generated diagram, the packet rule fits a large existing board.
- Missing dependencies: none.
- Partial success: two of five repos were only listed. Recorded here rather than presented as read.

## Sources Consulted

- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/memi-design__mermaid-jam/README.md
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/tmcw__figjam-mermaid/README.md
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/lauragalera__figjam-erd-plugin (listing)
- specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/bluescaban__blueprints (listing)

## Assessment

- New information ratio: 0.86
- Questions addressed: Q1, Q2, Q3
- Questions answered: Q1

## Reflection

- What worked and why: reading `figjam-builder` whole was worth the budget because its audit pass supplied the missing post-write standard — trace every edge, not just count connectors — and its palette tiers gave the corpus's clearest account of why the packet's one-accent rule is a subset rather than a competitor. `mermaid-jam`'s supported-input list answered Q1 directly.
- What did not work and why: two repos were only listed. Their names promised diagram-specific rules, but the builder grammar was more directly relevant to the open questions, so the reads were deliberately deferred rather than skipped silently.
- What I would do differently: read the ERD plugin before the builder grammar if Q1 were still open, since it is the only ERD-specific public tool in the corpus.

## Recommended Next Focus

Iteration 6: read the diagram-quality and design-system projects — `adobe__spectrum-design-data`, `figma__architecture-diagram-components`, `hferello__ai` (arch-flow FigJam references) and `ompug__diagram-codebase` — for layout, colour and density rules that bear on Q2, and for architecture-specific modelling the packet's lane table may not cover. Builds on iteration 5 finding 3 (edge trace, not counts) and iteration 3 finding 8 (lane table versus real board contents).
