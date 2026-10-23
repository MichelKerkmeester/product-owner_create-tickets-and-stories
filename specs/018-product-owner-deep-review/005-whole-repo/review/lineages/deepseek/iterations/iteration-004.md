# Review Iteration 004 - Maintainability (with security folded in)

## Dispatcher

- Session: `fanout-deepseek-1792580494888-r714jg`, lineage `deepseek`, iteration 4 of 5
- Executor: cli-pi (deepseek-v4.1-flash), detached fan-out lineage; iteration executed in-process, no nested dispatch
- Target: `specs/product-owner/018-product-owner-deep-review/005-whole-repo`, reviewing the Product Owner tree named in `spec.md` Files to Change
- Sources consulted before this iteration: `steer.md`, the state log projection, the findings registry, the strategy file
- Focus selected from strategy Next Focus: maintainability of the playbooks, graders and guides, with the security dimension folded in

## Dimension

Maintainability: can a careful maintainer trust the guides, the playbook indexes and the quoted gate
outputs? Security: does anything in the tracked configuration leak a credential?

## Files Reviewed

- `AI Systems/Product Owner/manual-testing-playbook/manual-testing-playbook.md:1-30` and its 7 hub scenarios
- `AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/manual-testing-playbook.md:1-20`
- `AI Systems/Product Owner/benchmark/grader/README.md:1-20`
- `AI Systems/Product Owner/README.md:676-700` (the clone smoke matrix)
- `AI Systems/Product Owner/.env.example` and `.gitignore` (read whole)
- `AI Systems/Product Owner/AGENTS.md` (21 repository paths extracted and resolved)
- `AI Systems/Product Owner/graph-metadata.json` (read whole, 135 lines)
- `AI Systems/Product Owner/description.json`, `SKILL.md:14`, `mode-registry.json:3`, `hub-router.json:3` (version carriers)
- `AI Systems/Product Owner/benchmark/gates/example_lint.py` (read-only run)
- `AI Systems/Product Owner/steer.md` (lead rulings for this lineage)

## Findings by Severity

### P0 Findings

None.

### P1 Findings

None.

### P2 Findings

1. **The smoke matrix quotes 42 example files and the lint prints 49** -- AI Systems/Product Owner/README.md:683 -- The table's `example_lint.py` row gives the result as `PASSED 42 example files and the worked replies on both packagings`. A read-only run of the same command on this tree prints `PASSED 49 example files and the worked replies on both packagings` [SOURCE: benchmark/gates/example_lint.py:102]. The gap is the 7 FigJam source examples added with the Flow packet, which agrees with the coverage finding recorded against the gate in iteration 3, and it is the second stale expected output in the same table after the gold-row count.
   Finding class: documentation-count drift
   Scope proof: the command was run read-only and its output quoted verbatim; the README row was opened
   Affected surface hints: `AI Systems/Product Owner/README.md` smoke matrix, `example_lint.py` row
   Case: an operator runs the lint, reads 49 where the guide promised 42, and has to decide whether seven files arrived or seven were miscounted.

## Traceability Checks

| Protocol | Status | Evidence |
|----------|--------|----------|
| `spec_code` | pass | Root, playbook, grader and script paths named in `spec.md` exist and were read |
| `checklist_evidence` | notApplicable | No `checklist.md` in the staging packet |
| `skill_agent` | pass | The hub's four version carriers (`SKILL.md`, `description.json`, `mode-registry.json`, `hub-router.json`) all read 1.0.0.0 |
| `agent_cross_runtime` | notApplicable | No runtime mirror opened |
| `playbook_capability` | pass | Hub playbook holds 7 `hub-routing/` scenarios, the packet playbook holds 50 scenarios in 12 category folders, and README states both |
| `feature_catalog_code` | notApplicable | No feature catalog in the target |

## Integration Evidence

- `node .skilled/commands/doctor/scripts/parent-skill-check.cjs` against this hub reported every hard invariant PASS with zero warnings: 4 registered modes, packets resolving to real folders, discriminators complete, 13 unique aliases, matching `packetSkillName` frontmatter, transport axis consistent, router signals and vocabulary classes complete, every router resource resolving, leaf-manifest regeneration byte-identical, ROUTER.md conforming, and the four version carriers agreeing. This is the authoritative hub gate and it is green on the reviewed tree.
- Every `.skilled`, `AI Systems`, packet, `benchmark` and `scripts` path named in `AGENTS.md` (21 of them) resolves on disk.
- Every `references/`, `assets/`, `scripts/` and `manual-testing-playbook/` path cited in the four packet `SKILL.md` files resolves, apart from two literal `<type>` placeholders that are pattern text rather than paths.
- `benchmark/grader/README.md` says the folder holds five files and the folder holds exactly five.

## Edge Cases

- **Security sweep found no credential.** `.env.example` carries four empty ClickUp keys, `.gitignore` ignores `.env` and `.env.*` while re-including `.env.example`, and a scan for bearer tokens, API keys and ClickUp URLs in tracked sources returned only the playbook's documented placeholder URL and fake keys inside `specs/` (out of scope).
- **The working tree is mid-change.** `git status` in the Product Owner repository shows 88 modified, 4 deleted and 54 untracked paths, including the hub files themselves, so the reviewed content is working-tree state rather than a committed release. This also explains why the shared parity gate refuses to run.
- **`run_gates.sh` row unverified.** The smoke matrix promises `all 12 gates pass`; the aggregate runner was not executed because it runs self-tests that stage temporary trees, so that one row is unverified rather than confirmed.
- **`benchmark/format/fixtures/` holds 19 entries but no JSON manifest**, so the "59 cases" half of its row was not independently counted.

## Confirmed-Clean Surfaces

- Hub structure: the doctor gate's 58 invariants pass, so packet registration, routing tables, leaf manifest and version agreement need no change.
- Playbook indexes: both state their scope, their persistence contract and which packet owns artifact behaviour, and neither claims the other's scenarios.
- `graph-metadata.json` describes the four-packet hub, its packets and its transport split as the tree is today.

## Ruled Out

- **The hub playbook duplicates the packet playbook** -- ruled out: the hub index limits itself to mode resolution and names the packet as the owner of artifact behaviour.
- **The hub and packet `changelog/` folders collide** -- ruled out: each holds its own release line under the versioning split `SKILL.md:14` declares, and the doctor check 13b/13d passes on both.
- **A stale path set in `AGENTS.md`** -- ruled out: all 21 extracted paths resolve.

## Verdict

No P0 or P1 findings were raised in this iteration. One P2 advisory joins the earlier documentation drifts. The active set still carries the P1 that iteration 3 raised, so the PASS line below follows the per-iteration mapping (this iteration added no P0/P1), while iteration 5 adjudicates the active set. The structural and security surfaces checked here are clean.

## Next Focus

- Dimension: correctness and security, final cross-check pass
- Focus area: re-read every active P1/P2 at its cited line, confirm each still reproduces, and close any that the working tree has already fixed; then check `benchmark/format/` fixture-count claims and `run_gates.sh` aggregate claims
- Reason: last iteration before synthesis; the registry must be honest about what is active
- Rotation status: D1 twice, D3, D4; final adjudication next
- Blocked/productive carry-forward: productive -- running a gate read-only produced verifiable evidence each time; do not re-enter already-swept hub, parity or playbook angles
- Required evidence: each finding re-opened at its line, with a pass/fail on whether it still reproduces
- Recovery note: none

Review verdict: PASS
