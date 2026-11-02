# Iteration 3 — Traceability: routing, cross-references and the vendored copy's provenance

## Dimension

- Dimension: D3 Traceability (SKILL.md routing against the files that exist, cross-reference integrity, contract parity between references, templates and examples)
- Budget profile: verify (11–13 tool calls)
- Sources read this iteration: `specs/product-owner/018-product-owner-deep-review/002-sk-create-figjam/review/lineages/deepseek/steer.md` (rulings), `SKILL.md`, `README.md`, `references/flow-mode.md`, `references/quality-rubric.md` (headings and rule lines), `references/hybrid-workflow.md` (headings), `assets/flow-templates.md` (headings), `references/types/{user-flow,process,architecture,sequence,state,er,gantt}.md`, `assets/templates/` and `assets/examples/` (executed), `manual-testing-playbook/manual-testing-playbook.md` and its 52 scenario files, `AI Systems/Product Owner/vendor.json`, `AI Systems/Product Owner/ROUTER.md:33`

## Files Reviewed

- `AI Systems/Product Owner/sk-create-figjam/SKILL.md:64` — the resource loading table
- `AI Systems/Product Owner/sk-create-figjam/SKILL.md:141` — the packet tree
- `AI Systems/Product Owner/sk-create-figjam/README.md:49` — the same tree, written a second time
- `AI Systems/Product Owner/sk-create-figjam/README.md:62` — the vendored-copy line
- `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:20` — the file's own loading condition
- `AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:19` — the extension file's loading condition
- `AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:18` — the rubric's loading condition
- `AI Systems/Product Owner/vendor.json` — the `mermaid-extract` package entry
- `AI Systems/Product Owner/ROUTER.md:33` — the FLOW leaves the hub loads
- `scripts/figjam_checks/gantt.py:19` and `references/types/gantt.md:67` — the gantt budget pair
- `scripts/figjam_checks/er.py:19` and `references/types/er.md:72` — the ER budget pair
- `assets/examples/*.md` and `assets/templates/*.md` — executed through `scripts/flow_check.py`

## Findings by Severity

### P0 Findings

None.

### P1 Findings

None new. `R1-P1-001` remains active and is carried.

### P2 Findings

1. **`references/flow-mode.md` declares itself `ON-DEMAND` while the contract loads it on every Flow route** — `references/flow-mode.md:20` — the file's own header reads `**Loading Condition:** ON-DEMAND`, and `SKILL.md:64` puts the same file in the `CONDITIONAL` row with the note "on every Flow route", beside `assets/flow-templates.md`. `assets/flow-templates.md:18` agrees with `SKILL.md` (`CONDITIONAL, with references/flow-mode.md whenever Flow intent is selected`), and every type reference and the rubric are `CONDITIONAL` too (`references/quality-rubric.md:18`, `references/types/user-flow.md:18` and its six siblings). The packet writes the level token two ways as well: `ON-DEMAND` here against `ON_DEMAND` at `SKILL.md:65` and `references/hybrid-workflow.md:19`.
   - Finding class: routing-contract drift between a file's own header and the routing table that loads it.
   - Scope proof: read the loading-condition header of all twelve reference files and the two asset files; `SKILL.md:61-65` is the only loading table, and `references/flow-mode.md:20` is the only place the level is stated for the workflow file. `AI Systems/Product Owner/ROUTER.md:33` confirms the hub loads the flow pair for every Flow route, which is the `CONDITIONAL` behaviour.
   - Affected surface hints: `references/flow-mode.md:20` (the header), or `SKILL.md:64` if the table is the side that should change; the token spelling appears at `SKILL.md:65` and `references/hybrid-workflow.md:19`.
   - Case: a router that resolves a resource's level from the file's own header reads `ON-DEMAND` for `references/flow-mode.md` and defers it until the user asks, so a `$flow` request runs with `assets/flow-templates.md` and no workflow, intake or gate section at all.
   - Claim adjudication: `{"type":"routing-drift","claim":"the workflow reference declares a loading level that contradicts the routing table which loads it","evidenceRefs":["AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:20","AI Systems/Product Owner/sk-create-figjam/SKILL.md:64","AI Systems/Product Owner/sk-create-figjam/assets/flow-templates.md:18","AI Systems/Product Owner/ROUTER.md:33"],"counterevidenceSought":"read every sibling reference's header and the ROUTER FLOW leaf list to see whether any document agrees with ON-DEMAND","alternativeExplanation":"ON-DEMAND was meant to say the file is read after the route is chosen rather than at every request, so the two levels describe the same moment","finalSeverity":"P2","confidence":0.85,"downgradeTrigger":"none foreseen; raise only if a runtime is shown to resolve loading from the reference header instead of SKILL.md"}`
   - Fix file: `references/flow-mode.md:20`.

2. **The contract says the vendored extractor is kept in step through `vendor.json` but never says where that manifest lives, and the README names a different control** — `SKILL.md:156` — the packet tree lists `scripts/vendored/` as "the Mermaid extractor, a byte copy kept in step through vendor.json", and the tree describes packet-internal paths only, so a reader looks inside the packet and finds no such file. The manifest is at `AI Systems/Product Owner/vendor.json` (package `mermaid-extract`, `local_path: sk-create-figjam/scripts/vendored`, `upstream_path: .skilled/skills/sk-design/sk-design-diagram/scripts`, `base_commit: 330427cf…`), and `README.md:62` names a third thing again — `../scripts/vendor-sync.py`, the tool rather than the manifest. `scripts/flow_check.py:28-29` repeats the bare `vendor.json` name. I checked the control itself and it currently holds: the vendored file's SHA-256 is `4562fe4d…59756d`, exactly the digest the manifest records, and the upstream file at the recorded commit has the same digest, so this is a naming-location gap rather than drift.
   - Finding class: provenance documentation that names a path the packet does not contain, and two documents naming two different controls for one file.
   - Scope proof: `ls` of `scripts/vendored/` shows `mermaid_extract.py` alone; `find` for `vendor.json` returns nothing inside the packet and returns `AI Systems/Product Owner/vendor.json` at the hub root; parsed that manifest's `mermaid-extract` entry; hashed both copies.
   - Affected surface hints: `SKILL.md:156`, `README.md:62`, `scripts/flow_check.py:28`, and `references/flow-mode.md` where the extractor is introduced.
   - Case: a reviewer looking for the drift control inside the packet finds no `vendor.json`, concludes the byte copy is unmanaged, and hand-edits `mermaid_extract.py` to fix a parser bug — the edit then silently differs from upstream with nothing recording why, because the manifest that would have caught it points at a path the reviewer never found.
   - Fix file: `SKILL.md:156` (name `../../vendor.json`, or say the manifest lives at the Product Owner root) and `README.md:62` (name the manifest beside the sync tool).

## Traceability Checks

| Protocol | Level | Status | Evidence | Notes |
|----------|-------|--------|----------|-------|
| `spec_code` | core | partial | `scripts/figjam_checks/gantt.py:19-21` against `references/types/gantt.md:67`; `scripts/figjam_checks/er.py:19-21` against `references/types/er.md:72` | The gantt budget (12 tasks, sections past 8, 5 parallel) and the ER budget (9 entities, 12 relationships, 10 attributes) both match exactly. The user-flow connector budget remains the one mismatch in the packet. |
| `checklist_evidence` | core | pass | `AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md` against its 52 scenario files | Every one of the 52 scenario files is linked from the index, no link is dead, and the 43 `FJ-` ids appear in both directions. |
| `skill_agent` | overlay | pass | `SKILL.md:224` and `SKILL.md:64` against `AI Systems/Product Owner/ROUTER.md:33` | The hub's FLOW leaves are `sk-create-figjam/references/flow-mode.md` and `assets/flow-templates.md`, exactly the pair the packet claims. |
| `agent_cross_runtime` | overlay | notApplicable | no agent file in the packet | Steer §4 keeps `claude-plugin/` out of scope. |
| `feature_catalog_code` | overlay | notApplicable | the packet ships no `feature-catalog/` | Its siblings do; this packet does not, and nothing in it claims one. |
| `playbook_capability` | overlay | pass | `manual-testing-playbook/pre-write-check/user-flow-over-budget.md` expects `10 nodes, at most 9: split the flow`, which is the message at `flowchart.py:238`; `manual-testing-playbook/pre-write-check/layout-measures-refuse-a-wide-rank.md` expects `a rank holds 5 steps, at most 4: split the flow so a rank reads at a glance`, which is `layout.py:134-135` | Two scenarios checked verbatim against the code's wording. |

## Edge Cases

- Executing `scripts/flow_check.py` writes nothing: `PYTHONDONTWRITEBYTECODE=1` kept `__pycache__` out of `scripts/figjam_checks/`, confirmed by a post-run `find` for `*.pyc` and `__pycache__` that returned nothing. Every shipped model was run, not read.
- The style guide's palette record was recomputed from `common.ACCENT_PAIRS` and `LANE_PAIR` rather than trusted: ten rows, every fill-to-stroke pair identical to the code's table, and all ten contrast pairs measuring to the recorded ratio.
- The reading-distance budgets (`references/flow-mode.md:279-285`, and each type's `Wall` counts) have no path through `scripts/flow_check.py`, which takes one file argument and no distance option (`flow_check.py:244-251`). Not recorded as a finding: no document claims the check enforces the dial, and `references/flow-mode.md:287` puts the setting in the gate's own message.

## Confirmed-Clean Surfaces

- Zero broken local links across the packet: every `[…](…)` target in all 81 markdown files resolves, including the eight `../` links into the hub.
- Section cross-references resolve: `references/flow-mode.md:24` and `:61` point at `assets/flow-templates.md` Sections 3 and 5, which exist; `:65` and `:99` point at `references/quality-rubric.md` Sections 2 and 3, which exist; `:342` and `:437` point at `references/hybrid-workflow.md` Sections 7 and 8, which exist.
- Every shipped model passes: all seven examples and all six templates under `assets/` exit 0 when checked, and each example's quoted `Read-back:` line matches what the check actually prints (for example `assets/examples/user-flow-fernhouse-return.md` quotes `9 nodes and 9 connectors, widest rank 2 steps, longest path 7 steps, 1.0 connectors per step, labels average 16 characters, 0 crossing pairs`, which is the live output).
- The style guide's `FIGJAM_PALETTE` block matches `common.ACCENT_PAIRS` and `LANE_PAIR` exactly, and all ten contrast pairs measure true.
- `references/types/user-flow.md:20` and its six siblings each name the asset they pair with, and each named file exists; `user-flow` correctly pairs with `assets/flow-templates.md` because it has no template of its own, which matches `SKILL.md:102-106`.

## Ruled Out

- **The vendored copy has drifted from its manifest.** Hashed it: `4562fe4d0aab108e179a5f522c1b857a28b66226ad8ff5cec6dfb9b40059756d`, identical to the manifest and to the upstream file at `base_commit 330427cf…`.
- **A missing template for the user flow.** `SKILL.md:104-105` deliberately withholds `assets/templates/user-flow.md`, and `assets/flow-templates.md` carries the five user-flow patterns instead.
- **The reading-distance budgets being unenforced.** No document claims `flow_check.py` sees the dial, and `references/flow-mode.md:287` puts the setting in the gate message.

## Next Dimension

- Dimension: D4 Maintainability
- Focus area: the duplicated packet tree in `SKILL.md:141-157` and `README.md:49-63`, `scripts/figjam_checks/fixtures.py` as one 739-line module, and the shape of `flow_check.py`'s dispatch.
- Reason: three dimensions are covered; nothing has judged the cost of the next change.
- Rotation status: D1, D2 and D3 complete, D4 next.
- Blocked/productive carry-forward: `R1-P1-001` remains active; the two P2s from this iteration must not be re-counted.
- Required evidence: a resolving `[SOURCE: path:line]` per finding, and the file a fix changes.
- Recovery note: none.

## Assessment

- New findings ratio: 0.17 (weighted new 2 against weighted total 12).
- Dimensions addressed: traceability.
- Novelty justification: both findings are first records. The three routing, index and example checks that came back clean are reported as clean surfaces rather than as findings.

Review verdict: CONDITIONAL
