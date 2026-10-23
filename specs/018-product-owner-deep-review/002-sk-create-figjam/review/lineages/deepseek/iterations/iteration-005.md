# Iteration 5 — Consolidation and adversarial replay

## Dimension

- Dimension: consolidation (all four dimensions covered in iterations 1 to 4; this pass replays the active findings against current file content and closes the last open directions before synthesis)
- Budget profile: adjudicate (8–10 tool calls)
- Sources read this iteration: `specs/product-owner/018-product-owner-deep-review/002-sk-create-figjam/review/lineages/deepseek/steer.md` (rulings), `scripts/figjam_checks/flowchart.py` (the P1's two sites, re-read), `references/types/user-flow.md` (the P1's two sites, re-read), `references/flow-mode.md:298` (the P1's governing rule, re-read), `references/style-guide.md:105-125` (gates and recorded departures), `scripts/figjam_checks/common.py` (palette tables), and three scratch models run through `scripts/flow_check.py`

## Files Reviewed

- `AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:47` — the budget table, re-read
- `AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/flowchart.py:236` — the budget comparison, re-read
- `AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:66` — the user-flow budget, re-read
- `AI Systems/Product Owner/sk-create-figjam/references/types/user-flow.md:80` — the budget section, re-read
- `AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:298` — the shared budget rule, re-read
- `AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:105` — the gates and the recorded departures
- `AI Systems/Product Owner/sk-create-figjam/scripts/figjam_checks/common.py:46` — `ACCENT_PAIRS`, `LANE_PAIR`, `CHARCOAL`, `CANVAS`
- `specs/product-owner/018-product-owner-deep-review/002-sk-create-figjam/review/lineages/deepseek/.scratch/thirteen-connectors.md` — a nine-node, thirteen-connector user flow written for this replay
- `specs/product-owner/018-product-owner-deep-review/002-sk-create-figjam/review/lineages/deepseek/.scratch/pie.md` — an unsupported header
- `specs/product-owner/018-product-owner-deep-review/002-sk-create-figjam/review/lineages/deepseek/.scratch/graph-header.md`, `.scratch/type-on-sequence.md`, `.scratch/arch-td.md` — three dispatch cases

## Findings by Severity

### P0 Findings

None. No P0 was raised in any iteration, so there is no P0 to replay.

### P1 Findings

1. **`R1-P1-001` re-confirmed by execution: a user flow is never held to the 12-connector budget the shared rule states** — `scripts/figjam_checks/flowchart.py:47` — re-read the two code sites and the two document sites. The table still reads `BUDGET = {USER_FLOW: (9, None), PROCESS: (9, 12), ARCHITECTURE: (9, 12)}` and the comparison still guards on `if max_edges is not None`, so the user-flow branch has no connector cap. `references/types/user-flow.md:66` still sets only "At most 9 nodes", and `references/flow-mode.md:298` still says "sk-design-diagram's general budget of 9 nodes and 12 connectors applies unless the type sets its own". This iteration ran the check on a model built for the purpose — nine nodes, thirteen connectors, no decision, one crossing, labels averaging four characters — and the check printed `diagram 1, user flow: ok, 9 nodes and 13 connectors, widest rank 2 steps, longest path 6 steps, 1.4 connectors per step, labels average 4 characters, 1 crossing pairs` and `PASSED 1 diagram(s)`, exit 0. The documented cap is 12, so the model the rule forbids is written.
   - Case: the scratch model above, which is inside every other rule the type holds.
   - Counterevidence: re-read `references/types/user-flow.md` Sections 2 to 4 for a type-specific connector count; Section 2 says only that every connector is a solid one-way arrow, and Section 4 discusses nodes alone. No document gives the user flow its own connector budget.
   - Severity held at P1: the gate a document promises does not exist for this type, and a board drawn from the model has four connectors more than the packet's own specification allows.

### P2 Findings

The ten P2 findings from iterations 1 to 4 were re-checked against current file content and all still stand; none is resolved and none is upgraded. Two were replayed in full this iteration:

- **`R1-P2-001`** — `scripts/figjam_checks/flowchart.py:155` still exempts `node.id == first_id`, and `first_id` is still `steps[0].id` at `:233`, so the first-declared-node waiver is unchanged.
- **`R2-P2-002`** — `scripts/flow_check.py:225-233` still skips a shipped model with no fence and prints `SKIP` for an absent mirror, and the summary at `:239-241` still counts results rather than the shipped set.

No new P2 was raised this iteration.

## Traceability Checks

| Protocol | Level | Status | Evidence | Notes |
|----------|-------|--------|----------|-------|
| `spec_code` | core | partial | `references/flow-mode.md:298` against `scripts/figjam_checks/flowchart.py:47`, re-read and executed | The only budget mismatch in the packet, now proved by a passing run rather than by reading alone. |
| `checklist_evidence` | core | pass | `AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/` index against its 52 files | Complete in both directions (iteration 3). |
| `skill_agent` | overlay | pass | `SKILL.md:169` requires the check before the gate, and the check runs | Verified by executing it on five models this session. |
| `agent_cross_runtime` | overlay | notApplicable | no agent file in the packet | Steer §4 keeps `claude-plugin/` out of scope. |
| `feature_catalog_code` | overlay | notApplicable | the packet ships no `feature-catalog/` | — |
| `playbook_capability` | overlay | pass | `manual-testing-playbook/pre-write-check/` scenario wording against live output | `FJ-014`'s and `FJ-043`'s expected strings are the strings the code prints. |

## Edge Cases

- The scratch models were written inside this lineage under `.scratch/`, never in the reviewed packet, and `PYTHONDONTWRITEBYTECODE=1` kept `__pycache__` out of `scripts/figjam_checks/`; a post-run search for `*.pyc` and `__pycache__` under the packet returned nothing.
- The style-guide numbers in `references/style-guide.md:105-125` were recomputed rather than trusted: white on violet 4.57:1, white on `#3DADFF` 2.44:1, white on `#66D575` 1.85:1 and the lane stroke 2.1:1 all measure exactly as recorded, and the seven accent strokes under the mark gate run 1.53:1 to 2.65:1 as the table says.
- An unresolved ambiguity, carried rather than closed: `scripts/figjam_checks/state.py:21` accepts `TD` while `references/types/state.md:60` says `LR` or `TB`. If `TD` is the intended synonym of `TB`, the fix is wording in two places; if not, the check accepts a direction the type forbids. `R1-P2-003` holds the question open.

## Confirmed-Clean Surfaces

- The dispatch table behaves as documented on five inputs: `graph TD` is read as a user flow and passes; a `%% type: process` on a `sequenceDiagram` is refused with "the header already names the kind"; an unsupported `pie` block is refused with exit 1, which is the code the README promises for a rule failure rather than exit 2; an architecture in `TD` is refused with the left-to-right message; and a legitimate three-node flow passes.
- No write escaped the packet or the lineage: the reviewed packet has no new file, no new `__pycache__` and no modified byte file.

## Ruled Out

- **A wrong exit code for an unsupported kind.** A `pie` model exits 1 with "a pie block: the board generator does not draw it", matching `README.md:43`, so the extractor never turns an unsupported header into an exit-2 "unreadable".
- **The style guide's seven-stroke arithmetic being wrong.** `ACCENT_PAIRS` holds nine strokes; seven measure under the 3.0 mark gate (1.53 to 2.65) and the two above it are violet `#874FFF` at 4.57 and pink `#F849C1` at 3.13, which is exactly what the table claims.
- **`graph` being an accepted header hole.** It is read as a flowchart, which the packet treats as a user flow, and it passes; no document claims `graph` is refused.

## Next Dimension

- Dimension: none. All four dimensions are covered and the iteration cap is reached.
- Focus area: synthesis. Every finding above is active and unverified by a human.
- Reason: `config.maxIterations` is 5 and this is iteration 5.
- Rotation status: D1, D2, D3 and D4 complete.
- Blocked/productive carry-forward: `R1-P1-001` and ten P2 findings carry into the report.
- Required evidence: the report's verdict is recomputed from the findings registry, not from this line.
- Recovery note: none.

## Assessment

- New findings ratio: 0.0 (no new finding this iteration).
- Dimensions addressed: consolidation across all four.
- Novelty justification: the value of this pass is confirmation, not novelty: the P1 is now proved by a passing run, and three candidate findings were disproved by execution.

Review verdict: CONDITIONAL
