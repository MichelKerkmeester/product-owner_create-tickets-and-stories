# Iteration 001 — Hub Routing and the Backlog Packet

## Dispatcher

- Mode: `review`
- Dimension: `correctness`
- Target agent: `@deep-review` (LEAF, single iteration)
- Review target: `AI Systems/Product Owner` (hub + nested packets)
- Budget profile: `verify` (discovery 16 calls incl. 3 verification rereads)
- Iteration source: JSONL-derived iteration 1 (dispatch said 1; agreement confirmed)

## Files Reviewed

- `AI Systems/Product Owner/SKILL.md:1-103` (frontmatter, layout, ALWAYS/NEVER, references)
- `AI Systems/Product Owner/ROUTER.md:1-145` (intent model, stage one rules, `## 3. MACHINE ROUTER`, compiled routing)
- `AI Systems/Product Owner/hub-router.json:1-262` (`routerPolicy`, `stageOneOrder`, `routerSignals`, `vocabularyClasses`)
- `AI Systems/Product Owner/mode-registry.json:1-182` (discriminator, extensions, four modes)
- `AI Systems/Product Owner/leaf-manifest.json:1-117` (88 leaves across 4 modes)
- `AI Systems/Product Owner/description.json:1-28`
- `AI Systems/Product Owner/sk-product-owner/SKILL.md:1-20` (frontmatter + `## 2. SMART ROUTING` presence)
- `AI Systems/Product Owner/sk-product-owner/ROUTER.md:22-40` (sibling router headings)
- `AI Systems/Product Owner/benchmark/gates/check_hub.py:1-26` (gate contract docstring)
- `AI Systems/Product Owner/benchmark/hub-routing-cases.json` (existence + gold-row claim)
- `AI Systems/Product Owner/changelog/v1.0.28.0.md:1-12` (release/version authority)
- Disk existence probes: `sk-create-figjam/ROUTER.md`, `mcp-figma/ROUTER.md`, `mcp-code-mode/leaf-manifest.json`, `scripts/`, `mcp-click-up/SKILL.md:302`

Not opened, per operator instruction: `AI Systems/Product Owner/.env`.

## Findings - New

### P0 Findings

None.

### P1 Findings

1. **Hub NEVER rule forbids the packet-local `ROUTER.md` that three packets already carry and the gate requires** — `AI Systems/Product Owner/SKILL.md:87` — The hub's `### NEVER` block states, in absolute form, "NEVER add a `ROUTER.md`, `graph-metadata.json` or leaf-manifest file inside a packet". All three workflow/transport packets ship exactly that file: `sk-product-owner/ROUTER.md`, `sk-create-figjam/ROUTER.md` and `mcp-figma/ROUTER.md`. The gate contract in `benchmark/gates/check_hub.py:23` describes the opposite rule as the supported shape: a packet *with* a sibling `ROUTER.md` keeps its machine router there under a final `## 3. MACHINE ROUTER`, and its `SKILL.md` Section 2 links that file. `sk-product-owner/ROUTER.md:40` is that heading. The hub also sends readers to the same file twice (`ROUTER.md:46`, `ROUTER.md:67`), and `SKILL.md:82` tells maintainers to keep "each workflow packet's routing in its `SKILL.md` Section 2", which is the `without one` branch only. A maintainer following `SKILL.md:87` deletes three files the gate asserts.

   Finding class: `contract_drift`
   Scope proof: `SKILL.md:87` is in the reviewed hub; all four corroborating files were read on disk this iteration.
   Affected surface hints: `AI Systems/Product Owner/SKILL.md` (rule text), `benchmark/gates/check_hub.py` (gate branch), the three packet `ROUTER.md` files, `.skilled/skills/sk-doc/sk-create-skill/` parent-hub contract if it is the upstream source of the `### NEVER` wording.

   Case: a maintainer reads `SKILL.md:87` as authoritative and removes `sk-product-owner/ROUTER.md` to "comply"; the packet loses its machine router `## 3` block, `check_hub.py` fails, and the hub's own `ROUTER.md:46`/`:67` pointers dangle.

   ```json
   {
     "type": "spec_mismatch",
     "claim": "SKILL.md:87 absolutely forbids a packet-local ROUTER.md, while three packets carry one and check_hub.py requires that shape for packets that have it.",
     "evidenceRefs": [
       "AI Systems/Product Owner/SKILL.md:87",
       "AI Systems/Product Owner/SKILL.md:82",
       "AI Systems/Product Owner/ROUTER.md:46",
       "AI Systems/Product Owner/ROUTER.md:67",
       "AI Systems/Product Owner/sk-product-owner/ROUTER.md:40",
       "AI Systems/Product Owner/benchmark/gates/check_hub.py:23"
     ],
     "counterevidenceSought": "Searched for a reading that reconciles the two: checked whether the NEVER targets a second/redundant router, whether the packet ROUTER.md files are legacy or generated, and whether SKILL.md scopes the rule to 'new' files. SKILL.md:82 speaks only of SKILL.md Section 2 routing, and SKILL.md:87 admits no exception clause; check_hub.py:23 makes the sibling file a supported branch rather than a violation.",
     "alternativeExplanation": "The NEVER intends 'do not add a router where the packet already routes in its SKILL.md Section 2', and the three packets are the exception the sentence failed to write.",
     "finalSeverity": "P1",
     "confidence": "high",
     "downgradeTrigger": "Downgrade to P2 if a conditional clause in the upstream sk-create-skill parent-hub contract states that the sibling ROUTER.md is the supported shape for packets that declare one, making SKILL.md:87 merely a truncated quotation of a rule the gate follows correctly."
   }
   ```

### P2 Findings

2. **`scripts/` is claimed as a declared repo-root-hub path but is absent from `repoPaths`** — `AI Systems/Product Owner/SKILL.md:69` — The layout block says "specs/ export/ claude project/ scripts/ — repository files, declared in the repo-root-hub extension". `mode-registry.json` `extensions.repo-root-hub.repoPaths` lists fourteen entries and none is `scripts`; the set is `AGENTS.md, Favicon.jpg, LICENSE, SYNC.md, benchmark, claude project, context, export, mcp-aside-devtools, mcp-chrome-devtools, mcp-code-mode, opencode.json, specs, vendor.json`. The drift runs both ways: `context` is in `repoPaths` but missing from the `SKILL.md:68-69` layout line, and `scripts/` (which holds `README.md`, `code-mode.cjs`, `tests/`, `vendor-sync.py`, `vendored/`) is on disk but not declared. A checker that skips hub entries by reading `repoPaths` therefore walks `scripts/` as skill content.

   Finding class: `registry_disk_drift`
   Scope proof: `repoPaths` read from `mode-registry.json:35-50`; `scripts/` confirmed present and enumerated on disk.
   Affected surface hints: `AI Systems/Product Owner/mode-registry.json` (`repoPaths`), `SKILL.md` layout block, skilled checkers that consume `repoPaths`.

   Case: a skilled checker or a future hub audit enumerates the hub's repo entries from `repoPaths` and reports `scripts/` as an undeclared skill-like folder, or conversely a maintainer trusts the layout block and assumes `scripts/` is already skipped.

3. **`ROUTER.md` names a parser script that does not exist anywhere in the repository** — `AI Systems/Product Owner/ROUTER.md:73` — The machine-router preamble says the block "is the source sk-create-skill's `leaf-route-replay.cjs` parses when it is run against this hub". A repository-wide `find -name 'leaf-route-replay*'` returns no match. The file at that directory that does exist is `generate-leaf-manifest.cjs`; `scripts/lib/leaf-resource-contract.cjs` also exists and is cited correctly at `ROUTER.md:19`. The parity work this sentence promises is actually carried by `benchmark/gates/check_leaf_map_parity.py:1-...` cited at `ROUTER.md:54`, so the outcome is covered by a different tool while the named one is a dead path in a package that is a vendored/pinned dependency (`.skilled/skills/sk-doc/`), which is where a rename would have landed.

   Finding class: `stale_cross_reference`
   Scope proof: name searched repository-wide this iteration; the two sibling `lib/` scripts were probed and resolve.
   Affected surface hints: `AI Systems/Product Owner/ROUTER.md`, `.skilled/skills/sk-doc/sk-create-skill/scripts/` (upstream of the rename), `benchmark/gates/check_leaf_map_parity.py` (the actual replay).

   Case: a maintainer changing a `RESOURCE_MAP` row tries to run the named parser to confirm the hub still dual-reads to canonical pairs, gets "MODULE_NOT_FOUND", and either skips the check or hand-audits the map.

4. **The `INSTALL-GUIDE.md` exclusion is justified by a `ROOT_RESOURCES` array the vendored packet does not have** — `AI Systems/Product Owner/ROUTER.md:19` — The sentence excludes a packet's `INSTALL-GUIDE.md` from the leaf contract because "it is never a leaf here: `mcp-click-up/SKILL.md` loads it from its own `ROOT_RESOURCES` on an install route". `mcp-click-up/SKILL.md` contains no `ROOT_RESOURCES` and no `rootResources`; its single mention of the guide is a plain reference-list link, `mcp-click-up/SKILL.md:302`, "the condensed top-level install front door at the packet root … and the router's INSTALL-intent target". The exclusion itself is sound, since the guide sits at the packet root outside `references/` and `assets/`, but the stated load mechanism is unbacked, so the one place that explains why the guide is not a leaf cannot be verified against the packet.

   Finding class: `unbacked_justification`
   Scope proof: `ROOT_RESOURCES`/`rootResources` grepped in `mcp-click-up/SKILL.md` (zero hits) and in `mcp-figma/SKILL.md` (zero hits); `INSTALL-GUIDE` grepped in the same file (one hit, line 302).
   Affected surface hints: `AI Systems/Product Owner/ROUTER.md`, `mcp-click-up/SKILL.md` reference list, `mcp-figma/SKILL.md` (same guide, same absence), `leaf-manifest.json` (the guide's correct absence from all four leaf sets).

   Case: an install-route request reaches the packet, the reader looks for `ROOT_RESOURCES` to confirm the guide is loaded outside the leaf contract, and finds a flat reference link instead, so the exclusions at `ROUTER.md:19` and the `leaf-manifest.json` shape look arbitrary.

## Traceability Checks

| Protocol | Level | Status | Evidence |
|---|---|---|---|
| `spec_code` | core | partial | Hub prose vs machine files: `stageOneOrder` (`hub-router.json:24-81`) and `RESOURCE_MAP` (`ROUTER.md:96-132`) agree with the prose at `ROUTER.md:27-37`; `DEFAULT_RESOURCE` vs `routerPolicy.defaultResource` are explicitly distinguished at `ROUTER.md:37`, so that near-miss is not drift. One prose/source mismatch recorded as finding 1. |
| `checklist_evidence` | core | partial | `SKILL.md` `### ALWAYS`/`### NEVER` (`:78-89`) checked line by line against disk: `:80` AGENTS.md exists, `:81` `mode-registry.json` + `ROUTER.md` + packet `SKILL.md` all exist, `:82` contradicted by `:87` (finding 1), `:83` generator `generate-leaf-manifest.cjs` confirmed present, `:88` `scripts/vendor-sync.py` confirmed present. |
| `skill_agent` | overlay | partial | Hub identity `product-owner` ↔ `description.json:2` ↔ `graph-metadata.json` single identity ↔ `mode-registry.json` four `workflowMode` values ↔ `SKILL.md:22-27` mode table ↔ `leaf-manifest.json` four modes: all four mode keys match exactly. |
| `agent_cross_runtime` | overlay | notApplicable | No agent definition in this surface; `AGENTS.md` bootstrap exists but is out of this iteration's dimension. |
| `feature_catalog_code` | overlay | notApplicable | No feature catalog in the hub; catalog mode belongs to the packet packets and was not in this focus. |
| `playbook_capability` | overlay | partial | `manual-testing-playbook/manual-testing-playbook.md` and `benchmark/` referenced at `SKILL.md:103`; both present. Playbook body not yet read against capabilities. |

## Integration Evidence

Exact surfaces touched by this iteration's findings:

- `AI Systems/Product Owner/benchmark/gates/check_hub.py` — the hub gate that owns the sibling-`ROUTER.md` branch (finding 1) and that `ROUTER.md:54` names as the stage one replay.
- `AI Systems/Product Owner/benchmark/gates/check_leaf_map_parity.py` — the FLOW-keyword replay named at `ROUTER.md:54`, which covers the parity duty finding 3 attributes to a missing script.
- `AI Systems/Product Owner/benchmark/hub-routing-cases.json` — gold rows replayed by both gates; present, not replayed this iteration.
- `.skilled/skills/sk-doc/sk-create-skill/scripts/lib/leaf-resource-contract.cjs` — the one contract boundary `ROUTER.md:19` names; resolves.
- `.skilled/skills/sk-doc/sk-create-skill/scripts/generate-leaf-manifest.cjs` — the generator `SKILL.md:83` requires; resolves.
- `.skilled/bin/compiled-route.cjs` — the compiled-routing front door `ROUTER.md:141` invokes; resolves.
- `.skilled/skills/system-skilled-doctor/` and `.skilled/commands/doctor/overlay.md` — named in the operator focus for the vendor-sync replacement question; not reached this iteration.

## Edge Cases

- **Dispatch/JSONL iteration agreement.** Dispatch said iteration 1 of 10; the state log holds a `config` record and an `iteration_start` record but no `type:"iteration"` record, so the JSONL-derived number is 1. No mismatch.
- **First-run absence.** `iterations/` and `deltas/` were empty; `deep-review-findings-registry.json` is the initial empty projection; `deep-review-strategy.md` is still the pristine template with unpopulated `[from config]` placeholders. Treated as `lineageMode=new`, not as corrupt state.
- **Path-resolution self-correction.** An initial probe resolved `.skilled/...` as `../../../` from the packet folder and reported three false misses. Re-probed from the repository root; `compiled-route.cjs`, `leaf-resource-contract.cjs` and `generate-leaf-manifest.cjs` all resolve, and only `leaf-route-replay.cjs` is genuinely absent. Finding 3 rests on the corrected probe.
- **`defaultResource` name collision.** `hub-router.json:18-21` and `ROUTER.md:77-80` both define a `defaultResource`/`DEFAULT_RESOURCE` with different values and different meanings. `ROUTER.md:37` calls the collision out explicitly, so this is a documented hazard rather than drift; recorded here so a later iteration does not re-raise it as a finding.
- **`description.json` `lastUpdated`.** `description.json:27` carries `2026-10-20T18:00:00Z` while the frontmatter `version` is `1.0.28.0` and `changelog/v1.0.28.0.md` is the newest entry. Timestamp staleness is not separately actionable because `SKILL.md:14` makes `version` the authority and `description.json` agrees with it.
- **`.env` not opened.** Per operator instruction, `AI Systems/Product Owner/.env` was neither read nor quoted; only its presence appears in the directory listing.

## Confirmed-Clean Surfaces

- **All 18 routed paths resolve.** Every `DEFAULT_RESOURCE` and `RESOURCE_MAP` path in `ROUTER.md:77-132` was probed on disk: 18/18 present, 0 missing.
- **All 88 leaf-manifest entries resolve.** All four modes' leaves (`mcp-click-up` 3, `mcp-figma` 6, `sk-create-figjam` 40, `sk-product-owner` 39) were probed against their `packet` field: 0 missing.
- **Version authority holds.** `SKILL.md:5` `1.0.28.0` = `hub-router.json:3` = `mode-registry.json:3` = `description.json:4` = `changelog/v1.0.28.0.md:9`, and that changelog is the newest entry in `changelog/`. `sk-product-owner/SKILL.md:5` `1.2.16.0` matches the version the same changelog announces.
- **Contract version parity.** `mode-registry.json:4` `resourceContractVersion: 1` = `leaf-manifest.json:116` `resourceContractVersion: 1`.
- **Registry preamble honesty.** `mode-registry.json:5` states the shared parent-hub contract requires an empty `toolSurface.bashAllowlist` where no shell command is approved, and all four modes carry `[]` (`:70`, `:104`, `:133`, `:166`).
- **Mode table parity.** `SKILL.md:22-27` names `sk-product-owner` and `sk-create-figjam` as `workflow`, `mcp-click-up` as `workflow` and `mcp-figma` as `transport`; `mode-registry.json:56/90/119/150` carries exactly those `packetKind` values, and the `transport-axis` extension names only `mcp-figma`.
- **Vendored-packet isolation.** `mode-registry.json:26` says the vendored packets carry no mode; the `vendored-packets` extension lists exactly `mcp-figma` and `mcp-click-up`, and `check_hub.py:19-21` enforces that the default is never one — the default is `sk-product-owner` (`hub-router.json:5`).
- **`mcp-code-mode` leaf-manifest exception is real.** `SKILL.md:64` and `:72` describe it as a vendored server that is not a workflow packet and therefore exempt from the no-leaf-manifest rule; `mcp-code-mode/leaf-manifest.json` exists, and `SKILL.md:87`'s rule covers packets, so this is not a second violation of finding 1.
- **Stage one ordering is self-consistent.** `hub-router.json:24-81` `stageOneOrder` has six rules in the order `SKILL.md:40` and `ROUTER.md:42` describe (commands → artifact request → opening signal → default artifact word → single signal → default), and the four worked examples at `ROUTER.md:43-44` follow from the verb/noun and alias classes as written.
- **`orderedBundle` is consistently declared never to form at stage one** in both `hub-router.json:15` and `ROUTER.md:51`, including the same FigJam-second-output exception.

## Ruled Out

- **Routed-file existence as a defect source.** 18/18 `RESOURCE_MAP` paths and 88/88 manifest leaves resolve; no dangling leaf, no phantom reference. Not a finding.
- **Version drift between hub authority files.** All four `1.0.28.0` carriers agree and the newest changelog matches. Not a finding.
- **`DEFAULT_RESOURCE` vs `routerPolicy.defaultResource` collision as drift.** Distinguished on purpose at `ROUTER.md:37` with `defaultResourceSemantics: fallback-only`. Not a finding.
- **Mode/packet kind mismatch.** `packetKind`, `backendKind`, `transport-axis` and the `SKILL.md` mode table agree across four modes. Not a finding.
- **`mcp-code-mode` leaf-manifest as a rule violation.** Exempted twice in the hub and genuinely not a packet. Not a finding.
- **`leaf-manifest.json` mode ordering differing from `hub-router.json.tieBreak`.** The manifest sorts by packet name because it is generated; `tieBreak` is a routing policy. Different purposes, no behavioral consequence.
- **`documentation`/`clarify` missing from `vocabularyClasses.artifact-request-nouns`** while present in `product-owner-artifacts`. Examined as a possible rule-2 gap: a request such as "write documentation for X" misses the artifact-request rule and lands on the single-signal rule instead, but both resolve to `defaultMode` `sk-product-owner`, so the outcome is identical. Cosmetic redundancy, not actionable at any severity.

## Next Focus

- **Dimension:** traceability
- **Focus area:** `AI Systems/Product Owner/sk-product-owner/` — `SKILL.md` `## 2. SMART ROUTING`, the sibling `ROUTER.md` `## 2. INTENT MODEL` and `## 3. MACHINE ROUTER`, plus `references/router-contract.md` and `references/routing.md` against the hub's stage two claims.
- **Reason:** finding 1 shows the hub's packet-router rules have drifted from what the packets and the gate actually implement. The backlog packet is the default mode and the one the hub delegates every unmatched request to, so its stage two contract is the highest-blast-radius unverified surface left in the routing chain.
- **Rotation status:** `correctness` D1 marked reviewed with this iteration's score; `traceability` (D3) opened next because two of the four findings are cross-reference integrity defects rather than logic errors.
- **Blocked/productive carry-forward:** none. No approach is exhausted; the stage two router has not been read yet.
- **Required evidence:** `sk-product-owner/ROUTER.md` machine-router block vs `sk-product-owner/references/router-contract.md` scoring table vs `SKILL.md` Section 2 markers, each cross-checked against `benchmark/router/` fixtures and `benchmark/gates/check_hub.py`.
- **Recovery note:** not applicable; iteration 1 ran clean.
- **Operator focus carried forward:** the vendored-packet sync question (`vendor.json`, `scripts/vendor-sync.py`, `doctor:overlay`, `system-skilled-doctor`) was not reached this iteration and stays on the frontier for a later iteration.

Review verdict: CONDITIONAL
