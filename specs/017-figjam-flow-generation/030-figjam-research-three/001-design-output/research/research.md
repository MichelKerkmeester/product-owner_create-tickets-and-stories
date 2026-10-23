# FigJam design output research

## 1. Summary

The packet is disciplined about content and silent about composition. It says what a diagram must contain and almost nothing about how a finished board reads, so a board can pass every check and still have no beginning. The generator owns geometry and the model owns little, which led the packet to conclude that layout cannot be redesigned. It can be constrained instead, and the published board sources state the constraints. Top three changes: write the first glance down before modelling, put a visible title on every diagram, and give the board a spacing scale with a proximity ratio.

## 2. What the packets already do well

- The three-layer ownership model holds for every type, and nothing ranked below moves a generated node [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:164]
- The palette record is measured, each departure carries its number and the self-test re-measures both columns [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:58]
- It refuses to invent, because "A diagram of a real, partial system beats a polished one of an imagined system" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:144]
- Its content rules are stricter than Figma's own universal constraints, with a 40 character label cap and a per type budget where Figma states neither [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:160] [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/001-design-output/research/corpus/lightspeedwp__.github/plugins/figma/figma-generate-diagram/SKILL.md:49]
- The read-back compares two endpoint ids, two end caps and a label for every connector, which is more than most diagram tools check [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:223]
- The board check already asks whether the accent reads first and whether a second node competes with it [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:83]
- A lost Layout or Legibility point is already attributed to the model or the generator before it is recorded [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/board-quality/user-flow-board-quality.md:79]
- The pass shape, a total floor plus three dimensions held at 2, is better than one aggregate number [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md:87]
- The split rule is deliberate and says why, since "a board has no zoned mode to fall back on" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:150]
- Process lanes keep the neutral pair against Figma's tint per subgraph, so the accent stays the only signal [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/process.md:95]

## 3. Ranked changes

### Rank 1. Write the first glance down before modelling

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md` Section 3, `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 2 step 7 and Section 8
- **Comes from:** [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/001-design-output/research/corpus/prasantloki__figjam-builder/references/composition-grammar.md:9] and [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/001-design-output/research/corpus/prasantloki__figjam-builder/references/composition-grammar.md:13]
- **The gap:** the rubric tests whether the accent reads first, but nothing is written down in advance, so a board can only be judged against itself and a title that repeats the focal claim is never caught
- **What changes:** three lines are written before the model, naming the first, second and last glance, and they travel into the gate so the accent choice has a target and the reply can say what should win
- **Effort:** small
- **Mirror or kernel:** `Product Owner - Rules - Flow Quality Rubric.md` and `Product Owner - Templates - Flow Mode.md`. The kernel is unchanged, because its Flow gate line already lists the rubric [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:185]

### Rank 2. Put a visible title on every diagram, not only when asked

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md` Section 3, `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 6
- **Comes from:** [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/001-design-output/research/corpus/lightspeedwp__.github/plugins/figma/figma-use-figjam/references/plan-board-content.md:84] and [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/001-design-output/research/corpus/lightspeedwp__.github/plugins/figma/figma-generate-diagram/references/workflow.md:70]
- **The gap:** a title is a text node reached only when the gate named an extension [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:150], and nothing says the generator's `name` renders on the board [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:186]
- **What changes:** every write emits one title text node at the board skill's 60 to 96px scale, set from the same string as `name`, and the extension gate treats it as part of the write rather than an addition. Figma treats a title block as needing no inspection, so the extra cost is one write call and no extra read [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/001-design-output/research/corpus/lightspeedwp__.github/plugins/figma/figma-generate-diagram/references/workflow.md:70]
- **Effort:** small
- **Mirror or kernel:** `Product Owner - Templates - Flow Hybrid Workflow.md` and `Product Owner - Templates - Flow Mode.md`. The kernel is unchanged

### Rank 3. Give the board a spacing scale and a proximity ratio

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/style-guide.md` new spacing section, `AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md` recipes, `AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md`
- **Comes from:** [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/001-design-output/research/corpus/lightspeedwp__.github/plugins/figma/figma-use-figjam/references/plan-board-content.md:42], [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/001-design-output/research/corpus/prasantloki__figjam-builder/references/composition-grammar.md:31] and [SOURCE: .skilled/skills/sk-design/sk-design-fundamentals/references/diagnosis-table.md:50]
- **The gap:** every number in the packet is a constant chosen for one recipe, a 250px legend gutter, a 40px sticky clearance and a 24px tint expansion, and none of them states a relationship, so a tint can wrap two nodes that sit far apart and read as one loose rectangle
- **What changes:** state the three board bands once, 60 to 92px inside one thought, 200 to 400px between topics and 1000px or more between parts of the board, add the operative rule that unrelated groups are never closer than the text blocks inside a card, replace the fixed tint expansion with "larger than the group's own internal gap" and put the legend column on the 64px sticky grid Figma publishes [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/001-design-output/research/corpus/lightspeedwp__.github/plugins/figma/figma-use-figjam/references/plan-board-content.md:254]
- **Effort:** small
- **Mirror or kernel:** `Product Owner - Rules - Flow Style Guide.md`, `Product Owner - Templates - Flow Hybrid Workflow.md` and `Product Owner - Rules - Flow Quality Rubric.md`. The kernel is unchanged

### Rank 4. Compose a multi-diagram board instead of appending to it

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md` new section, `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 6 and Section 8, `AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/board-creation/split-flow-one-board.md`
- **Comes from:** [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/001-design-output/research/corpus/lightspeedwp__.github/plugins/figma/figma-use-figjam/references/plan-board-content.md:92] and [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/001-design-output/research/corpus/lightspeedwp__.github/plugins/figma/figma-use-figjam/references/plan-board-content.md:117]
- **The gap:** the only multi-diagram rule is that the work stays on one board through the `fileKey` [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:187], and the split scenario asks only that the two diagrams do not overlap [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md:698]
- **What changes:** a board holding more than one diagram gets a fixed reading direction, a zone heading per diagram carrying an ordinal and the diagram's name, 92px between zones in a row and 120px between rows [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/001-design-output/research/corpus/lightspeedwp__.github/plugins/figma/figma-use-figjam/references/plan-board-content.md:118], and the reply names the zone a reader should open first. The diagram is still never reparented into a section
- **Effort:** medium
- **Mirror or kernel:** `Product Owner - Templates - Flow Hybrid Workflow.md` and `Product Owner - Templates - Flow Mode.md`. The kernel is unchanged

### Rank 5. Define what "better Mermaid" means, and verify lane order

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 5, `AI Systems/Product Owner/sk-create-figjam/references/types/process.md` Section 7
- **Comes from:** [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/001-design-output/research/corpus/lightspeedwp__.github/plugins/figma/figma-generate-diagram/references/workflow.md:148] and [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/process.md:82]
- **The gap:** the fix for a cramped diagram is described as reshaping the model [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:164], and no file says which levers survive on an ELK layout or that the check never reads lane order, though the type file asks lanes to follow the order work reaches them
- **What changes:** one table states the levers that do something, which are direction, node declaration order, the edge set and subgraph presence, with the limits that `&` does not group, invisible links move nodes unpredictably and a length hint is a dagre feature. The process read-back gains a lane order comparison, so a process that renders its lanes in reverse is caught rather than passed
- **Effort:** small
- **Mirror or kernel:** `Product Owner - Templates - Flow Mode.md` and `Product Owner - Templates - Flow Type - Process.md`. The kernel is unchanged

### Rank 6. Make the legend the board's key, and give tints a second channel

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md` Section 3, `AI Systems/Product Owner/sk-create-figjam/references/style-guide.md` Section 2, `AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md`
- **Comes from:** [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:358], [SOURCE: .skilled/skills/sk-design/sk-design-fundamentals/references/color-system.md:126] and [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/foundations/style-guide.md:143]
- **The gap:** the legend covers annotated nodes only and is a column of numbered stickies [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:66], while the tint recipe says to add no legend at all [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:144], so a board using four shapes and two tints explains none of them
- **What changes:** a legend enumerates every shape, tint and dash the board actually uses and appears once a board uses three or more shape kinds. The tint takes a lighter fill than the accent it borrows and adds a dash pattern to its stroke, which the palette already carries for optional and security treatments, so membership survives greyscale. The "add no legend" sentence is replaced rather than left standing beside a new default
- **Effort:** medium
- **Mirror or kernel:** `Product Owner - Templates - Flow Hybrid Workflow.md`, `Product Owner - Rules - Flow Style Guide.md` and `Product Owner - Rules - Flow Quality Rubric.md`. The kernel is unchanged

### Rank 7. Add reading distance as the third dial

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` Section 4 and the budget sections of `AI Systems/Product Owner/sk-create-figjam/references/types/*.md`
- **Comes from:** [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/001-design-output/research/corpus/prasantloki__figjam-builder/references/typography-grammar.md:24] and [SOURCE: .skilled/skills/sk-design/sk-design-diagram/references/foundations/output-spec.md:81]
- **The gap:** the packet holds that "A FigJam board fixes the format and the size, so two remain" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:148], yet the generator's font cannot be changed afterwards [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:128], so a board read on a wall keeps laptop type
- **What changes:** a third dial records where the board will be read, and it moves node count and label length rather than font size, because that is the only lever left. A wall board gets fewer nodes and shorter labels, and the gate states which dial setting it used
- **Effort:** medium
- **Mirror or kernel:** `Product Owner - Templates - Flow Mode.md` and the seven `Product Owner - Templates - Flow Type - *.md` files. The kernel is unchanged

### Rank 8. Measure the graph before the write, not after

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py`, a new `AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/layout.py`, `AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md`
- **Comes from:** [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:129] and [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/common.py:21]
- **The gap:** `check_block` returns a profile, a size summary and a direction, which is a node count and a connector count, and the scorecard's Layout dimension is a crossing counter [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md:81], so two models of nine nodes pass the same test whether one is calm and the other unreadable
- **What changes:** the same parse also reports rank width, edges per node, longest path, total label characters against the 40 character cap already held in `MAX_LABEL_CHARS`, and an estimate of edge pairs that must cross. A number out of band is fixed in the model before a write is spent
- **Effort:** large
- **Mirror or kernel:** no Project file follows, because the checker and its planted fixtures are skill side only and no knowledge file mirrors a script

### Rank 9. Rebuild the scorecard around composition, at two zooms

- **Changes:** `AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md` Section 3, `AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/board-quality/*.md`, `AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md`
- **Comes from:** [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/001-design-output/research/corpus/prasantloki__figjam-builder/references/composition-grammar.md:110], [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/001-design-output/research/corpus/prasantloki__figjam-builder/references/composition-grammar.md:101] and [SOURCE: .skilled/skills/sk-design/sk-design-fundamentals/references/review-checklist.md:149]
- **The gap:** a board is scored from one screenshot at 100% zoom [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md:80], Clarity asks three content questions a reader can answer in any order [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/board-quality/user-flow-board-quality.md:31] and Hygiene puts four independent invariants on one bit [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md:84], so an unexamined dimension scores a silent 2
- **What changes:** an overview screenshot joins the reading zoom, a Composition dimension tests the planned glance order against the actual one, crossings, shared trunks and label collisions are scored apart, Hygiene splits into its four checks, and every lost point carries a location and a fix. The floor plus mandatory dimensions shape stays
- **Effort:** medium
- **Mirror or kernel:** `Product Owner - Rules - Flow Quality Rubric.md`. The playbook has no Project counterpart, so no other Project file follows

## 4. Rejected ideas

- **Wrapping a generated diagram in a section, including from the selection menu.** The plugin route reparents, and reparenting makes coordinates parent relative and recreates connectors [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/001-design-output/research/corpus/lightspeedwp__.github/plugins/figma/figma-use-figjam/references/position-figjam-nodes.md:85]. Wrapping a selection is a person's UI action that no tool call performs, and the earlier research already rejected it [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/research.md:216]
- **Replacing the generator's layout with an editorial one.** The comparator's own rule [SOURCE: .skilled/skills/sk-design/sk-design-diagram/SKILL.md:279] cannot apply, because the architecture layout is the only way that type draws [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/architecture.md:16]. The transferable intent, that automatic spacing must respect grouping, survives in Rank 3
- **Re-adding the 4px grid, node sizes, the type ramp or the horizontal legend strip.** The packet records each omission with its reason [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:129]
- **Adopting the 1200px overview figure as a board constant.** It assumes a wrapper the packet does not own, so Rank 7 takes the method and not the number [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/001-design-output/research/corpus/prasantloki__figjam-builder/references/typography-grammar.md:24]
- **A floating point quality score.** A decimal built from seven judgements reads as precision the evidence cannot support
- **Letting the checker score the board.** The checker sees Mermaid text and the board is an image plus a node list, so computed measures belong before the write and reader measures belong in the playbook
- **Asking for a second page.** `figma.createPage()` throws in a FigJam file [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:52]

## 5. Corrections to the iterations

- Iteration 002 finding 4 and the draft's Rank 4 say the packet names no model side cause of a tangled route. The playbook already names declaration order and a long label [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/board-quality/user-flow-board-quality.md:79]
- Iterations 001, 002 and 003 say nothing at board level asks where the eye lands. The rubric already asks that the accent reads first with no competitor [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:83], so Rank 1 is about a written plan, not a missing check
- Iteration 002 finding 3 presents the missing zoned mode as an unnoticed gap. The packet says it outright [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:150]
- Iteration 002 finding 11 cites `style-guide.md:63` for the departure table. That line is a palette row and the table is at line 115 [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:115]
- Iteration 002 finding 3 cites `flow-mode.md:170` for "Over budget, split rather than shrink". The sentence is at line 162 and line 170 holds the split order [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:162]
- Iteration 003 finding 14 says Figma's fallback archetype only asks for distinct fills. Figma names green Yes and red No pills, an octagon for blockers and a diamond for decisions [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/001-design-output/research/corpus/lightspeedwp__.github/plugins/figma/figma-use-figjam/references/plan-board-content.md:244], so the packet is ahead on label discipline, not on shape vocabulary
- Iteration 005 finding 5 cites a `fileProtection` block at `flow-mode.md:246`. No such block exists in the packet and line 246 is the no-export rule. The case for splitting Hygiene stands on the scorecard text alone [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md:84]
- Iteration 005 findings 7 and 9 and the draft's Rank 10 say the playbook keeps no score series. The playbook requires every run's outcome and evidence under a dated report folder [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md:28], and one such run exists [SOURCE: AI Systems/Product Owner/benchmark/reports/2026-10-20--manual-testing-playbook--sk-create-figjam-shell/manifest.json:2]. Rank 10 is dropped
- Iteration 005 finding 7 cites `SKILL.md:198` for the shipped examples. Line 198 is the flow check pointer and the examples line is 154 [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:154]
- The draft's withdrawal of iteration 004 finding 2 is correct and stays withdrawn. A selection wrap is not a route the packet can take

## 6. Claims not verified

These cite a URL I cannot open here, so each rests on the quoting iteration and is kept only for that reason. The Figma help pages on sections, pages and accessible boards, quoted in iterations 004 and 005. The Mermaid layout note at `https://line9.ai/mermaid/layout`, which carries the sibling subgraph reversal, the `&` limit and the ELK length hint used in Rank 5. The Mermaid direction guidance at `https://mermaid.ai/docs/build-and-edit/write-diagram-syntax`. The IBM technical diagram page on pairing colour with line styles. The Dell EMC deck on macro and micro whitespace. The architecture deck quoted for "understand our diagram in seconds". The `node-link-and-diagram-layout` skill page. Because the section and page pages are unreadable here, iteration 004 finding 1, which calls the one page sentence half wrong, is not ranked. The sentence stands as written.

## 7. Sources

**Packet**
`AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md`, `references/hybrid-workflow.md`, `references/style-guide.md`, `references/quality-rubric.md`, `references/types/user-flow.md`, `types/process.md`, `types/architecture.md`, `scripts/flow_check.py`, `scripts/figjam_checks/common.py`, `manual-testing-playbook/manual-testing-playbook.md`, `manual-testing-playbook/board-quality/user-flow-board-quality.md`, `SKILL.md`. Kernel line 185 of `AI Systems/Product Owner/claude project/Custom Instructions.md`

**Comparators**
`.skilled/skills/sk-design/sk-design-diagram/SKILL.md`, `references/foundations/output-spec.md`, `references/foundations/style-guide.md`, `.skilled/skills/sk-design/sk-design-fundamentals/references/diagnosis-table.md`, `color-system.md`, `review-checklist.md`

**Corpus**
`AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/001-design-output/research/corpus/lightspeedwp__.github/plugins/figma/figma-use-figjam/references/plan-board-content.md`, `position-figjam-nodes.md`, `.../figma-generate-diagram/SKILL.md`, `references/workflow.md`, `AI Systems/Product Owner/specs/017-figjam-flow-generation/030-figjam-research-three/001-design-output/research/corpus/prasantloki__figjam-builder/references/composition-grammar.md`, `typography-grammar.md`

**Prior research**
`AI Systems/Product Owner/specs/017-figjam-flow-generation/009-figjam-skill-research/research/research.md` and `016-figjam-improvement-research/research/research.md`, whose ranks 1 to 17 are implemented and none of which is re-proposed here

**URLs cited above and unverified in this session**
`https://line9.ai/mermaid/layout`, `https://mermaid.ai/docs/build-and-edit/write-diagram-syntax`, `https://help.figma.com/hc/en-us/articles/4939765379351-Organize-your-FigJam-board-with-sections`, `https://help.figma.com/hc/en-us/articles/24005082123159-Create-and-manage-pages-in-FigJam`, `https://help.figma.com/hc/en-us/articles/14477101678359-Create-accessible-FigJam-boards`, `https://www.ibm.com/design/language/infographics/technical-diagrams/design/`, `https://learning.dell.com/content/dam/dell-emc/documents/en-us/2015KS_Pantyukhin-Principles_of_Design_Diagramming.pdf`, `https://www.lasssim.com/wp-content/uploads/2022/06/WeAreDevelopers_Lasselsberger_Simon_220610.pdf`, `https://github.com/openai/plugins/blob/main/plugins/build-web-data-visualization/skills/node-link-and-diagram-layout/SKILL.md`
