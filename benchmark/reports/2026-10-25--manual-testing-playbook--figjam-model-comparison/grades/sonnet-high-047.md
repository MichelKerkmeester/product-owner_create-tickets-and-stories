# Rerun on v1.0.13.0, Claude Sonnet 5.5 high (sonnet-high-047)

One grader scored all four runs on one scale from the transcripts, the tool streams, every render at 100% and in greyscale and two fresh readers per scored board. FJ-017 carries no scorecard and had no readers, so its gate, its Sides lines and where each sticky landed were checked against the scenario's signals and PASS line on the page render.

| Scenario | v1.0.12.0 verdict | v1.0.12.0 total | v1.0.13.0 verdict | v1.0.13.0 total |
|---|---|---|---|---|
| FJ-017 Notes land after the write | FAIL | no scorecard | FAIL | no scorecard |
| FJ-022 User flow board quality | FAIL | 20 | PASS | 21 |
| FJ-023 Process board quality | FAIL | 19 | FAIL | 21 |
| FJ-036 Dense flow at budget | FAIL | 19 | FAIL | 22 |

**Pass count: 1 of 4. Fail count: 3. Not run: 0.** Phase 047's SC-003 asked for at least 3, so it is not met. The counts and totals above include the skeptic rulings listed at the end.

Nothing was written before a gate's yes in any run. Every playback and gate ends on its stop and so does every intake round but FJ-036's, which ends on a Why line after its last question. No stop carries an `HVR self-scan:` line. All four gates show the checked model line for line with every `%%` and `style` line and the check's `PASSED` line as printed. Fidelity, Signal, Clarity, Reply and all four Hygiene checks are full on every scored board, and no scored board loses a point to a crossing, a trunk or a label collision. FJ-022 loses one Legibility point to a stranded word.

Every evidence path in `sonnet-high-047.jsonl` points into the run folder: `renders/sonnet-high-047-<ID>-1-3.png` for the full-size renders, `grades/sonnet-high-047/grey/` for the greyscale copies and `grades/sonnet-high-047/readers/` for the reader notes.

## Remaining failures

**FJ-017, a skill gap the scenario exposes.** Every v1.0.13.0 fix the scenario touches works. The check printed `Sides: Cancelled takes its sticky below, left aligned` and `Sides: No-show takes its sticky left, centred`, the gate named both and the notes call put each sticky 64 px from its node on that side and in that alignment, inside the board, with the composed board unchanged at 2208 by 1912. The one miss is the reply: the scenario expects a `Finding:` line naming any sticky that sits below or left of its node, and both do, but the reply names neither. `references/hybrid-workflow.md` Section 3 asks for that Finding only when a sticky is pushed off its first side by a sticky already placed or when its named side is taken at the write. Here the check chose below and left itself, so the model followed the skill and missed the scenario's wider signal.

**FJ-036, the playback signal.** The board scores 22 of 22 and nothing was written before the gate's yes. Intake round one, a round the scenario's expected signals do not name, ends on 'Why: nothing you sent states those steps, and drawing them would mean inventing them' after its last question. Playbook Section 5 says text after an extra intake round's question misses the playback signal, so the signal is missing and the scenario's FAIL line applies. `assets/flow-templates.md` Section 5 does not say where the Why line goes on a round's last block, which is the skill gap behind it.

**FJ-023, Composition 1, a skill gap in the glance order.** The plan copies the check's `Glance:` line exactly: Approve the claim, then Damage reported, Damage clear in the photo?, Send the second photo, Claims table, Book a courier, Inspect the item and Refund released. Both readers read Approve the claim, Damage clear in the photo?, Damage reported and then the rest in plan order. The decision sits directly left of the accent in the CS agent lane, and the entry sits in the first column of the Customer lane above it. Both readers named the decision in a step of its own, so the set reading does not apply, and the entry clause frees only the entry against the goal. One part read early costs one point, so the board totals 21 of 22 and misses the full Composition a pass needs. No model change moves it, because the accent must sit on Approve the claim and the composer sets the columns.

## v1.0.13.0 fixes, as the rerun shows them

- **D1, the glance follows the drawing:** working on FJ-022 and FJ-036, where both readers keep the Glance order and Contact support now draws below the row. On FJ-023 both readers go from the accent to its lane neighbour before the entry.
- **D2, the row advisory:** FJ-036's check printed a `Row:` line for the bend from See other rooms to New price?. The gate named it and kept it, and the reply repeats it on a Finding line. FJ-022 and FJ-023 printed none.
- **D3, sticky reach and alignment:** working. FJ-017's Sides lines name the alignment, no square past one sticky width was offered and the notes call placed both stickies exactly there, 64 px from their nodes against 328 px last time.
- **D4, the verbatim gate sketch:** working on all four gates, against one of four last time.
- **D5, label measures:** partly working. FJ-022's turn 1 printed a `leaves` line for Drop-off point or courier pickup? and then a `may leave` line for Drop-off or courier pickup?. Its turn 2 printed a `leaves` line for Drop-off or pickup? and a `leaves` line for the trial Where is it returned?. The final label Drop-off point or courier? printed none, yet the composed diamond leaves 'courier?' alone on its last line, so the check's wrap model does not match the composer's diamond width. FJ-036's first check printed one `leaves` line for New price vs current? and two `may leave` lines for Pay the difference and Get the difference as credit, and its rewordings cleared all three on the board. FJ-017 and FJ-023 printed no `Label:` line.
- **D6, parts named together read as a set:** used on FJ-036, where reader a names Pick new dates with Room free on those dates? and both readers name Credit difference with Pay difference in one step.
- **D7, the dials in intake round one:** working on FJ-017, FJ-023 and FJ-036. FJ-022 opened no intake round and named the three dials as assumed in its playback.
- **D8, an extra intake round ends on its question:** FJ-017 and FJ-023 close round one on a question. FJ-036 closes it on the last question's Why line and misses the playback signal under playbook Section 5.
- **D9, the harness:** not graded by this rerun.

## Skill gaps the rerun still shows, most important first

1. `sk-create-figjam/scripts/flow_check.py` Glance line with `sk-create-figjam/references/quality-rubric.md` Section 3 and the playbook Composition row: on a laned process the line orders the nodes column by column after the accent, while readers step from the accent to its neighbour in the same lane before going back to the entry. FJ-023 fails on this alone.
2. `sk-create-figjam/scripts/flow_check.py` label wrap measure, with the label rules in `references/quality-rubric.md` and `references/flow-mode.md`: the check passed Drop-off point or courier? at both widths, while the composed diamond wraps it narrower and strands 'courier?'. FJ-022 loses one Legibility point on this and still passes.
3. `sk-create-figjam/references/hybrid-workflow.md` Section 3 against `manual-testing-playbook/board-write/hybrid-extension-written.md`: the skill asks for a Finding line only for a sticky pushed off its first side, while the scenario asks for one on every sticky below or left of its node. FJ-017 fails on this alone.
4. `sk-create-figjam/references/flow-mode.md` Section 4 says the gate names all three dials by their words. FJ-017, FJ-022 and FJ-023 name only the reading distance at the gate and FJ-036 names none. Playbook Section 5's gate signal does not check the dials, so no grade counted it, the same reading the v1.0.12.0 grade applied.
5. `sk-create-figjam/assets/flow-templates.md` Section 5 shapes every intake question as Reading, Question, Recommended and Why, while `references/flow-mode.md` Section 8 and playbook Section 5 say a round ends on its question. The template does not say where the Why line goes on a round's last block, and FJ-036 fails on this alone.

## What the skeptics changed

- **FJ-022 Legibility:** 2 to 1. The method decision Drop-off point or courier? leaves 'courier?' alone on its last line in the full-size render. The loss names the composer as the cause.
- **FJ-022 total and verdict:** 22 to 21, verdict stays PASS. The reason no longer says the label clears the wrap.
- **FJ-022 scorecard signal cite:** now records Legibility 1 and a total of 21, met stays true.
- **FJ-022 skill gaps:** none to one, the D5 label wrap measure in `flow_check.py` against the composer's diamond width.
- **FJ-022 Label: lines:** the D5 entry now lists all four lines the run printed, two per turn, and says the final label printed none.
- **FJ-022 evidence paths:** now cite the work folder files that exist instead of run folder paths that do not.
- **FJ-036 playback signal:** met true to met false, since intake round one ends on a Why line after its question.
- **FJ-036 verdict:** PASS to FAIL, total stays 22. The reason, the loss and the D8 entry now record the missing signal.
