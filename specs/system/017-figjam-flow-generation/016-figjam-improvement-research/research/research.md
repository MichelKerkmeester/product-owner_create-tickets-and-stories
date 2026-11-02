# FigJam Packet and Product Owner Integration: Research Synthesis

This synthesis covers the 10-iteration DeepSeek lineage of run 1792527089584-nrdj43. It ranks changes to `sk-create-figjam` and to how that packet works with `sk-product-owner`, the hub, the kernel, the Claude Project and the vendored `mcp-figma` and `mcp-click-up` packets.

Every finding used below was checked against the cited corpus line and the Product Owner line it would change. Where an iteration said Product Owner lacked something, Product Owner was searched for it first. Eighteen iteration or draft claims failed that check and are listed in Section 6.

---

## 1. Summary

Three changes matter most.

1. **A FigJam board made for an artifact should land in that artifact.** Every Story, Epic, Task and Bug template already has a `Flows` link group, but the board URL Flow Mode returns never counts as a supplied link. So it never reaches the artifact or the ClickUp push that carries the artifact.
2. **A request for an artifact and a FigJam diagram together loses the diagram today.** The router oracle routes "write a story for saved searches and make a FigJam flow of its screens" to Story alone, with no question. The fix is an ordered pair: artifact first, then the diagram drawn from it, the way a Story with its tasks already works.
3. **The primary write route is undocumented, and the vendored Figma packet calls it unsupported.** `sk-create-figjam` writes through Figma's hosted MCP server first. Its only MCP surface is Code Mode, and the vendored `mcp-figma` wiring guide says Code Mode cannot reach that server. Figma's own plugin now declares the hosted server at its root, which gives the packet a documented way to name the connection.

The packet's checking, read-back and failure rules are already stronger than most of the corpus. Section 2 lists them so a later change keeps them.

---

## 2. What the packet already does better than the corpus

These are protected. No change in Section 4 removes them.

- **A pre-write check that fails closed.** `flow_check.py` refuses any Mermaid kind the generator cannot draw and every broken rule before a board exists [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:6], [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:64]. Nothing is written until every diagram passes [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:63]. Figma's own skill goes from context gathering to the tool call with no model checker [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:59], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:81].
- **A self-test that proves its own rules.** The self-test plants a failing model per rule, re-measures every palette row and runs the templates, examples and Project mirrors through the same check [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:165], [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:170]. During this synthesis it ran 148 of 148 checks passed, exit 0, with no mirror skipped.
- **Measured contrast.** The palette pairs are exactly Figma's nine light pairs [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:285], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:63]. The packet measures each one and refuses the saturated fills Figma allows, because white text on them measures 1.85:1 [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:295], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:118].
- **Provenance with a fidelity ledger.** Every claim gets one of five source classes, an authority order and a conflict gate [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:120]. Every source item that is in no diagram is listed with its reason [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:119]. Figma says only not to invent edges [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:71].
- **Read-back against an expected model.** The board is compared with the model by count, label, endpoints and direction. It is never called done on a mismatch [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:211], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:228]. A screenshot-only read is labelled visual, because a picture cannot prove joins [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:215]. The corpus board readers describe a board well but have no expected model to call it wrong [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/README.md:22].
- **Strict retry and rollback.** A timeout is not proof that nothing landed, and the target is read before any retry [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:184]. ompug carries the same rule [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/docs/DESIGN.md:223]. The packet goes further on rollback. It deletes only nodes this write created, and only after a yes. It stops on a node it did not create [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:187]. Figma's skill instead offers to keep old attempts beside new ones [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:110].
- **A bounded repair loop.** After two attempts at one diagram the packet stops and asks [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:246]. This is Figma's own rule [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:98], and Adobe follows it too [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md:161].
- **A machine-checked architecture lane table.** The six lanes and the allowed-edge table come from Figma's architecture reference [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/architecture.md:48], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/architecture.md:65]. Figma and hferello state them as prose [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/arch-flow/references/figjam-architecture.md:10]. The packet checks them in code [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:47], [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:49].
- **A four-shape user flow with a merge dot.** One meaning per shape, and a wordless circle where branches rejoin [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:40], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:45]. No corpus source has the merge dot.
- **The schema is confirmed at run time.** The packet lists the connected tools and uses the fields the server reports [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:180]. The corpus proves why: Figma's diagram skill sends `mermaidSyntax` [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:85], while its project-plan block sends `mermaid` with `editorType` [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:57].
- **A stated disclosure reason for the plan.** The plan is fixed before the write because a board in the wrong plan is visible to that plan at once [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:254].
- **No stand-in file.** With no route the packet offers the checked model and never renders an image, an HTML page or a Mermaid file as the board [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:203]. The Project mirror states it most tightly [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:168].
- **Split rather than shrink, with ordered cuts.** Budgets are already per type [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:162], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/sequence.md:71], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/gantt.md:67]. Cuts run in a fixed order [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:170].

Two more behaviors match the corpus rather than beat it, and should also stay. The board URL goes to the user before any extension runs [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:47], as Figma asks [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/workflow.md:107]. Extensions are ranked by type value [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:41], as Figma ranks them [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/workflow.md:27].

---

## 3. What changed upstream

### The finding

Almost nothing changed. Between the phase 009 pin `7047cb45` and this pin `056adaf7` there is one commit. It adds two root files, `mcp.json` with 35 lines and `plugin.json` with 19 lines. This came from the GitHub compare API, run during this synthesis. The status is `ahead` by 1 commit. That commit is "Add root plugin and MCP configuration files (#84)", dated 2026-10-20. Those two files are the only ones it changes.

The local copies agree. A recursive diff of the phase 009 corpus copy against this pin reports only `mcp.json` and `plugin.json` as new. The phase 009 copy is dated today, so that diff alone would not prove the old state, but the compare API does.

The three folders the question names were already upstream when phase 009 pinned. Phase 009 did not read them. Its source table cites only the diagram skill, its flowchart reference and the FigJam skill [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/009-figjam-skill-research/research/research.md:296]. The GitHub commit history for each path at `7047cb45` gives the first commit:

| Path | First commit | Date |
|---|---|---|
| `figma-power/` | `bad69b58` | 2026-02-25 |
| `skills/figma-use-figjam/` | `85ecc5cf` | 2026-04-27 |
| `workflow-skills/generate-project-plan/` | `76c729bc` | 2026-04-28 |
| `skills-figquery/` | `a5e7e047` | 2026-09-10 |

Iteration 2 treated these as new material. That premise is wrong, so this section reports what each holds, not what changed.

### Each item and what the packet should do

- **`mcp.json` and `plugin.json`, the real change.** Figma's plugin now declares the hosted server at its root, at `https://mcp.figma.com/mcp`, with 18 tool titles [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/mcp.json:5], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/mcp.json:15]. The list includes `generate_diagram`, `get_figjam`, `use_figma`, `upload_assets` and `whoami` [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/mcp.json:21], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/mcp.json:29], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/mcp.json:30]. The plugin is version 2.2.163 [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/plugin.json:5]. The older `.mcp.json` beside it also lists `generate_image`, which the new file does not, so the two upstream lists already disagree. Action: rank 3 uses this to name how the hosted route is reached. Rank 9 uses `whoami`. The packet keeps confirming tool names at run time, because the upstream lists differ.
- **`skills-figquery/`.** Its README says it is a variant for Cursor only, and every other client reads `skills/` [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills-figquery/README.md:3], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills-figquery/README.md:7]. Its diagram skill is byte-identical to `skills/`. Its FigJam skill differs only in `references/edit-text.md`. Action: none. Do not count it as a second source.
- **`skills/figma-use-figjam/` with `plan-board-content.md`.** This holds the FigJam node API and board layout numbers: 4px spacing, cluster distances and a sticky grid [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills-figquery/figma-use-figjam/references/plan-board-content.md:17], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills-figquery/figma-use-figjam/references/plan-board-content.md:229]. The `skills/` copy is identical. Action: none beyond what the packet already took from it in phase 009. The numbers govern hand-built boards, and Section 5 explains why the packet should not adopt them.
- **`workflow-skills/generate-project-plan/`.** Three facts transfer. It resolves the plan through `whoami` and asks which team when there are several [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:341], which rank 9 adopts. Its diagram-section block shows that wrapping a generated diagram in a section means collecting every page-level node and deleting and recreating each connector [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:72], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:143]. That confirms the packet's rule never to wrap a generated node [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:148]. It also warns that a connector label written through `use_figma` can read back as present while it renders invisible [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:196]. The packet creates no connectors through `use_figma`, so that warning needs no action today.
- **`figma-power/`.** This is a Kiro power. Its tool table names `get_figjam`, `generate_diagram` and `whoami` [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/figma-power/POWER.md:46], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/figma-power/POWER.md:48]. It carries no diagram guidance. Action: none.

---

## 4. Ranked improvements

Twelve changes are ranked below. Five are integration changes, marked **[INTEGRATION]**. Ranks weigh how certain the gap is, how many requests it touches and the effort.

Project mirror means a file under `claude project/knowledge/`. Kernel means `claude project/Custom Instructions.md`. Changing a mirror follows the manual parity method [SOURCE: AI Systems/Product Owner/SYNC.md:10]. The frozen parent decisions are D1 to D7 in the parent goal [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/goal.md:47], [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/goal.md:52].

### Rank 1. Write a verified board URL back into the artifact's `Flows` group [INTEGRATION]

- **Changes:** `sk-product-owner/references/story-mode.md` line 163, `sk-product-owner/assets/story-template.md` line 103, `sk-product-owner/assets/epic-template.md` line 74, `sk-product-owner/references/task-mode.md` line 134 and `sk-product-owner/assets/bug-report-template.md` near line 84. For a Doc, the Related references block in `sk-product-owner/assets/doc-templates.md` line 447.
- **Comes from:** hferello finishes the doc first, then adds a `## Visual diagram` section with the board link [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/arch-flow/SKILL.md:166], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/arch-flow/SKILL.md:170]. The slot already exists in every Product Owner template [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/story-template.md:103], [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/epic-template.md:77], [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/task-templates.md:55], [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/bug-report-template.md:84].
- **The gap:** links appear only when supplied, and a Figma destination is never invented [SOURCE: AI Systems/Product Owner/sk-product-owner/references/story-mode.md:163]. A URL that Flow Mode wrote in the same session is neither invented nor supplied under that wording. The Flow reply carries the board and nothing else [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:221]. So the board never enters the artifact.
- **What changes:** a board URL this session wrote, whose read-back matched the model, counts as a supplied link. It goes under `Flows` with the diagram's name as the link text. A board with a mismatched read-back, or with `Read-back: not possible`, never goes in. An artifact already saved is re-saved under its own filename, as the refinement rule does [SOURCE: AI Systems/Product Owner/AGENTS.md:47].
- **Effort:** medium. Five templates and their mirrors change, each by one sentence.
- **Mirror or kernel:** the matching Knowledge files for Story Mode, the Story, Epic, Task and Bug templates and Doc Templates. The kernel sentence that says References carries supplied links only also changes [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:158].
- **Frozen decision:** none. D6 governs the Flow reply, which does not change.
- **Why first:** the slot exists everywhere, so this is the cheapest change that connects the two packets. Once the URL is in the artifact body, the existing ClickUp push carries it, because the body travels verbatim [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:248]. Rank 2 depends on it.

### Rank 2. Stop dropping a FigJam output named beside an artifact, and form an ordered pair [INTEGRATION]

- **Changes:** `sk-product-owner/references/routing.md` line 26, `sk-product-owner/references/router-contract.md` lines 493 to 495, `benchmark/router/route_contract.py` lines 626 to 627, the kernel router at `claude project/Custom Instructions.md` lines 600 to 601, `ROUTER.md` line 37. The outcome wording changes at hub `SKILL.md` line 79 and `hub-router.json` line 15. New gold rows go in `benchmark/hub-routing-cases.json` and `benchmark/router/fixtures.json`, and a new playbook boundary scenario beside `sk-create-figjam/manual-testing-playbook/boundaries/figjam-as-task-subject.md`.
- **Comes from:** the Story with nested Tasks bundle, which turned two artifacts into one dependent deliverable that asks no question [SOURCE: AI Systems/Product Owner/SYNC.md:49], [SOURCE: AI Systems/Product Owner/AGENTS.md:93]. hferello sets the order: the doc first, then the diagram from it, with labels that match the doc [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/arch-flow/SKILL.md:168].
- **The gap:** when FigJam wording sits beside another artifact's framing, the router discards FLOW [SOURCE: AI Systems/Product Owner/sk-product-owner/references/router-contract.md:493], [SOURCE: AI Systems/Product Owner/sk-product-owner/references/routing.md:26]. That is right for "write a task to fix the figjam board export". It is wrong when the user asks for both. Running the oracle during this synthesis showed it. "write a story for saved searches and make a FigJam flow of its screens" returned intent `STORY`, source `framing`, `needs_disambiguation` false. "write a runbook for refunds with a FigJam process diagram" returned `DOC` the same way. The diagram is silently lost. The hub claims Interactive Mode asks which comes first [SOURCE: AI Systems/Product Owner/SKILL.md:79], but no question is asked here.
- **What changes:** separate FigJam as the subject from FigJam as a second output. A second output is an output verb aimed at FigJam, such as "make", "draw" or "with a FigJam ... diagram", joined to the artifact request. It forms an ordered pair. The artifact exports and is read back first under the normal protocol. Then Flow Mode runs with that artifact as its product-doc source, which its intake already handles [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:119], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:169]. Its own gate and yes still apply. Rank 1 then writes the URL back. Stage one can stay as it is, because the pair forms in stage two.
- **Effort:** large. It changes the router oracle, the kernel's copy of the router and the gold rows.
- **Mirror or kernel:** the kernel router must change with the contract, because the kernel copies it and `benchmark/router/differential.py` fails any second copy that differs [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:77]. The Router Contract Knowledge file is a byte copy [SOURCE: AI Systems/Product Owner/SYNC.md:23].
- **Frozen decision:** no numbered parent decision. It amends a settled routing rule that a playbook scenario tests, so it should land as a recorded amendment.
- **Why second:** the loss is confirmed and touches every combined request. It ranks below rank 1 because it is larger and needs rank 1 to finish the loop.

### Rank 3. Name how the hosted route is reached, and resolve the clash with the vendored `mcp-figma` [INTEGRATION]

- **Changes:** `sk-create-figjam/references/flow-mode.md` Section 6, lines 176 to 180. `sk-create-figjam/SKILL.md` line 4 (allowed tools) and line 216 (integration points). A note for `mcp-figma/references/mcp-wiring.md` lines 152 to 157 goes upstream through `scripts/vendor-sync.py push`, never as a local edit [SOURCE: AI Systems/Product Owner/SKILL.md:124].
- **Comes from:** Figma's new root `mcp.json` [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/mcp.json:5]. Figma's plugin manifest [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/plugin.json:4].
- **The gap:** the hosted route is the primary write route [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:176], [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/goal.md:51]. The packet never says how it is connected, and its only MCP tool is Code Mode [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:4]. The vendored wiring guide calls the hosted server "not a supported path in this release", because Code Mode has no HTTP manual [SOURCE: AI Systems/Product Owner/mcp-figma/references/mcp-wiring.md:154], [SOURCE: AI Systems/Product Owner/mcp-figma/references/mcp-wiring.md:156]. The vendored packet's optional MCP is Framelink, not the hosted server [SOURCE: AI Systems/Product Owner/mcp-figma/SKILL.md:376]. The write-route spike was blocked with no Figma MCP in the session [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md:104].
- **What changes:** Section 6 says the hosted route is a native MCP connection to Figma's server, made by Figma's own plugin or the client's connector. It never runs through Code Mode. It keeps "list the connected tools first". It says the vendored wiring guide covers the Code Mode path only.
- **Effort:** medium. One live session should confirm the connection before the text claims it.
- **Mirror or kernel:** none. A Project reaches Figma through its connector [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:252].
- **Frozen decision:** none. It documents D5. D7 stays, so the Product Owner plugin still ships no MCP entry and Figma's plugin supplies the server.
- **Why third:** every hosted write depends on it, and two packets in one hub now say opposite things. It ranks below the two artifact changes because operators who already have the server connected are not blocked.

### Rank 4. Pick the accent with a test, and use the `userIntent` sentence as the cut test

- **Changes:** `sk-create-figjam/references/quality-rubric.md` Section 3 line 47 and Section 2 lines 35 to 41. `sk-create-figjam/references/style-guide.md` lines 32 and 86.
- **Comes from:** Adobe reserves the accent for "the one node the diagram exists to explain" and never assigns it by position. Two equal candidates mean the diagram should split [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:22], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:31]. Every diagram earns one sentence, and anything that does not serve it is cut [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:71].
- **The gap:** the rubric lists four candidates for the accent with no way to choose [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:47]. The style guide picks the pair by meaning, not the node [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:86]. The one-sentence reader question already exists as `userIntent` [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:182], but nothing uses it to cut nodes.
- **What changes:** the accent goes to the node a reader would keep if they could keep only one. A tie means split. The remove test adds one line: every node serves the `userIntent` sentence, or it is cut and named under `Left out:`.
- **Effort:** small.
- **Mirror or kernel:** Rules - Flow Quality Rubric and Rules - Flow Style Guide.
- **Frozen decision:** none. No reply line is added, so D6 holds.
- **Why fourth:** it improves every diagram for two sentences of text. It is a taste rule, so its gain cannot be measured before a scored board.

### Rank 5. Turn the rubric's board check into a bounded critic pass

- **Changes:** `sk-create-figjam/references/quality-rubric.md` Section 6 line 76 and `sk-create-figjam/references/flow-mode.md` line 68.
- **Comes from:** Adobe runs a critic on the Mermaid source and a screenshot, checking clutter, accent misuse, redundant labels and whether the caption matches the canvas, then applies the findings once and stops [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:82]. figjam-builder traces every required edge in the screenshot, because a count does not prove clarity [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:371]. The packet's own scorecard already scores connector crossings [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md:81].
- **The gap:** the runtime screenshot check covers stretched shapes, cut labels and overlap only [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:76]. Crossings and misleading routes are scored in the playbook and never checked in a real run.
- **What changes:** the same screenshot also checks crossings, any edge whose route looks like it joins the wrong node, accent placement and whether the board answers the `userIntent` sentence. A finding is reported. It is fixed only by reshaping the model and regenerating after a yes, inside the existing two-attempt bound [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:246].
- **Effort:** small.
- **Mirror or kernel:** Rules - Flow Quality Rubric and Templates - Flow Mode.
- **Frozen decision:** none.
- **Why fifth:** it closes a gap between the run and the packet's own scorecard. It ranks below rank 4 because a finding often cannot be fixed without a regeneration.

### Rank 6. Tag what a write created, so a revision works in a later session

- **Changes:** `sk-create-figjam/references/flow-mode.md` lines 183, 187 and 246 plus `sk-create-figjam/references/hybrid-workflow.md` lines 166 to 168.
- **Comes from:** ompug tags each section it creates with shared plugin data (`diagram_id`, `run_id`, `content_hash`), so later runs find and replace their own work [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/README.md:236], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/docs/DESIGN.md:229]. It notes that `use_figma` forbids `setPluginData`, so it uses shared plugin data and wraps every access in a try and catch [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/scripts.py:24], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/scripts/diagram_codebase/figma/scripts.py:56]. It reconciles from those tags before regenerating, to avoid duplicates [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/skills/diagram-codebase/references/troubleshooting.md:63].
- **The gap:** every revision reuses the `fileKey` [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:183]. The rollback stops on any node this write did not create [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:187]. In a new session nothing records which nodes an earlier write created. So a revision there can delete nothing and would duplicate the diagram, which the packet itself warns against [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:246].
- **What changes:** after the read-back, one `use_figma` call tags each created node with a namespace, the diagram's name and a run id. A later session reads the tags before it deletes or regenerates. When the tag call fails, the current rule stands and the user removes the old diagram by hand.
- **Effort:** medium. It depends on behaviour nobody has checked live.
- **Mirror or kernel:** Templates - Flow Mode and Templates - Flow Hybrid Workflow. In a Project it depends on the connector's write tool.
- **Frozen decision:** none of D1 to D7. Tagging writes metadata to generated nodes. The packet forbids moving, resizing or restyling them [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:180], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:17]. Metadata is not named there, so it needs an explicit ruling first.
- **Why sixth:** it fixes a real hole in cross-session revision with a proven pattern. Its main dependency is unverified.

### Rank 7. Close the kernel's no-connector parity gap [INTEGRATION]

- **Changes:** `claude project/Custom Instructions.md` line 255.
- **Comes from:** the Flow Knowledge mirror labels the fenced block as the model and never as the board, and bans an image or HTML stand-in [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:168], [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:195]. The skill states the same ban [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:203].
- **The gap:** the kernel sentence says "labelled as the model" and drops "never as the board" and the stand-in ban [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:255].
- **What changes:** one sentence carries both qualifiers.
- **Effort:** small.
- **Mirror or kernel:** the kernel itself. The kernel review by the operator is recorded as pending [SOURCE: AI Systems/Product Owner/SYNC.md:49].
- **Frozen decision:** none.
- **Why seventh:** it is certain and tiny. It matters only when the kernel is read without the mirror being retrieved.

### Rank 8. Repoint two stale Flow delivery pointers [INTEGRATION]

- **Changes:** `AGENTS.md` line 39 and `sk-product-owner/SKILL.md` line 170. Then rebuild the plugin with `scripts/build-plugin.py`, because `claude-plugin/skills/product-owner/AGENTS.md` and its `sk-product-owner/SKILL.md` carry the same two lines.
- **Comes from:** the Flow reply lives in Section 8, DELIVERY [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:219]. Section 6 is WRITE ROUTES [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:174]. The FigJam packet's own pointer is right [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:173].
- **The gap:** both lines send the reader to "Section 6" for the reply [SOURCE: AI Systems/Product Owner/AGENTS.md:39], [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:170]. `AGENTS.md` line 39 also leaves out the `Extensions:` line the packet ships [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:225].
- **What changes:** both say Section 8. `AGENTS.md` line 39 names the `Extensions:` line.
- **Effort:** small.
- **Mirror or kernel:** none. The kernel points at its own Section 9 [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:91].
- **Frozen decision:** D6 lists the reply lines without `Extensions:` [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/goal.md:52]. The packet already ships that line, so D6 should gain a recorded amendment rather than the packet losing the line.
- **Why eighth:** certain and cheap. The cost of leaving it is a reader landing on the write routes when they want the reply.

### Rank 9. Resolve the plan with `whoami` before the gate

- **Changes:** `sk-create-figjam/references/flow-mode.md` line 181 and Section 9 lines 252 to 254.
- **Comes from:** Figma's project-plan skill calls `whoami`, uses the one plan or asks which team when there are several [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:341]. Phase 009 proposed the same from ompug [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/009-figjam-skill-research/research/research.md:199]. A search of Product Owner found no `whoami` outside the phase 009 research.
- **The gap:** the packet says to name the plan and pass a plan field where one exists [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:181], but not how to learn which plans the account holds.
- **What changes:** where the server reports `whoami`, call it before the gate. With one plan, name it in the gate. With several, ask which one before the gate.
- **Effort:** small.
- **Mirror or kernel:** Templates - Flow Mode Section 6, conditional on the connector exposing `whoami`.
- **Frozen decision:** none.
- **Why ninth:** it guards the disclosure risk the packet names [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:254]. It ranks here because phase 009 already proposed it, and the reason it did not land is not recorded.

### Rank 10. Tell the user how to edit the board themselves

- **Changes:** `sk-create-figjam/references/flow-mode.md` Section 9, line 246, plus one new line in Section 9 for a move, font or restyle request.
- **Comes from:** Figma's skill says the tool cannot change fonts, move shapes or edit node by node. It recommends editing in Figma [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:25], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:30]. After two attempts it suggests editing manually [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:98]. Adobe says the same [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md:162].
- **The gap:** the packet forbids itself from moving generated nodes [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:164]. It never tells the user they may. After two attempts it only asks what is wrong [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:246].
- **What changes:** a request to move, resize or restyle a generated node gets a plain answer. The packet will not do it, and the user can do it in FigJam. After two attempts the question also offers that.
- **Effort:** small.
- **Mirror or kernel:** Templates - Flow Mode Section 9.
- **Frozen decision:** none.
- **Why tenth:** small and certain, but it only fires on revision requests.

### Rank 11. Flag repeated edge labels, with decision exits exempt

- **Changes:** `sk-create-figjam/references/quality-rubric.md` Section 2 lines 39 to 40 plus the judged-by-hand lists in `references/types/process.md` and `references/types/architecture.md`.
- **Comes from:** Adobe says a diagram with four or more identical edge labels should have none or one [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:50], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:54].
- **The gap:** the rubric bans a label that repeats its shape and a connector that restates the layout [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:39], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:40]. It says nothing about the same label on every connector.
- **What changes:** four or more identical labels on non-decision edges in one diagram become none or one. Decision exits are exempt, because the user flow asks exits to read the same way across a flow [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:70]. Sequence messages are exempt, because each must carry its specifics [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/sequence.md:77]. It could later become a rule in `figjam_checks/flowchart.py`.
- **Effort:** small.
- **Mirror or kernel:** Rules - Flow Quality Rubric and the Flow Type files for process and architecture.
- **Frozen decision:** none.
- **Why eleventh:** a narrow rule that needs the exemptions to avoid false failures.

### Rank 12. Name how read-back derives direction, and how to read a busy board

- **Changes:** `sk-create-figjam/references/flow-mode.md` Section 7, lines 209 to 215.
- **Comes from:** parse-figjam reads each connector's start and end endpoint ids, then both caps for direction [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/rrichardsonv__parse-figjam/SKILL.md:44], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/rrichardsonv__parse-figjam/SKILL.md:50]. ecestnrkl resolves the caps to forward, reverse, two-way or undirected [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/src/lib/connectorGraph.ts:48]. figjam-builder reads a large board in smaller batches and halves the batch on a timeout [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:395], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:412].
- **The gap:** the read-back requires the same direction [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:212] but never says how direction is read from the board. It reads node by node [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:68] with no rule for a read that times out on a board that already holds content.
- **What changes:** direction comes from the endpoint ids and the end caps, never from position. A reversed or two-headed connector is a mismatch. A read that times out is retried on fewer nodes at a time.
- **Effort:** small to medium, depending on what `get_figjam` returns.
- **Mirror or kernel:** Templates - Flow Mode Section 7.
- **Frozen decision:** none.
- **Why last:** it makes an existing rule exact rather than adding one. It also rests on an unverified tool output.

---

## 5. Rejected ideas

- **A recolour pass on generated nodes.** Adobe restyles every node through `use_figma` after the generator runs [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md:67], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md:87]. The packet never restyles a generated node [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:180]. It sets colour in the model, from FigJam's own swatches, so anyone on the board can recolour it [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:27].
- **Export, crop and embed an image.** Adobe screenshots the board, crops per diagram and embeds a PNG [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md:98], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md:113]. D1 makes FigJam the only output [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/goal.md:47]. The packet leaves no image file [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:230]. Artifacts carry no image [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/story-template.md:103].
- **Wrapping the diagram in a section.** Figma's block, mermaid-jam and ompug all put a diagram in a section [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/memi-design__mermaid-jam/README.md:30]. Reparenting means deleting and recreating every connector [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:143]. That replaces the generated connectors, which breaks the read-back and the rule that a section never wraps a generated node [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:148].
- **Preserving moved positions on update.** mermaid-jam keeps moved nodes when ids match [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/memi-design__mermaid-jam/README.md:27]. The packet's generator owns layout and accepts no geometry [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:164].
- **Hand-built journey, mindmap and timeline kinds.** mermaid-jam builds these natively [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/memi-design__mermaid-jam/README.md:37], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/memi-design__mermaid-jam/README.md:40]. A hand-built board has no generator layout and no checker. The packet builds by hand only when the generator cannot draw a type and the request is mostly styling [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/gantt.md:87]. Its nearest-type table already answers these kinds [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:95].
- **Figma's full shape set and dotted or thick edges in a user flow.** Figma documents 18 shapes and three strokes [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:35], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:78]. Phase 009 settled on one meaning per shape and solid arrows [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:59]. Nothing new reopens it.
- **A flat budget raise to 20 or 25 nodes.** Figma and ompug allow about 25 [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/references/flowchart.md:350], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/docs/DESIGN.md:192]. Those tools lay out or move nodes differently. The packet cannot move a node, and its budgets are already per type.
- **Connectors that always recede.** Adobe keeps every connector a dark neutral [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:46]. The packet lets its one accent mark the happy-path connectors [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:83]. That use is a single accent, not a second colour channel, so it stays.
- **A light-to-dark neutral ramp for ordering.** Adobe shows precedence in steps of gray [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:39]. The packet's palette has one gray pair beside the lane pair [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:71]. A ramp would break the one-accent rule. Gantt styling is stripped anyway [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/gantt.md:65].
- **Board layout constants for extensions.** Figma's 4px grid and sticky grid govern hand-built boards [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills-figquery/figma-use-figjam/references/plan-board-content.md:85]. The packet places its extensions relative to the diagram [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:101], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:114]. It records why the grid stays behind [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:129].
- **Version history and blame.** southleft binary-searches versions through REST [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/southleft__figma-console-mcp-skills/skills/figma-blame-node/SKILL.md:20]. It needs a terminal and a personal token, and does not run in a claude.ai chat [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/southleft__figma-console-mcp-skills/skills/figma-version-history/SKILL.md:17].
- **A snapshot diff and board retrieval.** ecestnrkl diffs two board snapshots and answers questions from a board [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/README.md:23]. It keeps a local cache [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/README.md:89]. The packet's question is whether the board matches a known model, which a diff does not answer.
- **A run manifest on disk.** ompug writes `manifest.json` with Figma ids and a pending action [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/docs/DESIGN.md:60]. The packet leaves no file [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:177], and D6 exempts Flow from the export step. Rank 6 keeps the record on the board instead.
- **A ClickUp offer or attachment from the Flow reply.** The kernel offers ClickUp "outside Flow Mode" on purpose [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:236]. The Flow reply carries nothing else [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:254]. An attachment is a file upload [SOURCE: AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:150]. Rank 1 carries the URL through the artifact, and the artifact's existing offer then applies.
- **Mirroring `mcp-click-up` into the Project.** A Project reaches ClickUp through its own connector [SOURCE: AI Systems/Product Owner/SYNC.md:75].
- **A reply caption line.** Adobe's caption is useful as a cut test, which rank 4 adopts. A caption line in the reply would change D6, so it stays out.
- **Counting redistributions as separate evidence.** `openai__plugins` differs from Figma's diagram skill only in `references/workflow.md`. `lightspeedwp__.github` is a differing copy. `skills-figquery` is a Cursor variant. They are one source.

---

## 6. What the research changed its mind about

### During the iterations

- **Shape breadth is a defence, not a weakness.** Iteration 3 first treated the packet's four shapes as a gap, then reversed it, because most Mermaid shapes render as plain rectangles [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/lineages/deepseek/iterations/iteration-003.md:73].
- **Density became a trade-off, not a missing rule.** Iteration 3 found the checker already automates most of Figma's pre-call checks [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/lineages/deepseek/iterations/iteration-003.md:72].
- **The corpus does cover more kinds.** Iteration 2 found no new type in Figma's guide. Iteration 5 found mermaid-jam builds journey, mindmap and timeline natively [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/lineages/deepseek/iterations/iteration-005.md:22]. This synthesis still rejects adopting them (Section 5).
- **Whole-board and node-by-node reads fit different boards.** Iteration 5 recorded the conflict and resolved it by board size [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/lineages/deepseek/iterations/iteration-005.md:53].
- **The hub note and the subject rule are both true.** Iteration 7 found that they work at different layers, and that the diagram is lost in the gap [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/lineages/deepseek/iterations/iteration-007.md:51]. This synthesis confirmed the loss with the oracle (rank 2).
- **Failure handling was stronger than expected.** Iteration 8 said so after reading the recovery section [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/lineages/deepseek/iterations/iteration-008.md:72].
- **The no-connector case was already solved.** Iteration 9 found only a one-sentence gap [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/lineages/deepseek/iterations/iteration-009.md:34].
- **The budget raise was rejected.** Iteration 10 resisted the loudest evidence [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/lineages/deepseek/iterations/iteration-010.md:31], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/lineages/deepseek/iterations/iteration-010.md:82].

### At this synthesis

Checking each claim against its source dropped or corrected these.

1. **Upstream premise.** Iteration 2 said `figma-use-figjam` and `workflow-skills/` do not exist in the older tree. `skills/figma-use-figjam` exists, and its SKILL and board-content files match the figquery copy. All three named folders predate the 009 pin (Section 3).
2. **Four missing generator constraints.** Iteration 2 finding 2 said the packet lacks quoting, the sequence note drop, the gantt style drop and the `createPage` warning. All four are present [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:61], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/sequence.md:58], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/gantt.md:65], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:52]. Dropped.
3. **No section verb.** Iteration 2 finding 4 said the extension surface has no section. The legend section exists [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:146]. Corrected.
4. **URL only at the end.** Iteration 2 finding 11 said the user sees nothing until extensions finish. The URL goes first [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:47]. Dropped.
5. **No extension triage.** Iteration 2 finding 12 said there is no per-type ranking. It exists [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:41]. Dropped.
6. **No caption.** Iteration 6 finding 5 said the packet never asks for one sentence. `userIntent` is that sentence [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:182]. Corrected in rank 4 to "not used as a cut test".
7. **Coverage report.** Draft rank 5 asked for a coverage ledger. The fidelity ledger exists [SOURCE: AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:119], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:77]. Dropped.
8. **One global budget.** Draft rank 6 and iteration 10 finding 6 said every type uses 9 and 12. Budgets are per type (Section 2). Dropped.
9. **The artifact cannot be a source.** Draft rank 8 asked for a new source class. Product docs are already a source class [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:119]. Folded into rank 2.
10. **The ClickUp offer is missing by accident.** Iteration 9 finding 10 and draft rank 10 framed it as an oversight. The kernel excludes Flow on purpose [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:236]. Moved to Section 5.
11. **No revision contract.** Draft rank 12 asked for one. It exists [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:183], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:246]. The real gap is cross-session (rank 6).
12. **The neutral ramp.** Draft rank 2 paired it with the label rule. The ramp breaks the palette and the one-accent rule. Dropped, and the label rule kept with exemptions (rank 11).
13. **Unmatched retry rule.** Iteration 8 finding 2 and the draft said no corpus source matches it. ompug does [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/docs/DESIGN.md:223]. Corrected.
14. **Independent two-attempt convergence.** Iteration 8 finding 5 called Adobe and the packet unrelated skills converging. Both follow Figma's own rule [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:98]. Corrected.
15. **hferello corroborates independently.** Iteration 6 finding 9 said so. The lane table is Figma's, and the packet's checker says so [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:48]. Corrected.
16. **No corpus plan gate.** Iteration 8 finding 8 said no corpus source has one. Figma's project-plan skill asks which team [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/SKILL.md:341]. Corrected: the packet's stated disclosure reason stays its own.
17. **Ruled-out count.** The draft reports 18 ruled-out directions. The merged registry holds 31. Corrected.
18. **mermaid-jam line.** The draft cites README line 27 for journey, mindmap and timeline. Line 27 is the preserved-positions claim, and the kinds sit at lines 37 to 42. Corrected.

---

## 7. Claims not verified

Nobody should act on these as fact.

- Whether the claude.ai Figma connector exposes `generate_diagram`, `get_figjam`, `use_figma` or `whoami`. Phase 009 also left this open [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/009-figjam-skill-research/research/research.md:277].
- Whether a CLI runtime with Figma's plugin installed reaches the hosted server as rank 3 describes. No live session was run.
- Whether `use_figma` can set shared plugin data on a node `generate_diagram` drew. ompug only wraps the call in a try and catch.
- Whether `get_figjam` returns connector caps and endpoint ids for the packet's own diagrams (rank 12).
- Which `generate_diagram` call shape the live server accepts, `mermaidSyntax` alone or `mermaid` with `editorType`.
- Whether the 18 tools in the new root `mcp.json` are the live tool list. The older `.mcp.json` lists one more.
- That `lightspeedwp__.github` is an older copy. It differs, but nothing in the corpus dates it.
- That the packet's scorecard is the only scored board instrument in the corpus. Eight corpus repos are never cited by any iteration: `figma__community-resources`, `bluescaban__blueprints`, `arinspunk__claude-talk-to-figma-mcp`, `lauragalera__figjam-erd-plugin`, `IamTheLime__dotfiles`, `mkaralevich__pi-figma-labor`, `amo-tech-ai__rocket-path-ai` and `atezer__FMCP`. Iteration 5 only listed two of them, and iteration 4 called `atezer__FMCP` a dead end.
- That generative tools optimise for compactness. That is figjam-builder's opinion [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:46].
- That mermaid-jam really preserves moved positions. Only its README was read.
- That Code Mode has no HTTP manual. That comes from the vendored guide's own inspection [SOURCE: AI Systems/Product Owner/mcp-figma/references/mcp-wiring.md:156], and was not re-checked here.
- The kernel review status. The file records it as pending [SOURCE: AI Systems/Product Owner/SYNC.md:49], and no operator confirmation was seen.
- Why phase 009's `whoami` proposal did not land. No record was found.

---

## 8. Sources

### Corpus repos and pinned commits

The first fifteen pins come from the run's pin file [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/scratch/pins.txt:1]. That file marks the seven phase 009 repos only as "009 pin", so their commits come from the phase 009 goal [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/009-figjam-skill-research/goal.md:81].

| Repo | Pin | Corpus folder |
|---|---|---|
| figma/mcp-server-guide | `056adaf7` | `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/` |
| figma/community-resources | `d868fb1f` | `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__community-resources/` |
| figma/architecture-diagram-components | `c22de634` | `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__architecture-diagram-components/` |
| adobe/spectrum-design-data | `900b522b` | `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/` |
| hferello/ai | `181b6fd7` | `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/` |
| prasantloki/figjam-builder | `2a271c94` | `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/` |
| rrichardsonv/parse-figjam | `2722e737` | `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/rrichardsonv__parse-figjam/` |
| ecestnrkl/figjam-mcp | `8b484791` | `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/` |
| bluescaban/blueprints | `2b987625` | `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/bluescaban__blueprints/` |
| arinspunk/claude-talk-to-figma-mcp | `c7adf243` | `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/arinspunk__claude-talk-to-figma-mcp/` |
| ulasbilgen/mcp-skills-plugins | `c61e27d4` | `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ulasbilgen__mcp-skills-plugins/` |
| tmcw/figjam-mermaid | `57cf9174` | `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/tmcw__figjam-mermaid/` |
| lauragalera/figjam-erd-plugin | `71bda9d7` | `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/lauragalera__figjam-erd-plugin/` |
| lightspeedwp/.github | `8f28eca8` | `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/lightspeedwp__.github/` |
| openai/plugins | `0722921d` | `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/openai__plugins/` |
| amo-tech-ai/rocket-path-ai | `a616047d` | `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/amo-tech-ai__rocket-path-ai/` |
| atezer/FMCP | `364c0ce6` | `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/atezer__FMCP/` |
| IamTheLime/dotfiles | `77976c17` | `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/IamTheLime__dotfiles/` |
| memi-design/mermaid-jam | `568c1e8c` | `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/memi-design__mermaid-jam/` |
| mkaralevich/pi-figma-labor | `97e4c6d8` | `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/mkaralevich__pi-figma-labor/` |
| ompug/diagram-codebase | `b1e20f57` | `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/` |
| southleft/figma-console-mcp-skills | `807fcc1c` | `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/southleft__figma-console-mcp-skills/` |

No iteration added a repo. The merged registry cites only repos from this list.

The phase 009 pin of figma/mcp-server-guide was `7047cb45` [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/009-figjam-skill-research/goal.md:81].

### Product Owner sources read

- `AI Systems/Product Owner/sk-create-figjam/`: `SKILL.md`, `references/flow-mode.md`, `references/quality-rubric.md`, `references/style-guide.md`, `references/hybrid-workflow.md`, `references/types/*.md`, `assets/flow-templates.md`, `scripts/flow_check.py`, `scripts/figjam_checks/flowchart.py` and `manual-testing-playbook/manual-testing-playbook.md`
- The hub: `SKILL.md`, `ROUTER.md`, `hub-router.json`, `mode-registry.json`, `AGENTS.md` and `SYNC.md`
- `AI Systems/Product Owner/sk-product-owner/`: `SKILL.md`, `references/routing.md`, `references/router-contract.md`, `references/story-mode.md`, `references/doc-mode.md`, `references/task-mode.md`, `references/interactive-mode.md`, `assets/story-template.md`, `assets/epic-template.md`, `assets/task-templates.md`, `assets/bug-report-template.md` and `assets/doc-templates.md`
- `AI Systems/Product Owner/claude project/Custom Instructions.md` and `claude project/knowledge/Product Owner - Templates - Flow Mode.md`
- `AI Systems/Product Owner/mcp-figma/SKILL.md`, `mcp-figma/references/mcp-wiring.md`, `mcp-click-up/SKILL.md` and `mcp-click-up/references/mcp-tools.md`
- `AI Systems/Product Owner/benchmark/hub-routing-cases.json`, `benchmark/gates/check_hub.py`, `benchmark/router/route_contract.py` and `benchmark/router/fixtures.json`
- `AI Systems/Product Owner/specs/017-figjam-flow-generation/goal.md`, `spec.md` and the phase 009 `research/research.md`

### Lineage inputs

- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/lineages/deepseek/iterations/iteration-001.md` to `iteration-010.md`
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/lineages/deepseek/research.md`, the lineage draft, treated as claims
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/findings-registry.json`: 119 key findings, 31 ruled-out directions, 5 resolved questions, 0 open

### Checks run during this synthesis

- `flow_check.py --self-test`: 148 of 148 passed, exit 0
- `benchmark/router/route_contract.py --request` on three combined requests: the two artifact-plus-FigJam requests routed to `STORY` and `DOC` with no disambiguation, and "make a FigJam flow from the saved searches story" routed to `FLOW`
- GitHub compare `7047cb45...056adaf7` on figma/mcp-server-guide: one commit, two added files
- Recursive diffs of `skills/` against `skills-figquery/`, of the `openai__plugins` and `lightspeedwp__.github` diagram skills against Figma's, and of the phase 009 corpus copy against this pin

---

## 9. Extension: five more iterations (2026-10-21)

### What ran

Five more iterations ran on DeepSeek V4.1 Flash at max reasoning through cli-pi [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/extension/findings-registry.json:7]. The run stopped at `maxIterationsReached` [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/lineages/deepseek-extension/deep-research-state.jsonl:7]. Its merged registry holds 43 key findings [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/extension/findings-registry.json:1013]. As with the first lineage, the run worked in a staging spec folder and its output was copied in afterwards [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/lineages/deepseek-extension/deep-research-config.json:16]. The lineage sits at `research/lineages/deepseek-extension/`.

Every claim kept below was checked against its cited line or the current Product Owner file. This section cites Product Owner lines as they read today, so its numbers differ from the iterations'. During this synthesis the router oracle ran on 29 distinct requests. `flow_check.py` ran on one planted model and on its self-test. Three Figma developer pages and the upstream history of Figma's `figma-use` skill were fetched.

### Implemented changes found wanting

Eight of the twelve ranks need a follow-up edit. Ranks 4, 7, 10 and 11 were checked against their sources and hold.

#### Rank 1, the board link in the artifact

The shipped rule stops at the link. `flow-mode.md` puts the URL into the artifact's `Flows` group when the read-back matched [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:236]. Rank 1 also asked for the saved artifact to be re-saved under its own filename [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/research.md:83]. No file now ties the link to a re-save. The router contract also ends at the link [SOURCE: AI Systems/Product Owner/sk-product-owner/references/router-contract.md:865]. So the `export/` copy keeps no link and nothing reads it back. The kernel's pair sentence is silent too, so a Project never re-renders its Deliverable Block with the link [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:256].

A Doc has no `Flows` group. Its template puts the board under `Related references` [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/doc-templates.md:460]. Yet `flow-mode.md` and the router contract say `Flows` for every artifact. The pair scenario also ends at the Flow gate, so no playbook step tests the link [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/boundaries/artifact-plus-board-pair.md:31].

The fix: after a matched read-back, add the link, re-save the artifact at its existing export path and read it back. A Project re-renders its Deliverable Block. Both files name `Related references` for a Doc. FJ-037 gains a turn that says yes at the gate and checks the link in the re-saved Story. Reporting the re-save adds a line to the Flow reply, so D6 needs a recorded amendment [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/goal.md:52].

#### Rank 2, the ordered pair

The pair still drops the diagram after common sequencing words. The second-output pattern accepts an output verb only at the start of the text, after "and " or after a comma [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:367]. These six probes each returned `STORY` with no `then` value:

- "write a story for Fernhouse saved searches, then make a figjam diagram of it"
- "write a story for Fernhouse saved searches and then draw a figjam flow of it"
- "write a story for Fernhouse saved searches. Then draw a figjam flow of it"
- "write a story for Fernhouse saved searches plus a figjam diagram"
- "write a story for Fernhouse saved searches and a figjam user flow"
- "write a story for Fernhouse saved searches and also draw a figjam flow"

The controls behaved. "write a story for Fernhouse saved searches and draw the flow in figjam" returned `STORY` with `then: "FLOW"`. "write an epic for Roamstay checkout with a figjam user flow" returned the Epic shape with `then: "FLOW"`.

The fix: let the pattern open after "then", "and then", "and also" or a sentence break. It should also accept "plus" or "and" before "a FigJam" and a diagram noun. The change lands in all three copies [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:367], [SOURCE: AI Systems/Product Owner/sk-product-owner/references/router-contract.md:637], [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:717]. Each phrasing gets a fixture. Rank 13 covers the separate framing gap behind the two requests the dispatcher named.

#### Rank 3, the hosted route connection

The packet gives a reason that the repo's own Code Mode config contradicts. It says the call never runs through Code Mode "because every manual Code Mode holds here is stdio and none reaches an HTTP server" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:180]. Every manual is stdio. But the ClickUp manual is a stdio process that runs `mcp-remote` against ClickUp's hosted server [SOURCE: .utcp_config.json:71], [SOURCE: .utcp_config.json:75], [SOURCE: .utcp_config.json:76]. Three more manuals use the same bridge [SOURCE: .utcp_config.json:159], [SOURCE: .utcp_config.json:177], [SOURCE: .utcp_config.json:235]. So a stdio manual can reach an HTTP server.

The true facts are narrower. Code Mode holds no manual for Figma's hosted server. Its `figma` manual runs Framelink's `figma-developer-mcp` [SOURCE: .utcp_config.json:92]. Whether Figma's OAuth-gated server would admit a Code Mode client is unverified [SOURCE: AI Systems/Product Owner/mcp-figma/references/mcp-wiring.md:157].

Two smaller gaps sit beside it. The packet frontmatter still names Code Mode as its only MCP tool [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:4]. Phase 019 left that on purpose, because no source confirms the native tool prefix [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/019-hosted-route-connection/implementation-summary.md:84]. Figma also marks `generate_diagram`, `use_figma` and `whoami` as remote only [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/]. The packet names the remote URL but never says the desktop server lacks the write tool.

The fix: replace the reason with the narrower facts. Add one sentence that a session connected only to the desktop server has no `generate_diagram`, so it falls to the `fj` route or to No route. Section 6 says the frontmatter waits for a live session to name the native tool prefix.

#### Rank 5, the board critic pass

Step 10 lists the screenshot checks without "a label cut off", which the rubric's board section names [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:68], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:78]. Neither file says where the screenshot comes from. Figma documents that `get_figjam` returns an XML outline plus screenshots of the nodes [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/]. `get_screenshot` also reads FigJam, but it fails without a node id [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md:21]. Adobe's critic also checks weak visual hierarchy, which no packet check names [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:85], [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:86]. Redundant labels are covered, because the rubric checks them on the model before the write [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:41], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:42].

The fix: step 10 and the rubric take the screenshot from `get_figjam` first and from `get_screenshot` with a node id from that read second. Step 10 gains the cut-label check. The board section gains one line: the accent node reads first and no other node competes with it.

#### Rank 6, tags on created nodes

The tag paragraph rests on a superseded Figma rule. It writes shared plugin data "because `use_figma` may refuse `setPluginData`" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:188]. That refusal comes from older copies of Figma's `figma-use` skill, as the lightspeedwp copy shows [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/lightspeedwp__.github/plugins/figma/figma-use/SKILL.md:28]. Figma's own file kept that rule until commit `864d2111` of 2026-07-09 [SOURCE: https://raw.githubusercontent.com/figma/mcp-server-guide/864d2111/skills/figma-use/SKILL.md]. Commit `ef474d18` of 2026-07-30 replaced it, saying shared plugin data "should almost never be needed" [SOURCE: https://raw.githubusercontent.com/figma/mcp-server-guide/ef474d18/skills/figma-use/SKILL.md]. The pinned copy now says "Return node IDs and keep workflow state outside the Figma file" [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-use/SKILL.md:27]. Shared plugin data still works through `use_figma`, because Figma's pinned workflow skill writes it in a `use_figma` script [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/workflow-skills/video-interaction-mapper/scripts/generate_figma_calls.py:6], [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/workflow-skills/video-interaction-mapper/scripts/generate_figma_calls.py:327].

The paragraph also leaves out four things a model needs.

- It never says which value is the key. It packs "one namespace, with the diagram's name and a run id" into one clause [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:188]. A later session can find a tag only by a key it can rebuild. It cannot know an earlier run id
- It never says where the set of created nodes comes from. Figma's block takes the id the tool returns. When there is none, it scans the page children [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:63]. It then counts every new page-level node outside known content as diagram [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:76]. A `use_figma` call hands back only what its script returns, because `console.log` output never reaches the agent [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md:19]
- An architecture write is a set of nodes that can include one or two sections the layout makes [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:67], [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:68]. The tag and the rollback must cover those sections
- Any plugin can read shared plugin data [SOURCE: https://developers.figma.com/docs/plugins/api/properties/nodes-setsharedplugindata/]. A tag should carry ids and the diagram name and nothing from the source material

The fix: name `setSharedPluginData` with a fixed namespace. Use the diagram name as the key and put the run id and the write time in the value. Take the created set from the ids the write returned. When it returns none, take the page-level nodes that were absent before the write, sections included. The tag call returns the ids it tagged. The paragraph records that the tag departs from Figma's rule on workflow state because Flow Mode leaves no file [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:238].

#### Rank 8, the Flow delivery pointers

The pointer in `sk-product-owner/SKILL.md` lists the board URL, the read-back line and the `Extensions:` line only [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:170]. `AGENTS.md` also names the `Left out:` line and the self-scan [SOURCE: AI Systems/Product Owner/AGENTS.md:39]. D6 lists them too [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/goal.md:52]. A reader of the packet file alone misses two lines. The fix: name all five lines or keep only the pointer to Section 8.

#### Rank 9, the plan through whoami

`whoami` says which plans the account holds. It does not say which plan owns a file. Figma's spec skill tells the caller to ask instead [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-spec/SKILL.md:9]. The packet says a single plan from `whoami` "resolves the gap and the gate names it" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:266]. That holds for a new file. A revision writes into a board whose plan was set when it was made, so a plan read from `whoami` can misname it [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:183].

The fix: on a revision the gate names the board and states its plan only when the user supplied it. The plan-field condition stays as it is, because Figma documents `planKey` for generative plugins and shaders only [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/].

#### Rank 12, read-back direction

The direction rule has no answer for a connector with a missing end. The corpus parser skips such a connector, because "without both endpoints there is no relation to express" [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/src/lib/connectorGraph.ts:13]. It also treats an end pinned to the page or canvas as no node [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/src/lib/connectorGraph.ts:17], [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/src/lib/connectorGraph.ts:29]. The packet reads every connector by its two endpoint ids and never names a cap value [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:218]. Figma's cap type has six plain values, `NONE` and five end shapes, plus six ER cardinality markers [SOURCE: https://developers.figma.com/docs/plugins/api/ConnectorStrokeCap/].

The fix: a connector with a missing or canvas-pinned end is a mismatch named as dangling. It is never matched by its position. The cap fields get named once a live `get_figjam` read shows them. Rank 17 covers the ER markers.

#### The ranks that hold

The accent line keeps Adobe's one-node test and its split rule [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:49], [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:23], [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:32]. The cut test uses the `userIntent` sentence [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:38]. That settles rank 4. For rank 7, the kernel's no-connector sentence carries both qualifiers [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:255]. For rank 10, the self-edit answer and the hand-edit offer are both in place [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:254], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:258]. For rank 11, the repeated-label rule matches Adobe's none-or-one count with the exemptions rank 11 named [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:42], [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:54]. Rank 11 left the script check for later [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/research.md:193], so rank 15 below proposes it as a new change.

### Further ranked improvements

Five changes are ranked below. None repeats ranks 1 to 12. Two are integration changes, marked [INTEGRATION].

#### Rank 13. Make "write a doc" and "write a bug" frame their artifacts [INTEGRATION]

It changes `AI Systems/Product Owner/benchmark/router/route_contract.py`, the Router Contract copy in `sk-product-owner/references/router-contract.md` and the kernel's router copy, plus `benchmark/router/fixtures.json` and `benchmark/hub-routing-cases.json`.

The router contract names "write a task/bug/PRD/doc" requests as artifact framing [SOURCE: AI Systems/Product Owner/sk-product-owner/references/routing.md:26], [SOURCE: AI Systems/Product Owner/sk-product-owner/references/router-contract.md:857]. The oracle frames only two of those four. Its DOC nouns hold `docs` and `document` but no bare `doc` [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:305]. Its BUG frames need "bug report", "defect report" or a symptom verb [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:261], [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:262]. The kernel copies the same noun list [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:559].

It matters because both failures were observed during this synthesis. "write a doc about Roamstay onboarding", "write a bug about the Loomlist export" and "file a bug for the Loomlist export" each returned `INTERACTIVE` from the fallback with a question. With a board named, "write a doc about onboarding and draw it on a figjam board" and "write a bug about it and add a figjam diagram" returned `FLOW`. The artifact is lost and no pair can form, because FLOW is dropped only when a second frame matched [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:648]. The pair rides only on an artifact intent [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:718]. The controls "write a task about the Loomlist export" and "write a PRD for Fernhouse saved searches" framed correctly.

The change: add `doc` to the DOC noun list and a "write, file or log a bug about or for" frame to BUG in all three copies. Each phrasing gets a fixture and a gold row. A Bug pair joins the fixtures, which hold a Story pair and a runbook pair today [SOURCE: AI Systems/Product Owner/benchmark/router/fixtures.json:2516], [SOURCE: AI Systems/Product Owner/benchmark/router/fixtures.json:2527].

#### Rank 14. End the pair's first reply on the Flow gate and offer ClickUp after the link is in [INTEGRATION]

It changes the Closing Line section of `AI Systems/Product Owner/sk-product-owner/assets/interactive-response-templates.md`, the kernel at lines 256 and 296 and the FJ-037 scenario.

The pair has no defined reply ending. The delivery shape closes an artifact reply on one line, which is the ClickUp offer when ClickUp is connected [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/interactive-response-templates.md:188]. It adds that nothing follows the closing line [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/interactive-response-templates.md:192]. FJ-037 expects the same reply to deliver the Story and then end on Flow Mode's gate [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/boundaries/artifact-plus-board-pair.md:31]. The kernel delivers the artifact first "in its own reply shape" [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:256]. That shape ends on the ClickUp offer [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:296].

It matters because a user who accepts that offer pushes an artifact with no board link yet. ClickUp has no other way to carry the board, because its attach tools take a local file [SOURCE: AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:150], [SOURCE: AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:151]. The body link is the only route [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:248].

The change: when the route carries `then: "FLOW"`, the artifact reply ends on the Flow gate with no ClickUp offer. The offer comes once the link is written back and the artifact is re-saved. This splits Section 5's rejection of a ClickUp offer from the Flow reply [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/research.md:227]. The attachment stays rejected. The offer moves to the end of the pair.

#### Rank 15. Count repeated edge labels in the checker

It changes `AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py` and the self-test's planted models.

Rank 11's rule is checked by hand only. Its phase records that the check script does not count repeated labels [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/027-repeated-edge-labels/implementation-summary.md:92]. During this synthesis a process model with four edges all labelled `then` passed `flow_check.py` with exit 0. Adobe states the rule as a count, so a script can enforce it [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:54].

The change: the user-flow and process check counts identical labels on non-decision edges and fails at four [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:196]. The self-test plants one failing model. It passes 148 of 148 checks today. Architecture keeps its own edge rules [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:294]. Sequence messages stay exempt [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:42].

#### Rank 16. Name the read-call allowance in the gate

It changes `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` step 7 and Section 6. It also changes the Flow Mode Project mirror.

Figma's guide limits Starter users and View or Collab seats to "6 tool calls per month" [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/README.md:8]. Read tools are rate limited, while some write tools are exempt [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/README.md:6]. Figma lists `whoami`, `get_figjam` and `get_screenshot` as read tools [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/]. A one-diagram write spends a `whoami` call before the gate, a `get_figjam` read-back and a screenshot when the read carries none [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:183], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:187], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:68].

It matters because such a user can spend the month's allowance in two one-diagram writes. Their read-backs then fail for a reason the packet never names. The change: the gate states the read calls the write will spend [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:65]. A read refused for the limit gives `Read-back: not possible` with the limit named. The board is never called done.

#### Rank 17. Read an ER's cardinality from the end caps

It changes `AI Systems/Product Owner/sk-create-figjam/references/types/er.md` Section 7 and `flow-mode.md` Section 7.

The ER read-back checks each relationship's "two ends and label" [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/er.md:109]. It never checks cardinality, though the type says the right cardinality matters more than a full column list [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/er.md:81]. The model allows four markers on each end [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/er.md:69]. Figma's cap type carries matching markers such as `ERD_EXACTLY_ONE`, `ERD_ZERO_OR_ONE`, `ERD_ZERO_OR_MORE` and `ERD_ONE_OR_MORE` [SOURCE: https://developers.figma.com/docs/plugins/api/ConnectorStrokeCap/].

It matters because the Section 7 direction rule reads every cap as an arrow or none [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:218]. An ER connector with markers at both ends could then read as two-way and fail. The corpus parser has the same blind spot, because it counts only arrow caps [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/src/lib/connectorGraph.ts:45].

The change: an ER read-back compares each end's cap with the model's cardinality. Section 7 says the arrow rule does not apply to ER markers. Its gain depends on the generator drawing ERD caps, which no live read has shown.

### What the public docs settle

- The hosted tool list is settled. Figma's tools page lists 18 read tools and 14 write tools, with Weave tools listed apart [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/]. The plugin's root `mcp.json` names 18 titles, so it is a subset [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/mcp.json:13], [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/mcp.json:30]. The page marks `generate_diagram`, `use_figma`, `create_new_file` and `whoami` as remote only, while `get_figjam` and `get_screenshot` also run on the desktop server. The packet's rule to list the connected tools at run time stays right [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:182]
- `whoami` is settled. It returns the signed-in email, every plan and the seat on each plan [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/]. It cannot say which plan owns a file [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-spec/SKILL.md:9]. Its `planKey`, in the form `(team|organization)::<numeric-id>`, feeds generative plugins and shaders. No source gives `generate_diagram` a plan field
- The `get_figjam` fields are settled in part. It returns an XML outline like `get_metadata` plus screenshots of the nodes [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/]. The XML carries the ids of pages, sections, stickies and connectors [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-use-figjam/SKILL.md:17]. The attribute names for connector endpoints and caps stay unverified
- Plugin data in `use_figma` is settled for the skill text and open for a live diagram. Older `figma-use` text said `setPluginData` is not supported while shared plugin data is [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/lightspeedwp__.github/plugins/figma/figma-use/SKILL.md:28]. Figma dropped that rule on 2026-07-30 [SOURCE: https://raw.githubusercontent.com/figma/mcp-server-guide/ef474d18/skills/figma-use/SKILL.md]. The pinned rule now keeps workflow state outside the file [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-use/SKILL.md:27]. Figma's own workflow skill still writes shared plugin data through `use_figma` [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/workflow-skills/video-interaction-mapper/scripts/generate_figma_calls.py:327]. The API page asks for a namespace of at least three alphanumeric characters [SOURCE: https://developers.figma.com/docs/plugins/api/properties/nodes-setsharedplugindata/]. Whether the call succeeds on a node `generate_diagram` drew stays unverified

### Corrections to the iterations

Twenty iteration or draft claims were dropped or corrected.

1. Iteration 1 finding 8 said the critic lacks Adobe's redundant-label check. The rubric checks redundant labels on the model before the write [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:41]. Only weak hierarchy is missing. Corrected
2. Iteration 1 finding 9 said nothing catches a repeated-label breach. The rubric's remove test is walked by hand at step 6 [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:64]. Only the script check is missing, which rank 15 adds. Corrected
3. Iteration 1 cited the phase 022 and 027 limitations at lines 96 and 95. They sit at line 93 [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/022-created-node-tags/implementation-summary.md:93] and line 92 [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/027-repeated-edge-labels/implementation-summary.md:92]. Corrected
4. Iteration 1 finding 10 called the Code Mode sentence unverified. Its reason is contradicted by the repo's own config [SOURCE: .utcp_config.json:75]. Strengthened under rank 3
5. Iteration 2 finding 1 called the `setPluginData` refusal a current prohibition. It comes from a `figma-use` version Figma replaced in July 2026 [SOURCE: https://raw.githubusercontent.com/figma/mcp-server-guide/ef474d18/skills/figma-use/SKILL.md]. Corrected
6. Iteration 2 finding 2 said the shared-data namespace needs no manifest entry. The API page says nothing about a manifest [SOURCE: https://developers.figma.com/docs/plugins/api/properties/nodes-setsharedplugindata/]. Dropped
7. Iteration 2 finding 4 and draft rank 3 treated `planKey` as the plan field for a diagram write. Figma documents it for generative plugins and shaders only [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/]. Corrected
8. Iteration 2 finding 7 said a desktop-server reader must find the missing write tool alone. The packet names the remote URL and lists the tools first [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:182]. Narrowed to the one-sentence fix under rank 3
9. Iteration 2 finding 8 said user flow and process rest on an unstated inference. Both are `flowchart` blocks [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:38], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/types/process.md:41]. Figma lists flowcharts [SOURCE: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/]. Dropped
10. Iteration 3 finding 3 counted five `ERD_*` caps. Figma lists six [SOURCE: https://developers.figma.com/docs/plugins/api/ConnectorStrokeCap/]. Corrected
11. Iteration 3 finding 4 said read tools are capped at six calls a month. The README says "6 tool calls per month" without naming reads [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/README.md:8]. Corrected
12. Iteration 3 finding 6 said the packet lacks the draft-file cost. The packet passes the `fileKey` after the first call and sends the user to the drafts after a failed first call [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:185], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:186]. Dropped
13. Iteration 3 finding 7 treated `figma-use-slides` as web material published after the pins. It is in the pinned corpus at `figma__mcp-server-guide/skills/figma-use-slides/`. Corrected
14. Iteration 4 finding 2 said the Flow row promises a doc-sourced board that the router never makes. Drawing from a supplied doc routes to Flow as intended. "turn this doc into a figjam board" returned `FLOW` [SOURCE: AI Systems/Product Owner/benchmark/router/differential_corpus.json:39]. Dropped
15. Iteration 4 finding 3 said no gold row or fixture pairs a Doc with a board. The runbook pair exists [SOURCE: AI Systems/Product Owner/benchmark/router/fixtures.json:2527], [SOURCE: AI Systems/Product Owner/benchmark/hub-routing-cases.json:177]. Only a Bug pair is missing. Corrected
16. Iteration 5 findings 1 and 2 said the lightspeedwp copy is newer than the pin. Figma's history shows the reverse, because the rule sat in `figma-use` until July 2026 [SOURCE: https://api.github.com/repos/figma/mcp-server-guide/commits?path=skills/figma-use/SKILL.md]. Reversed. Section 5's rejection of redistributions as separate evidence stands without the qualification
17. Iteration 5 finding 4 said the run-manifest rejection is stronger now. Figma now prefers workflow state outside the file [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-use/SKILL.md:27]. The rejection rests on D6 alone [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/goal.md:52]. Corrected
18. Draft rank 7 listed ERD caps as arrowheads. They are cardinality markers [SOURCE: https://developers.figma.com/docs/plugins/api/ConnectorStrokeCap/]. Corrected in rank 17
19. The draft's verdict table passed phase 017 and failed phase 027. Phase 017 lacks the re-save and the Doc wording, as rank 1 above shows. Phase 027 matches its corpus line. Its missing script is new work. Corrected
20. The draft left open whether the plugin-data refusal is a sandbox policy or a version difference. The skill history shows a version difference in Figma's text [SOURCE: https://raw.githubusercontent.com/figma/mcp-server-guide/864d2111/skills/figma-use/SKILL.md]. Corrected

### Claims not verified

- Whether `setSharedPluginData` succeeds through `use_figma` on a node `generate_diagram` drew. One live tag call followed by a read of the tag would confirm it
- The attribute names `get_figjam` uses for connector endpoints and caps. Whether a generated ER carries `ERD_*` caps is open too. One live read of a generated ER would settle both
- Whether `generate_diagram` returns node ids or only a link. Figma's block allows either [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:63]. A live call would show it
- Which call shape the live server accepts. The pinned tree holds `mermaidSyntax` [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-generate-diagram/SKILL.md:85] beside `mermaid` with `editorType` [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/workflow-skills/generate-project-plan/references/blocks/diagram-section.md:57]. The schema the server reports at run time decides it
- Whether Figma's OAuth-gated server admits a Code Mode client through `mcp-remote`. Only a live connection attempt would show it [SOURCE: AI Systems/Product Owner/mcp-figma/references/mcp-wiring.md:157]
- Whether the six-call monthly cap counts every tool call or only reads. Figma's rate-limit help page would confirm it
- Whether the packet's `allowed-tools` line blocks native Figma MCP tools in a given runtime. A Claude Code run with Figma's plugin installed would show it
- `create_session`, which the pinned `figma-use` asks for "when available" [SOURCE: AI Systems/Product Owner/specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/skills/figma-use/SKILL.md:9]. The tools page does not list it
- The Figma blog post and community skills page that iteration 3 cited. Neither was opened during this synthesis
- The ClickUp ordering gap in rank 14. It rests on written contracts. No push was observed
- Whether the claude.ai Figma connector exposes `generate_diagram`, `get_figjam`, `use_figma` or `whoami`. This stays open from Section 7
