# Review Iteration 002 - Traceability (Project mirror and parity claims)

## Dispatcher

- Session: `fanout-deepseek-1792580494888-r714jg`, lineage `deepseek`, iteration 2 of 5
- Executor: cli-pi (deepseek-v4.1-flash), detached fan-out lineage; iteration executed in-process, no nested dispatch
- Target: `specs/product-owner/018-product-owner-deep-review/005-whole-repo`, reviewing the Product Owner tree named in `spec.md` Files to Change
- Sources consulted before this iteration: `steer.md`, `deep-review-state.jsonl`, `deep-review-findings-registry.json`, `deep-review-strategy.md`
- Focus selected from strategy Next Focus: traceability of `claude project/` against its skill sources, and the parity/count claims the documentation makes

## Dimension

Traceability: does every claim the Project package and the guides make about versions, counts and
paths resolve against the tree as it is now?

## Files Reviewed

- `AI Systems/Product Owner/claude project/Custom Instructions.md:1` (kernel H1) and its six Knowledge pointers
- `AI Systems/Product Owner/claude project/README.md:3,11,57,107,168,180`
- `AI Systems/Product Owner/claude project/kernel-review.json`
- `AI Systems/Product Owner/claude project/knowledge/` (all 62 files enumerated)
- `AI Systems/Product Owner/SYNC.md:8-18,23-54`
- `AI Systems/Product Owner/README.md:184,547,651-652,684,764,776`
- `AI Systems/Product Owner/benchmark/README.md:15`
- `AI Systems/Product Owner/benchmark/gates/rule_parity.py` (declaration and a read-only run)
- `AI Systems/Product Owner/benchmark/parity/run_parity.sh`
- `AI Systems/Product Owner/sk-product-owner/SKILL.md:1-5`
- `AI Systems/Product Owner/steer.md` (lead rulings for this lineage)

## Findings by Severity

### P0 Findings

None.

### P1 Findings

None confirmed. The parity method in `SYNC.md:10` names the second skill directory for Flow Mode, so the 25 `sk-create-figjam`-sourced mirrors are covered by the documented procedure rather than omitted.

### P2 Findings

1. **SYNC.md still names kernel v1.0.0 and skill 1.0.0.0 while both files carry later versions** -- AI Systems/Product Owner/SYNC.md:18 -- The sentence says the kernel's H1 version is "currently v1.0.0" and the skill frontmatter "currently 1.0.0.0". The kernel H1 is v1.2.2 [SOURCE: claude project/Custom Instructions.md:1] and `sk-product-owner/SKILL.md` frontmatter is `version: 1.2.1.0` [SOURCE: sk-product-owner/SKILL.md:5]. The same repository's README already states the correct pair [SOURCE: README.md:651], so the parity note and the guide disagree about the live versions. Doubt stated: this contradicts the note's own instruction to bump the H1 in the same change, which suggests staleness rather than a different versioning intent; it is scored P2 because no gate and no script reads this line.
   Finding class: documentation-version drift
   Scope proof: both cited lines opened in this iteration; no file outside `claude project/`, `SYNC.md` and `sk-product-owner/SKILL.md`
   Affected surface hints: `AI Systems/Product Owner/SYNC.md` paragraph under the method list; a review note recording the version bump for v1.1.0 and v1.2.0 is the place the numbers would move
   Case: a maintainer reads SYNC.md to date the kernel, quotes v1.0.0 in a review note, and the note then misdescribes the file it reviewed.

2. **Three documents say 33 gold rows and the gate replays 37** -- AI Systems/Product Owner/README.md:684 -- The README quotes the gate's expected output as `PASSED the hub, 4 registry packets and 33 gold rows`, and the tree entry repeats "the hub's 33 gold rows" [SOURCE: README.md:776]. `benchmark/README.md` says the same [SOURCE: benchmark/README.md:15]. The case file holds 37 cases and the gate prints its own count from that file [SOURCE: benchmark/gates/check_hub.py:300], so the quoted line is an output the code no longer produces.
   Finding class: documentation-count drift
   Scope proof: count measured from `benchmark/hub-routing-cases.json` (37) and from the gate's own `gold_rows()` (37)
   Affected surface hints: `AI Systems/Product Owner/README.md` smoke table and tree; `AI Systems/Product Owner/benchmark/README.md` opening paragraph
   Case: an operator runs `check_hub.py`, sees 37 where the README promised 33, and cannot tell whether the gate gained rows or the file lost four.

3. **The rule-parity gate declares a floor of 1 for a rule seven pairs teach** -- AI Systems/Product Owner/benchmark/gates/rule_parity.py:160 -- The declaration block defines `min_pairs` as "how many declared pairs teach the rule today, measured by running this gate's own counting logic over the current tree" [SOURCE: benchmark/gates/rule_parity.py:78]. The flow rule carries `min_pairs: 1`, and the gate's own run reports "taught by 7 pair(s), 1 declared" with `PASSED 8 rules`. The gate therefore still passes if six of the seven mirrors drop the rule, which is the drift the count exists to catch.
   Finding class: gate-declaration drift
   Scope proof: gate executed read-only in this iteration; its output and its declaration read directly
   Affected surface hints: `AI Systems/Product Owner/benchmark/gates/rule_parity.py` RULES entry for the flow rule
   Case: a mirror is rewritten during a later Flow edit and loses the connected-node rule; the gate stays green because one pair still teaches it.

## Traceability Checks

| Protocol | Status | Evidence |
|----------|--------|----------|
| `spec_code` | pass | Each `spec.md` File to Change exists; the Project mirror counts 62 knowledge files, matching `systems.py`'s 62 declared pairs |
| `checklist_evidence` | notApplicable | No `checklist.md` in the staging packet |
| `skill_agent` | pass | Kernel H1 v1.2.2 and `sk-product-owner/SKILL.md` 1.2.1.0 agree with `claude project/README.md:57`; kernel Knowledge pointers all resolve to files present in `claude project/knowledge/` |
| `agent_cross_runtime` | notApplicable | No runtime mirror opened |
| `playbook_capability` | deferred | Scheduled for the maintainability iteration |
| `feature_catalog_code` | notApplicable | No feature catalog in the target |

## Integration Evidence

- `benchmark/gates/rule_parity.py` was executed read-only: `62 of 62 declared pairs compared`, `PASSED 8 rules hold on both sides of every pair that teaches them`.
- `benchmark/parity/run_parity.sh` delegates to the shared gate at `../../../z — Claude Project Sync Loop/validate_parity.py` and refused this run with exit 2: the declaration `systems.py` differs from its HEAD revision. The mutation sits outside the declared target, so it is recorded as an edge case rather than a finding.
- `claude project/kernel-review.json` describes itself as read by no tool, and `README.md:654` says the same, so the dated record is consistent with its own status.
- README counts verified against the tree: 62 knowledge files (34 core + 28 examples), six templates under `sk-product-owner/assets/`, 12 reference files, 21 worked examples, 29 release notes under `sk-product-owner/changelog/`, 141 router fixtures and 19 format fixtures all match.

## Edge Cases

- **Parity gate cannot run in this working tree.** `validate_parity.py` fails closed when its declaration file is uncommitted-modified. Green status for `benchmark/parity/` is therefore unverifiable from here, and no conclusion about pair parity should be drawn from its absence.
- **Kernel references six Knowledge files by Project filename.** The other 56 are reached by topic, so a filename-level sweep cannot prove the kernel's pointer set complete; only the six it names were checked.
- **Historical notes are not claims about today.** `SYNC.md:23` says 37 knowledge files and 27 byte-identical copies; that is a dated record of the 2026-09-09 review, not a current count, and it is not reported as drift.
- **`sk-product-owner/manual-testing-playbook/` and the hub `manual-testing-playbook/` both exist.** The README accounts for both (50 packet scenarios, 7 hub routing scenarios), so this is duplication to keep in step, not an undocumented path.

## Confirmed-Clean Surfaces

- `claude project/README.md` version claims (kernel v1.2.2, skill v1.2.1.0) match both files.
- Four shared rule files are byte copies on both sides, as `claude project/README.md:107` and `SYNC.md:44` state.
- Knowledge counts, template counts, fixture counts and release-note counts in `README.md` all match the tree.

## Ruled Out

- **The parity method omits `sk-create-figjam`** -- ruled out: `SYNC.md:10` names both Flow Mode directories, which covers the 25 `sk-create-figjam`-sourced mirrors.
- **Kernel points at Knowledge files that no longer exist** -- ruled out: every `Product Owner - ... .md` name in the kernel resolves inside `claude project/knowledge/`.
- **`kernel-review.json` contradicts the review protocol** -- ruled out: it states it is a dated record and nothing reads it, and the README says the same.

## Verdict

No active P0 or P1 findings. Three P2 advisories: two documentation drifts a reader would act on, and one gate floor that is looser than its own definition.

## Next Focus

- Dimension: correctness (second pass, script and gate behaviour)
- Focus area: `scripts/build-plugin.py`, `scripts/vendor-sync.py`, `benchmark/gates/example_lint.py`, `benchmark/grader/*`, `benchmark/format/validate-output-format.cjs`
- Reason: routing and the Project mirror are covered; the declared focus names gate and script defects as the third area
- Rotation status: D1, D3 done; D1 second pass next
- Blocked/productive carry-forward: productive — running a read-only gate settled a parity question in one call
- Required evidence: file:line in the script plus the tree state that contradicts it
- Recovery note: do not re-enter the "count the docs" angle for already-verified counts; those held

Review verdict: PASS
