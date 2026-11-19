# Review Iteration 002

## Dispatcher

- Iteration: 2 of 10 (JSONL-derived count: 1 prior `type:"iteration"` record, so 2 is correct; dispatcher value matched).
- Mode: `review`, target agent `@deep-review`, LEAF single iteration.
- Operator focus addressed: gate and script correctness across `benchmark/`, `scripts/` and the Sync Loop scripts, plus the vendored-artifact sync question. Addressed by reading `run_gates.sh` in full, both fixture runners, the gate entry points, `scripts/vendor-sync.py` (setup/exit paths), `scripts/tests/test_vendor_sync.py`, and by a byte comparison of the two copies of the output-format validator.
- Budget profile: `verify` (10 tool calls used, ceiling 13).

BINDING: target=AI Systems/Product Owner (hub, packets, benchmark gates, scripts, Sync Loop)
BINDING: maxIterations=10
BINDING: convergence=0.1
BINDING: mode=review
BINDING: dimensions=correctness
BINDING: specFolder=specs/054-po-system-deep-review

## Dimension

`correctness` — second pass, narrowed by dispatch to the executable surface: gate runner, gate entry points, fixture harnesses, `scripts/`, and the Sync Loop scripts. Logic errors, dead paths, checks that cannot fail, and exit-code handling. Prior iteration covered the routing contracts; none of its findings are re-reported here.

## Files Reviewed

- `AI Systems/Product Owner/benchmark/gates/run_gates.sh` (all 108 lines)
- `AI Systems/Product Owner/benchmark/router/run_fixtures.sh` (all 31 lines)
- `AI Systems/Product Owner/benchmark/format/run_fixtures.sh` (`check()` helper lines 34-70, result block lines 248-256)
- `AI Systems/Product Owner/benchmark/format/validate-output-format.cjs` (exit sites; compared byte-wise)
- `AI Systems/z — Claude Project Sync Loop/validate-output-format.cjs` (compared byte-wise)
- `AI Systems/z — Claude Project Sync Loop/run_fixtures.sh` (header and argument contract, lines 1-40)
- `AI Systems/Product Owner/scripts/vendor-sync.py` (docstring, `find_upstream_root`, status/pull/push returns, `main`)
- `AI Systems/Product Owner/scripts/tests/test_vendor_sync.py` (test contract and `__main__` block)
- `AI Systems/Product Owner/benchmark/gates/rule_parity.py` (path derivation lines 62-68)
- `AI Systems/Product Owner/benchmark/gates/check_leaf_map_parity.py`, `check_hub.py`, `example_lint.py` (entry-point and `--self-test` handling)
- `AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py`, `compose_board.py` (`--self-test` handling)
- File inventory of `benchmark/`, `scripts/`, and `AI Systems/z — Claude Project Sync Loop/`

## Findings — New

### P0 Findings

None. No exploitable path and no destructive data loss path was found in the gate or script surface.

### P1 Findings

5. **The Product Owner release gate runs a diverged fork of the output-format validator the Sync Loop owns** -- `AI Systems/Product Owner/benchmark/format/validate-output-format.cjs:1` -- The Product Owner ships `benchmark/format/validate-output-format.cjs` at 1733 lines while `AI Systems/z — Claude Project Sync Loop/validate-output-format.cjs` holds 1878 lines, and `cmp` reports the two files differ. The two fixture runners also expose different contracts: the Sync Loop runner is parameterised as `run_fixtures.sh <entry-script> <blocking|advisory> [fixtures-dir]` and only resolves its validator from `$1` [SOURCE: AI Systems/z — Claude Project Sync Loop/run_fixtures.sh:19], while the Product Owner runner hard-codes `VALIDATOR="./validate-output-format.cjs"` and `FIXTURES="./fixtures"` with no argument path [SOURCE: AI Systems/Product Owner/benchmark/format/run_fixtures.sh:26]. `run_gates.sh` therefore can only ever exercise the local copy [SOURCE: AI Systems/Product Owner/benchmark/gates/run_gates.sh:44]. Because the local copy has no blocking/advisory second argument, and the shared runner's header describes punctuation, purity, cut-rule and keep-side cases that depend on that argument [SOURCE: AI Systems/z — Claude Project Sync Loop/run_fixtures.sh:15], a deliverable that violates a mechanic present only in the 1878-line copy passes `run_gates.sh` with `all 15 gates pass` [SOURCE: AI Systems/Product Owner/benchmark/gates/run_gates.sh:100].
    Finding class: `duplicate_artifact_drift`
    Scope proof: both files read on disk this iteration; `wc -l` returned 1733 and 1878; `cmp -s` returned non-zero; both fixture runners' argument contracts read directly. No source file was modified.
    Affected surface hints: `AI Systems/Product Owner/benchmark/format/validate-output-format.cjs`, `AI Systems/Product Owner/benchmark/format/run_fixtures.sh`, `AI Systems/Product Owner/benchmark/gates/run_gates.sh`, `AI Systems/z — Claude Project Sync Loop/validate-output-format.cjs`, `AI Systems/Product Owner/vendor.json`, `AI Systems/Product Owner/SYNC.md`
    Case: a deliverable breaks a rule that exists only in the Sync Loop copy of the validator; the Product Owner gate reports every format fixture passing and `run_gates.sh` exits 0, so the release changelog records a clean format gate.
    ```json
    {"type":"spec_mismatch","claim":"the Product Owner format gate exercises a 145-line-smaller fork of the Sync Loop's validator through a runner that cannot accept the shared runner's entry-script and blocking/advisory arguments","evidenceRefs":["AI Systems/Product Owner/benchmark/format/validate-output-format.cjs:1","AI Systems/z — Claude Project Sync Loop/validate-output-format.cjs:1","AI Systems/Product Owner/benchmark/format/run_fixtures.sh:26","AI Systems/z — Claude Project Sync Loop/run_fixtures.sh:19","AI Systems/Product Owner/benchmark/gates/run_gates.sh:44"],"counterevidenceSought":"Checked whether the Product Owner runner can be pointed at an external validator (it cannot, the path is a literal), whether the two files are identical (cmp says they differ), and whether the local validator accepts a blocking/advisory argument (its only exits are 64/66/1 and it is invoked with file arguments alone). Not re-read this iteration: vendor.json and SYNC.md, which could record a deliberate pin for this file.","alternativeExplanation":"The Product Owner copy is a deliberately pinned, self-contained release artifact and the Sync Loop copy is the newer development variant; the pin is recorded elsewhere and the divergence is expected between syncs.","finalSeverity":"P1","confidence":"medium","downgradeTrigger":"Downgrade to P2 if `AI Systems/Product Owner/vendor.json` or `AI Systems/Product Owner/SYNC.md` records this validator as a pinned copy with an upstream commit or sha and a stated re-sync step, making the divergence an accounted-for pin refresh rather than an unmanaged fork."}
    ```

### P2 Findings

6. **The release runner reports a clean pass while five checked-in parity and residency scripts never run** -- `AI Systems/Product Owner/benchmark/gates/run_gates.sh:29` -- The header states that the shared parity and residency checks are deliberately excluded and `run from benchmark/parity/ once a batch is committed` [SOURCE: AI Systems/Product Owner/benchmark/gates/run_gates.sh:29], but nothing enforces that condition and the success line prints only the gate count [SOURCE: AI Systems/Product Owner/benchmark/gates/run_gates.sh:100]. Five scripts sit in `benchmark/parity/` (`run_query.sh`, `run_parity.sh`, `run_receipts.sh`, `run_receipt_write.sh`, `run_residency.sh`) and no entry in the `GATES` array invokes any of them [SOURCE: AI Systems/Product Owner/benchmark/gates/run_gates.sh:42]. The documented exit-0 contract says the summary `names the skip` [SOURCE: AI Systems/Product Owner/benchmark/gates/run_gates.sh:35], yet the skip it names is only the `.skilled` and Sync Loop folder absence; the parity exclusion is silent in the output.
    Finding class: `checker_undercoverage`
    Scope proof: `GATES` array read in full (15 entries, lines 42-58); `benchmark/parity/` inventory taken on disk (5 `.sh` files, none referenced in the array); header lines 29-37 read directly.
    Affected surface hints: `AI Systems/Product Owner/benchmark/gates/run_gates.sh`, `AI Systems/Product Owner/benchmark/parity/`
    Case: a release runs the documented single command, reads `all 15 gates pass`, and writes the changelog with receipt and residency parity unverified; the operator has no line in the output telling them those five scripts still had to be run by hand.

7. **Gate wiring derives the existence-check path from the second whitespace token, so any gate needing a flag before its script is reported MISSING instead of run** -- `AI Systems/Product Owner/benchmark/gates/run_gates.sh:65` -- `script="$(printf '%s' "$command" | awk '{print $2}')"` assumes every entry is `interpreter path ...`, and `[ ! -f "$script" ]` then decides whether to run it at all [SOURCE: AI Systems/Product Owner/benchmark/gates/run_gates.sh:85]. Adding a gate as `python3 -u benchmark/gates/check_hub.py` or `env PO_STRICT=1 python3 scripts/vendor-sync.py status` makes `$2` a flag or an assignment, so the gate prints `MISSING`, increments the failure count, and never executes the script that does exist.
    Finding class: `fragile_gate_wiring`
    Scope proof: array construction and the `$2` extraction read directly at lines 63-65 and the consumer at lines 85-89; every current entry was checked to begin with an interpreter and a path, so the defect is latent rather than active today.
    Affected surface hints: `AI Systems/Product Owner/benchmark/gates/run_gates.sh`
    Case: a maintainer adds a gate with an interpreter flag or an inline environment assignment, sees `MISSING` next to a script they can confirm exists on disk, and either deletes the gate or hard-codes the path check.

## Traceability Checks

| Protocol | Level | Status | Note |
| --- | --- | --- | --- |
| `spec_code` | core | partial | The gate runner's stated exit contract (lines 34-38) matches its implementation (`exit 2` on unreachable root, `exit $failed`, `exit 0` on skip-only) — one exception recorded as finding 6, where the exit-0 summary does not name the parity exclusion the header declares. |
| `checklist_evidence` | core | partial | `run_gates.sh:22-23` claims vendor sync compares against a shared skill folder; verified against `vendor-sync.py:94-103`, whose `VENDOR_UPSTREAM_ROOT` override and upward `.skilled` walk match the guard at `run_gates.sh:80`. Self-test gates claim coverage: `check_hub.py:701`, `example_lint.py:337`, `flow_check.py:636` and `compose_board.py:1761` all implement `--self-test`, so none of those four entries is silently a no-op. |
| `skill_agent` | overlay | notApplicable | No skill or agent definition changed in this focus. |
| `agent_cross_runtime` | overlay | notApplicable | No agent definition in this surface. |
| `feature_catalog_code` | overlay | partial | `AI Systems/z — Claude Project Sync Loop/feature-catalog/output-format-gate/output-format-validator.md` and `fixture-runner.md` exist and describe the gate the Product Owner forks; the catalog text was not read this iteration, so finding 5's direction of drift is stated as unverified. |
| `playbook_capability` | overlay | partial | The manual-testing playbook's gates are the ones `run_gates.sh` wires; the playbook body was not read this iteration. Capability-to-script coverage for `benchmark/parity/` stays open (finding 6). |

## Integration Evidence

- `AI Systems/Product Owner/benchmark/gates/run_gates.sh:43` invokes `benchmark/router/run_fixtures.sh`, which runs `route_contract.py fixtures.json` and `differential.py` and combines both statuses without `-e` [SOURCE: AI Systems/Product Owner/benchmark/router/run_fixtures.sh:29] — the combination is correct: either failure yields exit 1, and both always run.
- `AI Systems/Product Owner/benchmark/gates/run_gates.sh:48` invokes `scripts/vendor-sync.py status`; the script's `main` returns the worst per-package status and maps `SetupError` to `EXIT_SETUP` [SOURCE: AI Systems/Product Owner/scripts/vendor-sync.py:600], so a missing upstream tree fails the gate rather than passing it.
- `AI Systems/Product Owner/scripts/tests/test_vendor_sync.py:352` ends with `unittest.main(verbosity=2)`, so the `vendor sync tests` gate cannot pass by importing a module that runs nothing.
- `AI Systems/Product Owner/benchmark/gates/rule_parity.py:68` resolves the declaration folder as `dirname(repo root)/z — Claude Project Sync Loop`, the same folder `run_gates.sh:66` tests for before skipping, so the gate's skip guard and the script's own path agree.

## Edge Cases

- **Dispatch/strategy disagreement on focus.** The strategy's `Next Focus` named `traceability` on `sk-product-owner/`, while the dispatch assigned `correctness` on the gate and script surface. The dispatch owns focus; this iteration followed it and left the strategy's `sk-product-owner` stage-two traceability direction recorded for a later iteration rather than treating it as done.
- **Direction of the validator divergence is unproven.** Finding 5 proves the two copies differ and that the Product Owner runner cannot consume the shared runner's contract. It does not prove which copy is newer. The finding is filed as drift with a named downgrade trigger rather than as a claim that the Product Owner copy is stale.
- **Archived gate copies excluded.** `benchmark/reports/**/after/skill/**/exports/benchmark/**` holds older snapshots of `rule_parity.py`, `validate-output-format.cjs` and the fixtures runners (for example a 293-line `rule_parity.py` against today's 345). These are recorded run outputs, not the live gate, and were not reviewed as defects.
- **`.env` never opened.** The operator prohibition was honoured; nothing from `AI Systems/Product Owner/.env` was read, quoted or inferred.

## Confirmed-Clean Surfaces

- `run_gates.sh` exit-code handling: `2` for an unreachable root, `$failed` for failures or missing scripts, `0` only when nothing failed, with the total derived from the array length rather than a literal [SOURCE: AI Systems/Product Owner/benchmark/gates/run_gates.sh:59].
- `run_gates.sh` deliberate `set -uo pipefail` without `-e`, so one red gate never hides the rest, documented at the top of the file [SOURCE: AI Systems/Product Owner/benchmark/gates/run_gates.sh:38].
- Format fixture harness `check()`: it compares the exit code, then tests the required pattern and the forbidden antipattern, and guards both against an empty string, so no case degenerates into a match-everything assertion [SOURCE: AI Systems/Product Owner/benchmark/format/run_fixtures.sh:52].
- The herestring in `check()` avoids the `pipefail` plus `grep -q` SIGPIPE false failure, and the reason is recorded inline [SOURCE: AI Systems/Product Owner/benchmark/format/run_fixtures.sh:48].
- `vendor-sync.py` refuses a pull when the local copy carries edits upstream does not, when upstream is dirty, and when the pin cannot be read, rather than overwriting [SOURCE: AI Systems/Product Owner/scripts/vendor-sync.py:510].
- `vendor-sync.py` treats a planted symlink as a setup error (exit 2) rather than copying through it, and `test_vendor_sync.py:162` pins that behaviour.
- Router gate combines both contract checks and still exits 1 if either fails [SOURCE: AI Systems/Product Owner/benchmark/router/run_fixtures.sh:28].

## Ruled Out

- **`vendor sync tests` gate that cannot fail**: ruled out. `scripts/tests/test_vendor_sync.py:352` runs `unittest.main(verbosity=2)` and the suite asserts real exit codes 0/1/2 across eight cases.
- **Self-test gates wired to scripts that do not implement `--self-test`**: ruled out. `check_hub.py`, `example_lint.py`, `flow_check.py` and `compose_board.py` each parse `--self-test` and return a non-zero count when a planted defect does not fire.
- **`run_gates.sh` skip guard resolving a different Sync Loop folder than `rule_parity.py`**: ruled out. Both resolve to `dirname(Product Owner)/z — Claude Project Sync Loop`.
- **`vendor sync` guard reading a different environment variable than the script**: ruled out. `run_gates.sh:80` tests `VENDOR_UPSTREAM_ROOT`, `vendor-sync.py:103` reads the same name.
- **Router fixture gate masking the first failure with `|| status=1`**: ruled out. Both checks run unconditionally and the combined status is 1 if either failed.
- **Format `check()` degrading into a match-everything assertion on an empty antipattern**: ruled out. Both pattern branches are guarded by `[ -n ... ]`.
- **Archived gate snapshots as live drift**: ruled out as a defect source; they are recorded run output under `benchmark/reports/`.

## Next Focus

- **Dimension:** security.
- **Focus area:** `AI Systems/Product Owner/scripts/` (path containment in `vendor-sync.py`, `code-mode.cjs`), `AI Systems/Product Owner/benchmark/gates/check_markdown_links.py` and the fixture harnesses for path handling and shell quoting, plus `AI Systems/z — Claude Project Sync Loop/*.py` argument and path handling.
- **Reason:** correctness on the executable surface is now covered except for the sync-loop Python bodies; the gate surface is where operator input, file paths and shell interpolation meet, which is exactly the security dimension's reach. The `.env` prohibition makes secret handling in the runners an explicit non-target.
- **Rotation status:** `correctness` completed its second pass this iteration; `security` becomes the active dimension while `traceability` and `maintainability` stay queued. The strategy's queued `sk-product-owner` stage-two traceability direction is carried forward, not dropped.
- **Blocked/productive carry-forward:** productive direction to carry — the validator fork (finding 5) needs one read of `vendor.json` and `SYNC.md` to settle whether the pin is recorded; that read is deferred, not exhausted.
- **Required evidence:** `scripts/vendor-sync.py` containment helpers (`contained_path`, `copy_tree`), `scripts/code-mode.cjs`, `check_markdown_links.py` path resolution, and the Sync Loop Python entry points, each checked for path traversal, shell interpolation of untrusted values, and secret exposure.
- **Recovery note:** not applicable; this iteration ran clean within budget.
- **Operator focus carried forward:** the vendored-package sync question is now partly answered — `vendor-sync.py` is a real, tested, three-verb sync tool with pin verification, and the one artifact it does *not* cover is the format validator that has already diverged (finding 5). Whether `doctor:overlay` plus repinning could subsume `vendor-sync.py` remains open for a later iteration.

Review verdict: CONDITIONAL
