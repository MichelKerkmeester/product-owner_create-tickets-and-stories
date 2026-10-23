# FigJam Packet After Twelve Implementations: Follow-up Synthesis

This synthesis covers the 5-iteration DeepSeek lineage of run `fanout-deepseek-1792558554351-13ddom`. It takes the twelve ranked changes of the phase 016 synthesis as shipped, in phases 017 to 028, and asks four things: does each implementation match the line it came from, what can public documentation now settle, what does the wider web add, and which integration gaps remain.

The earlier synthesis is `AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/research.md`. Its `research/corpus/` citations were resolved against `research/corpus/`, which holds the same repositories. Nothing was edited under `AI Systems/`; every write stayed in `research/lineages/deepseek-extension/`.

---

## 1. Summary

Five changes matter most, and none of them is among the twelve.

1. **The ordered pair cannot fire for the two requests that need it.** The pair rides on a route whose intent is `TASK`, `BUG`, `DOC` or `STORY` [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:718], while `detect_framing` drops `FLOW` only when a second artifact frame already matched [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:648]. "write a doc about onboarding and draw it on a figjam board" and "write a bug about it and add a figjam diagram" both return `intent: FLOW` with no artifact lane, so the diagram is not lost any more - the artifact is.
2. **The tag step cannot be built from the text as written.** It says to tag "every node the write created" without saying where that set comes from [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:188], while Figma documents the discovery rule the packet lacks - the id the tool returns, or a page-children scan when it returns nothing [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:63].
3. **The plugin-data hedge is a documented prohibition.** `getPluginData()` and `setPluginData()` are "**not supported** in `use_figma`"; `getSharedPluginData()` and `setSharedPluginData()` are [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-use/SKILL.md:28]. The packet says "may refuse", which leaves a model guessing about a settled fact [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:188].
4. **`whoami` answers the account, not the file.** Figma marks `whoami` as returning "identity, plans, and seats" [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/] and its own spec skill warns that `whoami` "does not identify which plan owns a file" [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-spec/SKILL.md:9]. Phase 025 reads as if the plan question is answered by the call.
5. **The pair's ClickUp offer fires before the link exists.** The artifact is delivered first "in its own reply shape" [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:256], and that shape closes on the ClickUp offer [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:236]. A user who accepts pushes the artifact before Flow Mode has written the board URL back.

The packet's checking, read-back, accent, architecture and failure rules came through this run confirmed. Section 3 lists what each phase got right, so a later change keeps it.

---

## 2. What the twelve did right

- **The board link reads correctly in every template.** A board URL this session wrote counts as a supplied link once its read-back matched, goes under `Flows` with the diagram's name, and a mismatched or unread board is never linked [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/story-template.md:103]; a Doc takes it in `Related references` [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/doc-templates.md:460].
- **The accent test matches Adobe exactly.** "the node a reader would keep if they could keep only one", never a position, and a tie splits the diagram [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:49] beside Adobe's "if a reader could only take away one node" and "split it or pick one" [SOURCE: research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:22], [SOURCE: research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:32].
- **The architecture reference was already exact and needed nothing.** The layout accepts `flowchart LR` only and requires subgraph ids from a fixed six-value set [SOURCE: research/corpus/openai__plugins/plugins/figma/skills/figma-generate-diagram/references/architecture.md:46], [SOURCE: research/corpus/openai__plugins/plugins/figma/skills/figma-generate-diagram/references/architecture.md:48]; the packet states the same six ids and the same direction [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/architecture.md:78].
- **The read-back direction rule is semantically right.** Endpoint ids and end caps, never position, and a reversed, two-way or swapped connector is a mismatch [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:218]. Only the vocabulary is missing (Section 4, rank 7).
- **The delivery pointers now land on the reply.** `AGENTS.md` sends the reader to `flow-mode.md` Section 8 and names the `Extensions:` line [SOURCE: AI Systems/Product Owner/AGENTS.md:39]; `sk-product-owner/SKILL.md` says the same [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:170].
- **The kernel's no-connector sentence carries both qualifiers.** The offered block is "labelled as the model and never as the board", and no image or HTML page stands in [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:255].
- **The self-edit guidance is in place.** A move, resize or restyle request gets a plain answer, and the two-attempt question offers hand editing [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:254].
- **The Project's Flow mirror is current.** It carries the tag step, the tag-aware rollback, the `whoami` step and the plan question [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:163], [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:229].

---

## 3. The twelve, judged

Every implemented change is listed. "Wanting" means the shipped text leaves out, overstates or misdirects something a model would act on.

| Phase | Verdict | What is wanting |
|---|---|---|
| 017 board link in the artifact | holds | Nothing found. The rule reads correctly in the Story, Doc and Bug templates and names the mismatch case. |
| 018 artifact-plus-board pair | **wanting** | The pair is unreachable for a Doc or a Bug request, and no gold row, fixture or playbook scenario tests either form (ranks 1). Its own limitation calls the gap pre-existing; the code shows it is structural. |
| 019 hosted route connection | **wanting** | It promotes an unchecked claim to fact - "every manual Code Mode holds here is stdio and none reaches an HTTP server" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:180] - and it does not distinguish the remote server from the desktop server, where `generate_diagram`, `use_figma` and `whoami` do not exist (rank 8). |
| 020 accent and cut test | holds | Nothing found. The tie rule, the position ban and the `userIntent` cut are all present and match the corpus. |
| 021 board critic pass | **wanting** | It has no stated screenshot source, although `get_figjam` returns screenshots [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/] and `get_screenshot` fails on an empty node id [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md:21]; it omits two of Adobe's five checks, redundant labels and weak hierarchy [SOURCE: research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:85] (rank 5). |
| 022 created-node tags | **wanting** | Three defects: a documented prohibition written as "may refuse"; no statement of where the created-node set comes from; and a namespace, key and run id named in one breath without saying which is which, which can defeat the cross-session case the tag exists for [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:188] (ranks 2 and 4). |
| 023 kernel no-connector sentence | holds | Verified at the sentence itself, with the mirror matching. |
| 024 Flow delivery pointers | holds | Both pointers name Section 8 and the `Extensions:` line. |
| 025 plan through `whoami` | **wanting** | It lets a model read `whoami` as answering which plan owns the file, and it never names the `planKey` field or its `(team|organization)::<numeric-id>` format [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/] (rank 3). |
| 026 self-edit guidance | holds | The new subsection and the two-attempt offer are both present. |
| 027 repeated edge labels | **wanting** | The rule has no verification path: the checker does not count labels and the screenshot critic does not name them, so nothing catches a breach [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:78] (rank 5). |
| 028 read-back direction | **wanting, mildly** | The semantics are right, but no field or cap value is named, the ERD caps are absent from the vocabulary the corpus uses, and a dangling connector has no rule [SOURCE: research/corpus/ecestnrkl__figjam-mcp/src/lib/connectorGraph.ts:13], [SOURCE: https://developers.figma.com/docs/plugins/api/ConnectorStrokeCap/] (rank 7). |

Five of twelve hold. Seven need an edit: two of those need a new rule with a gate row behind it (018, and 021 together with 027) and five need a text change (019, 022, 025, 027's own wording and 028).

---

## 4. Ranked further improvements

None of these is among the twelve. Each names the Product Owner file it changes and the source it comes from. Rank weighs certainty, how many requests it touches, and the size of the edit.

### Rank 1. Make the pair reachable for a Doc and a Bug, and put it in the gate [INTEGRATION]

- **Changes:** `benchmark/router/route_contract.py` DOC frame list and BUG frames, `sk-product-owner/references/router-contract.md`, `claude project/Custom Instructions.md` router copy, `benchmark/router/fixtures.json`, `benchmark/router/differential_corpus.json`, `benchmark/hub-routing-cases.json`, `sk-create-figjam/manual-testing-playbook/boundaries/artifact-plus-board-pair.md`.
- **Comes from:** the two failing requests, the oracle result (`intent: FLOW`, no artifact lane) and the framing code path [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:648], [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:718]. The DOC noun list omits a bare `doc` [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:305], and every BUG frame requires a report noun or a symptom [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:261].
- **What changes:** add `doc` to the DOC noun alternation in all three copies, and add a `write|file|log a bug about <subject>` frame ahead of the symptom patterns. When a request names a board and an artifact output verb, the artifact lane wins and carries `then: "FLOW"`. Then add one gold row and one fixture per phrasing and extend FJ-037 into two more scenarios.
- **Effort:** medium. Three synchronized copies, two gold rows, two fixtures, two playbook scenarios.
- **Why first:** it is the only defect the dispatcher names independently, it silently loses a deliverable, and the gate can prove the fix. Every other rank is either narrower or already guarded.

### Rank 2. Rebuild the tag step on the verified call [INTEGRATION]

- **Changes:** `sk-create-figjam/references/flow-mode.md` Sections 5, 6 and 9, `references/hybrid-workflow.md`, and the Flow Mode and Hybrid Workflow mirrors.
- **Comes from:** Figma's prohibition and its replacement [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-use/SKILL.md:28]; the supported call's own contract, namespace at least three characters and no manifest entry [SOURCE: https://developers.figma.com/docs/plugins/api/properties/nodes-setsharedplugindata/]; and the created-node discovery rule [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:63].
- **What changes:** name `setSharedPluginData` as the only call, with a fixed namespace such as `po-figjam`; make the diagram name the key and `{runId, diagramName, writtenAt}` the value; take the created-node ids from the write's return value or, when it returns nothing, from page children that were not on the board before; and have the tag call `return` the ids it tagged so the next session can verify.
- **Effort:** small. One paragraph becomes four sentences.
- **Why second:** it turns an unbuildable instruction into a mechanical one, and the cross-session revision that rank 6 of the earlier run aimed at only works once the key is stable.

### Rank 3. Separate the account's plans from the file's plan [INTEGRATION]

- **Changes:** `sk-create-figjam/references/flow-mode.md` Sections 6 and 9, and the Flow Mode mirror.
- **Comes from:** `whoami` returns identity, plans and seats and is remote-only [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/]; `planKey` has a stated format copied from `whoami` [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/]; and `whoami` cannot say which plan owns a file [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-spec/SKILL.md:9].
- **What changes:** `whoami` names the plans the account holds and their `planKey` values. Which plan owns the file is asked, never inferred. A new file uses the one `planKey` when there is one, and asks which team when there are several. The gate states the `planKey` it will pass.
- **Effort:** small.
- **Why third:** the disclosure risk the packet already names is the reason the gate exists, and the current wording can make a model believe the risk is resolved when it is not.

### Rank 4. Treat an architecture write as a page-level node set

- **Changes:** `sk-create-figjam/references/flow-mode.md` Sections 6, 7 and 9, and `references/types/architecture.md`.
- **Comes from:** a `FIGMA_DIAGRAM_2026` write produces one to two `SECTION` nodes plus multiple `SHAPE_WITH_TEXT` and `CONNECTOR` nodes at page level [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:67], [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:69].
- **What changes:** the architecture section says a write creates a set, that the set may include a section, and that the tag, rollback and read-back all operate on the set. The rollback's "stop on a node this write did not create" gains the set test: a node tagged by this work, or inside a section this write created, counts as created.
- **Effort:** small.
- **Why fourth:** it is the only type where the one-write-one-node reading is false, and the failure mode is a rollback that stops halfway.

### Rank 5. Give the critic a screenshot source, the two missing checks, and a label check

- **Changes:** `sk-create-figjam/references/quality-rubric.md` Sections 2 and 6, `references/flow-mode.md` step 10, and their mirrors.
- **Comes from:** `get_figjam` returns the XML outline plus node screenshots [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/]; `get_screenshot` needs a node id [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md:21]; Adobe's critic also checks redundant labels and weak hierarchy [SOURCE: research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:85].
- **What changes:** step 10 says the screenshot comes from the read tool's own node images, or from a screenshot call with the node id the read returned. The board checklist gains a repeated-label count and a hierarchy line, which also gives phase 027's rule the verification path it lacks.
- **Effort:** small.
- **Why fifth:** it closes a rule with no check and removes a step a model currently has to invent.

### Rank 6. Hold the ClickUp offer until the pair has finished [INTEGRATION]

- **Changes:** `claude project/Custom Instructions.md` Flow Mode Delivery bullet, `AGENTS.md` Flow exemption, `sk-product-owner/assets/*` board-link sentences.
- **Comes from:** the artifact's reply shape closes on the offer [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:236], [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:296], the pair delivers the artifact first [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:256], and ClickUp can only attach a local file, never a board [SOURCE: AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:151].
- **What changes:** when `then: "FLOW"` is present, the artifact reply states that the board is still to come and offers ClickUp after the Flow step, when the URL is in the body. The offer is never withdrawn, only sequenced.
- **Effort:** small.
- **Why sixth:** it is cheap and certain, but it only bites on the combined request, which rank 1 makes reachable first.

### Rank 7. Name the cap vocabulary and the dangling-connector rule

- **Changes:** `sk-create-figjam/references/flow-mode.md` Section 7, `references/types/er.md`, and the Flow Mode mirror.
- **Comes from:** the documented cap union, including `DIAMOND_FILLED`, `CIRCLE_FILLED` and the five `ERD_*` values [SOURCE: https://developers.figma.com/docs/plugins/api/ConnectorStrokeCap/]; a parser that skips a connector missing an endpoint [SOURCE: research/corpus/ecestnrkl__figjam-mcp/src/lib/connectorGraph.ts:13].
- **What changes:** the read-back names the two endpoint ids and the two cap fields, says any non-`NONE` cap counts as an arrowhead, lists the ERD caps as arrowheads for an ER, and says a connector with a missing endpoint is reported as dangling rather than counted as a mismatch.
- **Effort:** small.
- **Why seventh:** it makes an existing rule exact rather than adding one, and it prevents a false failure on ER diagrams.

### Rank 8. Say which server, which allowance, and what a retry costs

- **Changes:** `sk-create-figjam/references/flow-mode.md` Sections 6 and 9, `SKILL.md` allowed tools, and the Flow Mode mirror.
- **Comes from:** the remote-only markers on `generate_diagram`, `use_figma`, `create_new_file` and `whoami` [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/]; the six-call monthly allowance on low plans with writes exempt [SOURCE: research/corpus/figma__mcp-server-guide/README.md:8]; and the draft-file cost of a `fileKey`-less call [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:102].
- **What changes:** Section 6 names the remote server as the write route and says what a desktop-server session is missing; the gate states the read calls the read-back will spend; and the retry rule says a second `fileKey`-less call leaves a second draft file.
- **Effort:** small.
- **Mirror or kernel:** the mirror, since a Project reaches the connector directly.
- **Why last:** it is the least certain to matter, because most users are on a paid seat, but it is the only place a user learns why a five-call verification fails on a Starter plan.

---

## 5. What this run settled

These were open in the earlier synthesis's Section 7. Each is now answered from public documentation or from a corpus copy that was previously discounted.

- **The hosted tool list.** Figma publishes read and write tool tables, with remote-only markers, and the list is larger than the 18 titles in the plugin's root `mcp.json` [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/]. The packet's confirm-at-run-time rule remains correct.
- **`whoami`.** It returns identity, plans and seats; it is remote-only; it cannot say which plan owns a file [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/], [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-spec/SKILL.md:9].
- **What `get_figjam` returns.** An XML outline of the node tree plus screenshots of the nodes [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/], [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md:17]. The attribute names inside that XML are still unproven.
- **Plugin data.** `setPluginData` is not supported through `use_figma`; `setSharedPluginData` is, with no manifest entry and a three-character minimum namespace [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-use/SKILL.md:28], [SOURCE: https://developers.figma.com/docs/plugins/api/properties/nodes-setsharedplugindata/].
- **An architecture write is a node set, not a node** [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:67].

## 6. Rejections re-tested

Fourteen of the earlier synthesis's fifteen rejected ideas still stand. One needs a qualification rather than a reversal: "counting redistributions as separate evidence" is right about independence and wrong about currency, because a discounted copy is where a changed rule appears. The `figma-use` prohibition is absent from the pin and present in the copy, so that copy is newer despite the file dates [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-use/SKILL.md:1], [SOURCE: research/corpus/lightspeedwp__.github/plugins/figma/figma-use/SKILL.md:28].

Two rejections are now better supported. A disk run manifest is less needed because the board can carry shared plugin data. A ClickUp attachment is impossible for a board, because the attach tools take a local file [SOURCE: AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:151].

One rejection was too broad. "A ClickUp offer or attachment from the Flow reply" rejects the attachment correctly and the offer incorrectly: the defect is the offer's timing, not its existence (rank 6).

## 7. Claims still unverified

- Which `generate_diagram` call shape the live server accepts. The pinned tree holds both shapes, so the claim is now a documented contradiction rather than an unknown [SOURCE: research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:85], [SOURCE: research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:57].
- Whether a CLI runtime with Figma's plugin installed reaches the hosted server, and whether a desktop-server session can write a diagram at all.
- The exact XML attribute names `get_figjam` uses for connector endpoints and caps.
- Whether `use_figma`'s plugin-data refusal is a sandbox policy or a version difference between the pin and the shipped skill.
- That Code Mode holds no HTTP manual. This is the one place an unchecked claim became packet instruction [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:180].
- The kernel review status. No operator confirmation was seen.
- That the packet's scorecard is the only scored board instrument in the corpus. Eight corpus repositories remain uncited by any iteration, and this run added none of them.

## 8. Method corrections

- Iteration 1 recorded three line numbers off by one or two on the rubric's board checklist and one Adobe critic line. They are corrected in that narrative and used correctly below.
- The delta rows for iteration 1 keep the numbers as first written, because the delta stream is append-only and this run does not rewrite it.
- Total: 5 iterations, 43 findings, 5 of 5 key questions answered.

## 9. Sources

### Product Owner files read

- `sk-create-figjam/`: `SKILL.md`, `references/flow-mode.md`, `references/quality-rubric.md`, `references/style-guide.md`, `references/types/architecture.md`, `manual-testing-playbook/boundaries/artifact-plus-board-pair.md`
- `sk-product-owner/`: `SKILL.md`, `assets/story-template.md`, `assets/doc-templates.md`
- Hub and router: `AGENTS.md`, `benchmark/router/route_contract.py`, `benchmark/hub-routing-cases.json`, `claude project/Custom Instructions.md` and `claude project/knowledge/Product Owner - Templates - Flow Mode.md`
- ClickUp: `mcp-click-up/references/mcp-tools.md`
- Phases `017-board-link-in-artifact` to `028-readback-direction`, each `implementation-summary.md`

### Corpus files read

- `figma__mcp-server-guide/`: `skills/figma-use-figjam/SKILL.md`, `skills/figma-use/SKILL.md`, `skills/figma-spec/SKILL.md`, `skills/figma-generate-diagram/SKILL.md`, `workflow-skills/generate-project-plan/references/blocks/diagram-section.md`, `README.md`
- `lightspeedwp__.github/plugins/figma/figma-use/`: `SKILL.md`, `references/gotchas.md`, `references/plugin-api-standalone.index.md`
- `openai__plugins/plugins/figma/skills/figma-generate-diagram/references/architecture.md`
- `adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md`
- `ecestnrkl__figjam-mcp/src/lib/connectorGraph.ts`

### Public pages

- `https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/`
- `https://developers.figma.com/docs/plugins/api/properties/nodes-setsharedplugindata/`
- `https://developers.figma.com/docs/plugins/api/ConnectorStrokeCap/`
- `https://github.com/figma/mcp-server-guide/blob/main/skills/figma-generate-diagram/references/architecture.md`
- `https://github.com/figma/mcp-server-guide/blob/main/skills/figma-use-slides/SKILL.md`
- `https://www.figma.com/blog/figjam-your-coding-agents-whiteboard/`
- `https://www.figma.com/community/skills`

---

## 10. Convergence report

| Field | Value |
|---|---|
| Stop reason | `maxIterationsReached` |
| Iterations completed | 5 of 5 |
| Key questions answered | 5 of 5 |
| Findings recorded | 43 |
| newInfoRatio by iteration | 1.0, 0.88, 0.75, 0.92, 0.85 |
| Mean newInfoRatio | 0.88 (1.0, 0.88, 0.75, 0.92, 0.85; the registry's convergence score reads the latest, 0.85) |

Convergence was off by configuration, so the ratio is telemetry only. The series did not decay: iteration 3 fell because the corpus-widening half found distribution rather than discipline, and iteration 4 rose again on the integration surfaces.

### Checks run

- The append gateway accepted one run-open record and one record per iteration, each with exit 0 and a receipt; the state projection refreshed after every append with no error.
- The reducer reported `iterationsCompleted: 5` and `corruptionCount: 0` after the final iteration, and emitted `resource-map.md`.
- The synthesis close-out ran its artifact and reconstruction invariants over `research.md` and `findings-registry.json` and staged `synthesis_complete` rather than `synthesis_incomplete`, so no missing artifact or unreconstructed finding was reported. Its record carries `stopReason: maxIterationsReached`.
- The state projection now holds one run-open record, five iteration records and one synthesis record.
- The registry holds 43 findings, matching this synthesis's count.
- The router oracle was run on four combined requests; two returned `FLOW` where an artifact was asked for.
- No file outside `research/lineages/deepseek-extension/` was created or modified.
