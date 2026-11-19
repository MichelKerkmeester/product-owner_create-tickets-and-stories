# Deep Review Iteration 004

**Run:** `2026-11-10T18:34:20Z` | **Session:** `2026-11-10T18:34:20Z` | **Generation:** 1 | **Lineage:** new
**Mode:** review | **Target agent:** `@deep-review` | **Resolved route:** `mode=review target_agent=deep-review`

## Dimension

`maintainability`, the fourth and final dimension. Coverage is now 4 of 4.

Two things bound this pass. The iteration-1 duplication finding (three diverging `norm` copies at `mcp-tools.md:579`, `:626` and `:714`) had to be either confirmed or closed, and the strategy named reading all three copies in full as required evidence, so the duplication axis was read to its end rather than sampled. The operator's maintainability-adjacent focus items were also still open: the size of section 8, the feedback-ticket template against Task Mode and the Claude Project mirror, fixture naming, and the house writing rules on em dashes, semicolons and the Oxford comma.

## Files Reviewed

| Surface | Lines read | Why |
| --- | --- | --- |
| `mcp-click-up/references/mcp-tools.md` | `:332`-`:918` (all of section 8), heading map for all 944 lines | Duplicated normalizers, duplicated programs, section size, leftover-marker lists |
| `benchmark/format/run_fixtures.sh` | `:1`-`:175` (62 `check` calls) and fixture-name references throughout | Fixture wiring, assertion style, naming convention |
| `z — Claude Project Sync Loop/run_fixtures.sh` | name references, `:427`-`:496` (117 assertions) | The byte-parity twin harness |
| `benchmark/format/fixtures/` (21 files) and `z — Claude Project Sync Loop/fixtures/` (56 files) | full directory listings, byte diff of the three new fixtures | Fixture duplication across the two trees |
| `sk-product-owner/assets/task-templates.md` | `:297`-`:385` (Section 6, the feedback ticket) | Template wording |
| `sk-product-owner/references/task-mode.md` | `:43`, `:69`, `:83`, `:243`-`:254` (Section 3, Feedback Tickets) | Mode wording against the template |
| `claude project/knowledge/Product Owner - Assets - Task Templates.md` | `:277`-`:359` | The Claude Project mirror of Section 6 |
| `SYNC.md` | em-dash and semicolon hits with line context (`:43`, `:44`, `:69`, `:98`, `:130`, `:131`) | House writing rules |
| `vendor.json` | the `mcp-click-up` file map | Vendored manifest integrity |
| `z — Claude Project Sync Loop/feature-catalog/output-format-gate/output-format-validator.md` | `:1`-`:67` | `feature_catalog_code` overlay, deferred twice |

## Findings - New

### P0 Findings

None.

### P1 Findings

None new. Three P1s from earlier iterations remain open and are not re-reported here: `R1-P1-001` (the browser-first delivery gate cannot fail on a lost divider or a lost indent), `R2-P1-001` (ungated local image read), `R3-P1-001` (packet 028 certifies mirror-to-source equality with a gate whose own contract excludes it).

### P2 Findings

1. **The delivery report's gap count is computed by two different expressions, so the same page can be delivered or refused depending on which browser ran** -- `AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:694` -- The Aside program writes `const gapsLeft = browser.editor && !browser.login && browser.done !== false ? (browser.left ?? plainHits) : plainHits;` while the Chrome program writes `const gapsLeft = editor && !login ? left : plainHits;` at `:776`. Same reported field, same step-4 contract ("A page with gaps left or changed text is not delivered", `:614`), two different guards. The Aside expression carries `done !== false`, which the loop at `:686` makes unreachable as a false when a parsed result exists, and a `??` fallback the Chrome expression lacks, so the only live difference is which unset state maps to `plainHits`.
   Case: an Aside REPL call that returns an unparseable string leaves `browser = { error: ... }` at `:690`, so `browser.editor` is `undefined` and `gapsLeft` falls back to `plainHits`, which counts an image at the end of a page as a gap. The Chrome path has no such object and reports `left` from the editor pass instead. Two runs over the same page state therefore disagree about the gap count that decides delivery.
   Finding class: maintainability
   Scope proof: both expressions are inside section 8 of a file in the declared review target, and both feed `report.push` at `:695` and `:777`.
   Affected surface hints: `AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md`, `AI Systems/Product Owner/specs/system/026-browser-first-doc-writer/implementation-summary.md`

2. **The "leftover placeholder" marker set is enumerated in three places with three different member lists, so one leak is one finding on one path and two on another** -- `AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:570` -- The page-writer verify block matches `(BODY|IMG-\d+|COLS|\||\/COLS)` at `:570`. The read-back normalizer ten lines below filters only `(COLS|\||\/COLS)` at `:580`, so `BODY` and `IMG-n` stay in `importDiff` while the other three are dropped. The columns program keeps a third list, `markers.filter(...)` plus `IMG-[^\]]*` at `:905`, keyed on a `markers` variable rather than a regex. Three hand-maintained enumerations of one defect family, pairwise different.
   Case: a page that leaks `[[COLS]]` on the page-writer path is reported once, by `leftovers`. A page that leaks `[[BODY]]` on the same path is reported twice, by `leftovers` and by `importDiff`, because `:580` never filters it. A maintainer adding a fourth marker to `:570` and forgetting `:580` and `:905` silently converts a "not delivered" page into a delivered one.
   Finding class: maintainability
   Scope proof: all three sites are inside the declared review target; `:570` and `:580` are in the same verify block, `:905` is in the columns program in the same section.
   Affected surface hints: `AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md`, `AI Systems/Product Owner/specs/system/026-browser-first-doc-writer/implementation-summary.md`

3. **`checkbox-form-violation.md` is the only rule fixture in either tree that carries its near-miss assertion inside a violation file, and it has no `-silent` twin** -- `AI Systems/Product Owner/benchmark/format/run_fixtures.sh:172` -- Every other rule in `benchmark/format/fixtures/` and `z — Claude Project Sync Loop/fixtures/` splits the two cases into `{rule}-silent.md` and `{rule}-violation.md`: `mask-paths`, `catalog-entry`, `conciseness`, `house-grammar`, `length-caps`, `delivery-placeholder`, `requirements-narration`, `over-compression`, `sanctioned-shapes`, `artifact-purity`. The new checkbox-form rule ships one file, and its silent assertion is expressed as an expected exit of 1 with an empty required output and a forbidden output at `:172` (`check "checkbox form: the house form stays silent" 1 "" "checkbox-form-violation.md:14:"`). The mark-as-done rule does follow the convention, so the divergence is visible inside the same commit window.
   Case: a maintainer editing `checkbox-form-violation.md` to add a violation case moves line 14, and the near-miss assertion at `:172` silently starts asserting about a different line while the harness stays green on the moved text. A `-silent` file would have made the two intents independent.
   Finding class: maintainability
   Scope proof: the fixture file and both harness lines are inside the declared review target, and the convention is read off the 21-file and 56-file directory listings.
   Affected surface hints: `AI Systems/Product Owner/benchmark/format/fixtures`, `AI Systems/Product Owner/benchmark/format/run_fixtures.sh`, `AI Systems/Product Owner/benchmark/format/README.md`

4. **The two fixture harnesses pin different amounts of the shared core, and the new rows are written in two different helper styles** -- `AI Systems/z — Claude Project Sync Loop/run_fixtures.sh:487` -- The Product Owner harness makes 62 `check` calls; the Sync Loop harness makes 117. The new mark-as-done rows use plain `check` in both (`benchmark/format/run_fixtures.sh:155`-`:162` against `:427`-`:434`), while the new checkbox-form rows use plain `check` in the Product Owner harness (`:168`-`:174`) and `check_core ... --system product-owner` in the Sync Loop harness (`:487`-`:492`), which additionally asserts the same fixture against `barter-copywriter` at `:496`. So the same commit window added the same rule to two harnesses in two shapes, and only one harness covers the cross-system half.
   Case: the shared validator core gains a rule that the Sync Loop harness pins and the Product Owner harness does not. Both harnesses stay green, so the system under review can regress against the core it vendors without either gate turning red.
   Finding class: maintainability
   Scope proof: both harnesses appear in `config.reviewScopeFiles`; the counts are mechanical (`grep -c '^check '`), and the helper names are read directly.
   Affected surface hints: `AI Systems/Product Owner/benchmark/format/run_fixtures.sh`, `AI Systems/z — Claude Project Sync Loop/run_fixtures.sh`, `AI Systems/z — Claude Project Sync Loop/systems.py`

## Operator Focus Disposition

The four named focus items were all addressed across iterations 1 to 4. This pass closed the two that traceability left open.

- **ClickUp page writer converter and verify logic.** Iteration 1 read the converter branch by branch (open P1 on the delivery gate). This pass read the verify block's own bookkeeping and found that the gap count that decides delivery is computed two ways (finding 1) and that the leftover-marker family is enumerated three ways (finding 2). The verify block does not prove a clean page by a single contract, it proves it by four independently maintained counters.
- **The flipped Mark-as-done rule and its byte-parity twin.** Iterations 1 and 2 ruled out twin divergence inside the rule text. This pass moved to the harnesses that pin it and found the assertion-count and helper-style asymmetry (finding 4).
- **Feedback ticket template against Task Mode and the Claude Project mirrors.** Read Section 6 at `task-templates.md:297`-`:385`, Task Mode Section 3 at `task-mode.md:243`-`:254`, and the mirror at `claude project/knowledge/Product Owner - Assets - Task Templates.md:277`-`:359`. The three agree on the title grammar, on `## Feedback` replacing `### Requirements`, on the release-blocking line and on the grouping rule, and the mirror carries the release-blocking sentence the source carries. No finding.
- **Version and count drift across READMEs, SYNC.md and changelogs.** Iteration 3 opened three drift findings (`R3-P2-001`, `R2-P2-002`, `R3-P2-002`, `R3-P2-003`). Nothing new this pass, and the three em dashes in `SYNC.md` are inside maintenance records that name the literal path `z — Knowledge/`, so they are not prose dashes.

## Traceability Checks

| Protocol | Level | Status | Evidence |
| --- | --- | --- | --- |
| `spec_code` | core | partial | No packet file was re-read this pass, so no new requirement-to-code mapping is claimed. The four findings are prose-to-artefact inside section 8 and inside the fixture trees. |
| `checklist_evidence` | core | finding | Carried from iteration 3. The observation-shaped verify rows in 027 and 028 still go stale unnoticed, and this pass added no new evidence that they reproduce. |
| `skill_agent` | overlay | clean | Carried from iteration 3. Kernel H1 `v1.2.18` equals `README.md:128`, and all three release links resolve. |
| `agent_cross_runtime` | overlay | finding | New. The two fixture harnesses that pin the same core make 62 and 117 assertions and use two helper styles (`benchmark/format/run_fixtures.sh:168`-`:174` against `z — Claude Project Sync Loop/run_fixtures.sh:487`-`:496`). |
| `feature_catalog_code` | overlay | clean | Read `feature-catalog/output-format-gate/output-format-validator.md:42`-`:55`. Its Source Files table names the handler, the shared registry, the test harness, the fixtures and `reference-parity.cjs`, and every role matches what this session observed. Recorded limitation: the entry documents the Sync Loop tree only, so it is silent on the Product Owner twin, which is why it could not have caught finding 4. |
| `playbook_capability` | overlay | deferred | The 14 manual-testing-playbook files in the review scope were not read. This is the last iteration, so the protocol closes unverified rather than clean. |

## Integration Evidence

- `benchmark/format/run_fixtures.sh:155`-`:175` and `z — Claude Project Sync Loop/run_fixtures.sh:427`-`:496` were read together as one rule triple with the validator and the fixtures. The comparison is what produced finding 4.
- `feature-catalog/output-format-gate/output-format-validator.md:44`-`:55` names five source files. Each one exists at the path the entry gives, and each role matches the file's actual content as read this session.

## Edge Cases

- **The maintainability fix path for section 8 runs upstream, not here.** `vendor.json` records a SHA-256 for `mcp-click-up/references/mcp-tools.md` (`53b1c0b3...`) inside the `mcp-click-up` vendored entry. Section 8 is 587 of the file's 944 lines (`:332`-`:918`), and the one-topic concentration plus the four embedded programs is the direct cause of findings 1 and 2. Splitting the programs into an asset would break the recorded hash, so the structural finding is recorded as context and the two concrete findings are the reportable ones. The recorded hash was **not** recomputed against the file as packet 026 left it, so no claim is made about whether the manifest is currently satisfied. Recorded as blocked in the search ledger, not as clean.
- **The `leftovers` regex at `:570` and the `norm` filter at `:580` are ten lines apart and already disagree.** That proximity is why finding 2 is P2 and not higher: the disagreement changes how a defect is classified in the report, never whether it is caught at all, because `leftovers` still holds the full set.
- **`markasdone-divider` as a name.** It runs the rule constant `MARK_AS_DONE` together with no separator while every other fixture hyphenates its rule name. Recorded as a naming observation folded into finding 3 rather than a separate finding, because the cost is the same one: a grep over the fixture directory no longer groups by rule.
- **House writing rules are clean on every changed prose surface.** Zero em dashes in `mcp-tools.md`, `task-templates.md`, `task-mode.md` and the Task Templates mirror. The 349 semicolons in `mcp-tools.md` are all inside fenced JavaScript (the first hit inside section 8 is `const WORKSPACE = "WORKSPACE_ID";`), and `task-templates.md` and `task-mode.md` carry none at all. `SYNC.md`'s three em dashes are inside maintenance records naming the literal `z — Knowledge/` path. No Oxford-comma construction needed adjudication on these surfaces.
- **Budget.** This iteration used one tool call more than the soft max to obtain exact line numbers for the duplicated symbols, because five of the nine findings-adjacent claims in this pass depend on telling `:694` from `:776` and `:570` from `:580`. The overrun is recorded rather than absorbed.

## Confirmed-Clean Surfaces

- `benchmark/format/fixtures/checkbox-form-violation.md`, `markasdone-divider-silent.md` and `markasdone-divider-violation.md` are byte-identical to their `z — Claude Project Sync Loop/fixtures/` counterparts. The two trees have not drifted on any fixture added in this commit window.
- `sk-product-owner/assets/task-templates.md:297`-`:385`, `sk-product-owner/references/task-mode.md:243`-`:254` and `claude project/knowledge/Product Owner - Assets - Task Templates.md:277`-`:359` agree on the feedback-ticket title grammar, the `## Feedback` substitution, the release-blocking line and the one-area-versus-many-areas grouping rule.
- `feature-catalog/output-format-gate/output-format-validator.md` names five source files and all five match their stated roles.
- No em dash appears in any prose surface changed in this commit window.

## Ruled Out

- **Fixture drift between the two trees.** `diff` is empty for all three new fixtures, and both harnesses reference all three (`benchmark/format/run_fixtures.sh:155`-`:175`, `z — Claude Project Sync Loop/run_fixtures.sh:427`-`:440`).
- **A house-rule violation on the new prose.** Em dash count is zero on all five changed prose surfaces, and every semicolon hit resolves to fenced JavaScript.
- **A single shared `norm` in the two programs that could simply be deduplicated.** The Aside and Chrome copies at `:626` and `:714` are identical, but the page-writer copy at `:579` is not, and the three sites are inside fenced markdown that is copied by a reader rather than imported. The duplication is real and unfixed, and this pass confirms the iteration-1 finding rather than closing it.
- **Feedback-ticket template drift against Task Mode and the mirror.** All three carry the same six rules and the same title grammar.
- **A feature-catalog entry that contradicts the code.** Every file the entry names exists and matches its role.

## Traceability Follow-Ups

- `playbook_capability` closes unverified. The 14 files are in the review scope and were never read across four iterations.
- The `vendor.json` hash for `references/mcp-tools.md` is unrecomputed, so the manifest's current satisfaction is unknown.
- `run_gates.sh` was never located, so the "1 of 15 fails" row shared by all three packets remains recorded and unverified across two iterations.

## SCOPE VIOLATIONS

None. No write, rename or delete was attempted outside `specs/053-po-clickup-session-review/review/`.

## Next Focus

- Dimension: none. All four dimensions are complete and this is the last of the five configured iterations.
- Focus area: release decision on the three open P1s plus the 12 open P2s.
- Reason: `stopPolicy` is `max-iterations`, so convergence is telemetry only and the loop ends here regardless of ratio.
- Blocked carry-forward: `run_gates.sh` unlocated, `vendor.json` hash unrecomputed, the 14 playbook files unread, and the silent `- - -` fixture never read with `od -c` on this host.
- Productive carry-forward: reading two harnesses side by side as one artefact is what exposed the assertion-count asymmetry, the same way reading two normalizers side by side exposed the divergence.
- Required evidence: nothing further is reachable inside this loop.

## Verdict

Three P1 findings remain active and none of them was closed this iteration: `R1-P1-001`, `R2-P1-001`, `R3-P1-001`. The four findings raised here are all P2. Under the contract the verdict maps over findings active at this iteration rather than only the ones it raised, so an open P1 forces CONDITIONAL even though this pass added none.

Review verdict: CONDITIONAL
