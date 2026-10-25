# Recheck of phase 035 changes (set recheck-035)

Run: PO/benchmark/reports/2026-10-25--manual-testing-playbook--first-glance-and-routing/recheck. Six scenarios rerun after the crossing rule, the key's In focus sample, the outline pass without stops, the playback-first reply rule and the one-node first glance. Graded against the current skill and scenario files. Compared with SP/grade/g7-035-a.jsonl, g7-035-b.jsonl and g7-035-c.jsonl.

## Clarity was self-read

No fresh reader ran. I answered each scenario's reader questions from the two colour screenshots only, before I opened any reply or transcript. A self-read is weaker than a fresh reader because I knew the question while looking, so every Clarity score below carries that caveat.

My answers, written first:

- FJ-019: no reader questions, the scenario has no scorecard.
- FJ-024. Q1: the API Gateway. Q2: sync-service publishes changes to the Change Stream, Push Worker consumes them and calls Apple Push Service, labelled Wakes iOS devices. Q3: the three dashed ones, Publishes changes, Consumes changes and Apple Push Service: Wakes iOS devices. Scenario answers match, 3 of 3.
- FJ-026. Q1: Completed, No-show and Cancelled, the gray pills with ringed end dots. Q2: Pending and Confirmed, from the two guest cancels arrows. Q3: check in. Scenario answers match, 3 of 3.
- FJ-027. Q1: one room, because Room is 1 to 0..n Booking and Booking carries a single FK roomId. Q2: Property. Q3: yes, zero or more payments. Q1 took a moment of reasoning, see the label risk below. 3 of 3 with the scenario's Q3 wording off (the board says zero or more, the scenario says at least one).
- FJ-032. Q1: Completed, No-show and Cancelled. Q2: the card is authorised. Q3: I cannot answer, the screenshots hold only the new section and no retro content. 2 of 3.
- FJ-036. Q1: the guest sees Other rooms shown. Q2: Difference given as credit (automatic). Q3: no, Nothing charged (automatic). Scenario answers match, 3 of 3.

## Results

| ID | Verdict | Total | Composition | Before (phase 035 grade) |
| --- | --- | --- | --- | --- |
| FJ-019 | PASS | unscored | n/a | PASS |
| FJ-024 | PASS | 21 | 2 | PASS, 19 |
| FJ-026 | PASS | 22 | 2 | FAIL, 19 (Composition 0) |
| FJ-027 | PASS | 22 | 2 | PASS, 20 |
| FJ-032 | FAIL | 20 | 1 | FAIL, 19 (Composition 0) |
| FJ-036 | PASS | 21 | 2 | PASS, 20 |

## What changed and why

- **FJ-026, FAIL to PASS, 19 to 22.** The gate now plans Pending as the one first glance and says the layout shows it first, so the plan and the board agree. Composition 0 to 2. Shared trunks 1 to 2 because the Completed to end dot edge no longer rides the missed check-in vertical.
- **FJ-027, 20 to 22.** The subtitle fits one line (Legibility 1 to 2) and the key's In focus sample is now a pink ring on a white entity like Booking (Signal 1 to 2).
- **FJ-024, 19 to 21.** Writes Blocks now loops over the Events zone and no longer lands on Consumes (Crossings 1 to 2). The key sample matches the marked node (Signal 1 to 2). Clarity 1 to 2 on my own read, not comparable with the fresh reader before. Legibility 2 to 1 because the subtitle wraps and leaves the word Engineering alone on its second line.
- **FJ-036, 20 to 21.** Signal 1 to 2 for the key sample. The run stopped five times (two intake rounds, playback, gate, delivery) against nine before, so the outline pass no longer adds stops and the contract defect named last round is gone.
- **FJ-032, still FAIL, 19 to 20.** Composition 0 to 1. The gate plans Pending first, which the layout shows first. It plans the six event labels second and the gray end states last, and the end states read second. The board is pixel-identical in layout to FJ-026 and only the planned second and last differ. Clarity stays 1 because the reader packet holds only the new board. The model again made no second read of the retro nodes after the write. The Assumed row for the check in transition that the last run carried is gone.
- **FJ-019, PASS both times.** The dashed-over-solid crossing is gone and the key sample now matches Sync Service.

## Operator observation on the In focus swatch

Fixed on every board where it showed (FJ-019, FJ-024, FJ-027, FJ-036). The key sample is now the marked node's own kind under the pink outline, and the greyscale copies keep it. No Signal or Legibility loss remains from it.

## Crossing rule check

I looked for a bend that lands on another edge on all six boards. The only candidate is FJ-036, where the Pick a room bend meets the Yes line about 55 to 65 pixels before the price diamond's left tip. Both edges end at that one magnet, which style-guide Section 3 allows as a merge, so I scored it as Shared trunks 1 and not as a crossing. If a grader reads it as a crossing, FJ-036 drops to 20 and stays PASS.

## Judgement calls and open items

- **FJ-026 Composition 2 is a judgement.** The request is about colouring the end states and the plan names Pending. The skill says a planned first glance is one thing and never the end states as a group, so I scored the plan against the board. A grader who holds the end states are the element the request is about would score 1 and FAIL the scenario.
- **FJ-032 versus FJ-026.** Same layout, different Composition, because the plans word the second glance differently. A contract hint would remove the gap. Proposed one-line amendment for style-guide Section 3 after line 150: 'Fixed gray end states and keyed fills outweigh edge labels in the overview, so plan them before the labels.'
- **Playback and recommended answers.** FJ-019 turn 3: the runner sent a second 'Use your recommended answers.' after the playback and the model sent the gate. flow-mode.md Section 8 does not say whether that phrase answers the playback. Proposed one line for the end of The gate is its own reply: 'A request to use the recommended answers sent after the playback counts as the playback's answer.' The model's reading is defensible, no write happened.
- **Scenario defects.** FJ-032 needs the retro content in the reader packet for Q3. FJ-027's Q3 answer says at least one payment while the model, agreed in turn 1, draws zero or more.
- **FJ-027 label risk, not scored.** 'is reserved by (1 to 0..n)' reads from Room to Booking. Labelling from Booking's side would remove the ambiguity.
- **FJ-019 reply.** A sentence precedes the board URL in turn 5, so the URL is not the first line. Unscored here.
- **Hygiene.** No export file, no edit call after any compose and a temp folder removed in every delivery. FJ-032's Hygiene rests on the single composing call because the existing nodes were not read again.

Verdict counts: five PASS and one FAIL. Evidence paths are in the jsonl.
