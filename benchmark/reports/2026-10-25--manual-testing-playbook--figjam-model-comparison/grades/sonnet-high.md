# Sonnet high grades, full playbook run after phase 039

These are the grades for all 54 scenario runs Claude Sonnet 5.5 made at high effort on `sk-create-figjam` v1.0.5.0. One grader scored every run, so every total sits on one scale. Skeptics then challenged 37 of the grades and an adjudicator ruled on each dispute. Every ruling is folded into `sonnet-high.jsonl`, where each adjudicated row carries an `adjudication` note that names what changed. That file holds the per-run detail with every signal, cite, loss, location and fix. The tables below are computed from it.

## How the grades were set

- **Signals.** Each run starts from the independent checker's reading in `sonnet-high/checks/<ID>.json`. Where the grade or an adjudication overturns it, the signal's cite says so. An adjudicated cite starts with `Adjudicated:`.
- **Turn shifts.** An intake round that pushes the playback, gate or write one turn later is accepted, as the Flow scenarios' commands allow. A stop that lands in the wrong place is not.
- **Contract against scenario.** Where the skill tells the model to do one thing and the scenario expects another, the signal still counts as missing and the run fails. The conflict is recorded as a skill gap below, so a reader can tell a model slip from a contract that cannot be met.
- **Harness.** Signals that need an operator step the driver never ran are marked harness. FJ-018 and FJ-035 test the `fj` route, which the driver never set up, so both are SKIP and each written board is still scored. FJ-044 and FJ-045 were graded SKIP at first, but the hosted Figma server was connected, so the SKIP condition did not hold and both are FAIL. A read-only command that a grader or skeptic ran, such as the hub check, counts on its own output where an adjudication says so.
- **Clarity.** Fresh readers answered from the colour renders, which sit in the run folder's `renders/` as `sonnet-high-<ID>-<node>.png`. Their notes are in `sonnet-high/readers/`. Clarity is scored from their answers against each scenario's three questions.
- **Composer losses.** Every Crossings, Shared trunks, Label collisions and Legibility loss names its cause. All of them are the composer's except the FJ-017 Legibility point, where the model chose the note text and the sticky size.

## All 54 runs

First grade shows the grader's verdict and total before adjudication where an adjudication changed either.

| ID | Verdict | Total | First grade |
|---|---|---|---|
| FJ-001 | PASS | no board |  |
| FJ-002 | FAIL | no board |  |
| FJ-003 | PASS | no board |  |
| FJ-004 | PASS | no board |  |
| FJ-005 | FAIL | no board | PASS, no board |
| FJ-006 | PASS | no board |  |
| FJ-007 | PASS | no board |  |
| FJ-008 | PASS | 22 |  |
| FJ-009 | FAIL | no board |  |
| FJ-010 | PASS | no board |  |
| FJ-011 | FAIL | no board |  |
| FJ-012 | FAIL | no board |  |
| FJ-013 | PASS | no board |  |
| FJ-014 | PASS | no board |  |
| FJ-015 | PASS | no board |  |
| FJ-016 | PASS | no board |  |
| FJ-017 | FAIL | 20 | PASS, 22 |
| FJ-018 | SKIP | 20 | SKIP, 22 |
| FJ-019 | FAIL | 22 |  |
| FJ-020 | FAIL | no board |  |
| FJ-021 | PASS | no board |  |
| FJ-022 | PASS | 22 |  |
| FJ-023 | PASS | 21 |  |
| FJ-024 | FAIL | 20 |  |
| FJ-025 | FAIL | 21 |  |
| FJ-026 | FAIL | 19 | FAIL, 21 |
| FJ-027 | FAIL | 20 | PASS, 22 |
| FJ-028 | PASS | 21 |  |
| FJ-029 | FAIL | 22 |  |
| FJ-030 | PASS | 22 |  |
| FJ-031 | FAIL | 20 | PASS, 22 |
| FJ-032 | FAIL | 18 | PASS, 22 |
| FJ-033 | FAIL | 20 | FAIL, 22 |
| FJ-034 | FAIL | 22 |  |
| FJ-035 | SKIP | 19 | SKIP, 22 |
| FJ-036 | FAIL | 20 | PASS, 21 |
| FJ-037 | FAIL | no board | PASS, no board |
| FJ-038 | FAIL | no board |  |
| FJ-039 | FAIL | no board |  |
| FJ-040 | FAIL | no board |  |
| FJ-041 | FAIL | no board |  |
| FJ-042 | FAIL | no board |  |
| FJ-043 | FAIL | no board | PASS, no board |
| FJ-044 | FAIL | no board | SKIP, no board |
| FJ-045 | FAIL | 20 | SKIP, 22 |
| FJH-001 | PASS | no board |  |
| FJN-001 | PASS | no board |  |
| FJR-001 | FAIL | no board | PASS, no board |
| FJR-002 | PASS | no board |  |
| FJR-003 | PASS | no board |  |
| FJR-004 | PASS | no board |  |
| FJR-005 | FAIL | no board | PASS, no board |
| FJR-006 | PASS | no board |  |
| FJR-007 | PASS | no board |  |

Totals: 23 PASS, 29 FAIL and 2 SKIP. The grader's first pass gave 33 PASS, 17 FAIL and 4 SKIP. Nothing was written to a board before a gate's yes in any run. No run saved a file to `export/` outside the Product Owner artifact lanes (FJ-020, FJ-021, FJ-037 and FJN-001), but FJ-020 saved a Task in turn 2 beyond the one clarification its scenario allows.

The 20 written boards score 411 of 440 points, from 18 to 22: six at 22, three at 21, eight at 20, two at 19 and one at 18. Nine pass the board scorecard, which needs 18 or more with Composition, Fidelity, Reply and the four Hygiene checks at full marks and no dimension at 0: FJ-008, FJ-019, FJ-022, FJ-023, FJ-025, FJ-028, FJ-029, FJ-030 and FJ-034. Before adjudication eighteen boards passed it, where this file first said sixteen. Six of the eleven that now fail it drop to Signal 0 in greyscale (FJ-018, FJ-026, FJ-032, FJ-033, FJ-035 and FJ-045). Three lose a Composition point (FJ-017, FJ-031 and FJ-036) and two score Reply 0 (FJ-024 and FJ-027). FJ-019, FJ-025, FJ-029 and FJ-034 pass the scorecard and still fail on a missing expected signal.

## Pass count by category

| Category | Pass | Fail | Skip | First grade (pass, fail, skip) |
|---|---|---|---|---|
| Type choice (7) | 4 | 3 | 0 | 4, 3, 0 |
| Pre-write check (7) | 5 | 2 | 0 | 7, 0, 0 |
| Board write (6) | 2 | 3 | 1 | 3, 2, 1 |
| Board quality (9) | 3 | 6 | 0 | 4, 3, 2 |
| Board creation (8) | 1 | 6 | 1 | 4, 3, 1 |
| Boundaries (8) | 1 | 7 | 0 | 2, 6, 0 |
| Intra-routing recall (9) | 7 | 2 | 0 | 9, 0, 0 |


## What the skeptics changed

Skeptics disputed 37 grades and an adjudicator ruled on every item. No ruling was rejected when the rulings were folded in.

- **Twelve verdicts moved.** Ten went from PASS to FAIL (FJ-005, FJ-017, FJ-027, FJ-031, FJ-032, FJ-036, FJ-037, FJ-043, FJR-001 and FJR-005) and two from SKIP to FAIL (FJ-044 and FJ-045).
- **Ten board totals fell, from 433 to 411 points.** FJ-017, FJ-018, FJ-027, FJ-031, FJ-033 and FJ-045 went from 22 to 20, FJ-026 from 21 to 19, FJ-032 from 22 to 18, FJ-035 from 22 to 19 and FJ-036 from 21 to 20.
- **Signal in greyscale.** The shipped role palette renders start, goal, exit, first state, final state, gateway and outside system as near identical light greys, so six boards drop to Signal 0. The grader had scored all six at 2.
- **Glance order.** FJ-017, FJ-031, FJ-032 and FJ-036 lose a Composition point where the fresh reader's first glance landed before the planned focus. FJ-031 also loses a Signal point because its one accent sits on Return confirmed with QR code and not on the revision's subject, Request an exception.
- **Signals marked harness that the run could show.** FJ-005 planted a readable id where Command 1 plants a short id, so the short id failure never printed. FJR-001 and FJR-005 fail on the stale `-> <type>` grep in step 2, a playbook defect and not a model one. FJ-043 never ran the passing check on the shipped example, which is a model omission.
- **Other missing signals.** FJ-027 scores Reply 0 because its self-scan reports 0 hard blockers while it keeps a structural ban. FJ-037's first reply is a Story Mode clarification instead of the Story. FJ-044 piped the design check through `head`, so its exit status was never shown. FJ-011, FJ-012, FJ-020, FJ-029 and FJ-040 each lose one or two signals with no change to their FAIL.
- **Harness readings both ways.** The FJR-001 hub, leaf and topology commands and the FJR-007 hub check were rerun read-only and now read met. The FJR-003, FJR-004 and FJR-006 commands and two FJH-001 signals moved to harness or missing as their adjudications ruled.
- **Upheld.** FJ-022, FJ-030 and FJ-034 stand as graded. FJ-019, FJ-023, FJ-024, FJ-025, FJ-028, FJ-039, FJN-001 and the rest of the adjudicated rows keep their verdict and total with corrected cites, losses or skill gaps.
- **One ruling is contested.** A later review of `hvr-core.md` holds that the FJ-027 Reply 0 rests on a misread: the file never says whether a term under Kept with reason counts in N, and FJ-008 counted the same kept verb as 1. FJ-027 stays at Reply 0 in this record until that rule is written and the run is scored again.

## Against Claude Opus 5.5 medium on its 24 scenarios

The opus-medium runs used an earlier driver that sent up to three `Yes, go ahead.` turns after any stop with no board, so it drew boards in 17 of its 24 runs, most of them in scenarios that expect none (FJ-001, FJ-002, FJ-004, FJ-005, FJ-007, FJ-010 to FJ-015 and FJR-002 to FJR-005). That reflects the driver, not the model, so this compares where each model stopped on the scenario's own turns. On these 24 Sonnet drew one board (FJ-008) and got no supplementary turn except the three FJ-009 turns the brief discounts.

- **Same stop.** Both stop on the gate in FJ-001, FJ-007, FJ-010, FJ-011 and FJ-012. Both stop on the playback in FJ-002 and FJ-013. Both report a refused check in FJ-004, FJ-005 and FJ-015, though Sonnet's FJ-005 now fails because it planted two of the three defects. Both reach intake in FJR-001 and both stop on a missing source in FJR-006 and FJR-007. Both write the FJ-008 board.
- **Opus further on.** Opus reached the playback where Sonnet held at intake for a source in FJR-002 and FJR-003. In FJH-001 it was the other way round: Sonnet reached the playback and Opus stayed at intake.
- **Exports.** Opus saved Doc or Task files in FJ-003 (1) and FJ-006 (2), which both ask only for a refusal or a check. Sonnet saved nothing there and kept exports to FJN-001, where a Task is the right output.
- **FJ-009.** Opus had a live Figma connection and wrote a gantt board on the scripted yes, so its run did not meet the scenario's no-route precondition. Sonnet ran without Figma and named the missing route.
- **FJ-014.** Opus turned a budget check into a gate and two boards on the driver's yes. Sonnet reported the failing check and stopped.

## FJ-022 to FJ-028 against the five graded models

Ranked by total, then pass over fail, then fewer supplementary turns. The deepseek, glm and swe rows come from `FJ-02N.jsonl` and the luna and opus-low rows from `luna-opus-low.jsonl`. Those grades came from other graders who had no skeptic round, so treat a one-point gap with care.

- **FJ-022 user flow.** glm 22 PASS, deepseek 22 PASS, sonnet-high 22 PASS, luna 22 PASS (one supplementary turn), swe 20 FAIL, opus-low 20 FAIL. Sonnet opened an intake round but needed no supplementary turn.
- **FJ-023 process.** sonnet-high 21 PASS, deepseek 20 PASS, swe 20 FAIL, opus-low 20 FAIL, glm 17 FAIL, luna 16 FAIL. Sonnet's one loss is a composer trunk into Damage clear?.
- **FJ-024 architecture.** swe 22 PASS, deepseek 22 PASS, luna 22 FAIL, opus-low 21 PASS, glm 21 FAIL, sonnet-high 20 FAIL. Sonnet's board is clean and names file storage under Left out, but a Finding claims four dashed edges where three are drawn.
- **FJ-025 sequence.** glm 22 PASS, swe 22 PASS, deepseek 22 PASS, sonnet-high 21 FAIL, luna 21 FAIL, opus-low 20 FAIL. Like swe, luna and opus-low, Sonnet drew the declined card as a second board. It also drew the hub message as a plain request, so the async signal is missing.
- **FJ-026 state.** glm 22 PASS, luna 20 FAIL, swe 19 FAIL, sonnet-high 19 FAIL, opus-low 18 FAIL, deepseek 16 FAIL. Sonnet drew the Confirmed composite correctly but loses Signal in greyscale and stopped on an unasked question about an older same-named board, so the write came on a supplementary turn and it sits behind swe.
- **FJ-027 ER.** swe 22 PASS, glm 22 PASS, luna 22 PASS, then sonnet-high, opus-low and deepseek tied at 20 FAIL. Sonnet's board is complete, but its Reply scores 0 for the self-scan count.
- **FJ-028 gantt.** deepseek 22 PASS, glm 22 PASS, swe 22 PASS, sonnet-high 21 PASS, opus-low 20 FAIL, luna 19 FAIL. Sonnet's one loss is the composer dropping the design arrow onto the end of the Sync engine bar.

Across the seven, Sonnet passes three (FJ-022, FJ-023 and FJ-028). On the same grade files deepseek and glm pass five, swe four, luna two and opus-low one. Sonnet's 21 is the top FJ-023 score.

## Skill gaps, most important first

1. **The role palette fails in greyscale.** `assets/figjam-design.md` gives start, goal, exit, first state, final state, gateway and outside system fills whose lightness sits within a few steps of each other, so the kinds vanish in a greyscale copy. Six boards score Signal 0 for it (FJ-018, FJ-026, FJ-032, FJ-033, FJ-035 and FJ-045). No model change fixes it.
2. **Neighbouring zones share a tint.** On FJ-022, FJ-030, FJ-031 and FJ-045 the Request the return and Done zones are both teal, and on FJ-019 board 2 Entry and Services are both light orange. The zone cycle in `assets/compose-board.js` breaks the rule in `assets/figjam-design.md` and the root playbook that a zone skips the tint before it.
3. **One question against one round.** `SKILL.md` Section 4 rule 2 and `references/flow-mode.md` Section 2 let the type question ride in a three-question intake round. FJ-002 and FJ-041 fail a reply with more than one question. Two FAILs come straight from this.
4. **Split against cut on architecture.** `references/types/architecture.md` Section 4 says split rather than shrink. FJ-012 and FJ-019 expect file storage cut and one six-lane board. Two more FAILs.
5. **Composite state exits.** The composer draws the missed check-in exit from the Confirmed section as a broken leg with its label pressed against Completed (FJ-017, FJ-026 and FJ-032). Three readers misread it.
6. **Two edges on one magnet.** The composer merges two incoming edges on one segment or anchor in FJ-023, FJ-028 and FJ-036. These are the only geometry points the run lost.
7. **Read-back line with no route.** `references/flow-mode.md` Section 8 prescribes `Read-back: not possible` without excluding the case where no board was written, and FJ-009 fails on it.
8. **Fixed scratch pointers in /tmp.** Runs kept fixed pointer files such as `/tmp/loomlist-scratch-path`. Under eight lanes two runs shared one, and FJ-019 deleted the pointer FJ-029 relied on. `references/flow-mode.md` Section 8 should require a pointer-free mktemp folder.
9. **No pre-write read on a file with content.** FJ-027 and FJ-034 wrote beside existing boards with no read before the write, so the comparison `references/flow-mode.md` Section 7 asks for could not run. The gate template leaves that read optional.
10. **Quick energy against the draw-ready stop.** FJ-042 applied the stop rule under `$quick` and never modelled. `references/flow-mode.md` Sections 1 and 2 do not say which wins.
11. **Playbook commands and scenario drift.** The FJR routing scenarios grep for a `-> <type>` line that `SKILL.md` no longer holds, which fails FJR-001 and FJR-005. The FJ-005 prompt asks for two planted defects while Command 1 and its Expected block need three. FJ-011 expects a lane style the process reference makes optional. FJ-020 meets a clarification template that adds a board block. FJ-037 expects the Story before Story Mode's own context question.
12. **Smaller points.** The gantt key lists Critical while the only critical bar is drawn in focus, and its arrows land mid-bar (FJ-028). The pin recipe has no rule for a diamond (FJ-030). FJ-008 counted the kept verb `offers` as 1 on the self-scan line and FJ-027 counted it as 0. `hvr-core.md` agrees with itself on structural bans, but it never says whether a term kept with reason counts in N, and lines 29 and 120 call the always-cut edits structural removals, one word away from structural bans.
