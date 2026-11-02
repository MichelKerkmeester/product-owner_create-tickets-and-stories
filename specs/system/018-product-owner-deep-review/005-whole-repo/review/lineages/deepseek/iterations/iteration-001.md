# Review Iteration 001 - Correctness (hub routing against the packets)

## Dispatcher

- Session: `fanout-deepseek-1792580494888-r714jg`, lineage `deepseek`, iteration 1 of 5
- Executor: cli-pi (deepseek-v4.1-flash), detached fan-out lineage; iteration executed in-process, no nested dispatch
- Target: `specs/product-owner/018-product-owner-deep-review/005-whole-repo` (review setup binds the Product Owner tree named in `spec.md` Files to Change)
- Sources consulted before this iteration: `steer.md` (lead rulings), `spec.md`, `deep-review-config.json`, `deep-review-strategy.md`
- Focus selected from strategy Next Focus: correctness of hub routing (`mode-registry.json`, `hub-router.json`, `ROUTER.md`) against the four packets (`sk-product-owner`, `sk-create-figjam`, `mcp-click-up`, `mcp-figma`)

## Dimension

Correctness: do the hub layers agree with each other and with the code that executes them? A reader
who follows `ROUTER.md` must reach the same routing the gate and the oracle compute.

## Files Reviewed

- `AI Systems/Product Owner/mode-registry.json` (read whole, 179 lines)
- `AI Systems/Product Owner/hub-router.json` (read whole, 141 lines)
- `AI Systems/Product Owner/ROUTER.md` (read whole, 121 lines)
- `AI Systems/Product Owner/leaf-manifest.json` (leaf inventory, all four modes)
- `AI Systems/Product Owner/benchmark/gates/check_hub.py:234-263` (stage-one router implementation)
- `AI Systems/Product Owner/benchmark/router/route_contract.py:86-100,492-522` (artifact commands, resource lanes, skill root)
- `AI Systems/Product Owner/benchmark/router/differential.py:79-83` (which document the replay parses)
- `AI Systems/Product Owner/sk-product-owner/SKILL.md:244` (commands that must not route)
- `AI Systems/Product Owner/AGENTS.md:44,54,172-173,284` (Human Voice preload claim in `ROUTER.md`)
- `AI Systems/Product Owner/steer.md` (lead rulings for this lineage)

## Findings by Severity

### P0 Findings

None. No correctness failure, security defect, or spec contradiction was confirmed in hub routing.

### P1 Findings

None. Every consistency claim checked in this iteration held once the cited line was opened.

### P2 Findings

1. **ROUTER.md says a replay parses its python block, and no gate replays it** -- AI Systems/Product Owner/ROUTER.md:43 -- The section header states the block is "the single machine-readable projection ... the byte-for-byte source a deterministic replay parses". The only replay in the tree, `benchmark/router/differential.py`, executes `sk-product-owner/references/router-contract.md` and reads `references/routing.md` [SOURCE: benchmark/router/differential.py:79-83], and no file under `benchmark/` opens the hub `ROUTER.md` python fence [SOURCE: benchmark/gates/check_hub.py:143]. A reader who edits that block expecting routing to change, or who trusts it to be enforced, is wrong in both directions.
   Finding class: documentation-behaviour drift
   Scope proof: claim and counter-evidence are both inside the declared target (`ROUTER.md` and `benchmark/router/`)
   Affected surface hints: `AI Systems/Product Owner/ROUTER.md` section 3 preamble; if enforcement is wanted, the gate that would parse it does not exist yet
   Case: a maintainer changes a keyword in `ROUTER.md` section 3, runs the benchmark gates, and gets green because nothing reads that fence.

2. **The named contract boundary resolves only under a parent directory ROUTER.md does not name** -- AI Systems/Product Owner/ROUTER.md:19 -- The text points at "the sk-create-skill `leaf-resource-contract.cjs`". `sk-create-skill` is not a top-level skill: the file lives at `.skilled/skills/sk-doc/sk-create-skill/scripts/lib/leaf-resource-contract.cjs`, and `.skilled/skills/sk-create-skill` does not exist. Doubt stated: the skill name itself is real, so this is path precision rather than a wrong contract, which is why it stays P2.
   Finding class: path-reference drift
   Scope proof: cited path verified absent; the real path verified present
   Affected surface hints: `AI Systems/Product Owner/ROUTER.md` section 1; any reader or checker resolving the boundary by the named location
   Case: a reader greps `.skilled/skills/sk-create-skill/` for the contract and concludes the boundary was removed.

## Traceability Checks

| Protocol | Status | Evidence |
|----------|--------|----------|
| `spec_code` | pass | Every path in `spec.md` Files to Change exists: hub files, `claude project/`, `scripts/`, `benchmark/`, `manual-testing-playbook/`, and the four packet folders |
| `checklist_evidence` | notApplicable | The staging packet carries no `checklist.md`; there is no evidence set to align |
| `skill_agent` | pass (partial) | `check_hub.py` returned zero problems: each registry `packetSkillName` equals its packet `SKILL.md` frontmatter name, and each packet exposes a Section 2 SMART ROUTING block |
| `agent_cross_runtime` | notApplicable this iteration | No runtime mirror was opened; `.skilled` is a symlink to an external checkout |
| `playbook_capability` | deferred | `manual-testing-playbook/` is scheduled for the maintainability iteration |
| `feature_catalog_code` | notApplicable | The target carries no feature catalog |

## Integration Evidence

- `benchmark/gates/check_hub.py` stage-one router (`route_stage_one`, lines 234-263) replayed 37 gold rows from `benchmark/hub-routing-cases.json` with **0 mismatches**, and `check_hub()` reported no problems.
- `ROUTER.md` RESOURCE_MAP: all 19 packet-qualified paths resolve on disk, and all 19 appear in the matching `leaf-manifest.json` mode `leaves` list, so the section 3 claim "Every `RESOURCE_MAP` path resolves on disk and is registered in `leaf-manifest.json`" holds today.
- `ROUTER.md:37` says `DEFAULT_RESOURCE` is `hvr-core.md` and `conciseness.md` loaded on every request; `AGENTS.md:172-173` lists exactly those two under its always-load tier, so the claim holds.
- `sk-product-owner/SKILL.md:244` states `$document`, `$docs`, `$prds`, `$stories` and `$email` do not route, and `route_contract.py:86-100` omits all five from `ARTIFACT_COMMANDS`, so the oracle matches the prose on the false-prefix rule.

## Edge Cases

- **Two implementations of stage one.** `check_hub.py:234-263` executes `hub-router.json`, while `route_contract.py` executes stage two alone. Neither is the hub's runtime router, so "consistent" here means the two agree with each other and with the registry, not that a live model routes this way.
- **`packetCommands` names only `sk-create-figjam`.** `$task`, `$bug`, `$doc`, `$story`, `$epic` fall under `stageOneOrder` rule 1's "any other $ command starts in the default mode", which is that packet. The outcome is right; the rule reads as if those commands were unowned. Recorded, not raised, because behaviour matches.
- **`route_contract.py` FLOW lane is guarded to empty.** `RESOURCE_MAP["FLOW"]` names files under `sk-create-figjam`, and `_guard_in_skill` drops them against `sk-product-owner`, so a FLOW route carries an empty lane by design (comment at `route_contract.py:508-510`). Recorded as intended, not a defect.
- **`benchmark/hub-routing-cases.json` is the only stage-one oracle.** Its 37 rows pass, but they are gold rows chosen by hand, so a green run bounds confidence rather than proving stage one correct.

## Confirmed-Clean Surfaces

- `mode-registry.json` `repo-root-hub.repoPaths` is complete in the sense the doctor check enforces: it names no packet, no `HUB_ROOT_FILES` entry, and no nested path, and `parent-skill-check.cjs` allowlists `scripts`, `changelog` and `manual-testing-playbook` as top-level directories.
- `hub-router.json` routerSignals, vocabularyClasses and the registry `aliases` agree for all four modes; every vocabulary keyword is a non-empty phrase.
- `ROUTER.md` frontmatter carries both markers `check_hub.py:144` requires (`router_state`, `skill_pointer`).

## Ruled Out

- **`ROUTER.md` route table vs the registry as a drift source** -- ruled out: the table is stage two, the registry is stage one, and `check_hub.py` asserts the registry's inventory against the hub prose through `inventory_problems`.
- **`$email` as a documented-but-unimplemented command** -- ruled out: `sk-product-owner/SKILL.md:244` names it as a token that must not route, and the oracle agrees.
- **Missing `graph-metadata.json` identity under the hub** -- ruled out: the file exists at the hub root and check 1a passes.

## Verdict

No active P0 or P1 findings. Two P2 advisories are recorded, both documentation drift inside `ROUTER.md`, and neither changes routing behaviour today.

## Next Focus

- Dimension: traceability
- Focus area: `claude project/Custom Instructions.md` and `claude project/knowledge/` against their skill sources, plus `SYNC.md` parity claims and `benchmark/gates/rule_parity.py`
- Reason: routing is one half of the declared focus; the Project kernel and knowledge mirror are the other half and were untouched in this iteration
- Rotation status: D1 correctness done; D3 traceability next
- Blocked/productive carry-forward: productive — direct read plus the gate's own functions proved consistency without running repo tooling
- Required evidence: paired file:line citations on both sides of each parity claim
- Recovery note: none

Review verdict: PASS
