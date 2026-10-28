# Rerun on v1.0.14.0, Claude Sonnet 5.5 high (sonnet-high-048)

One grader scored all four runs on one scale from the transcripts, the tool streams, every render at 100% and in greyscale and two fresh readers per scored board. FJ-017 carries no scorecard and had no readers, so its gate, its Sides lines and where each sticky landed were checked against the scenario's signals and PASS line on the page render.

| Scenario | v1.0.13.0 verdict | v1.0.13.0 total | v1.0.14.0 verdict | v1.0.14.0 total |
|---|---|---|---|---|
| FJ-017 Notes land after the write | FAIL | no scorecard | PASS | no scorecard |
| FJ-022 User flow board quality | PASS | 21 | FAIL | 20 |
| FJ-023 Process board quality | FAIL | 21 | FAIL | 21 |
| FJ-036 Dense flow at budget | FAIL | 22 | PASS | 21 |

**Pass count: 2 of 4. Fail count: 2. Not run: 0.** Phase 048's SC-003 asks for at least 3, so it is not met.

Nothing was written before a gate's yes in any run. Every intake round ends on its closing question, every playback names the detail level, the audience and the distance by their words and every gate shows the checked model line for line with the check's `PASSED` line. No stop carries an `HVR self-scan:` line. Fidelity, Signal, Clarity and all four Hygiene checks are full on every scored board. No scored board loses a point to a crossing, a shared trunk or a label collision. A first launch of all four scenarios stopped at turn 1 on the account's usage limit. Those runs are incomplete runs kept outside the record. The four graded here are their reruns.

Every evidence path in `sonnet-high-048.jsonl` points into the run folder: `renders/sonnet-high-048-<ID>-1-3.png` for the full-size renders, `grades/sonnet-high-048/grey/` for the greyscale copies and `grades/sonnet-high-048/readers/` for the reader notes.

## What the skeptics changed

- **FJ-036, Shared trunks 2 to 1, total 21 to 20, verdict PASS kept.** The Yes edge from Room free on those dates? and the Pick a room edge from Other rooms both run on board x 1728 into the left of the price decision and end 24 board units apart, under the 56 px gap playbook Section 3 and style-guide Section 7 require. At 100% they read as one stem with two arrowheads, reader b found the two entries hard to tell apart and the run's own turn 5 Finding names the fault. The cause is the composer, which owns the routing. The record gains a Shared trunks loss. Its reason, its crossing signal cite and its scorecard signal cite now say 20 of 22 with Shared trunks at 1. No dimension falls to 0, so the board still passes.

The pass count, the fail count and every other verdict and total stand as graded.

## What the completeness check changed

A completeness critic on Claude Sonnet 5.5 high opened every reader note and render behind the records, and each change below was confirmed against those files. No verdict changed.

- **FJ-022, Composition 2 to 1, total 21 to 20.** Both readers read Contact support last, reader a twelfth and reader b tenth, where the plan put it fifth. The record had said reader a read the planned order.
- **FJ-023, Composition 2 to 1, total 22 to 21.** Both readers read Damage reported before the decision the plan put second: reader a went accent, entry, decision and reader b went entry, decision, accent. The record had said reader b read the planned order, so D1 is not shown working.
- **FJ-036, Shared trunks 1 back to 2, total 20 to 21.** The two runs into the price decision only arrive, and style-guide Section 2 lets edges arriving at a choice meet on one side. FJ-023 kept its 2 for the same kind of pair, so one rule now scores both.
- **FJ-022 gains a skill gap** for the sentence that announces the delivery reply above the URL, a slip seen in six earlier runs.

## Remaining failures

**FJ-022, Reply 1 and Composition 1.** The run is clean through the gate: turn 1 is the intake round with no model and no check before the playback's answer and the playback names the dials. The delivery reply opens on 'The board is written and read back, so I'm sending the delivery reply now.' above the URL in the same final text block. `references/flow-mode.md` Section 8 says nothing comes before the URL, so Reply scores 1. The slip recurs across six earlier runs, so the rule needs to name it. Both readers also read the Contact support exit last, after the main row, where the Glance line placed it at its column, so Composition scores 1. The total is 20.

**FJ-023, Composition 1 and two expected signals.** The board scores 21 of 22, because both readers read the entry Damage reported before the decision the Glance line put right after the accent. Turn 1 is the playback while its Assumed list names the reader ('a mixed team of CS and warehouse leads'), so the sources leave the reader unsettled and playbook Section 5's turn 1 intake rule makes the skipped round a missed playback signal. The model also drew the warehouse queue as a store of its own, so the board reads back 9 of 9 nodes and 9 of 9 connectors where the scenario expects 8 and 8. `references/types/process.md` lists a queue as a store and the runbook names the queue, so the count miss is partly a playbook gap. The scenario file still says Turn 1 ends on the playback with no reader rule, which invites the first miss.

## v1.0.14.0 fixes, as the rerun shows them

- **D1, the accent's row neighbour:** not shown working on FJ-023. The Glance line prints Approve the claim, then Damage clear in the photo?, then Damage reported, but reader a reads the accent, the entry and then the decision and reader b reads the entry, the decision and then the accent, so neither takes the decision right after the accent and the entry costs a Composition point. On FJ-036 Other rooms stands between Room free on those dates? and the price decision, the plain order holds and both readers keep it. FJ-022 does not exercise it.
- **D2, the closing question:** working. FJ-022's round one and FJ-036's rounds one and two end on 'Take the recommended answers, or correct any of them?'. FJ-017 and FJ-023 opened no round.
- **D3, the Finding on a moved sticky:** working on FJ-017. Both stickies landed on the sides their Sides lines named, so the reply owed no Finding and gave none. The scenario passes.
- **D4, the diamond label trace:** partly working. FJ-022's diamonds wrap evenly with no Label line. FJ-036's check flagged both price outcomes and the rewordings clear on the board, but it passed 'New price compared to old?', 26 characters on a 336 px diamond, while FigJam leaves 'old?' alone on the last line of that accented diamond. FJ-036 loses one Legibility point and still passes on 21 of 22.
- **D5, the dials at the playback:** working on all four playbacks.
- **D6, the Composition levels:** applied on FJ-022 and FJ-023, where both readers read one part out of its planned place, so each scores 1.
- **D7, the turn 1 intake:** working on FJ-022 and FJ-036, whose tool streams show no model and no check before the playback's answer. FJ-023 skipped the round with the reader unsettled and misses the playback signal. FJ-017 named its reader in the request and assumed two rows, so the rule does not call for a round.
- **D8, the release:** not graded by this rerun.

## Skill gaps the rerun still shows, most important first

1. `sk-create-figjam/scripts/figjam_checks/board_geometry.py` `reading_order` with `references/quality-rubric.md` Section 3: the lifted decision and the column order put an exit or an entry where neither FJ-022's nor FJ-023's readers met it. Both readers took FJ-022's main row before its Contact support exit and FJ-023's lane entry before its lifted decision, so the plan the Glance line prints costs Composition on both boards.
2. `references/flow-mode.md` Section 8 first bullet and `SKILL.md`: nothing may come before the board URL, yet no rule names the sentence that announces the reply, and the slip recurs in sonnet-high-041 FJ-032, sonnet-high-042 FJ-036 and FJ-031, sonnet-high-044 FJ-026, sonnet-high-045 FJ-036, sonnet-high-rerun FJ-036 and FJ-022 here.
3. `sk-create-figjam/manual-testing-playbook/board-quality/process-board-quality.md` against playbook Section 5 and the draw-ready threshold in `references/flow-mode.md` Section 2: the FJ-023 scenario still says Turn 1 ends on the playback and states no reader rule, while FJ-022 spells out the same rule for the same unstated reader. FJ-023 fails on the skipped round.
4. `sk-create-figjam/manual-testing-playbook/board-quality/process-board-quality.md` against `references/types/process.md`: the scenario fixes the board at 8 of 8 nodes while the runbook names the warehouse queue and the type reference draws a queue as a store, so a source-faithful model misses the count. FJ-023 fails on this too.
5. `sk-create-figjam/scripts/figjam_checks/board_geometry.py` and `scripts/compose-trace.mjs` with `references/flow-mode.md` Section 2 step 5: the D4 trace passed 'New price compared to old?' on an accented 336 px diamond that FigJam wraps with 'old?' alone. The unaccented and the FJ-022 accented diamonds wrap evenly, so the accent outline may narrow the text box, an inference a trace of an accented diamond would confirm. FJ-036 loses one Legibility point on this and still passes.
