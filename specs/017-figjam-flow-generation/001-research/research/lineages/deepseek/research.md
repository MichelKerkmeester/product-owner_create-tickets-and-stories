# Research: Product Owner turning screenshots, Figma flows and product docs into FigJam flows (deepseek lineage)

Twenty forced-depth iterations, evidence-cited from local files. Every claim below is tagged `[CONFIRMED]` when a cited local line states it, or `[INFERRED]` when it is derived from cited lines. Nothing here claims a live Figma run: no `figma-ds-cli` was installed or executed in this environment.

## 1. Executive Summary

The capability the topic assumes does exist, but not where the topic says. FigJam writing is a CLI verb group, `fj sticky|shape|text|connect|move|update`, with read-only `fj list|info|nodes`, destructive `fj delete` and arbitrary `fj eval`; the "Figma MCP" registered in this repo is a third-party read-only design-context server that never touches FigJam. `[CONFIRMED]` FigJam writes exist only in the unpublished 1.2.0 build from the silships repository; npm publishes 1.0.0 with no `fj` verbs at all, so the first practical requirement is a pinned repo build, not a design decision. `[CONFIRMED]`

Within that surface the whole design collapses to one intermediate model: nodes with a kind, label, platform and source pointer, plus edges with source, target and condition, positioned manually because there is no layout verb. `[INFERRED]` The diagram grammar that survives is the model-level part of `sk-design-diagram`: shape carries type, at most three exits per decision, every branch labelled, no colour-encoded types, one emphasis colour. The renderer-specific rules (merge dot, arc jump, HTML/SVG geometry) have no FigJam equivalent and need text or placement substitutes. `[CONFIRMED]` + `[INFERRED]`

Product Owner needs four coordinated changes: a second skill package with generated leaf manifests, a Claude Code plugin whose skill copy is an untracked build output with a source-difference refusal, a parent-hub conversion following the Moneybird two-registry pattern with one router per packet, and a Project mirror that splits into Project-applicable rules and runtime-only rules because a claude.ai Project cannot run a CLI or write a file. `[CONFIRMED]` + `[INFERRED]` The sync path is two hops, not one: skill to embedded copy can be generated with a refusal; copy to Project mirror cannot, because the workspace contract requires a human per-paragraph decision and a dated review. `[CONFIRMED]`

## 2. Scope and Method

- **Scope**: the eight parts of the topic, plus the delivery contract they collide with. No file outside this research packet was modified.
- **Method**: 20 iterations, each opening a new question or deepening an earlier finding, each citing local file and line. Sources were read directly; no web sources were used, and no repository tooling that writes was run.
- **Constraint**: `figma-ds-cli` was not available, so every verb-level claim stays documentation-grade and is marked as such. The skill's own reference records that it was never executed during its own research either. `[CONFIRMED]` (`.skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:367`)

## 3. Sources

| Source | What it contributed |
|---|---|
| `.skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md` | The four gating classes, the full verb table, the `fj` group, destructive and arbitrary sets |
| `.skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md` | Binary identity, the npm 1.0.0 versus repo 1.2.0 gap, daemon token, uncertainty list |
| `.skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md` | Framelink MCP is read-only, Code Mode stdio, prefixed token |
| `.skilled/skills/mcp-tooling/mcp-figma/README.md` | Desktop and daemon dependency, macOS baseline, connect modes |
| `.skilled/skills/sk-design/sk-design-diagram/SKILL.md` | Two supported formats, canvas artifacts out of scope |
| `.skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md` | The flowchart grammar and anti-patterns |
| `.skilled/skills/sk-design/sk-design-diagram/scripts/validate-flowchart.sh` | The decision-label check |
| `AI Systems/Product Owner/AGENTS.md` | Identity, export protocol, skill reading instructions, command registry, DAG |
| `AI Systems/Product Owner/sk-product-owner/SKILL.md`, `leaf-manifest.config.json`, `graph-metadata.json` | Artifact lanes, routing, package parts, generated manifests |
| `AI Systems/Product Owner/SYNC.md`, `claude project/Custom Instructions.md`, `kernel-review.json` | Manual parity, vendored cards, Project runtime limits |
| `AI Systems/Product Owner/benchmark/{gates,parity}` | Shared gate wrappers, `systems.py` declarations, receipts, residency |
| `AI Systems/Media Editor/runtime/claude-plugin/README.md` and its phase 8 record | Plugin manifest, build output, parity refusals, superseded assumptions |
| `AI Systems/Moneybird Accountant/{hub-router.json,mode-registry.json,SKILL.md}` and phase 17/18 records | Hub anatomy, routing cost, review findings |
| `Product Context/a — Screenshots/...` | Screenshot corpus layout and filename grammar |
| `specs/z-staging-po-017-research/{goal.md,spec.md,plan.md,tasks.md}` | Packet directive, acceptance criteria, unfilled scaffolds |

## 4. Track 1: FigJam capability and limits

1. FigJam authoring exists only as the CLI `fj` group: read-only `fj list|info|nodes`, mutating `fj sticky|shape|text|connect|move|update`, destructive `fj delete`, arbitrary `fj eval`. `[CONFIRMED]` (`.skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:149`, `.skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:348`)
2. The registered Figma MCP is read-only design context: a third-party Framelink server over the Figma REST API that does not drive Figma Desktop. `[CONFIRMED]` (`.skilled/skills/mcp-tooling/mcp-figma/references/mcp-wiring.md:35`, `:68`)
3. `figma-ds-cli` ships no MCP server; an MCP for Figma is always external. `[CONFIRMED]` (`.skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:360`)
4. npm publishes only 1.0.0, whose help lists no `daemon`, no `extract`, no safe `connect` and no `fj`; the full surface exists only in the unpublished 1.2.0 repo build. `[CONFIRMED]` (`.skilled/skills/mcp-tooling/mcp-figma/references/figma-cli-reference.md:54`, `:57`)
5. Writes require Figma Desktop open with a file, a healthy local daemon on `127.0.0.1:3456`, Node 18+, and macOS is the supported baseline; the daemon is idle-timed and not reboot-persistent. `[CONFIRMED]` (`.skilled/skills/mcp-tooling/mcp-figma/README.md:26`, `:99`, `:109`)
6. Every write is gated MUTATING with confirmation, explicit target and rollback; destructive and arbitrary verbs are outside the default path. `[CONFIRMED]` (`.skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:51`, `:184`)
7. The documented surface drifts from source, so flags must be verified with `--help`. `[CONFIRMED]` (`.skilled/skills/mcp-tooling/mcp-figma/references/tool-surface.md:17`)

**Limit statement.** Within the documented surface a FigJam board can hold sticky notes, shapes, text, connectors between existing nodes, and can be repositioned and updated. It cannot hold images, frames, sections, tables, code blocks or embedded files, and there is no automatic layout. `[CONFIRMED]` for the verb list; `[INFERRED]` for the exclusions, which rest on the absence of any such verb in a table the skill presents as complete.

## 5. Track 2: Input handling per type

| Input | Native evidence | What it supplies | What it cannot supply |
|---|---|---|---|
| Screenplay screenshots | `Flow/<platform>/` ordered steps plus `Components/<platform>/` states; filenames encode trigger and post-state `[CONFIRMED]` | Step order, platform, trigger phrase, state names | Branch conditions, non-captured states, on-screen control identity without OCR |
| Figma frames | `node tree`, `inspect`, `export screenshot` `[CONFIRMED]` | Hierarchy, node names, per-node specs, pixels | Transitions; no documented design-to-FigJam bridge, and `fj` has no image verb `[CONFIRMED]` |
| Product docs | PO doc lane covers behavior references, runbooks, architecture docs `[CONFIRMED]` | Actors, conditions, outcomes, vocabulary | States, visual hierarchy, platform split, coordinates `[INFERRED]` |

Three consequences:

1. The corpus is already structured; intake should take one `Flow/<platform>` folder (7 images in Change Location) rather than 341 images. `[CONFIRMED]` (directory listing)
2. `sk-vision` is the only local pixel reader: 13 tools, no API key, opt-in and idle, one-time Bun build. `[CONFIRMED]` (`.skilled/skills/sk-vision/SKILL.md:11`, `:38`)
3. No input type supplies a complete edge; the agent must synthesize every source-target-condition triple. `[INFERRED]` (from the three-column table above)

**The intermediate model** (the handoff contract all three inputs feed):

```text
node  { id, kind: start|end|step|decision|state|note, label, platform, source }
edge  { from, to, condition? }
layout{ column, row, group }
```

It is exactly renderable by the six verbs, and nothing larger is. `[INFERRED]` (verb ceiling at `tool-surface.md:150`)

## 6. Track 3: Which sk-design-diagram rules carry over

**The source grammar.** Oval start/end, rectangle step, diamond decision with at most three exits, filled dot merge; top-to-bottom flow, Yes right and No below, every outgoing arrow labelled, coral only on the happy path or one decision, arc jump for crossings; three anti-patterns: colour-encoded type, four-plus exits, unlabelled branches. `[CONFIRMED]` (`.skilled/skills/sk-design/sk-design-diagram/references/types/type-flowchart.md:20`, `:25`, `:29`)

**The machine check that exists.** The ASCII validator fails a run when decision words appear with no YES/NO labels. `[CONFIRMED]` (`.skilled/skills/sk-design/sk-design-diagram/scripts/validate-flowchart.sh:82`)

**Classification for FigJam:**

| Rule | Verdict | Replacement or dependency |
|---|---|---|
| Shape carries type | Portable as intent | `fj shape` kinds and flags are undocumented; confirm with `--help` `[CONFIRMED]` gap |
| ≤3 exits per decision | Portable (model-level) | Validate in the model before writing |
| Every branch labelled | Portable (model-level) | If `fj connect` cannot carry a label, put the condition in the target node's label `[INFERRED]` |
| No colour-encoded type | Portable | FigJam colour is decoration only |
| One emphasis colour | Portable | Happy path only |
| Merge dot | Unenforceable | Several edges into one target node |
| Arc jump | Unenforceable | Column placement |
| Top-down layout | Expensive | Manual `move`/`update`; no layout verb |
| HTML/SVG rendering | Unenforceable | One node at a time; the skill's canvas exclusion applies `[CONFIRMED]` (`.skilled/skills/sk-design/sk-design-diagram/SKILL.md:42`) |

**Enforcement must move with the rules.** No FigJam validator exists; the pipeline needs its own model check before any write. `[INFERRED]`

## 7. Track 4: Embedding, plugin form and sync

**Embedding.** A Product Owner skill is a leaf package with fixed parts (`SKILL.md`, `graph-metadata.json`, two leaf manifests and aliases, `references/`, `assets/`, `changelog/`, `manual-testing-playbook/`, `README.md`). `[CONFIRMED]` (`AI Systems/Product Owner/sk-product-owner/leaf-manifest.config.json:2`) The manifests are generated (`generate-leaf-manifest.cjs`, `ci-skill-root-metadata.cjs --fix`), so a copy must ship the generator or its manifests rot. `[CONFIRMED]` (same file, `:11`) `graph-metadata.json` declares inter-skill edges, so a new skill must declare its relation to `sk-product-owner`. `[CONFIRMED]` (`AI Systems/Product Owner/sk-product-owner/graph-metadata.json:3`, `:9`) Product Owner is a nested git repository, which is the concrete "two repos". `[CONFIRMED]` (`AI Systems/Product Owner/.git`) The package is explicitly single-mode with no `mode-registry.json`. `[CONFIRMED]` (`leaf-manifest.config.json:9`)

**Plugin form.** The Media Editor precedent is a five-field `plugin.json` plus a one-plugin local marketplace; the plugin payload (`server/`, `bin/`, `skills/<skill>/`) is untracked build output, the copied skill folder is replaced wholesale each build, and the build refuses any copied file that differs from its source, any link, and a `plugin.json` declaring an MCP server. `[CONFIRMED]` (`AI Systems/Media Editor/runtime/claude-plugin/README.md:31`, `:78`, `:83`) It registers no MCP server, which costs claude.ai/Cowork compatibility. `[CONFIRMED]` (`:15`)

**Sync.** The current state is a three-hop manual chain: shared card to vendored copy (four rule cards, declared `vendored_shared_copies`) to Project mirror under a four-step manual parity method with no manifest, lock file or checksum ledger. `[CONFIRMED]` (`AI Systems/Product Owner/SYNC.md:9`, `:17`, `:44`) A hand-written mirror proves neither review nor deployment. `[CONFIRMED]` (`AGENTS.md:138`)

**Recommendation (sync).** Two hops with two different owners:

- Hop 1, skill to embedded copy: **generated**, with the Media Editor refusal triple (source-difference, no links, whole-folder replacement) and regenerated manifests. `[INFERRED]`
- Hop 2, copy to Project mirror: **manual**, with the split rule from Track 6 and a dated review sentence. A fully generated mirror would contradict the workspace contract. `[CONFIRMED]` + `[INFERRED]`

## 8. Track 5: Parent-hub conversion

A Moneybird-style hub is two small registries: `hub-router.json` (`version`, `routerPolicy.defaultMode|handoff|fallback`, per-mode signals) and `mode-registry.json` (`hub`, per-mode `workflowMode|packet|packetSkillName|packetKind|router|default`). `[CONFIRMED]` (`AI Systems/Moneybird Accountant/hub-router.json:1`, `AI Systems/Moneybird Accountant/mode-registry.json:1`) The hub `SKILL.md` is a packet picker; routing is two stages with the packet's `ROUTER.md` as stage two. `[CONFIRMED]` (`AI Systems/Moneybird Accountant/SKILL.md:10`, `:30`) A hub ships its own consistency checkers. `[CONFIRMED]` (`:38`)

**Measured cost.** One shared router inflated an accountant request from 9,635 to 16,664 `o200k_base` tokens, so one router per packet replaced it. `[CONFIRMED]` (`.../017-parent-hub-and-router/implementation-summary.md:74`) Review found four P1s, including about fifty stale pointers and checks that passed with nothing to test. `[CONFIRMED]` (same line) The blast radius is tooling: every routing reader had to move. `[CONFIRMED]` (`:54`) Hub scoring needed its own gold rows. `[CONFIRMED]` (`.../018-hub-scoring-and-contract-gaps/implementation-summary.md:56`)

**Product Owner change list, in order:**

1. Add `hub-router.json` and `mode-registry.json` at the Product Owner root. `[INFERRED]`
2. Move `sk-product-owner` section 2 routing into `sk-product-owner/ROUTER.md`, leaving a pointer. `[CONFIRMED]` pattern
3. Add the new packet directory with its own `ROUTER.md`, `SKILL.md`, generated manifests and graph metadata. `[CONFIRMED]` pattern
4. Repoint the bootstrap surfaces that move together: Section 3 STEP 1, the Command Registry, Routing Compatibility, Document Loading Order and the Full DAG. `[CONFIRMED]` (`AI Systems/Product Owner/AGENTS.md:159`, `:186`, `:200`, `:230`)
5. Update the Project mirror (new knowledge document, kernel command list, kernel H1 bump). `[CONFIRMED]` (`AI Systems/Product Owner/SYNC.md:19`, `:20`)
6. Extend the fixtures and declare the new pair in the shared `systems.py` (38 pairs today). `[CONFIRMED]` (`AI Systems/Product Owner/benchmark/gates/README.md:22`)

## 9. Track 6 (cross-cutting): Delivery, gates and risk

**Delivery.** Product Owner blocks delivery until a markdown artifact is saved and read back from its exact path. `[CONFIRMED]` (`AI Systems/Product Owner/AGENTS.md:37`, `:46`) A board cannot satisfy that literally. The coherent reading is one delivered artifact, the board, plus a **non-deliverable verification receipt** holding the node read-back and the model. `[INFERRED]` The only board read-back is `fj list|info|nodes`, which proves existence but not correctness. `[CONFIRMED]` (`tool-surface.md:149`) A claude.ai Project cannot execute any of this: it has no filesystem, cannot run the CLI, and renders only a Canvas Artifact. `[CONFIRMED]` (`AI Systems/Product Owner/claude project/Custom Instructions.md:2`, `:265`, `:279`)

**Gates.** The parity gate is shared and external; it reads 38 declared pairs from `z — Claude Project Sync Loop/systems.py`, counts verbatim rule spans, lints examples, and under `--receipts` treats a missing or stale upload receipt as a finding; residency holds declared kernel statements to their declared home. `[CONFIRMED]` (`AI Systems/Product Owner/benchmark/gates/README.md:22`, `:23`, `:27`; `.../benchmark/parity/README.md:31`, `:34`, `:48`)

**Risk register, ranked by reducibility:**

| Risk | Severity | Reducible? |
|---|---|---|
| FigJam verbs only in unpublished 1.2.0 `[CONFIRMED]` | Blocker | Yes: pin the repo build, verify `--help` |
| Public MIT repo carries the copy and examples `[CONFIRMED]` | High | No: structural |
| Figma PAT for the MCP path; daemon token `[CONFIRMED]` | High | Partly: avoid the MCP path, never echo tokens |
| Undocumented rate limits `[CONFIRMED]` absence | Medium | No: external owner |
| `fj delete`/`fj eval` against a real board `[CONFIRMED]` | High | Yes: policy + model validation |
| Local, fragile runtime (Desktop, daemon, yolo patch) `[CONFIRMED]` | Medium | Partly: safe connect, declared prerequisites |
| Docs-versus-source drift `[CONFIRMED]` | Medium | Yes: `--help` verification step |

## 10. Confirmed versus inferred register

- **Confirmed**: FigJam verb inventory and classes; MCP read-only role; version gap; Desktop/daemon/Node/macOS requirements; gating policy; screenshot corpus layout; absence of a design-to-FigJam bridge; sk-vision capability; flowchart grammar and validator; PO package parts and generated manifests; nested repo; plugin structure, build output and refusals; hub registries, routing stages, token cost, P1s; manual parity and vendored cards; Project runtime limits; gate declarations and receipts; the plan/tasks scaffolds are unfilled.
- **Inferred**: the six-verb exclusions (image/frame/table/section) from absence; the intermediate model and its field set; the label-carries-condition fallback; the transfer classifications that depend on unverified `fj shape`/`fj connect` flags; the two-hop sync recommendation; the board-versus-receipt distinction; the phase ordering.

## 11. Copy-and-avoid: Media Editor plugin

**Copy**

- Five-field `plugin.json` plus a one-plugin local marketplace pointing at `./`. `[CONFIRMED]` (`AI Systems/Media Editor/runtime/claude-plugin/.claude-plugin/plugin.json:2`, `.claude-plugin/marketplace.json:9`)
- Payload as untracked build output, with the skill folder replaced wholesale each build. `[CONFIRMED]` (`AI Systems/Media Editor/runtime/claude-plugin/README.md:78`, `:83`)
- The refusal triple: source-difference, no links, no MCP server in `plugin.json`. `[CONFIRMED]` (`:83`)
- A spike before shipping a runtime assumption; the Node assumption was recorded and superseded. `[CONFIRMED]` (`.../008-claude-code-plugin/acceptance-criteria.md:63`)

**Avoid**

- Assuming the runtime supplies Node or expands bundle settings. `[CONFIRMED]` (`.../implementation-summary.md:55`)
- A blanket redirect-refusal rule that silently removes platform coverage: it blocked eight of ten pinned URLs until amended. `[CONFIRMED]` (`.../decision-record.md:163`, `:179`)
- Testing against the development dependency instead of the shipped payload: 45 capability-unrelated failures. `[CONFIRMED]` (`.../implementation-summary.md:122`)
- Shipping links in a package. Product Owner already had to replace four symlinked rule cards for a clone to work. `[CONFIRMED]` (`AI Systems/Product Owner/SYNC.md:44`)
- Copying the "no MCP server" choice blindly: it is why that plugin reaches Claude Code only. `[CONFIRMED]` (`README.md:15`)

## 12. Copy-and-avoid: Moneybird Accountant hub

**Copy**

- Two registries and a routing-only hub `SKILL.md`; two-stage routing with one `ROUTER.md` per packet. `[CONFIRMED]` (`hub-router.json:1`, `mode-registry.json:1`, `SKILL.md:10`, `:30`)
- Default mode = the workflow packet; tool packets activate by whole-word signal only. `[CONFIRMED]` (`SKILL.md:32`)
- Hub consistency checkers and hub-level gold rows. `[CONFIRMED]` (`SKILL.md:38`, `.../018-hub-scoring-and-contract-gaps/implementation-summary.md:56`)
- Per-file contract checks rather than one aggregate check. `[CONFIRMED]` (`.../018.../implementation-summary.md:54`)

**Avoid**

- One shared router file: measured +73 percent tokens on the default path. `[CONFIRMED]` (`.../017-parent-hub-and-router/implementation-summary.md:74`)
- Declaring the conversion done when the files exist: two review rounds found P1s afterwards, including ~50 stale pointers. `[CONFIRMED]` (`:74`)
- Ignoring the routing readers: ten scripts and their tests had to move. `[CONFIRMED]` (`:54`)
- Leaving structural metadata out: nine phase folders lacked `description.json` and `graph-metadata.json`. `[CONFIRMED]` (`.../018.../implementation-summary.md:58`)

## 13. Eliminated Alternatives

| Alternative | Why it is out |
|---|---|
| Build the board through the Figma MCP | The MCP is read-only and does not drive Desktop. `[CONFIRMED]` |
| Use `fj eval` to fill capability gaps | Arbitrary execution against a live board; outside the default policy. `[CONFIRMED]` |
| Headless or scheduled generation | No headless path; Desktop, daemon, macOS, idle timeout. `[CONFIRMED]` |
| Embed images or tables in the board | No documented verb; excluded by the six-verb ceiling. `[INFERRED]` |
| Reuse the HTML/SVG renderer | The diagram skill excludes canvas artifacts and has no FigJam export. `[CONFIRMED]` |
| Symlink or submodule the shared skill | Links fail in a clone; the plugin build rejects links. `[CONFIRMED]` |
| Generate the Project mirror | Contradicts the manual parity contract and the review gate. `[CONFIRMED]` + `[INFERRED]` |
| One shared router for all packets | Measured +73 percent tokens. `[CONFIRMED]` |
| Plan against npm `figma-ds-cli` latest | It has no FigJam verbs at all. `[CONFIRMED]` |

## 14. Divergence Map

- Saturated directions: none. No direction was retried without new evidence.
- Completed pivots: 0. Failed pivots: 0. Audited overrides: 0.
- Frontier at close: live verification of the FigJam verb surface, which no amount of local reading can settle.
- Coverage: capability (4 iterations), inputs and model (3), rule transfer (2), embedding and plugin (3), hub (3), sync and gates (3), risk and delivery (2). All five key questions were investigated; four are ticked in the strategy, the capability question remains unticked because its flags are unverified.

## 15. Recommended Later Phases

Later phases, in order, with scope and verification. None of these ran in this phase.

| # | Phase | Scope | Verification |
|---|---|---|---|
| 1 | **Surface verification** | Install the 1.2.0 repo build; capture `fj --help`, `fj shape --help`, `fj connect --help`, `fj info --help`; record whether shape kinds and connector labels exist and whether creation returns ids | A dated capture file per verb; every claim in Track 1 and Track 3 re-tagged confirmed or corrected; the unticked key question closed |
| 2 | **Flow model specification** | Write the intermediate model, its validation rules (three-exit ceiling, labelled branches, kind vocabulary) and the source-pointer rule; define the markdown verification receipt | A validator that fails a four-exit decision, an unlabelled branch and an unknown kind; a worked example per input type |
| 3 | **Skill embedding** | Create the Product Owner packet: `sk-po-figjam` with `SKILL.md`, `ROUTER.md`, `graph-metadata.json`, generated leaf manifests; vendor the FigJam surface it needs; build step that copies and refuses divergence | `ci-skill-root-metadata.cjs --fix` clean; a deliberate copy drift fails the build; no links in the package |
| 4 | **Plugin packaging** | Add `plugin.json` and a local marketplace; decide the transport honestly (no MCP server, and state the claude.ai cost) | `claude plugin validate` if available; a `--plugin-dir` session lists the skill; a rebuild reproduces the skill folder byte for byte |
| 5 | **Parent hub conversion** | Add `hub-router.json` and `mode-registry.json`; move routing into per-packet `ROUTER.md`; repoint the four bootstrap surfaces; add hub gold rows | Route fixtures pass for default, new-command, CLI-only and refusal requests; `AGENTS.md` read order matches the hub; token count on the default path does not rise |
| 6 | **Project mirror** | New knowledge document for the model and refusal path; kernel command and version bump; declare the new pair in `systems.py`; runtime-only markers | `run_parity.sh`, `run_receipts.sh`, `run_residency.sh` and `run_gates.sh` pass; a deliberate rule-span drift fails; the dated review sentence is present |
| 7 | **End-to-end board** | Generate one real board from one screenshot flow in a scratch FigJam file, with the receipt | `fj nodes` read-back matches the model node count; every edge has a label; the receipt names the source per node; no destructive or arbitrary verb used |

Rationale for the order: phase 1 fixes the facts, phase 2 fixes the contract, 3–6 build the packaging in dependency order, and phase 7 is the first point where a board exists at all. `[INFERRED]`

## 16. Open Questions

1. Does `fj shape` accept a diamond or only generic shapes, and does `fj connect` accept a label? Only a live `--help` can answer. `[CONFIRMED]` gap
2. Does a creation verb return a node id on stdout, or must every connector step read ids back? `[CONFIRMED]` gap (no return contract documented)
3. What does `fj info` emit, and can it serve as the receipt's read-back evidence? `[CONFIRMED]` gap
4. Are there Figma-side node or connector limits per board that constrain a large flow? Nothing local documents one. `[CONFIRMED]` absence
5. What are the API rate limits for the MCP path? External and unpinned. `[CONFIRMED]` absence
6. Will claude.ai ever expose a Figma connector? External; the Project path stays model-only until then. `[INFERRED]`
7. Is the unpublished 1.2.0 build distributable to a Product Owner user, or must the user build it from the silships repo? Only packaging research can settle it. `[INFERRED]`

## 17. Verification Plan

- Every Track 1 and Track 3 claim marked with a `--help` gap becomes confirmed or corrected by phase 1's captures; no phase may cite it as confirmed before then.
- The flow-model validator from phase 2 is the admission gate for every write; a four-exit decision or unlabelled branch fails before any CLI call.
- The embedding build from phase 3 fails on copy divergence, links, or a hand-edited manifest; the plugin in phase 4 reproduces the skill folder byte for byte.
- The hub in phase 5 keeps the existing route fixtures green and adds cases for the new command and the refusal path.
- The Project mirror in phase 6 passes the shared parity gate with receipts and residency, and declares its new pair in `systems.py`.
- The end-to-end board in phase 7 is the only phase that proves the capability; its receipt is the delivery evidence, and the board is the only artifact.

## 18. Provenance and Deviations

- **Provenance**: 20 iteration files and 20 delta records in this lineage, one canonical ledger event per iteration through the append gateway, strategy/registry/dashboard refreshed by the reducer at close.
- **Deviations**: (a) the topic names the Figma MCP as the capability, while the repo's write path is the CLI; both were researched and each claim attributes its transport. (b) The packet's `plan.md` and `tasks.md` are still template scaffolds, so Section 15 is authored from this research rather than from them. (c) No live Figma run was possible, so seven verb-level questions remain open by construction. (d) The `steer.md` channel was checked before every iteration and never existed, so no lead ruling bound this lineage.

## Appendix: Convergence Report

- **Stop reason**: maxIterationsReached
- **Total iterations**: 20 of 20
- **Questions answered**: 4 of 5 ticked; the fifth (capability limits) is answered at documented level and held open for live verification
- **Average new information ratio**: 0.91 (range 0.45 to 1.00; the low points are the two synthesis iterations, 5 and 20)
- **Convergence threshold**: 0.05, mode off; convergence was telemetry only, and no iteration stopped early
- **Source diversity**: 20 distinct local sources across five domains (Figma tooling, diagram rules, Product Owner package, plugin precedent, hub precedent); no finding rests on a single weak source
- **Remaining questions**: the seven in Section 16, of which the first three are closable with a live `--help` capture
