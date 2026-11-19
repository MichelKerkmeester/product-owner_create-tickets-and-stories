# Iteration 004 - Traceability: Skilled `sk-doc` alignment

**Mode:** review
**Dimension:** traceability
**Operator focus addressed:** "Check alignment with Skilled sk-doc (sk-create-skill package shape, README, changelog, frontmatter, playbook and catalog modes)". This iteration reads the `sk-doc` rule lines and diffs them against the on-disk Product Owner trees, so every claim below names the rule it breaks rather than asserting a house style.
**Budget profile:** `scan` (9 tool calls used of 12 soft / 13 hard)

## Dispatcher

`/deep:review` iteration 4 of 10, fanned out in parallel with iterations 3-9. Focus supplied by the packet prompt: sk-doc alignment for `sk-product-owner`, `sk-create-figjam` and the hub. Iteration number derived from the JSONL: two `type:"iteration"` records on disk, so this narrative is `iteration-004.md`.

## Files Reviewed

- `.skilled/skills/sk-doc/SKILL.md:1-80` (hub identity, mode table, version-authority sentence)
- `.skilled/skills/sk-doc/sk-create-skill/SKILL.md:96-155` (required standalone shape, frontmatter contract) and `:160-240` (parent-hub and packet shape)
- `.skilled/skills/sk-doc/sk-create-changelog/SKILL.md:1-46` and `:62-95`, `:138-148`, `:320-360` (global placement, packet-local deprecation, topology resolution, anti-patterns)
- `AI Systems/Product Owner/SKILL.md:1-14`
- `AI Systems/Product Owner/sk-product-owner/SKILL.md:1-14`
- `AI Systems/Product Owner/sk-create-figjam/SKILL.md:1-14`
- `AI Systems/Product Owner/.gitignore:1-60`
- `AI Systems/Product Owner/manual-testing-playbook/manual-testing-playbook.md:1-30`
- `AI Systems/Product Owner/benchmark/` (top-level listing) and `benchmark/reports/` (run-folder grammar)
- Directory trees: `sk-product-owner/{references,assets,changelog,manual-testing-playbook}`, `sk-create-figjam/{references,assets,scripts,changelog,manual-testing-playbook}`, `.skilled/changelog/` (component list)

## Findings - New

### P0 Findings

None this iteration.

### P1 Findings

None new this iteration. The two active P1 findings from iteration 2 (hub `NEVER` rule forbidding packet-local `ROUTER.md`; diverged `validate-output-format.cjs` fork) were not re-opened and remain active.

### P2 Findings

1. **The system keeps 92 packet-local changelog entries in the placement `sk-create-changelog` has deprecated, and no global component changelog exists for the `product-owner` identity** -- `.skilled/skills/sk-doc/sk-create-changelog/SKILL.md:10` -- The changelog packet states that it writes to `.skilled/changelog/{component}/v{VERSION}.md` and that "Packet-local (nested) changelogs under a spec packet's `changelog/` folder are deprecated, and this workflow no longer writes them". It refuses `--nested` at `:65` and `:144`. The Product Owner system stores its entire release history in exactly the deprecated location: `AI Systems/Product Owner/changelog/` (29 entries), `sk-product-owner/changelog/` (44 entries) and `sk-create-figjam/changelog/` (19 entries). `.skilled/changelog/` holds 15 component folders (`cli-classifier` through `system-spec-kit`) and none of them is `product-owner`, `sk-product-owner` or `sk-create-figjam`. The rule conflict is inside `sk-doc` itself: the shape packet still mandates the deprecated folder at `.skilled/skills/sk-doc/sk-create-skill/SKILL.md:165` ("Create each nested packet with `SKILL.md`, `README.md`, its own `ROUTER.md`, and `changelog/`"). Existing entries stay valid per `:94`, so this is placement drift awaiting the next version bump, not a broken file.
   Finding class: documentation-placement drift between a hub's declared version authority and the authoring rule that owns changelog placement.
   Scope proof: every rule line read is under `.skilled/skills/sk-doc/**` and every count is under `AI Systems/Product Owner/**`, both inside the declared review target; no file outside the target was read for this finding.
   Affected surface hints: the hub `SKILL.md` version-authority sentence at `AI Systems/Product Owner/SKILL.md:11`, `/create:changelog` routing through `mode-registry.json`, `SYNC.md` release notes, the packet version-bump workflow, and any gate that resolves a changelog path.
   Case: A maintainer bumps the hub to `1.0.29.0` and runs `/create:changelog`. The mode refuses the packet-local path and writes `.skilled/changelog/product-owner/v1.0.29.0.md`. The hub's history now lives in two placements, and a reader who follows the 92 existing entries never sees the new release.

   ```json
   {
     "type": "claim",
     "claim": "The Product Owner system's release history sits entirely in the changelog placement sk-doc's changelog packet now deprecates, and no global component changelog exists to accept the next entry.",
     "evidenceRefs": [
       ".skilled/skills/sk-doc/sk-create-changelog/SKILL.md:10",
       ".skilled/skills/sk-doc/sk-create-changelog/SKILL.md:65",
       ".skilled/skills/sk-doc/sk-create-changelog/SKILL.md:94",
       ".skilled/skills/sk-doc/sk-create-skill/SKILL.md:165",
       "AI Systems/Product Owner/changelog/",
       "AI Systems/Product Owner/sk-product-owner/changelog/",
       "AI Systems/Product Owner/sk-create-figjam/changelog/",
       ".skilled/changelog/"
     ],
     "counterevidenceSought": "Looked for a `product-owner` component under `.skilled/changelog/` (absent across all 15 components) and for a carve-out in the changelog packet that grandfathers a hub-level `changelog/` (found only the grandfathering of existing files at :94, which preserves them but does not make the placement current).",
     "alternativeExplanation": "The hub predates the global-changelog convention and is deliberately frozen in the old placement, with migration scheduled elsewhere. No migration note, no component folder and no sync-loop reference supports that reading, so the drift is real until such a note exists.",
     "finalSeverity": "P2",
     "confidence": "median",
     "downgradeTrigger": "A stated migration decision for this hub's changelog placement, or a `product-owner` component folder appearing under `.skilled/changelog/`, downgrades this to informational."
   }
   ```

2. **`.gitignore` has no rule for Python cache directories although two `.pytest_cache` trees already sit inside the shippable skill folder** -- `AI Systems/Product Owner/.gitignore:2` -- The ignore file covers `.DS_Store`, `export/*`, `.env*`, `claude project/local/`, `mcp-code-mode/mcp-server/{node_modules,dist}`, `context/*` and `specs/personal/*`, and nothing else. `AI Systems/Product Owner/.pytest_cache/` and `AI Systems/Product Owner/sk-create-figjam/.pytest_cache/` both exist in the working tree today, and `sk-create-figjam/scripts/figjam_checks/` is a Python package that produces `__pycache__` on every check run. The `sk-create-skill` required package shape (`.skilled/skills/sk-doc/sk-create-skill/SKILL.md:98-121`) lists no cache directory, and the packet's own completion rule at `:95` ships the folder with `scripts/package_skill.py`, so whatever is present gets packaged.
   Finding class: packaging hygiene gap in the ignore contract.
   Scope proof: `.gitignore` is a declared review-scope file and both `.pytest_cache` trees live under the declared target directory; `git ls-files` shows them untracked today, so this is a latent packaging defect rather than committed noise.
   Affected surface hints: `scripts/package_skill.py` invocation used to ship the packets, the repo-root `package`/release path, and `sk-create-figjam/scripts/figjam_checks/` test runs.
   Case: A maintainer runs the FigJam check suite locally, then packages `sk-create-figjam`. The archive ships `.pytest_cache/v/cache/nodeids` and `__pycache__/*.pyc` because nothing in the ignore contract or the packager excludes them.

   ```json
   {
     "type": "claim",
     "claim": "The Product Owner ignore contract omits Python cache directories that already exist in the tree and that the packager would ship.",
     "evidenceRefs": [
       "AI Systems/Product Owner/.gitignore:2",
       "AI Systems/Product Owner/.pytest_cache/",
       "AI Systems/Product Owner/sk-create-figjam/.pytest_cache/",
       ".skilled/skills/sk-doc/sk-create-skill/SKILL.md:95",
       ".skilled/skills/sk-doc/sk-create-skill/SKILL.md:98"
     ],
     "counterevidenceSought": "Checked `git ls-files` for tracked cache paths (none) and re-read the whole ignore file for an existing `pytest`/`pycache` rule (none); also checked whether the repo root carries a global cache ignore (the Product Owner tree is its own Git repository, so a parent rule does not apply).",
     "alternativeExplanation": "The maintainers may rely on the packager to filter caches at package time. The shape contract names no such filter and the packager is invoked on the folder as it stands, so nothing proves the filter exists.",
     "finalSeverity": "P2",
     "confidence": "high",
     "downgradeTrigger": "A cache-excluding rule inside `package_skill.py` or in the skill's own ignore file, whichever the packager actually honours."
   }
   ```

## Traceability Checks

| Protocol | Level | Status | Evidence |
|---|---|---|---|
| `spec_code` | core | partial | `sk-create-skill/SKILL.md:98-121` required standalone shape and `:203-231` parent-hub shape diffed against both packet trees and the hub root; the two deviations are recorded above, the remaining shape elements match |
| `checklist_evidence` | core | partial | both new findings cite the exact rule line they break (`sk-create-changelog/SKILL.md:10`, `sk-create-skill/SKILL.md:95`), not a house-style judgement |
| `skill_agent` | overlay | partial | all three `SKILL.md` files carry `name`/`description`/`allowed-tools`/`version`, and each `name` matches its folder (`sk-product-owner`, `sk-create-figjam`); the four-part versions are `1.0.28.0`, `1.2.16.0`, `1.0.18.0` |
| `agent_cross_runtime` | overlay | notApplicable | no agent definition in this surface |
| `feature_catalog_code` | overlay | notApplicable | no feature catalog exists under the hub; the `sk-create-feature-catalog` mode owns catalogs elsewhere and no Product Owner artifact routes to it |
| `playbook_capability` | overlay | pass | hub index `manual-testing-playbook/manual-testing-playbook.md:1-30` declares the four-mode scope and the result-persistence contract, `hub-routing/` holds the 7 named scenario files, and `benchmark/reports/` run folders follow the `<YYYY-MM-DD>--<subject>--<variant>` grammar from `sk-create-skill/SKILL.md:110-121` |

## Integration Evidence

Named `sk-doc` surfaces actually checked, not merely referenced: the hub router `sk-doc/SKILL.md:22-46`, `sk-create-skill` (package shape and frontmatter contract), `sk-create-changelog` (placement and deprecation), `sk-create-manual-testing-playbook` and `sk-create-benchmark` (ownership hand-off read at `sk-create-skill/SKILL.md:136-140`), `sk-create-feature-catalog` (checked for a routed consumer, none found), and `sk-create-frontmatter` (owns the four-part `version` derivation the three frontmatters satisfy). The `sk-doc` parent-hub runtime resolver `.skilled/bin/compiled-route.cjs` was not executed; `sk-doc` itself records that compiled routing is its default, and executing it is outside a read-only review iteration.

## Edge Cases

- **Rule conflict inside `sk-doc`.** `sk-create-skill/SKILL.md:165` still mandates a per-packet `changelog/` folder while `sk-create-changelog/SKILL.md:10` deprecates exactly that folder. Adjudicated as a documentation conflict owned by `sk-doc`, not as a Product Owner defect: the Product Owner files are 92 pre-existing entries that `:94` keeps valid. Reported as context for finding 1 and left unresolved because resolving it means editing `sk-doc`, which is out of scope.
- **Budget deferral carried from iteration 2.** The `vendor.json` and `SYNC.md` pin read that would settle whether the diverged validator's pin is recorded is still deferred, not exhausted. It is not repeated here because this iteration's focus is `sk-doc` alignment.
- **Non-drift deliberately hunted and cleared.** Three plausible `sk-doc` deviations were examined and ruled out rather than filed; they are listed under Ruled Out so a later iteration does not re-open them.

## Confirmed-Clean Surfaces

- `AI Systems/Product Owner/SKILL.md:2-5`, `sk-product-owner/SKILL.md:2-5` and `sk-create-figjam/SKILL.md:2-5` all satisfy the four-field frontmatter contract at `sk-create-skill/SKILL.md:144-149`, including the four-part `version`.
- `AI Systems/Product Owner/benchmark/README.md` exists, and `benchmark/reports/` holds dated run folders in the shape the contract names.
- The packet shape holds for both workflow packets: `SKILL.md` + `ROUTER.md` + `README.md` + `references/` + `assets/` + `changelog/` + `manual-testing-playbook/`, with `scripts/` added only on the packet that runs code.
- The hub playbook index delegates packet-local artifact tests rather than duplicating them, matching the corpus/output split the contract describes.

## Ruled Out

- **`references/README.md` missing from both packets**: ruled out. All eight installed skills that carry a top-level `references/` folder also lack one, and `sk-create-skill/SKILL.md:48` describes that packet's own route map rather than a rule imposed on every package.
- **`procedures/` missing from the workflow packets**: ruled out. The rule at `sk-create-skill/SKILL.md:167` is conditional, and the reference implementation `sk-create-skill` itself carries no `procedures/` folder.
- **`benchmark/` shape deviation**: ruled out. `benchmark/README.md` is present and `reports/` uses the contracted dated folder grammar.
- **`leaf-manifest.config.json` missing at the hub root**: ruled out. The parent-hub shape at `sk-create-skill/SKILL.md:203-215` does not list it; only a class-S standalone skill authors one.

## Verdict

Two P2 findings this iteration, no P0 and no P1 raised. The verdict is carried by the two active P1 findings from iteration 2, which remain open and unremediated.

## Next Dimension

`security`, per the strategy's queued focus: path containment in `scripts/vendor-sync.py` and `scripts/code-mode.cjs`, `benchmark/gates/check_markdown_links.py` path resolution, the fixture harnesses' shell quoting, and the Sync Loop Python entry points. The `sk-doc` alignment direction is now largely swept; what remains of it is the changelog placement decision, which needs a maintainer choice rather than more reading.

Review verdict: CONDITIONAL
