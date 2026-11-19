# Review Iteration 6 — Maintainability (sk-code language-standard alignment)

**Dispatcher**: `/deep:review` fan-out lane 6 of 10 (parallel with iterations 3-5 and 7-9; each lane owns its own focus).
**Mode**: review. **Dimension**: maintainability. **Budget profile**: verify (13 tool calls used; hard max 13).
**Operator focus carried in**: alignment of `benchmark/` scripts, `scripts/`, the format validators and the JavaScript programs in `mcp-click-up/references/mcp-tools.md` against sk-code language standards, each deviation named with its rule.

## Files Reviewed

- `AI Systems/Product Owner/benchmark/gates/run_gates.sh:1-108`, `check_hub.py`, `check_leaf_map_parity.py`, `check_markdown_links.py`, `example_lint.py`, `rule_parity.py` (shebang, banner, docstring census)
- `AI Systems/Product Owner/benchmark/format/validate-output-format.cjs:1-12, :29-34, :93, :1718-1723` (structure, console surface, doc census)
- `AI Systems/Product Owner/benchmark/format/run_fixtures.sh:1-256`, `benchmark/router/run_fixtures.sh:24-31`, `benchmark/grader/check_report.sh:29-82`, `benchmark/parity/run_{parity,query,receipts,receipt_write,residency}.sh`
- `AI Systems/Product Owner/benchmark/grader/{hvr_lint,lint_replies,twin_divergence}.py`, `benchmark/router/{differential,route_contract}.py` (test / self-test census)
- `AI Systems/Product Owner/scripts/{code-mode.cjs,vendor-sync.py,tests/test_vendor_sync.py}`, `scripts/vendored/code-mode/{mcp-code-mode-launcher.cjs,lib/node-engine-resolver.cjs}`
- `AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:71-140, :639-700` (2 of 5 embedded JavaScript programs, 983 lines total)
- `AI Systems/Product Owner/vendor.json` (all seven package entries)
- Rule sources: `.skilled/skills/sk-code/sk-code-skilled/references/javascript/quality-standards/overview-modules-and-docs.md:202, :228`; `.../shell/quality-standards/overview-and-priority-blockers.md:68`; `.../python/quality-standards.md:44-70`; `.skilled/skills/sk-code/sk-code-review/references/review-core.md:44-60` (severity and reach calibration)

## Findings - New

### P0 Findings

None.

### P1 Findings

None this iteration.

### P2 Findings

1. **The output-format validator carries no function documentation and no module prefix in its result output** -- `AI Systems/Product Owner/benchmark/format/validate-output-format.cjs:1718` -- 1733 lines and 34 top-level functions with zero `/** ... */` blocks (`grep -c '^\s*/\*\*'` returns `0`), so the only contract for each of the 34 checks is its body; the advisory and statistics block prints bare labels (`Advisory:`, `Statistics:` at :1718-1723), so when the gate runner prints this tool's output next to another gate's output no line attributes it here.
   Finding class: documentation and observability gap on a checking surface.
   Scope proof: whole-file census plus direct reads of `:1-12`, `:29-34`, `:1718-1723`, all inside the declared `benchmark/` format validator.
   Affected surface hints: `benchmark/format/run_fixtures.sh`, the gate runner's format step, any future edit to one check inside the 1733-line file.
   Case: a maintainer adds one prohibited pattern to a check and, with no per-function doc block and one shared state object, has to reconstruct which of the 34 functions owns the pattern from body reads; a mixed gate log shows `Advisory:` with no tool attribution.
   Rule: sk-code JavaScript standard §5 JSDoc Documentation → Function Documentation (`.../javascript/quality-standards/overview-modules-and-docs.md:228`) and §4 Console Logging → Bracketed Module Prefix (`:202`). The file already satisfies the local P0 header convention (`// MODULE: Output Format Validator`, :3-5) and `'use strict'` (:2), so the deviation is confined to the two named rules.
   ```json
   {"type":"claim-adjudication","claim":"A 1733-line, 34-function validator has no function documentation and no bracketed module prefix, deviating from the sk-code JavaScript standard's JSDoc and console-prefix rules.","evidenceRefs":["AI Systems/Product Owner/benchmark/format/validate-output-format.cjs:1718","AI Systems/Product Owner/benchmark/format/validate-output-format.cjs:3",".skilled/skills/sk-code/sk-code-skilled/references/javascript/quality-standards/overview-modules-and-docs.md:228",".skilled/skills/sk-code/sk-code-skilled/references/javascript/quality-standards/overview-modules-and-docs.md:202"],"counterevidenceSought":"Checked whether the file uses another documentation convention (numbered section banners at :7-9) and whether the console lines are error paths that already use stderr (:29-34, :93). Banners exist and stderr use is correct, so the finding is narrowed to the two JS rules and claims no error-output defect.","alternativeExplanation":"The numbered section banners are the authors' deliberate substitute for JSDoc, chosen for a diff-friendly layout.","finalSeverity":"P2","confidence":"high","downgradeTrigger":"Already at the lowest tier; upgrade to P1 only if a change to one of the 34 checks produces a documented behaviour regression traced to the missing contract."}
   ```

2. **Every live shell runner under `benchmark/` omits `-e` from its strict-mode line; four of nine say why, and the five parity wrappers record nothing** -- `AI Systems/Product Owner/benchmark/gates/run_gates.sh:39` -- nine checked-in runners declare `set -uo pipefail` and never `set -euo pipefail`: `run_gates.sh:39`, `benchmark/format/run_fixtures.sh:19`, `benchmark/grader/check_report.sh:30`, `benchmark/router/run_fixtures.sh:25` each carry a WHY comment on the line above (:38, :18, :29, :24) stating that aborting would stop the counting; `benchmark/parity/run_parity.sh:16`, `run_query.sh:15`, `run_receipts.sh:15`, `run_receipt_write.sh:14`, `run_residency.sh:13` omit `-e` with no stated reason and delegate in a single `exec` (:19, :18, :18, :17, :16).
   Finding class: doctrine-versus-code deviation on a checking surface.
   Scope proof: `grep -n '^set '` over the nine live runners plus five `exec` lines and four rationale comments, all inside the declared `benchmark/` target.
   Affected surface hints: `benchmark/gates/run_gates.sh`, `benchmark/format/run_fixtures.sh`, `benchmark/grader/check_report.sh`, `benchmark/router/run_fixtures.sh`, and the five `benchmark/parity/run_*.sh` wrappers.
   Case: a standards pass that applies the shell P0 rule mechanically reports nine hard blockers on this repository, so the rule is either ignored wholesale or the runners gain `-e` and lose the count-all contract documented at `run_gates.sh:12-15`.
   Rule: sk-code shell standard §2 P0 — Hard Blockers → Strict Mode (`.../shell/quality-standards/overview-and-priority-blockers.md:68`), whose enforcement column says "must fix before commit". The code does not break the intent, it breaks the written rule; the defect is that the intentional deviation lives only in four inline comments and nowhere a rules consumer reads, and not at all for the five parity wrappers.
   Recommended resolution: do not add `-e`; record the deviation where the standard's consumers look (a named override note for the `benchmark/` surface) and add one comment line to each parity wrapper stating that the delegated checker owns the exit code.
   ```json
   {"type":"claim-adjudication","claim":"Nine live shell runners omit -e from their strict-mode line, deviating from the shell standard's P0 Strict Mode rule; four document the intent inline and five parity wrappers record nothing.","evidenceRefs":["AI Systems/Product Owner/benchmark/gates/run_gates.sh:38","AI Systems/Product Owner/benchmark/gates/run_gates.sh:39","AI Systems/Product Owner/benchmark/format/run_fixtures.sh:18","AI Systems/Product Owner/benchmark/grader/check_report.sh:29","AI Systems/Product Owner/benchmark/router/run_fixtures.sh:24","AI Systems/Product Owner/benchmark/parity/run_parity.sh:16","AI Systems/Product Owner/benchmark/parity/run_parity.sh:19",".skilled/skills/sk-code/sk-code-skilled/references/shell/quality-standards/overview-and-priority-blockers.md:68"],"counterevidenceSought":"Read the four WHY comments and all five parity exec lines before classifying: the counting runners deliberately keep going, and an exec'd process's status already becomes the wrapper's status, so -e would be a no-op there. That removed any correctness reach and left a doctrine-recording gap only.","alternativeExplanation":"The standard may describe a shell script that does multi-step work rather than a runner that counts failures or delegates in one line, in which case the rule text needs the carve-out.","finalSeverity":"P2","confidence":"high","downgradeTrigger":"Already at the lowest tier; upgrade to P1 if a runner stops delegating or counting and starts doing multi-step work where a mid-script failure would be silently ignored."}
   ```

## Traceability Checks

| Protocol | Status | Evidence |
| --- | --- | --- |
| core: `spec_code` | partial | This lane compared the `benchmark/` and `scripts/` surfaces against their governing standard files, not against the packet spec text; `AI Systems/Product Owner/specs/` was not read in this pass. Recorded as partial rather than pass. |
| core: `checklist_evidence` | covered | Both findings name the rule file and line they deviate from and name what already complies (local header, `'use strict'`, `uo pipefail`, stderr error output), so the checklist claim is bounded to the named rules. |
| overlay: `skill_agent` | covered | Governing authority `.skilled/skills/sk-code/sk-code-skilled/references/**` exists at every cited path and is the doctrine this repo's review pass loads through `sk-code-review/references/review-core.md:44-60`. |
| overlay: `agent_cross_runtime` | deferred | Canonical-agent versus runtime-mirror parity is outside this lane's language-standard focus and is claimed by no lane here. |
| overlay: `feature_catalog_code` | covered (narrow) | The two embedded JavaScript programs read in `mcp-click-up/references/mcp-tools.md` were checked against the JS standard's guard-clause, try-catch and WHY-comment sections; no gap was raised, so no feature-catalog claim is made. |
| overlay: `playbook_capability` | deferred | The vendored packages carry their own `manual-testing-playbook/` trees per `vendor.json` file lists; per-package playbook capability was not exercised in this pass. |

## Integration Evidence

Exact surfaces checked this iteration: `.skilled/skills/sk-code/sk-code-skilled/references/javascript/quality-standards/overview-modules-and-docs.md` (sections 2-5), `.skilled/skills/sk-code/sk-code-skilled/references/shell/quality-standards/overview-and-priority-blockers.md` (sections 2-4), `.skilled/skills/sk-code/sk-code-skilled/references/python/quality-standards.md` (section 2), `.skilled/skills/sk-code/sk-code-review/references/review-core.md` (severity, reach calibration, evidence rules), and `AI Systems/Product Owner/vendor.json` (all seven package entries, including `code-mode-launcher` → `scripts/vendored/code-mode` and `mermaid-extract` → `sk-create-figjam/scripts/vendored`).

Vendored-sync observation (context for the operator's sync question, not a finding): each package entry carries `local_path`, `upstream_path`, `base_commit` and a per-file SHA-256 map, so `scripts/vendor-sync.py` is a hash-and-repin tool over a declared file list, not a copier. That declarative shape is what a Skilled overlay or repin mechanism would have to drive; because no overlay or repin capability was read in this pass, the replacement question is carried to `Next Focus` instead of being asserted.

## Edge Cases

1. **Iteration-number derivation mismatch (resolved, reported).** `deep-review-state.jsonl` holds completed `iteration` records for 1 and 2 plus `iteration_start` records for lanes 3-7, so a JSONL-derived next number is 3, not 6. The dispatch pins lane 6 for the parallel fan-out. Resolution: this artifact uses 6 per the dispatch's lane identity and records the mismatch here rather than silently following either number. Lanes 3-5 and 7-9 write their own records in parallel; this lane writes none of them.
2. **`hvr_lint.py` reachability unverified.** `benchmark/grader/check_report.sh:65` loops over `lint_replies` and `twin_divergence` only, so `hvr_lint.py` sits outside the report-check loop. A repository-wide reference grep was issued but its output was lost to a 50 KB truncation, so no dead-code finding is filed. Deferred to `Next Focus` with the exact query.
3. **Archived run trees hold non-compliant scripts.** `benchmark/reports/**` carries roughly 40 checked-in Python and shell programs, some without a shebang (`redact_run.py`, `aggregate.py`) or with `#!/bin/bash` instead of `#!/usr/bin/env bash` (`run_full.sh`, `run_compare.sh`). Iteration 2 ruled these are recorded run output, not a live drift source; honored here, they are excluded from the census.
4. **Empty catch in a cleanup path.** `mcp-click-up/references/mcp-tools.md:110` swallows the error from closing a probe tab inside `finally`. Deliberate best-effort cleanup with the outcome recorded in outer state; not filed (see Ruled Out).
5. **Budget.** 13 of 13 hard-max calls used in the `verify` profile: 8 discovery, 4 evidence reads, 1 census. Two verification queries were cut (the `hvr_lint` reference sweep and Product Owner `specs/` traceability), both recorded as deferred rather than inferred.

## Confirmed-Clean Surfaces

- **Python surface is fully compliant with the sk-code Python P0 list**: all 12 live `benchmark/` Python scripts plus `scripts/vendor-sync.py` and `scripts/tests/test_vendor_sync.py` carry `#!/usr/bin/env python3`, the `COMPONENT` banner block and a module docstring (`.../python/quality-standards.md:44-70`). Zero TODO/FIXME/XXX markers across the whole live surface.
- **Shell surface is compliant on the other four P0 items**: every live runner has a shebang, the `COMPONENT` banner, quoted path expansions, and no commented-out code; error text goes to stderr (`check_report.sh:35`, `:41`).
- **Vendored trees are declared, not hand-copied**: `vendor.json` registers `scripts/vendored/code-mode/{mcp-code-mode-launcher.cjs,lib/node-engine-resolver.cjs}` under `code-mode-launcher` with `base_commit` and per-file hashes, so the two `.cjs` files that lack the local banner convention are upstream artefacts, not local style drift.
- **Embedded JavaScript programs in `mcp-click-up/references/mcp-tools.md` hold to the standard's error-handling shape**: guard clauses for missing tools (`:79-81`), `try/catch` around every await that can fail (`:82`, `:97`, `:117`), and WHY comments for the non-obvious waits and tab reuse (`:100`, `:655-661`).
- **`scripts/code-mode.cjs` carries the local header and `'use strict'`**, and `scripts/vendored/code-mode/lib/node-engine-resolver.cjs` carries a banner despite having no shebang, which is correct for a required module.

## Ruled Out

- **`set -e` omission as a correctness defect.** The four counting runners stay abort-free on purpose and the five parity wrappers `exec` a single delegated checker, so a mid-script failure cannot be skipped silently. Only the doctrine-recording gap survives (finding 2).
- **Missing shebang and banner in `benchmark/reports/**`.** Recorded run output; iteration 2 ruling honored (edge case 3).
- **`vendor.json` missing the vendored `scripts/vendored/` tree.** It is registered as `code-mode-launcher` with `upstream_path: .skilled/bin` and both files hashed.
- **`mermaid-extract` pointing at a nonexistent tree.** Its `local_path` is `sk-create-figjam/scripts/vendored`, not `scripts/vendored`; the assumption that every vendored package lives under `scripts/` was wrong, not the manifest.
- **Swallowed error in probe-tab cleanup.** `mcp-tools.md:110` ignores a failed close in `finally`; the resource is best-effort and the outer state already records the outcome.
- **`norm()` duplicated across the five document programs.** Copy-paste REPL snippets cannot import; the duplication is stated in-line at `mcp-tools.md:644` and the alternative (a runtime-injected prelude) does not exist here.
- **The `-e` omission being one author's oversight.** The same WHY comment appears in four files, so it is a shared, deliberate convention.
- **Python script quality as a deviation source.** Fully compliant on the P0 list; no action.
- **Self-tests missing from `benchmark/grader/*.py` and `benchmark/router/*.py`.** Observed but not filed: no rules line for a test requirement was verified inside this lane's budget, and the router pair is exercised by `run_fixtures.sh` against `fixtures.json` and `differential_corpus.json`. Deferred with evidence, not converted into a pass.

## SCOPE VIOLATIONS

None. No reviewed file was modified; every write landed on this lane's narrative, its delta, the append-gateway ledger and the strategy sections this lane owns.

## Next Focus

- **Dimension**: traceability (the only dimension with no completed lane; correctness lanes 1-5 and parallel lanes 7-9 own their own scopes).
- **Focus area**: (a) close `hvr_lint.py` reachability with `grep -rn hvr_lint` from the repo root excluding `benchmark/reports/` and `export/`; (b) settle test-coverage doctrine for `benchmark/grader/*.py` by citing the sk-code rule or closing the direction; (c) read `.skilled/commands/doctor/overlay.md` and `.skilled/skills/system-skilled-doctor` to answer the operator's sync question: whether overlay plus repin can drive the seven `vendor.json` entries instead of `scripts/vendor-sync.py`.
- **Reason**: those are the two strands that could turn the deferred evidence above into findings, and the sync question is the operator's explicit ask that no lane has yet answered from source.
- **Rotation status**: maintainability is fully reviewed in this lane; traceability has no completed lane yet.
- **Blocked/productive carry-forward**: productive — reading the rule line before judging the code produced two bounded findings and eight clean rulings in one pass; keep that order.
- **Required evidence**: a rule line for any test-coverage finding, and a direct read of the overlay or repin surface before asserting a replacement for `vendor-sync.py`.

Review verdict: CONDITIONAL
