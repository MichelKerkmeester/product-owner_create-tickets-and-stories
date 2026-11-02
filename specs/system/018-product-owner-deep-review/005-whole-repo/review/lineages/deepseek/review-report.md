# Review Report - Product Owner whole-repository review (deepseek lineage)

- Session: `fanout-deepseek-1792580494888-r714jg`, lineage `deepseek`, generation 1, lineageMode `new`
- Review target: `specs/product-owner/018-product-owner-deep-review/005-whole-repo` (review setup binds the Product Owner tree named in its Files to Change)
- Iterations: 5 of 5, `stopPolicy = max-iterations`, stopReason `maxIterationsReached`
- Dimensions covered: correctness (twice), traceability, maintainability, security (folded into iteration 4)

## 1. Executive Summary

- **Overall verdict: CONDITIONAL**
- `hasAdvisories`: false (the verdict is not PASS; the eight P2 items ride alongside the active P1)
- Active findings: **P0 = 0, P1 = 1, P2 = 8** (9 total, 0 resolved)
- Review scope: the Product Owner repository's root hub files, the Claude Project kernel and its 62 knowledge files, `scripts/`, `benchmark/`, `manual-testing-playbook/`, and how the four packets (`sk-product-owner`, `sk-create-figjam`, `mcp-click-up`, `mcp-figma`) fit together
- What held: the hub's structural gate passes every invariant, the 62 Project pairs compare, all 37 stage-one gold rows route as expected, all 19 `ROUTER.md` leaf paths resolve and are registered, and no credential is committed
- What did not: one builder ships 53 files its own rule excludes; the rest are documentation that states counts, versions or paths the tree no longer has, plus two gate-perimeter gaps

## 2. Planning Trigger

`/speckit:plan` is required: the active P1 is a code change in `scripts/build-plugin.py`.

```json
{
  "triggered": true,
  "verdict": "CONDITIONAL",
  "hasAdvisories": false,
  "activeFindings": [
    {"id": "R3-P1-001", "severity": "P1", "file": "AI Systems/Product Owner/scripts/build-plugin.py:57", "title": "The plugin build ships the FigJam playbook its own rule excludes", "findingClass": "builder-contract violation", "fixCompleteness": "add Path(\"sk-create-figjam/manual-testing-playbook\") to UNSHIPPED, rebuild, and confirm the shipped file count drops by 53"},
    {"id": "R1-P2-001", "severity": "P2", "file": "AI Systems/Product Owner/ROUTER.md:43", "title": "ROUTER.md says a replay parses its python block, and no gate replays it", "findingClass": "documentation-behaviour drift", "fixCompleteness": "either qualify the sentence or add the parser the sentence promises"},
    {"id": "R1-P2-002", "severity": "P2", "file": "AI Systems/Product Owner/ROUTER.md:19", "title": "The named contract boundary resolves only under a parent directory ROUTER.md does not name", "findingClass": "path-reference drift", "fixCompleteness": "name the full path .skilled/skills/sk-doc/sk-create-skill/scripts/lib/leaf-resource-contract.cjs"},
    {"id": "R2-P2-001", "severity": "P2", "file": "AI Systems/Product Owner/SYNC.md:18", "title": "SYNC.md still names kernel v1.0.0 and skill 1.0.0.0 while both files carry later versions", "findingClass": "documentation-version drift", "fixCompleteness": "state v1.2.2 and 1.2.1.0, or point at the H1 and frontmatter as the authority"},
    {"id": "R2-P2-002", "severity": "P2", "file": "AI Systems/Product Owner/README.md:684", "title": "Three documents say 33 gold rows and the gate replays 37", "findingClass": "documentation-count drift", "fixCompleteness": "update README.md:684, README.md:776 and benchmark/README.md:15"},
    {"id": "R2-P2-003", "severity": "P2", "file": "AI Systems/Product Owner/benchmark/gates/rule_parity.py:160", "title": "The rule-parity gate declares a floor of 1 for a rule seven pairs teach", "findingClass": "gate-declaration drift", "fixCompleteness": "raise min_pairs to the measured count, or restate what min_pairs means"},
    {"id": "R3-P2-001", "severity": "P2", "file": "AI Systems/Product Owner/scripts/build-plugin.py:8", "title": "The builder's description of the tracked plugin folder names a README that is not there", "findingClass": "documentation-path drift", "fixCompleteness": "drop the README from the sentence or track one"},
    {"id": "R3-P2-002", "severity": "P2", "file": "AI Systems/Product Owner/benchmark/gates/example_lint.py:49", "title": "The example lint reads every Project example mirror but only the product-owner source examples", "findingClass": "gate-coverage gap", "fixCompleteness": "lint sk-create-figjam/assets/examples as well, or state the one-packet perimeter"},
    {"id": "R4-P2-001", "severity": "P2", "file": "AI Systems/Product Owner/README.md:683", "title": "The smoke matrix quotes 42 example files and the lint prints 49", "findingClass": "documentation-count drift", "fixCompleteness": "replace 42 with 49 in the smoke matrix"}
  ],
  "remediationWorkstreams": [
    {"order": 1, "severity": "P1", "workstream": "Builder exclusion", "findings": ["R3-P1-001"], "surface": "AI Systems/Product Owner/scripts/build-plugin.py"},
    {"order": 2, "severity": "P2", "workstream": "Guide and parity-note truth", "findings": ["R2-P2-001", "R2-P2-002", "R4-P2-001", "R3-P2-001"], "surface": "README.md, benchmark/README.md, SYNC.md, scripts/build-plugin.py docstring"},
    {"order": 3, "severity": "P2", "workstream": "Gate strictness and coverage", "findings": ["R2-P2-003", "R3-P2-002"], "surface": "benchmark/gates/rule_parity.py, benchmark/gates/example_lint.py"},
    {"order": 4, "severity": "P2", "workstream": "Router document precision", "findings": ["R1-P2-001", "R1-P2-002"], "surface": "ROUTER.md"}
  ],
  "specSeed": [
    "Record that the plugin ships skills only, and that a first-party packet's manual-testing-playbook is excluded while a vendored packet ships whole",
    "Record that the hub ROUTER.md leaf map is documentation, while the executable router lives in sk-product-owner/references/router-contract.md"
  ],
  "planSeed": [
    "Add sk-create-figjam/manual-testing-playbook to UNSHIPPED and rebuild the plugin; assert the shipped file count and re-run --self-test",
    "Correct the smoke-matrix expected outputs (37 gold rows, 49 example files) and the benchmark README row count",
    "Update SYNC.md's live-version sentence to v1.2.2 and 1.2.1.0",
    "Raise the flow rule's min_pairs to the measured pair count, or document the floor semantics it actually uses",
    "Extend example_lint.py's EXAMPLES sweep to sk-create-figjam/assets/examples",
    "Name the full leaf-resource-contract path and qualify or implement the ROUTER.md replay claim"
  ],
  "findingClasses": ["builder-contract violation", "documentation-behaviour drift", "path-reference drift", "documentation-version drift", "documentation-count drift", "gate-declaration drift", "documentation-path drift", "gate-coverage gap"],
  "affectedSurfacesSeed": [
    "AI Systems/Product Owner/scripts/build-plugin.py",
    "AI Systems/Product Owner/ROUTER.md",
    "AI Systems/Product Owner/SYNC.md",
    "AI Systems/Product Owner/README.md",
    "AI Systems/Product Owner/benchmark/README.md",
    "AI Systems/Product Owner/benchmark/gates/rule_parity.py",
    "AI Systems/Product Owner/benchmark/gates/example_lint.py"
  ],
  "fixCompletenessRequired": true
}
```

## 3. Active Finding Registry

| ID | Sev | Dimension | Title | File:line | Disposition |
|----|-----|-----------|-------|-----------|-------------|
| R3-P1-001 | P1 | correctness | The plugin build ships the FigJam playbook its own rule excludes | `AI Systems/Product Owner/scripts/build-plugin.py:57` | active, confirmed twice |
| R1-P2-001 | P2 | correctness | ROUTER.md says a replay parses its python block, and no gate replays it | `AI Systems/Product Owner/ROUTER.md:43` | active |
| R1-P2-002 | P2 | correctness | The named contract boundary resolves only under a parent directory ROUTER.md does not name | `AI Systems/Product Owner/ROUTER.md:19` | active |
| R2-P2-001 | P2 | traceability | SYNC.md still names kernel v1.0.0 and skill 1.0.0.0 while both files carry later versions | `AI Systems/Product Owner/SYNC.md:18` | active |
| R2-P2-002 | P2 | traceability | Three documents say 33 gold rows and the gate replays 37 | `AI Systems/Product Owner/README.md:684` | active |
| R2-P2-003 | P2 | traceability | The rule-parity gate declares a floor of 1 for a rule seven pairs teach | `AI Systems/Product Owner/benchmark/gates/rule_parity.py:160` | active |
| R3-P2-001 | P2 | correctness | The builder's description of the tracked plugin folder names a README that is not there | `AI Systems/Product Owner/scripts/build-plugin.py:8` | active |
| R3-P2-002 | P2 | correctness | The example lint reads every Project example mirror but only the product-owner source examples | `AI Systems/Product Owner/benchmark/gates/example_lint.py:49` | active |
| R4-P2-001 | P2 | maintainability | The smoke matrix quotes 42 example files and the lint prints 49 | `AI Systems/Product Owner/README.md:683` | active |

## 4. Remediation Workstreams

1. **Builder exclusion (P1).** Add `Path("sk-create-figjam/manual-testing-playbook")` to `UNSHIPPED` in `scripts/build-plugin.py`, rebuild `claude-plugin/skills`, and confirm the shipped tree loses the 53 playbook files while `--self-test` still refuses every planted condition.
2. **Guide and parity-note truth (P2).** Correct the two stale expected outputs in the README smoke matrix, the gold-row count in `benchmark/README.md`, the live-version sentence in `SYNC.md`, and the builder docstring's README claim.
3. **Gate strictness and coverage (P2).** Raise or redefine the flow rule's `min_pairs`, and extend the example lint to the FigJam packet's source examples.
4. **Router document precision (P2).** Name the full `leaf-resource-contract.cjs` path and either qualify or implement the replay claim in `ROUTER.md` section 3.

## 5. Spec Seed

- The plugin contract is "skills only": hub files plus the four packets, with the Product Owner and FigJam playbooks and both packet changelogs excluded, and a vendored packet shipping whole because its files are hashed.
- The hub `ROUTER.md` is the human and replay-facing leaf map, but the executable router the differential gate proves is `sk-product-owner/references/router-contract.md`.
- Version authority for the hub is `SKILL.md` frontmatter, mirrored by `description.json`, `mode-registry.json` and `hub-router.json`; the packet keeps its own release line and the kernel keeps its H1.

## 6. Plan Seed

- Fix the builder exclusion, rebuild and re-run its self-test.
- Bring the smoke matrix, the benchmark README and `SYNC.md` back in line with the counts and versions the tree reports.
- Decide whether `min_pairs` is a measured count or a floor, and make the flow entry match that decision.
- Extend the example lint to `sk-create-figjam/assets/examples` so the FigJam worked examples are read on both sides.

## 7. Traceability Status

| Protocol | Level | Status | Notes |
|----------|-------|--------|-------|
| `spec_code` | core | pass | Every path in `spec.md` Files to Change exists; out-of-scope paths were not opened |
| `checklist_evidence` | core | notApplicable | The staging packet carries no `checklist.md` |
| `skill_agent` | overlay | pass | Registry `packetSkillName` matches each packet's `SKILL.md` frontmatter; kernel v1.2.2 matches skill 1.2.1.0 in the Project README |
| `agent_cross_runtime` | overlay | notApplicable | `.skilled` is an external checkout reached by symlink; no runtime mirror was in scope |
| `feature_catalog_code` | overlay | notApplicable | No feature catalog in the target |
| `playbook_capability` | overlay | pass | Hub playbook 7 scenarios, packet playbook 50 across 12 folders, both stated by the guide |

`AC_COVERAGE`: disabled. This staging packet is not a Level 2+ spec folder with a checklist and an in-progress implementation summary, so the advisory signal does not apply.

`resource_map_present` is false for this packet, so the Resource Map Coverage Gate is skipped; no `resource-map.md` exists to audit `target_files` against.

## Dimension Expansion Map

- Completed pivots: 0 (no pivot was needed; each iteration's next focus was planned at init)
- Failed pivots: 0
- Audited overrides: 0
- Selected review directions: hub routing against the packets (iteration 1), Project mirror and parity claims (iteration 2), builders and gates (iteration 3), playbooks, guides and security (iteration 4), adjudication (iteration 5)
- Swept directions: hub inventory, false-prefix commands, graph identity, parity-method coverage, `$email`, the parity runner's verdict, the playbook/changelog duplication question
- Remaining frontier: `benchmark/format/` case-level count (59) and the aggregate `run_gates.sh` result were not independently verified; the Product Owner working tree is mid-change, so a commit may close several P2 items without code edits

## 8. Deferred Items

- **Vendored packet hygiene** is not reviewed here: `mcp-click-up` and `mcp-figma` are byte copies whose truth lives upstream, and `scripts/vendor-sync.py status` was not run because the shared declaration is dirty.
- **Historical run output** under `benchmark/reports/` and `export/` is out of scope by the review setup.
- **`benchmark/format/` case count.** The 19 fixture files were counted; the 59 cases they drive were not.
- **Aggregate gate run.** `bash benchmark/gates/run_gates.sh` stages temporary trees, so it was not executed; its documented "all 12 gates pass" is unverified rather than contradicted.

## 9. Search Ledger

- `searchCoverage`: required bug classes for this review were documentation-count drift, documentation-version drift, path-reference drift, gate-declaration drift, gate-coverage gap, builder-contract violation and credential exposure. All were searched; the credential class was ruled out; the rest produced the nine findings above.
- `candidateCoverage`: 30 scope entries from `spec.md` were visited across five iterations (hub files, Project kernel and knowledge, scripts, benchmark gates/router/format/grader/parity, both playbooks, the four packets).
- `searchDebt`: the two items in Deferred Items.
- `ruledOutCandidates`: hub inventory drift, false-prefix command handling, graph identity, parity-method packet coverage, kernel Knowledge pointers, playbook/changelog duplication, `vendor-sync.py` containment, build determinism, credential exposure.
- `cleanSearchProof`: read-only runs of `check_hub.py` (37 gold rows, 0 mismatches), `rule_parity.py` (62 of 62 pairs, 8 rules), `example_lint.py` (49 files), and `parent-skill-check.cjs` (58 invariants, 0 warnings).
- `hasSearchDebt`: true (two unresolved verification items, neither affecting the verdict).

## 10. Audit Appendix

- **Convergence:** `convergenceMode` is off by configuration, so the loop ran to `maxIterations = 5`; novelty was 2, 3, 3, 1 and 0 new findings per iteration.
- **Coverage:** correctness ×2, traceability, maintainability, security; all four dimensions have at least one full iteration.
- **Adjudication:** all nine active findings were re-opened at their cited lines in iteration 5 and all nine reproduced; nothing was downgraded or resolved.
- **Sources reviewed:** 30 scope entries, plus context reads in `.skilled` (the doctor gate, the shared parity gate, and the reduction/closeout scripts) used only as evidence and never as review targets.
- **Write discipline:** every artifact this lineage created lives under `specs/product-owner/018-product-owner-deep-review/005-whole-repo/review/lineages/deepseek/`; no reviewed file was modified.
