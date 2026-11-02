# Review Iteration 003 - Correctness (scripts and gates)

## Dispatcher

- Session: `fanout-deepseek-1792580494888-r714jg`, lineage `deepseek`, iteration 3 of 5
- Executor: cli-pi (deepseek-v4.1-flash), detached fan-out lineage; iteration executed in-process, no nested dispatch
- Target: `specs/product-owner/018-product-owner-deep-review/005-whole-repo`, reviewing the Product Owner tree named in `spec.md` Files to Change
- Sources consulted before this iteration: `steer.md`, the state log projection, the findings registry, the strategy file
- Focus selected from strategy Next Focus: gate and script defects in `scripts/` and `benchmark/`

## Dimension

Correctness: does each builder and gate do what its own stated contract says, and does it cover the
surfaces the hub now ships?

## Files Reviewed

- `AI Systems/Product Owner/scripts/build-plugin.py` (read whole, 248 lines)
- `AI Systems/Product Owner/scripts/vendor-sync.py:1-120`
- `AI Systems/Product Owner/scripts/tests/test_vendor_sync.py` (listed, 201 lines)
- `AI Systems/Product Owner/benchmark/gates/example_lint.py:1-60,102-103`
- `AI Systems/Product Owner/benchmark/format/validate-output-format.cjs` (Flow coverage sweep)
- `AI Systems/Product Owner/claude-plugin/.claude-plugin/plugin.json` (output tree, read for the builder's claims)
- `AI Systems/Product Owner/sk-create-figjam/assets/examples/` (7 worked examples enumerated)
- `AI Systems/Product Owner/steer.md` (lead rulings for this lineage)

## Findings by Severity

### P0 Findings

None.

### P1 Findings

1. **The plugin build ships the FigJam playbook its own rule excludes** -- AI Systems/Product Owner/scripts/build-plugin.py:57 -- The comment above the exclusion set says "The playbooks, the changelogs and the hub benchmark cite repository paths and release history a plugin install does not carry, so they stay out of the shipped skill". The set excludes `sk-product-owner/manual-testing-playbook` and both changelogs, but not `sk-create-figjam/manual-testing-playbook`, so 53 playbook files are copied into `claude-plugin/skills/product-owner/sk-create-figjam/manual-testing-playbook/` on every build (376 files shipped in total). The one exception the same comment allows, "A vendored packet ships whole", covers `mcp-figma` and `mcp-click-up` only; `sk-create-figjam` is a first-party packet.
   Finding class: builder-contract violation
   Scope proof: the exclusion set and the shipped tree were both read; the comment and the coded set are in one file
   Affected surface hints: `AI Systems/Product Owner/scripts/build-plugin.py` `UNSHIPPED` set; the plugin output is generated, so the fix belongs to the builder
   Case: a plugin install loads the FigJam skill and finds 53 scenario files that cite repository paths the install does not carry, because the build never excluded them.

   ```json
   {
     "type": "claim-adjudication",
     "claim": "build-plugin.py ships sk-create-figjam/manual-testing-playbook although its own comment says playbooks stay out of the shipped skill",
     "evidenceRefs": ["AI Systems/Product Owner/scripts/build-plugin.py:54", "AI Systems/Product Owner/scripts/build-plugin.py:57-58", "claude-plugin/skills/product-owner/sk-create-figjam/manual-testing-playbook (53 files)"],
     "counterevidenceSought": "Checked whether a separate rule ships the FigJam playbook on purpose: the only stated exception is a vendored packet shipping whole, and sk-create-figjam is not in vendor.json's packages. Checked whether the playbook is empty or ignored elsewhere: `find` counts 53 regular files in the built tree.",
     "alternativeExplanation": "The operator may intend the FigJam scenarios to ship because they are the mode's worked guidance, and the comment's 'playbooks' may mean only the Product Owner playbook.",
     "finalSeverity": "P1",
     "confidence": "medium-high",
     "downgradeTrigger": "A builder comment that states the FigJam playbook ships deliberately, or an UNSHIPPED entry that names it, resolves this to P2 documentation or closes it."
   }
   ```

### P2 Findings

1. **The builder's description of the tracked plugin folder names a README that is not there** -- AI Systems/Product Owner/scripts/build-plugin.py:8 -- The docstring says "The plugin under `claude-plugin/` tracks only its manifests and README". The folder holds `.claude-plugin/` and `skills/` and no `README.md`, so a reader trusting the docstring looks for a file the repository does not track.
   Finding class: documentation-path drift
   Scope proof: folder listing read directly; the claim is in the in-scope builder
   Affected surface hints: `AI Systems/Product Owner/scripts/build-plugin.py` module docstring
   Case: a maintainer updates the plugin install instructions, searches `claude-plugin/README.md` as the docstring says, and finds nothing to update.

2. **The example lint reads every Project example mirror but only the product-owner source examples** -- AI Systems/Product Owner/benchmark/gates/example_lint.py:49 -- `EXAMPLES` is `sk-product-owner/assets/examples`, while `MIRROR_GLOB` is `Product Owner - Examples - *.md`, which also matches the seven Flow mirrors in `claude project/knowledge/`. The seven source examples under `sk-create-figjam/assets/examples/` are therefore unchecked on the skill side while their mirrors are checked, so the gate's premise ("models copy a worked example more closely than they follow a rule") holds for one packet only.
   Finding class: gate-coverage gap
   Scope proof: constants and both globs read; the FigJam example count measured on disk
   Affected surface hints: `AI Systems/Product Owner/benchmark/gates/example_lint.py` `EXAMPLES` constant and its `rglob`
   Case: a Flow example is edited into an em-dash or a missing section on the skill side; the lint stays green until the mirror is hand-updated to match.

## Traceability Checks

| Protocol | Status | Evidence |
|----------|--------|----------|
| `spec_code` | pass | `scripts/` and `benchmark/` files named in `spec.md` exist and were read |
| `checklist_evidence` | notApplicable | No `checklist.md` in the staging packet |
| `skill_agent` | pass | The builder derives its packet list from `mode-registry.json` rather than a hardcoded list, so a new mode ships without a builder edit |
| `agent_cross_runtime` | notApplicable | No runtime mirror opened |
| `playbook_capability` | deferred | Scheduled with maintainability |
| `feature_catalog_code` | notApplicable | No feature catalog in the target |

## Integration Evidence

- `scripts/vendor-sync.py` states its three-tree contract and enforces containment, symlink refusal and a refused push over upstream edits in the first 120 lines read; no defect found in the read portion.
- `scripts/build-plugin.py` refuses a symlinked source, a symlinked plugin path, a `skills/` that resolves outside the repository, a vendored hash mismatch, an MCP-registering `plugin.json` and a `bin/` folder, and its `--self-test` plants each of those conditions.
- `benchmark/format/validate-output-format.cjs` mentions Flow/FigJam in six places, so the Flow artifacts are not wholly absent from the validator; only `example_lint.py` misses the source examples.

## Edge Cases

- **The plugin output is out of scope.** `claude-plugin/` is generated by the builder, so both builder findings name the builder as the fix site and use the output tree only as evidence.
- **`unship` intent cannot be proven from the repository.** Whether the FigJam playbook should ship is an operator decision; the finding rests on the builder's own stated rule, not on a guess about intent.
- **`benchmark/reports/` is out of scope** and was not read, so no conclusion is drawn about historical run output.

## Confirmed-Clean Surfaces

- The builder's packet list comes from `mode-registry.json`, so registering a mode cannot silently leave it out of the plugin.
- Determinism: the build hashes both sides and refuses on any differing byte, and the self-test compares two consecutive builds.
- `claude-plugin/.claude-plugin/plugin.json` registers no MCP server and the folder holds no `bin/`, which is what the builder requires.

## Ruled Out

- **`vendor-sync.py` lets a manifest path escape its root** -- ruled out: `contained_path` is applied to the local path and every include entry, and `SetupError` is converted to a refusal.
- **The build is non-deterministic** -- ruled out: file iteration is sorted and the tree hash comparison is exact.

## Verdict

One active P1 (the FigJam playbook ships against the builder's own rule) and two P2 advisories. Verdict follows the P1.

## Next Focus

- Dimension: maintainability
- Focus area: `manual-testing-playbook/` (hub, 7 scenarios) and `sk-product-owner/manual-testing-playbook/` (50 scenarios), `benchmark/grader/`, `benchmark/format/` README claims, and `changelog/` vs `sk-product-owner/changelog/`
- Reason: the last declared dimension; the declared focus also names documentation that states behaviour the code no longer has
- Rotation status: D1 twice, D3 once; D4 next, with D2 security folded into the same pass
- Blocked/productive carry-forward: productive -- reading a builder against its own comment found the P1; do not re-enter hub-routing or Project-mirror parity
- Required evidence: file:line in the doc or script plus the tree state that contradicts it
- Recovery note: none

Review verdict: CONDITIONAL
