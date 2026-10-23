# FigJam Packet and Product Owner Integration: Research Synthesis

**Run:** fanout-deepseek-1792527089584-nrdj43
**Spec folder:** specs/017-figjam-flow-generation/016-figjam-improvement-research
**Lineage:** specs/017-figjam-flow-generation/016-figjam-improvement-research/research/lineages/deepseek
**Iterations:** 10 of 10
**Key questions:** 5 of 5 answered
**Stop reason:** maxIterationsReached

---

## 1. Overview

This lineage asked how Product Owner's `sk-create-figjam` packet and its integration with `sk-product-owner` can improve when judged against public FigJam work. Ten iterations compared the packet's rules and the hub's integration surfaces with a pinned corpus of 22 public repositories. The packet turns screenshots, Figma flows and product docs into a checked Mermaid model of one of seven types and writes it to FigJam through the hosted Figma MCP, with `figma-ds-cli fj` as the Figma Desktop fallback.

The short answer: the packet's verification, retry and rollback rules are stronger than anything in the corpus, and its delivery contract is unusually honest. Its weaknesses are taste selection (which node gets the accent, which diagram earns its caption), revision mechanics (no manifest, no partial update), coverage accounting, and every seam that crosses into `sk-product-owner`, the claude.ai kernel or ClickUp. Twelve improvements are ranked below; five are integration changes.

---

## 2. Research Question

How can Product Owner's `sk-create-figjam` packet and its integration with `sk-product-owner` improve, judged against the public FigJam work online?

Five key questions structured the work:

- **Q1** — Which diagram types, diagram kinds and model rules does the public corpus expose that the packet's seven types do not cover? *(answered, iteration 5)*
- **Q2** — Which layout, colour, density and board-quality measurement practices exceed the packet's style guide, quality rubric and manual-testing scorecard? *(answered, iteration 6)*
- **Q3** — How do public projects handle read-back, revision, fileKey reuse, failure and retry, and delivery, and what does the packet do differently? *(answered, iteration 8)*
- **Q4** — How does a Flow request reach the packet through the hub and `sk-product-owner`, and where does the handoff back to a Story, Epic, Doc, Task or Bug break? *(answered, iteration 7)*
- **Q5** — What must the claude.ai kernel and knowledge files change so a Project without a Figma connector can still run Flow, and should a board URL reach ClickUp through the vendored transport? *(answered, iteration 9)*

---

## 3. Scope and Method

**Packet sources read:** `SKILL.md`, `references/flow-mode.md`, `references/types/*.md` (user flow, process, architecture, sequence, state, ER, gantt), `references/style-guide.md`, `references/quality-rubric.md`, `references/hybrid-workflow.md`, `assets/flow-templates.md`, `scripts/flow_check.py`, `scripts/figjam_checks/flowchart.py`, and the board-quality scorecard in the manual-testing playbook.

**Integration surfaces read:** the hub `SKILL.md`, `ROUTER.md`, `hub-router.json`, `mode-registry.json`, `AGENTS.md`; `sk-product-owner/SKILL.md`, `references/routing.md`, `references/router-contract.md`, `references/doc-mode.md`, `references/story-mode.md`, `assets/story-template.md`; the claude.ai kernel and the Flow Knowledge mirror; `mcp-click-up`'s tool guide; `SYNC.md`.

**Corpus read (22 pinned repositories):** `figma__mcp-server-guide` (skills, `skills-figquery`, `workflow-skills/generate-project-plan`, `figma-power` sampled), `figma__community-resources`, `figma__architecture-diagram-components`, `openai__plugins` (sampled), `lightspeedwp__.github`, `adobe__spectrum-design-data`, `hferello__ai`, `prasantloki__figjam-builder`, `rrichardsonv__parse-figjam`, `ecestnrkl__figjam-mcp`, `bluescaban__blueprints`, `arinspunk__claude-talk-to-figma-mcp`, `ulasbilgen__mcp-skills-plugins`, `tmcw__figjam-mermaid`, `lauragalera__figjam-erd-plugin`, `IamTheLime__dotfiles`, `southleft__figma-console-mcp-skills`, `mkaralevich__pi-figma-labor`, `amo-tech-ai__rocket-path-ai`, `atezer__FMCP`, `ompug__diagram-codebase`, `memi-design__mermaid-jam`.

**Method:** each iteration read a new surface or deepened an earlier finding, cited every claim as `[SOURCE: path:line]`, appended its delta and iteration record through the gateway, and ran the state reducer. Convergence mode was off; the run ended at the configured cap.

**Boundaries honored:** no `AI Systems/Product Context`, no screenshots, no board URLs, no containment-folder content, no Barter product flows; no nested CLI or agent dispatch; writes confined to the lineage directory.

---

## 4. What the Packet Already Does Better Than the Corpus

These are protected strengths. None of the recommendations below removes them.

1. **Machine-checked model rules.** The lane table is checked, not prose: fixed architecture lanes, dotted async/external edges, cycle detection, lane count. `hferello` carries the same table as prose only [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/arch-flow/references/figjam-architecture.md:10], [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:47].
2. **Failure honesty.** A timeout is unknown, not failed; the target is read before a retry; a first-call failure sends the user to their drafts [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:183]. No corpus source matches this.
3. **Scoped rollback.** Only nodes and connectors this write created may be deleted, after a yes, and the run stops on a foreign node [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:186].
4. **Bounded repair.** Two attempts at the same diagram, then stop and ask [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:245]. Adobe independently converges on the same bound [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md:161].
5. **Measured palette with contrast gates.** Every palette pair is re-measured by `flow_check.py --self-test`; corpus palette systems give hex values and tiers but no contrast proof.
6. **A scored quality instrument.** The seven-dimension 0–2 scorecard is the only scored board-quality instrument in the corpus; every other source stops at guidance.
7. **A confidentiality gate.** The plan is fixed before the write because a board in the wrong plan is visible to that plan's members immediately [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:253].
8. **Truthful degradation.** With no route, the packet offers the checked model and refuses an image, HTML or Mermaid stand-in [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:203].

---

## 5. Findings by Theme

### 5.1 Type coverage (Q1)

The packet draws seven types; public FigJam work covers more. `mermaid-jam` exposes journey, mindmap, timeline and markdown user-flow kinds, with diagnostics for pie, gantt, ERD and class [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/memi-design__mermaid-jam/README.md:27]. Adobe explicitly refuses pie charts, mindmaps, venn diagrams, class diagrams and timelines because the generator does not support them [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md:157]. The packet's type-fit rule already says to answer an unsupported kind with the nearest it draws or a plain no [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:29]; what is missing is a named boundary list and a reason, not a new type.

The corpus also documents what a generated architecture cannot express: owned-versus-external service variants and icon overlays from a manual component library [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__architecture-diagram-components/README.md:23]. The packet should not promise those.

### 5.2 Model rules and diagram grammar (Q1)

`figjam-builder` contributes a board-quality grammar — eleven principles, three palette tiers with a job per tier, paired type roles, and a fourteen-item audit pass — with one rule the packet needs most: trace every required edge source-to-target, because neither a connector count nor a collision-free bounding box proves clarity [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:323]. It also documents the large-board reading ladder (whole board, then child ids, metadata batches, parallel screenshots, halving on timeout), the section-local coordinate trap, and the 5-per-call upload limit [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:382], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/SKILL.md:412].

`mermaid-jam` preserves manually moved node positions during updates when ids match and offers a rules-based Revise cleanup [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/memi-design__mermaid-jam/README.md:83]; `figjam-mermaid` runs the reverse direction the packet never runs, turning stickies and connectors into Mermaid text [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/tmcw__figjam-mermaid/README.md:1].

### 5.3 Layout, colour and density (Q2)

Adobe's house style is the strongest single source:

- One accent = the node the diagram exists to explain, never by position or habit, at most one per diagram, split when two tie [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:22].
- Precedence as a light-to-dark neutral step, not a hue per stage [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:36].
- Connectors recede; four or more identical edge labels become zero or one [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:50].
- One header per column instead of a phase name in every node; consistent node size and radius; aligned parallel chains [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:56].
- One message per diagram with a one-sentence caption that cuts completeness nodes [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:69].
- Cross-diagram consistency on a shared board [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md:76].

Density evidence spans three numbers: the packet's 9 nodes and 12 connectors [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:162], Figma's own 20/25 guidance, and `diagram-codebase`'s 25/30 with 12–20 for a master and split-with-notes [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/docs/DESIGN.md:192]. The packet's number is defensible only because it cannot move generated nodes; the transferable rule is a per-type budget with explicit skips, not a flat raise.

### 5.4 Read-back, revision, retry and delivery (Q3)

The packet leads on read-back and failure handling. It compares the board to the model by count, label, endpoints, direction and type extras, and labels a screenshot read as visual because a picture cannot prove joins [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:211], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:215]. Adobe's critic uses a screenshot as its main evidence, which is fine for visual judgment and insufficient for join proof; the packet's distinction is the sharper one.

The corpus leads on revision mechanics. `diagram-codebase` reuses one file across `--resume` and `--update` and regenerates only affected diagrams [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/README.md:192], [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/README.md:232]; `mermaid-jam` preserves moved positions [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/memi-design__mermaid-jam/README.md:27]. The packet has no manifest, no coverage report and no revision mode: a bad layout is fixed only by splitting or reshaping [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:164].

Delivery is the packet's weakest reach and its strongest honesty: the reply carries the board, its proof and the self-scan and nothing else [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:221], no file is left behind, and a missing route offers the checked model. Adobe instead exports, crops by bounding box, normalizes the canvas and embeds an image with alt text [SOURCE: specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md:98].

### 5.5 Integration (Q4, Q5)

Routing is correctly two-stage, with FigJam as a sibling packet [SOURCE: AI Systems/Product Owner/SKILL.md:38], [SOURCE: AI Systems/Product Owner/ROUTER.md:21]. The handoff, however, is prose: the Product Owner resource map keeps a FLOW lane that a guard drops [SOURCE: AI Systems/Product Owner/sk-product-owner/references/router-contract.md:146], and the Flow reply is terminal. The two halves even have incompatible completion protocols: artifacts save to `export/` before replying, Flow is the sole exemption [SOURCE: AI Systems/Product Owner/AGENTS.md:37], [SOURCE: AI Systems/Product Owner/AGENTS.md:39].

Three concrete breaks follow:

1. **Artifact-side FigJam is a subject, never a route.** "FigJam wording beside another artifact's framing is that artifact's subject", so a runbook with a FigJam process never loads Flow Mode [SOURCE: AI Systems/Product Owner/sk-product-owner/references/routing.md:26]. Doc Mode preserves supplied diagrams as text but never commissions one [SOURCE: AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:275].
2. **A Story cannot carry the board.** Story Mode never invents a Figma destination and forbids images or paths, because images are embedded in ClickUp after export [SOURCE: AI Systems/Product Owner/sk-product-owner/references/story-mode.md:163], [SOURCE: AI Systems/Product Owner/sk-product-owner/assets/story-template.md:103]. The `Flows` sub-label exists, but a same-session board URL is not "supplied" under the current wording.
3. **Two-packet requests cost a question.** Stage one never forms an ordered bundle; two packets' signals start in the default mode and ask which comes first [SOURCE: AI Systems/Product Owner/hub-router.json:15], [SOURCE: AI Systems/Product Owner/SKILL.md:79].

The Project packaging already solves the no-connector case: with no Figma connector the kernel says so, never claims a board, and offers the checked model as a fenced Mermaid block [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:255], and the Flow Knowledge mirror states it more tightly, labelled as the model and never as the board, with no image or HTML stand-in [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:168]. The kernel's sentence omits that qualifier — a one-sentence parity gap.

ClickUp is a link problem, not an upload problem. The transport supports comments and file attachments [SOURCE: AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:102], [SOURCE: AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:150], but an attachment is a file upload and the artifact rules forbid images. The board URL belongs in the artifact's `Flows` group or a task comment. The ClickUp offer never fires after a Flow reply, because it follows a Deliverable Block that Flow does not render [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:295].

---

## 6. Recommendations (ranked)

Each row names the Product Owner file it changes and the evidence it comes from. Integration changes are marked **[INTEGRATION]**.

| # | Change | Product Owner file(s) | Evidence |
|---|---|---|---|
| 1 | Replace the four-candidate accent menu with the "one node the diagram exists to explain" test, and require a one-sentence caption that cuts anything not serving it | `sk-create-figjam/references/style-guide.md`, `references/quality-rubric.md` §3 | Adobe house style :22, :69; packet rubric :47 |
| 2 | Add a redundant-edge-label rule (4+ identical → 0 or 1) and a neutral light-to-dark ordering ramp | `references/style-guide.md`, `references/types/process.md`, `references/types/gantt.md` | Adobe house style :36, :50; packet style guide :31 |
| 3 | Add a bounded post-write critic pass over the Mermaid plus one screenshot, applied in one batch, stopped by the existing two-attempt bound | `references/quality-rubric.md` §6, `references/flow-mode.md` §7 | Adobe house style :82; packet flow-mode :245 |
| 4 | Emit a run manifest: fileKey, diagram titles, written node ids, pending action, content hash | `references/flow-mode.md` §8, `assets/flow-templates.md`, `scripts/flow_check.py` | `diagram-codebase` DESIGN :59, :60, :175 |
| 5 | Add a coverage and skipped report beside `Left out:`, accounting for every source item as drawn, split or skipped with a reason | `references/flow-mode.md` §8, provenance table | `diagram-codebase` DESIGN :148; packet flow-mode :226 |
| 6 | Make the budget type-specific (e.g. user flow 9, gantt/ER higher) with split-with-notes, instead of one global 9 | `references/types/*.md`, `scripts/figjam_checks/*.py` | `diagram-codebase` DESIGN :192–193; packet flow-mode :162 |
| 7 | **[INTEGRATION]** Write the board URL back into the asking artifact: `Flows` group for Story/Epic, `## Visual diagram` for Doc, link field for Task; treat a same-session board as supplied | `sk-product-owner/references/story-mode.md`, `assets/story-template.md`, `references/doc-mode.md`, `references/task-mode.md` | `hferello` SKILL :166, :170, :173; packet story-template :103 |
| 8 | **[INTEGRATION]** Carry the artifact into Flow Mode as a source class and pass its reference across the router guard, so labels quote the artifact's own words | `sk-create-figjam/references/flow-mode.md` §4, `sk-product-owner/references/router-contract.md` | `hferello` SKILL :166, :168; packet flow-mode :144 |
| 9 | **[INTEGRATION]** Form the artifact-then-diagram ordered bundle at stage one instead of asking which comes first | `SKILL.md` stage-one rules, `hub-router.json` `outcomes`, `ROUTER.md` tie rule | packet hub-router :15, ROUTER :37, hub SKILL :79 |
| 10 | **[INTEGRATION]** Offer ClickUp after a Flow reply; carry the URL as a body `Flows` link or comment, never an attachment | `claude project/Custom Instructions.md` Flow Mode Delivery, `sk-product-owner/references/task-mode.md` | kernel :295, :250; mcp-tools :102, :150; story-template :103 |
| 11 | **[INTEGRATION]** Carry the mirror's "never as the board" qualifier and image/HTML ban into the kernel sentence | `claude project/Custom Instructions.md` (one sentence) | kernel :255; Flow Knowledge :168 |
| 12 | Define a revision contract: same fileKey, delete the diagram's own nodes, re-check, re-read, report the change; state that moved positions cannot be preserved | `references/flow-mode.md` §9 | packet flow-mode :182, :164, :245; `diagram-codebase` README :192; `mermaid-jam` README :27 |

**Sequencing.** Ranks 1–3 are rule edits that need no new tooling and improve every diagram immediately. Rank 4 is the prerequisite for rank 12 and for any future incremental write. Ranks 7–11 are independent of each other and can land in any order, but rank 9 changes routing, so it should follow ranks 7 and 8 so the bundle has a working return path.

---

## 7. Eliminated Alternatives

| Approach | Reason Eliminated | Evidence | Iteration(s) |
|---|---|---|---|
| Blanket budget raise from 9 to 25 nodes | The corpus tools own layout differently; the packet cannot move generated nodes, so a flat raise trades legibility for coverage | `diagram-codebase` DESIGN :192; packet flow-mode :164 | 6, 8, 10 |
| Export-and-embed pipeline inside Flow Mode | Conflicts with the no-file delivery rule and needs a site build; belongs to a Doc/publication route | Adobe SKILL :98; packet flow-mode :203 | 6, 10 |
| Preserve manually moved positions during revision | Requires external geometry the generator does not accept | `mermaid-jam` README :27; packet flow-mode :164 | 5, 8, 10 |
| Treat `figjam-mermaid` as a read-back route | Reads stickies and connectors only, not a typed model | `tmcw` README :1 | 5, 10 |
| Adopt `figjam-builder` vibrant palette tiers for diagram fills | Fails the packet's measured contrast gate | `figjam-builder` SKILL :154; packet style guide | 5, 10 |
| Mirror `mcp-click-up` into the Project | A Project uses its own connector; CLI verbs do not exist there | `SYNC.md` :75 | 9, 10 |
| A screenshot as proof of structure | A picture cannot prove which nodes a connector joins | packet flow-mode :215; Adobe house style :82 | 7, 8, 10 |
| A file attachment as the ClickUp carrier for a board | Artifact rules forbid images and paths; an attachment is a file upload | story-template :103; mcp-tools :150 | 7, 9, 10 |
| A new packet for diagrams | Flow already routes to a sibling packet; the gaps are inside existing files | hub SKILL :38; ROUTER :33 | 7, 10 |
| Adopting the component library's ownership variants | Manual library; `generate_diagram` cannot express variants | `architecture-diagram-components` README :23 | 6 |

---

## 8. Open Questions

None. All five key questions are answered. Three boundary notes remain for a later run, none of which blocked a finding:

- `figma-power` and the OpenAI plugins packaging were sampled rather than read in full; no recommendation depends on them.
- The kernel v1.2.2 review is pending per `SYNC.md`; this synthesis reports the state as it stands, not as reviewed.
- ClickUp was assessed through its documented tool surface, not a live connector session.

---

## 9. Evidence Quality and Limits

- **Strong:** the packet's own rules were read directly, at line level, and its checks are executable; corpus claims come from pinned repository files.
- **Medium:** density and revision conclusions rest on three independent sources but no live board measurement; the corpus never measured against this packet's no-move constraint.
- **Weak:** the ClickUp and Project integration conclusions rest on documented tool surfaces and kernel text, not on a live connector run. No claim here asserts deployment, review or runtime state.
- **Not asserted:** that any change was implemented, reviewed, deployed or tested. This synthesis recommends; it does not claim execution.

---

## 10. Sources

**Product Owner packet**
- `AI Systems/Product Owner/sk-create-figjam/SKILL.md`
- `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md`
- `AI Systems/Product Owner/sk-create-figjam/references/types/*.md`
- `AI Systems/Product Owner/sk-create-figjam/references/style-guide.md`
- `AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md`
- `AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md`
- `AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py`, `scripts/figjam_checks/flowchart.py`

**Integration**
- `AI Systems/Product Owner/SKILL.md`, `ROUTER.md`, `hub-router.json`, `mode-registry.json`, `AGENTS.md`
- `AI Systems/Product Owner/sk-product-owner/SKILL.md`, `references/routing.md`, `references/router-contract.md`, `references/doc-mode.md`, `references/story-mode.md`, `assets/story-template.md`
- `AI Systems/Product Owner/claude project/Custom Instructions.md`
- `AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md`
- `AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md`
- `AI Systems/Product Owner/SYNC.md`

**Corpus (22 pinned repositories)**
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__mcp-server-guide/`
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__community-resources/`
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/figma__architecture-diagram-components/`
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/openai__plugins/`
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/lightspeedwp__.github/`
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/adobe__spectrum-design-data/`
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/hferello__ai/`
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/prasantloki__figjam-builder/`
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/rrichardsonv__parse-figjam/`
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ecestnrkl__figjam-mcp/`
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/bluescaban__blueprints/`
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/arinspunk__claude-talk-to-figma-mcp/`
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ulasbilgen__mcp-skills-plugins/`
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/tmcw__figjam-mermaid/`
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/lauragalera__figjam-erd-plugin/`
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/IamTheLime__dotfiles/`
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/southleft__figma-console-mcp-skills/`
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/mkaralevich__pi-figma-labor/`
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/amo-tech-ai__rocket-path-ai/`
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/atezer__FMCP/`
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/ompug__diagram-codebase/`
- `specs/017-figjam-flow-generation/016-figjam-improvement-research/research/corpus/memi-design__mermaid-jam/`

---

## 11. Metrics and Provenance

| Field | Value |
|---|---|
| Iterations completed | 10 |
| Key questions answered | 5 of 5 |
| Key findings in registry | 119 |
| Ruled-out directions | 18 |
| New-information trend | 0.92, 0.88, 0.86, 0.84, 0.86, 0.92, 0.88, 0.85, 0.87, 0.42 |
| Stop reason | maxIterationsReached |
| Convergence mode | off |
| Corpus repositories | 22 pinned |
| State authority | append-only ledger via `append-mode-event.cjs`; reducer after every iteration |
