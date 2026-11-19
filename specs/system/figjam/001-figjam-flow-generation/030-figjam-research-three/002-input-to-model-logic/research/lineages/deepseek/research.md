# Turning screenshots, Figma files and product logic into a correct FigJam model

This synthesis covers the five-iteration DeepSeek lineage `fanout-deepseek-1792563734045-dk52ro`, which ran `cli-pi` at `deepseek-v4.1-flash` with maximum reasoning. The lineage asked one question: how can the AI most reliably turn screenshots, Figma flows and product logic into a correct FigJam model? It studied only the input half — extraction, inference, merging, provenance, gap marking, type choice, chunking and the check against sources — and left the write path, the read-back and the reply alone, because phases 009 and 016 already settled those and their changes are implemented.

Thirty-one findings were recorded across five iterations. Every one was checked against the cited line before it was ranked, and the Product Owner file each rank would change was opened and read. Nothing here was drawn on a live board, and no screenshot, image file, `figma.com` board URL or containment folder was opened. Examples use fictional companies.

---

## 1. Summary

Three changes matter most.

1. **Read the graph the Figma file already carries.** A design file stores each frame's navigation as `reactions` on the node, and `use_figma` can read that because it runs plugin JavaScript in the file. The packet's Figma intake reads frame content and infers every move, so the one stated source of edges is skipped.
2. **Keep one record per item: node or edge, with a source, a class and a confidence.** The provenance table classifies a node and only adds an edge row when the edge's source differs from its ends, so an inferred connector — the item most likely to be wrong — carries no class at all. Every other finding in this lineage reduces to filling that hole.
3. **Check the model against its sources, not only against the board.** `flow_check.py` says its own scope: the generator silently drops much of what Mermaid can say, so a model can promise a reader what the board never shows. Nothing reads a source, so a model can equally promise a reader what the source never said. The provenance table and the `Left out:` list are claims no check verifies.

---

## 2. What the packets already do well

These are protected. Every rank below leaves them in place.

- **A fail-closed pre-write check.** "The rules each diagram kind carries are checked on the Mermaid model first, and a model that breaks one is never written" [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:12]. No corpus source has an equivalent; Figma's own diagram skill goes from context gathering to the tool call [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:59].
- **A read-back compared with the model, never with memory.** "Every read-back compares the board with the model, never with memory" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:217]. The corpus's screenshot workflow verifies by looking at its own output instead [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/video-interaction-mapper/SKILL.md:265].
- **A rollback limited to this write.** "The rollback for an existing board is to delete only the nodes and connectors the write created" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:195].
- **A fidelity ledger.** `Left out:` names every source item in no diagram, with its reason [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:119].
- **The five source classes and the Doc Mode conflict gate, already cited by the intake** [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:145], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:120].
- **One consolidated question, never a stream of them** [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:186].
- **A per-type budget and ordered cuts** [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:162], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:170].

The input half is the thin half. That is the whole of Section 3.

---

## 3. Ranked changes

Order weighs three things: whether a current rule fails on its own terms, whether the failure is silent to a reader, and how cheap the proof is. Each rank names the Product Owner file it changes and the source it comes from. No rank touches a frozen parent decision, adds a reply line, or changes the write path; where a rank would add a reply line, it says so and the alternative is used instead.

### Rank 1. Read the reaction graph before reading any frame content

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md`, Section 4 "Figma flows".
- **Comes from:** the plugin API exposes `ReactionMixin` with `reactions`, beside `FramePrototypingMixin` [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-use/references/plugin-api-standalone.index.md:194], [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-use/references/plugin-api-standalone.index.md:198]; a published skill returns "prototype reactions" through `use_figma`, `get_design_context` and `get_metadata` [SOURCE: research/corpus/figma__community-resources/agent_skills/README.md:105], [SOURCE: research/corpus/figma__community-resources/agent_skills/README.md:106]; an implementation lists the triggers and actions a reaction carries [SOURCE: research/corpus/arinspunk__claude-talk-to-figma-mcp/CHANGELOG.md:29].
- **What changes:** where the input is a design file or a prototype link, the first read is one read-only `use_figma` call returning, for each top-level frame, its id, its name and its `reactions`. Frame content is read afterwards, once per frame that becomes a node. The section says plainly that this call is a read, not a write route, and that it never creates, moves or deletes a node.
- **Why first:** it replaces inference with a stated fact for the item a model is most wrong about, and it lowers the cost of the intake, which currently reads node by node before it knows a single edge [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:116].
- **Verified?** The property's existence is documented. Whether `use_figma` returns `reactions` on frames the generator drew is not; the rank is written so a failed read falls back to the current route.

### Rank 2. Keep one intake record per item, and make it the only input the model is written from

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` step 3 (Intake) and step 4 (Model), plus `AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md` Section 3.
- **Comes from:** the uncertainty vocabulary Figma's own screenshot workflow carries — `unknown trigger`, `inferred`, `uncertain`, `visible: false`, `confidence: medium|low` — with uncertain markers suppressed by default [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/video-interaction-mapper/SKILL.md:111], [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/video-interaction-mapper/SKILL.md:317]; the before/after pair as the unit that carries a trigger [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/video-interaction-mapper/SKILL.md:130]; the grammar's typed labels for an assumption, a question and a rule [SOURCE: research/corpus/bluescaban__blueprints/docs/specs/card-grammar.md:80], [SOURCE: research/corpus/bluescaban__blueprints/docs/specs/card-grammar.md:81].
- **What changes:** the intake produces one row per item before any Mermaid is written, each row carrying the item's kind (node or edge), its source, its class and its confidence. An edge row carries its from, its to and its trigger. The model is then written from the rows, and every node and connector in the Mermaid block traces to exactly one row. The record lives beside the model as the provenance table already does, so no reply line changes.
- **Why second:** every other rank in this list writes into this record, and the packet already ships the surface for it.

### Rank 3. Verify an image-derived label before it becomes a node

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md`, Section 4 "Screenshots", and the judged-by-hand label rule at Section 5.
- **Comes from:** the OCR checkpoint is a preview whose "output ... can repeat tokens. Verify against ground truth when exactness matters" [SOURCE: .skilled/skills/sk-vision/SKILL.md:204]; the scene read classifies type, layout, elements and state but returns no coordinates [SOURCE: .skilled/skills/sk-vision/feature-catalog/scene-understanding/inspect.md:32]; a second read on an upscale "is where zoomed text actually becomes readable" [SOURCE: .skilled/skills/sk-vision/feature-catalog/pixel-analysis/zoom.md:26].
- **What changes:** a label taken from an image is re-read on a crop or an upscale before it is written, and the intake records which read produced it — the outline read, the OCR read or the visual read. Where the two disagree, the label goes to the one question, or the node is drawn with the source class that names the doubt, never silently. The packet's existing rule that a visual-only read-back is labelled `read visually` [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:245] becomes the model's rule too, on the read side.
- **Why third:** the label is the first thing a reader checks and the cheapest thing to get wrong. It costs one extra read per uncertain label and nothing else.

### Rank 4. Decide screen against state by the trigger, and use a pixel diff for adjacency

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 4 "Screenshots", and the judged-by-hand rules in `AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md`.
- **Comes from:** a pixel diff returns a changed percentage and up to twelve changed-region boxes, with anti-aliasing excluded [SOURCE: .skilled/skills/sk-vision/feature-catalog/pixel-analysis/diff.md:22]; a reaction's action separates `NAVIGATE` from `OVERLAY` and `BACK` [SOURCE: research/corpus/arinspunk__claude-talk-to-figma-mcp/CHANGELOG.md:29]; Figma's SwiftUI guidance models loaded, empty and loading states as variants rather than frames [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-swiftui/references/code-to-design.md:183]; the shape table calls one rectangle "a screen or an action" and has no state at all [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:43].
- **What changes:** two rules. A pair of images whose changed area sits inside one region is one screen in two states; a pair whose changed area spans the viewport is two screens. And a state earns its own node only when a different action or event reaches it, or when a reader can be trapped in it; otherwise it belongs in its screen's label, with the detail under `Left out:`. The rule keeps the four shapes and adds no fifth.
- **Why fourth:** it removes the largest source of invented nodes in a screenshot set, and it is decided by measurement rather than by reading a caption.

### Rank 5. State the inference ladder, and let explicit evidence suppress inference

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 4 "Never invent".
- **Comes from:** "When you provide explicit definitions (e.g., `E:` edges), the system uses ONLY those. When omitted, the system infers intelligently" [SOURCE: research/corpus/bluescaban__blueprints/docs/specs/card-grammar.md:26], [SOURCE: research/corpus/bluescaban__blueprints/docs/specs/card-grammar.md:27]; sequential ordering within a lane by numbered steps [SOURCE: research/corpus/bluescaban__blueprints/docs/specs/card-grammar.md:143]; numbers as the signal that order is the point [SOURCE: research/corpus/prasantloki__figjam-builder/SKILL.md:34]; the packet's own rule that a contradicted edge is a finding rather than a connector [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:61].
- **What changes:** the ladder is written down and used in order: an explicit source edge, then explicit step numbering, then lane or container order, then screenshot adjacency, then the filename's trigger grammar, then one question. The record names which rung produced each edge. An inferred edge never overrides an explicit one, and a conflict between them is a finding.
- **Why fifth:** it is the algorithm the never-invent rule lacks, and it makes the question a last resort rather than the first response to an unordered set.

### Rank 6. Read an acceptance criterion as a triple, and a Then with no When as a gap

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 4 "Product docs".
- **Comes from:** a criterion "holds `Given/When/Then/And` bullets" with "One outcome per Then or And line", Story criteria verifying screen-level behaviour and Epic criteria staying release-level [SOURCE: AI Systems/Product Owner/sk-product-owner/references/story-mode.md:151]; a criterion deliberately leaves the mechanism to the developer, same line; a Story keeps an undecided part visible with an `**Open:**` line [SOURCE: AI Systems/Product Owner/sk-product-owner/references/story-mode.md:74].
- **What changes:** a Story or an Epic is read as triples rather than as prose. Given contributes a state, When contributes the edge trigger, and each Then or And contributes one outcome. A Then with no When yields a node and no edge into it, and the missing trigger becomes a named gap. An Epic's release-level criterion contributes no node at all.
- **Why sixth:** it turns the one pre-structured input type into edges directly, and it is the cheapest gain in the lineage. It ranks below the ladder because it needs that ladder to know when a When outranks an inferred one.

### Rank 7. Give an edge an actor

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 4 "What each type needs from its sources", user-flow and process rows.
- **Comes from:** `S:` is a "User-performed action" and `SYS:` a "System/app-performed action (automatic)" [SOURCE: research/corpus/bluescaban__blueprints/docs/specs/card-grammar.md:60], [SOURCE: research/corpus/bluescaban__blueprints/docs/specs/card-grammar.md:61], with a cross-lane handoff rule for the person-to-system-to-person chain [SOURCE: research/corpus/bluescaban__blueprints/docs/specs/card-grammar.md:179]; the packet's connector carries only "an optional label" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:47].
- **What changes:** the needs table's user-flow row asks for "the trigger for each move" and adds who performs it; the record carries that field, and the process type's lane assignment reads it. A system-performed move is not a missing user action, which is the distinction that stops a loading view becoming a screen.
- **Why seventh:** it changes no shape and no label; it changes what the intake must ask for before it may draw.

### Rank 8. Give the provenance table a class per inferred edge

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md` Section 3.
- **Comes from:** the table adds an edge row only for a relationship "whose source differs from its ends" [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:110]; Doc Mode classifies "at section, field, table row, or individual claim level" [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:140], with `Unknown` as a legal class [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:149]; the intake claims to apply that rule [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:120].
- **What changes:** every edge carries a row when it is inferred, whatever its ends say, and the row carries the class and the confidence. A user-flow connector drawn from adjacency is never `current behavior`.
- **Why eighth:** it closes the gap between the rule the intake cites and the artifact that is supposed to carry it, and it is one table instruction.

### Rank 9. Give a contested item a surface the reply already has

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 4 "Product docs" and Section 8's `Left out:` sentence, and `AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md` Section 2.
- **Comes from:** the conflict gate's two endings — a winner within scope, or "stop composition" and one consolidated question [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:184], [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:186]; the rubric's rule that a contradicted edge "is a finding, not a connector" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:61]; the `Left out:` line that already names what the board does not hold [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:119].
- **What changes:** a contested edge is removed and the item is named on the `Left out:` line with both sources and the reason, or the gate's one question asks which source governs. It is never removed silently. No reply line is added, because `Left out:` already exists.
- **Why ninth:** an unreported deletion is worse than a drawn guess, because the reader cannot see it. It ranks below the record changes because it depends on the record existing.

### Rank 10. Test the chosen type against its own needs row before modelling

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 3.
- **Comes from:** the type is picked by the reader's question [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:75], while the needs table states what each type requires [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:134], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:138], and the packet never joins the two.
- **What changes:** after the type is picked, the intake tests it against that type's needs row. When the input cannot supply a needed item, the answer is one question, a different type, or a named gap, and the chosen route is recorded. A state diagram with no events in the input is the case this prevents.
- **Why tenth:** it is a two-sentence rule that stops a whole class of drawing-without-evidence, but it fires less often than the record changes.

### Rank 11. Allocate the chunks from the source list before drawing

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 5 budget rule, and the split pattern in `AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md` Section 2.
- **Comes from:** the budget is per type and splits rather than shrinks [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:162], the cuts run in a fixed order [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:170], and "Every source step lands in one of the diagrams or is listed as left out" [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:91].
- **What changes:** the ordered record is divided into diagram-sized groups before the first Mermaid block is written, each group getting a hand-off node and a name. The ledger then checks an allocation rather than reconstructing a split.
- **Why eleventh:** it changes no output, but only large inputs feel it.

### Rank 12. Bound the source re-read to the rows that are silent when wrong

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` step 10 (read-back), plus one line in `AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md` Section 6.
- **Comes from:** the check "parses text only and never renders or runs anything in a label" [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:26], so no source is read at all; the packet's own reason for the check is that a model can promise what the board never shows [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:10]; and the bounded-reread discipline a research agent already uses, "perform the narrowest reread and record the reason" [SOURCE: .skilled/agents/deep-research.md:42].
- **What changes:** before the gate, one narrow reread per row whose class is not `current behavior` or whose edge is inferred, with the reason recorded on the row. Rows that quote a source line are not re-read. The whole pass stays inside the intake's existing token budget.
- **Why twelfth:** it is the only mechanism that checks the source-to-model contract at all, and it is deliberately partial, which is why it ranks below the changes that make the record worth checking.

### Rank 13. Parse a Figma URL's node id correctly

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 4 "Figma flows".
- **Comes from:** the documented parsing rule turns `node-id=609-35535` into `nodeId` `609:35535` [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-generate-design/SKILL.md:80], while the packet says only to take the node id from the URL [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:116].
- **What changes:** one clause: a hyphenated `node-id` becomes a colon before the read.
- **Why last:** it is one character and it fails loudly on the first call, so it costs the least of anything here. It is listed because it is the first step of the whole Figma intake and it is currently wrong for every hyphenated URL.

---

## 4. Recorded conflicts and how they were settled

Each of these was a "which truth prevails" decision met mid-run. Under a fan-out lineage with no operator, each was recorded and the run continued.

- **`TBD` on a label.** Story Mode lets an unknown value stand as `TBD...` rather than an inferred estimate [SOURCE: AI Systems/Product Owner/sk-product-owner/references/story-mode.md:155]; Flow Mode requires a label to use the source's own words and sends anything missing to `Left out:` [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:169]. Settled in rank 2 and rank 9: a `TBD` supplied by the source is the source's own word and may be carried with the class that marks it open; a value the writer would have to invent stays out and is named under `Left out:`. The two rules are compatible once the record carries a class, which is why the record ranks second.
- **A frame name against the screen's own heading.** Both are "the source's words", so the label rule cannot choose. Settled in rank 2: the visible heading wins for the label, the layer name is kept in the record's source field, and a disagreement is recorded rather than resolved silently. No corpus source decides this; the decision is the packet's to make and is marked as a house choice.
- **A contradicted edge.** Doc Mode stops composition and asks [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:184]; Flow Mode removes the connector and reports nothing [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:61]. Settled in rank 9: the removal stands and the item moves to the `Left out:` line, because an unreported deletion is the one outcome neither source intended.
- **The hosted read tools against `use_figma` as a read.** The packet lists `use_figma` only among the write tools. Rank 1 adds it as a read and says so explicitly, so the write gate rules are untouched.

---

## 5. Ruled out

- **Drawing every loading, empty and error view as its own node.** The user flow is capped at nine nodes and the remove test cuts any two nodes that always travel together [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:39]. Only a state reached by a different action, or one that traps the reader, earns a node.
- **Reading the trigger of a reported error out of a support ticket.** No corpus source supports it, and Doc Mode limits an authority signal to the scope it covers [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:175], so a ticket evidences the exit state and not the move into it.
- **Treating OCR as an exact transcription channel.** The skill states the checkpoint can repeat tokens [SOURCE: .skilled/skills/sk-vision/SKILL.md:204].
- **Reading a whole design file's frame content to build the model.** Token-heavy and unnecessary before the graph is known; ruled out in iteration 4.
- **Verifying every provenance row against its source.** It defeats the intake's token budget and re-proves rows that quote a line; rank 12 bounds it instead.
- **Adding a reply line for any of this.** The delivery shape is frozen by the parent's D6 decision and every rank above reuses `Left out:` or the record rather than adding a line.

---

## 6. Claims not verified

Nobody should act on these as fact.

- **Whether `use_figma` can read `reactions` on frames written by `generate_diagram`.** The property is documented; the call on a generated frame was never made. Rank 1 is written to fall back to the current route.
- **Which attribute names `get_figjam` returns for connector caps and endpoints.** Phase 016 left this open and this lineage did not reopen it.
- **Whether a `figma.com/proto` URL carries navigation metadata a design URL does not.** No corpus source describes its parameters. The lineage answers the prototype-link question from `reactions` and marks the URL question open.
- **Whether the claude.ai Figma connector exposes `use_figma`, `get_figjam` or `whoami`.** Phase 009 left this open; no session was run.
- **That a support ticket behaves as an exit-state-only source.** That is an inference from Doc Mode's scope limit, not a quoted rule, and no corpus source was found.
- **That the visible heading should beat the layer name.** No source decides it. It is recorded above as a house choice.
- **Any live board behaviour.** No board was written. Every claim about what the generator or the reader does on a board rests on documentation.
- **The packet's own scorecard as the only scored board instrument.** Not re-tested here.

---

## 7. Sources

### Repo surfaces read

- `AI Systems/Product Owner/sk-create-figjam/`: `references/flow-mode.md`, `references/quality-rubric.md`, `references/types/user-flow.md`, `references/types/state.md`, `assets/flow-templates.md`, `scripts/flow_check.py`, `scripts/figjam_checks/flowchart.py`, `SKILL.md`
- `AI Systems/Product Owner/sk-product-owner/`: `references/story-mode.md`, `references/doc-mode.md`
- `AI Systems/Product Owner/mcp-figma/references/tool-surface.md`
- `.skilled/skills/sk-vision/SKILL.md` and its feature catalog: `scene-understanding/inspect.md`, `scene-understanding/ocr.md`, `pixel-analysis/zoom.md`, `pixel-analysis/diff.md`
- `.skilled/agents/deep-research.md`

### Earlier research read first, and not re-proposed

- `AI Systems/Product Owner/specs/017-figjam-flow-generation/009-figjam-skill-research/research/research.md`
- `AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/research.md`, Sections 1 to 9

### Corpus repositories used

All paths are under `research/corpus/`.

| Repository | Files used |
|---|---|
| `figma__mcp-server-guide` | `workflow-skills/video-interaction-mapper/SKILL.md`, `skills/figma-use/references/plugin-api-standalone.index.md`, `skills/figma-generate-diagram/SKILL.md`, `skills/figma-generate-diagram/references/flowchart.md` |
| `figma__community-resources` | `agent_skills/README.md` |
| `bluescaban__blueprints` | `docs/specs/card-grammar.md`, `docs/flows/_grammar_example.md` |
| `prasantloki__figjam-builder` | `SKILL.md` |
| `lightspeedwp__.github` | `plugins/figma/figma-swiftui/references/code-to-design.md`, `plugins/figma/figma-generate-design/SKILL.md` |
| `arinspunk__claude-talk-to-figma-mcp` | `CHANGELOG.md` |

Eighteen corpus repositories were not cited by any iteration. Four of them (`figma__community-resources`, `prasantloki__figjam-builder`, `bluescaban__blueprints`, `arinspunk__claude-talk-to-figma-mcp`) had never been cited for the intake side by phases 009 or 016.

### Lineage inputs

- `research/lineages/deepseek/iterations/iteration-001.md` to `iteration-005.md`
- `research/lineages/deepseek/deltas/iter-001.jsonl` to `iter-005.jsonl`

### Checks run

- Six append-gateway records accepted, exit 0 each: one config row and five iteration rows, sequence 1 to 6, every one with a receipt. `node .skilled/skills/system-deep-loop/runtime/scripts/append-mode-event.cjs`.
- The reducer ran after every iteration, exit 0 each time, `corruptionCount` 0 and `iterationsCompleted` advancing 0 to 5.
- Every delta file was parsed line by line as JSON before its record was appended.
- No `flow_check.py` run, no `--self-test` run, no live board. None is claimed.

---

## 8. Convergence report

- **Stop reason:** `maxIterationsReached`. The configured `stopPolicy` is `max-iterations` and `convergenceMode` is off, so convergence before the cap would have been telemetry only.
- **Total iterations:** 5 of 5.
- **Questions answered:** 9 of 9 from the strategy's key-question set.
- **newInfoRatio trend:** 0.80, 0.70, 0.62, 0.68, 0.55. Declining, with iteration 4 rising because the Figma reaction graph was new evidence rather than a deepening.
- **Findings:** 31 across five iterations, ranked into 13 changes.
- **Ruled out:** 6 directions, listed in Section 5.
- **Scope violations:** none. Every write landed under `research/lineages/deepseek`.
