# Iteration 4 — Maintainability: duplicated declarations and the cost of the next change

## Dimension

- Dimension: D4 Maintainability (documentation quality, pattern compliance, duplication, safe follow-on change cost)
- Budget profile: scan (9–11 tool calls)
- Sources read this iteration: `specs/product-owner/018-product-owner-deep-review/002-sk-create-figjam/review/lineages/deepseek/steer.md` (rulings), `SKILL.md`, `README.md`, `references/flow-mode.md` (structure and section count), `references/quality-rubric.md`, `references/style-guide.md`, `references/hybrid-workflow.md` (lengths and headings), `scripts/flow_check.py`, `scripts/figjam_checks/fixtures.py`, `assets/examples/` and `assets/templates/` (inventory), `AI Systems/Product Owner/claude project/knowledge/` (inventory of the mirrored Flow files)

## Files Reviewed

- `AI Systems/Product Owner/sk-create-figjam/SKILL.md:77` — `DIAGRAM_TYPES` and the resource constants beside it
- `AI Systems/Product Owner/sk-create-figjam/SKILL.md:141` — the packet tree
- `AI Systems/Product Owner/sk-create-figjam/README.md:49` — the second copy of that tree
- `AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:63` — the dispatch tables
- `AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/fixtures.py:12` — `GOOD`, and `:158` `PLANTED`
- `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md` — the whole file's shape, counted in sections and lines
- `AI Systems/Product Owner/sk-create-figjam/references/hybrid-workflow.md:25` — as the model for a concern split into its own conditional reference
- `AI Systems/Product Owner/sk-create-figjam/assets/templates/` and `assets/examples/` — the per-type inventory

## Findings by Severity

### P0 Findings

None.

### P1 Findings

None new. `R1-P1-001` remains active and is carried.

### P2 Findings

1. **The packet's file map is written twice and the two copies already disagree** — `SKILL.md:141` and `README.md:49` — `SKILL.md:141-157` lists the packet as a directory tree and `README.md:49-63` lists the same packet as a two-column table. They already diverge on the two lines that carried the most detail: the vendored extractor is "a byte copy kept in step through vendor.json" in `SKILL.md:156` and "a byte copy … that `../scripts/vendor-sync.py` keeps in step" in `README.md:62`, and the check is "the pre-write check for every type and its self-test" in `SKILL.md:154` against "Its self-test plants one defect per rule and checks every template, example and the palette record" in `README.md:60`. Neither copy is derived from the other or from disk, so both must be edited by hand on every file added to the packet.
   - Finding class: duplicated structural documentation that has diverged.
   - Scope proof: read both maps in full and diffed them line by line; the packet has eight top-level entries and both maps carry all eight, so the divergence is in the descriptions rather than in the set of files.
   - Affected surface hints: `SKILL.md:141-157`, `README.md:49-63`.
   - Case: a contributor adds a ninth `scripts/` module. `SKILL.md`'s tree must be edited and `README.md`'s table carries the same information under a different wording, so the second copy is the one that goes stale, exactly as the vendor line did here.
   - Fix file: `README.md:49-63` (link to `SKILL.md` Section 3 instead of restating the tree).

2. **The seven-type vocabulary is declared twice with nothing asserting that the two agree** — `SKILL.md:77` — `DIAGRAM_TYPES = ("user-flow", "process", "architecture", "sequence", "state", "er", "gantt")` in the routing pseudocode and `NAMES` at `scripts/flow_check.py:70-71` keyed `{"user-flow", "process", "architecture", "sequence", "state", "er", "gantt"}` are the same vocabulary held in two files. They agree today. Nothing tests it: `--self-test` iterates `fixtures.GOOD` and `fixtures.PLANTED`, and no fixture asserts that the type list equals the router's, while `references/types/` and `assets/examples/` are keyed to the same seven names without an assertion either.
   - Finding class: unasserted duplicate declaration of a shared vocabulary.
   - Scope proof: `SKILL.md:77` is the only type tuple in the contract; `flow_check.py:63` `FLOWCHART_TYPES` and `:70` `NAMES` are the dispatch keys; `references/types/` holds exactly seven files and `assets/examples/` exactly seven, one per name; grepped for any assertion over the type list and found none.
   - Affected surface hints: `SKILL.md:70-80`, `scripts/flow_check.py:63-71`, and `--self-test` if the fix is an assertion.
   - Case: a type is added to the router's tuple and its reference is written, but `NAMES` is missed. `SKILL.md` routes the request and loads the reference, and `flow_check.py:148` then prints `diagram 1, unknown` for a model the packet told the reader to draw.
   - Fix file: `scripts/flow_check.py` (derive the dispatch key set from one source, or assert the two lists agree in `--self-test`).

3. **The largest reference is loaded on every Flow route, against the packet's own tiered-loading design** — `SKILL.md:64` — `references/flow-mode.md` is 441 lines in nine sections, and the routing table puts it in the `CONDITIONAL` row "on every Flow route" beside `assets/flow-templates.md`. The packet's own pattern is to split a concern that only applies to one step into its own file: `references/hybrid-workflow.md` (216 lines) loads only "when the gate names an extension" (`references/hybrid-workflow.md:19`), and the rubric and style guide load only before the gate. The write routes, the read-back and the delivery reply in `references/flow-mode.md` Sections 6 to 8 apply only after the model passes, yet they travel in the same file as the intake that every route needs.
   - Finding class: loading-tier mismatch between a file's size and the moment its content is needed.
   - Scope proof: counted the nine section headings and the 441 lines of `references/flow-mode.md`; compared with `references/quality-rubric.md` (124 lines), `references/style-guide.md` (162) and `references/hybrid-workflow.md` (216), each of which is scoped to one moment; read `SKILL.md:61-65` for the tier each file is assigned.
   - Affected surface hints: `references/flow-mode.md` (Sections 6 to 8), `SKILL.md:64-65`.
   - Case: a `$flow` request that turns out to be a Doc question still loads 441 lines of workflow, write routes and delivery rules before the packet's `When NOT to Use` check can hand it back, and every such request pays that cost.
   - Fix file: `references/flow-mode.md` and `SKILL.md:64-65` (split Sections 6 to 8 into an `ON_DEMAND` reference, as `hybrid-workflow.md` was split). Doubt stated: the packet may have chosen one workflow file deliberately, so this is recorded at P2 as a cost rather than a defect.

## Traceability Checks

| Protocol | Level | Status | Evidence | Notes |
|----------|-------|--------|----------|-------|
| `spec_code` | core | partial | `references/types/` and `assets/examples/` inventory against `SKILL.md:77` | Seven references and seven examples, one per type, all present. The vocabulary is complete; finding 2 is about the assertion, not the set. |
| `checklist_evidence` | core | partial | `scripts/figjam_checks/fixtures.py:12` `GOOD` (9 models) and `:158` `PLANTED` (106 defects) | The self-test data is broader than the packet's own claim that it plants "one defect per rule": 106 planted models against roughly 40 rules, so a rule may be planted more than once. Not a defect, so no finding. |
| `skill_agent` | overlay | pass | `references/hybrid-workflow.md:19` as the worked example of a tiered split | The pattern the packet states is the pattern it follows for the extension reference. |
| `agent_cross_runtime` | overlay | notApplicable | no agent file in the packet | Steer §4 keeps `claude-plugin/` out of scope. |
| `feature_catalog_code` | overlay | notApplicable | the packet ships no `feature-catalog/` | — |
| `playbook_capability` | overlay | partial | `manual-testing-playbook/` holds 52 scenario files for 43 ids | The playbook's own index is complete (iteration 3); the 52-to-43 ratio means nine files carry no id, which the index does not explain. |

## Edge Cases

- `scripts/figjam_checks/fixtures.py` (739 lines, 106 planted models) ships inside the runtime rule package but is imported only inside `self_test()` (`scripts/flow_check.py:211`), so production never pays for it. Recorded as a clean surface, not a finding.
- The self-test reads Project mirrors from `AI Systems/Product Owner/claude project/knowledge/` (`flow_check.py:173-179`). The seven mirror files it globs exist with the exact names it expects (`Product Owner - Assets - Flow Templates.md`, six `… - Flow Templates - <Type>.md`, seven `Product Owner - Examples - Flow - <Type>.md`), so the coupling resolves today; the skip behaviour is already recorded as `R2-P2-002`.
- Doubt stated on finding 3: the packet may deliberately keep one workflow file so a reader follows one narrative end to end, which would make the load cost the accepted price of coherence.

## Confirmed-Clean Surfaces

- No dead module: every import in `scripts/flow_check.py:54-60` is used, and `scripts/figjam_checks/__init__.py` is empty by design.
- The shared helpers are genuinely shared rather than copied: `length_problems`, `id_problems`, `raw_problems` and `statements` live in `common.py` and are imported by the flowchart, sequence, state, ER and gantt modules; `MAX_LABEL_CHARS` is defined once and derived into `MAX_LABEL_AVERAGE` in `layout.py:33`.
- Each rule module owns one diagram grammar with a docstring naming what the generator drops for that grammar; none of them reaches into another module's tables.

## Ruled Out

- **`fixtures.py` bloating the runtime package.** It is imported lazily inside `--self-test` and never on the check path.
- **`flow_check.py`'s dispatch chain being unmaintainable.** The four tables at `:63-71` are small, colocated and keyed by the same nine header words; the cost is the duplication in finding 2, not the branch structure.
- **The nine-section workflow file hiding a second concern that belongs in a type reference.** Sections 6 to 8 are route mechanics shared by every type, so their home is the workflow; finding 3 is about when they load, not where they live.

## Next Dimension

- Dimension: consolidation and adversarial replay (all four dimensions covered; iteration 5 re-checks the active P1 and the three highest-severity P2s rather than opening a new direction)
- Focus area: `R1-P1-001` (user-flow connector budget), `R1-P2-001` (first-node waiver), `R2-P2-002` (self-test skip), and the synthesis inputs.
- Reason: the cap is reached after this iteration, so the last pass must confirm the carried findings still stand rather than add new ones.
- Rotation status: D1 to D4 complete.
- Blocked/productive carry-forward: every finding above stays active.
- Required evidence: a re-read of the cited line for each replayed finding.
- Recovery note: none.

## Assessment

- New findings ratio: 0.2 (weighted new 3 against weighted total 15).
- Dimensions addressed: maintainability.
- Novelty justification: all three are first records and each names a different duplication or load decision.

Review verdict: CONDITIONAL
