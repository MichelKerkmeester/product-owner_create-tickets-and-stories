# Deep Review Iteration 1

## Dimension

Inventory pass, then correctness review of the assigned executable surfaces. The review also recorded security impact where a correctness boundary allowed writes outside its package root.

## Files Reviewed

* `scripts/vendor-sync.py`, `scripts/tests/test_vendor_sync.py`, `scripts/build-plugin.py`, `vendor.json`, and vendored hash integrity for `mcp-figma/**`
* `sk-product-owner/scripts/flow_check.py`, `benchmark/gates/check_hub.py`, and `benchmark/gates/run_gates.sh`
* `benchmark/router/route_contract.py`, `benchmark/router/differential.py`, `benchmark/router/fixtures.json`, and `benchmark/router/differential_corpus.json`
* `benchmark/format/validate-output-format.cjs` and the outer Sync Loop `systems.cjs` / `validate-output-format.cjs`

## Findings by Severity

### P0

None

### P1

#### R1-P1-001 — Manifest paths can redirect sync writes outside package roots

* Case: a reviewed `vendor.json` entry sets `local_path` to a path such as `../../outside-dir`, then an operator runs `vendor-sync.py pull`
* File: [SOURCE: scripts/vendor-sync.py:164]
* Evidence: `resolve_dirs` joins manifest paths without resolving or checking containment. When `include` is absent, `copy_tree` removes and replaces the target. Its include branch also copies or unlinks the joined paths. The pull conflict guard is skipped when the recorded baseline is empty. [SOURCE: scripts/vendor-sync.py:174] [SOURCE: scripts/vendor-sync.py:185] [SOURCE: scripts/vendor-sync.py:222]
* User impact: a pull or push using changed manifest metadata can overwrite or delete files outside the vendored package, including files outside the repository or shared-skill tree
* Finding class: class-of-bug
* Scope proof: static audit of `resolve_dirs`, both `copy_tree` branches, and `pull_package` found no absolute-path, parent-component, or resolved-root containment check. Existing scratch tests cover normal pull/push/include behavior but no escaping path
* Recommendation: reject absolute paths and parent traversal, resolve each package path beneath its designated root, and resolve every include entry beneath both package roots before any read or write. Add scratch-world tests proving pull and push refuse escapes without touching the outside target
* Counterevidence sought: pull refuses local edits that upstream does not carry, and push refuses upstream drift. Those checks compare file hashes but do not constrain paths; an empty recorded baseline skips the pull conflict check
* Alternative explanation: `vendor.json` is repository metadata and pull is an explicit operator action, so its paths may be treated as trusted. A changed manifest in a reviewed branch can still redirect the command before that metadata is trusted
* Final severity: P1
* Confidence: 0.95
* Downgrade trigger: downgrade only if a trusted preflight validates every package and include path beneath its designated root before each mutating command, and the CLI refuses otherwise

### P2

#### R1-P2-002 — Plugin build does not reject symlinked hub source files

* Case: a root hub file such as `SKILL.md` is a symlink to a file outside the repository when `build-plugin.py` runs
* File: [SOURCE: scripts/build-plugin.py:71]
* Evidence: `shipped_sources` inserts `HUB_FILES` directly into the source map, while the symlink scan runs only inside packet directory walks. `shutil.copyfile` follows the hub symlink, and the source/copy hash comparison then succeeds on the copied target bytes. [SOURCE: scripts/build-plugin.py:77] [SOURCE: scripts/build-plugin.py:124]
* User impact: the plugin can ship content not stored at the expected tracked source path, including an unintended local file, while reporting a successful build
* Finding class: class-of-bug
* Scope proof: the hub-file map is built before the packet-only symlink check. The existing self-test plants its symlink under `sk-product-owner/references`, so it does not cover a `HUB_FILES` entry
* Recommendation: reject symlinks for every `HUB_FILES` source and add a scratch self-test that plants a root hub symlink and expects refusal
* Confidence: 0.90

## Traceability Checks

* Core `spec_code`: partial. Router contract parity and fixtures passed; broader acceptance-criteria mapping remains open
* Core `checklist_evidence`: partial. Executable self-tests and the ten-gate suite passed; documentation and playbook evidence were not assessed in this slice
* Overlay `skill_agent`: partial. Route fixtures passed; full skill behavior traceability remains open
* Overlay `agent_cross_runtime`: partial. Router differential checks passed. The outer validator could not start because the host Node runtime lacks `libsimdutf.36.dylib`
* Overlay `feature_catalog_code` and `playbook_capability`: deferred to a later traceability pass
* The resource map is absent, so graph coverage used a graphless fallback
* Read-only checks: `run_gates.sh` passed 10/10 gates; `build-plugin.py --self-test` passed 5/5 checks; `route_contract.py --self-check` passed 5 expectations; Product Owner output-format validation passed across 44 source files with advisories. The outer validator command failed before loading its script because the host runtime could not load `libsimdutf.36.dylib`
* The working tree showed no additional target changes after the read-only checks

## Next Dimension

Iteration 2 should continue with security boundary review of manifest paths, symlink handling, and the remaining executable surfaces. Re-run the outer output-format validator after the host Node runtime is available.

## Verdict

Review verdict: CONDITIONAL
