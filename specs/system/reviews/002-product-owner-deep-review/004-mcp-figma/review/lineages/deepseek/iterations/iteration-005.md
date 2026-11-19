# Iteration 5 - Close-out pass (adversarial replay + unopened surfaces)

**Dimension:** maintainability / verification close-out
**Iteration:** 5 of 5 (terminal; `stopPolicy: max-iterations`)
**Target:** `AI Systems/Product Owner/mcp-figma/`, `vendor.json`, `scripts/vendor-sync.py`, plus the gates that guard them
**Route:** Resolved route: mode=review target_agent=deep-review, execution=single_review_iteration
**Sources read this iteration:** steer.md (lineage), every previously cited line re-opened, `feature-catalog/export/export.md`, `feature-catalog/render-and-create/render-and-create.md`, `feature-catalog/feature-catalog.md`, `changelog/v1.1.0.0.md`–`v1.1.3.0.md`, `mcp-servers/figma-cli/README.md`, `mcp-servers/figma-cli/setup.sh`, `mcp-servers/figma-mcp/README.md`, `scripts/tests/test_vendor_sync.py`, `benchmark/gates/run_gates.sh`, `benchmark/gates/check_hub.py`, `hub-router.json`, `mode-registry.json`; oracle: `figma-ds-cli --help`, `figma-ds-cli --version`, `figma-ds-cli create --help`, `figma-ds-cli fj --help`.

## Files Reviewed

| File | Close-out question asked |
|---|---|
| all six P1 sites | Does each still reproduce against the cited line, and does any later iteration's evidence resolve it? |
| `feature-catalog/feature-catalog.md`, `feature-catalog/render-and-create/render-and-create.md` | Was the create-primitives claim a one-file slip or a repeated conclusion? |
| `changelog/v1.1.0.0.md`–`v1.1.3.0.md` | Are the three falsifiable claims in the release trail true of the files? |
| `scripts/tests/test_vendor_sync.py`, `benchmark/gates/run_gates.sh`, `benchmark/gates/check_hub.py` | Does anything actually run the vendor check the manifest exists for? |
| `mcp-servers/figma-cli/README.md`, `mcp-servers/figma-mcp/README.md` | Do the embedded-server pages add claims the rest of the packet does not support? |
| `mode-registry.json`, `hub-router.json` (read-only) | Does the hub registry actually mark this packet as vendored, so the gate has its input? |

## Adversarial replay of the active P1 set

| Id | Replayed against | Result | Movement |
|---|---|---|---|
| R1-P1-001 | `tool-surface.md:98` + `figma-ds-cli create --help` | Reproduces. The binary lists `rect\|rectangle`, `ellipse\|circle`, `text`, `line`, `component`, `group`, `autolayout\|al` as `create` SUBcommands and exposes none of them at top level. | **Scope widened**: the same inverted conclusion ("source proves top-level aliases; REFERENCE's `create rect` is drift") is repeated at `feature-catalog/feature-catalog.md:18` and `:120` and at `feature-catalog/render-and-create/render-and-create.md:28`. It is a settled conclusion carried across three files, not a typo. Severity unchanged at P1; the remediation must touch all three. |
| R1-P1-002 | `_common.sh:19-23` | Reproduces: no `--version`/`--help` probe before returning `figma-cli`. | Second site confirmed in iteration 2 (`examples/safe-connect-daemon-health.sh:34-38` probes and then proceeds anyway). Remediation is the shared helper; the example inherits the fix. |
| R1-P1-003 | `connect-safe.sh:20`, executed with stdin redirected from `/dev/null` | Reproduces: non-interactive notice, exit `0`, no connection attempted. | Unchanged. |
| R1-P1-004 | `doctor.sh:48`, resolution walk | Reproduces: five levels up = `MEGA/Development`, four = `AI Systems/` where the `figma` manual is registered. | Unchanged. Fix confirmed feasible: `vendor-sync.py:74-84` already implements root discovery by walking to the folder that holds `.skilled`. |
| R2-P1-001 | `README.md:86`, `INSTALL-GUIDE.md:268`/`:291`, `figma-ds-cli extract --help` | Reproduces: `extract [options] [output]`, no `--out`; the packet's own reference and example use the positional form. | Unchanged. |
| R3-P1-001 | the seven link sites | Reproduces. | **Impact re-read**: the optional path's mechanics are also stated inline in `mcp-wiring.md` §3 and §4, so the dead links are redundant guidance rather than the only source. This sits on the P1/P2 boundary; the registry keeps the recorded grade and synthesis flags it as the first candidate for downgrade. |

No finding was resolved by another iteration's evidence, and no new P0 appeared under replay. The two P0 candidates that were considered and rejected are recorded under "Ruled out".

## Findings by Severity

### P0 Findings

None.

### P1 Findings

None **new** this iteration. The six P1 findings above remain open; they are re-verified, not re-counted.

### P2 Findings

None new this iteration.

## Surfaces opened for the first time (no defects)

- **The release trail is honest.** Three falsifiable claims were checked: v1.1.0.0 says the README rewrite has "zero em dashes, zero semicolons and zero Oxford commas" (README contains 0 `—` and 0 `;`); v1.1.1.0 says the `sk-doc-template` comment was removed from 8 catalog files (grep across `feature-catalog/` returns nothing, and the catalog holds exactly 8 non-index files); v1.1.3.0 says the frontmatter version key was added to older changelog entries (all six carry a `version:` key). The changelog is not decoration.
- **The vendor check is actually run.** `benchmark/gates/run_gates.sh:47-48` runs both `python3 scripts/vendor-sync.py status` and `python3 scripts/tests/test_vendor_sync.py`, and skips the first honestly when no shared skill folder exists. The test suite builds scratch upstream repositories and covers in-step status, a one-byte local edit blocking pull (and surviving the refusal), symlink refusal, push writing a diff upstream, push refused when upstream moved, re-baselining after a committed push, `include` scoping sparing a sibling upstream file, and path-escape refusal for all three commands. My iteration-1 reasoning about the pull guard is corroborated by tests that assert the same behaviour.
- **The hub registry marks the packet as vendored.** `mode-registry.json` carries a `vendored-packets` extension naming `mcp-figma`, which is the input `benchmark/gates/check_hub.py` cross-checks against `vendor.json`, and `hub-router.json` names `mcp-figma/SKILL.md`, which exists.
- **The embedded-server pages add no unsupported claims.** `mcp-servers/figma-cli/README.md` restates the naming trap and version trap correctly and delegates the safety model to `SKILL.md`; `setup.sh` is a three-line `exec` of the canonical installer, so there is no second install path to keep in step.
- **Every command the catalog and references name exists at top level.** A sweep of every `figma-ds-cli <token>` mention across all 58 files against the 72 top-level commands found exactly one unrecognized command token, `rect`, whose two sites are already finding R1-P1-001.

## Traceability Checks

| Protocol | Level | Status | Evidence |
|---|---|---|---|
| `spec_code` | core | pass | Carried forward; re-verified against the manifest and the tree. |
| `checklist_evidence` | core | not_applicable | No `checklist.md` in the staging folder. |
| `skill_agent` | overlay | pass | Carried forward from iteration 4. |
| `agent_cross_runtime` | overlay | not_applicable | No runtime agent definition in the packet. |
| `feature_catalog_code` | overlay | partial | Final: catalog commands match the binary except the create-primitives claim, and its section counts match the reference. |
| `playbook_capability` | overlay | partial | Final: 17 files for 17 scenarios, five cited IDs resolve, spot-checked command forms match the installed 1.2.0; 12 of 17 not audited line by line. |

## Ruled out this iteration

- **P0 candidate: an unconfirmed destructive path.** `connect-yolo.sh` refuses without its consent flag, `unpatch.sh` is the stated rollback, `arrange` is labeled destructive by the binary itself and by `tool-surface.md:102`, and every destructive verb appears in the confirm-plus-target-plus-rollback set. No documented routine path reaches a destructive verb unconfirmed.
- **P0 candidate: a credential leak.** Re-checked after reading the three scripts never opened before (`setup.sh`, `print-utcp-snippets.sh`, `unpatch.sh`): none reads or prints the token, and the token-shaped string scan over the whole packet is still empty.
- **"The 58-file scope was mis-enumerated."** 58 files on disk, 58 in the manifest, 58 in upstream, byte-identical.
- **"The README's AT-A-GLANCE/quick-start flow teaches the wrong ordering."** Step 1 verify binary, step 2 safe connect, step 3 daemon status, step 4 read-only export matches the skill's own phase model and its global preconditions.

## Next Dimension

None. The loop has reached `config.maxIterations` (5 of 5) under `stopPolicy: max-iterations`; convergence was off by configuration, so the loop closes on the cap rather than on a similarity score. Synthesis follows: 17 active findings (0 P0, 6 P1, 11 P2) and a report verdict of CONDITIONAL, with the P1 set driving remediation and R3-P1-001 named as the first downgrade candidate.

Review verdict: PASS
