---
title: "Playbook run: composed FigJam boards on SWE 2 MAX and Claude Sonnet 5.5 high"
description: "The FigJam playbook run after Flow Mode moved from generate_diagram to boards composed with use_figma from a checked model, on SWE 2 MAX before the composer and playbook fixes and on Sonnet 5.5 high after them."
trigger_phrases:
  - "composed boards playbook run"
  - "swe 2 max figjam run"
  - "compose-board playbook run"
importance_tier: "normal"
contextType: "general"
---

# Playbook run: composed FigJam boards on SWE 2 MAX and Claude Sonnet 5.5 high

This run tests one change: Flow Mode composes every FigJam board with `use_figma` from a checked model, using `sk-create-figjam/assets/compose-board.js`, where it used to call `generate_diagram`. Two model sets ran against a live Figma route, one before the composer and playbook fixes and one after them, and a no-Figma pair ran earlier. Of 26 graded rows, 3 pass, 22 fail and 1 is skipped. The failures are mostly stop discipline and composer geometry, not boards that cannot be read. A rerun of all 18 board scenarios after phase 034 (section 10) fixed stop discipline in every run: 2 pass and 16 fail, now on first-glance emphasis, composer routing and reply tails.

---

## 1. Verdict

**What composing bought**

- **Boards that match their model.** Fidelity scores 2 of 2 on all 14 scored boards, so every read-back count and label matched the checked model
- **Boards a reader can use.** A fresh Sonnet reader answered the three clarity questions from colour screenshots alone and got 3 of 3 on 13 of 14 scored scenarios. The one miss is FJ-033, where the leadership board kept an engineering gateway hop. The SWE answers come from `notes.md` only, because the verbatim answers for those boards were not kept
- **A better design rubric score.** The same "Start a return" flow scores 7 of 16 on the 2026-10-22 generated board and 15 of 16 on the composed board 29:1663 (FJ-031), on `quality-rubric.md` Section 7. The grader agrees on seven of eight criteria and scores Colour by meaning 1 where `notes.md` scores 2, because the three zone tints have no key entry, which gives 14 of 16. The criterion by criterion table is in section 7

| Criterion | 10-22 board | Composed board |
|---|---|---|
| Frame and entry | 0 | 2 |
| Reading order | 2 | 2 |
| Colour by meaning | 1 | 2 (grader: 1) |
| Grouping | 0 | 2 |
| Legibility | 2 | 2 |
| Connector clarity | 1 | 2 |
| Key and source | 0 | 2 |
| Proportion | 1 | 1 |
| Total | 7 | 15 (grader: 14) |

The 7 comes from `notes.md` and its screenshot is not in the run folder. The grader could not check it, and neither could I. The two boards also differ in model and in route, so the gain is not attributable to composing alone.

**What still fails**

- **Stops.** The playback and the gate merge into one stop in 14 of the 23 board runs in sets 1 and 2 and in both no-Figma runs. Five of the 13 Sonnet runs wrote on the reading yes (section 4)
- **Scored boards.** Only FJ-028 passes, at 22 of 22. Eight of the 14 scored boards reach 18 or more, and all but FJ-028 fail on a full-marks condition or on an early write
- **Composer geometry.** Labels collide with zone titles, composite state exits share a vertical, parallel edges to one target route over a zone and a loop edge crosses its return (section 5.2)
- **No clean before and after.** No scored board ran in both sets. The two nearest same-flow pairs both score lower on the fixed composer: damaged-item refund 19 (FJ-034, SWE) against 17 (FJ-023, Sonnet) and start a return 21 (FJ-031, SWE) against 16 (FJ-022, Sonnet). Different model, different scenario signals and different model choices sit between each pair, so this does not show the fixes failed, but it does not show they worked
- **Reply voice.** 15 of the 25 SWE reply files carry an em dash and 14 carry a semicolon. None of the 40 Sonnet reply files carries either, counted by character. SWE replies that claim 0 hard blockers still hold the characters (FJ-027 per the grader)

---

## 2. Run integrity

| Set | Model | Runtime | Scenarios | Turns | Incomplete |
|---|---|---|---|---|---|
| 1 | SWE 2 MAX, permission dangerous | Devin 3000.11.205 (6dea39440ae3) | 11 graded of 12 scheduled | 24 on the 10 finished scenarios, 27 logged ok turns in all | FJ-023 never reached its write turn and FJ-025 never ran |
| 2 | Claude Sonnet 5.5 high (`llmgateway/claude-sonnet-5-5#high`) | OpenCode v2.1.4 | 13 | 40, every scenario on its first attempt | none |
| 0 | Claude Sonnet 5.5 high, in-session agents | no Figma route | 2 (SFL-001 and FJ-009) | 4 and 3 | not applicable |

**Set 1, SWE 2 MAX through Devin**

- Ran on the composer and playbook before their fixes. No snapshot of that playbook was kept, so the SWE grade reads the manifest turns against the working tree's signals
- Every scenario got its own scratch tree, its own Devin session and a seatbelt sandbox, one scenario at a time because all boards land on one shared file
- Devin's free-model limits hit repeatedly. FJ-027 failed three attempts and ran again later, FJ-023 timed out on turn 2 at 1500 s then died on turn 3, and a final batch waited on a 118 minute limit until the operator said not to use SWE further. Logged wall time is 139.9 minutes with the failures included
- **FJ-023** has no board. Attempt 2 reached the gate on turn 2 and died on turn 3, and attempt 3 died in 3.8 s
- **FJ-025** is missing from the grader file. Its two attempts ended in about 3 s with no export, its scenario folder is empty and no row exists for it. The task brief and the grader file name only FJ-023 as unfinished
- `first-pass/` holds copies of the FJ-024, FJ-029 and FJ-032 runs and is identical to their `skill/` folders

**Set 2, Sonnet 5.5 high through OpenCode 2**

- The fixed composer and the fixed playbook. 13 scenarios, 40 turns, 61.0 minutes of logged wall time, about 12.23 USD as reported by the runtime and 302,077 output tokens
- Each scenario ran in a seatbelt sandbox from a fresh tree with the same isolation proof as the 2026-10-22 runner
- Four reported "Figma tools gone" turns made zero tool calls (section 4)

**Set 0, the no-Figma pair**

- SFL-001 and FJ-009 ran earlier as Sonnet 5.5 high agents inside the session with no Figma route and instruction-level isolation only, no seatbelt
- Their transcripts are not in the run folder, so their verdicts rest on the operator's grading notes in `notes.md` and I could not check them
- Two harness artifacts touched them. The agents called the driver the coordinator and treated the relayed yes as not the user's, and SFL-001 wrote scratch files outside its tree. The fix, a first prompt saying every later message is the user's own words, was applied to the Figma set only. Whether a rerun would change either verdict is UNKNOWN

**Harness facts**

- The claude.ai Figma connector dropped mid-session and mcp-remote is refused by Figma's client registration with HTTP 403, so OpenCode 2's own Figma client was the route
- Every board went onto one shared fictional test file, so a same-title board from an earlier scenario can read as a revision to a later one
- OpenCode 2 hides MCP tools behind `execute`. The Figma server connects late, so a first call can report "Unknown tool figma". That text appears in 7 Sonnet transcripts
- Board links and emails are redacted in replies. Graders used screenshots taken through OpenCode 2 that are not kept here
- A backup copy of OpenCode's database avoided a start-up hang when it shared the live file with peer sessions

---

## 3. Results

Score is the 22-point board scorecard. A dash means the scenario has no scored board. A fail on a scored board can come from the stops, the hygiene checks or the reply as well as the total. Full signal lists and every loss with its location and fix are in the grader files and `results.jsonl` holds one line per row.

### 3.1 Set 1, SWE 2 MAX (11 rows: 1 pass, 9 fail, 1 skip)

| ID | Verdict | Score | Reason |
|---|---|---|---|
| FJ-023 | SKIP | - | No board. Devin timeout then rate limit before the write turn |
| FJ-024 | FAIL | - | No board. The pre-fix two-turn script ended on the gate, a playbook defect |
| FJ-027 | FAIL | 16 | Two boards, composer output hand-patched, recompose with no yes, shared trunk, card one row short, temp files left |
| FJ-028 | PASS | 22 | Gantt with no crossings or trunks and Android left out. Playback and gate were one stop |
| FJ-029 | FAIL | - | No board. Intake, outline stop and gate outran two turns |
| FJ-030 | FAIL | 18 | Deleted a tagged board the run did not create, temp files left, extra reply line |
| FJ-031 | FAIL | 21 | Old board deleted on the compose yes, then a false claim of one board in the file |
| FJ-032 | FAIL | - | No board. The model held the stops and the script had no turn left for the write |
| FJ-033 | FAIL | 19 | 7 nodes against 6, gateway lane kept, shared trunk, clarity 2 of 3 |
| FJ-034 | FAIL | 19 | Source line edited after the compose, back edge through a node, a tint per lane |
| FJ-036 | FAIL | 17 | One crossing and three shared trunks |

FJ-024, FJ-029 and FJ-032 are FAIL by the PASS line with the cause named as the playbook, and FJ-023 is SKIP. Treat all four as invalid runs. The playbook SKIP clause at grading time named only an unavailable Figma MCP, so the FJ-023 SKIP stretched it.

### 3.2 Set 2, Sonnet 5.5 high (13 rows: 2 pass, 11 fail)

| ID | Verdict | Score | Reason |
|---|---|---|---|
| FJ-008 | FAIL | - | Wrote on the reading yes after a merged stop. Counts 6 of 6, 6 of 6 and 12 of 12. A close call |
| FJ-017 | FAIL | - | Merged stop and early write. Notes landed as pins and a legend column at the far right, not single stickies |
| FJ-019 | PASS | - | Stops held and 9 of 9 nodes, 8 of 8 connectors and 6 of 6 lanes. Two zone titles struck through by connectors |
| FJ-022 | FAIL | 16 | No early write. The Drop-off point label prints over the Done zone title |
| FJ-023 | FAIL | 17 | Merged stop and write on the reading yes |
| FJ-024 | FAIL | 17 | Two edges strike zone titles and cross. Held only by an unverified tools-gone claim |
| FJ-025 | FAIL | 21 | Best board of the set, but both boards were written on the reading yes |
| FJ-026 | FAIL | 18 | Composition 1 on a single-lens call, would pass at 19 with Composition 2 |
| FJ-029 | FAIL | 19 | Clean stops. The reply misses the split under Left out and the one line per diagram |
| FJ-032 | FAIL | 17 | Merged stop, early write and the named board never read |
| FJ-039 | FAIL | - | Nothing written but the model was built before the playback and the gate merged into it |
| FJ-040 | PASS | - | Nothing written and a waiting gate. The scope is four boards, not one narrowed flow |
| FJ-041 | FAIL | - | Modelled over a screen path brief with no question, then wrote on "use your recommendation" |

FJ-025 and FJ-029 each carry two boards. FJ-025 scores 21 on both. FJ-029 shows the per-dimension minimum of its two boards, 19, and its first board alone scores 21. FJ-032 shows its first compose at 17 and its recompose scores 19. FJ-008 has no screenshot, so its board findings are the run's own.

### 3.3 Set 0, no Figma route (2 rows: 2 fail)

| ID | Verdict | Score | Reason |
|---|---|---|---|
| SFL-001 | FAIL | - | Turn 1 opened an intake round the fixed pass criteria forbid. The fj route was not named as the second missing route |
| FJ-009 | FAIL | - | Wrote nothing and named the missing connection, but did not say the fj route cannot draw a gantt chart or offer the checked model |

Both rows rest on `notes.md` alone, since no transcript is in the run folder.

### 3.4 Where graders and `notes.md` disagree

Verdicts follow the graders. For each point I say what I checked.

- **FJ-008 write timing.** Notes say it wrote on the playback turn and ask whether turn 1 carried the gate. The grader says it did. I read the turn-1 reply and it ends on a Gate block and a line asking to write, so the grader holds. The close call is real. It flips to PASS only if a yes to a merged stop counts as the gate's yes
- **FJ-028 Signal.** Notes score 0 because the critical bar is marked by colour alone. The grader scores 2 because the greyscale bar matches the key swatch. I viewed the greyscale screenshot and the grader holds, with weak contrast and without the `, critical` suffix the skill asks for
- **FJ-036 trunks.** Notes count one shared trunk and the grader counts three. I viewed the overview screenshot and found three
- **FJ-030 delete.** Notes accept the delete of the tagged probe board and call the legend stickies default blue. The grader fails nothing-else-changed and says the code sets the colour explicitly. I did not recheck either point
- **FJ-031 rubric.** 15 of 16 against 14, as in section 1. I did not view the screenshot
- **FJ-022 label.** Notes call it Drop-off at store. The reply and board say Drop-off point, and 48:2080 is the connector while the board is 48:2023. The grader's text writes the connector id where it means the board
- **FJ-032 Sonnet.** Notes describe an existing retro board. The runner pinned the shared file, so the retro is one section among many

---

## 4. Stop discipline

Flow Mode's staged stops are an intake round, an outline pass, a playback that waits for its own yes, a gate that waits for its own yes, the write and the read-back. `flow-mode.md` Section 8 says the playback answer is not the gate's yes. Counts below are the graders' calls unless a line says I checked.

**Merged playback and gate** (one reply that holds both and asks one yes)

- Set 2: 8 of 13. FJ-008, FJ-017, FJ-023, FJ-024, FJ-025, FJ-026, FJ-032 and FJ-039. I read the turn-1 replies of FJ-008 and FJ-023 and the rest stand on the graders' word
- Set 1: 6 of the 10 finished scenarios. FJ-027, FJ-028, FJ-030, FJ-033, FJ-034 and FJ-036. I read the turn-1 tails of FJ-027, FJ-028, FJ-030 and FJ-033. The pre-fix two-turn playbook rewarded this, so the six are not like for like with set 2
- Set 0: 2 of 2 per the notes
- Sets 1 and 2 together: 14 of 23 board runs

**Wrote on the reading yes**

- Set 2: 5 of 13. FJ-008, FJ-017, FJ-023, FJ-025 and FJ-032. FJ-019 refused the same phrase as a write yes, which is the strongest sign these were model errors and not playbook defects
- FJ-041 wrote on "use your recommendation" with no recommendation on offer, a sixth wrong write
- Set 1 cannot show this, because its two turns made the merged stop equal the gate

**Held only by a claim with no tool call behind it**

- FJ-024 turn 2, FJ-026 turn 2 and FJ-039 turn 3 declined to write because the Figma tools were gone. FJ-025 turn 3 made the same claim after it had already written. The run log shows zero tool calls in each of those turns
- The cause is likely the late-connecting Figma server under OpenCode 2, since "Unknown tool figma" shows up in 7 transcripts. I did not confirm it for these four turns

**Model built before the playback**

- FJ-023, FJ-024, FJ-025, FJ-026, FJ-039 and FJ-041 ran the check and the compose before the playback yes. `flow-mode.md` Section 8 puts the playback first, and FJ-041 and FJ-039 expect no model at all

**Held the intended sequence**

- Set 2: FJ-019, FJ-022, FJ-029 and FJ-040, 4 of 13. FJ-022 spent the reading yes on its intake round, so no separate full playback ran
- Set 1: FJ-024 and FJ-032 held every stop and ran out of script. FJ-029 stopped for an extra outline answer

**Deletes**

- Set 1: FJ-030 and FJ-031 deleted an older board on the compose yes. Set 2: none. FJ-032 and FJ-022 asked for a separate yes before any delete, as `flow-mode.md` Section 9 requires

---

## 5. Composer findings

### 5.1 Fixed between sets

The composer fixes merged after set 1 cover back edges, fan-in trunks, group overlap, card height, the critical-bar cue, lane height and composite edges. The Sonnet set shows these effects, with the caveat that no scored scenario ran in both sets:

| Fix | Set 1 defect | Set 2 evidence |
|---|---|---|
| Back edge | FJ-034: Send a second photo to Damage clear? ran through Approve the claim, `magnets()` never ran `clear()` on the `r1 <= r0` branch | FJ-023 on the same flow shows no run through a node, but its Unclear and return edges still cross |
| Fan-in trunks | FJ-027, FJ-033 and FJ-036: edges into one node shared a trunk | FJ-024 has fan-in from three clients with Shared trunks 2. Remaining trunks are fan-out from a diamond or group exits |
| Lane height | FJ-034 and FJ-033: lanes far taller than content | FJ-023 records no lane height loss. I did not view the board |
| Group overlap | FJ-027: Partner side drew over Guest side with only a warning | Not exercised. No Sonnet scenario uses group zones |
| Card height | FJ-027: the last field sat on the card's bottom edge | Not verified. FJ-008 drew an ER board but has no screenshot |
| Critical-bar cue | FJ-028 critical bar carried by colour with a weak greyscale contrast | Not exercised. FJ-028 did not run in set 2 |
| Composite edges | FJ-026 and FJ-032 style exits from a group | Not holding, see 5.2 |

### 5.2 Open, fixed in 034

Found on the fixed composer and carried into phase 034, `specs/017-figjam-flow-generation/034-stop-and-label-fixes`:

- **Labels over zone titles.** FJ-022 Drop-off point prints over the Done title. FJ-019 and FJ-024 have the Edge and Events titles struck through by connectors
- **Parallel edges to one target.** FJ-022: two edges from one diamond to one goal, the second routed over the top of the Done zone
- **Loop edge crossing its return.** FJ-023: Unclear crosses the return edge under its own label. The agent tried seven variants and found no model fix
- **Composite exits.** FJ-026 and FJ-032: guest cancels leaves the Confirmed group on one vertical shared with the no-show edge and its label sits on that line
- **Parallel edges between one pair of states.** FJ-041: the choose refund arc leaves from the middle of the choose store credit line
- **Sequence lifeline.** FJ-025: Booking confirmed crosses the PaymentProvider lifeline. The scenario fixes the participant order, so this is a composer or playbook limit. The async hub message also lacks an open arrow
- **Accent and tint clashes.** FJ-023 gives a data store and the in-focus node the same violet. FJ-026 and FJ-032 give the first state a blue that beats the planned end-state glance
- **Check gap.** FJ-019 reported 0 crossing pairs in the composer check while the drawn board crosses at Consumes and Publishes
- **Live ER routing.** FJ-008's own report of a Guest to Booking crossing and a fork. No screenshot, so unverified
- **Sticky size.** FJ-030's legend stickies read smaller than node labels, a model-side extension setting

The 034 scope is as stated by the operator. I did not open its documents.

Model-side faults that are not composer defects: temp model and script files left behind (FJ-027 and FJ-030), a source line edited after the compose (FJ-034), reply shape (FJ-027, FJ-029 and FJ-030) and the FJ-022 model that dropped the two method nodes the example carries.

---

## 6. Playbook and skill contract mismatches

Found at grading time on 2026-10-24 and rechecked against the working tree at about 18:24. The playbook root changed at 18:18 and `flow-mode.md` at 18:20, after the graders finished at about 18:11, so some of this has moved.

| Mismatch | State now |
|---|---|
| Two-turn scripts had no turn for the gate's yes (FJ-023, FJ-024, FJ-029, FJ-032) | Fixed in the Sonnet manifests with three turns and FJ-019 with four. FJ-029 may still be one turn short if the outline pass stops again |
| `flow-mode.md` Section 9 said the delete waits only "after the user agrees", the playbook expected a second yes | Section 9 now says the delete waits for its own yes |
| FJ-034 said "each tinted by the composer" and "no colour per team" while the composer tints each lane | The phrases are gone and the scenario now says each lane takes the composer's zone tint. Not re-run |
| Scorecard Signal had no rule for zone tints, pins and legend stickies | Section 3 now has "Marks the key does not list". The grader likely read the older text |
| The SKIP clause covered only an unavailable Figma MCP | The playbook now says an incomplete run is not a SKIP |
| Gantt read-back: playbook 5 of 5 tasks, skill example 6 of 6 | Still 5 of 5 in the playbook. FJ-028 followed the skill and counts the milestone among 6 |
| FJ-033 asks for at most 6 nodes in capability words but the check forces a gateway lane node | Still open |
| FJ-017 expects "2 of 2 notes" while `hybrid-workflow.md` Section 6 shows the pin form of Extensions | Both forms now appear among the Extensions examples in that file. Not re-run and Section 3 not rechecked |
| FJ-040 asks for one recommended scope and a playback with no model while `flow-mode.md` Section 2 has an outline pass | Not rechecked |
| FJ-022 expects 9 nodes while the brief supports 7 | Not rechecked |
| FJ-025 answer key wording (BookingCreated, 201 Booking confirmed) differs from the example boards (Booking confirmed, 201 Created) | Not rechecked. The reader was scored on meaning |

The graders read the scenario signals as they stood during grading, and no snapshot of the playbook as run exists. A signal text that moved afterwards is a source of error I cannot size.

---

## 7. Comparison with 2026-10-22

The 2026-10-22 run was DeepSeek V4.1 Flash max on OpenCode v2.0.32 through the `generate_diagram` route, with two-turn scripts. It has no README, and `results.jsonl` holds 29 rows from its batch A only, none of which is a scenario here. Its batch B of 21 scenarios ran and left replies but no verdicts. A verdict against verdict comparison is therefore not possible for any scenario. FJ-009 did not run there at all.

The table below shows what can be said without a verdict: whether the 2026-10-22 run ended with a board read-back, found by looking for a `Read-back:` line in its replies, which is not a grade.

| ID | 2026-10-22 | This run |
|---|---|---|
| FJ-008 | 2 turns, board | Sonnet FAIL |
| FJ-017 | 2 turns, board | Sonnet FAIL |
| FJ-019 | 2 turns, board | Sonnet PASS |
| FJ-022 | 2 turns, board | Sonnet FAIL 16 |
| FJ-023 | 2 turns, board | SWE SKIP, Sonnet FAIL 17 |
| FJ-024 | 2 turns, board | SWE FAIL no board, Sonnet FAIL 17 |
| FJ-025 | 2 turns, no board | Sonnet FAIL 21 |
| FJ-026 | 2 turns, board | Sonnet FAIL 18 |
| FJ-027 | 2 turns, board | SWE FAIL 16 |
| FJ-028 | 2 turns, board | SWE PASS 22 |
| FJ-029 | 2 turns, board | SWE FAIL no board, Sonnet FAIL 19 |
| FJ-030 | 2 turns, board | SWE FAIL 18 |
| FJ-031 | 2 turns, no board | SWE FAIL 21 |
| FJ-032 | 2 turns, no board | SWE FAIL no board, Sonnet FAIL 17 |
| FJ-033 | 2 turns, board | SWE FAIL 19 |
| FJ-034 | 3 turns, board | SWE FAIL 19 |
| FJ-036 | 2 turns, board | SWE FAIL 17 |
| FJ-039 | 2 turns, no board | Sonnet FAIL |
| FJ-040 | 2 turns, board | Sonnet PASS |
| FJ-041 | 2 turns, board | Sonnet FAIL |
| SFL-001 | 2 turns, board | no-Figma FAIL |
| FJ-009 | not run | no-Figma FAIL |

A board written on 2026-10-22 does not mean it passed. FJ-039 and FJ-040 are no-write scenarios in this run's playbook, and the playbook text changed between the two runs. The one comparison with a measure behind it is the design rubric in section 1. Grading the 2026-10-22 batch B boards on the same scorecard would turn this table into a comparison. That was not done.

---

## 8. Deviations from the playbook

- **Turns.** Set 1 ran the pre-fix scripts, two turns for most scenarios, three for FJ-034 and five for FJ-031 with FJ-022's turns run first as its setup. Set 2 ran the fixed scripts, three turns for most and four for FJ-019. SFL-001 got an extra "Use your recommended answers." turn after it opened an intake round
- **The shared file.** All boards went onto one fictional test file, so a same-title board looked like a revision (FJ-030 and FJ-031 both saw an earlier "Start a return") and the FJ-032 "existing retro board" is one section of the shared file. FJ-032's key placeholder was replaced by the test file's key. Its composed boards land 400 px right of all content, so it cannot overlap the retro
- **The file pin.** Every first turn gained a line telling the agent to write into the existing test file. FJ-008 got a line to create a new file in the operator's personal plan instead, which is the new-file path under test. That file is still to be deleted by the operator
- **Follow-up turns.** The runner can append "Yes, go ahead." up to a cap when a scenario ends with no board. It was set to 2 for FJ-027 and FJ-028 and neither needed one. FJ-024, FJ-029 and FJ-032 ran without it. The planned follow-up reruns were replaced by the Sonnet set
- **The screenshot route.** Boards were photographed through OpenCode 2 at overview size, at 100% zoom and in greyscale. The shots and the clarity answers are in the grader's scratch folder and none is kept here
- **Playbook state.** The SWE set was graded against the working tree's signals and the Sonnet set against the manifest's turns. Neither playbook version is preserved

---

## 9. Not done

- No SWE board for FJ-023, and no SWE run of FJ-025 at all. The four invalid SWE runs were repeated with Sonnet, not with SWE
- FJ-027, FJ-028, FJ-030, FJ-031, FJ-033, FJ-034 and FJ-036 never ran on the fixed composer, so the group overlap, card height, critical-bar cue and lane height fixes have no live evidence
- FJ-008 has no screenshot and no scorecard, and the new file it made is still to be deleted
- The 2026-10-22 batch B boards were not graded
- The no-Figma transcripts are not in the run folder
- Only one board was scored on the design rubric, and the 7 of 16 for the older board was not verified by me
- Verbatim reader answers for the SWE boards were not kept
- FJ-029 on SWE and the unverified tools-gone claims have no confirmed cause

---

## 10. Rerun after phase 034

All 18 board scenarios ran again after phase 034, on the skill and playbook that phase left, with Claude Sonnet 5.5 high. FJ-017, FJ-019, FJ-022 and FJ-023 ran on OpenCode 2 on 2026-10-24. The LLM Gateway then reached its daily quota, so the other 14 ran on 2026-10-25 through the Claude Code CLI (`run/claude_playbook_runner.py`) with Figma's hosted MCP server, the same model and effort and the same sandbox builder and isolation. Rows are in `results.jsonl` under `"set": "rerun"`, evidence in `rerun-034/` and `rerun-034-adapted/`.

### 10.1 Verdicts

2 pass and 16 fail.

| Scenario | Verdict | Score | Second lens on Composition | What decides it |
|---|---|---|---|---|
| FJ-017 | PASS | n/a | n/a | Playback, gate and write held, two single stickies, true Extensions line |
| FJ-019 | PASS | n/a | n/a | Four stops held, one compose call, six lanes |
| FJ-022 | FAIL | 21 | 1 | Composition 1 |
| FJ-023 | FAIL | 20 | 1 | Composition 1, shared stub at the decision |
| FJ-024 | FAIL | 20 | 0 | Composition 1, shared stub at sync-service |
| FJ-025 | FAIL | 20 | 0 | Composition 1, one crossing |
| FJ-026 | FAIL | 17 | 0 | Composition 1, InStay label, shared trunks |
| FJ-027 | FAIL | 17 | 2 | Shared trunks, a crossing, a label at a junction |
| FJ-028 | FAIL | 21 | 2 | Reply 1, text after the HVR line |
| FJ-029 | FAIL | 19 | 1 | Composition 1, split not named under Left out |
| FJ-030 | FAIL | 20 | 0 | Composition 1, 7 nodes where 9 are expected |
| FJ-031 | FAIL | 21 | 1 | Composition 1, revision skipped its playback |
| FJ-032 | FAIL | 19 | 0 | Composition 1, Clarity 1 |
| FJ-033 | FAIL | n/a | n/a | No gateway node added, type switched on a bare yes |
| FJ-034 | FAIL | 20 | 1 | Reply ties a colour to each team |
| FJ-036 | FAIL | 17 | 1 | Shared trunks 0, Composition 1 |
| FJ-039 | FAIL | n/a | n/a | Second intake round where the PASS line allows none |
| FJ-041 | FAIL | n/a | n/a | Never named the type mismatch |

### 10.2 What the rerun shows

- **Stop discipline is fixed.** No run wrote before the gate's own yes, every delete waited for its own yes and a yes that answered no gate never wrote (FJ-031 adapted, turn 5). FJ-031's main chain refused a delete whose target its own rollback line had named wrongly and asked again
- **First glance is the main blocker.** The model plans a first glance on a node the composer leaves quiet, such as a goal at the far right, a grey end state or a plain service, and the blue start pill and the kind fills read first. `quality-rubric.md` Section 3 already puts the accent on the first-glance node, so nothing enforces a rule the skill states. The two boards that score 2 on both lenses put the one accent on the planned first element. On FJ-023 the accent violet matches the store fill
- **Routing still fails connector clarity on architecture and ER.** Edges run along zone borders, two edges leave one node on a shared stub and ER relationships share corridors. The design rubric moved from 4 to 11 on architecture and 5 to 11 on ER with connector clarity at 0 on both, and from 5 to 15 on user flow (`quality-rubric.md` Section 7, against the 2026-10-22 boards)
- **Reply tails.** Several delivery replies carry commentary after the HVR line, which `flow-mode.md` says is the last line
- **Model misses the skill already covers.** FJ-033 did not add the gateway node `architecture.md` requires on a simplified board, FJ-034's reply ties a colour to each team and FJ-041 modelled the named type without naming the mismatch

### 10.3 Harness notes

- **Turn shift.** Each scenario tells the operator to answer an intake round with the recommended answers. The runner sent fixed turns, so a run that opened an intake round reached each later yes one stop early. FJ-027, FJ-032 and FJ-036 got supplementary turns (`turn-supplementary*` files, `supplementary_turns` in `meta.json`) and FJ-031 ran again with `run/adaptive_scenario.py`, which answers an intake round when a small classifier labels the reply one. Stop discipline is graded on the declared turns
- **Shared test file.** Boards stayed on the test file between scenarios, so FJ-032 found an earlier "Booking status" section and FJ-031 found earlier "Start a return" sections. Neither is counted against the model
- **Screenshots** for the Claude Code boards were rendered through the Figma REST API at 100%, with the overview downscaled to 2048 px and a greyscale copy
- **Clarity** comes from fresh blind readers who saw only the screenshots and the questions

These findings open phase `specs/017-figjam-flow-generation/035-first-glance-and-routing`.
