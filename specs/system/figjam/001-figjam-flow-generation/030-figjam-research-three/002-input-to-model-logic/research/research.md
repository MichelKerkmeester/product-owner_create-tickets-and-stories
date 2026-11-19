# Input to model logic research

## 1. Summary

The most reliable route is to read structure the sources already state before reading pixels, then infer in a fixed order, then keep a record that says who said what. Three changes carry most of the gain. Read the navigation graph a Figma file already stores before any frame content, because a reaction holds the designer's own trigger and destination for each move. Keep one record per drawn item with a source, a class, a confidence and the rung that produced it, so a guessed edge is visible instead of silent. Verify a label taken from an image on a crop before it becomes a node, because the OCR checkpoint is a preview and the packet names no read tool at all.

## 2. What the packets already do well

- A fail-closed pre-write check, where "a model that breaks one is never written" [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:12]
- A read-back compared with the model, never with memory [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:217]
- A rollback limited to what this write created [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:195]
- A fidelity ledger that names what the board does not hold [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:119]
- Five source classes, and a conflict gate that stops rather than guesses [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:184], [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:185]
- A per-type budget and cuts in a fixed order [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:162], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:170]
- A needs table per type that already exists, so the gate below is a wiring job and not new prose [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:134], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:138]
- Type choice by the reader's question, and labels in the source's own words [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:75], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:169]
- A provenance table already sits beside the model, per item, so the record change reuses a surface [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:110]
- Never invent, with one or two focused questions, which matches Figma's own guidance [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:144], [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:69]

## 3. Ranked changes

Mirror names below follow the kernel's own loading table, which sends any FigJam diagram to the Flow Mode knowledge file [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:207]. No rank adds a reply line, so the kernel needs no change.

### Rank 1. Read the reaction graph before any frame content

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 4 "Figma flows"
- **Comes from:** the typed plugin API stores prototyping on the node, a NODE action carries `destinationId` and `navigation` [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/figma__mcp-server-guide/skills/figma-use/references/plugin-api-standalone.d.ts:3473], [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/figma__mcp-server-guide/skills/figma-use/references/plugin-api-standalone.d.ts:3475], with five navigation values [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/figma__mcp-server-guide/skills/figma-use/references/plugin-api-standalone.d.ts:3536] and a trigger set that includes a timer [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/figma__mcp-server-guide/skills/figma-use/references/plugin-api-standalone.d.ts:3509]. A frame carries both mixins [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/figma__mcp-server-guide/skills/figma-use/references/plugin-api-standalone.index.md:194], [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/figma__mcp-server-guide/skills/figma-use/references/plugin-api-standalone.index.md:200]. A published skill returns prototype reactions through `use_figma` [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/figma__community-resources/agent_skills/README.md:105], [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/figma__community-resources/agent_skills/README.md:106], a corpus server exposes a read verb for them [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/arinspunk__claude-talk-to-figma-mcp/CHANGELOG.md:30], and reading first is the stated pattern [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/mkaralevich__pi-figma-labor/skills/figma-prototype/SKILL.md:123]
- **The gap:** the intake reads node by node for content and infers every move, and `use_figma` appears only as a write [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:116], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:190]
- **What changes:** where the input is a design file, the first read is one read-only `use_figma` call returning id, name and reactions per top-level frame. NAVIGATE or SWAP to another frame is a new screen, OVERLAY, SCROLL_TO or CHANGE_TO is a state of the same screen, and AFTER_TIMEOUT is a system trigger. The section says the call is a read, that a dynamic-page plugin can only read `reactions` [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/mkaralevich__pi-figma-labor/skills/figma-prototype/SKILL.md:171], and that a hyphenated `node-id` becomes a colon before any lookup [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/lightspeedwp__.github/plugins/figma/figma-generate-design/SKILL.md:78]
- **Effort:** medium
- **Mirror or kernel:** knowledge `Product Owner - Templates - Flow Mode.md` Section 4

### Rank 2. Keep one intake record per item, with a class and a confidence

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` steps 3 and 4, and the provenance table in `AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md` Section 3
- **Comes from:** a named uncertainty vocabulary with markers suppressed by default [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/figma__mcp-server-guide/workflow-skills/video-interaction-mapper/SKILL.md:113], [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/figma__mcp-server-guide/workflow-skills/video-interaction-mapper/SKILL.md:115], an unknown trigger instead of a guess [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/figma__mcp-server-guide/workflow-skills/video-interaction-mapper/SKILL.md:317], and one record per moment carrying trigger, label and both ends [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/figma__mcp-server-guide/workflow-skills/video-interaction-mapper/SKILL.md:130]
- **The gap:** a row is added for an edge only when its source differs from its ends, so an inferred user-flow connector has no class at all [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:110], while the rubric asks only that every node has a row [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:59], and no confidence word appears anywhere in the packet
- **What changes:** the intake produces one row per item before any Mermaid, carrying kind, source, class, confidence and the rung that produced it. The table gains a confidence column and an edge row whenever the edge was inferred. A frame name and the visible heading both land in the row, the heading labels the node and a disagreement is recorded rather than resolved
- **Effort:** medium
- **Mirror or kernel:** knowledge `Product Owner - Assets - Flow Templates.md` Section 3 and `Product Owner - Templates - Flow Mode.md` steps 3 and 4

### Rank 3. Verify an image-derived label before it becomes a node

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 4 "Screenshots"
- **Comes from:** the OCR checkpoint is a preview whose output "can repeat tokens" [SOURCE: .skilled/skills/sk-vision/SKILL.md:204], a second read on an upscale is where small text becomes readable [SOURCE: .skilled/skills/sk-vision/feature-catalog/pixel-analysis/zoom.md:26], the scene read classifies layout and state but not coordinates [SOURCE: .skilled/skills/sk-vision/feature-catalog/scene-understanding/inspect.md:24], and a diff returns a changed percentage with changed-region boxes [SOURCE: .skilled/skills/sk-vision/feature-catalog/pixel-analysis/diff.md:24]
- **The gap:** the click target "is read off the image" and no read tool, checkpoint or verification appears in the packet [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:113], so a label is a transcription of an approximate read and nothing records that
- **What changes:** a label taken from an image is re-read on a crop or an upscale, and the row names which read produced it. Where two reads disagree the label goes to the one question or carries the unknown class, and the existing `read visually` wording becomes the model's rule as well as the reply's [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:245]
- **Effort:** small
- **Mirror or kernel:** knowledge `Product Owner - Templates - Flow Mode.md` Section 4. The portable part is the verification step, because the local vision tools are off by default and need a build [SOURCE: .skilled/skills/sk-vision/SKILL.md:12]

### Rank 4. State the inference ladder

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 4 "Never invent"
- **Comes from:** explicit edges suppress inference [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/bluescaban__blueprints/docs/specs/card-grammar.md:27], with an explicit edge label to match [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/bluescaban__blueprints/docs/specs/card-grammar.md:74], steps in one lane connecting in order [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/bluescaban__blueprints/docs/specs/card-grammar.md:145], numbers as the signal that order is the point [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/prasantloki__figjam-builder/SKILL.md:34], and the before and after pairing around a trigger [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/figma__mcp-server-guide/workflow-skills/video-interaction-mapper/SKILL.md:20]
- **The gap:** the intake names only the filename grammar and one question, so a set with no numbering falls straight to the question [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:111]
- **What changes:** the ladder is written and used in order, an explicit source edge, then numbering, then lane or container order, then screenshot adjacency, then the filename grammar, then one question. The record names the rung, an inferred edge never overrides a stated one, and a clash between the two is a finding
- **Effort:** small
- **Mirror or kernel:** knowledge `Product Owner - Templates - Flow Mode.md` Section 4

### Rank 5. Decide screen against state by the action that reaches it

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 4 "Screenshots" and the judged-by-hand rules in `AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md` Section 3
- **Comes from:** the five navigation values [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/figma__mcp-server-guide/skills/figma-use/references/plugin-api-standalone.d.ts:3536], a change list that counts loaded content, selected state and validation state [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/figma__mcp-server-guide/workflow-skills/video-interaction-mapper/SKILL.md:99], loaded, empty and loading modelled as variants rather than frames [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/lightspeedwp__.github/plugins/figma/figma-swiftui/references/code-to-design.md:183], and a measurable diff [SOURCE: .skilled/skills/sk-vision/feature-catalog/pixel-analysis/diff.md:24]
- **The gap:** one rectangle means "a screen or an action" and a state has no entry at all [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:43], so two supplied images of one screen become two nodes
- **What changes:** a pair whose changed area sits inside one region is one screen in two states, and a pair that differs across the viewport is two screens. A state earns a node only when a different action reaches it or a reader can be trapped in it, and otherwise the detail goes in the label and under `Left out:` [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:240]. The four shapes stay as they are [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:42]
- **Effort:** small
- **Mirror or kernel:** knowledge `Product Owner - Templates - Flow Mode.md` Section 4 and `Product Owner - Templates - Flow Type - User Flow.md`

### Rank 6. Read an acceptance criterion as a triple

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 4 "Product docs"
- **Comes from:** a criterion "holds `Given/When/Then/And` bullets" with one outcome per Then or And line, leaves the mechanism to the developer, and splits Story behavior from Epic release behavior [SOURCE: AI Systems/Product Owner/sk-product-owner/references/story-mode.md:151], beside the legal place for an open value [SOURCE: AI Systems/Product Owner/sk-product-owner/references/story-mode.md:74]
- **The gap:** the packet never names acceptance criteria, so the one pre-structured input arrives as prose and is asked only to be classified [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:120]. A `TBD` the source supplies is its own word and may travel with the open class, while a value the writer would invent stays out
- **What changes:** Given is a state, When is the edge trigger and each Then or And is one outcome node. A Then with no When yields a node and a named gap. An Epic's release-level criterion contributes no node
- **Effort:** small
- **Mirror or kernel:** knowledge `Product Owner - Templates - Flow Mode.md` Section 4

### Rank 7. Give an edge an actor

- **Changes:** the needs table row for a user flow in `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 4 and `AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md` Section 2
- **Comes from:** a step typed by who performs it, with a system step marked automatic [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/bluescaban__blueprints/docs/specs/card-grammar.md:60], [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/bluescaban__blueprints/docs/specs/card-grammar.md:61], and a timer trigger that no person fires [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/figma__mcp-server-guide/skills/figma-use/references/plugin-api-standalone.d.ts:3509]
- **The gap:** a connector takes an optional label and nothing else [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:47], while the process row already asks who performs each step [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:135]
- **What changes:** the user-flow row asks who acts on each move, the record carries the actor, and a system or timer move is never counted as a missing user action
- **Effort:** small
- **Mirror or kernel:** knowledge `Product Owner - Templates - Flow Mode.md` Section 4 and `Product Owner - Templates - Flow Type - User Flow.md`

### Rank 8. Name what each source can and cannot evidence

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 4, a ticket row beside the four input types, and the "Never invent" rule
- **Comes from:** an authority signal is limited to the scope it covers [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:175], a Then without a When carries no edge [SOURCE: AI Systems/Product Owner/sk-product-owner/references/story-mode.md:151], and missing trigger evidence takes an unknown trigger [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/figma__mcp-server-guide/workflow-skills/video-interaction-mapper/SKILL.md:317]
- **The gap:** the intake has four input types and no ticket row [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:109], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:125], and nothing says which item kinds a source may contribute, so a reported error invites an invented trigger
- **What changes:** one line per input type names the item kinds it can evidence. A ticket evidences an error or exit node and not the move into it, a criterion's When evidences an edge, a reaction evidences an edge. A trigger with no evidence becomes an unknown trigger
- **Effort:** small
- **Mirror or kernel:** knowledge `Product Owner - Templates - Flow Mode.md` Section 4

### Rank 9. Test the chosen type against its needs row

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 3
- **Comes from:** the type is picked by the reader's question [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:75] and the needs table states what each type requires [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:134], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:138], while Figma's own skill warns that the diagram is only as good as the context behind it [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:61]
- **The gap:** the two sections are never joined, so a state diagram ordered for a Loomlist billing screen whose screenshots show no events is drawn with invented events
- **What changes:** after the pick, the intake tests the input against that row. A missing need becomes one question, a different type or a named gap, and the route taken is recorded
- **Effort:** small
- **Mirror or kernel:** knowledge `Product Owner - Templates - Flow Mode.md` Section 3

### Rank 10. Give a contradicted item a surface the reply already has

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 4 and the `Left out:` sentence in Section 8, plus `AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md` Section 4
- **Comes from:** the gate stops and asks when no source wins [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:184], [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:185], the contradicted edge rule [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:61], and the ledger that already exists [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:119]
- **The gap:** followed literally the rule removes the connector and reports nothing a reader can see, and an unreported deletion is worse than a drawn guess
- **What changes:** the item moves to the `Left out:` line with both sources and the reason, or the gate's one question asks which source governs. It is never removed silently and no line is added
- **Effort:** small
- **Mirror or kernel:** knowledge `Product Owner - Templates - Flow Mode.md` Section 4 and Section 8, and `Product Owner - Rules - Flow Quality Rubric.md`

### Rank 11. Allocate the chunks from the source list before drawing

- **Changes:** the budget rule in `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 5 and the split pattern in `AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md` Section 2
- **Comes from:** over budget, split rather than shrink [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:162], cuts in a fixed order [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:170], and every source step landing in a diagram or under `Left out:` [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:91], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:77]
- **The gap:** the split is decided from the model while the ledger is checked against the sources afterwards, so a large input is corrected late instead of allocated first
- **What changes:** the ordered record is divided into diagram-sized groups before the first Mermaid block, each with a hand-off node and a name, so the ledger checks an allocation
- **Effort:** medium
- **Mirror or kernel:** knowledge `Product Owner - Templates - Flow Mode.md` Section 5 and `Product Owner - Assets - Flow Templates.md` Section 2

### Rank 12. Re-read only the rows that fail silently, before the gate

- **Changes:** step 10 in `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` and `AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md` Section 6
- **Comes from:** the check parses text only and reads no source [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:26], its own reason is that a model can promise what the board never shows [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:10], and the narrow-reread discipline already in use [SOURCE: .skilled/agents/deep-research.md:42]
- **The gap:** nothing reads a source, so the provenance table and the `Left out:` list are claims no check verifies, and a model can equally promise what the source never said
- **What changes:** one narrow reread per row whose class is not current behavior or whose edge is inferred, with the reason recorded on the row. A row quoting a source line is not re-read
- **Effort:** small
- **Mirror or kernel:** knowledge `Product Owner - Templates - Flow Mode.md` step 10 and `Product Owner - Rules - Flow Quality Rubric.md` Section 6

## 4. Rejected ideas

- Drawing every loading, empty or error view as its own node, because a user flow is capped at nine nodes and the remove test merges two nodes that always travel together [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:64], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:39]
- Reading the trigger of a reported error out of a ticket, because a ticket reports one path and a signal is limited to the scope it covers [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:175]
- Treating OCR as an exact channel, because the preview checkpoint can repeat tokens [SOURCE: .skilled/skills/sk-vision/SKILL.md:204]
- Reading every frame's content before the graph, which the packet's own cost rule rules out for content [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:116]
- Verifying every provenance row against its source, which re-proves rows that quote a line and spends the intake budget, so rank 12 bounds it
- Adding a reply line for any of this, because `Left out:` already carries it [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:119]
- Trusting a prototype URL's parameters as navigation metadata, because no source describes them and no URL was opened
- Adding a fifth shape for a state, because the four shapes stay [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:42]
- The seventeen changes ranked in the earlier improvement research, because they are implemented and out of scope here [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/research.md:78]

## 5. Corrections to the iterations

- Iteration 1 finding 2 cites `inspect.md:32` for the scene read and its fixed prompt. The text is at `:24` and `:26` [SOURCE: .skilled/skills/sk-vision/feature-catalog/scene-understanding/inspect.md:24]
- Iteration 1 finding 4 cites `diff.md:22` for the changed percentage and the region boxes. The numbers are at `:24` [SOURCE: .skilled/skills/sk-vision/feature-catalog/pixel-analysis/diff.md:24]
- Iteration 2 finding 1 quotes the numbering rule as "of 25". The file says "of N" [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/prasantloki__figjam-builder/SKILL.md:34]
- Iteration 2 finding 1 cites `card-grammar.md:143` for steps in one lane connecting in order. That sentence is at `:145` [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/bluescaban__blueprints/docs/specs/card-grammar.md:145]
- Iteration 2 finding 1 cites `card-grammar.md:141` for explicit edges. That line states the opposite case, and the precedence rule is at `:27` with the edge label at `:74` [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/bluescaban__blueprints/docs/specs/card-grammar.md:27]
- Iteration 3 finding 4 cites `doc-mode.md:140` for claim-level classification. It is at `:141` [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:141]
- Iteration 3 finding 5 cites `doc-mode.md:186` for the consolidated question. The question is at `:185` and the no-winner rule at `:186` [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:185]
- Iteration 4 finding 3 lists NAVIGATE, OVERLAY and BACK as the action values. Navigation has five values, and BACK is an action type rather than a navigation value [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/figma__mcp-server-guide/skills/figma-use/references/plugin-api-standalone.d.ts:3536], [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/figma__mcp-server-guide/skills/figma-use/references/plugin-api-standalone.d.ts:3433]
- Iteration 5 finding 3 cites `flowchart.py:215` for the list of enforced rules. That line is the `check_flow` signature, which shows the checks take a parsed diagram and the block text [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:215]
- The lineage draft says eighteen of the 22 corpus repos were uncited. The count was sixteen, and this synthesis adds two, `openai__plugins` and `mkaralevich__pi-figma-labor`, so fourteen remain uncited
- Rank 1 of the draft omits the read-only caveat, which matters because a dynamic-page plugin cannot write reactions at all [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/mkaralevich__pi-figma-labor/skills/figma-prototype/SKILL.md:171]

## 6. Claims not verified

- That a read-only `use_figma` call returns `reactions` on frames the generator drew, since no call was made and rank 1 falls back to the current route
- Which attribute names `get_figjam` returns for connector ends and caps
- Whether a prototype URL carries navigation metadata a design URL does not
- Whether a Project's Figma connector exposes `use_figma`, `get_figjam` or `whoami`
- That a ticket evidences an exit state only, which is an inference from the scope rule rather than a quoted rule
- That the visible heading should beat the layer name, which is a house choice no source decides
- Whether the local vision tools exist in a given run, since they are opt-in and need a build [SOURCE: .skilled/skills/sk-vision/SKILL.md:12]
- The corpus reaction read, which is documented in a changelog entry and a tool description rather than run [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/arinspunk__claude-talk-to-figma-mcp/CHANGELOG.md:30]
- Any live board behavior, since no board was written and no screenshot or image file was opened

## 7. Sources

- `AI Systems/Product Owner/sk-create-figjam/`: `references/flow-mode.md`, `references/quality-rubric.md`, `references/types/user-flow.md`, `assets/flow-templates.md`, `scripts/flow_check.py`, `scripts/figjam_checks/flowchart.py`
- `AI Systems/Product Owner/sk-product-owner/`: `references/story-mode.md`, `references/doc-mode.md`
- `AI Systems/Product Owner/claude project/Custom Instructions.md`, and the knowledge files `Product Owner - Templates - Flow Mode.md`, `Product Owner - Assets - Flow Templates.md`, `Product Owner - Rules - Flow Quality Rubric.md`, `Product Owner - Templates - Flow Type - User Flow.md`
- `AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/research.md`, Sections 1 to 9
- `.skilled/skills/sk-vision/SKILL.md` with `feature-catalog/scene-understanding/inspect.md`, `feature-catalog/pixel-analysis/zoom.md`, `feature-catalog/pixel-analysis/diff.md`, and `.skilled/agents/deep-research.md`
- `AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/figma__mcp-server-guide/`: `workflow-skills/video-interaction-mapper/SKILL.md`, `skills/figma-use/references/plugin-api-standalone.index.md`, `skills/figma-use/references/plugin-api-standalone.d.ts`, `skills/figma-generate-diagram/SKILL.md`
- `AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/figma__community-resources/agent_skills/README.md`
- `AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/bluescaban__blueprints/docs/specs/card-grammar.md`
- `AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/prasantloki__figjam-builder/SKILL.md`
- `AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/lightspeedwp__.github/`: `plugins/figma/figma-swiftui/references/code-to-design.md`, `plugins/figma/figma-generate-design/SKILL.md`
- `AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/arinspunk__claude-talk-to-figma-mcp/CHANGELOG.md`
- `AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/mkaralevich__pi-figma-labor/skills/figma-prototype/SKILL.md`
- `AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic/research/corpus/openai__plugins/plugins/figma/skills/figma-use/references/plugin-api-standalone.d.ts`
