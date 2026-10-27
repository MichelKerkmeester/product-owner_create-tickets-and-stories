# Rerun on v1.0.11.0, Claude Sonnet 5.5 high (sonnet-high-045)

One grader scored all four runs on one scale from the transcripts, the tool streams, every render at 100% and in greyscale and two fresh readers per scored board. The full-size renders are in `renders/`, and the reader notes and greyscale renders in `grades/sonnet-high-045/`.

| Scenario | v1.0.10.0 verdict | v1.0.10.0 total | v1.0.11.0 verdict | v1.0.11.0 total |
|---|---|---|---|---|
| FJ-017 Notes land after the write | FAIL | no scorecard | FAIL | no scorecard |
| FJ-026 State board quality | FAIL | 19 | PASS | 22 |
| FJ-029 Split flow on one board | FAIL | 19 | PASS | 21 |
| FJ-036 Dense flow at budget | FAIL | 20 | FAIL | 20 |

**Pass count: 2 of 4.** Phase 045's SC-003 asked for at least three, so it is not met.

## What the skeptics changed

Two skeptic reviews were adjudicated. No verdict or total changed: FJ-017 stays FAIL with no scorecard and FJ-026 stays PASS at 22. The pass count stays 2 of 4.

- **FJ-017, the signal 'It moves no composed node and draws no colour':** met stays true. The cite no longer rests on the page render, which is a byte twin of the board render and shows only the board. It now rests on the turn 3 tool calls: one compose and one `use_figma` that only runs findAll and returns boxes.
- **FJ-017, the pass line:** met stays false. The cite drops the page render as evidence of the rest of the page and names the missing notes call instead.
- **FJ-017, the boxed-in signal:** met stays false. The cite now says the key takes Cancelled's right side whether the sticky is top aligned or centred and the guest cancels leg blocks only the centred placement. The 688 px figure is gone.
- **FJ-026, the Composition loss entry:** Composition stays 2. The entry no longer says No-show and Completed hold their planned order. Both readers read No-show first, the reverse of how the plan lists them, which costs nothing because the plan names them as one group of end states.
- **FJ-026, the signal 'Turn 2 ends on the gate and writes nothing':** met stays true. The cite adds a model slip: the gate shows no Mermaid sketch, answers none of the four critique questions and does not say the check passed. It costs no score.
- **FJ-026, the reason:** reworded to match the corrected reading order and to name the gate slip.

## Remaining failures

**FJ-017, skill gap and scenario gap.** The run took the after-compose branch exactly as `hybrid-workflow.md` Section 3 and phase 045's edge case describe it. Its second `use_figma` call only measured the board and wrote nothing. No notes call ran and the reply asks for `pins` or `recompose`. The scenario file asks for something else. At Turn 2, when every side of Cancelled or NoShow is taken, the gate must say so and offer pins with a legend or a recompose before any write. The two-call and `Extensions:` signals then apply only to the single-sticky option the operator picks. This run's gate planned two single stickies without checking a side, so the scenario's Turn 2 signal is missing. Its pass line still asks for a sticky beside each node and the reply has no `Extensions:` line. Cancelled really is boxed in. A 240 px sticky 64 px past its end dot would overlap the key whether it is top aligned or centred on the node. The guest cancels leg just above it blocks only the centred placement. A connector enters from the left and Completed sits 80 px above. The skill gives the gate no way to see that before the write.

**FJ-036, model slip with a skill gap behind it.** The detour fix works: See other rooms is planned on the main row and both readers read it in place. The model then put its one accent on the goal Updated booking, at the far right end of the row and planned it first. Both readers read Booking page, Pick new dates, Room free on those dates?, See other rooms, How does the price compare?, Get credit back and Pay difference before reaching it. Composition scores 0 and the board totals 20 of 22. The playback and the gate also each end on an `HVR self-scan:` line after their question, against Flow Mode's rule that a stop ends on its question.

## v1.0.11.0 fixes, as the rerun shows them

- **State boards planned as drawn (D1):** working. FJ-026 plans Pending, then Upcoming and In stay, then Cancelled leading the end states. Both readers read Pending, Upcoming and In stay in that order and Cancelled first among the end states, which the Composition row allows. Both read No-show before Completed, while the plan lists them the other way round as one group of end states, so no point is lost. The gate showed no Mermaid sketch, a model slip that costs no score.
- **Flow glance lines (D2):** working. Both FJ-029 boards plan the drawn main row in path order and board 2 reads exactly as planned for both readers. FJ-036's detour is read in place.
- **Boxed-in sticky (D3):** half working. FJ-017's after-compose branch wrote nothing and asked the question. The before-write branch never fired, because nothing tells the gate how to see a node's sides.
- **Intake (D4):** working. FJ-029 and FJ-036 each ran one intake round and the next reply was the playback.
- **Revision playback (D5):** not exercised.
- **Connector labels (D6):** every labelled count matched the composing write's return.
- **Grading conventions (D7):** applied. Two notes: the entry and the goal carried no order in FJ-029 and the FJ-036 arrivals about 24 px apart were not counted as a trunk.
- **Label trace:** ran on every run, with no `Label: skipped` line anywhere. FJ-017 and FJ-026 printed no `Label:` line. FJ-029's last check printed one, for Which method?. FJ-036's first check printed three and its last printed none.

## Harness notes

- The grader found the file keys and a plan key in plain text before redaction. `run/redact_run.py` now also redacts plan keys, and it ran over the whole run folder before the commit, which also cleared the plan keys older runs in this folder carried.

## Skill gaps the rerun still shows, most important first

1. `sk-create-figjam/references/hybrid-workflow.md` Section 3 requires the gate to say a noted node is boxed in before any write, but never says how to see the node's sides at that point. The check already composes the board in memory for its `Label:` lines, so the gate could read the sides from that trace.
2. `sk-create-figjam/manual-testing-playbook/board-write/hybrid-extension-written.md` accepts the boxed-in offer only from the Turn 2 gate. It names no signal for the after-compose branch, gives the operator no turn to pick and keeps a pass line that needs two stickies.
3. `sk-create-figjam/references/quality-rubric.md` Section 3 offers the goal as a first-glance accent on a user flow. The composer draws the goal at the end of the left-to-right row, so readers take it last.
4. `sk-create-figjam/scripts/flow_check.py`, through `compose-trace.mjs`, missed the lone `tip` that FigJam draws in FJ-029's Editor with welcome tip, so a clean label check does not prove that no label wraps alone.
5. `sk-create-figjam/references/flow-mode.md` (The gate is its own reply) and `AGENTS.md` step 8 never say whether the self-scan line may follow a stop's question. FJ-036 and FJ-029's intake round put it there, while the other stops end on the question.
