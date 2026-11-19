# Deep Review Iteration 008

**Dimension:** correctness
**Focus (pass 8):** `sk-create-figjam`, `manual-testing-playbook/` and the vendored MCP packages — drift between the Product Owner copies and how the hub and `sk-product-owner` call them (tool names, manual names, Code Mode registration in `.utcp_config.json`), broken references and stale examples.
**Mode:** review · **Router:** `Resolved route: mode=review target_agent=deep-review`
**Operator focus addressed:** the "how easily do the vendored mcp and browser packages sync from Skilled" question was answered this pass at the point where a vendored package stops describing its own upstream and starts describing the Product Owner's live registration — that seam is where the two artifacts disagree (P1 below). The `doctor:overlay`/repin comparison stays open; the evidence gathered here bounds it (see Next Dimension).

## Files Reviewed

- `AI Systems/Product Owner/.utcp_config.json:49` — the `chrome_devtools_live` manual template (`chrome-devtools-mcp@0.26.0`, `--autoConnect`)
- `AI Systems/Product Owner/.utcp_config.json:57` — the pinned chrome transport argument
- `AI Systems/Product Owner/.utcp_config.json:66`, `:75` — the `figma` manual template (`figma-developer-mcp@latest --stdio`)
- `AI Systems/Product Owner/.utcp_config.json:16`, `:25` — the `clickup_official` manual template (`npx -y mcp-remote https://mcp.clickup.com/mcp`)
- `AI Systems/Product Owner/mcp-chrome-devtools/README.md:95`, `:136`
- `AI Systems/Product Owner/mcp-chrome-devtools/assets/utcp-chrome-devtools-manuals.md:53`, `:69`, `:93`, `:115`
- `AI Systems/Product Owner/mcp-chrome-devtools/INSTALL-GUIDE.md:73`, `:81`, `:359`, `:373`, `:385`, `:933`
- `AI Systems/Product Owner/manual-testing-playbook/manual-testing-playbook.md:28`, `:36-44`, `:56`
- `AI Systems/Product Owner/manual-testing-playbook/hub-routing/` — 7 scenario files enumerated on disk
- `AI Systems/Product Owner/sk-product-owner/SKILL.md:288-292`, `sk-product-owner/manual-testing-playbook/` — 69 markdown files enumerated
- `AI Systems/Product Owner/mcp-click-up/**` and `mcp-figma/**` — manual/tool-name vocabulary sampled by frequency
- `AI Systems/Product Owner/vendor.json` — `mcp-chrome-devtools`, `mcp-code-mode`, `mermaid-extract`, `code-mode-launcher` entries

## Findings — New

### P0 Findings

None.

### P1 Findings

1. **The vendored chrome-devtools package documents two manuals the Product Owner config never registers, so every parallel-instance scenario cites a manual that does not exist** — `AI Systems/Product Owner/mcp-chrome-devtools/README.md:95` — The vendored README states as fact that "the `chrome_devtools_1` and `chrome_devtools_2` manuals in `.utcp_config.json` pin `chrome-devtools-mcp@0.26.0` with `--isolated=true`", and repeats at `:136` that "the MCP path registers `chrome-devtools-mcp@0.26.0` entries with `--isolated=true`". The registration that actually exists carries exactly one chrome manual, `chrome_devtools_live`, with `--autoConnect` and no `--isolated=true` (`AI Systems/Product Owner/.utcp_config.json:49`, args at `:57`). `assets/utcp-chrome-devtools-manuals.md:53` goes further and resolves the contradiction in the wrong direction — "the live registration pins the version. The live config wins" — while listing three separate `chrome_devtools_1`/`chrome_devtools_2`/`chrome_devtools_3` JSON blocks at `:69`, `:93` and `:115` that appear in no config on disk. Everything the package ships for parallel work depends on the missing pair: `feature-catalog/mcp-parallel-instances/dual-instance-parallel.md`, `manual-testing-playbook/mcp-parallel-instances/dual-instance-parallel.md`, `page-context-isolation.md`, `close-and-select-page.md` and `multi-tab-same-instance.md`. A tester following those scenarios is told to call `chrome_devtools_1.*` and `chrome_devtools_2.*`; Code Mode resolves manual names from `.utcp_config.json`, so both calls fail on an unregistered manual before any assertion runs. The single registered manual is the *live* one, which attaches to the user's own Chrome via `--autoConnect` — the opposite of the isolated-instance contract the parallel scenarios assert (`INSTALL-GUIDE.md:385` frames `chrome_devtools_live` as an *optional third* entry for signed-in work, not the only one). The scenario set therefore cannot pass as written, and the one path that can run mutates the user's real browser session instead of an isolated one.
   Finding class: `contract_drift`
   Scope proof: Every cited file is inside the declared review target; `.utcp_config.json` was read whole (4 `manual_call_templates`, none named `chrome_devtools_1`/`_2`/`_3`), and both vendored claims were read at the cited lines.
   Affected surface hints: `AI Systems/Product Owner/.utcp_config.json`, `AI Systems/Product Owner/mcp-chrome-devtools/README.md`, `AI Systems/Product Owner/mcp-chrome-devtools/assets/utcp-chrome-devtools-manuals.md`, `AI Systems/Product Owner/mcp-chrome-devtools/feature-catalog/mcp-parallel-instances/`, `AI Systems/Product Owner/mcp-chrome-devtools/manual-testing-playbook/mcp-parallel-instances/`
   Case: An operator runs the `dual-instance-parallel` playbook scenario to verify context isolation. It calls `chrome_devtools_1.navigate` and `chrome_devtools_2.navigate`; no manual with either name is registered, so both calls raise an unknown-manual error and the scenario reports FAIL against a product defect that does not exist. If the operator adapts the scenario to the one registered manual, both "instances" are the same `--autoConnect` session on their real Chrome, which is the isolation the scenario is meant to prove absent.
   ```json
   {"type":"P1","claim":"The vendored chrome-devtools README and manual asset describe a two/three-manual isolated registration in .utcp_config.json that the Product Owner config does not contain; the parallel-instance feature catalog and playbook scenarios depend on manuals that do not exist.","evidenceRefs":["AI Systems/Product Owner/.utcp_config.json:49","AI Systems/Product Owner/.utcp_config.json:57","AI Systems/Product Owner/mcp-chrome-devtools/README.md:95","AI Systems/Product Owner/mcp-chrome-devtools/README.md:136","AI Systems/Product Owner/mcp-chrome-devtools/assets/utcp-chrome-devtools-manuals.md:53","AI Systems/Product Owner/mcp-chrome-devtools/assets/utcp-chrome-devtools-manuals.md:69","AI Systems/Product Owner/mcp-chrome-devtools/assets/utcp-chrome-devtools-manuals.md:115","AI Systems/Product Owner/mcp-chrome-devtools/INSTALL-GUIDE.md:385"],"counterevidenceSought":"Searched for a second config file that could carry the missing manuals (no other .utcp_config.json exists in the target); checked whether .mcp.json or opencode.json registers chrome_devtools_1/2 (grep over both found no such name); checked whether README is framed as an example rather than a statement of fact (:95 and :136 both use indicative present tense about 'the manuals in .utcp_config.json').","alternativeExplanation":"The vendored package is a byte-identical copy of the upstream Skilled packet, and upstream's own reference deployment registers the two isolated manuals; the Product Owner's single-live-manual config is a deliberate simplification made after vendoring. Under this reading the drift is in the vendored docs, not in the config, and the fix is a local override note rather than a config change.","finalSeverity":"P1","confidence":"high","downgradeTrigger":"Downgrade to P2 if a Product Owner config outside the declared target registers chrome_devtools_1 and chrome_devtools_2, or if the parallel-instance scenarios are shown to resolve manual names from the package's own asset file rather than from .utcp_config.json."}
   ```

### P2 Findings

2. **Code Mode registration mixes a pinned package with a floating `@latest` and an unversioned remote fetch, so the reviewed artifact is not the one that runs** — `AI Systems/Product Owner/.utcp_config.json:75` — `chrome_devtools_live` pins `chrome-devtools-mcp@0.26.0` (`:57`), while the `figma` template runs `npx -y figma-developer-mcp@latest --stdio` (`:75`) and `clickup_official` runs `npx -y mcp-remote <url>` with no version at all (`:25`). The rest of the system takes reproducibility seriously: `vendor.json` records a `base_commit` per vendored package plus a sha256 per file, and `INSTALL-GUIDE.md:359`/`:373`/`:385` consistently pin the chrome version in prose. Only the two `npx` templates resolve whatever upstream published that morning. The consequence is narrow but real: `mcp-figma`'s `figma_get_figma_data` contract and the `clickup_official` tool catalog are validated against the vendored copies, and `@latest` silently allows the live manual to diverge from the contract the catalog documents.
   Finding class: `reproducibility_gap`
   Scope proof: `.utcp_config.json` read whole; all four `manual_call_templates` inspected, and `chrome-devtools-mcp@0.26.0` confirmed as the only pinned argument in the file.
   Affected surface hints: `AI Systems/Product Owner/.utcp_config.json`, `AI Systems/Product Owner/vendor.json`, `AI Systems/Product Owner/mcp-figma/SKILL.md`, `AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md`
   Case: `figma-developer-mcp` publishes a breaking rename of `get_figma_data` between two runs of the same reviewed release. Nothing in the repository changes, every gate still passes against the vendored `mcp-figma` copy, and the live figma manual no longer exposes the tool that `mcp-figma`'s catalog and playbook scenarios call.
   Finding class: `reproducibility_gap`
   Scope proof: as above.
   Affected surface hints: as above.

## Traceability Checks

- **core `spec_code`** — partial. The hub's declared companion set at `SKILL.md:59` and `:103` names `changelog/`, `manual-testing-playbook/` and `benchmark/`; all three exist. Within this pass the spec-to-code check is limited to the playbook and the vendored registration surface.
- **core `checklist_evidence`** — partial. Playbook execution policy at `manual-testing-playbook/manual-testing-playbook.md:9` ("every scenario runs against the live `product-owner` routing contract, with no mocks") is honoured by the 7 hub-routing scenarios; it is *not* satisfied for the vendored packages' scenarios once their manuals are unregistered (finding 1).
- **overlay `playbook_capability`** — partial, and the source of finding 1. Playbook capability claims were checked against the registration that backs them: the hub's own 7 scenarios (MT-001..MT-007, `manual-testing-playbook.md:36-44`) map one-to-one onto the 7 files on disk, while `mcp-chrome-devtools/manual-testing-playbook/mcp-parallel-instances/` maps onto manuals absent from `.utcp_config.json`.
- **overlay `feature_catalog_code`** — partial. `mcp-chrome-devtools/feature-catalog/mcp-parallel-instances/*.md` (6 entries) documents capabilities whose backing manuals are unregistered; `mcp-chrome-devtools/feature-catalog/dom-and-screenshot/`, `console-and-network/` and `protocol-discovery/` map onto the single live manual and are unaffected.
- **overlay `skill_agent`** — unchanged from iteration 1; no agent definition in this surface.
- **overlay `agent_cross_runtime`** — notApplicable; no agent definition in this surface.

## Integration Evidence

- `AI Systems/Product Owner/.utcp_config.json` is the Code Mode registration consumed at runtime; it is the integration point between every vendored MCP package and the host agent.
- `AI Systems/Product Owner/vendor.json` is the only record of what was vendored and from which `base_commit`; `scripts/vendor-sync.py` is the producer that reads and verifies it (established in iteration 2, not re-read here).
- `AI Systems/Product Owner/manual-testing-playbook/manual-testing-playbook.md:20` names `benchmark/reports/<dated-run-label>/` as the persistence target for scenario outcomes; `benchmark/` is in scope but its runner was not re-read this pass.

## Edge Cases

1. **Vendored-copy ownership vs Product Owner ownership.** `vendor.json` records `mcp-chrome-devtools.upstream_path: .skilled/skills/mcp-tooling/mcp-chrome-devtools` with `base_commit a58f9220…`, so `README.md:95` and `assets/utcp-chrome-devtools-manuals.md` are upstream text, not hand-authored drift. Finding 1 is therefore filed against the *seam* (a vendored doc asserting a fact about a locally owned config), not against the vendored file as a defect. Fixing the vendored text locally would be overwritten by the next `vendor-sync.py` run; the durable fix is local: register the isolated manuals, or add a local override note the sync never touches.
2. **`.utcp_config.json` and `.env`.** The config declares `load_variables_from` a `.env` file and the figma template interpolates `${FIGMA_API_KEY}`. The `.env` file was never opened and no secret value was read; only the variable *name* is cited, which is already public in the config.
3. **Whether `@latest` is intentional (finding 2).** `figma-developer-mcp` has no version pinned anywhere else in the repository, so there is no second artifact proving an intended pin. Kept at P2 with a downgrade-to-non-finding trigger rather than raised.
4. **`vendor.json` exclude-list asymmetry.** `mcp-code-mode` carries an `exclude` array (`node_modules`, `dist`, `mcp-server/README.md`, `graph-metadata.json`) while `mcp-chrome-devtools`, `mcp-aside-devtools` and `mcp-figma` carry none, and `mcp-code-mode` alone ships `leaf-manifest.json`/`leaf-aliases.json`/`leaf-manifest.config.json`. Two readings — a genuine per-package difference, or a stale exclude that silently drops a file the package needs — cannot be separated without running `vendor-sync.py --verify` against the upstream tree, which is outside this iteration's read-only budget. Recorded as open, not as a finding.
5. **Iteration number.** The state log carried 2 `type:"iteration"` records while the dispatch named iteration 8 of 10 with iterations 3-9 running in parallel. Per the dispatch contract the assigned number was used; the JSONL-derived value is not authoritative under fan-out.

## Confirmed-Clean Surfaces

- **"The 68 artifact scenarios" (`sk-product-owner/SKILL.md:290`) is accurate.** `sk-product-owner/manual-testing-playbook/` holds 69 markdown files: 1 index plus 68 scenario files across 12 folders (`project-backlog-modes`, `project-document-modes`, `project-flow-modes`, `project-identity`, `project-interactive-routing`, `project-story-modes` and their six `skill-*` counterparts).
- **The hub playbook's self-description matches its own contents.** `manual-testing-playbook.md:28` claims 7 scenario files and 41 gold rows in `benchmark/hub-routing-cases.json`; all 7 files (`MT-001``..``MT-007`) exist under `hub-routing/` and the table at `:36-44` lists exactly those ids.
- **`clickup_official` is the manual name the clickup package itself uses** — 268 occurrences across `mcp-click-up/**/*.md`, with tool calls in `clickup_official.{tool}` form. No name drift between `.utcp_config.json:16` and the package docs.
- **The `figma` manual name matches the figma tool vocabulary** — `figma_get_figma_data`, `figma_download_figma_images` resolve under the registered `figma` manual. Only the version pin is at issue (finding 2), not the namespace.
- **`sk-create-figjam` carries no manual registration of its own**, so its figma dependency is entirely via the hub's `mcp-figma` packet; no duplicate or conflicting registration exists to drift.
- **Every vendored package directory listed in scope exists and carries `SKILL.md`, `README.md` and `ROUTER.md`** (`mcp-click-up`, `mcp-aside-devtools`, `mcp-chrome-devtools`, `mcp-code-mode`, `mcp-figma`, `sk-create-figjam`).

## Ruled Out

- **`sk-product-owner/SKILL.md:290` "68 scenarios" as a stale count** — ruled out; 69 files minus the index is 68.
- **The hub playbook claiming scenarios it does not ship** — ruled out; 7 declared, 7 on disk.
- **Manual-name drift between `.utcp_config.json` and the clickup package** — ruled out; `clickup_official` is used consistently, 268 times.
- **Manual-name drift for figma** — ruled out; the `figma` namespace matches the `figma_*` tool vocabulary.
- **`sk-create-figjam` registering a competing figma manual** — ruled out; the package carries no manual registration.
- **A second `.utcp_config.json` in the target carrying the isolated chrome manuals** — ruled out; the target has exactly one, with four templates.
- **Chrome version pin drift as the defect** — ruled out; `chrome-devtools-mcp@0.26.0` in `.utcp_config.json:57` matches every pinned reference in `INSTALL-GUIDE.md` and `assets/utcp-chrome-devtools-manuals.md`. The drift is the *manual set*, not the version (finding 1).

## Next Dimension

**Security**, on the same operator focus where it meets this pass: the `npx`-launched manuals are supply-chain surface (three of four templates execute a network-fetched package), and `${FIGMA_API_KEY}` interpolation from `.env` is the one secret path in the reviewed config. Carried forward unresolved: the `vendor.json` exclude-list asymmetry (edge case 4) and whether `doctor:overlay` plus repinning could subsume `scripts/vendor-sync.py`.

Review verdict: CONDITIONAL