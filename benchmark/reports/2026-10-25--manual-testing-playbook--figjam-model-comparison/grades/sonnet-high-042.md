# Sonnet high rerun grades on v1.0.8.0

These are the grades for the 14 FigJam scenarios that failed on `sk-create-figjam` v1.0.7.0, run again by Claude Sonnet 5.5 at high effort on v1.0.8.0. One grader scored every run from the transcripts, the tool calls, the renders and the fresh readers' answers, so every total sits on one scale. The per-run detail with every signal, cite, loss, location and fix is in `sonnet-high-042.jsonl`.

After the skeptic adjudication and the operator's two rulings folded into the records, the rerun passes 7 of the 14 scenarios. 7 fail. None is NOT RUN. The count rests on those rulings, set out under Operator rulings below: without them it is 6.

## How the grades were set

- **Glance order.** The plan comes from the gate's glance lines and the first glance from the read-back's `first glance:` clause. The measured order is the reader's section 2, checked against the render. On a state board the composite section counts as frame, as v1.0.8.0 sets, but the states drawn inside it still count as parts, applied as written on every state board by the operator's ruling. Lanes and zones count as frame on every type, like the title block, by the operator's ruling.
- **Legibility.** A label that wraps with one word alone on its last line, in a box with room to spare, costs one point, as the FJ-029 adjudication set on v1.0.7.0. It decides no verdict here, because Legibility is not a full-marks dimension.
- **Near-parallel runs.** Two connector runs about 24 px apart that never merge keep Shared trunks at 2, as the FJ-017 adjudication set, and are recorded as a composer finding.
- **Turn shifts.** An intake round that pushes the playback, the gate and the write one turn later is accepted (FJ-029 and FJ-036).
- **Harness.** FJ-031's operator sticky is the operator's node and stayed untouched. FJ-045's design break (`step2.txt`, exit 1 with three `DESIGN` lines) and restore (`step6.txt`, exit 0) are the operator's and both held.
- **Evidence.** The reader notes, greyscale renders and operator files sit in `grades/sonnet-high-042/` and the renders in `renders/`, and every evidence path in the records resolves inside the run folder.
- **Adjudication.** A skeptic challenged the grades of eleven scenarios and an adjudicator ruled on each point. Every ruling the skeptic won is folded into `sonnet-high-042.jsonl`, and every count and total below is taken from the folded records.

## The 14 scenarios

| ID | v1.0.7.0 | v1.0.7.0 total | v1.0.8.0 | v1.0.8.0 total |
|---|---|---|---|---|
| FJ-009 | FAIL | no board | FAIL | no board |
| FJ-017 | FAIL | no scorecard | FAIL | no scorecard |
| FJ-023 | FAIL | 21 | PASS | 21 |
| FJ-026 | FAIL | 19 | FAIL | 21 |
| FJ-029 | FAIL | 16 | FAIL | 19 |
| FJ-031 | FAIL | 21 | FAIL | 18 |
| FJ-032 | FAIL | 20 | FAIL | 21 |
| FJ-033 | FAIL | 21 | PASS | 20 |
| FJ-034 | FAIL | 20 | PASS | 21 |
| FJ-036 | FAIL | 21 | FAIL | 20 |
| FJ-038 | FAIL | no board | PASS | no board |
| FJ-040 | FAIL | no board | PASS | no board |
| FJ-042 | FAIL | no board | PASS | no board |
| FJ-045 | FAIL | 21 | PASS | 22 |

Pass count: 7 of 14, up from 0 of these 14 on v1.0.7.0. SC-001 asks for at least 7, so it is met only under the operator's rulings.

## Remaining failures

- **FJ-009, model slip.** Nothing was written and turn 3 now names the missing route, the `fj` limit and the kept model. The turn 2 gate still carries a Plan line and a Calls line and asks to write once the tools connect, where `references/flow-mode.md` Section 6 No route puts the missing route in their place. That signal alone fails the run. Turn 3's promise that the earlier yes will cover a later write is recorded as contradictory evidence under the skill gap. No shipped example shows a missing-route gate, which contributed.
- **FJ-017, model slip.** Two `use_figma` calls, no moved node and both stickies inside the widened board covering no node, but the sticky code shifted each sticky 64 px off level. The No-show note reads against Completed and its end dot, not beside No-show, and the reply reports only that offset, not the Cancelled note's drop. The fallback order in `references/hybrid-workflow.md` Section 3 covered the crowded case.
- **FJ-026, skill gap.** 21 with Composition at 1. The reader takes Upcoming and In stay inside the Confirmed section before the accented Cancelled, while the state rule plans them last. Applied as written, the same reading that costs FJ-032 its point.
- **FJ-029, model slip and skill gap.** 19 with Reply at 0. The boards land 400 px apart with `start here: 1. Sign up` and all three reader answers, but no `Left out:` line names the split. The second board is titled `2. Setup`, the spelling `assets/flow-templates.md` line 113 gives, where the scenario and `references/hybrid-workflow.md` line 170 expect `2. Workspace setup`.
- **FJ-031, model slip and skill gap.** 18 with Composition at 1 and Reply at 0. The compose, the separate delete question and the tagged delete held and the operator sticky stayed put. The gate put the changed Request an exception first in a second glance line shared with the light blue entry and both decisions, and the reader reached it only after the entry and the decisions. Items in one glance line carry no order, so the missed changed end costs one point. Turn 7 opens on prose before the URL and carries no `Left out:` line for the free pickup over EUR 100. The gate's numbered-title rule left the final board titled `Start a return 2`.
- **FJ-032, skill gap.** 21 with Composition at 1. The reader reads Upcoming and In stay inside the Confirmed frame before Pending, the state the plan puts first, while the state rule plans those inner states last.
- **FJ-036, model slip.** 20 with Reply at 1. The board reads in its planned order with no crossing, but the reply opens on a status sentence above the board URL.

## The v1.0.8.0 fixes

- **Composite as frame and the state glance order.** Partly working. On FJ-026 (state named) and FJ-032 (no state named) the reader takes the states inside the composite before the planned first glance, so both score 21 and fail. The inner states need a place in the plan.
- **Light blue entry and goal planned in the second glance.** Working on FJ-023, FJ-033, FJ-034, FJ-036 and FJ-045 once lanes read as frame. On FJ-034 the reader never names the entry, which costs nothing because the goal reads second as planned.
- **Left out: in the reply and the gate.** Working on FJ-034 and FJ-040. Missed on FJ-029, where the split is not named, and on FJ-031's turn 7 reply.
- **Single sticky past the end dot.** Not working on FJ-017: two `use_figma` calls and no third move, but the code shifted both stickies 64 px off level and the No-show note sits beside Completed.
- **Same-title revision found by write time.** Not exercised. FJ-031 took a numbered title instead.
- **First split title `1. Sign up`.** Working. The second title still differs.
- **FJ-009 gate names the missing route.** Not shown by the run.
- **FJ-038 second yes after the read-back.** Working.
- **FJ-045 light green goal as the first glance.** Working.
- **The `Label:` line.** Not seen in any run, see gap 1.

## Skill gaps the rerun still shows, most important first

1. **The `Label:` check never reached a run.** No export holds a `Label:` line, while the same shipped `scripts/flow_check.py` on the run models prints them for FJ-023, FJ-031, FJ-034, FJ-036, FJ-042 and FJ-045. `label_words` returns nothing in silence when node is not on the PATH or its trace fails. The cause inside the runs is inferred. Where it does print, its prediction differs from the drawn board: it flags FJ-036's `Pay the difference` and FJ-045's `Within 30 days?`, both drawn on one line, and misses FJ-036's `New price vs old?`, which wraps. Orphan wraps cost Legibility on six of the nine scored boards.
2. **Two spellings of the second split title.** `assets/flow-templates.md` line 113 uses `2. Setup` and `references/hybrid-workflow.md` line 170 uses `2. Workspace setup`. FJ-029 followed the first.
3. **A revision competes with the entry for the second glance.** `references/quality-rubric.md` Section 3 makes a changed non-failure end the second glance and also plans every light blue entry there, with no order between them. FJ-031's reader took the entry.
4. **Numbered title on a revision.** `references/flow-mode.md` Section 2 step 7 recommends a numbered title for any same-titled section, so a revision that deletes the old board keeps `Start a return 2` and never reaches the Section 6 write-time rule.
5. **Composer runs closer than 56 px.** On FJ-017, FJ-026 and FJ-032 the check out and missed check-in runs lie about 24 px apart beside the Confirmed section, and on FJ-036 the Yes and Pick a room arrivals share one vertical line with a 24 px gap, against `references/style-guide.md` Section 7.
6. **No example of a missing-route gate.** `references/flow-mode.md` Section 6 No route states the rule in one sentence and `assets/examples/gantt-loomlist-offline.md` shows only the composed-route gate, which FJ-009 copied. The turn 3 promise that the earlier yes covers a later write is recorded against this gap as contradictory evidence.

## What the skeptics changed

Each listed run's grade was challenged by a skeptic and settled by an adjudicator. These are the changes where the skeptic won, folded into the jsonl records. The grader's rulings held in full on FJ-026, FJ-042 and FJ-045 and in part on FJ-029, FJ-032 and FJ-034.

- **FJ-009, FAIL stays FAIL, no board.** The signal that the gate's yes carries over to no later write is removed, because the scenario names no such signal. The turn 3 promise is recorded as contradictory evidence against `references/flow-mode.md` Section 6 No route under the existing skill gap. The turn 2 signal stays unmet and fails the run alone.
- **FJ-017, PASS to FAIL, no scorecard.** The sticky signal is now unmet: the No-show note reads level with Completed and its end dot, not beside No-show. Its cite now records that the Cancelled note is also 64 px off level and that the reply reports only the No-show offset. The neighbouring-rows skill gap is removed and ruled a model slip, because the rule's fallback order covered the case. The turn 2 cite now records the local `mktemp -d` scratch folder and its `model.md`, removed in turn 3, with no board or repository write.
- **FJ-023, PASS 21 to FAIL 20.** Composition goes to 1, with a new loss, because the reader reads the title and the three swimlanes before the accented Approve the claim. The glance signal is unmet with the reader's real text as its cite and the scorecard signal is unmet. The Legibility loss location is corrected to the leftmost Warehouse operator step and the `Send a` break, and `Damage clear?` is dropped from it. Legibility stays at 1.
- **FJ-029, FAIL stays FAIL, total stays 19.** The Legibility loss cause becomes model (long label), with the missing `Label:` line kept as a skill gap. `Code correct?` is dropped from its location. Legibility stays at 1.
- **FJ-031, total 19 to 17.** Composition goes to 0, because two parts read ahead of the changed end the plan put first in the second glance. Reply goes to 0, scored on turn 7, which opens on prose before the URL and has no `Left out:` line for the free pickup over EUR 100. The turn 6 clause leaves the Composition loss and joins the Reply loss as a reply fault against `references/quality-rubric.md` Section 3 line 67. Verdict stays FAIL.
- **FJ-032, PASS 22 to FAIL 21.** Composition goes to 1, with a new composer loss, because Upcoming and In stay inside the Confirmed frame read before Pending. The glance signal and the scorecard signal are unmet.
- **FJ-033, total 21 to 20.** Clarity goes to 1, with a new loss, because the reader's Q2 answer names the Entry point and denies the Sync platform. The reader signal stays met with its cite corrected. Verdict stays PASS.
- **FJ-034, PASS 21 to FAIL 20.** Composition goes to 1, with a new loss, because the reader reads the lanes the plan puts last at the second glance and never names the planned entry. The glance signal and the scorecard signal are unmet. The accent signal's cite now names the three neutral lane style lines beside the one node style on approve. Reply stays at 2, the grader's ruling.

## Operator rulings

The completeness critic found two rules the grades applied unevenly, and the operator ruled on both on 2026-10-27. Every record above follows these rulings.

- **Lanes and zones read as frame on every type,** like the title block. FJ-023 and FJ-034 each get back the Composition point a reader's early read of the lane bands cost them. Both now read accent first and goal second, as planned, and pass at 21. FJ-045's zones already cost nothing.
- **The state rule applies as written.** It plans the states inside a composite last, so a reader who takes them early costs a point on every state board. FJ-026 goes from 22 to 21 and fails, the same ruling FJ-032 already carried.
- **FJ-031 within one glance line.** The critic's correction is folded: items named in one glance line carry no order, so FJ-031 loses one Composition point for the changed end read late rather than two. Its total goes from 17 to 18 and it still fails on Reply.

