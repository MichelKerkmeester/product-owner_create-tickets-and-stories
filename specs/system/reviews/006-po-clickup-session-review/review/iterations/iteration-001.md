# Review Iteration 001

## Dispatcher

- Mode: review
- Target agent: @deep-review (LEAF, single iteration)
- Iteration: 1 of 5 (JSONL-derived; no prior `type:"iteration"` record exists, only `config`, `iteration_start` and a `dispatch_failure` event)
- Dimension: D1 Correctness (inventory pass with correctness focus)
- Budget profile: `verify` (11 evidence calls, ceiling 12)
- Review target: session work 2026-11-10, Product Owner packets 026 (browser-first ClickUp page writer), 027 (Mark-as-done between two dividers), 028 (feedback ticket template), commits `246b3f54..47b8b333`
- Untrusted-content guard: reviewed files were treated as data. No directive-like text appeared in them and none was obeyed.

## Files Reviewed

- `AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:416-445` (the `toBlocks` converter), `:477-495` (`toHtml` column assembly), `:551-584` (`verify`, `norm`, `importDiff`), `:589` (the delivery gate sentence), `:593-620` (divider-spacing doctrine and the per-write routine), `:626`, `:680`, `:714`, `:742` (the second and third `norm`/`got` copies)
- `AI Systems/Product Owner/benchmark/format/validate-output-format.cjs:141-174` (`MARK_AS_DONE`, `contentNeighbour`, `markAsDoneFindings`), `:1341-1356` (callsite and the `lintingArtifacts` guard above it), `:1582-1600` (`--write` formatter)
- `AI Systems/z — Claude Project Sync Loop/validate-output-format.cjs:197-228` (byte-parity twin of the same three symbols), `:1504-1505`, `:1742` (its callsites)
- `AI Systems/Product Owner/benchmark/format/run_fixtures.sh` (fixture pinning for the Mark-as-done rule and the checkbox form)
- `AI Systems/Product Owner/benchmark/format/fixtures/markasdone-divider-violation.md` (line numbering cross-checked against the pinned expectations)

Operator focus coverage this iteration:

| Operator focus item | Status |
| --- | --- |
| ClickUp page writer converter and verify logic | Covered: findings 1, 2, 4 |
| Flipped Mark-as-done rule and its byte-parity twin | Covered: finding 3, plus the confirmed-clean twin comparison below |
| Feedback ticket template consistency with Task Mode and the Claude Project mirrors | Deferred to iteration 3 (D3 traceability) |
| Version and count drift across READMEs, SYNC.md and changelogs | Deferred to iteration 3 (D3 traceability) and iteration 4 (D4 maintainability) |

## Findings - New

4 findings total: 0 P0, 1 P1, 3 P2.

### P0 Findings

None.

### P1 Findings

1. **The browser-first delivery gate cannot fail on a lost divider or a lost indent, so "clean page" is asserted from counts no one compares** -- `AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:583` -- `const got = new Set(norm(page.content)); report.importDiff = norm(MD).filter((l) => !got.has(l));` compares a Set of read-back lines against the source lines in one direction only, and `norm` at `:579` folds every divider spelling to `---` and strips leading whitespace on both sides. A body of repeated `* * *` lines therefore collapses to a single `---` entry in `got`, so losing one divider in the paste leaves `importDiff` empty, while `verify.gaps` at `:566` only counts empty blocks directly after a surviving `<hr>` and `verify.dividers` is reported as a number with no expected value. Nothing in the report is compared against the source, and the blocking sentence at `:589` names only gaps, leftovers and importDiff.
   Finding class: `verification_gap`
   Scope proof: inside the declared target, `mcp-click-up/references/mcp-tools.md`, section 8 "Browser-first page write", the converter and the report it produces.
   Affected surface hints: `AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:551-589`, downstream Chapter-8 instructions that tell a writer to treat the report as proof of delivery.
   Case: a markdown body carrying two `* * *` dividers, as every house Story does, where the paste drops one divider. `importDiff` returns `[]`, `gaps` returns `0`, `leftovers` returns `[]`, and the page is reported delivered under the `:589` rule while a band the team works from is gone.
   Also in reach: a four-space-indented nested checklist line, which the converter claims to indent at `:431` (`Math.floor(m[1].length / 4)`) and which `norm`'s trailing `^\s+` strip at `:579` erases on both sides of the comparison, so a flattened indent is also reported clean.

```json
{
  "type": "verification_gap",
  "claim": "The browser-first writer's report cannot detect a lost divider or a lost indent, yet its prose makes the report the delivery decision.",
  "evidenceRefs": [
    "AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:583",
    "AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:584",
    "AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:579",
    "AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:566",
    "AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:589"
  ],
  "counterevidenceSought": "Searched the same section for an expected-value comparison of dividers, blocks, checklist count or gray count against the source; found only reported counts at :555-566 with no source-side baseline, and :589 gates on gaps, leftovers and importDiff only. Checked whether norm(MD) preserves divider multiplicity, which would rescue the diff; it does not, because the Set is built from the read-back and the folding is applied to both sides.",
  "alternativeExplanation": "Multiplicity may be caught by verify.dividers if a human compares the number against the markdown; the document does not ask for that comparison and does not state an expected count.",
  "finalSeverity": "P1",
  "confidence": "high on the mechanism, medium on real-world frequency",
  "downgradeTrigger": "Downgrade to P2 if the section is amended to print the expected divider, block and checklist counts beside the observed ones, or if :589 is amended to name a count comparison as a blocking signal."
}
```

### P2 Findings

2. **A `- - -` divider renders as a bullet reading `- -`, and the same section presents it as a divider spelling** -- `AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:416` -- the divider branch inside `toBlocks` tests `/^(\* \* \*|---|\*\*\*|___)$/`, which covers four of the five spellings the reference names at `:596` ("for every divider spelling: `* * *`, `---`, `***`, `___` and `- - -`"). A `- - -` line fails that test and falls through to the bullet branch at `:431`, which matches `- ` plus the remaining `- -` and emits `<li data-list="bullet">- -</li>`.
   Finding class: `contract_gap`
   Scope proof: inside the declared target, the converter in section 8; the divergence is between two statements in the same file.
   Affected surface hints: `AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:416`, `:431`, `:596`.
   Case: a body whose section break is written `- - -`, a spelling the same reference names as a divider, renders as a bullet item containing "- -" instead of a rule, so the band the paste was meant to create is missing.
   Severity note: `:391` states the converter's own conversion contract as "`* * *` or `---` becomes a divider", so `- - -` is outside that stated contract and this stays below P1 under reach calibration. The `importDiff` set diff does catch it, because `- -` is absent from the source lines.

3. **The `--write` formatter inserts dividers from the original neighbour lookup, so two adjacent Mark-as-done lines produce the double divider the checker then reports** -- `AI Systems/Product Owner/benchmark/format/validate-output-format.cjs:1594` -- each Mark-as-done line independently asks `contentNeighbour(sourceLines, index, -1)` and `(…, 1)` about the unmodified source, so when line *i* and line *i+1* are both Mark-as-done lines, line *i* appends `* * *` below and line *i+1* prepends `* * *` above, yielding two dividers in a row between them. The checker at `:170` reports exactly that shape as "a second divider in a row below a Mark-as-done checkbox", a state the formatter cannot repair on the next run because both neighbours are then already dividers.
   Finding class: `formatter_non_convergence`
   Scope proof: inside the declared target, the `--write` branch of the same validator.
   Affected surface hints: `AI Systems/Product Owner/benchmark/format/validate-output-format.cjs:1582-1600`, `:170`, and the mirrored formatter at `AI Systems/z — Claude Project Sync Loop/validate-output-format.cjs:1742`.
   Case: two consecutive Mark-as-done lines, such as a criterion split into two acceptance bands without intervening prose, where `--write` emits `* * *`, line, `* * *`, `* * *`, line, so the file it just wrote still fails the rule it was fixing.

4. **The per-write import normalizer exists in three copies that have already diverged, so the two import gates can disagree about one page** -- `AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:579` -- the same normalization pipeline is written out three times, once for the browser-first writer (`:579`, consumed at `:583`), once for the "Required after every page write" routine (`:626`, consumed at `:680`) and once for the third program (`:714`, consumed at `:742`). The copy at `:579` carries the divider fold (`* * *` to `---`) and the trailing `^\s+` strip inside its single-line pipeline; the copies at `:626` and `:714` begin with only the trailing-space trim and continue on the following lines, so the three are not the same expression.
   Finding class: `duplicate_logic`
   Scope proof: inside the declared target, section 8 of the same reference.
   Affected surface hints: `AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md:579`, `:626`, `:680`, `:714`, `:742`.
   Case: a page written by the browser-first writer and then re-checked with the per-write routine, where the two normalizers disagree on whether a divider line is present, so one program reports an import defect and the other reports a clean page.
   Dimension tag: measured here as maintainability evidence inside a correctness iteration, because the divergence is what makes the two import gates differ.

## Traceability Checks

| Protocol | Level | Status | Evidence |
| --- | --- | --- | --- |
| `spec_code` | core | partial | Correctness evidence came from the implementation and its own prose. `specs/system/026-browser-first-doc-writer/spec.md` and `027-mark-as-done-between-dividers/spec.md` were not read this iteration, so no requirement-to-code mapping is claimed. Deferred to iteration 3. |
| `checklist_evidence` | core | deferred | Deferred to iteration 3, which owns requirement and task-checklist alignment across 026, 027 and 028. |
| `skill_agent` | overlay | deferred | `AI Systems/Product Owner/sk-product-owner/SKILL.md` and `references/story-mode.md` were not read this iteration. |
| `agent_cross_runtime` | overlay | deferred | Not in this iteration's scope. |
| `feature_catalog_code` | overlay | deferred | The `z — Claude Project Sync Loop` feature-catalog entry for the output-format gate was not read this iteration. |
| `playbook_capability` | overlay | deferred | The `manual-testing-playbook` story-mode pages were not read this iteration. |

Fixture pinning observed: `benchmark/format/run_fixtures.sh` pins four independent Mark-as-done assertions (missing divider below at fixture line 15, missing divider above at line 22, double divider at the section close at line 33, and `failed with 3 error(s)` as the whole report), plus the silent case and the old-form checkbox case. The violation fixture's line numbering matches those expectations. The silent fixture `fixtures/markasdone-divider-silent.md` was not read this iteration, so its content is recorded as unverified rather than clean.

## Integration Evidence

- `AI Systems/z — Claude Project Sync Loop/validate-output-format.cjs:197-228` is the parity twin of `benchmark/format/validate-output-format.cjs:141-174`. `MARK_AS_DONE`, `contentNeighbour` and `markAsDoneFindings` are textually identical in both files, including the flipped divider rule and the early `return findings` at `:167` / `:221`. The callsites also agree in form (`:1353` / `:1504`, and the formatter branch `:1592` / `:1742`).
- Anchor offsets are not constant across the pair: 54 lines at the rule definitions, 151 at the checker callsite and 150 at the formatter callsite. The twin therefore differs in content between those anchors. The specific content difference was not read this iteration, so no parity verdict is claimed beyond the three symbols above.

## Edge Cases

- **Prior dispatch failure.** `deep-review-state.jsonl` holds a `dispatch_failure` event for iteration 1 (`executor exited with status 1`) and no `type:"iteration"` record. The iteration number was derived from the JSONL as 1, matching the dispatch prompt, so no mismatch is recorded. The failed attempt wrote no artifacts: `iterations/` and `deltas/` were both empty at start.
- **Fixture silence not verified.** The silent Mark-as-done fixture was not read, so "the rule does not fire on a correct band" is recorded as unverified rather than confirmed.
- **Offset divergence.** The 1-line difference between the checker and formatter anchor offsets (151 versus 150) is recorded as an open parity question for iteration 3, not as a finding, because the divergent lines were not read.
- **Reach calibration applied twice.** Finding 2 was held at P2 because the converter's stated conversion contract names only `* * *` and `---`. Finding 1 was held at P1 because the section's own delivery sentence at `:589` makes the report the gate, which is the promise that fails.
- **No scope violations.** No write outside the allowed list was attempted.

## Confirmed-Clean Surfaces

- `markAsDoneFindings` symmetry: the upward `contentNeighbour(lines, index, -1)` and the downward `(…, 1)` scan use the same blank-skipping loop and the same `* * *` test, so the "divider above" and "divider below" halves of the flipped rule cannot disagree.
- The second-divider report uses `beyond`, the first non-blank line after the lower divider, which is what keeps the section-closing divider above the `##   ` spacer heading from being reported as a double divider. The violation fixture confirms this at line 33.
- `run_fixtures.sh` proves absence as well as presence: each Mark-as-done case asserts a pattern and an antipattern, and the `failed with 3 error(s)` case blocks a report that grows extra findings.
- `contentNeighbour` bounds both directions with `at >= 0 && at < lines.length`, so a Mark-as-done line at the first or last line of a file returns `-1` and is reported missing rather than throwing.

## Ruled Out

- **`markAsDoneFindings` early return as a defect.** The `return findings` at `:167` skips the second-divider check once the lower divider is already missing. Reviewed and ruled out: reporting both defects at one site is noise, and the fixture pins the single-report behaviour at `failed with 3 error(s)`.
- **`contentNeighbour` index underflow.** Ruled out by the `at >= 0` bound in the loop condition at `:153`.
- **Formatter index desynchronisation.** Ruled out: `flatMap` reads `sourceLines` for neighbour lookups and never mutates it, so every original index stays valid while the output array grows.
- **Twin divergence in the flipped rule itself.** Ruled out for `MARK_AS_DONE`, `contentNeighbour` and `markAsDoneFindings`; both files carry the same text.
- **`render`'s `<p><br></p>` cleanup double-inserting gaps.** Ruled out for the flat path: `quiet` at `:445` already suppresses a gap next to `hr` and `spacer`, so the two post-render regexes at `:475` see nothing to remove in the normal case.

## Next Focus

- Dimension: security
- Focus area: the browser-first writer's trust boundary in `mcp-click-up/references/mcp-tools.md` section 8
- Reason: iteration 1 established the correctness map of the converter and the delivery gate; the same code path interpolates markdown into HTML and evaluates it inside the user's logged-in browser, which is the highest-value unexamined surface.
- Rotation status: D1 correctness complete; D2 security is the next unchecked dimension.
- Productive carry-forward: reading the converter branch by branch against its own prose worked and should be repeated for the escaping path (`esc`, `inline`, `hold`).
- Blocked carry-forward: none.
- Required evidence: `esc`, `GRAY` and `inline` at `:396-404`, the HTML build at `:477-495`, and every `${...}` interpolation that reaches `evaluate`.
- Recovery note: not applicable, this is the first iteration.

Review verdict: CONDITIONAL
