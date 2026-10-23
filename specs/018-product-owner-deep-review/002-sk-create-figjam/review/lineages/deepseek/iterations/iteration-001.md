# Iteration 1 — Correctness of the check scripts

## Dimension

- Dimension: D1 Correctness (logic of the Python checks, and thresholds a document states against the threshold the code enforces)
- Budget profile: verify (11–13 tool calls)
- Sources read this iteration: `specs/product-owner/018-product-owner-deep-review/002-sk-create-figjam/review/lineages/deepseek/steer.md` (rulings), `AI Systems/Product Owner/sk-create-figjam/SKILL.md`, `references/flow-mode.md`, `references/types/user-flow.md`, `references/types/process.md`, `references/types/architecture.md`, `references/types/state.md`, `references/types/sequence.md`, `scripts/flow_check.py`, `scripts/figjam_checks/common.py`, `scripts/figjam_checks/layout.py`, `scripts/figjam_checks/flowchart.py`, `scripts/figjam_checks/sequence.py`, `scripts/figjam_checks/state.py`

## Files Reviewed

- `AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:47` — the `HEADER_KINDS` and `UNSUPPORTED` tables, `profile_of`, `check_block`, `check`, `self_test`
- `AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:47` — the budgets and the per-type rule tables
- `AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:236` — the node and connector budget comparison
- `AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:155` — the "no way in" rule
- `AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/sequence.py:24` — the arrow tables
- `AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/state.py:21` — the accepted directions
- `AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/common.py:21` — label, id, emoji and palette rules
- `AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/layout.py:24` — the five layout measures
- `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:298` — the shared budget every type inherits
- `AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:66` — the user-flow budget
- `AI Systems/Product Owner/sk-create-figjam/references/types/process.md:74` — the laned-process budget
- `AI Systems/Product Owner/sk-create-figjam/references/types/architecture.md:85` — the architecture budget and allowed-edge table
- `AI Systems/Product Owner/sk-create-figjam/references/types/state.md:60` — the state direction and budget
- `AI Systems/Product Owner/sk-create-figjam/references/types/sequence.md:67` — the sequence budget and id length

## Findings by Severity

### P0 Findings

None. No correctness failure was found that corrupts a written board or a shipped model.

### P1 Findings

1. **A user flow is never held to the 12-connector budget the shared rule states** — `scripts/figjam_checks/flowchart.py:47` — `BUDGET` sets `USER_FLOW: (9, None)`, and the comparison at `flowchart.py:236` reads `max_edges, None` as "no connector cap", so a user flow with any number of connectors passes as long as the layout measures agree. `references/flow-mode.md:298` says "sk-design-diagram's general budget of 9 nodes and 12 connectors applies unless the type sets its own", and `references/types/user-flow.md:66` sets only the node count ("At most 9 nodes"), so the user flow inherits the 12-connector cap. The only bound left on connectors is `layout.MAX_CONNECTORS_PER_STEP = 2.0` (`layout.py:35`), which is an average over steps and allows 18 connectors on a 9-node flow.
   - Finding class: contract drift between a doc-stated threshold and the enforcing code (missing validation).
   - Scope proof: `flowchart.py:47` defines the budget table for all three flowchart profiles; `flowchart.py:236-240` is the only place a node or connector budget is compared, and its `max_edges is not None` guard is the branch that skips the cap; `references/flow-mode.md:298` and `references/types/user-flow.md:66` are the two documents that state the rule. No other module in `scripts/figjam_checks/` reads `BUDGET`.
   - Affected surface hints: `scripts/figjam_checks/flowchart.py` (the budget table, or the comparison), `references/types/user-flow.md` and `references/flow-mode.md` if the intent is instead that a user flow sets its own connector budget.
   - Case: a nine-node user flow written as `start([Start]) --> a --> b --> c`, plus `start --> d`, `a --> e`, `b --> f`, `c --> g` and five further steps joined once each, reaches 13 or more connectors with `1.4` connectors per step and a rank width of 2. `flow_check.py` exits 0 and the model is written to the board, although `references/flow-mode.md:298` promises it will be refused at 12.
   - Claim adjudication: `{"type":"threshold-drift","claim":"the general 12-connector budget stated for every type is not enforced for a user flow","evidenceRefs":["AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:47","AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:236","AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:298","AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:66"],"counterevidenceSought":"read user-flow.md Section 4 and Section 3 in full for a type-specific connector budget, and grepped every reference for a second budget table; the only counting bound found was the per-step average in layout.py","alternativeExplanation":"the per-step average was intended as the user flow's own control, so the type does set its own budget","finalSeverity":"P1","confidence":0.82,"downgradeTrigger":"downgrade to P2 if user-flow.md is read as setting its own budget through the connectors-per-step average, or if the budget table is amended to record the intent"}`
   - Fix file: `scripts/figjam_checks/flowchart.py` (set the user-flow budget to `(9, 12)`, or state the intended cap in `references/types/user-flow.md:66` and here).

### P2 Findings

1. **The first declared node is excused from the "every step has a way in" rule whatever its shape** — `scripts/figjam_checks/flowchart.py:155` — the rule reads `if node.shape not in ENDPOINT_SHAPES and exits and not entries and node.id != first_id`, and `first_id` is `steps[0].id` (`flowchart.py:233`), the first *declared* step rather than the start stadium. A rectangle declared first with no entry therefore passes, and `references/types/user-flow.md:59` says "Only a stadium starts or ends the flow".
   - Finding class: rule waiver keyed to declaration order instead of shape.
   - Scope proof: `flowchart.py:233` sets `first_id` from the declaration order of non-container nodes; `flowchart.py:155` is the only consumer of `first_id`; `user-flow.md:59` states the shape rule. The exemption is needed only for a loop back into a start stadium, which `ENDPOINT_SHAPES` already excuses at the same line.
   - Affected surface hints: `scripts/figjam_checks/flowchart.py` (the two lines), possibly `references/types/process.md:70` where the same rule is restated.
   - Case: a model declared as `flowchart TD` / `a[Screen] --> b([End])` / `a --> c[Other]` has no start stadium at all; `a` has two exits and no entry, and because it is declared first the "has no way in: only a stadium starts a flow" problem is never raised, so the check reports only `c` and the model reaches the board without an entry point.
   - Fix file: `scripts/figjam_checks/flowchart.py:155` (exempt a start only when its shape is a stadium, and let the loop-back case stay covered by `ENDPOINT_SHAPES`).

2. **An arrow table in the sequence check is defined and never read** — `scripts/figjam_checks/sequence.py:24` — `ARROWS` maps the four accepted arrows to `request`, `return`, `async request` and `async return`, and no line in the file reads it; every decision uses `REFUSED_ARROWS` (`sequence.py:83`) or the `MESSAGE` pattern (`sequence.py:33`). A second table beside the real one invites a later edit to the wrong one.
   - Finding class: dead constant.
   - Scope proof: grepped the packet for `ARROWS`; the only hit inside `sequence.py` outside its definition is `REFUSED_ARROWS`, and no other module imports the name.
   - Affected surface hints: `scripts/figjam_checks/sequence.py` only.
   - Case: a maintainer correcting the accepted-arrow list edits `ARROWS` at line 24, and the check keeps accepting the four arrows the `MESSAGE` alternation encodes, so the correction silently does nothing.
   - Fix file: `scripts/figjam_checks/sequence.py:24` (delete the table, or use it where the arrow is classified).

3. **The state check accepts `TD` while its own message and the type reference allow `LR` or `TB`** — `scripts/figjam_checks/state.py:21` — `DIRECTIONS = {"LR", "TB", "TD"}` accepts three directions, the refusal at `state.py:46` reads "a state machine runs LR or TB", and `references/types/state.md:60` says "running `LR` or `TB`". A `stateDiagram-v2` with no `direction` line inherits the extractor default `TD` (`scripts/vendored/mermaid_extract.py:101`), so a state machine with no declared direction passes, and one written `direction TD` passes too.
   - Finding class: message and reference narrower than the accepted set (documented threshold differs from the code).
   - Scope proof: `state.py:21` and `state.py:45-46` are the whole direction rule for the state profile; `mermaid_extract.py:101` sets the `TD` default; `state.md:60` is the type's stated rule. Doubt stated: `TD` and `TB` are the same Mermaid direction, so the acceptance may be deliberate and only the wording is stale.
   - Affected surface hints: `scripts/figjam_checks/state.py:21` and `:46`, or `references/types/state.md:60` and `references/flow-mode.md` where the direction rule is restated.
   - Case: a model written `stateDiagram-v2` with transitions but no `direction` line is checked against `TD` and passes, so a state board is accepted without the `LR` or `TB` the type reference requires, and the refusal text would never name the direction it silently allowed.
   - Fix file: `scripts/figjam_checks/state.py:21` (drop `TD`, or fold it into `TB` the way `flowchart.direction_family` does) and align `:46` and `references/types/state.md:60` with the decision.

## Traceability Checks

| Protocol | Level | Status | Evidence | Notes |
|----------|-------|--------|----------|-------|
| `spec_code` | core | partial | `references/types/process.md:74` against `flowchart.py:48`; `references/types/architecture.md:85` against `flowchart.py:47`; `references/types/sequence.md:67-71` against `sequence.py:19-21`; `references/types/state.md:61-68` against `state.py:18-27` | The process lane budget (12/16), the architecture lanes and allowed-edge table, and the sequence and state budgets all match the code exactly. The user-flow connector budget does not, which is the P1 above. |
| `checklist_evidence` | core | partial | `references/quality-rubric.md:88` points at `scripts/figjam_checks/layout.py` for the layout budgets rather than restating numbers | The rubric defers to the code, so no drift is possible there. This packet has no `checklist.md`; the rubric is the checklist surface. |
| `skill_agent` | overlay | pass | `SKILL.md:169` (rule 3) requires `scripts/flow_check.py` before the write gate; `SKILL.md:198` names `--self-test` | The routing and the check gate agree. |
| `agent_cross_runtime` | overlay | notApplicable | no agent file in the packet | Steer §4 keeps `claude-plugin/` out of scope. |
| `feature_catalog_code` | overlay | pending | — | Deferred to D3. |
| `playbook_capability` | overlay | pending | — | `manual-testing-playbook/pre-write-check/` scenarios FJ-014, FJ-043 assert budgets that this iteration read only in passing. |

## Edge Cases

- `references/flow-mode.md:298` states one shared budget for every type; four of the seven types restate their own. The user flow restates only its node count, so the connector half of the shared rule has no owner — recorded as the P1 rather than as seven separate drifts.
- `layout.MAX_LABEL_AVERAGE` is `MAX_LABEL_CHARS * 7 // 10` = 28 (`layout.py:33`), a derived number no document restates; the rubric defers to `layout.py`, so this is consistent by construction and not a finding.
- The `fj` route cannot draw most of these types (`references/flow-mode.md:356`), so no check-script finding here can change a `fj` write.

## Confirmed-Clean Surfaces

- `flow_check.py:64` `HEADER_KINDS` covers every grammar the packet names, and `UNSUPPORTED` (`:67`) matches the list at `references/flow-mode.md:151`.
- `flowchart.py:52` `ALLOWED_ARCHITECTURE_EDGES` is the same ten rows as the table at `references/types/architecture.md:57-68`.
- `flowchart.py:48` `LANED_PROCESS_BUDGET = (12, 16)` matches `references/types/process.md:74`; `MIN_LANES, MAX_LANES = 2, 6` (`:49`) matches the same line and `references/flow-mode.md:319`.
- `sequence.py:19-21` `MAX_PARTICIPANTS = 5`, `MAX_MESSAGES = 12`, ids of 3 to 20 characters match `references/types/sequence.md:67-71`.
- `state.py:18-20` `MAX_STATES = 9`, `MAX_TRANSITIONS = 12`, `MAX_CHOICE_EXITS = 3` match `references/types/state.md:64-68`.
- `common.py:21` `MAX_LABEL_CHARS = 40` matches `references/flow-mode.md:296` and every type reference.

## Ruled Out

- **A missing header check for `graph TD`.** `flow_check.py:64` maps `graph` to the flowchart kind deliberately, and `references/types/user-flow.md:38` names only `flowchart`; the mapping is a legacy alias, not a hole.
- **`layout.closing_edges` failing to drop loop connectors.** The walk in `layout.py:53-74` marks every popped step closed and removes it from the open set, so a rank is computed on the acyclic remainder as the module docstring says; no rank inflation was found.
- **`common.hex_colour` mishandling an uppercase fill.** It lowercases before matching (`common.py:135-139`), so `#CDF4D3` is accepted as a palette fill.

## Next Dimension

- Dimension: D2 Security
- Focus area: `scripts/flow_check.py` file handling and `scripts/figjam_checks/fixtures.py`, plus the untrusted-source rules in `references/flow-mode.md` Section 4.
- Reason: iteration 1 spent its budget on thresholds; the security dimension has not been touched.
- Rotation status: D1 complete, D2 next.
- Blocked/productive carry-forward: the P1 is carried forward as an active finding and must not be re-counted as new.
- Required evidence: a resolving `[SOURCE: path:line]` per finding, and the input that reaches the wrong result.
- Recovery note: none.

## Assessment

- New findings ratio: 1.0 (`P1=1, P2=3`; weighted new 5+3=8 against weighted total 8, first iteration).
- Dimensions addressed: correctness.
- Novelty justification: every finding is a first record; the P1 is a doc-to-code threshold gap, not a refinement.

Review verdict: CONDITIONAL
