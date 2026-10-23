# Iteration 005 — Deep Review

## Dispatcher

- Mode: review; target_agent: deep-review; execution: inline lineage executor (no nested dispatch)
- Iteration: 5 of 5; Dimension: maintainability
- Lineage: sessionId=fanout-deepseek-1792580454700-vajsq8, generation=1, lineageMode=new
- Sources read this iteration: `specs/product-owner/018-product-owner-deep-review/003-mcp-click-up/spec.md`, `specs/product-owner/018-product-owner-deep-review/003-mcp-click-up/review/lineages/deepseek/steer.md`, `deep-review-strategy.md`, all four earlier iteration files in this lineage, `AI Systems/Product Owner/mcp-click-up/SKILL.md:100-215`, `feature-catalog/FEATURE-CATALOG.md:1-40,320-345`, `changelog/v1.2.2.0.md:1-30`, `AI Systems/Product Owner/AGENTS.md:110-125`, `AI Systems/Product Owner/sk-product-owner/SKILL.md:279-312`, `sk-product-owner/references/doc-mode.md:414-418`, `AI Systems/Product Owner/benchmark/gates/README.md:15-40`, `benchmark/gates/run_gates.sh:1-50`, `AI Systems/Product Owner/manual-testing-playbook/manual-testing-playbook.md:1-20`

## Dimension

Maintainability — what keeps this packet and its hub contract from drifting a second time: where each fact lives, how many owners it has, and what a maintainer pays to change one behaviour.

## Files Reviewed

- `AI Systems/Product Owner/mcp-click-up/SKILL.md:100-215` (router, resource bases, intent map)
- `AI Systems/Product Owner/mcp-click-up/feature-catalog/FEATURE-CATALOG.md:1-40, 320-345`
- `AI Systems/Product Owner/mcp-click-up/changelog/v1.2.2.0.md:1-30`
- `AI Systems/Product Owner/mcp-click-up/references/cupt-commands.md` and `references/mcp-tools.md` (ownership comparison)
- `AI Systems/Product Owner/AGENTS.md:110-125`
- `AI Systems/Product Owner/sk-product-owner/SKILL.md:279-312`
- `AI Systems/Product Owner/sk-product-owner/references/doc-mode.md:414-418`
- `AI Systems/Product Owner/benchmark/gates/README.md:15-40`, `benchmark/gates/run_gates.sh:1-50`
- `AI Systems/Product Owner/manual-testing-playbook/manual-testing-playbook.md:1-20`

## Findings by Severity

### P0 Findings

None.

### P1 Findings

None new. Two P1 findings from iteration 3 (`R3-P1-001`, `R3-P1-002`) and one from iteration 4 (`R4-P1-001`) remain active and are the reason this iteration's verdict is not PASS.

### P2 Findings

1. **The command surface and its counts are hand-restated in three layers, and the latest strict validator pass did not catch the disagreement** -- AI Systems/Product Owner/mcp-click-up/feature-catalog/FEATURE-CATALOG.md:17 -- the catalog summary asserts "50 features across 10 command areas" and "`--json` output on `add` and 4 of its read commands"; the per-command claims live again in 111 cards (`cupt-global-flags/json-flag.md:19` names five commands); and the authority for the surface, `references/cupt-commands.md`, states neither count. `changelog/v1.2.2.0.md:13` records that a strict catalog validator ran and repaired the catalog, yet the `add` claim survived it and now contradicts four other documents (see `R4-P1-001`).
Finding class: duplicated-fact
Scope proof: the three layers are all in the packet, and the reference that owns the surface documents no `add` command; the validator's own changelog entry is the evidence that this layer is machine-checked.
Affected surface hints: `feature-catalog/FEATURE-CATALOG.md` (fix site, upstream), `feature-catalog/cupt-global-flags/json-flag.md`, `references/cupt-commands.md`
Case: cupt ships a new `--json`-capable command; a maintainer edits the reference, then must remember two catalog lines and one flag card that restate the same list, and the validator passes because each file is internally well-formed.
Fix site: `mcp-click-up/feature-catalog/FEATURE-CATALOG.md` upstream — drop the enumerated `--json` command list from the summary (link the reference instead) and derive the two counts, or fail the catalog validator when a summary claim is not present in the reference.

2. **The ClickUp handoff contract has three independent authors and no stated owner** -- AI Systems/Product Owner/AGENTS.md:117 -- the trigger set appears in `AGENTS.md:117`, the offer and push-target rules in `sk-product-owner/SKILL.md:283-306`, and a third restatement in `sk-product-owner/references/doc-mode.md:416`. Each states its own version of when the offer fires and who owns the transport mechanics; no document declares which governs. That structure produced three findings in this review (`R3-P1-001` trigger divergence, `R3-P1-002` parameter drift, `R3-P2-001` stale owner name) from one behaviour.
Finding class: unowned-duplication
Scope proof: the three statements are quoted in iteration 3; each was read at its current line, and none names itself subordinate to another for the trigger set.
Affected surface hints: `AGENTS.md` (fix site, hub), `sk-product-owner/SKILL.md`, `sk-product-owner/references/doc-mode.md`
Case: a maintainer changes when the offer fires; they edit Section 7, the authoritative-looking statement, and `AGENTS.md:117` keeps offering on a runtime Section 7 excludes — the exact mismatch iteration 3 recorded.
Fix site: `AI Systems/Product Owner/AGENTS.md:117` — make Section 7 the named owner of the trigger set and the offer, and reduce the `AGENTS.md` paragraph to a pointer plus the one sentence about where push targets live.

3. **The packet's router declares an `assets` discovery base that does not exist** -- AI Systems/Product Owner/mcp-click-up/SKILL.md:105 -- `RESOURCE_BASES = (SKILL_ROOT / "references", SKILL_ROOT / "assets")`, and the packet has no `assets/` folder. Discovery therefore runs over one live base and one dead one, and the packet-root install guide needs a separate `ROOT_RESOURCES` special case two lines later (`:107`) to be discoverable at all. This is the same shape of debt as the hub's leaf contract in `R3-P2-002`: the resource vocabulary does not describe the packet's real files.
Finding class: dead-vocabulary
Scope proof: a directory listing of the packet root shows no `assets/`, and both the base tuple and the special case are in the same code block.
Affected surface hints: `mcp-click-up/SKILL.md` (fix site, upstream), `ROUTER.md:19` and `leaf-manifest.json` (the same vocabulary in the hub)
Case: a maintainer adds an asset to the packet expecting it to be routable under `assets/`, and it is never loaded because the base does not exist; or they add a second packet-root file and must remember the special case.
Fix site: `mcp-click-up/SKILL.md` upstream — drop the `assets` base and state the root-file rule once, or add the folder the base already names.

## Traceability Checks

- `Core: spec_code` — the staging spec's three named entries and the steer's focus list were re-read against the four earlier iterations' findings; every finding names a fix site in the file its steer rule requires. Status: pass.
- `Core: checklist_evidence` — no checklist exists in the staging wrapper; the four prior iterations' evidence lines were re-opened where this iteration depends on them (`AGENTS.md:117`, `sk-product-owner/SKILL.md:283`, `SKILL.md:105`, `FEATURE-CATALOG.md:17`). Status: pass.
- `Overlay: playbook_capability` — the hub-level playbook states that "each vendored packet owns its own" playbook (`Product Owner/manual-testing-playbook/manual-testing-playbook.md:11`), so the two playbooks are a documented split rather than duplication. Status: pass.
- `Overlay: feature_catalog_code` — the catalog reconciliation stands at 50 cupt cards and 61 MCP tool cards; the unresolved part is the claim layer, not the counts. Status: partial, carried from iteration 4.

## Integration Evidence

- `benchmark/gates/run_gates.sh:46-47` is the single automated check that the vendored copy stays byte-identical, and `benchmark/gates/README.md:81` documents it as a command an operator runs; there are no Git hooks in this repository (`.git/hooks` holds samples only), so the invariant is release-gated rather than commit-gated.
- `scripts/build-plugin.py:104-117` re-checks the same hashes before shipping, which gives the manifest a second consumer but not a second schedule.
- `Product Owner/manual-testing-playbook/manual-testing-playbook.md:11` names the ownership split for playbooks, which is the pattern the handoff contract lacks.

## Edge Cases

- Restating a fact is sometimes the correct choice: `AGENTS.md` is the bootstrap an agent reads before any skill, so it must carry enough of the handoff to be actionable. The finding asks for a named owner and a pointer, not for the paragraph's removal.
- The catalog counts are useful to a reader; the finding targets the enumerated command list, which is the part that rots, not the totals.

## Confirmed-Clean Surfaces

- The packet is byte-identical to its upstream and the manifest is complete (iteration 1), so maintainability concerns here are about the shared upstream copy, not about a local fork.
- The vendoring mechanism has a gate, a test suite and a second consumer (plugin build); the process gap is scheduling, not absence.
- The hub's four documents share one version value, so the hub itself is single-sourced on release numbering.
- Playbook ownership is explicitly assigned at the hub level, and the packet's 43 playbook files stay inside it.

## Ruled Out

- "The two manual-testing-playbooks duplicate each other": the hub playbook states the split, and the hub file set is 8 files against the packet's 43.
- "The packet is an unmaintained fork": it is a byte copy with a manifest, a gate and a test suite.
- "The hub has no version discipline": all four hub documents read 1.0.0.0, as its own version-authority paragraph requires.

## Next Dimension

- None. This is the fifth and final iteration of the cap; synthesis compiles the registry, the report and the planning packet from these five iteration files and deltas.

## Source Tags

- R5-P2-001 — [SOURCE: mcp-click-up/feature-catalog/FEATURE-CATALOG.md:17]
- R5-P2-002 — [SOURCE: AGENTS.md:117]
- R5-P2-003 — [SOURCE: mcp-click-up/SKILL.md:105]

## Verdict

Three P2 findings this iteration and no new P0 or P1. Across the lineage, four P1 findings remain active (`R2-P1-001`, `R3-P1-001`, `R3-P1-002`, `R4-P1-001`) and twelve P2, so the release verdict is CONDITIONAL: the vendored copy is faithful and its gates exist, but the hub's handoff promises two things it cannot always keep and the packet contradicts itself on `cupt add`.

Review verdict: CONDITIONAL
