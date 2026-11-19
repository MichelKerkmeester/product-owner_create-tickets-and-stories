# Review Iteration 007

## Dispatcher

- Mode: review
- Dimension: maintainability
- Agent: @deep-review (LEAF, single iteration)
- Run: 054-po-system-deep-review, session `2026-11-10T20:08:17Z`, generation 1, lineage `new`
- Budget profile: `verify` (11 tool calls used of soft max 12)
- **Iteration-number mismatch (edge case):** dispatch assigned iteration 7 and pre-substituted `iteration-007.md` / `iter-007.jsonl`, while the state log holds 2 `type:"iteration"` records, which derives iteration 3. This iteration is one of seven parallel workers (3–9) on disjoint focuses, so the dispatcher-assigned number is the collision-free one and is used. The JSONL-derived 3 is already owned by a sibling worker; using it would overwrite another iteration's artifact.

## Files Reviewed

- `AI Systems/Product Owner/vendor.json` — full manifest structure (7 packages, 529 file hashes, per-package `include`/`exclude`/`base_commit`)
- `AI Systems/Product Owner/scripts/vendor-sync.py` — header contract, path containment, exclude/include handling, copy and status paths ([SOURCE: AI Systems/Product Owner/scripts/vendor-sync.py:1-56])
- `AI Systems/Product Owner/scripts/README.md`, `README.md`, `AGENTS.md`, `SYNC.md`, `USER-GUIDE.md` — cross-reference grep for overlay vocabulary
- `.skilled/commands/doctor/overlay.md` — router contract, targets `status|apply|repin`, flag ownership
- `.skilled/skills/system-skilled-doctor/SKILL.md` — owned-command boundary
- `.skilled/skills/system-skilled-doctor/references/overlays.md` — overlay folder layout, five sync states, engine refusals
- `.skilled/commands/doctor/scripts/overlay-engine.cjs` — constants, `--root` model, repin diff scoping
- `.skilled/skills/mcp-code-mode/` upstream tree, compared against the vendored copy

## Findings - New

### P0 Findings

None.

### P1 Findings

None this iteration; two P1 findings from iterations 1–2 remain active and are carried, not re-reported.

### P2 Findings

1. **The only `exclude` list in `vendor.json` mixes build output with upstream content and records no rationale** -- `AI Systems/Product Owner/vendor.json` (`mcp-code-mode.exclude`) -- The manifest excludes `["node_modules", "dist", "mcp-server/README.md", "graph-metadata.json"]` from hashing, copying and comparison. `node_modules` and `dist` are build output and belong there. `graph-metadata.json` is a real file in the upstream tree (`.skilled/skills/mcp-code-mode/graph-metadata.json`) and is absent from the vendored copy, so a full-tree coverage reading reports 529/529 files present and 0 drift while the vendored package is structurally short of upstream. Nothing in `vendor.json` distinguishes "generated, correctly skipped" from "upstream content, deliberately dropped", so a reader cannot audit which one applies.
   Finding class: documentation/coverage gap in a contract artifact.
   Scope proof: read-only inspection of `AI Systems/Product Owner/vendor.json` and `ls .skilled/skills/mcp-code-mode/`; no target file modified.
   Affected surface hints: `AI Systems/Product Owner/vendor.json` (`mcp-code-mode` entry), `scripts/vendor-sync.py` exclude docstring ([SOURCE: AI Systems/Product Owner/scripts/vendor-sync.py:24-28]), `scripts/README.md`.
   Case: an operator regenerates or hand-authors `graph-metadata.json` upstream, runs `status`, and reads a clean 0-drift result because the file is not in the hash set at all; the vendored `mcp-code-mode/` never receives it and nothing reports the gap.
2. **Two independent vendor-sync mechanisms coexist with disjoint verbs and zero cross-reference in any Product Owner document** -- `AI Systems/Product Owner/scripts/vendor-sync.py` vs `.skilled/commands/doctor/scripts/overlay-engine.cjs` -- `vendor-sync.py` (608 lines, plus the 352-line suite exercised by the `vendor sync tests` gate) owns byte-identity, three verbs (`status|pull|push`) and a per-file sha256 record. `/doctor:overlay` owns divergence reconciliation, `status|apply|capture|repin|rollback` and a five-state model (`in-sync`, `overlay-edited`, `live-edited`, `both-changed`, `upstream-moved`) keyed on a pinned upstream commit plus `overlay-manifest.json` and `sync-state.json`. A grep of `scripts/README.md`, `README.md`, `AGENTS.md`, `SYNC.md` and `USER-GUIDE.md` finds no mention of `doctor:overlay`, `overlay-engine`, `skilled-overlays` or `overlay-manifest`, so the handle a maintainer reads first names only `pull`.
   Finding class: documentation/maintainability gap across two shipped mechanisms.
   Scope proof: read-only greps and reads across the named files; no target file modified.
   Affected surface hints: `AI Systems/Product Owner/scripts/README.md`, `AI Systems/Product Owner/README.md`, `AI Systems/Product Owner/AGENTS.md`, `AI Systems/Product Owner/SYNC.md`, `AI Systems/Product Owner/USER-GUIDE.md`, `.skilled/skills/system-skilled-doctor/references/overlays.md`.
   Case: a maintainer hand-edits a vendored file to fix an upstream bug, reads `scripts/README.md` for the safe path, and finds only `pull` — the overlay vocabulary that describes exactly this situation (`live-edited`, `apply --capture`) never appears, so the edit is either pushed upstream blind or lost on the next re-copy.

## Operator Focus Analysis: can `/doctor:overlay` + repin replace `scripts/vendor-sync.py`?

Answer: **no, not as the engine stands**, and the four blockers are structural rather than effort-sized.

Verified state on disk: all 7 packages are byte-identical to their recorded hashes — 529 of 529 files present, 0 missing, 0 drift. There are therefore **no local overlays to protect today**; the overlay state machine has no consumer in this repository right now.

| Blocker | Evidence |
|---|---|
| Wrong tree model | The engine is scoped to a vendored *Skilled* tree: `VENDOR_ROOT = '.skilled'` and `repin` computes its change set as `diffNames(..., [VENDOR_ROOT])`. `AI Systems/Product Owner/` has no `.skilled/` at all; it vendors seven packages into peer folders (`mcp-click-up/`, `mcp-aside-devtools/`, `mcp-chrome-devtools/`, `mcp-code-mode/`, `mcp-figma/`, `scripts/vendored/code-mode/`, `sk-create-figjam/scripts/vendored/`). (`overlay-engine.cjs:73`, `:2606`) |
| One pin, seven pins | Overlay/repin moves one tree to one commit. `vendor.json` records a *different* `base_commit` per package (`mcp-code-mode` `ab14c677`, `code-mode-launcher` `60fb9fe2`, `mcp-aside-devtools` `6a619da8`, `mcp-chrome-devtools` `a58f9220`), because each package last moved at its own time. Collapsing them means re-pinning packages that did not change. |
| Sub-package vendoring has no analog | Two packages are file subsets — `code-mode-launcher` (`include: mcp-code-mode-launcher.cjs, lib/node-engine-resolver.cjs` from `.skilled/bin`) and `mermaid-extract` (`include: mermaid_extract.py` from `sk-design-diagram/scripts`). Repin replaces whole trees; the `include` list exists precisely so a push never disturbs the sibling files. |
| No upstream-write verb | `vendor-sync.py push` writes into the upstream working tree so a local fix can travel to Skilled. Overlay's `apply --capture` moves a live edit into the *local* overlay folder — a holding pen, not an upstream push. Adopting overlay would silently delete the outbound half of the workflow. |

What overlay would genuinely *add* here is the one thing `vendor-sync.py` does not model: a named state for "the local copy diverged", with `apply --capture` to keep the edit and `repin --rollback` to undo a bad move ([SOURCE: .skilled/skills/system-skilled-doctor/references/overlays.md:40]). Whether `pull` currently refuses to overwrite a locally-modified file, or overwrites it because `status` merely *reports* drift at exit 1, was not reached inside this iteration's budget. That single read decides whether the gap is theoretical (status gates the workflow) or a real data-loss path (pull runs regardless). It is carried to Next Focus as required evidence rather than reported as a finding, because it is unverified.

Cheapest simplification available without adopting the overlay engine: vendor the seven packages under one `skilled-overlays.json` + `overlay-manifest.json` pair *if* PO were ever converted to vendoring the whole Skilled tree — a much larger structural move — or, far smaller, document the two mechanisms against each other and make `vendor.json` self-describing per exclusion. Finding 2 and finding 1 respectively.

## Traceability Checks

- **spec_code** — `vendor.json` is a hand-authored contract with no spec carrying it; the review target names it explicitly, and `scripts/vendor-sync.py` is the only implementation that reads it. No spec-side drift found in scope.
- **checklist_evidence** — the vendored-package sync question in the operator focus is answered above with four named blockers, each tied to a file and line; the "zero overlays today" claim rests on a computed hash comparison over all 529 recorded files, not on prose.
- **skill_agent** — `@deep-review` LEAF boundary held: no sub-agent, no Task tool, no delegation.
- **agent_cross_runtime** — no runtime-mirror file was read as authority or edited; `.skilled/commands/doctor/overlay.md` and the `system-skilled-doctor` packet were read as upstream contracts only.
- **feature_catalog_code** — not exercised this iteration; the vendored `feature-catalog/` trees are byte-identical copies and were covered by the hash comparison rather than re-read.
- **playbook_capability** — not exercised; `manual-testing-playbook/` copies are also covered by the 529-file hash comparison.

## Integration Evidence

- `/doctor:overlay` contract: `.skilled/commands/doctor/overlay.md` §2 owned assets, §3 mode routing (targets `status|apply|repin`, flag ownership table).
- Overlay engine contract: `.skilled/commands/doctor/scripts/overlay-engine.cjs:24-39` usage block, `:61-67` setting/manifest/lock/state constants, `:73` `VENDOR_ROOT`.
- Skill ownership boundary: `.skilled/skills/system-skilled-doctor/SKILL.md` §1 owns `/doctor:overlay`, explicitly *does not* own `sk-code`/`sk-doc`/`git` doctor commands.
- Gate wiring: `vendor sync tests` gate → `scripts/tests/test_vendor_sync.py` (verified as a real suite in iteration 2, ruled out there as a cannot-fail check).

## Edge Cases

- **Iteration-number disagreement** (dispatch 7 vs JSONL-derived 3): resolved to 7 for the reason under Dispatcher; recorded rather than silently reconciled.
- **Verdict-mapping ambiguity:** the pack text maps the verdict to this iteration's new findings, while the `@deep-review` contract maps it over *active* findings and forbids downgrading a carried P1. The contract governs; the two carried P1 findings from iterations 1–2 therefore hold the verdict at CONDITIONAL even though this iteration raised only P2. Prior iterations took the same reading.
- **`exclude` intent is genuinely ambiguous** for `graph-metadata.json`: it exists in the `.skilled` upstream tree, but `.skilled` is a **symlink** into the Skilled checkout whose contents are not git-tracked from this repository (`git ls-files .skilled` → 0 entries, `check-ignore` → "beyond a symbolic link"), so whether that file is hand-authored or build-generated could not be settled here. Finding 1 is filed at P2 with an explicit downgrade trigger for that reason, and a downgrade to "correct behaviour, document it" is the expected outcome if it proves generated.
- **`pull`-overwrites-drift unverified** — carried to Next Focus as required evidence; not converted into a finding and not treated as a pass.

## Ruled Out

- **Replacing `vendor-sync.py` with `/doctor:overlay` + `repin`**: ruled out with four named blockers (tree model, one-pin-vs-seven-pins, include-list packages, missing upstream-write verb). Not an effort question.
- **A vendored copy currently carrying local overlays**: ruled out — 0 drift and 0 missing across 529 files in all 7 packages.
- **`exclude` and `include` set on the same package** (which the script refuses): ruled out — `vendor.json` respects the mutual exclusion at [`AI Systems/Product Owner/scripts/vendor-sync.py:357`.
- **Vendored copies missing recorded files**: ruled out — every one of the 529 manifest entries resolves on disk.
- **`overlay-manifest.json` / `.skilled-overlays.json` present in Product Owner and pointing nowhere**: ruled out — neither file exists in the target, consistent with the engine being unused here.
- **`scripts/vendored/code-mode` and `sk-create-figjam/scripts/vendored` as undocumented drop points**: ruled out — both are `include`-scoped manifest packages with recorded commits.

## Confirmed-Clean Surfaces

- `vendor.json` path containment: `local_path`, `upstream_path`, every `include` and `exclude` entry is validated beneath its root, absolute paths and `..` parts are setup errors, and the local copy must resolve inside the repository ([SOURCE: AI Systems/Product Owner/scripts/vendor-sync.py:343-367]).
- Symlink refusal on both sides, so a hash can never claim byte equality a clone cannot reproduce ([SOURCE: AI Systems/Product Owner/scripts/vendor-sync.py:151]).
- `include`-scoped copies are file-by-file, so a push never disturbs the sibling files upstream ([SOURCE: AI Systems/Product Owner/scripts/vendor-sync.py:415-420]).
- Excluded local entries are carried into a replaced copy, so a local build survives a `pull` ([SOURCE: AI Systems/Product Owner/scripts/vendor-sync.py:381-392]).
- `upstream_dirty` is consulted through `git status --porcelain` scoped to the package, so a push reads the same working-tree signal the operator sees ([SOURCE: AI Systems/Product Owner/scripts/vendor-sync.py:222-236]).
- The overlay engine's refusal set is sound where it applies: held lock is never auto-cleared, `.env` is never read even when a manifest entry names it, and `apply` writes nothing while `both-changed` or `upstream-moved` is present.

## Next Focus

- **Dimension:** maintainability (continue), rotating to security on the next iteration.
- **Focus area:** the `pull` guard question — read `vendor-sync.py`'s `pull` implementation end to end and determine whether a locally-modified file is refused or overwritten, then decide whether that is a P1 data-loss path or a clean gate. Second: settle whether `graph-metadata.json` and `mcp-server/README.md` are build-generated in Skilled, which closes or downgrades finding 1.
- **Reason:** this iteration proved the two mechanisms cannot merge and left exactly one unverified behavioural question that decides a severity. Closing it is cheaper than opening a new surface.
- **Rotation status:** `maintainability` now has one pass with its central question answered; `security` and `traceability` remain queued per the strategy and are untouched by this iteration except for the traceability checks above.
- **Blocked/productive carry-forward:** productive — the overlay analysis is complete and needs no re-entry; do not re-derive the four blockers. The `.skilled`-is-a-symlink finding is fresh context worth carrying.
- **Required evidence:** `vendor-sync.py` `pull` command body and its pre-write local-drift check; `git -C .skilled/skills/mcp-code-mode log -- graph-metadata.json` or an equivalent provenance read.
- **Recovery note:** not applicable; the iteration ran clean at 11 of 12 budgeted calls, with discovery deliberately stopped to protect the write phase.

Review verdict: CONDITIONAL
