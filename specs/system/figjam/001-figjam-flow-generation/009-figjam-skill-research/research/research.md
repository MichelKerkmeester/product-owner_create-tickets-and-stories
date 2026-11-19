# What Flow Mode should adopt from public FigJam diagram skills

Twenty iterations compared Product Owner's Flow Mode with eight pinned public repositories and one repository found during the run. This synthesis rechecked every finding it uses. It opened the cited corpus line and the Flow Mode line each finding would change. It also ran `flow_check.py` against planted models to test claims the iterations made about the check. Nothing here was observed on a live FigJam board.

---

## 1. Summary

Three changes matter most.

1. **Stop writing to a page.** FigJam files have one implicit page. The plugin API cannot create another. Flow Mode should write the first diagram of a flow into a new FigJam file. Every later diagram and revision should pass that file's `fileKey`. A rollback should remove only what the write created. Nine lines across the skill, its Project mirror and the kernel state the page rule today.
2. **Teach the check the generator's hard limits.** Figma's own skill says the tool rejects emoji and that `end`, `subgraph` and `graph` must not be node IDs. It warns that underscores in node IDs can break edge routing. A model with any of the three passes `flow_check.py` today.
3. **Make the read-back structural.** Read the board with `get_figjam`, then check that each connector joins the same two nodes the model joins. Counting connectors cannot tell a correct wiring from a swapped one.

---

## 2. Verdicts on the four known gaps

### (a) One implicit page, and figma.createPage throws

**Verdict: adopt.** The new-page target and the page-clearing rollback should go.

- Figma's FigJam skill says `figma.createPage()` throws in FigJam. It says FigJam files have a single implicit page and that content is organised with sections [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md:13]. The diagram skill repeats the warning for any `use_figma` step that follows a diagram [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:57].
- The hosted tool creates its own file, so calling `create_new_file` first is wrong [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:92]. Every call without a `fileKey` creates a new file in the user's drafts [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:102]. A call with a `fileKey` adds the diagram to that file [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:109]. To replace a diagram, delete its old nodes through `use_figma` and regenerate with the same `fileKey` [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:110].
- Flow Mode's gate names a "plan, file and page" and requires a new or confirmed-empty page [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:63]. Its write bullet and its rollback both rest on that page [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:115] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:117]. Its recovery re-runs the write "into a cleared page" [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:159].
- The Project mirror repeats all four lines [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:41] [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:93] [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:95] [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:127]. The kernel names "file and page" and "a new or confirmed-empty page" in one line [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:249].
- On a file with one page, clearing the page clears the whole board. The rule's own safeguard then stops the write on any board that holds other work.
- IamTheLime says a board can hold several pages, listed through `figma.root.children` [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/references/api-notes.md:20]. It agrees that no page can be created from a plugin [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/references/api-notes.md:18]. The two sources disagree on whether extra pages exist. They agree that Flow Mode cannot create one. That is the point the rule depends on.

The replacement keeps the gate's intent with the file as the unit. The gate names the plan and either a new file or the `fileKey` of a board this flow already wrote. For a new file, the write is the whole file, so no other work is at risk. For an existing file, the rollback deletes only the nodes this write created, after a read with `get_figjam` [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md:17].

Section wrapping should not be the default replacement. ompug wraps each generated diagram in a section by moving its top-level nodes into it [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/scripts.py:150-159]. Flow Mode forbids moving a generated node [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:103] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:116]. Iteration 19 proposed one allowed move to resolve this. A file per flow gives the same isolation without an exception to the never-move rule.

The `fj` rollback duplicates the page before the first write [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:127]. Whether that works on a FigJam file was not established. It stays unchanged here and is listed in section 6.

### (b) Emojis in Mermaid source

**Verdict: adopt, as an error on the whole Mermaid block.**

- Figma's universal constraint 1 is "No emojis in any part of the Mermaid source. The tool rejects them" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:49]. Its label audit repeats it [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:318]. rocket-path states it for every diagram type [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md:41].
- ompug raises an error on any source line that matches its emoji pattern [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:150-151]. The pattern covers the pictograph planes, dingbats, technical symbols, variation selectors and the zero-width joiner [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/sanitize.py:173-185].
- A model with an emoji in a node label and in an edge label passed `flow_check.py` in the probe. The check's markup list holds only angle brackets, a newline, double asterisks and a backtick [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:44].
- Scan the raw block rather than the cleaned labels. The vendor rule covers the whole source. ompug scans every line. Reuse ompug's pattern rather than drafting a narrower one.

### (c) Reserved node IDs end, subgraph, graph

**Verdict: adopt, matched without regard to case.**

- Figma says not to use `end`, `subgraph` or `graph` as node IDs [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:52] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:322].
- ompug raises an error on those three and on eight Mermaid keywords, including `style`, `class`, `click` and `default` [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:37-47]. It lowercases the ID before it compares [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:520-524].
- Node IDs named `end` and `graph` both passed `flow_check.py` in the probe.
- rocket-path bans `end` in state-diagram class names [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md:79]. That shows the word is hazardous elsewhere. It is not evidence about flowchart node IDs.

### (d) Underscores in node IDs

**Verdict: adopt, as an error.**

- Figma asks for camelCase IDs and warns that "Underscores can break edge routing in some processors" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:53] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:321]. The wording is hedged. This is a precaution against a named failure, not a certain rejection.
- ompug makes an underscore an error and a non-camelCase ID only a warning [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:525-532].
- Mermaid Jam accepts underscores in Mermaid node IDs [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/parser/mermaidJam.ts:1001]. The corpus is not unanimous. The hosted tool is Flow Mode's target. Its vendor names the risk, so the vendor wins.
- The cost is low. The templates already ask for short, stable IDs [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md:33]. No shipped pattern uses an underscore.
- Skip the camelCase warning. The check has a pass or fail exit and no warning channel [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:28].

---

## 3. Verdicts on the five deliberate limits

### Top to bottom only

**Verdict: loosen.**

- **Why it exists:** Flow Mode states the rule without a reason [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:100]. The check's docstring does the same [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:18].
- **Corpus:** Figma makes `flowchart LR` the default for sequential processes and most two or three level decision trees [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:26]. It switches to `TD` for deep narrow trees or many siblings at one level [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:27]. rocket-path defaults to LR and uses TD for decision trees [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md:47]. ompug accepts five directions [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:211]. Mermaid Jam accepts the same five [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/parser/mermaidJam.ts:113]. No source mandates TD.
- **Recommendation:** keep TD as the default and let the check accept LR. Require one direction across all diagrams of one flow, in line with Figma's "Never change direction mid-diagram" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:29]. If TD serves a reason the file does not record, write that reason down and keep the rule. This verdict rests on missing rationale, not on a defect.

### At most 9 nodes

**Verdict: keep.**

- **Why it exists:** a longer flow is split into diagrams that hand off through a named end and start [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:99].
- **Corpus:** Figma calls about 20 nodes usually fine [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:329]. Its checklist asks for about 25 or fewer [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:350]. ompug's readability limit is about 25 nodes [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/references/diagram-types.md:32]. rocket-path's hand-written process flowcharts have 9 and 8 nodes [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/references/examples.md:20-31] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/references/examples.md:35-45].
- **Recommendation:** nine sits well inside every cap and matches what a hand-drawn user flow uses. It also keeps an exact read-back cheap. Add ompug's rule that a split names anything it leaves out (ranked change 10).

### At most 3 exits per decision

**Verdict: keep.**

- **Why it exists:** a fourth outcome means the decision is two decisions [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:98].
- **Corpus:** no source sets an exit cap. rocket-path's decision examples use two or three exits and never four [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/references/examples.md:92-97] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/references/examples.md:104-106] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/references/examples.md:113-117].
- **Recommendation:** nothing in the corpus argues for more exits. The check is exact and costs nothing [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:68-74].

### One accent colour

**Verdict: keep, counted as one hex value.**

- **Why it exists:** colour marks the happy path or one decision, never a category scheme [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:102].
- **Corpus:** Figma allows colour for status, ownership and subsystem grouping [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:267-271]. It also says not to paint every node and not to rely on colour alone [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:275-277]. IamTheLime puts all emphasis on one main colour and bans a second accent family [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/SKILL.md:19-25]. Its palette still keeps note and warning roles [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/references/themes.md:27-28].
- **Recommendation:** keep one hex. Iteration 12 withdrew iteration 10's "accent family" idea. The withdrawal holds. A family needs a palette or a role map. Flow Mode has neither.
- **One detail for the templates:** Figma pairs each fill with a darker stroke [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:285-293]. The check counts a `linkStyle` stroke as a colour [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:47]. A node fill and a connector stroke taken from one vendor pair therefore count as two. The good fixture avoids this by using one hex for both [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:115-116]. The templates should say so.

### Four shapes

**Verdict: keep.**

- **Why it exists:** shapes carry the type. No other shape is allowed [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:97].
- **Corpus:** Figma's table lists only shapes that render as a distinct FigJam shape. Rectangle, stadium, circle and diamond are all in it [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:37-41]. Most other Mermaid shapes fall back to a plain rectangle [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:33]. rocket-path advertises a "full range" that includes `flag` [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md:52]. Figma lists `flag` among the shapes that render as plain rectangles [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:58].
- **Recommendation:** keep the four. Figma reads the circle as an entry or exit point [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:40], while Flow Mode uses it as a merge dot. Figma also lists a summing-junction shape for merges [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:56]. How either renders as a small merge dot was not observed, so the current circle stays.

---

## 4. Ranked improvements

The order weighs three questions. Does the current rule fail on the vendor's own terms? Does the failure lose work or only a call? How cheap is the proof?

### 1. Replace the page target and rollback with a file target

- **Changes:** the gate [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:63], the hosted write and rollback bullets [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:115] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:117] and the recovery step [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:159].
- **Comes from:** [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md:13] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:102] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:109-110].
- **What changes:** the gate names the plan and either a new file or the `fileKey` of a board this flow already wrote. A flow's first diagram is written without a `fileKey`, which creates a new file. The rollback for a new file is that file. The rollback for an existing board deletes only the nodes this write created, after a `get_figjam` read. The recovery step takes Figma's replacement recipe: delete the old diagram's nodes, then regenerate with the same `fileKey`.
- **Why first:** it is the only Flow Mode rule that is impossible on the vendor API and can destroy other work on a shared board.
- **Mirror and kernel:** both. The mirror's gate, write, rollback and recovery lines change the same way [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:41] [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:93] [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:95] [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:127]. The kernel line changes too [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:249]. Its H1 version moves in the same change [SOURCE: AI Systems/Product Owner/SYNC.md:17].

### 2. Add emoji, reserved-ID and underscore errors to the check

- **Changes:** the constants [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:40-47], `diagram_problems` [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:57-80], the planted models [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:119-151] and the docstring [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:18-25]. The rule list gains the three rules. The sentence that says the check enforces "the first six rules" must be recounted [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:95].
- **Comes from:** [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:49] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:52-53] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:37-47] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:520-530] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/sanitize.py:173-185].
- **What changes:** three conditions, each with its own planted model. The emoji test runs on the raw block with ompug's pattern. The reserved-ID test lowercases each node ID and compares it with ompug's two sets. The underscore test looks for `_` in each node ID.
- **Why second:** each rule guards a failure the vendor names. All three pass today. Each is one constant and one condition. The self-test proves each one. Its baseline is 8 of 8 passing.
- **Mirror:** yes. A Project checks the model rule by rule [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:40], so the mirror's rule list needs the same three rules [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:73-81]. The kernel needs no change.

### 3. Keep every diagram of a flow in one file, and name each one

- **Changes:** the one-diagram-per-call bullet [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:114] and the split pattern [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md:86-101].
- **Comes from:** [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:84] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:102-105] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:339].
- **What changes:** after the first call, every later diagram of the same flow and every revision passes the returned `fileKey`. Each diagram gets a distinct `name` that matches its hand-off.
- **Why third:** Flow Mode sends one diagram per call. Each call without a `fileKey` makes its own draft file. A split flow therefore lands in as many files as it has diagrams, while the reply promises one board URL [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:139]. The fix is one sentence. It ranks below change 2 because it scatters a flow rather than failing a call.
- **Mirror and kernel:** the mirror's connector route changes [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:92]. The kernel's "one diagram per call" clause should add "into the same file", in the same edit as change 1 [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:249].

### 4. Make the read-back structural, with a connector endpoint check

- **Changes:** the read-back step [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:65], the read-back line [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:140] and the reply shape [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md:120-124].
- **Comes from:** `get_figjam` is FigJam's inspection tool, `get_metadata` fails on boards and `get_screenshot` needs a real node ID [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md:17-21]. A whole-page `get_figjam` can exceed the response limit [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/references/api-notes.md:11-13]. southleft reads each connector's start and end node [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/references/figjam-snippets.md:219-236]. Labor checks that connector endpoints are correct [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md:127-133]. parse-figjam derives direction from the endpoint IDs and caps [SOURCE: https://github.com/rrichardsonv/parse-figjam/blob/2722e73738b7eac17a0fbe67eacb180a5e7ae4aa/SKILL.md:44-50].
- **What changes:** the read-back uses `get_figjam` scoped to the written diagram, never the whole page. For each model edge, it confirms that a connector joins the matching board nodes in the same direction with the same label. A screenshot of that diagram's node then checks stretching and overlap. When only a visual read is available, the line says the read was visual.
- **Why fourth:** a swapped branch passes a count today. Flow Mode already names missing or extra items on a mismatch [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:142], so the new part is the endpoint check and the tool recipe. It ranks below changes 1 to 3 because it improves the proof of a write rather than preventing a bad one. The fields `get_figjam` returns for connectors were not observed on a live board.
- **Mirror:** yes, the mirror's read-back step and delivery section [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:43] [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:103-113]. Whether the claude.ai connector offers `get_figjam` is unverified. The kernel names the `Read-back:` line without its contents, so it needs no change.

### 5. Treat a failed or timed-out hosted call as uncertain

- **Changes:** a new bullet in the hosted route [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:111-117] and the read-back recovery [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:157-159].
- **Comes from:** ompug records each counted action before it runs. An action whose outcome is unknown is reconciled with `get_figjam`, or with a question to the user, before any retry [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:3-7] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:255-261].
- **What changes:** a failed or timed-out `generate_diagram` call is not proof that nothing landed. Read the target file before a retry. Retry only when the diagram is absent.
- **Why fifth:** a blind retry puts a second copy on the board, the duplicate Flow Mode already warns about [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:159]. The rule is one sentence and needs no tooling. It ranks below change 4 because a failed call is rarer than a write.
- **Mirror:** yes, the mirror's connector route and recovery [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:87-95] [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:125-127]. The kernel needs no change.

### 6. Decide the edge vocabulary and enforce it

- **Changes:** the edge loop in the check [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:77-79] and a new bullet in the rule list [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:97-103].
- **Comes from:** Figma's stroke, end-cap and both-ended tables give each operator its own meaning [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:73-95]. The extractor already records style, arrowhead and direction for every edge [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/vendored/mermaid_extract.py:648-656].
- **What changes:** in the probe, `---`, `<-->`, `-.->`, `==>`, `--x` and `--o` all passed. Allow only the solid one-way `-->`. Figma gives dotted the meaning "optional or happens later" and thick the meaning "critical path" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:78-79]. Flow Mode already puts a proposal's status in the label [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:88]. It already marks the happy path with its one accent [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:102]. A second channel for the same meaning would break the one-emphasis rule. Undirected and two-way edges do not fit a flow whose connectors mean "then". The error message should name the alternative.
- **Why sixth:** the gap is confirmed, but the rule is a house choice. Figma supports every one of these operators. Its own complete example uses dotted edges [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:376]. Iterations 18 to 20 ranked this first. That ranking rested on a frequency claim nobody measured and on a false statement that no corpus flowchart uses dashed edges.
- **Mirror:** yes, the mirror's rule list [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:73-81]. The kernel needs no change.

### 7. Move the markup check onto the raw block

- **Changes:** the markup marks [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:44], the two label tests [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:66-67] [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:77-79] and the docstring line [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:23].
- **Comes from:** the extractor strips tags and emphasis before the check sees a label [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/vendored/mermaid_extract.py:241-246]. ompug's HTML-tag error runs on the raw line [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py:154-158]. Figma bans HTML tags in labels [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:51].
- **What changes:** in the probe, a label with `**bold**` and `<b>tag</b>` passed. Scan the raw block for an HTML tag and for `**`. Do not scan for a bare angle bracket, because arrow operators contain one. Keep the newline test on the cleaned label, which already works [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:139-141].
- **Why seventh:** the generator drops markup rather than rejecting it [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:101], so the cost of the gap is a plain label where the author expected formatting. A rule that cannot fire still misleads whoever reads it.
- **Mirror:** no. The mirror states the rule, not the script.

### 8. Reject orphan nodes

- **Changes:** `diagram_problems` and the planted models [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:57-80], plus the rule list [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:97-103].
- **Comes from:** Figma's checklist asks that every node has at least one incoming or outgoing edge [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:344].
- **What changes:** in the probe, a model with an unconnected node passed. A node with no edge fails the check.
- **Why eighth:** an unconnected node sits loose on the board. The read-back counts it as part of the flow. The test is one condition. No iteration raised it.
- **Mirror:** yes, the mirror's rule list [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:73-81].

### 9. Stop regenerating after two attempts

- **Changes:** the read-back recovery [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:157-159].
- **Comes from:** after two dissatisfying attempts at the same diagram, stop and ask what is wrong [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:98].
- **What changes:** the recovery step gains a limit of two attempts per diagram, then one question.
- **Why ninth:** it bounds a retry loop the current recovery leaves open. It is cheap. It matters only after something has already gone wrong.
- **Mirror:** yes, the mirror's recovery [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:125-127].

### 10. Name what a split leaves out

- **Changes:** the node limit rule [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:99] and the split pattern note [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md:86-88].
- **Comes from:** ompug splits an oversized diagram into parts and names anything left out, "never dropped silently" [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/references/diagram-types.md:33-34].
- **What changes:** when a flow is split, every source step either appears in one diagram or is named as left out.
- **Why tenth:** the provenance table maps each node to a source [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md:107-114]. A step that falls between two diagrams has no node and no row. Nothing reports it. The rule is cheap, but no script can check it.
- **Mirror:** yes, the mirror's rule list and the Project's Flow Templates split pattern [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:77] [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Assets - Flow Templates.md:68].

### 11. Add a hosted-route preflight

- **Changes:** the first two hosted-route bullets [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:113-114].
- **Comes from:** Figma requires its diagram skill before every `generate_diagram` call [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:8]. ompug calls `whoami` for the plan key and asks the user when several plans exist [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:9]. Its driver states that `generate_diagram` wants a `planKey` when the user is signed in [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/driver.py:582].
- **What changes:** before the first call, load Figma's diagram skill where the runtime offers it. Use `whoami` to list the plans and pass the plan the gate named.
- **Why eleventh:** Flow Mode already says to name the plan, but not how the call carries it. The `planKey` field appears in ompug's driver and not in Figma's own parameter list [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:83-90], so it is unverified on the live server.
- **Mirror:** only if the claude.ai connector exposes the same tools, which is unverified.

### 12. Bound label length

- **Changes:** the label rule [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:101] and the label tests in the check [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:66-79].
- **Comes from:** Figma asks for node and edge labels of one to four words [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:315-316]. It warns that long labels stretch shapes [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:320]. ompug truncates generated labels at 80 characters [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/build.py:25]. Mermaid Jam shortens them at 120 [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/shared/reviser.ts:17].
- **What changes:** the rule states Figma's short-label guidance. The check adds a hard character cap as a backstop. The number is open. Eighty is ompug's truncation constant, not a measured board limit. The cap must pass the shipped patterns, whose longest label runs to five words [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md:82].
- **Why twelfth:** a long label hurts readability but never fails a call.
- **Mirror:** yes, the mirror's label rule [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:79].

### 13. Quote labels that carry special characters

- **Changes:** the usage notes and patterns [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md:31-35].
- **Comes from:** Figma requires quotes around labels with parentheses, colons or slashes [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:54]. rocket-path quotes every label [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md:48-50].
- **What changes:** a label with a parenthesis, a colon or a slash is written in double quotes. In the probe, quoted labels parsed and passed the check.
- **Why thirteenth:** it is a vendor constraint. Frame text retyped into the model can carry these characters [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:82]. No failure from it was observed, so it ranks low.
- **Mirror:** yes, the Project's Flow Templates usage notes [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Assets - Flow Templates.md:13].

### 14. Say plainly that subgraphs are not allowed

- **Changes:** the unknown-shape message [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:64-65], the planted models [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:119-151] and the shapes rule [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:97].
- **Comes from:** Figma reserves subgraphs for three or more related nodes and asks for a tinted fill on each [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:146-147] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:161]. A tint per subgraph collides with the one-accent rule. Mermaid Jam rejects subgraphs [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/parser/mermaidJam.ts:23].
- **What changes:** in the probe, a subgraph already fails, reported as a node with "the unknown shape container". The extractor models a subgraph as a container node [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/vendored/mermaid_extract.py:759-767]. Give it its own message and a planted model.
- **Why fourteenth:** behaviour does not change. Only the message and the proof improve.
- **Mirror:** only if the rule text changes.

### 15. Guard the `fj` route

- **Changes:** the `fj` route [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:121-127].
- **Comes from:** southleft and Labor confirm the open file is a FigJam board before any write [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/SKILL.md:22-23] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md:13]. FMCP says FigJam shapes default to Inter Medium, so loading Inter Regular is not enough [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md:59-65].
- **What changes:** confirm the open file is a FigJam board before the first `fj` write. The vendored packet lists `fj info` as a read-only verb [SOURCE: AI Systems/Product Owner/mcp-figma/references/tool-surface.md:149]. The font rule applies only if `fj` verbs do not load fonts themselves, which is unverified.
- **Why last:** it guards the fallback route. The vendored `mcp-figma` packet owns that route's mechanics [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:121].
- **Mirror:** no. A Project has no `fj` route [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:99].

### Considered and not ranked

- **Section wrapping per diagram.** It moves generated nodes, which Flow Mode forbids. Change 1 gets the isolation at the file level instead.
- **Subgraph support.** Iteration 12 rejected it. That verdict holds. Figma couples subgraphs to tinted fills and per-subgraph direction [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:169-175]. Each collides with an existing Flow Mode rule.
- **A label-repair pass.** Mermaid Jam and ompug repair labels before they render [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/shared/reviser.ts:133-141] [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/sanitize.py:307-315]. Flow Mode labels carry provenance, so a silent rewrite would break the link between a node and its source.

---

## 5. What the research changed its mind about

These reversals happened inside the twenty iterations.

- **Page existence, iteration 2.** Iteration 1 read Figma as saying there is no page at all. Iteration 2 found IamTheLime's note that a board can hold several pages. The claim narrowed to "no page can be created".
- **Executable checks, iteration 8.** Iteration 7 called ompug's linter the only other executable pre-write check. Iteration 8 added Mermaid Jam's parser diagnostics, which refuse generation on any error [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/src/parser/mermaidJam.ts:143-144].
- **Accent family, iteration 12.** Iteration 10 proposed counting an accent family instead of a hex. Iteration 12 withdrew it, because a family needs a palette Flow Mode does not have.
- **Subgraph support, iteration 12.** Iterations 8 and 11 left subgraphs open. Iteration 12 rejected them.
- **The markup rule, iteration 13.** Earlier iterations trusted the markup list. Iteration 13 found that the extractor strips tags and emphasis first, so those marks never fire. It also found that edge operators are never checked.
- **Raw-text scan, iteration 14.** Iteration 14 dropped iteration 13's plan to scan raw text for bare angle brackets, because arrow operators contain them.
- **Reserved-ID case, iterations 14 and 19.** Iteration 14 chose exact matching. Iteration 19 switched to case-insensitive matching to follow ompug.
- **The `fj` rollback, iteration 15.** Iteration 15 first rewrote the `fj` page duplication, then kept it as route-specific.
- **Page statement count, iteration 16.** Iteration 16 raised iteration 15's count of seven by adding the two recovery lines. Its total of eight was itself an arithmetic slip. The correct count is nine.
- **Edge rule first, iteration 18.** Iteration 18 put the edge-operator rule above the page rule.
- **Emoji range, section placement and `fileKey`, iteration 19.** Iteration 19 replaced a hand-drafted emoji range with ompug's pattern. It found that section placement moves generated nodes. It moved `fileKey` reuse from rank 10 to rank 3.

This synthesis changed four more conclusions.

- **The edge rule falls from first to sixth.** Figma documents dotted, thick, plain and two-way edges [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:73-95]. IamTheLime uses dashed lines for asynchronous flow [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/SKILL.md:168-169]. Mermaid Jam supports dotted and thick edges [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/memi-design__mermaid-jam/README.md:36].
- **Subgraphs already fail the check.** Iterations 13 and 18 said a subgraph passes silently. The probe shows it fails as an unknown shape.
- **Flow Mode already names missing and extra items.** Iterations 9, 11 and 16 said the read-back could not. The rule is in place [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:142].
- **Section wrapping is not the page replacement.** Iterations 11 to 20 built the replacement around sections. A file per flow does the same job without moving generated nodes.

---

## 6. Claims that could not be verified

Nobody should act on these as fact.

- **Live generator behaviour.** No board was written. That emoji, reserved IDs and underscores fail on the hosted tool today rests on Figma's documentation, not on an observed call.
- **How the merge dot renders.** Whether `((.))` renders as a small dot on the hosted generator was not observed.
- **Distinct dotted and thick edges.** Figma's table says they render distinctly. It was not observed.
- **How many pages a board holds.** Figma says a single implicit page. IamTheLime says several. Neither was tested.
- **The `fj` page duplication rollback.** Whether a FigJam page can be duplicated in Desktop before an `fj` write was not established.
- **The claude.ai connector's tools.** Whether the Project's Figma connector exposes `use_figma`, `get_figjam` or `whoami` is unknown. Changes 4, 5 and 11 depend on it inside a Project.
- **Atomic hosted calls.** southleft describes atomic `use_figma` scripts [SOURCE: specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/SKILL.md:16]. Whether a failed `generate_diagram` call can leave a partial diagram is unknown.
- **The `planKey` parameter.** It appears in ompug's driver and not in Figma's skill.
- **Fonts on `fj`.** Whether `fj` verbs load fonts themselves is unknown.
- **The parity gate state.** Iteration 17 said the parity gate exits 2 because a declaration file differs from its committed revision. This synthesis did not rerun that gate. It did confirm that the five Flow Mode files are untracked in the Product Owner repository at the time of writing.
- **Proposed version numbers.** Iterations 17 and 20 proposed specific kernel and skill version numbers. Version policy is the operator's call. The numbers are dropped.
- **Edge-operator frequency.** Iteration 18 claimed a habitual `---` happens often. Nobody measured it.
- **Search completeness.** Iteration 10 said broader GitHub searches found no other skill repositories. That was not repeated.
- **Registry counts.** The lineage draft reports 235 deduplicated findings and five of five questions resolved. Neither was checked.
- **Timestamps.** The DeepSeek state log carries timestamps later than the run's real end. No claim here depends on any of them.

---

## 7. Sources

### Corpus, pinned

| Repository | Pinned commit | Files used |
|---|---|---|
| figma/mcp-server-guide | 7047cb45 | `corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md`, `references/flowchart.md`, `skills/figma-use-figjam/SKILL.md` |
| IamTheLime/dotfiles | 77976c17 | `corpus/IamTheLime__dotfiles/agents/skills/figjam-diagrams/SKILL.md`, `references/api-notes.md`, `references/themes.md` |
| southleft/figma-console-mcp-skills | 807fcc1c | `corpus/southleft__figma-console-mcp-skills/skills/figjam-create-content/SKILL.md`, `references/figjam-snippets.md` |
| mkaralevich/pi-figma-labor | 97e4c6d8 | `corpus/mkaralevich__pi-figma-labor/skills/figjam-create/SKILL.md` |
| amo-tech-ai/rocket-path-ai | a616047d | `corpus/amo-tech-ai__rocket-path-ai/.agents/skills/figma/figjam-diagrams/SKILL.md`, `references/examples.md` |
| atezer/FMCP | 364c0ce6 | `corpus/atezer__FMCP/skills/figjam-diagram-builder/SKILL.md` |
| ompug/diagram-codebase | b1e20f57 | `corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/mermaid/lint.py`, `build.py`, `parsecheck.py`, `sanitize.py`, `figma/driver.py`, `figma/scripts.py`, `references/diagram-types.md` |
| memi-design/mermaid-jam | 568c1e8c | `corpus/memi-design__mermaid-jam/README.md`, `src/parser/mermaidJam.ts`, `src/shared/reviser.ts`, `src/plugin/main/renderer.ts` |

All corpus paths sit under `specs/017-figjam-flow-generation/009-figjam-skill-research/research/corpus/`.

### Added during the run, not pinned

- rrichardsonv/parse-figjam. Iteration 10 found it through a GitHub search and cited `HEAD`. This synthesis read the same file read-only at commit 2722e73738b7eac17a0fbe67eacb180a5e7ae4aa and confirmed the cited lines. It is not part of the local corpus copy.

### Flow Mode surfaces

- `AI Systems/Product Owner/sk-product-owner/references/flow-mode.md`
- `AI Systems/Product Owner/sk-product-owner/assets/flow-templates.md`
- `AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py`
- `AI Systems/Product Owner/sk-product-owner/scripts/vendored/mermaid_extract.py`
- `AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md`
- `AI Systems/Product Owner/claude project/knowledge/Product Owner - Assets - Flow Templates.md`
- `AI Systems/Product Owner/claude project/Custom Instructions.md`, the Flow Mode Delivery section
- `AI Systems/Product Owner/SYNC.md`
- `AI Systems/Product Owner/mcp-figma/references/tool-surface.md`

### How the claims were checked

- Every corpus line the iterations cited was printed and read in context. Lines that had drifted were corrected to the line that holds the claim.
- `flow_check.py --self-test` passed 8 of 8 before any probe ran.
- Twelve planted models were run through `flow_check.py`. The probes covered edge operators, markup, emoji, an `end` ID, a `graph` ID, underscored IDs, a subgraph, quoted labels, an unconnected node, a long label, a fill and stroke pair and an LR header. Only the subgraph and the LR header failed.
