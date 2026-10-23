# Deep Review Report — Product Owner sk-product-owner

- Session: `fanout-deepseek-1792580414886-kf3maf` (generation 1, lineageMode new, lineage `deepseek`)
- Review target: `AI Systems/Product Owner/sk-product-owner`
- Target type: skill packet
- Spec folder: `specs/product-owner/018-product-owner-deep-review/001-sk-product-owner`
- Executor: `cli-pi` / `deepseek-v4.1-flash`
- Iterations: 5 of 5 — stop reason `maxIterationsReached` (stop policy `max-iterations`, convergence treated as telemetry)

## 1. Executive Summary

- **Overall verdict: CONDITIONAL**
- **hasAdvisories: false** (advisories only apply to a PASS verdict)
- **Active findings: 15 — P0 0, P1 2, P2 13**
- **Review scope:** the full default packet — `SKILL.md`, all 13 `references/`, all 6 `assets/` scaffolds, all 22 `assets/examples/` worked artifacts, and the `manual-testing-playbook/` hub plus its 50 scenarios. Roughly 12,000 lines across 100 markdown files.
- **What the review found:** the packet's behavioral rules are unusually consistent — routing thresholds, quality floors, house grammar and delivery shape agree across the bootstrap, the mode references and the templates, and 779 of 787 resolvable relative links land. The two P1s are integrity defects at the packet's own seams: a quality rubric that imports the Claude Project's delivery proof into the skill's export path, and a router contract that advertises itself as the oracle's exact copy while being a different program. Thirteen P2s cover a stale count, a missing directory, root-relative citations, three over-budget examples, a duplicated contract preamble, kernel fragments in the rubric, a missing preamble, unstated Quick behavior, one unresolvable example bundle, an untrusted-input gap, an unconstrained export slug, and one uncovered Doc shape in the playbook.
- **Release posture:** nothing blocks shipping for safety. Both P1s mislead whoever maintains the packet next, and one of them can produce a delivery that claims success without a saved file, which is the failure the packet exists to prevent.

## 2. Planning Trigger

`/speckit:plan` is recommended: the verdict is CONDITIONAL, so remediation planning is required before the two P1 findings can be closed.

```json
{
  "Planning Packet": true,
  "triggered": true,
  "verdict": "CONDITIONAL",
  "hasAdvisories": false,
  "activeFindings": {
    "P0": 0,
    "P1": 2,
    "P2": 13,
    "total": 15,
    "ids": ["DR-DS-001", "DR-DS-004", "DR-DS-002", "DR-DS-003", "DR-DS-005", "DR-DS-006", "DR-DS-007", "DR-DS-008", "DR-DS-009", "DR-DS-010", "DR-DS-011", "DR-DS-012", "DR-DS-013", "DR-DS-014", "DR-DS-015"]
  },
  "remediationWorkstreams": [
    {"id": "WS-1", "severity": "P1", "title": "Remove Project-side delivery proof from the skill rubric", "findings": ["DR-DS-001"], "files": ["references/quality-scoring.md"], "dependsOn": []},
    {"id": "WS-2", "severity": "P1", "title": "Reconcile the router contract with the oracle it names", "findings": ["DR-DS-004", "DR-DS-005", "DR-DS-006", "DR-DS-010"], "files": ["references/router-contract.md", "references/routing.md"], "dependsOn": []},
    {"id": "WS-3", "severity": "P2", "title": "Correct bootstrap documentation defects", "findings": ["DR-DS-002", "DR-DS-003", "DR-DS-012"], "files": ["SKILL.md", "references/routing.md"], "dependsOn": []},
    {"id": "WS-4", "severity": "P2", "title": "Normalize path bases and example links", "findings": ["DR-DS-007", "DR-DS-008"], "files": ["SKILL.md", "references/routing.md", "references/router-contract.md", "assets/examples/doc/doc-example-readme.md"], "dependsOn": ["WS-2"]},
    {"id": "WS-5", "severity": "P2", "title": "Bring examples and authoring hygiene inside the packet's own rules", "findings": ["DR-DS-009", "DR-DS-011"], "files": ["assets/examples/doc/doc-example-how-it-works.md", "assets/examples/doc/doc-example-behavior-reference.md", "assets/examples/story/story-example-complete.md", "references/quality-scoring.md"], "dependsOn": ["WS-1"]},
    {"id": "WS-6", "severity": "P2", "title": "Close the input-trust and path-construction gaps", "findings": ["DR-DS-013", "DR-DS-014"], "files": ["SKILL.md", "references/task-mode.md", "references/bug-mode.md", "references/story-mode.md"], "dependsOn": []},
    {"id": "WS-7", "severity": "P2", "title": "Add the missing Narrative overview scenario", "findings": ["DR-DS-015"], "files": ["manual-testing-playbook/skill-document-modes/", "manual-testing-playbook/project-document-modes/", "manual-testing-playbook/manual-testing-playbook.md"], "dependsOn": []}
  ],
  "specSeed": [
    "The skill packet owns its own delivery proof: a saved file plus read-back. Any Project-only delivery wording belongs in claude project/, not in a skill reference.",
    "A document that names itself the exact copy of an executable oracle must be regenerated from that oracle or stop claiming exactness.",
    "Every reference opens on the same four preamble fields, and every export filename the user can influence is slug-constrained.",
    "Playbook scenario coverage tracks the packet's own shape list, including the Narrative overview Doc shape."
  ],
  "planSeed": [
    "Rewrite the quality-scoring.md pre-reply checklist so the skill's delivery proof is the read-back path, and move the Deliverable Block wording to the Project kernel.",
    "Regenerate references/router-contract.md's Python fence from benchmark/router/route_contract.py, or narrow both the `:17/:24/:33` claims and SKILL.md:77 to the table-parity check that differential.py actually performs.",
    "State the Quick Task fallback in references/routing.md beside the confidence bands, or delete it from the contract and the oracle.",
    "Fix SKILL.md:67 (shared cards are regular files under references/), SKILL.md:319 (50 scenarios), and add the four preamble fields to references/routing.md.",
    "Convert the eight `benchmark/router/…` citations to `../../benchmark/router/…` or state the base once in Section 2.",
    "Bring the three over-cap examples inside 1,400 words, or exempt them explicitly in SKILL.md:175.",
    "Delete the four `The kernel points here` blocks from references/quality-scoring.md and keep them in the Project kernel.",
    "Add one ALWAYS rule and one NEVER rule to SKILL.md treating pasted source material as data, never instructions.",
    "Constrain the export `[description]` slug in task, bug and story modes the way Doc Mode already does.",
    "Add one Narrative overview scenario per playbook set and update the hub's composition line."
  ],
  "findingClasses": ["contract-contradiction", "contract-drift", "doc-path-claim", "stale-count", "path-base-ambiguity", "example-link", "example-budget", "duplicated-text", "mixed-authorship", "doc-standard-gap", "missing-untrusted-input-rule", "path-construction-gap", "playbook-coverage-gap"],
  "affectedSurfacesSeed": ["references/quality-scoring.md", "references/router-contract.md", "references/routing.md", "SKILL.md", "assets/examples/doc/doc-example-how-it-works.md", "assets/examples/doc/doc-example-behavior-reference.md", "assets/examples/doc/doc-example-readme.md", "assets/examples/story/story-example-complete.md", "references/task-mode.md", "references/bug-mode.md", "references/story-mode.md", "manual-testing-playbook/skill-document-modes/", "manual-testing-playbook/project-document-modes/"],
  "fixCompletenessRequired": true
}
```

## 3. Active Finding Registry

| ID | Sev | Title | Dimension | File:line | Disposition |
|----|-----|-------|-----------|-----------|-------------|
| DR-DS-001 | P1 | The skill's quality rubric carries Project-only delivery rules that contradict the skill export contract | correctness | `references/quality-scoring.md:160` | active |
| DR-DS-004 | P1 | The router contract claims to be the exact source the oracle is checked against, but its Python fence and the oracle are different programs | traceability | `references/router-contract.md:17` | active |
| DR-DS-002 | P2 | The bootstrap describes the four shared cards as living in a directory that does not exist in the packet | correctness | `SKILL.md:67` | active |
| DR-DS-003 | P2 | The related-resource line understates the manual-testing playbook by two scenarios | correctness | `SKILL.md:319` | active |
| DR-DS-005 | P2 | The contract's ALWAYS lane loads two of the six resources the bootstrap marks ALWAYS and skips its own first entry by name | traceability | `references/router-contract.md:137` | active |
| DR-DS-006 | P2 | Quick energy falls back to Task in the contract but not in the routing rules | traceability | `references/router-contract.md:851` | active |
| DR-DS-007 | P2 | Oracle paths are written root-relative inside packet-relative prose | traceability | `SKILL.md:44` | active |
| DR-DS-008 | P2 | The README worked example links five bundle siblings the examples tree does not ship | traceability | `assets/examples/doc/doc-example-readme.md:60` | active |
| DR-DS-009 | P2 | Three worked examples break the packet's own word caps | maintainability | `assets/examples/doc/doc-example-how-it-works.md:10` | active |
| DR-DS-010 | P2 | The router contract repeats its own opening paragraph and its Section 1 payload | maintainability | `references/router-contract.md:33` | active |
| DR-DS-011 | P2 | The quality rubric carries kernel-owned index fragments including a delivery-prohibition list starting at item 7 | maintainability | `references/quality-scoring.md:183` | active |
| DR-DS-012 | P2 | The routing reference omits the preamble fields the packet requires of every reference | maintainability | `references/routing.md:1` | active |
| DR-DS-013 | P2 | Nothing in the packet treats pasted source material as untrusted data | security | `SKILL.md:30` | active |
| DR-DS-014 | P2 | The export filename description is unconstrained in three of the four modes that build a path from user wording | security | `references/task-mode.md:22` | active |
| DR-DS-015 | P2 | The playbook has no scenario for the Narrative overview Doc shape | traceability | `manual-testing-playbook/manual-testing-playbook.md:24` | active |

Per-finding detail — evidence, impact, fix recommendation, finding class, scope proof and affected surface hints — lives in the iteration file that raised it (`iterations/iteration-001.md` through `iteration-005.md`) and in the reduced registry `deep-review-findings-registry.json`.

### P1 detail

**DR-DS-001 — Project delivery proof inside the skill rubric.** Evidence: `references/quality-scoring.md:160` ("The Deliverable Block appears before commentary and is the only claimed delivery evidence"), `:161` and `:187`; contradicted by `SKILL.md:127` (read the exact export path, a path string alone does not pass) and `SKILL.md:170` (Flow is the one exception). Impact: a skill route that consults the rubric can claim a rendered block as delivery and skip the export, exactly the state the packet forbids. Fix: rewrite the checklist's delivery lines to the skill's read-back proof; keep the Project wording in `claude project/`. Fix-completeness: the fix is done only when the rubric contains no unqualified Project-only delivery requirement and the kernel still carries its own.

**DR-DS-004 — Router contract is not the oracle it names.** Evidence: `references/router-contract.md:17` and `:33` claim the fence is "the exact source `benchmark/router/differential.py` executes to prove `benchmark/router/route_contract.py` never drifts from it"; `SKILL.md:77` repeats it. The fence at `:41-832` is 2,992 code tokens against the oracle's 3,598, with disjoint function-name sets and different constant sets. Impact: the packet's stated drift invariant cannot hold, and a maintainer gets no signal when the prose and the oracle separate. Fix: regenerate the fence from the oracle, or narrow the claim to what `differential.py` actually checks. Fix-completeness: done only when a comparison of the fence and the oracle either matches or the claim describes the narrower check.

## 4. Remediation Workstreams

**P0 — none.**

**P1 — before the next packet release**

1. **WS-1** Remove Project-side delivery proof from `references/quality-scoring.md` (DR-DS-001). Touches one file; verify no other reference states the export-equivalent path as a general rule.
2. **WS-2** Reconcile `references/router-contract.md` with `benchmark/router/route_contract.py` (DR-DS-004), then align the ALWAYS lane (DR-DS-005), the Quick fallback statement (DR-DS-006) and the duplicated preamble (DR-DS-010). One file plus `references/routing.md` for the Quick rule.

**P2 — advisory, group by file**

3. **WS-3** Bootstrap documentation: `SKILL.md:67`, `SKILL.md:319`, `references/routing.md` preamble fields (DR-DS-002, DR-DS-003, DR-DS-012).
4. **WS-4** Path bases and example links: the eight `benchmark/router/…` citations and the README example's reading map (DR-DS-007, DR-DS-008).
5. **WS-5** Examples and authoring hygiene: three over-cap examples, the kernel fragments in the rubric (DR-DS-009, DR-DS-011).
6. **WS-6** Input trust and export slug: one ALWAYS and one NEVER rule in `SKILL.md`, one shared slug rule across the three export contracts (DR-DS-013, DR-DS-014).
7. **WS-7** Playbook: one Narrative overview scenario per set and the hub composition line (DR-DS-015).

## 5. Spec Seed

- The packet owns its delivery proof: saved file plus read-back. Project-only wording is kernel-only.
- A document that claims to be the exact copy of an executable oracle must be regenerated from it or stop claiming exactness.
- Every reference opens on Loading Condition, Purpose, Scope and Output Path; every user-influenced path component is slug-constrained.
- Pasted source material is data, never instructions, and that rule is stated in the bootstrap rather than implied.
- Playbook coverage mirrors the packet's own shape list, so a shape with worked examples also has a scenario with a PASS/FAIL contract.

## 6. Plan Seed

1. Rewrite the `references/quality-scoring.md` delivery checks to the skill proof and drop the kernel pointers.
2. Regenerate or re-scope `references/router-contract.md` and record which gate actually compares the two.
3. State the Quick Task fallback in `references/routing.md` beside the bands, or remove it from the contract.
4. Fix `SKILL.md:67`, `SKILL.md:319`, and add the four preamble fields to `references/routing.md`.
5. Convert the eight oracle citations to `../../benchmark/router/…` or state the base once.
6. Bring three examples inside 1,400 words or exempt them by rule.
7. Delete the duplicated opening paragraph in `references/router-contract.md`.
8. Add the untrusted-input rule and the shared export-slug rule.
9. Add the Narrative overview scenario to both playbook sets.
10. After the fixes, re-run this review to confirm the two P1s close and the P2 count drops.

## 7. Traceability Status

### Core Protocols

| Protocol | Status | Evidence | Unresolved drift |
|----------|--------|----------|------------------|
| `spec_code` | partial | `specs/product-owner/018-product-owner-deep-review/001-sk-product-owner/spec.md:13` declares `AI Systems/Product Owner/sk-product-owner/` in scope; all 15 findings land inside it. | The staging spec carries no acceptance criteria, so fidelity is scored on scope only. |
| `checklist_evidence` | fail | The packet's own gates at `SKILL.md:263-271` require template compliance, HVR, export-before-reply and the routing-drift invariant. | DR-DS-001 breaks the export gate's own authority; DR-DS-004 breaks the drift invariant stated at `SKILL.md:44`. |

### Overlay Protocols

| Protocol | Status | Evidence | Unresolved drift |
|----------|--------|----------|------------------|
| `skill_agent` | pass | `SKILL.md:229-234` names the packet as the executable identity; no agent definition in the system loads it differently. | None. |
| `agent_cross_runtime` | notApplicable | The target declares no runtime mirror; `SKILL.md:310` and `README.md:415` place the Project packaging outside it. | None. |
| `feature_catalog_code` | notApplicable | No feature catalog exists in this packet. | None. |
| `playbook_capability` | partial | 50 scenarios across 12 category folders, 403 in-range line anchors, both runtimes mirrored, every mode represented. | DR-DS-015: no Narrative overview scenario. |

`AC_COVERAGE`: exempt. The target is a skill packet, not a Level 2+ spec folder with a checklist, so the advisory signal does not apply.

### Resource Map Coverage Gate

Skipped: `specs/product-owner/018-product-owner-deep-review/001-sk-product-owner/resource-map.md` does not exist, so `resource_map_present` is false and the gate is not part of this run.

## 8. Deferred Items

- **Line-number anchor fragility in the playbook.** 403 anchors into `AGENTS.md`, `Custom Instructions.md`, `SKILL.md` and the mode references are current and in range, but any edit to those files invalidates them silently. No finding is recorded because nothing is stale today; a stable-heading scheme would remove the risk.
- **`references/conciseness.md` section numbering gaps.** The file jumps 5 → 7 → 8 → 12. Every internal citation resolves, so this is cosmetic.
- **Section-numbering and anchor cosmetics in `references/router-contract.md`.** The `## 1. OVERVIEW` duplication is covered by DR-DS-010; the rest is formatting.
- **Deeper Doc-shape scenario authoring.** Beyond the one missing shape, the doc scenarios' nine-field execution tables were read for consistency but not audited line by line; that is a follow-on task, not a finding.

## Dimension Expansion Map

- Completed pivots: 5 (correctness, traceability/paths, maintainability/templates, security, traceability/playbook).
- Failed pivots: 0.
- Audited overrides: 0 (no pivot override was requested or applied).
- Council artifact references: none — this is a single-lineage deep review, not a council run.
- Selected review directions, in order: bootstrap correctness → reference and path traceability → template and example consistency → input trust and export paths → playbook capability coverage.
- Saturated directions: routing thresholds, quality floors and house-grammar consistency, each verified twice and moved to Ruled Out.
- Remaining frontier: none. All four configured dimensions have at least one full iteration.

## 9. Search Ledger

- **Dimensions covered:** `correctness`, `traceability`, `maintainability`, `security` — 4 of 4.
- **Bug classes covered:** contract-contradiction, contract-drift, doc-path-claim, stale-count, path-base-ambiguity, example-link, example-budget, duplicated-text, mixed-authorship, doc-standard-gap, missing-untrusted-input-rule, path-construction-gap, playbook-coverage-gap.
- **Bug classes ruled out:** secret exposure, external-write gate failure, example grammar breach, scaffold divider breach, anchor drift, cross-runtime parity drift.
- **Search debt:** none (`searchDebtCount: 0` from the reducer).
- **Graph coverage mode:** `graphless_fallback`. The coverage graph was seeded from scope discovery only; every finding is backed by a direct read or an exact scan, and none relies on graph edges.
- **Candidate coverage:** every required bug class has at least one ledger row with cited evidence in `deltas/iter-00N.jsonl`.

## 10. Audit Appendix

### Convergence summary

- Stop policy `max-iterations` with `maxIterations: 5`; convergence was telemetry only, as the config declares, and no early stop was taken.
- `newFindingsRatio` by iteration: 1.00, 1.00, 1.00, 1.00, 1.00 — every iteration produced new findings, so no convergence claim is made. `convergenceScore: 0` in the registry is the reducer's untouched default for a run stopped at the ceiling, not a converged score.
- Adversarial replay at synthesis: both active P1 findings were re-read at their cited lines (`references/quality-scoring.md:160`, `references/router-contract.md:17`) and confirmed, not downgraded.

### Coverage summary

| Iteration | Dimension | Findings | Files touched |
|-----------|-----------|----------|---------------|
| 1 | correctness | 1 P1, 2 P2 | SKILL.md, routing.md, quality-scoring.md, conciseness.md, story-mode.md, doc-mode.md, playbook hub |
| 2 | traceability | 1 P1, 4 P2 | router-contract.md, routing.md, SKILL.md, doc-example-readme.md, oracle (read-only) |
| 3 | maintainability | 4 P2 | five scaffolds, interactive-response-templates.md, 22 examples, routing.md, quality-scoring.md |
| 4 | security | 2 P2 | SKILL.md, four export contracts, router-contract guard, push-target scenario, .gitignore/.env.example (read-only) |
| 5 | traceability (playbook) | 1 P2 | playbook hub, 50 scenarios, doc-mode.md |

### Ruled-out claims (consolidated)

Routing band boundaries agree across all three authorities; Story/Epic commands never conflict; `$quick` cannot bypass a Doc gate; rule 10 and rule 17 do not collide on bullet punctuation; example grammar (bullets, checkboxes, dividers, H1 shapes) is consistent across all 22 examples; no secret or live workspace link exists in the packet; the ClickUp write path is gated three times; the resource loader's traversal guard is sound; the playbook's line anchors are in range; the two playbook trees are name-for-name mirrors.

### Sources reviewed

`SKILL.md`; `README.md`; all 13 `references/*.md`; all 6 `assets/*.md`; all 9 `assets/examples/*/` groups (22 artifacts); `manual-testing-playbook/manual-testing-playbook.md` and its 50 scenarios; `benchmark/router/route_contract.py` and `benchmark/router/differential.py` (read-only, to test the packet's own claims); `AI Systems/Product Owner/AGENTS.md`, `.gitignore`, `.env.example`, `claude project/Custom Instructions.md` (read-only context, outside the fix scope).

### Review deviations

- **Single-writer lock not taken.** `phase_init/step_acquire_lock` was skipped: every fan-out lineage shares the same `spec_folder` packet id, so an acquire would either fail closed against a sibling lineage or block it. Lock ownership belongs to the fan-out dispatcher, which serialises cross-lineage work.
- **Nested dispatch never used.** Every iteration ran inside this process; no CLI, agent or sub-agent was spawned.
- **Write containment.** All writes landed under `specs/product-owner/018-product-owner-deep-review/001-sk-product-owner/review/lineages/deepseek/`: five iteration files, five deltas, one record per iteration under `prompts/`, the strategy, the registry and dashboard produced by the reducer, the config's terminal status flip, and this report. No file inside `AI Systems/Product Owner/sk-product-owner` was modified.
