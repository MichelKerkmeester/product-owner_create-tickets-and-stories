# Review Iteration 002 — Traceability (references and paths)

- Session: `fanout-deepseek-1792580414886-kf3maf` (generation 1, lineageMode new)
- Iteration: 2 of 5
- Dimension: traceability
- Stop policy: `max-iterations` (convergence is telemetry only)
- Review target: `AI Systems/Product Owner/sk-product-owner`

## Files Reviewed

- `AI Systems/Product Owner/sk-product-owner/references/router-contract.md:15-48`, `:136-152`, `:283-296`, `:706-725`, `:830-860` — preamble, fence constants, guard, ALWAYS loading loop, primary detection copy.
- `AI Systems/Product Owner/sk-product-owner/references/routing.md:1-81` — routing steps and thresholds, cited again for the Quick path.
- `AI Systems/Product Owner/sk-product-owner/SKILL.md:44`, `:71-77`, `:242` — the drift invariant, the ALWAYS lane, the oracle citations.
- `AI Systems/Product Owner/sk-product-owner/assets/examples/doc/doc-example-readme.md:50-64` — the only unresolved in-packet link group.
- Read-only context outside the target: `AI Systems/Product Owner/benchmark/router/route_contract.py:1-60`, `:492-503` and `AI Systems/Product Owner/benchmark/router/differential.py` function inventory — used only to test the packet document's claims about itself; recorded as provenance, never as a fix target.
- All 50 `manual-testing-playbook/*` files, `assets/*` and `references/*` were scanned mechanically for relative links (779 checked).

## Findings by Severity

### P0 Findings

None.

### P1 Findings

1. **The router contract claims to be the exact source the oracle is checked against, but its Python fence and the oracle are different programs** -- `AI Systems/Product Owner/sk-product-owner/references/router-contract.md:17` -- The file states, in its opening and again under Section 1, that it is "the exact source `benchmark/router/differential.py` executes to prove `benchmark/router/route_contract.py` never drifts from it" (:17, repeated verbatim at :33) and that it is "the exact algorithm `benchmark/router/route_contract.py` is checked against" (:24). `SKILL.md:77` repeats the claim and adds the invariant that "The code stays in that file alone". Direct comparison falsifies it: the fence at :41-832 tokenizes to 2992 tokens of code and the oracle at `benchmark/router/route_contract.py` to 3598, they share no function name (`route_product_owner_resources`, `finalize_artifact_route`, `detect_controls` in the fence; `route_request`, `detect_commands`, `detect_framing`, `runner` helpers in the oracle), and they carry different constant sets — the fence declares `RESOURCE_MAP` including an `ALWAYS` key and `DEFAULT_RESOURCE`/`UNKNOWN_FALLBACK_CHECKLIST`, while the oracle declares a top-level `ALWAYS`, `ON_DEMAND`, `ROUTE_FIELDS`, `ENERGY_VALUES` and nine `*_RE` guards the fence does not contain. The oracle's own module docstring (`route_contract.py:1-25`) describes three fixed failure classes and a Quick fallback the fence never states. A maintainer who trusts the packet gets a contract that cannot be the drift proof it advertises, and any gate that compared the two would fail.

```
Finding class: contract-drift
Scope proof: The claim and the fence are inside the declared target (`references/router-contract.md`); the oracle and the differential script were opened read-only at the system root purely to test that claim, and no finding is raised against them.
Affected surface hints: references/router-contract.md (fix target: regenerate the fence from the oracle or narrow both claims), SKILL.md:77 (repeat of the claim)
Case: A maintainer changes the oracle's Quick fallback, runs the packet's stated drift proof, and gets no signal because the fence is a different program; the prose and the executable oracle silently diverge for the next reader.
```

```json
{
  "type": "claim-adjudication",
  "claim": "references/router-contract.md is materially different from benchmark/router/route_contract.py while asserting it is the exact source that proves the two never drift.",
  "evidenceRefs": [
    "AI Systems/Product Owner/sk-product-owner/references/router-contract.md:17",
    "AI Systems/Product Owner/sk-product-owner/references/router-contract.md:33",
    "AI Systems/Product Owner/sk-product-owner/references/router-contract.md:41-832",
    "AI Systems/Product Owner/sk-product-owner/SKILL.md:77",
    "AI Systems/Product Owner/benchmark/router/route_contract.py:492-503"
  ],
  "counterevidenceSought": "Checked whether the fence is a documented subset (the 'Smart Router Pseudocode' section only), whether differential.py compares only tables rather than whole programs, and whether comment stripping would make the two equal. Stripped comments and blank lines: token streams diverge at token 0 and function-name sets are disjoint, so no normalization reconciles them. differential.py exposes extract_pseudocode, check_copy_parity and table-parity checks, which is narrower than 'the exact source proves the oracle never drifts'.",
  "alternativeExplanation": "The oracle may be the newer implementation and the packet document a stale copy awaiting regeneration, in which case the defect is staleness rather than a wrong invariant. Accepted as the likely history but not as a mitigation: whichever file is newer, the packet states an invariant that is false today, and the fix is to regenerate the fence or narrow the claim.",
  "finalSeverity": "P1",
  "confidence": "high",
  "downgradeTrigger": "Downgrade to P2 if the fence is regenerated from the oracle or both claims are rewritten to describe only the table-parity check that differential.py actually performs."
}
```

### P2 Findings

1. **The contract's ALWAYS lane loads two of the six resources the bootstrap marks ALWAYS, and skips its own first entry by name** -- `AI Systems/Product Owner/sk-product-owner/references/router-contract.md:137` -- `RESOURCE_MAP["ALWAYS"]` lists `sk-product-owner/SKILL.md`, `references/hvr-core.md` and `references/conciseness.md` (:137-140), and the loading loop at :716-718 iterates that list while skipping `sk-product-owner/SKILL.md` explicitly (`if reference != "sk-product-owner/SKILL.md"`). `SKILL.md:71` marks six ALWAYS resources for the first reply: the hub `../SKILL.md`, `../ROUTER.md`, this packet's `SKILL.md`, `references/hvr-core.md`, `references/conciseness.md` and `Section 3 of assets/interactive-response-templates.md`. The entry that the loop skips can never load anyway: `load_if_available` requires the path to be a key in `discover_markdown_resources` (:283-296), whose inventory is built only from `references/` and `assets/`, so a system-root-relative path has no key. Net effect: the contract's ALWAYS lane is two cards, while the prose requires the hub's stage-one rules, the leaf map and the delivery reply shape as well.

```
Finding class: contract-drift
Scope proof: Both sides are inside the declared target; the ALWAYS row and the fence are compared directly.
Affected surface hints: references/router-contract.md (fix target), SKILL.md:71 (governing prose)
Case: A reader runs the contract's resource plan before a first reply and gets hvr-core and conciseness only, so the delivery reply shape is never loaded and the reply format drifts.
```

2. **Quick energy falls back to Task in the contract but not in the routing rules** -- `AI Systems/Product Owner/sk-product-owner/references/router-contract.md:851` -- The primary-detection copy says "confidence < LOW (0.40) -> Interactive Mode ..., except under Quick energy, which keeps the narrow Task fallback" (:851, and the same exception at :847), and the oracle's docstring states it as rule (`route_contract.py:21`). `references/routing.md:30-34` states the four bands with no Quick exception, its step 7 routes by threshold alone, and its closing note says only that "Quick narrows the selected artifact". `SKILL.md:58` says `$quick` is "energy override only, never an intent". The three prose authorities therefore deny a behavior the contract implements for a bare `$quick` with no artifact named.

```
Finding class: doc-gap
Scope proof: All three citations are inside the declared target.
Affected surface hints: references/routing.md (fix target: state the exception beside the bands), references/router-contract.md:847-851 (already states it)
Case: A user types `$quick` with no artifact word; the contract invents a Task, while the routing rules say an unrecognized request must ask one consolidated question before drafting.
```

3. **Oracle paths are written root-relative inside packet-relative prose** -- `AI Systems/Product Owner/sk-product-owner/SKILL.md:44` -- Eight citations name `benchmark/router/…` from a packet whose own files sit one level down: `SKILL.md:44` ("the oracle and fixtures in `benchmark/router/`"), `SKILL.md:77` (`benchmark/router/route_contract.py`, `benchmark/router/differential.py`), `SKILL.md:242` (`benchmark/router/fixtures.json`), `references/routing.md:77`, and `references/router-contract.md:17`, `:24`, `:33`. In the same sentences the docs cite packet-relative paths (`references/routing.md`, `references/router-contract.md`), so a single base cannot resolve both: `sk-product-owner/benchmark/router/` does not exist, while `AI Systems/Product Owner/benchmark/router/` does. Every other citation in the packet is packet-relative (779 relative links were checked and none of them escape the packet).

```
Finding class: path-base-ambiguity
Scope proof: Citation sites inside the target; existence checked at both candidate bases. Doubt stated: the intended base is clearly the system root, so this is a resolution hazard rather than a dangling target.
Affected surface hints: SKILL.md:44, SKILL.md:77, SKILL.md:242, references/routing.md:77 (fix targets: use `../../benchmark/router/…` or state the base once)
Case: A maintainer opens `sk-product-owner/benchmark/router/route_contract.py` from the citation and finds nothing, then concludes the oracle is missing.
```

4. **The README worked example links five bundle siblings the examples tree does not ship** -- `AI Systems/Product Owner/sk-product-owner/assets/examples/doc/doc-example-readme.md:60` -- Its "Reading map" tells the reader to "Open these in order" and links `diagnosis-double-payout.md` (:60), `runbook-payout-reconciliation.md` (:61), `decision-idempotency-keys.md` (:62), `evidence/webhook-payloads/` (:63) and `evidence/payout-ledger-exports/` (:64). None exists under `assets/examples/doc/`; the folder holds seven self-contained example documents and no `evidence/` tree. All other example links resolve, and the three remaining unresolved link matches in the packet are documented placeholder syntax (`export/[###]…` in `references/story-mode.md:406-407` and `assets/task-templates.md:77`), not broken paths. Doubt stated: a delivered README would legitimately link a bundle that is not part of this packet, so this may be deliberate illustration rather than a defect.

```
Finding class: example-link
Scope proof: Link targets resolved relative to the example file; only this example group failed.
Affected surface hints: assets/examples/doc/doc-example-readme.md (fix target)
Case: A tester validates "examples obey the templates" by following the example's own reading map and hits five missing targets, which reads as a package defect rather than an illustrative bundle.
```

## Traceability Checks

| Protocol | Level | Status | Evidence |
|----------|-------|--------|----------|
| `spec_code` | core | partial | `specs/product-owner/018-product-owner-deep-review/001-sk-product-owner/spec.md:13` scope honoured; every finding sits inside `AI Systems/Product Owner/sk-product-owner`. No acceptance criteria exist in the staging spec to trace against. |
| `checklist_evidence` | core | fail | `SKILL.md:44` states the drift invariant that the contract must satisfy, and the contract fails it (P1-1); `SKILL.md:71` names the ALWAYS lane the contract drops (P2-1). |
| `skill_agent` | overlay | partial | The packet is self-contained as an executable identity (`SKILL.md:232`); no agent definition names this skill, so agent-side loading could not be compared. |
| `agent_cross_runtime` | overlay | notApplicable | No runtime mirror inside the target; `SKILL.md:310` and `README.md:415` place the Project packaging outside it. |
| `feature_catalog_code` | overlay | notApplicable | No feature catalog in this packet. |
| `playbook_capability` | overlay | partial | 779 relative links resolved across the packet, including all 50 playbook files and all worked examples except the one group in P2-4; per-scenario capability coverage remains scheduled for iteration 5. |

## Integration Evidence

- Drift gate: `AI Systems/Product Owner/benchmark/router/differential.py` exposes `extract_pseudocode`, `check_copy_parity`, `check_prose_table_parity`, `check_table_parity` and `build_skill_router`; the packet names it at `SKILL.md:77` and `references/router-contract.md:24` as the enforcement point. Named exactly because the finding depends on what that gate actually compares.
- Fixtures: `AI Systems/Product Owner/benchmark/router/fixtures.json` exists, so `SKILL.md:242`'s target resolves at the system root (see P2-3 for the base issue only).
- Hub: `AI Systems/Product Owner/SKILL.md` and `AI Systems/Product Owner/ROUTER.md` both exist, so `SKILL.md:71`'s hub entries are real files the contract's ALWAYS lane omits.

## Edge Cases

- **Duplicated preamble paragraph.** `references/router-contract.md:17` and `:33` carry the same sentence twice, and the `Purpose`/`Scope`/`Loads With` block at `:20-26` precedes a second `## 1. OVERVIEW`. It is the same file as P1-1; recorded for the maintainability iteration rather than counted twice here.
- **`SKILL_ROOT` base inside the fence.** The fence sets `SKILL_ROOT` to its own directory (`:47`) while the oracle sets it three levels up into the packet (`route_contract.py:492`). That difference is part of P1-1's evidence and is not recorded separately, because a fence is a copy that may legitimately be re-based when executed.
- **Second fence at `:852`.** The primary-detection block is a `text` fence after the Python fence closes at `:832`; the drift comparison covered the Python fence only, which is the one the docs call the code.

## Confirmed-Clean Surfaces

- 779 relative links across every `.md` in the packet resolve except the eight reported: zero dangling targets in `references/`, `assets/*.md`, `manual-testing-playbook/` (hub and 50 scenario files) and the five other example groups.
- Semantic topic names and trigger vocabulary agree between `references/routing.md:49-59` and `references/router-contract.md:100-135` (nine topics, same ordering, `ui_refinement` at 0.80 and `documentation`/`story` at 0.85).
- Confidence constants agree between `references/router-contract.md:50` and `references/routing.md:31-34`.
- Story/Epic shape precedence and the one-scaffold rule agree across `SKILL.md:55-56`, `references/routing.md:63-67` and the fence's shape tables.
- The Flow handoff is consistent in all three authorities: no packet file loads, and the `RESOURCE_MAP["FLOW"]` entries are explicitly documented as unreachable by the guard at `references/router-contract.md:148-151`.

## Ruled Out

- **Broken `export/[###]` links.** `references/story-mode.md:406-407` and `assets/task-templates.md:77` are placeholder naming syntax for the export path pattern, not citations. Ruled out.
- **`../claude project/README.md` as a broken link.** The README writes it percent-encoded (`../claude%20project/README.md`); decoded, it resolves. Ruled out.
- **Hub links escaping the packet.** `SKILL.md:71` and `:317` cite `../SKILL.md` and `../ROUTER.md`; both exist at `AI Systems/Product Owner/`, and the packet is explicitly one level inside that system, so the parent-relative form is correct here — unlike the `benchmark/router/` group in P2-3, which uses no `../` at all. Ruled out.

## Next Focus

- Dimension: maintainability
- Focus area: template-versus-rule agreement and example-versus-template obedience across `assets/` — the six scaffolds, the `assets/examples/` set, and the duplicated preamble in `references/router-contract.md`
- Reason: iteration 2 closed paths and contract traceability; the templates have not yet been compared to the rules that govern them, which is the largest unexamined surface in the packet
- Rotation status: correctness and traceability covered; security and maintainability remain (maintainability next, security at iteration 4, playbook coverage at iteration 5)
- Required evidence: `[SOURCE: path:line]` for both sides of every agreement check
- Recovery note: none

Review verdict: CONDITIONAL
