# Review Iteration 010 -- Final Pass

**Mode:** review | **Dimension:** correctness replay of every open finding plus cross-dimension sweep | **Iteration:** 10 of 10 (stop policy `max-iterations`)

## Dispatcher

`Resolved route: mode=review target_agent=deep-review`. Iteration number derived from the state log (9 prior `type:"iteration"` records) and confirmed against the dispatch value. This is the terminal pass: its job is not discovery but adjudication -- re-verify each of the 25 open findings against the files as they exist now, narrow or strengthen what the evidence supports, close what no longer holds, and sweep for anything nine passes missed.

Operator focus, addressed in this pass: drift, bugs and refinement opportunities across the whole Product Owner system; alignment with `sk-doc` (package shape, README, changelog, frontmatter, playbook and catalog modes) and `sk-code` (scripts and validators); and whether Skilled overlay/repinning (`/doctor:overlay`, `system-skilled-doctor`) could replace `scripts/vendor-sync.py`. The overlay question was closed with four named blockers in iteration 7; the `sk-doc`/`sk-code` alignment questions were answered across iterations 4 and 6. This pass adds the drift half: it confirms whether the findings accumulated against the system still describe the system, and it resolves the one item the strategy carried as **UNVERIFIED**.

`AI Systems/Product Owner/.env` was not opened or quoted.

## Files Reviewed

| File | Line(s) | Why |
|------|---------|-----|
| `AI Systems/Product Owner/SKILL.md` | 87 | NEVER rule that the ROUTER gate contradicts |
| `AI Systems/Product Owner/benchmark/gates/check_hub.py` | 61, 216-230 | packet-ROUTER requirement and its own carve-out comment |
| `AI Systems/Product Owner/benchmark/format/validate-output-format.cjs` | 1-40, 1718 | fork header, config block, console output |
| `AI Systems/z — Claude Project Sync Loop/validate-output-format.cjs` | 1-57 | upstream of the fork |
| `AI Systems/Product Owner/.utcp_config.json` | 75 | floating pin plus the registered manual set |
| `AI Systems/Product Owner/mcp-chrome-devtools/README.md` | 95 | unregistered manual claim |
| `AI Systems/Product Owner/mcp-chrome-devtools/references/cdp-patterns.md` | 412 | evidence-artifact commands |
| `AI Systems/Product Owner/mcp-code-mode/references/naming-convention.md` | 1 | second carrier of the unregistered manual names |
| `AI Systems/Product Owner/mcp-aside-devtools/references/discovery-fixture-2026-07-16.json` | 1 | third carrier, 156 occurrences |
| `AI Systems/Product Owner/.gitignore` | 28-45 | context/ and Python-cache boundaries |
| `AI Systems/Product Owner/context/README.md` | 1 | the carried-forward UNVERIFIED item |
| `AI Systems/Product Owner/graph-metadata.json` | 1-30 | hub-only graph identity |
| `AI Systems/Product Owner/USER-GUIDE.md` | 1-30 | reader-facing contract, version/count claims |

All 25 open-finding anchors were re-resolved in one sweep: 25/25 files exist, 25/25 cited lines are inside their files, 0 past-end, 0 moved.

## Findings -- New

### P0 Findings

None. No P0 is active and none was raised.

### P1 Findings

None new. The four active P1s were replayed and all four survive (see the refinement records below); none could be downgraded on current evidence.

### P2 Findings

None new. The 21 active P2s were replayed at anchor level and all survive.

## Replay -- refinements to active findings

1. **R10-REF-001 -- the ROUTER contradiction is total, not partial** -- `AI Systems/Product Owner/SKILL.md:87` -- The hub NEVER rule reads "**NEVER** add a `ROUTER.md`, `graph-metadata.json` or leaf-manifest file inside a packet". `check_hub.py:216` requires each packet to have `ROUTER.md`, `:222` fails the gate when a packet's `SKILL.md` Section 2 does not link it, `:226-228` fails on missing `router_state: active` frontmatter, and `:230` fails unless the file's last H2 is `## 3. MACHINE ROUTER`. The gate's own comment at `check_hub.py:61` carves the packet ROUTER out of `HUB_FILES` deliberately. On disk today, **7 of 7** packets carry a `ROUTER.md`, not the "three packets" the finding was filed with. The contradiction therefore covers every packet, and the NEVER rule is the stale side: the gate and the disk agree with each other, and only the prose disagrees.
Finding class: contract_drift
Scope proof: `SKILL.md:87` and `check_hub.py:216-230` are both inside the declared review target; the 7 on-disk `*/ROUTER.md` files were listed directly.
Affected surface hints: `AI Systems/Product Owner/SKILL.md`, `AI Systems/Product Owner/benchmark/gates/check_hub.py`, `AI Systems/Product Owner/sk-product-owner/ROUTER.md`, `AI Systems/Product Owner/mcp-figma/ROUTER.md`
Case: a maintainer follows `SKILL.md:87` and deletes a packet `ROUTER.md`; `benchmark/gates/check_hub.py` then fails the release gate on the same packet.

2. **R10-REF-002 -- the validator fork is a rewrite, not a stale copy** -- `AI Systems/Product Owner/benchmark/format/validate-output-format.cjs:1` -- The two files differ in 1425 lines over 1733 versus 1878 lines and share no hash (`efd072bb...` against `332b6286...`). The fork drops `require('./systems.cjs')` entirely and replaces the upstream source-perimeter model with a hardcoded `systemRoot = path.resolve(__dirname, '../..')` at `:38-40`, and it relocates `'use strict'` above the module banner. The upstream header block that explains the two modes, the artifact-purity rules and the deal rules is deleted from the fork. This strengthens the finding from "a diverged fork" to "the two validators no longer implement the same mode model", so a rule added to either one does not reach the other.
Finding class: duplicate_artifact_drift
Scope proof: both files were hashed and diffed in full this pass; both are named in `reviewScopeFiles`.
Affected surface hints: `AI Systems/Product Owner/benchmark/format/validate-output-format.cjs`, `AI Systems/z — Claude Project Sync Loop/validate-output-format.cjs`, `AI Systems/Product Owner/benchmark/format/run_fixtures.sh`
Case: a conciseness rule is fixed in the Sync Loop validator; the Product Owner release gate keeps enforcing the old behaviour and still reports a clean pass.

3. **R10-REF-003 -- the unregistered manual names reach three packets, not one** -- `AI Systems/Product Owner/mcp-chrome-devtools/README.md:95` -- `.utcp_config.json` registers exactly four `manual_call_templates` -- `clickup_official`, `aside`, `chrome_devtools_live`, `figma` -- and none is named `chrome_devtools_1` or `chrome_devtools_2`. The names the finding was filed against still appear in the chrome packet (README 9, `INSTALL-GUIDE.md` 47, `assets/utcp-chrome-devtools-manuals.md` 22, playbook 44), and they also appear in two packets the finding did not name: `mcp-code-mode/references/naming-convention.md` 25, `mcp-code-mode/INSTALL-GUIDE.md` 21, `mcp-code-mode/manual-testing-playbook/clickup-and-chrome-via-cm/chrome-navigate-screenshot.md` 13, and `mcp-aside-devtools/references/discovery-fixture-2026-07-16.json` 156. The fix is one rename across three packets; the blast radius was understated.
Finding class: producer_consumer_mismatch
Scope proof: the template list was parsed from `.utcp_config.json` and the occurrence counts recomputed across the target tree this pass.
Affected surface hints: `AI Systems/Product Owner/.utcp_config.json`, `AI Systems/Product Owner/mcp-chrome-devtools/`, `AI Systems/Product Owner/mcp-code-mode/`, `AI Systems/Product Owner/mcp-aside-devtools/`
Case: a reader follows a parallel-instance scenario that says to call `chrome_devtools_1`, and the running UTCP client has no manual of that name to dispatch to.

## Traceability Checks

| Protocol | Level | Status | Evidence |
|----------|-------|--------|----------|
| `spec_code` | core | partial | 25/25 open-finding anchors re-resolved with 0 stale paths and 0 past-end lines; the replay is an anchor-level check, and the four P1 magnitudes were re-read in full while the 21 P2 magnitudes were carried on verified anchors |
| `checklist_evidence` | core | pass | each surviving finding still cites the rule it breaks; the two load-bearing rule lines were re-read this pass (`SKILL.md:87`, `check_hub.py:61`) |
| `skill_agent` | overlay | notApplicable | no agent definition is defined by this surface |
| `agent_cross_runtime` | overlay | notApplicable | no runtime mirror belongs to this target; `.skilled/commands/doctor/overlay.md` was read in iteration 7 as an upstream contract only |
| `feature_catalog_code` | overlay | notApplicable | the hub ships no feature catalog and no Product Owner artifact routes to one |
| `playbook_capability` | overlay | partial | the hub playbook holds 7 declared scenarios against 7 files on disk; the chrome parallel-instance scenarios still cite manuals absent from the registered set, now known to extend into `mcp-code-mode`'s playbook |

## Integration Evidence

- `AI Systems/Product Owner/benchmark/gates/run_gates.sh` -- the release runner whose clean pass is finding 8's subject; its gate list was not re-executed this pass.
- `AI Systems/Product Owner/benchmark/format/run_fixtures.sh` -- the harness that points at the forked validator; it is the consumer side of R10-REF-002.
- `.skilled/skills/system-deep-loop/runtime/scripts/append-mode-event.cjs --mode review` -- the append gateway that recorded this iteration; it is the only writer of the state log.
- `.skilled/skills/sk-doc/sk-create-changelog/SKILL.md:10` -- the deprecated-placement rule cited by R4-P2-001; re-read to confirm the rule still states a global changelog under `.skilled/changelog`.

## Edge Cases

1. **The carried-forward UNVERIFIED item is now resolved clean.** The strategy listed as unverified the `.gitignore:34-37` claim that `context/.gitkeep` and `context/README.md` stay tracked, because the earlier check used a `/context/` pattern that cannot match a repo-relative path. Re-run as `git ls-files context`, both files are tracked, and `git ls-files --error-unmatch` accepts both. `.gitignore:34-37` ignores `/context/*` and negates the two exceptions exactly as its own comment says. The 60 KB reference file beside them, `context/BRAND INTEGRATION + COMMUNITIES 40c05799690c806da27bc5c0b1c2d58c.md`, is caught by `/context/*` and is therefore local-only. No finding; the item moves to Ruled Out.
2. **P2 replay depth is anchor-level, not magnitude-level, and is recorded as such.** Re-reading the magnitude of 21 P2s was not possible inside the iteration budget, so the P2s are carried as still-active on verified anchors rather than re-adjudicated. Carrying a finding forward does not downgrade it, and none is reported resolved.
3. **The R3-P1-001 replay narrows the finding's load-bearing half.** `cdp-patterns.md:412` still directs a HAR export to a repo-visible path with no redaction step, so the anchor holds. But a redaction rule does exist on the adjacent packet at `mcp-aside-devtools/SKILL.md:135`; it is the subject of R3-P2-002 and is weaker than its own catalog leaf. The P1's load-bearing half is therefore the **missing ignore boundary** for browser evidence artifacts, not the total absence of a redaction rule. Severity is unchanged because the artifact boundary is still absent.
4. **Budget.** Replaying 25 findings in one sweep used 12 tool calls before the first write, at the soft ceiling of 12 and one below the hard max of 13. The write phase is not discretionary, so this iteration's total exceeds the per-iteration call budget. Discovery was stopped at the ceiling rather than trimmed, and two cheaper checks that were planned -- re-parsing `mode-registry.json`'s `repo-root-hub` list for finding 2, and re-grepping `.gitignore` for `*.har` -- were dropped. Both findings remain active on anchors that were verified.
5. **Terminal pass under `stop_policy: max-iterations`.** `sessionId`, `generation` and `lineageMode` were read from the last canonical iteration record rather than assumed. Convergence is telemetry only here; the ratio below is recorded, not acted on.
6. **USER-GUIDE.md carries no version string and no numeric count claim** (grep for `1.0.2x`, `v1.x` and `N files|scenarios|entries|documents|modes|packets` returned nothing), so it cannot drift numerically against the hub. `graph-metadata.json` declares a single `product-owner` hub identity with empty `depends_on` and `conflicts_with`, matching `SKILL.md:72`'s claim that only the hub carries a graph manifest.
7. **No untrusted-content directive was found** in any file read this pass; the review targets were treated as data throughout.

## Confirmed-Clean Surfaces

- `context/` tracking boundary -- `.gitignore:34-37` and `git ls-files context` agree, and the private reference file is ignored.
- `graph-metadata.json` hub identity -- one manifest, one `product-owner` id, in agreement with `SKILL.md:72`.
- `USER-GUIDE.md` numeric claims -- none present, so none can drift.
- All 25 open-finding anchors -- every file exists and every cited line is in range.

## Ruled Out

- **`context/.gitkeep` and `context/README.md` as an untracked-but-claimed pair** -- ruled out; both are tracked and both are negated back in by `!` rules at `.gitignore:36-37`.
- **The 60 KB Notion export in `context/` as a packaging leak** -- ruled out; `/context/*` ignores it and it is absent from `git ls-files context`.
- **`USER-GUIDE.md` version drift** -- ruled out; it states no version and no count.
- **`graph-metadata.json` as a duplicate hub identity** -- ruled out; `SKILL.md:72` and the manifest agree that only the hub carries one.
- **A second `manual_call_templates` set somewhere in the target** -- ruled out again at the terminal pass; exactly four templates in exactly one `.utcp_config.json`.

## SCOPE VIOLATIONS

None. No would-be mutation outside the allowed write paths was required or attempted.

## Next Focus

- **Dimension:** terminal -- all four dimensions are complete (correctness replayed here, security at iteration 3, traceability at iteration 4, maintainability at iteration 9).
- **Focus area:** none; the loop reached `max-iterations` with 4 P1 and 21 P2 active.
- **Reason:** `stopPolicy: max-iterations` -- all 10 iterations run and convergence is telemetry only. Hand-off is to `/speckit:plan` for the four P1s, in the order R10-REF-001, R10-REF-002, R10-REF-003, then R3-P1-001.
- **Rotation status:** closed.
- **Blocked/productive carry-forward:** productive -- the three refinements are remediation-ready and each names the exact edit surface.
- **Required evidence:** none outstanding.
- **Recovery note:** budget edge case 4 above is the one process deviation; it did not change a finding.

Review verdict: CONDITIONAL
