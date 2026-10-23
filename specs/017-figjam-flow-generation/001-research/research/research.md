# Research Synthesis: Product Owner FigJam flow generation

Final synthesis of a 28-iteration deep-research run: 20 DeepSeek V4.1 Flash iterations and 8 GPT-6 Luna iterations. Written 2026-10-19 by a fresh Opus 5.5 agent from the iteration files, the two lineage syntheses, the merged registry and the cited source files themselves. Every claim carries `[CONFIRMED: file:line]` when a source line, a command run or a file listing states it, or `[INFERRED: ...]` with what would confirm it.

---

## 1. Executive Summary

**The write path is wider than either lineage found.** Both lineages concluded that the registered Figma MCP is read-only and that FigJam writes go only through the `figma-ds-cli` `fj` verbs. The first half holds: the registered `figma` manual is the third-party Framelink server, and it does not drive Figma Desktop [CONFIRMED: mcp-wiring.md:35, :112]. The second half does not hold for this repo. On 2026-08-29 an earlier packet built a real FigJam board, 5 Mermaid diagrams with 42 ids and 82 connectors, through the hosted official Figma MCP's `generate_diagram` tool [CONFIRMED: NEF/plan.md:24, :115, NEF/tasks.md:50, NEF/implementation-summary.md:73, :124]. Both lineages read only the `mcp-figma` skill, which declares the official Figma MCP out of scope [CONFIRMED: mcp-wiring.md:152-159], so neither saw it.

**The `fj` route is now verified at help level.** `figma-ds-cli` 1.2.0 is installed on this machine, and its live help shows `fj shape --type` accepts `ROUNDED_RECTANGLE`, `RECTANGLE`, `ELLIPSE` and `DIAMOND`, while `fj connect` takes only `<startId> <endId>` and a page option, with no label and no style flag [CONFIRMED: `figma-ds-cli --version` and `figma-ds-cli fj <verb> --help`, run read-only in this session]. A flowchart drawn through `fj` therefore cannot carry a label on any connector, so the "label every exit" rule needs a separate text node per edge, placed by hand.

**Recommended shape of the upgrade.** Product Owner becomes a two-packet hub. `sk-product-owner` stays the default workflow packet and gains a Flow Mode that owns intake, source classification, the flowchart rules and the FigJam-only delivery. A byte-identical vendored copy of `mcp-figma` becomes a tool packet [INFERRED: the Moneybird checker types every non-default packet as a tool, check-route-table.py:903, confirm by porting the check]. The flow model is Mermaid flowchart text, checked before any write with the existing `mermaid_extract.py`, then written by `generate_diagram` as the primary route and by `fj` as the Desktop fallback [INFERRED: confirm in phase 002]. Sync back to `.skilled` runs through one PO-owned script with `status`, `pull` and `push`, backed by a manifest of upstream commit and file hashes and a three-way drift check [INFERRED: design, proven by phases 003 and 008].

**What runs first.** Phase `002-write-route-spike` settles the write route on a scratch board. Phase `003-vendored-figma-and-sync` is the first build phase and can start at once, because nothing in it depends on the route decision (Section 15).

---

## 2. Research Objective and Scope

The parent packet asks Product Owner to turn screenshots, Figma flows and product docs into FigJam flows, with FigJam as the only output, an embedded duplicate of the figma skill, a Claude Code plugin like Media Editor, a parent hub like Moneybird Accountant and a low-effort sync of skill and plugin optimizations back to `.skilled` [CONFIRMED: spec.md (parent):64-67, :77-83]. HTML and SVG output are out of scope, and the shared skill changes only through the sync path [CONFIRMED: spec.md (parent):82-83].

The research phase covers capability, input handling, rule transfer, embedding, plugin form, sync, hub conversion, precedent lessons and risks, and it excludes edits to Product Owner, `.skilled` or any skill [CONFIRMED: 001/spec.md:74-83]. The two questions the phase spec leaves to research are "Which Figma MCP route (hosted, desktop, or both) can write to FigJam?" and "Should the plugin carry the figma skill or call the embedded copy?" [CONFIRMED: 001/spec.md:182-183]. Section 4 answers the first and Section 9 the second.

The two repositories are real and separate. Product Owner is its own git root with a GitHub origin and an MIT licence [CONFIRMED: `git rev-parse` in `AI Systems/Product Owner`, `AI Systems/Product Owner/LICENSE:1`]. `.skilled` is a symlink to `Code_Environment/Public/.skilled`, whose git root is `Code_Environment/Public` [CONFIRMED: `ls -la .skilled`, `git rev-parse` in that folder].

---

## 3. Evidence and Boundaries

### Inputs read

- All 20 DeepSeek iteration files and all 8 Luna iteration files, both lineage `research.md` files, `findings-registry.json`, `fanout-attribution.md`, `resource-map.md`, the parent spec, the research phase spec and the staging `goal.md` and `acceptance-criteria.md`
- The merged registry records 28 iterations, 161 key findings, 60 ruled-out directions, 9 resolved questions and 1 open question, with a convergence score of 0.485 [CONFIRMED: findings-registry.json `metrics`]
- DeepSeek ran on `cli-pi` with `deepseek-v4.1-flash`, Luna on `cli-codex` with `gpt-6-luna` [CONFIRMED: fanout-attribution.md:7-8]

### What this synthesis ran

- Opened 164 cited file:line locations across the two lineages (tally in the Appendix)
- Ran `figma-ds-cli --version` (1.2.0) and `figma-ds-cli fj --help` plus `fj shape|connect|sticky|nodes|info --help`. Help output only, no connection, no board touched
- Read one screenshot from the Change Location flow with the Read tool
- Ran `mermaid_extract.py --json` on a 7-node Mermaid sample written to the session scratchpad, then deleted the sample
- Wrote nothing except this file. `git status` at the end matched the start

### What was not run

- No FigJam board was created, read or changed by this synthesis, and no MCP tool discovery ran against the hosted Figma server, because it is not configured in this session [CONFIRMED: no `mcp.figma.com` entry in `~/.claude.json`, no Figma plugin under `~/.claude/plugins`]
- No `fj` write verb ran, so the creation id return and connector attach behaviour stay unverified

### Short names used for cited paths

| Short name | Path from the `AI Systems` repo root |
|---|---|
| `tool-surface.md`, `figma-cli-reference.md`, `mcp-wiring.md` | `.skilled/skills/mcp-tooling/mcp-figma/references/` |
| `mcp-figma/SKILL.md`, `mcp-figma/README.md`, `mcp-figma/scripts/doctor.sh` | `.skilled/skills/mcp-tooling/mcp-figma/` |
| `mcp-tooling/mode-registry.json` | `.skilled/skills/mcp-tooling/mode-registry.json` |
| `type-flowchart.md` | `.skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md` |
| `sk-design-diagram/SKILL.md`, `mermaid_extract.py`, `validate-flowchart.sh` | `.skilled/skills/sk-design/sk-design-diagram/` (scripts under `scripts/`) |
| `sk-vision/SKILL.md` | `.skilled/skills/sk-vision/SKILL.md` |
| `PO/AGENTS.md`, `PO/SYNC.md`, `PO/LICENSE` | `AI Systems/Product Owner/` |
| `PO/SKILL.md`, `doc-mode.md`, `leaf-manifest.config.json`, `PO/graph-metadata.json` | `AI Systems/Product Owner/sk-product-owner/` (`doc-mode.md` under `references/`) |
| `kernel` | `AI Systems/Product Owner/claude project/Custom Instructions.md` |
| `gates/README.md`, `parity/README.md`, `differential.py`, `router fixtures` | `AI Systems/Product Owner/benchmark/` (`gates/`, `parity/`, `router/`) |
| `systems.py`, `validate_parity.py` | `AI Systems/z*Claude Project Sync Loop/` (shell glob, see the note below) |
| `ME/README.md`, `plugin.json`, `marketplace.json` | `AI Systems/Media Editor/runtime/claude-plugin/` (manifests under `.claude-plugin/`) |
| `build-plugin.ts`, `build-plugin.vitest.ts` | `AI Systems/Media Editor/runtime/scripts/`, `runtime/tests/packaging/` |
| `ME-008/` | `AI Systems/Media Editor/specs/003-media-editor-extension/008-claude-code-plugin/` |
| `ME-005/spec.md` | `AI Systems/Media Editor/specs/005-media-editor-cli-runtime/spec.md` |
| `ME changelog v0.8.0.0` | `AI Systems/Media Editor/sk-media-editor/changelog/v0.8.0.0.md` |
| `MB/hub-router.json`, `MB/mode-registry.json`, `MB/SKILL.md`, `MB/AGENTS.md` | `AI Systems/Moneybird Accountant/` |
| `check-route-table.py` | `AI Systems/Moneybird Accountant/sk-moneybird-accountant/scripts/check-route-table.py` |
| `MB-017/`, `MB-018/`, `MB-019/` | `AI Systems/Moneybird Accountant/specs/013-skill-routing-implementation/017-parent-hub-and-router/`, `018-hub-scoring-and-contract-gaps/`, `019-review-findings-fixes/` |
| `NEF/` | `specs/017-notification-event-flow-map/` |
| `spec.md (parent)`, `001/spec.md` | `AI Systems/Product Owner/specs/017-figjam-flow-generation/spec.md` and `001-research/spec.md` |
| `DS-n`, `L-n` | `specs/z-staging-po-017-research/research/lineages/deepseek/iterations/iteration-0nn.md`, `.../luna/iterations/iteration-00n.md` |

Two folder names contain a long dash that this file does not reproduce, so they appear as shell globs that resolve to the real folders: `AI Systems/z*Claude Project Sync Loop/` and `Product Context/a*Screenshots/`.

### Citation audit outcome

Three citations failed and five claims were downgraded. None of the top recommendations rests on a failed citation.

| Claim (lineage) | Problem | Treatment here |
|---|---|---|
| `sk-vision` at `.skilled/sk-vision/SKILL.md` (DS-2) | Wrong path, `resource-map.md` lists it MISSING. The file is `.skilled/skills/sk-vision/SKILL.md`, and its content matches | Path corrected |
| Fixture runners named as pre-upload checks at `PO/SYNC.md:27` (DS-15) | Line 27 is an unrelated 2026-09-11 review note | Dropped. `gates/README.md:21` carries the runner list instead |
| "38 declared pairs" at `gates/README.md:22` (DS-16) | The README says 38, but `systems.py` now declares 37 `pairs` for `product-owner` | Downgraded to "37 today" [CONFIRMED: loading `systems.py`] |
| Only six FigJam verbs, so no image or section can reach a board (DS-3, DS-5) | True of the `fj` group only. The general surface has `create image` and `section create` [CONFIRMED: tool-surface.md:97, :130], and whether they act on a FigJam page is unknown | Downgraded to INFERRED |
| Screenshot folders hold "ordered step captures" (DS-2) | Filenames carry no order, and Change Campaign uses `Flows/<platform>/` where Change Location uses `Flow/<platform>/` | Corrected in Section 6 |
| `sk-vision` is the only pixel reader (DS-2) | True for text-only models. Claude reads PNG files natively | Corrected in Section 6 |
| `fj shape` kinds and `fj connect` labels unknown (DS-7, L-3) | Closed by live help | Now CONFIRMED |
| FigJam writes only through `fj` (both lineages) | Contradicted by the `NEF/` record | Corrected in Section 4 |

Four more citations pointed one or two lines away from the stated text (for example `figma-cli-reference.md:372` for the drift gap, which sits at :369-370 and :373). Those claims hold at the nearby line and are cited at the correct line below.

---

## 4. FigJam Write Path

### What can and cannot write FigJam nodes

| Route | Writes FigJam? | Needs | Evidence |
|---|---|---|---|
| Framelink `figma` manual through Code Mode, the MCP registered in this workspace | No. Two tools: file or node design data and referenced image downloads | `figma_FIGMA_API_KEY` in `.env`, this workspace's Code Mode | [CONFIRMED: mcp-wiring.md:35, :80, :112] |
| Hosted official Figma MCP (`https://mcp.figma.com/mcp`), `generate_diagram` | Yes. Mermaid text in, a FigJam diagram out, into one shared `fileKey` | A Figma account with OAuth and a chosen plan | [CONFIRMED: mcp-wiring.md:154, NEF/tasks.md:50, NEF/implementation-summary.md:73, :109] |
| Desktop-local official Dev Mode MCP (`http://127.0.0.1:3845/mcp`) | Unknown | Figma Desktop session | [CONFIRMED: exists per mcp-wiring.md:154] [INFERRED: write ability, confirm by tool discovery in phase 002] |
| `figma-ds-cli fj sticky|shape|text|connect|move|update` | Yes, node by node, no connector labels | Figma Desktop open with a FigJam file, the FigCli plugin bridge or the gated yolo patch, a healthy daemon on `127.0.0.1:3456`, Node 18+, macOS, the 1.2.0 repo build | [CONFIRMED: tool-surface.md:150, figma-cli-reference.md:57, :82-84, :100, :120, live `fj --help`] |
| `figma-ds-cli fj eval` | Yes, anything the Plugin API allows | Same as `fj` | Omitted from the default path by policy [CONFIRMED: tool-surface.md:191, :235-240] |

Settled:

- The registered MCP is read-only for FigJam purposes [CONFIRMED: mcp-wiring.md:35]
- Writes do not go only through `fj`. The hosted Figma MCP wrote a 5-diagram board here, verified by an in-file audit (42 of 42 ids, 0 of 82 connectors broken) and a screenshot [CONFIRMED: NEF/implementation-summary.md:121, :124]. This synthesis read that record, not the board itself
- The `fj` route has never written a FigJam node in this repo. Its help surface is now confirmed live, and `figma-ds-cli` 1.2.0 sits at `/opt/homebrew/bin` with Figma Desktop installed [CONFIRMED: `command -v`, `figma-ds-cli --version`, `/Applications/Figma.app`]
- The hosted route has two proven limits. Moving generator-created nodes through the API left 42 connectors stretched, and reassigning endpoints did not force a reroute, so the board keeps the generator's own layout [CONFIRMED: NEF/implementation-summary.md:166]. Mermaid labels allow no line breaks or markup [CONFIRMED: NEF/implementation-summary.md:168]

### Claude Code versus a claude.ai Project

| Runtime | `fj` route | Hosted `generate_diagram` route | Evidence |
|---|---|---|---|
| Claude Code on the operator's Mac | Works when Desktop is open, the bridge plugin runs and Bash is allowed | Works when a Figma MCP connection is present in the session | [CONFIRMED: README.md:26 for `fj` needs] [INFERRED: the NEF run was a Claude Code session, judged from its `claude.ai/code/artifact` link at NEF/implementation-summary.md:72, confirm the connection method in phase 002] |
| claude.ai Project | Impossible. A Project cannot run the CLI runtime or touch local files | Possible only through a claude.ai Figma connector that is enabled and exposes `generate_diagram` | [CONFIRMED: kernel:2] [INFERRED: connector tool list, confirm by discovery in a Project in phase 002] |
| Cowork | Unknown | Unknown | Media Editor reports Cowork does not install a plugin with a `bin/` folder [CONFIRMED: ME/README.md:15] |

The kernel already handles one connector-conditional action. It reaches ClickUp "only through the claude.ai ClickUp connector when it is present" and offers publishing only when that connector exists [CONFIRMED: kernel:2, :279]. A Figma connector would follow the same pattern. Without one, the Project can build and check the flow model but cannot deliver a board, and it must say so instead of rendering a Mermaid or Canvas diagram as a substitute, because that would be a second output format [INFERRED: from spec.md (parent):79-82 and kernel:265, operator decision Q5].

---

## 5. Limits and Safety Guarantees

### `fj` limits (live help, 1.2.0)

- Four shape types: `ROUNDED_RECTANGLE` (default), `RECTANGLE`, `ELLIPSE`, `DIAMOND`, each with `-x`, `-y`, `-w`, `-h` and `-p <page>` [CONFIRMED: `fj shape --help`]
- `fj connect <startId> <endId>` has no label, colour or routing option [CONFIRMED: `fj connect --help`]
- `fj sticky` takes `-c <hex>` for colour, `fj nodes` lists 20 nodes unless `-l` raises it [CONFIRMED: `fj sticky --help`, `fj nodes --help`]
- No layout verb, so every position is computed by the caller [CONFIRMED: `fj --help` command list]
- Whether a create verb prints the new node id is unknown, so connector steps may need `fj nodes -l` read-back between writes [INFERRED: confirm with one write on a scratch board in phase 002]
- The daemon idles out after 60 minutes and does not survive a reboot. The yolo connect patches `app.asar` and breaks on Figma updates. macOS is the only supported baseline [CONFIRMED: figma-cli-reference.md:125, :108, :83]
- npm publishes only 1.0.0, which has no `fj` group at all. The full surface comes from the silships repo build [CONFIRMED: figma-cli-reference.md:55-57]

### Hosted route limits

- Generator-owned layout, with node moves breaking connector routing [CONFIRMED: NEF/implementation-summary.md:166]
- Labels without line breaks or markup, so detail moves onto edges [CONFIRMED: NEF/implementation-summary.md:81, :168]
- A plan must be chosen. The earlier run published to the Barter B.V. plan because the other writable plan belonged to an unrelated client [CONFIRMED: NEF/implementation-summary.md:109]
- Tool names beyond `generate_diagram`, input schema, auth scope and rate limits are not recorded in this repo [INFERRED: confirm by tool discovery in phase 002]

### Guarantees to keep

- Every `fj` write is MUTATING and needs a stated effect, an explicit target, a one-line rollback and confirmation [CONFIRMED: tool-surface.md:181-184]
- `fj delete` and `fj eval` stay off the default path, reachable only on an explicit request with the destructive or arbitrary ceremony [CONFIRMED: tool-surface.md:186-191]
- Rollback order is duplicate first, then Undo in session, then version history. For `fj delete` the rollback is Undo on the page or a page duplicate before large clears [CONFIRMED: tool-surface.md:222, :229]
- The daemon token is never shown, and the daemon stays on `127.0.0.1` [CONFIRMED: tool-surface.md:255]
- The same confirm-target-rollback gate applies to `generate_diagram`, since it creates content in a shared Figma plan. The earlier run's rollback was "clear the FigJam page, nothing imports it" [CONFIRMED: NEF/plan.md:126] [INFERRED: that the gate should bind the hosted route too, operator decision Q6]

---

## 6. Input Handling by Type

### Screenshots

- The corpus holds 341 PNG files under `Product Context/a*Screenshots/` [CONFIRMED: `find` count]
- Change Location keeps 3 desktop and 4 mobile step images under `Flow/<platform>/` and 6 component states under `Components/<platform>/`. Change Campaign uses `Flows/<platform>/` for the same role, so intake must accept both folder names [CONFIRMED: directory listing]
- Filenames name the screen and the trigger (`Dashboard - Click_ Location Selector`, `Sheet - Menu - Locations - Click_ Location`, `Dashboard - Location Change - Success`) but carry no step number, so step order is inferred from the trigger grammar and confirmed with the user when two orders fit [CONFIRMED: listing] [INFERRED: the ordering rule, confirm against the 2 existing flows in phase 005]
- Claude reads PNG files directly. Reading `Sheet - Menu - Locations - Click_ Location.png` showed the sheet title "Locations (528)", the search field, the address list and a hand cursor on "Gedempt Hamerkanaal 40", which identifies the click target the filename leaves out [CONFIRMED: Read tool in this session]
- `sk-vision` gives OCR and detection to text-only models through a local Moondream runtime, is idle by default and needs a one-time Bun build [CONFIRMED: sk-vision/SKILL.md:3, :12, :14]. Flow Mode does not need it on Claude runtimes [INFERRED: holds while Product Owner runs on Claude models]
- The screenshots live in the AI Systems repo, outside the public Product Owner repo. Flow Mode reads them in place and never copies them into Product Owner [INFERRED: from the public MIT repo facts in Section 2]

### Figma flows

- A Figma URL yields `fileKey` and `nodeId` [CONFIRMED: mcp-wiring.md:130-133]
- Three read routes exist: Framelink in this workspace only, the hosted MCP's read tools or the CLI design verbs `node tree`, `inspect` and `export screenshot` that need the design file open in Desktop [CONFIRMED: mcp-wiring.md:112, tool-surface.md:108, :112, :137] [INFERRED: the hosted read tool names, confirm in phase 002]
- Reads must stay node-scoped, because responses are token-heavy and `extract` splits output above roughly 50k tokens [CONFIRMED: mcp-wiring.md:148, tool-surface.md:203]
- No documented verb copies a design frame into a FigJam board, so frame content is retyped into the flow model [INFERRED: from the absence of such a row in tool-surface.md:63-163]

### Product docs

- Flow Mode reuses Doc Mode's five source classes, current behaviour, approved direction, proposal, retired material and unknown [CONFIRMED: doc-mode.md:141-149]
- It reuses the authority order and the conflict gate, which stops composition and asks one consolidated question when no source wins [CONFIRMED: doc-mode.md:166-186]
- A proposal or unknown step is drawn with a visible status label or left out, and never drawn as current behaviour [INFERRED: Doc Mode treatment applied to nodes, confirm with a doc-sourced fixture in phase 005]
- The earlier board's method, asserting every causal edge from both ends and treating a mismatch as a defect, found 11 catalog defects and suits doc-sourced flows [CONFIRMED: NEF/implementation-summary.md:91]

### Mixed sources

A request that mixes inputs stays in the Product Owner workflow packet until sources are classified and the model and target are ready, and only then hands board operations to the tool packet [INFERRED: from MB/SKILL.md:32-35 and PO/SKILL.md:44, as L-6 argued].

---

## 7. Recommended End-to-End Architecture

1. **Route.** An explicit Flow command or explicit FigJam output wording selects Flow Mode in `sk-product-owner`. The bare word "figma" keeps routing UI refinement to Task Mode [CONFIRMED: PO/SKILL.md:97, router fixtures:1643] [INFERRED: the new rows, phase 004]
2. **Intake.** Per input type, as in Section 6
3. **Model.** The flow model is a Mermaid `flowchart TD` block plus a provenance table that maps each node id to its source file and source class. The model is working data, never a deliverable [INFERRED: from spec.md (parent):79, :82]
4. **Check.** A pre-write check parses the Mermaid with `mermaid_extract.py`, which already returns node shapes (`stadium`, `rect`, `rhombus`, `circle`), per-node out-degree, labelled-edge counts, entry points, terminals and budget flags [CONFIRMED: run on a 7-node sample in this session]. It fails a decision with more than 3 exits, an unlabelled decision exit, an unknown shape or a diagram over 9 nodes [CONFIRMED: rules at type-flowchart.md:23, :25, sk-design-diagram/SKILL.md:264] [INFERRED: the check itself, built in phase 005]
5. **Gate.** State the target plan and file with the effect and the rollback, then wait for confirmation [CONFIRMED: tool-surface.md:181]
6. **Write.** Primary: `generate_diagram` with one diagram per flow. Fallback: `fj shape` per node, `fj connect` per edge, `fj text` for each edge label, with ids read back between steps [INFERRED: route choice is operator decision Q1 after phase 002]
7. **Read back.** Compare node and connector counts and every node label against the model, and check connectors for stretching on a screenshot, as the earlier run did [CONFIRMED: NEF/implementation-summary.md:121, :124]
8. **Reply.** The board URL takes the place of the export path, and the verification line reports the read-back counts [INFERRED: operator decision Q3]

Responsibility split: Flow Mode owns steps 1 to 5, 7 and 8. The vendored `mcp-figma` tool packet owns `fj` mechanics and gating. The hosted route's procedure lives in Flow Mode until upstream `mcp-figma` documents it [INFERRED: operator decision Q2].

---

## 8. Flowchart Rules to Carry into FigJam

| `sk-design-diagram` rule | Source | Mermaid for `generate_diagram` | `fj` fallback | Verdict |
|---|---|---|---|---|
| Oval start and end | type-flowchart.md:21 | Stadium `([...])` | `--type ELLIPSE` | Carry. How the generator maps stadium to a FigJam shape is [INFERRED: phase 002] |
| Rectangle step | type-flowchart.md:22 | `[...]` | `--type RECTANGLE` | Carry |
| Diamond decision, at most 3 exits | type-flowchart.md:23, :31 | `{...}`, checked by out-degree | `--type DIAMOND` | Carry, enforced before the write |
| Small ink dot for a merge | type-flowchart.md:24 | `((.))` circle node | Small `ELLIPSE` | Carry as a circle node [INFERRED: rendering, phase 002] |
| Flow runs top to bottom | type-flowchart.md:25 | `flowchart TD` | Computed `-x`/`-y` | Carry |
| Yes to the right, No below | type-flowchart.md:25 | Not controllable in generator layout | Placement | Drop as a convention, keep the labels [INFERRED] |
| Label every outgoing arrow | type-flowchart.md:25, :32 | `-->|label|`, checked | One `fj text` node per edge, since `fj connect` has no label flag | Carry. Hard on the `fj` route [CONFIRMED: live `fj connect --help`] |
| Shape carries type, never colour | type-flowchart.md:20, :30 | No `classDef` per type | No colour per type | Carry |
| Coral on the happy path or one decision only, accent on 1 or 2 focal elements | type-flowchart.md:26, sk-design-diagram/SKILL.md:268 | One `linkStyle` or `classDef` | Sticky colour only, no connector colour | Carry, rendering [INFERRED: phase 002] |
| Arc jump at crossings | type-flowchart.md:27 | None | None | Drop. Split the diagram instead |
| One idea per node, density 4/10, split above 9 nodes | sk-design-diagram/SKILL.md:260-264 | Checked count | Same | Carry |
| Five connector rules: orthogonal, label gap, no overlap, fanned attach points, no routing behind boxes | sk-design-diagram/SKILL.md:291-295 | Owned by the generator | Owned by FigJam | Check after the write by screenshot, as NEF did [CONFIRMED: NEF/implementation-summary.md:124] |
| Never reproduce a Mermaid renderer layout | sk-design-diagram/SKILL.md:279 | Conflicts with the hosted route | Not affected | Waive for FigJam. Moving generator nodes breaks routing [CONFIRMED: NEF/implementation-summary.md:166] |
| 4px grid, accessible SVG contract, HTML wrapper, corpus check, ASCII validator | sk-design-diagram/SKILL.md:241-248, :266, :269-272 | Not applicable | Not applicable | Do not carry. They bind HTML/SVG and ASCII output, both excluded [CONFIRMED: spec.md (parent):82] |

The ASCII validator's one machine check, failing when decision words appear without YES/NO labels, becomes the "unlabelled decision exit" rule in the pre-write check [CONFIRMED: validate-flowchart.sh:81-84]. The earlier board coloured three categories (critical, D14 handoffs, terminal consequences) [CONFIRMED: NEF/implementation-summary.md:81], which sits at the edge of the "accent on 1 or 2 focal elements" rule, so Flow Mode should hold to one accent [INFERRED].

---

## 9. Embedding mcp-figma and the Claude Code Plugin

### The upstream package

- `.skilled/skills/mcp-tooling/mcp-figma/` holds 58 files (524K) and no symlinks [CONFIRMED: `find`, `du`]
- It is a packet of the shared `mcp-tooling` hub. Its registry row (packetKind `transport`, allowed `Read, Bash, Grep, Glob, mcp__code_mode__call_tool_chain`, forbidden `Write, Edit, Task`) lives in the hub's `mode-registry.json`, and the folder carries no `graph-metadata.json` or leaf manifest of its own [CONFIRMED: mcp-tooling/mode-registry.json `mcp-figma` entry, no `*.json` in the folder]
- The last commit touching it in `Code_Environment/Public` is `293caa90a8` on 2026-10-12 [CONFIRMED: `git log -1` there]
- Six relative links leave the folder and break inside Product Owner: `mcp-wiring.md:41` and `:170` and `troubleshooting.md:477` to `mcp-code-mode` and `mcp-chrome-devtools`, `SKILL.md:115` to `sk-doc`, `feature-catalog.md:71` to an `AGENTS.md` five levels up and `README.md:203` to `README.txt` [CONFIRMED: grep of `](../../` links]
- Its optional MCP path needs this workspace's Code Mode and `.utcp_config.json`, and its design authoring pairs with `sk-design-md-generator` [CONFIRMED: mcp-figma/SKILL.md:5, :42, mcp-wiring.md:25]. Neither exists in a Product Owner clone, and neither is needed for FigJam flows [INFERRED]

### Placement and tooling

- Place the copy at `AI Systems/Product Owner/mcp-figma/`, a root-level packet beside `sk-product-owner/`, as Moneybird places `cli-moneybird/` [CONFIRMED: MB/SKILL.md:44-53]
- Keep it byte-identical. Its `SKILL.md` carries `INTENT_SIGNALS` and `RESOURCE_MAP` [CONFIRMED: mcp-figma/SKILL.md:145, :154], which Moneybird's checker reports as an embedded router [CONFIRMED: check-route-table.py:67-72, :928-930]. Product Owner's hub check therefore exempts declared vendored packets and points their `router` field at the vendored `SKILL.md` [INFERRED: design choice, the alternative is splitting upstream, see Eliminated Alternatives]
- Product Owner's skill declares no Bash [CONFIRMED: PO/SKILL.md:4], while `mcp-figma` needs it [CONFIRMED: mcp-figma/SKILL.md:5]. The hub `SKILL.md` must allow Bash for the tool packet to run [INFERRED: confirm how Claude Code applies `allowed-tools` across a hub and its packets in phase 004]
- Placing the copy outside `sk-product-owner/` keeps its 58 files out of the parity gate's source inventory, which reads only `skill_dir` [CONFIRMED: validate_parity.py:471, systems.py `skill_dir` = `sk-product-owner`] [INFERRED: confirm with `run_parity.sh` after placement]

### The plugin

The phase spec asks whether the plugin carries the figma skill or calls the embedded copy. Answer: the plugin carries a build-time copy of the embedded copy, untracked and hash-checked, so exactly one tracked copy exists in Product Owner [INFERRED: from the Media Editor pattern at ME/README.md:78-83].

- Copy Media Editor's shell: a `plugin.json` with name, version, description, author, licence and keywords, plus a one-plugin local marketplace with source `./` [CONFIRMED: plugin.json, marketplace.json]
- The build replaces the whole `skills/` folder, dereferences links, hashes every shipped file against its source, refuses a copy that differs, refuses any link and refuses a `plugin.json` that registers an MCP server [CONFIRMED: build-plugin.ts:277-287, :372-377, :408-417]
- Ship no `bin/` folder unless the `fj` route proves it needs a shim. `figma-ds-cli` is already on PATH where the route works, and Media Editor's README says a `bin/` folder is what keeps claude.ai and Cowork from installing a plugin [CONFIRMED: ME/README.md:15] [INFERRED: that a bin-less plugin installs there, confirm in phase 006]
- Do not register the hosted Figma MCP in `plugin.json`. Auth and plan choice belong to the user's own Figma connection [INFERRED: from NEF/implementation-summary.md:109 and the refusal at build-plugin.ts:372]
- Claude Code reads plugin skills as `skills/<name>/SKILL.md` [INFERRED: from ME/README.md:80, confirm with a `--plugin-dir` session]. A plugin session never loads Product Owner's `AGENTS.md`, so the hub `SKILL.md` must carry the bootstrap it needs [INFERRED: confirm in phase 006]

---

## 10. Sync Path Recommendation

### Three hops, three owners

| Hop | Direction | Mechanism | Drift detection |
|---|---|---|---|
| 1. `.skilled` `mcp-figma` and Product Owner's tracked copy | Both ways, across two repos | One script plus a manifest | Three-way: local hashes against the manifest, upstream commits since the base, uncommitted upstream edits |
| 2. Tracked copy to the plugin's `skills/` | One way, build time | Media Editor build pattern | Hash parity, the build fails on any difference [CONFIRMED: build-plugin.ts:411-417] |
| 3. Skill sources to the Claude Project | One way, by hand | The manual parity method | Read-only commit-timestamp drift list, dated review sentences [CONFIRMED: PO/SYNC.md:8-15] |

The vendored `mcp-figma` copy is not mirrored into the Project, because a Project cannot run any of it [CONFIRMED: kernel:2]. Flow Mode's Project-applicable rules are mirrored through hop 3 [INFERRED: phase 007].

### Hop 1 design

- **Manifest** `AI Systems/Product Owner/vendor.json`, a list so a second vendored file can join later. Each entry holds a name, an upstream resolver (environment variable, else the realpath of the workspace `.skilled`), the upstream path, the base commit and a sha256 per file [INFERRED]
- **Script** `AI Systems/Product Owner/scripts/vendor-sync.py`, Python with no dependencies, run as `python3 -I` [INFERRED]
  - `status` classifies each entry as clean, local-ahead, upstream-ahead or diverged and flags links and unexpected files. It exits 0 when clean, 1 on drift and 2 on a configuration error
  - `pull` refuses unless the entry is clean or upstream-ahead, refuses uncommitted upstream edits, copies the committed upstream blobs byte for byte and rewrites the manifest
  - `push` refuses unless the entry is local-ahead, builds a patch from the base to the local copy, runs `git apply --check` in `Code_Environment/Public` and then applies it to that working tree. It never commits or pushes, and it prints the commit command for that repo and the follow-up `pull`
- **The one-command flow.** An optimization made in Product Owner goes upstream with `vendor-sync.py push`. The operator reviews and commits in `Code_Environment/Public`, then `vendor-sync.py pull` re-baselines. The upstream commit stays a human step, because commits and pushes need the operator's go-ahead [CONFIRMED: spec.md (parent):84, root AGENTS.md §6]
- **Two drift levels.** A public clone on GitHub has no `Code_Environment` beside it, so the hash check (local copy against the manifest) runs in `run_gates.sh` everywhere, while the upstream check runs only on the operator's machine [INFERRED]. A local edit turns the gate red, the same choice Product Owner made for its four vendored rule cards [CONFIRMED: PO/SYNC.md:44]
- **No links.** Never create a `.skilled` link inside Product Owner. A link that climbs out of the repo resolves to nothing in a clone [CONFIRMED: PO/SYNC.md:44], and a temporary `.skilled` link once made the Commit-Id hook refuse a Moneybird commit [CONFIRMED: MB-018/implementation-summary.md:78]

### Plugin optimizations

`.skilled` holds no Claude Code plugin. `.skilled/plugins` is a link to the OpenCode plugin folder [CONFIRMED: `ls -la .skilled/plugins`]. A plugin optimization can only travel upstream when it lands inside the vendored skill tree, for example in `mcp-figma/scripts/doctor.sh`, which is already a report-only preflight [CONFIRMED: mcp-figma/scripts/doctor.sh:2-3]. The plugin shell itself stays Product Owner-only unless the operator wants a shared home for it [INFERRED: operator decision Q9].

---

## 11. Parent Hub and Routing Design

### Files

| File | Role | Precedent |
|---|---|---|
| `AI Systems/Product Owner/SKILL.md` | Routing-only hub, links each packet router | [CONFIRMED: MB/SKILL.md:10, :16-20] |
| `hub-router.json` | `defaultMode` = the Product Owner workflow, whole-word signals for the tool packet | [CONFIRMED: MB/hub-router.json:2-12] |
| `mode-registry.json` | Two rows: `sk-product-owner` (`workflow`, default) and `mcp-figma` (`tool`, vendored) | [CONFIRMED: MB/mode-registry.json:4-27] |
| `sk-product-owner/ROUTER.md` | The current `SKILL.md` Section 2, with a pointer left behind | [CONFIRMED: MB-017/implementation-summary.md:54] |
| `PO/AGENTS.md` | STEP 1 reads the hub first, and the Command Registry, Routing Compatibility, Document Loading Order and Full DAG gain the Flow route | [CONFIRMED: PO/AGENTS.md:159, :186, :200, :230, MB/AGENTS.md:36, :44] |

### Why Flow Mode sits inside `sk-product-owner`

DS-8 and DS-15 proposed a separate FigJam packet with its own router. L-6 and L-8 proposed keeping flow policy in the default workflow packet. Three facts settle it for L-6:

- Moneybird's checker types the default packet as `workflow` and every other packet as `tool` [CONFIRMED: check-route-table.py:201, :903-905]
- The Sync Loop declares one `skill_dir` per system, so a second workflow packet would sit outside parity [CONFIRMED: systems.py `skill_dir`, validate_parity.py:471]
- Upstream already classes `mcp-figma` as a transport whose design judgement is handed to another skill [CONFIRMED: mcp-tooling/mode-registry.json `transport-axis`]

### Routing rules

- Explicit Flow command or explicit FigJam output wording routes to Flow Mode. No `$f` or `$flow` token exists today [CONFIRMED: grep of PO/AGENTS.md and PO/SKILL.md] [INFERRED: the name is operator decision Q4]
- "figma" on its own stays a UI refinement signal with its 0.80 override, and the fixture "figma says the padding is 8px off on the empty state" stays Task [CONFIRMED: PO/SKILL.md:97, router fixtures:1643]
- A request naming only a `figma-ds-cli` operation starts in the tool packet, whole words only [CONFIRMED: precedent at MB/SKILL.md:33]
- A refusal stays in the workflow packet [CONFIRMED: precedent at MB/SKILL.md:35]
- Negated or quoted Figma mentions never trigger a board write [INFERRED: from MB-018/implementation-summary.md:78, :90 and MB-019/spec.md:68]

### Blast radius

- `differential.py` reads the semantic topic table out of `sk-product-owner/SKILL.md`, so moving Section 2 to `ROUTER.md` breaks it until it is repointed [CONFIRMED: differential.py:78, :167-175]
- The router section says the oracle and fixtures in `benchmark/router/` must never drift from it [CONFIRMED: PO/SKILL.md:44]
- In Moneybird every routing reader had to move, roughly ten scripts with tests [CONFIRMED: MB-017/implementation-summary.md:54]
- The kernel carries its own copy of the router code since v0.21.0, so the Project side changes too [CONFIRMED: PO/SYNC.md:59]
- Moneybird is not declared in the Sync Loop, so Product Owner would be the first hub system the parity gate sees [CONFIRMED: `systems.py` keys list seven systems without Moneybird]

---

## 12. Media Editor: copy and avoid

### Copy

- The plugin shell: `plugin.json` with six fields and a one-plugin local marketplace [CONFIRMED: plugin.json, marketplace.json]
- Payload as untracked build output, with `skills/`, `bin/` and `server/` ignored by git [CONFIRMED: `AI Systems/Media Editor/runtime/.gitignore:9-11`]
- Whole-folder replacement of `skills/` on every build, so an old copy never ships beside a new one [CONFIRMED: build-plugin.ts:341-343, :409]
- Hash parity of the shipped copy, link dereferencing and the refusals for differing files, links and `mcpServers` [CONFIRMED: build-plugin.ts:277-287, :372-377, :382-388, :411-417]
- An exclusion list for folders a plugin need not ship (`feature-catalog`) [CONFIRMED: build-plugin.ts:226]
- A version equality check across package, plugin and server manifests [CONFIRMED: build-plugin.ts:363-369, :393-396]
- Verification by `claude plugin validate` and a live `--plugin-dir` session [CONFIRMED: ME-008/implementation-summary.md:149-153]
- A packaging test that the manifest registers no MCP server and that the built skill equals its source [CONFIRMED: build-plugin.vitest.ts:418-421, :436-440]

### Avoid

- Shipping a runtime the system does not own. Media Editor bundles its own server and ffmpeg [CONFIRMED: ME/README.md:11, :31], while `mcp-figma` drives an external CLI it says it does not vendor or redistribute [CONFIRMED: figma-cli-reference.md:384]
- Promising claude.ai or Cowork support from a `bin/` plugin [CONFIRMED: ME/README.md:15]

### Mistakes Media Editor already paid for

- **Node assumption.** The spike showed Claude Code supplies no Node for a bundle and does not fill its folder settings, so the manifest runs `node`. The Node 18 requirement was superseded by the 20.9.0 engines floor [CONFIRMED: ME-008/implementation-summary.md:55, ME-008/acceptance-criteria.md:63]
- **A safety rule that cut coverage.** "Any redirect fails" would have allowed installs on darwin-arm64 only, because all eight GitHub release URLs answer 302. It was amended the same day to one host-checked redirect [CONFIRMED: ME-008/decision-record.md:163, :177-179]
- **Development binary against shipped binary.** The suite ran against `ffmpeg-static` 6.0. With the shipped 9.0.2 swapped in, 45 tests failed [CONFIRMED: ME-008/implementation-summary.md:122]
- **A live-only defect.** ffmpeg 9.0.2 prints two flag characters per filter row, so ten filter-gated tools would have refused to run. Only the live plugin session found it [CONFIRMED: ME-008/implementation-summary.md:59]
- **The MCP-to-CLI move.** The phase 8 plugin ran an MCP server [CONFIRMED: ME-008/implementation-summary.md:150]. A later packet moved the plugin to a `bin` CLI with no `mcpServers`, because the skill reached its tools only through MCP and the folder name tied the runtime to one transport [CONFIRMED: ME-005/spec.md:60, :92, :143]
- **A rename across every surface.** The plugin copy path, the Project knowledge names and the re-upload and rebuild steps all moved in one release [CONFIRMED: ME changelog v0.8.0.0:83, :121]
- **Stale counts.** The dated summary says 39 tools while the current packaging test expects 40 [CONFIRMED: ME-008/implementation-summary.md:51, build-plugin.vitest.ts:432]. For Product Owner: record dated `fj --help` captures and never cite an old count as current [INFERRED]

---

## 13. Moneybird Accountant: copy and avoid

### Copy

- Two small registries and a routing-only hub `SKILL.md` [CONFIRMED: MB/hub-router.json:1-13, MB/mode-registry.json:1-30, MB/SKILL.md:10]
- Two-stage routing with one `ROUTER.md` per packet [CONFIRMED: MB/SKILL.md:30]
- The workflow packet as default, CLI packets on whole-word signals only, refusals kept in the workflow packet, one question when nothing fits [CONFIRMED: MB/SKILL.md:32-36]
- The hub checks: packet `SKILL.md` present, packet kind by default flag, name match, router path, router header lines, no embedded router, unregistered packet folders reported, `defaultMode` equal to the registry default, signals naming every mode [CONFIRMED: check-route-table.py:898-952]
- Hub gold rows replayed against the stage-one rules: 19 rows naming their expected packet chain [CONFIRMED: MB-018/implementation-summary.md:56, :103]
- Write-contract checks held per file instead of in aggregate [CONFIRMED: MB-018/implementation-summary.md:54]
- Mutants and a baseline diff as gates: 110 of 110 mutants killed, 0 changes over 167 earlier rows [CONFIRMED: MB-019/implementation-summary.md:105, :107]
- A token budget line for the default request: 11,734 of 12,000 tokens [CONFIRMED: MB-019/implementation-summary.md:123]

### Avoid

- Building the hub in place on the live tree. Moneybird built each phase in a scratch clone and applied one patch [CONFIRMED: MB-017/implementation-summary.md:74]
- Trusting a resolver as proof of model behaviour. The review states that the fixes are proven against the resolver, not against a live agent [CONFIRMED: MB-019 `scratch/verification/review-parent.md:98`]

### Mistakes Moneybird already paid for

- **One shared router.** A root `ROUTER.md` for all packets raised an accountant request from 9,635 to 16,664 tokens (about 73 percent), and the move was rebuilt as one router per packet [CONFIRMED: MB-017/implementation-summary.md:74]
- **Green before correct.** After the first green build a fresh reviewer found four P1s: an `AGENTS.md` read order that contradicted the hub, a write-contract check that lost a pointer line, four checks that passed with nothing to test and about 50 stale pointers to `SKILL.md` Section 2. A second reviewer found one more [CONFIRMED: MB-017/implementation-summary.md:74]
- **Prefix matching.** "Jortt clients" matched `jortt cli`, and a filing request naming `jortt-cli` handed off to both CLIs [CONFIRMED: MB-018/implementation-summary.md:78]
- **Raw-text negation.** The first filing fix read the raw text and dropped a valid invoice handoff that said "Don't submit anything" [CONFIRMED: MB-018/implementation-summary.md:78, :90]
- **Stage-one gaps.** Naming a CLI sent a migration request to the CLI packet alone, and a negated CLI name started that CLI [CONFIRMED: MB-019/spec.md:68]
- **A ceiling that stays.** After five review rounds the regex router still misses 46 of 741 reviewer prompts and 128 of 5,920 generated combinations [CONFIRMED: MB-019/implementation-summary.md:109, :122]
- **Metadata debt.** Nine phase folders lacked `description.json` and `graph-metadata.json` [CONFIRMED: MB-018/implementation-summary.md:58]
- **A temporary `.skilled` link.** It made the Commit-Id stamper treat the repo as covered, and the commit was refused [CONFIRMED: MB-018/implementation-summary.md:78]

---

## 14. Risk Register

| Risk | Severity | Reducible? | Control | Evidence |
|---|---|---|---|---|
| Hosted route schema, auth or plan behaviour differs from the 2026-08-29 run | High | Yes | Phase 002 discovery and one scratch write | [CONFIRMED: route exists, NEF/tasks.md:50] [INFERRED: drift] |
| Board lands in the wrong Figma plan | High | Yes | Name plan and file before every write | [CONFIRMED: NEF/implementation-summary.md:109] |
| Moving generator nodes breaks connectors | High | Yes | Never call `fj move` or layout edits on generator nodes, split diagrams instead | [CONFIRMED: NEF/implementation-summary.md:166] |
| `fj` edge labels need hand-placed text nodes | Medium | Partly | Prefer the hosted route for labelled flows | [CONFIRMED: live `fj connect --help`] |
| npm `figma-ds-cli` has no `fj` | Medium | Yes | Doctor check for 1.2.0 or later | [CONFIRMED: figma-cli-reference.md:57, mcp-figma/SKILL.md:18] |
| `fj delete`, `fj eval` or a hosted write on a real board | High | Yes | Gate, rollback, default-path omission | [CONFIRMED: tool-surface.md:181-191] |
| Public repo carries private Barter content or board links | High | Partly | No board URLs, screenshots or Barter flows in Product Owner examples | [CONFIRMED: PO/LICENSE:1, GitHub origin] |
| Private context leaves through an external prompt | Medium | Partly | Flow labels sent to Figma are Barter's own plan, review before any third-party model sees them | [CONFIRMED: 001/spec.md:145] |
| Hub conversion silently breaks routing readers | High | Yes | Repoint `differential.py`, baseline diff, fresh review | [CONFIRMED: differential.py:78, MB-017/implementation-summary.md:54, :74] |
| Token cost of the hub on the default path | Medium | Yes | Measure before and after | [CONFIRMED: MB-017/implementation-summary.md:74] |
| Vendored copy drifts or forks | Medium | Yes | `vendor-sync.py status` in `run_gates.sh` | [CONFIRMED: precedent at PO/SYNC.md:44] |
| Broken outbound links in the public copy | Low | Partly | Record them as known in the manifest | [CONFIRMED: grep of six links] |
| Parity gate sees new unpaired sources | Medium | Yes | Pair or `unmirrored_sources` entry per new file | [CONFIRMED: systems.py:19-21] |
| Rate limits and board size limits | Medium | No | Small diagrams, at most 9 nodes each | [INFERRED: nothing local documents either] |
| Desktop runtime fragility for `fj` | Medium | Partly | Safe connect, doctor preflight, never scheduled | [CONFIRMED: figma-cli-reference.md:108, :125] |

---

## 15. Later Phases

Seven child phases under `AI Systems/Product Owner/specs/017-figjam-flow-generation/`. The plan is a recommendation built from Sections 4 to 14 [INFERRED: each phase is confirmed only when its own verification passes]. Order and dependencies:

```text
002-write-route-spike ----------------------------+
                                                  v
003-vendored-figma-and-sync --> 004-parent-hub-conversion --> 005-flow-mode --+--> 006-claude-code-plugin --+
                                                                              +--> 007-project-mirror ------+--> 008-upstream-roundtrip-and-release
```

002 and 003 run in parallel. **003 is the first build phase**, because nothing in it depends on the write-route decision. 002 is a spike that gates 005.

### 002-write-route-spike

- **Order and dependencies:** first, none
- **In scope:** tool discovery for the hosted Figma MCP in Claude Code and in a claude.ai Project with the Figma connector. Record tool names, the `generate_diagram` schema, file and plan selection and the read-back tools. One scratch board through `generate_diagram` from the Change Location model, checking stadium, rhombus, circle, edge labels, `linkStyle` and `TD` direction. One scratch board through `fj`, recording whether create verbs print ids, whether connectors follow moved nodes and how label text nodes place. Discovery against the desktop-local Dev Mode MCP. A dated capture file per route
- **Out of scope:** any Product Owner source edit, any write to a non-scratch file
- **Verification:** both scratch boards exist and their read-back node and connector counts equal the model counts. The capture file holds the raw tool list and help output with dates. A one-page decision note names the primary route and the Project answer (Q1, Q5)

### 003-vendored-figma-and-sync

- **Order and dependencies:** first build phase, none
- **In scope:** `mcp-figma/` copied byte for byte at the Product Owner root, `vendor.json`, `scripts/vendor-sync.py` with `status`, `pull` and `push`, tests against a scratch git repository standing in for `Code_Environment/Public` and a hook into `benchmark/gates/run_gates.sh`
- **Out of scope:** hub registries, routing, Flow Mode, any write into `Code_Environment/Public`
- **Verification:** sha256 of every vendored file equals upstream at the base commit. `status` exits 0 right after `pull`. A one-byte local edit makes `status` exit 1 as local-ahead and `pull` refuse. A planted symlink is refused. `push` against the scratch upstream produces a diff that `git diff --stat` shows there. `run_gates.sh` and `run_parity.sh` exit 0 with the copy in place

### 004-parent-hub-conversion

- **Order and dependencies:** after 003
- **In scope:** root `SKILL.md`, `hub-router.json`, `mode-registry.json`, `sk-product-owner/ROUTER.md` with the Section 2 pointer, `AGENTS.md` read order and its four routing surfaces, a Product Owner hub check ported from `check-route-table.py` with the vendored exemption, `differential.py` and the other routing readers repointed, hub gold rows. Built in a scratch clone and applied as one patch
- **Out of scope:** Flow Mode content, the Project mirror
- **Verification:** router and format fixtures pass with the same counts as a baseline captured first. The hub check passes and fails on three planted defects (unregistered packet folder, wrong default, missing router pointer). Gold rows pass for a bare request, the fixture at `router fixtures:1643`, a `figma-ds-cli`-only request and a negated Figma mention. The default Task request's token count rises by no more than the hub `SKILL.md` itself, measured with one tokenizer before and after. A fresh reviewer reads the diff

### 005-flow-mode

- **Order and dependencies:** after 002 and 004
- **In scope:** `references/flow-mode.md`, `assets/flow-templates.md` with Mermaid patterns, the Flow command and routing rows, the pre-write check built on `mermaid_extract.py` (vendored through `vendor.json` or PO-owned, Q7), the write procedure for the route 002 chose and the delivery rule (Q3)
- **Out of scope:** plugin packaging, the Project mirror
- **Verification:** the check fails a four-exit decision, an unlabelled decision exit, an unknown shape and a 10-node diagram. It passes the Change Location model. Router fixtures pass for the Flow command and "make a FigJam flow from these screenshots". One end-to-end board from the 7 Change Location screenshots lands in a scratch FigJam file with read-back counts equal to the model and every decision exit labelled. `find export/` and `git status` show no HTML, SVG, PNG or Mermaid file created

### 006-claude-code-plugin

- **Order and dependencies:** after 005, parallel with 007
- **In scope:** `claude-plugin/` with `.claude-plugin/plugin.json`, `marketplace.json`, README and a build script that copies the hub, `sk-product-owner/` and `mcp-figma/` into an untracked `skills/` with Media Editor's refusals, plus `.gitignore` entries
- **Out of scope:** an MCP server entry, a bundled `figma-ds-cli`
- **Verification:** `claude plugin validate` exits 0. Two builds produce identical hash trees. A planted divergence and a planted link each fail the build. A `claude --plugin-dir` session lists the skill and routes the Flow command to Flow Mode. The README names Claude Code as the runtime and the Figma prerequisites

### 007-project-mirror

- **Order and dependencies:** after 005, parallel with 006
- **In scope:** a Flow Mode knowledge document with the Project-applicable rules, the kernel command list and router section, a kernel H1 minor bump, the connector-conditional write or refusal wording from Q5, pair and `unmirrored_sources` entries in `systems.py`
- **Out of scope:** mirroring `mcp-figma`, any generated mirror
- **Verification:** `run_parity.sh`, `run_receipts.sh`, `run_residency.sh` and `run_gates.sh` exit 0. `validate-output-format.cjs --system product-owner` passes. A deliberate rule-span drift fails. The dated review sentence lands in `PO/SYNC.md` only after the named human confirms [CONFIRMED: rule at root AGENTS.md:138-139]

### 008-upstream-roundtrip-and-release

- **Order and dependencies:** last, after 003 to 007
- **In scope:** one real optimization pushed upstream through `vendor-sync.py push`, for example the confirmed `fj` flags from 002 and, if Q2 says yes, the hosted FigJam route. Operator commit in `Code_Environment/Public`, `pull` to re-baseline, version bumps, changelog, README, a clean-clone test
- **Out of scope:** pushes to any remote without the operator's go-ahead
- **Verification:** the manifest base commit equals `Code_Environment/Public` HEAD for the path and `status` exits 0. A fresh `git clone` of Product Owner into a scratch folder has no dangling links and passes `run_gates.sh`. Every gate from 003 to 007 is rerun from the final state with its exit status read

---

## 16. Ranked Recommendations

1. **Run `002-write-route-spike` before any Flow Mode design work.** The hosted route has one recorded success and no recorded schema, and the `fj` route has help output but no write. Implementable now [CONFIRMED: NEF/tasks.md:50, live `fj --help`]
2. **Make the hosted `generate_diagram` route primary, with Mermaid as the checked model, and keep `fj` as the Desktop fallback.** It is the only route that has written a board here, and it carries edge labels that `fj connect` cannot. Needs an operator decision (Q1), and its upstream documentation needs Q2 [CONFIRMED: NEF/implementation-summary.md:124, live `fj connect --help`]
3. **Start `003-vendored-figma-and-sync` now:** a byte-identical root-level `mcp-figma/` packet, `vendor.json` and one `vendor-sync.py` with `status`, `pull` and `push`, gated in `run_gates.sh`. Implementable now [INFERRED: design, Section 10]
4. **Keep flow policy in `sk-product-owner` as Flow Mode and make the vendored copy the hub's only tool packet.** Implementable now [CONFIRMED: check-route-table.py:903, validate_parity.py:471]
5. **Build the pre-write check on `mermaid_extract.py`.** It already returns shapes, out-degree, labelled edges and budget flags. Implementable now, with Q7 for where it lives [CONFIRMED: run in this session]
6. **Convert the hub in a scratch clone, repoint `differential.py`, baseline every fixture count and measure the default-request tokens.** Implementable now [CONFIRMED: differential.py:78, MB-017/implementation-summary.md:74]
7. **Route Flow Mode only on an explicit command or explicit FigJam wording, and add gold rows for negation, quoting and the existing "figma" Task fixture.** Implementable now, with Q4 for the command name [CONFIRMED: PO/SKILL.md:97, router fixtures:1643, MB-018/implementation-summary.md:78]
8. **Replace the export step for Flow Mode with board-URL delivery and a read-back line, with no file in `export/`.** A Mermaid file in `export/` would be a second renderable diagram. Needs an operator decision (Q3) [CONFIRMED: protocol at PO/AGENTS.md:37-47] [INFERRED: the Mermaid concern]
9. **Ship a skills-only plugin with Media Editor's build refusals, no `bin/` and no `mcpServers`.** Implementable now, with Q8 for a later shim [CONFIRMED: build-plugin.ts:372-417, ME/README.md:15]
10. **Name the target Figma plan and file before every write, and keep board URLs and Barter screenshots out of the public repo.** Needs an operator decision for the default target (Q6) [CONFIRMED: NEF/implementation-summary.md:109, PO/LICENSE:1]

---

## Eliminated Alternatives

| Approach | Reason Eliminated | Evidence | Iteration(s) |
|---|---|---|---|
| Write the board through the registered Framelink MCP | It reads file and node data and downloads images, and does not drive Desktop | mcp-wiring.md:35, :112 | DS-1, L-1 |
| Treat `fj` as the only writer | The hosted Figma MCP wrote a 42-id board in this repo | NEF/tasks.md:50, NEF/implementation-summary.md:124 | DS-1, DS-17, L-1, L-8 (concluded `fj` only), corrected in synthesis |
| Carry edge labels on `fj connect` | No label flag exists | live `fj connect --help` | DS-7 (provisional), closed in synthesis |
| Rearrange generator nodes after `generate_diagram` | Connectors stay at the old positions, 42 stretched | NEF/implementation-summary.md:166 | Synthesis |
| Use `fj eval` to fill a gap | Arbitrary execution, off the default path | tool-surface.md:191, :235-240 | DS-3, DS-5, DS-17 |
| Headless or scheduled `fj` generation | Desktop session, daemon idle timeout, no reboot persistence | figma-cli-reference.md:84, :125 | DS-1, DS-17 |
| Plan against npm `figma-ds-cli` latest | 1.0.0 has no `fj` group | figma-cli-reference.md:57 | DS-17, L-1 |
| Reuse the HTML/SVG renderer or ship an HTML/SVG sidecar | FigJam is the only output, and the diagram skill excludes canvas deliverables | spec.md (parent):82, sk-design-diagram/SKILL.md:42 | DS-6, L-3 |
| PNG or SVG export as proof of delivery | Exactly what "only output" excludes | spec.md (parent):82 | DS-18 |
| A markdown receipt holding the Mermaid model in `export/` | Mermaid renders as a diagram on GitHub and similar viewers, a second output | spec.md (parent):79 (rule), inference on rendering | DS-18 (proposed), rejected in synthesis |
| `sk-vision` as the screenshot reader on Claude runtimes | Claude reads the PNG files natively | Read tool in this session, sk-vision/SKILL.md:3 | DS-2 |
| Symlink or submodule to `.skilled` | Links resolve to nothing in a clone, and a temporary link tripped the Commit-Id hook | PO/SYNC.md:44, MB-018/implementation-summary.md:78 | DS-13, DS-14 |
| Untracked build output as the embedded copy | A public clone would carry no skill, and the requirement asks Product Owner to carry the duplicate | spec.md (parent):67, Media Editor `runtime/.gitignore:9-11` | DS-14 (proposed), resolved in synthesis |
| Blind two-way copying between the repos | Overwrites unreviewed work in either repo | PO/SYNC.md:15 (no ledger), two git roots | L-4, L-8 |
| Generate the Claude Project mirror | Contradicts the manual parity method and the review rule | PO/SYNC.md:8-15, root AGENTS.md:138-139 | DS-14, DS-19 |
| One shared router file for all packets | +73 percent tokens on the default request | MB-017/implementation-summary.md:74 | DS-12, DS-20 |
| A separate FigJam workflow packet | The checker types non-default packets as tools, and the Sync Loop has one `skill_dir` | check-route-table.py:903, validate_parity.py:471 | DS-8, DS-15 (proposed), resolved in synthesis |
| Split upstream `mcp-figma` into `SKILL.md` plus `ROUTER.md` to satisfy the hub check | Changes the shared skill for one consumer, and an exemption for vendored packets costs less | check-route-table.py:928-930, mcp-figma/SKILL.md:145, :154 | Synthesis |
| Route any "figma" mention to FigJam | "figma" is a Task signal with an existing fixture, and Moneybird's prefix and negation bugs show the cost | PO/SKILL.md:97, router fixtures:1643, MB-018/implementation-summary.md:78 | L-7 |
| Bundle a Media Editor-style server in the plugin | The FigJam tools are external, and `mcp-figma` does not redistribute the CLI | ME/README.md:31, figma-cli-reference.md:384 | L-5, L-8 |
| Register the hosted Figma MCP in `plugin.json` | Auth and plan choice belong to the user, and the build pattern refuses `mcpServers` | build-plugin.ts:372-377, NEF/implementation-summary.md:109 | DS-9, synthesis |

---

## Divergence Map

### Saturated directions

- **The documented `fj` surface.** `tool-surface.md:149-152` and `figma-cli-reference.md:348` were restated in DS-1, DS-3, DS-5, DS-7, DS-17, DS-18, L-1, L-3 and L-8 without new evidence, because no lineage ran `--help`. Closed here by the live help capture
- **Moneybird hub anatomy.** DS-11, DS-15, L-6 and L-8 read the same registries and `SKILL.md` lines with matching results
- **The Media Editor build paragraph.** `ME/README.md:83` carried DS-9, DS-10, DS-14, DS-20, L-5 and L-8

### Frontier the run left open, and what this synthesis closed

| Item | At run close | Now |
|---|---|---|
| `fj shape` kinds, `fj connect` labels | Open in both lineages | Closed by live help |
| Screenshot extraction | Open in L-8 | Closed: native image reading on Claude |
| Any write route besides `fj` | Not found | Found: hosted `generate_diagram`, recorded in `NEF/` |
| `generate_diagram` schema, Mermaid shape mapping, connector tool list in a Project | Not asked | Open, phase 002 |
| `fj` create id return, connector attach on move | Open | Open, phase 002 |
| Plugin skill discovery for a nested hub | Not asked | Open, phase 006 |
| Rate limits and board size limits | Open | Open, nothing local documents them |

### Where the lineages diverged

| Topic | DeepSeek | Luna | Resolution |
|---|---|---|---|
| Screenshot intake | `sk-vision` OCR and detection (DS-2) | Unresolved spike, no proven OCR path (L-2, L-8) | Neither: Claude reads the images natively (Section 6) |
| Where flow policy lives | A new FigJam packet with its own router (DS-8, DS-15) | The default workflow packet, with `mcp-figma` as a tool packet (L-6, L-8) | Luna, on the checker, `skill_dir` and upstream transport facts (Section 11) |
| Embedded copy form | Generated build output with a source-difference refusal (DS-14) | Verbatim tracked subtree with an upstream revision and a reviewed patch cycle (L-4, L-8) | Both, at different hops: tracked copy with manifest for hop 1, Media Editor build output for hop 2 (Section 10) |
| Plugin form | `plugin.json` plus marketplace, no MCP server (DS-9, DS-15 phase 4) | Thin plugin with a `bin` shim that preflights the CLI (L-5, L-8) | Skills-only first, shim only if 002 shows the `fj` route needs one (Section 9) |
| Delivery proof | Non-deliverable markdown receipt with the model and read-back (DS-18) | Internal model, provenance notes on the board (L-2) | Board URL plus read-back line, no export file, pending Q3 |
| Pair count | 38 declared pairs (DS-16) | Not counted | 37 in `systems.py` today |
| Phase plan | Seven phases led by surface verification (DS research.md §15) | Six phases led by a feasibility spike (L research.md §14) | Merged into seven phases, 002 to 008 (Section 15) |

---

## 17. Open Questions for the Operator

1. **Primary write route.** After phase 002, should Flow Mode write through the hosted `generate_diagram` route or through `fj`, or offer both? Recommendation: hosted primary, `fj` fallback
2. **Upstream support for the hosted route.** `mcp-wiring.md:152-159` says not to wire or recommend the official Figma MCP. Should upstream `mcp-figma` adopt the hosted FigJam route through the sync path (phase 008), or should it live only in Product Owner's Flow Mode?
3. **Delivery under the export protocol.** `PO/AGENTS.md:37` blocks every reply until a markdown file is saved and read back. Should Flow Mode be exempt, replying with the board URL and a read-back line, or save a text receipt in `export/`, and if so with or without the Mermaid model?
4. **Command name.** `$flow`, `$figjam` or both, and which shortcut letter?
5. **Claude Project scope.** Should the Project write boards through the Figma connector when it is present, the way it publishes to ClickUp, or stay advisory and refuse board delivery?
6. **Default target.** Which Figma plan, team and file receive boards, and is that fixed or asked on every request?
7. **Where the pre-write check lives.** Vendor `mermaid_extract.py` from `sk-design-diagram` through `vendor.json`, or write a Product Owner-owned check?
8. **Plugin `bin/`.** Ship skills only, which may let claude.ai and Cowork install the plugin, or add a `bin` shim for the `fj` route and accept Claude Code only?
9. **A home for plugin optimizations.** `.skilled` has no Claude Code plugin. Should plugin-shell changes stay Product Owner-only, or should `.skilled` gain a shared plugin template?
10. **Sync Loop change.** If phase 007 finds the parity gate needs to know about the hub layout, may `systems.py` and its tools change, given that they serve seven systems?

---

## 18. References

- `specs/z-staging-po-017-research/research/resource-map.md` lists 62 references across READMEs, documents, skills, specs, scripts, tests, config and meta. Its one MISSING row, `.skilled/sk-vision/SKILL.md`, is a wrong path for `.skilled/skills/sk-vision/SKILL.md`
- Lineage records: `research/lineages/deepseek/iterations/iteration-001.md` to `iteration-020.md`, `research/lineages/luna/iterations/iteration-001.md` to `iteration-008.md`, `research/lineages/deepseek/research.md`, `research/lineages/luna/research.md`
- Merged state: `research/findings-registry.json`, `research/fanout-attribution.md`
- Sources found in this synthesis and absent from the resource map:
  - `specs/017-notification-event-flow-map/plan.md`, `tasks.md`, `implementation-summary.md`, the hosted-route board record
  - `.skilled/skills/mcp-tooling/mode-registry.json`, the upstream registry row for `mcp-figma`
  - `.skilled/skills/sk-design/sk-design-diagram/scripts/mermaid_extract.py`, the Mermaid parser
  - `AI Systems/Moneybird Accountant/sk-moneybird-accountant/scripts/check-route-table.py:67-72`, the embedded-router marks
  - `AI Systems/Product Owner/benchmark/router/differential.py:78`, the router file it parses
  - `AI Systems/z*Claude Project Sync Loop/systems.py` and `validate_parity.py:471`, the declaration and source inventory
  - `AI Systems/Media Editor/specs/005-media-editor-cli-runtime/spec.md`, the MCP-to-CLI move
  - `AI Systems/Media Editor/runtime/.gitignore:9-11`, the untracked payload
- Live captures in this session: `figma-ds-cli --version`, `figma-ds-cli fj --help` and `fj shape|connect|sticky|nodes|info --help`, the screenshot read, the `mermaid_extract.py` sample run

---

## Appendix: Convergence and Citation Audit

- **Stop reason:** both lineages reached their iteration cap, 20 and 8, with convergence stopping off [CONFIRMED: 001/spec.md:101-102, DS research.md appendix, L research.md convergence report]
- **Registry:** 28 iterations, 161 key findings, 60 ruled-out directions, 9 resolved and 1 open question ("What can the Figma MCP build, read and refuse inside FigJam"), which Section 4 now answers except for the hosted schema [CONFIRMED: findings-registry.json]
- **Citations opened:** 164. By source group: `mcp-figma` 42, `sk-design-diagram` 10, `sk-vision` 2, Product Owner 46, Media Editor 25, Moneybird 25, packet and root files 12, screenshot listings 2
- **Citations that failed:** 3. The `sk-vision` path, `PO/SYNC.md:27` and the 38-pair count. 4 more pointed one or two lines off and hold at the nearby line
- **Claims downgraded:** 5 (Section 3 table)
- **Claims upgraded by live checks:** `fj` shape kinds and connector options, screenshot reading, `mermaid_extract.py` output fields
- **Load-bearing facts neither lineage found:** the hosted-route board in `NEF/`, the upstream `mcp-tooling` registry row, the embedded-router conflict with Moneybird's checker, the single `skill_dir` in the Sync Loop, `differential.py` parsing `SKILL.md`, the Change Campaign folder name and the Media Editor MCP-to-CLI move
