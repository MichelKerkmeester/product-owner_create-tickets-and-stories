<!-- Round 4 review of remeasure-4. Reviewer: SWE-2 Max, Devin CLI, dangerous mode with a read-only instruction, worktree diffed afterwards: no file written. Covers all three systems. -->

# Round 4 remediation review: `remeasure-4` grading

Method note. Every file claim was checked against `meta.json` and `exports/`, every reply against `transcript-turn-N.md`, and every grade against the scenario definition as it stands now. Grading convention follows the two final reviews: PARTIAL means a named expected signal or pass bullet is unmet while no fail clause fires. Deal Templates scope is `SDP-004` and `PDP-004`, the only two folders executed. Copywriter scope is `SDL-001`, `PDL-001`, `SEN-001`, `PEN-001`, `SEN-002`, `PEN-002`, `SID-001`, `PID-001`.

## 1. Grading tables

### Barter - Deal Templates

**SDP-004** (skill, `export/001 - deal-product-penhold.md` in all three runs)

| Run | Verdict | Quoted evidence |
|---|---|---|
| 1 | PASS | Lead: `For anyone who's into stationery.` Reply: `` `export/001 - deal-product-penhold.md` `` then `DEAL Score: 24/25 \| HVR: Clean`. Ledger: file created, but the turn ends on `write` with no read-back. |
| 2 | PASS | Lead: `For anyone who's into stationery.` Reply: `Saved: export/001 - deal-product-penhold.md`. Ledger shows `write` then `read` on the export path. |
| 3 | PASS | Lead: `For anyone who likes to show off their setup.` Reply self-reports the gate: `the creator-fit lead passing the name test ("setup", a standing name, not one built from the offer)`. Ledger shows `write` then `read`. |

Lead and bullet detail per run:

- Run 1. Lead `For anyone who's into stationery.` takes declared shape 3 (`For anyone who's into [name].`). `stationery` is a standing interest name, the same name both final reviews passed in remeasure-3 as `a real interest domain`. It is not the offer noun plus `content`/`creator`/`niche`/`lover`/`fan`, it leaves people out, it is one sentence on one line, and it names the interest domain rather than the deal's €100 facts, so checks 1-6 hold. Bullets: `You film unboxings and first reactions` and `Your audience watches stationery hauls` and `You show your desk setup on camera` carry standing format or genre names. `You want fresh picks for your desk` invokes no name at all, a desire bullet, tolerated under the worked-example reading (the MINISO example ships `You film everyday fun`). Most concise correctly carries no lead; its bullets are `You film unboxings on camera` (standing) and `Your audience follows what lands on your desk` (descriptive, no name invoked, none invented).
- Run 2. Same lead, same verdict. Bullets: `desk setups and what's on your desk videos` and `stationery hauls and unboxings` are standing names. `You give your desk a refresh on camera` is descriptive. `You want stationery you get to keep` is an offer-fit desire bullet, the same class reviewers noted but did not fail in remeasure-3 (`You want a €100 desk upgrade you get to keep`). Most concise: no lead, two descriptive bullets.
- Run 3. Lead `For anyone who likes to show off their setup.` is shape 4 verbatim and the rule's own sanctioned example. Bullets: `desk setups and stationery hauls` and `what's-on-my-desk videos` are standing names. `You show new supplies in your day-to-day` and `You want fresh pieces for your filming background` are descriptive or offer-fit. Most concise: no lead, both bullets standing names.

Summary: all three runs take a declared shape with a standing name, no made-up name appears in lead or bullet, and Most concise omits the lead every time. The residual questions are check-2 strictness on nameless bullets (documented under diff audit) and run 1's skipped read-back (regression section).

**PDP-004** (project, rendered block, empty ledgers all three runs)

| Run | Verdict | Quoted evidence |
|---|---|---|
| 1 | PASS | Lead: `For anyone who likes to show off their setup.` Reply closes: `export/[NNN] - deal-product-penhold.md` / `DEAL 23/25 (D:5 E:7 A:5 L:6) \| HVR: clean`. The run read `Barter deals - Rules - Standards - v0.120.md`. |
| 2 | PASS | Lead: `For anyone who's into stationery.` Reply: `export/[NNN] - deal-product-penhold.md` / `DEAL 21/25 ... Floors: D5 E6 A4 L6, all pass`. Cleanest of the three, no preamble. |
| 3 | PASS | Lead: `For anyone who's into stationery.` Reply: `export/[NNN] - deal-product-penhold.md` / `DEAL 24/25`. |

Bullet detail:

- Run 1: `study-with-me videos`, `studygram posts`, and `stationery, planning and note-taking` are standing names. `You already shoot your posts at your desk` is a habit bullet invoking no name. Most concise carries two standing-name bullets, no lead. Two delivery-shape deviations not graded by this scenario: the reply opens with a `Route: $product → Product path...` facts paragraph before the block, and the block embeds an `<!-- Assumes: ... -->` comment beyond the header.
- Run 2: `stationery hauls and unboxings` and `desk-setup videos` standing, `You show new pieces in your routine` and `You want pieces you keep` descriptive or offer-fit. No lead in Most concise.
- Run 3: `stationery hauls and unboxings` and `desk setups` standing, `You test what lands on your desk, on camera` descriptive, `You want a whole set to keep` offer-fit. No lead in Most concise.

Summary: 6 of 6 Deal Templates runs pass the seven checks as the two final reviews applied them. For comparison, remeasure-3 went FAIL/PASS/PASS on both twins, with run-1 failures on `If you create stationery content.` (made-up name) and `If you're into stationery.` (undeclared shape). Both failure modes are absent in remeasure-4.

### Barter - Copywriter

**SDL-001** (skill)

| Run | Verdict | Quoted evidence |
|---|---|---|
| 1 | FAIL | Reply: `` `export/001 - write-creator-tagline.md` — saved and read back. MEQT 21/25, ship. `` File exists, header `Mode: $write`, read-back confirmed in transcript. But each of the four options carries a rationale sentence inside the body: `Barter's whole loop in four words. It answers the first question every new creator asks: what happens if I sign up.` The new fail clause `the body leaks scoring, rationale or process matter` fires. |
| 2 | PASS | `Saved to export/001 - write-creator-tagline.md (read-back confirmed).` Body: four bare task-fit-labelled options plus `Recommended: Most Barter`, header `Mode: $write`, verdict `MEQT 22/25, ship`, HVR status, `[Assumes:]` after the path, no floors or weakest-dimension line. |
| 3 | PARTIAL | `It ships six taglines grouped as 2 concise, 2 valuable and 2 authentic, plus a recommended pairing`. File exists, `Mode: $write`, ledger shows `write, read, edit, read` (a self-repair loop). Body: six grouped options plus a Recommended Combination whose appended two-sentence pairing note (`The first line lowers the bar, the second removes the risk...`) is rationale matter under the strict letter of the new clause. I grade PARTIAL because the note sits inside the one element whose job is to justify a pick; a strict grader would call it FAIL, and the twin asymmetry below makes the boundary worth flagging either way. |

Summary: exports, read-backs, `$write` headers, verdict order and reply hygiene are clean in all three runs. The remaining defect class is rationale prose inside the artifact body, the same class the author moved from unwritten to named-fail in this round.

**PDL-001** (project, all ledgers empty)

| Run | Verdict | Quoted evidence |
|---|---|---|
| 1 | PARTIAL | Block-first with `<!-- Mode: $write ...`, four grouped options, then `` `export/001 - write-new-creator-tagline.md` `` and `MEQT 21/25. Ships.` with `[Assumes:]` after the block. The block's Recommended Combination appends a rationale paragraph (`The primary line carries the mechanism, because paying with product instead of cash is what makes Barter different.`), which misses the expected signal `no other section, rationale or scoring matter`. PDL-001's fail list omits `rationale` where its twin's includes it, so no clause fires. |
| 2 | PARTIAL | Block clean: `Mode: $write`, six grouped options, bare Recommended Combination, `MEQT 22/25, ship \| HVR 0 hard blockers`. The reported path is malformed: `` `export/001 - $write-new-creator-taglines.md` `` puts `$write` in the filename's mode slot, so the `export/[###] - write-[description].md` shape is unmet. A strict reading of `puts anything else in its place` could grade this FAIL; the string is still a recognizable export path, so PARTIAL. |
| 3 | FAIL | No path at all. After the block the reply runs `HVR self-scan: 0 hard blockers...` then `MEQT 21/25, ship. I routed this as a $write, goal-based, at Standard energy...` and ends with a tightening offer. The `omits the export-equivalent path` clause fires. |

Summary: blocks render first in all three, headers are `Mode: $write` in all three, no file is claimed, no floors or weakest-dimension line appears, and `[Assumes:]` sits after the block in all three. The path contract, the item this round exists to fix, holds in only one run.

**SEN-001** (skill Fast, prompt `$f` then `A tooltip for the pricing page.`)

| Run | Verdict | Quoted evidence |
|---|---|---|
| 1 | FAIL | Turn 1 asks once, turn-1 ledger empty. Turn 2 writes and reads `export/001 - ux-pricing-page-tooltip.md` but the reply prints `it clears the Fast gates (compact-gate status: pass, 20/25)`. `Turn 2 prints a MEQT score` fires. |
| 2 | PASS | Turn 1 asks once, no artifact. Turn 2: `Fast lane: gates pass, options within the compact limit.` Export `export/001 - ux-pricing-tooltip.md` written and read, two options, `Mode: $ux`, no score. |
| 3 | PASS | `Fast lane, UX, 2 options, gates passed, no score narration.` Export written and read. |

**PEN-001** (project Fast, all ledgers empty)

| Run | Verdict | Quoted evidence |
|---|---|---|
| 1 | PARTIAL | Turn 1 asks once, renders nothing. Turn 2 renders a block headed `Mode: $fast` with a best pick plus two alternatives, reports `HVR clean \| Fast (compact gate)`, no score narrated. Three options exceed the scenario's `at most two options`, and both the header and the path `export/001 - fast-pricing-tooltip.md` put the energy token in the mode slot where the intent token belongs. |
| 2 | FAIL | Turn 1 asks once. Turn 2 renders no block: `One gap before I draft. What should the tooltip explain...` A second intake round after a meaningful task, and `renders no block` fires. |
| 3 | PARTIAL | Turn 2 renders a `Mode: $ux` block with two options and no score narrated, but the reply never reports compact-gate or HVR status, and the path is malformed: `Path: export/001 - $ux-pricing-page-tooltip.md`. |

**SEN-002** (skill Quick, `$q tagline for the Barter homepage aimed at creators`)

| Run | Verdict | Quoted evidence |
|---|---|---|
| 1 | PASS | `Compact gate: pass (Quick lane). HVR self-scan: 0 hard blockers.` No question, export written and read, five task-fit-labelled options, no score printed. Five options sit above the compact variant's three-line shape but below the six-option grid the fail clause names. |
| 2 | FAIL | Reply is clean (`Compact gate passes on the Quick lane, no printed score.`) but the export ships six labelled options, the full variation set for the 1-30 word tier, so `a full variation grid ships` fires. |
| 3 | PASS | `Compact gate passed, HVR self-scan: 0 hard blockers.` Recommended plus four labelled alternatives, export written and read, no score. Caveats: the reply carries two stray CJK tokens (`门槛`, `角度`) and a meta `(Note: ...)` line. |

**PEN-002** (project Quick, all ledgers empty)

| Run | Verdict | Quoted evidence |
|---|---|---|
| 1 | PASS | `` `export/001 - write-creator-homepage-tagline.md` \| HVR clean \| Quick (compact gate) ``. Block `Mode: $write`, best pick plus two alternatives, no score in the reply. Header reads `MEQT: ~21` inside the sanctioned comment, and the reply prose slips a stray `门槛`. |
| 2 | PASS | `Compact gate passed: HVR clean, creator terminology throughout`. Block `Mode: $write`, best pick plus three alternatives, no score. The reported path `export/001 - quick-creator-homepage-tagline.md` puts the energy token in the mode slot; the path shape is not a named element for this scenario, so it is a noted deviation, not a fail. |
| 3 | FAIL | The block ships the full 2/2/2 tiered grid (six options) plus a Recommended Combination, so `a full variation grid ships` fires. The reply itself is clean: `` `export/001 - write-creator-homepage-tagline.md` ``, `HVR 0 hard blockers, compact gate passed`, no score. |

**SID-001** (skill identity)

| Run | Verdict | Quoted evidence |
|---|---|---|
| 1 | PASS | `running from the skill package sk-barter-copywriter (v1.5.8...)` and `export/001 - write-new-creator-tagline.md (read back, confirmed)`. File exists, `Mode: $write`, final copy only. |
| 2 | PASS | `running from the skill package sk-barter-copywriter` and `export/001 - write-new-creator-tagline.md (read-back confirmed)`. Ledger: `write, read, edit, read`. |
| 3 | PASS | `running from the skill package sk-barter-copywriter (v1.5.8)` and `export/001 - write-creator-tagline.md (read back, confirmed)`. |

All three mention the Project packaging only to contrast it, which the scenario explicitly permits.

**PID-001** (project identity, all ledgers empty)

| Run | Verdict | Quoted evidence |
|---|---|---|
| 1 | PASS | Opens with the verbatim title line `# Barter Copywriter - Custom Instructions - v1.10.11`, states `Canvas Artifact` delivery, renders a `Mode: $write` block, reports `export/001 - write-new-creator-tagline.md`, claims no file. |
| 2 | PASS | `title line exactly as written: # Barter Copywriter - Custom Instructions - v1.10.11`, Canvas Artifact stated, block rendered, path reported. |
| 3 | PASS | `the loaded kernel is titled, exactly: > # Barter Copywriter - Custom Instructions - v1.10.11`, block-first, `export/001 - write-new-creator-tagline.md`, no file claim. |

The quoted line matches the kernel's line 1 byte for byte at run time.

## 2. Round 4, item by item

**Item 1, Deal Templates (five shapes in both prompts plus blocking creator-fit validation).** Behavior moved. `SDP-004` and `PDP-004` went 6 of 6 in remeasure-4 versus 4 of 6 in remeasure-3, and both named failure modes are gone: no `stationery content`-style product-noun name in any lead or bullet, and no undeclared sixth shape. Two corroborating details: `SDP-004` run 3's reply narrates the name test result, and all three `PDP-004` runs read the renamed `Standards - v0.120` knowledge doc. Two honest caveats. First, three runs certify direction, not a rate: the remeasure-3 failure rate was 1 of 3 per side. Second, `SDP-004` run 1 skipped the read-back entirely, so the new step-4 check cannot have run there even though its output happened to pass. Residual classification: model limit with a documentation ambiguity, detailed in section 5.

**Item 2, Copywriter (Project reports the export-equivalent path, and `PDL-001` grades it).** Partially moved. The remeasure-3 baseline was 0 of 3 correct (`Path: export-equivalent copy panel above`, `Path: $write, Standards energy...`, no path). Remeasure-4 produces one correct path (`export/001 - write-new-creator-tagline.md`), one malformed path (`export/001 - $write-new-creator-taglines.md`), and one omission. The scenario now names the path in its pass and fail lines, so the grading gap the reviewers flagged is closed. The behavior improved but does not bind reliably.

**Item 3, Copywriter (reply hygiene, `$` header token, `[Assumes:]` placement, aligned tagline shape).** Mostly moved. Across the six `SDL-001` and `PDL-001` runs: six of six headers read `Mode: $write` (remeasure-3 had `Mode: WRITE` in one), zero replies carry a floors line or weakest-dimension note (remeasure-3 had them in `PDL-001` runs 1 and 3 and `SDL-001` run 2), six of six `[Assumes:]` placements are correct (remeasure-3 had one above the block), and every body holds at most the six-option tier plus a Recommended Combination. The residual is rationale prose inside bodies, which the author's new `SDL-001` clause now catches: `SDL-001` run 1 fails it outright, and `SDL-001` run 3 and `PDL-001` run 1 show it inside the Recommended Combination.

**The author's added fail condition** (an unasked floors line or weakest-dimension note fails `SDL-001` and `PDL-001`) is sound. The governing text exists verbatim in `SKILL.md` Section 9 (`Unless the request asks for the score, the reply also carries no floors line and no note naming the weakest or lowest dimensions...`), `AGENTS.md` step 8, and the kernel's Section 9 paragraph, all added by this same commit. A scenario clause that enforces a written rule is exactly what the earlier reviews asked for.

## 3. Coverage findings

**Fast and Quick score narration.** Across eleven Fast and Quick delivery replies, one leaks a score: `SEN-001` run 1 turn 2 prints `(compact-gate status: pass, 20/25)`. The other ten keep the score out of the reply, and scores inside the artifact's comment header (`MEQT: 21/25` in a rendered block, or in a saved file's line 1) are sanctioned, not narration. Round-1 baseline had both project Fast and Quick printing full scores (`MEQT 21/25` and `MEQT 23/25 (M4, E7, Q6, T4, D2)`), so the project side improved from 0 of 2 clean to 6 of 6 clean. `PEN-001` run 2 delivered nothing at all on turn 2, which is an intake defect rather than a score leak.

**Identity gates.** Both pass all three runs after rounds 2 through 4. `SID-001` carries `sk-barter-copywriter` verbatim and a real written file every time. `PID-001` quotes `# Barter Copywriter - Custom Instructions - v1.10.11` verbatim, states Canvas Artifact delivery, renders the block, reports the export-equivalent path and claims no file. Round-1 had both gates failing, so this is recovered ground that held through three rounds of delivery-line edits.

## 4. Regression findings

Round 4 does not appear to suppress legitimate delivery. Blocks still render before replies, exports still save and read back, verdicts and HVR status still report, `[Assumes:]` still appears (now correctly placed), and the Quick intake skip still works.

Observed deviations, ranked by whether they touch round 4's surface:

- `SDP-004` run 1 ends on `write` with no read-back, where remeasure-3 had a read after every save. The new creator-fit check lives on that read, so this run could not have executed the check even though its content passed. Not scenario-graded, but it is a protocol regression against the export-first sequence the same diff strengthened.
- `PEN-001` run 2 burned a second intake round on a supplied task. Fast was not remeasured between round 1 and round 4, so this cannot be attributed to round 4, but it is a live one-question-contract breach.
- Mode-slot confusion on project paths is the same family as remeasure-3's `Path: $write` metadata, now shaped as filenames: `export/001 - $write-...`, `export/001 - quick-...`, `export/001 - fast-...`, `export/001 - $ux-...`. The diff's `[mode]` wording plausibly invites it (section 5).
- Two replies leak stray CJK tokens (`门槛` in `PEN-002` run 1, `门槛` and `角度` in `SEN-002` run 3). Voice-quality slips, not diff-caused.
- `PDP-004` run 1 narrates route, facts and defaults before the block (deliverable-first deviation) and embeds an `<!-- Assumes: -->` comment inside the block. Deal Templates check 21 bans a bracketed `[Assumes:]` tag; the HTML-comment form is unnamed there, unlike the Copywriter rule which explicitly sanctions it.

## 5. Diff audit findings

- **Twin fail-clause divergence (playbook defect, P2).** `SDL-001` fails on `the body leaks scoring, rationale or process matter` while `PDL-001` fails on `scoring or process matter` with no `rationale`, under identical expected signals that both ban `rationale`. The same body content now fails on skill and only partials on project, visible in this very batch (`SDL-001` run 1 versus `PDL-001` run 1).
- **The `[mode]` filename slot is misreadable (playbook defect, P1).** The kernel's new Delivery line says `export/[###] - [mode]-[description].md, with the mode and a short description filled in`, while the same diff teaches `the mode is written as its $ token, such as Mode: $write`. A runtime that fills `[mode]` with the token form produces exactly what was observed: `export/001 - $write-...` (`PDL-001` run 2), `export/001 - $ux-...` (`PEN-001` run 3), and the energy-token variants `quick-` and `fast-` (`PEN-002` run 2, `PEN-001` run 1). The fix is one clause: the mode name without its `$`, with a concrete `export/001 - write-...` example in the kernel and `SKILL.md`.
- **Check 7 over-reads the bullet test relative to the system's own example (rule gap, P2).** The scenario requires every bullet to pass checks 2 and 3, which read literally demands a standing name in every bullet. The cited compliance example, `deal-example-miniso.md`, ships `You film everyday fun` and `You collect blind boxes and plushies`, which carry none. Both final reviews and this review grade under the lenient reading (a bullet fails only by inventing a name). The contract and the example disagree and one of them should move.
- **Fast option count conflicts with the compact variant (playbook defect, P2).** `SEN-001` and `PEN-001` demand `at most two options` while the artifact template's compact variant is a best pick plus up to two alternatives, three lines. `PEN-001` run 1 shipped exactly the sanctioned compact shape and missed the scenario's own number.
- **Deal Templates diff is clean on copies and repoints.** The five-shape sentence and the `If you're into skincare.` versus `For anyone who's into skincare.` contrast are identical in `AGENTS.md` and the kernel, the `v0.119` to `v0.120` rename is repointed consistently across the knowledge directory, ten playbook files, `SYNC.md` and `carrier_query_evidence.py`, and the diff collapses a pre-existing duplicated Standards row in `conflicting-type-clarification.md`. One placement nit (P2): in `AGENTS.md` the five-shape sentence sits at the tail of Section 5 (ESCALATION) inside the category-knowledge paragraph, so the step-2 and step-4 reference `the five shapes in Section 5` resolves but the shapes live under an escalation heading.
- **Contradictions:** none found between source and mirror. The `[Assumes:]` rules agree per packaging (`after the path` on skill, `after the block` on project), and the failed-floor and spent-attempt exceptions are stated identically in all three places.

Adversarial self-check on the P1 findings:

| Finding | Hunter severity | Skeptic challenge | Referee verdict | Final |
|---|---|---|---|---|
| Path contract still unreliable | P1 | Run 2's `$write-` path is close enough to count | The pass bullet names the shape literally and run 3 omits it; 2 of 3 miss | Confirmed, P1 model limit |
| `[mode]` wording invites wrong token | P1 | The model would have used `$` anyway, blame the model | The wording is the fixable surface and four malformed paths correlate with the ambiguous slot | Confirmed, P1 playbook defect |
| Rationale prose in bodies | P1 | The Recommended Combination's own justification is the element's payload | `SDL-001` run 1's per-option glosses are outside any sanctioned element and fire the clause plainly; the RC cases are documented borderline | Confirmed P1 model limit for run 1; boundary question downgraded to the P2 ambiguity above |

## 6. Final recommendation

**Not ready as-is.** Only Deal Templates and Copywriter carry round-4 changes and remeasure-4 evidence, so this verdict covers the two systems exercised here. Deal Templates is close: 6 of 6 with both named failure modes gone and the check now written into both prompts, though the margin is three runs against a previous 1-of-3 failure rate and one run never executed the read-back the check lives on. Copywriter is not done: the export-equivalent path contract that item 2 exists to fix still fails in 2 of 3 `PDL-001` runs, and `SDL-001` fails its own new body-purity clause in at least 1 of 3.

Remaining issues:

| # | Priority | Classification | Issue and evidence | Remaining action |
|---|---|---|---|---|
| 1 | P1 | model limit | `PDL-001` export-equivalent path unreliable: correct 1/3, malformed 1/3, absent 1/3 | Apply fix 2, remeasure three runs; if the path still misses in 2 of 3, record as accepted model limit |
| 2 | P1 | playbook defect | `[mode]` slot admits `$` and energy tokens; four malformed paths observed | State `the mode name without its $, for example export/001 - write-new-creator-tagline.md` in the kernel Delivery line and `SKILL.md` |
| 3 | P1 | model limit | Rationale prose in artifact bodies: `SDL-001` run 1 per-option glosses, plus RC-internal notes in `SDL-001` run 3 and `PDL-001` run 1 | Rule is written and partially binding; fix 4 then remeasure to see the true rate |
| 4 | P2 | playbook defect | Twin fail clauses diverge on `rationale` | Add `rationale` to `PDL-001`'s fail list, or declare that a Recommended Combination may carry its own justification |
| 5 | P2 | rule gap | Check 7's literal reading conflicts with the MINISO worked example's nameless bullets | Reconcile the contract with the example, either by writing `no made-up name` into check 7 or by fixing the example |
| 6 | P2 | playbook defect | `at most two options` conflicts with the compact variant's three-line shape | Align the number or name the compact shape in `SEN-001`/`PEN-001` |
| 7 | P2 | model limit | One Fast reply prints `20/25`; one Quick reply's export is a full grid; `PEN-001` run 2 asked a second question | No new rule needed; the rules are written and the residual is binding rate |
| 8 | P2 | model limit | `SDP-004` run 1 skipped the export read-back the new check rides on | Note for the next remeasure; the protocol text is already in place |
| 9 | P2 | placement gap | `PDP-004` run 1's `<!-- Assumes: -->` comment inside the block is unnamed in Deal Templates' check 21, where Copywriter explicitly sanctions the comment form | Decide whether deal artifacts permit HTML-comment assumptions and write the answer into `standards.md` |

The single structural takeaway: the rules now say the right things almost everywhere, and the remaining failures are binding rate on GLM 5.3 Flash rather than missing rules, with two cheap documentation fixes (the `[mode]` slot and the twin-clause divergence) worth landing before the next remeasurement.
