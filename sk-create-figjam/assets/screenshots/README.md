---
title: "sk-create-figjam - Board Screenshots"
description: "Overview renders of real FigJam boards the skill composed, one per diagram type plus two harder writes, each with the playbook scenario and scorecard result it came from."
trigger_phrases:
  - "figjam board screenshots"
  - "figjam gallery"
  - "sk-create-figjam examples images"
version: 1.0.14.0
---

# sk-create-figjam - Board Screenshots

> Overview renders of boards this skill composed, kept as a reference for what a finished board looks like.

---

## 1. OVERVIEW

The skill composed every board here on a fictional test file, with invented brands such as Roamstay, Loomlist and Fernhouse. Each board was then rendered through the Figma REST API as an overview image with its longest edge at 2048 px or less. Each one was graded on the 22-point board scorecard in [`../../manual-testing-playbook/manual-testing-playbook.md`](../../manual-testing-playbook/manual-testing-playbook.md).

The seven type boards and the dense flow come from the [model comparison run](../../../benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/README.md). On 2026-10-26 Claude Sonnet 5.5 high ran again the 31 scenarios its first run did not pass, plus FJ-022, FJ-023 and FJ-028 for the gallery, with the v1.0.6.0 composer and the design file `../figjam-design.md`. One Opus grader scored every board on the 22-point scorecard, and skeptics and an adjudicator checked each verdict. One judge then picked the best board of each type: the type shown most fully and the faster read first, then the total. The process and state images come from failing runs, because no board of either type passed. Each caption names the scenario, the model and the score, and says why a failing run failed. The existing-board image is older, because the rerun's FJ-032 board scored lower. On 2026-10-27 the same model ran the scenarios that still failed again on v1.0.7.0, and the same judge rule replaced only the process image, with the FJ-023 board from that run. On 2026-10-27 it ran them once more on v1.0.8.0, and the same rule replaced only the state image, with that run's FJ-026 board, which scores 21 where the earlier one scored 20. On 2026-10-28 a rerun on v1.0.13.0 replaced the user flow image with that run's FJ-022 board, which passes at the same 21 with the accent on the 30-day decision rather than on the goal. A second rerun that day, on v1.0.14.0, replaced the process image with that run's FJ-023 board, which scores the same 21 and reads straighter. The last rerun, on v1.0.15.0, replaced it again with that run's FJ-023 board, which scores 22 and draws the warehouse queue as a line label. On 2026-10-29 the status lane board joined as the one image not taken from a graded run.

---

## 2. IMAGES

- [`user-flow-board.png`](user-flow-board.png): user flow, from [FJ-022](../../manual-testing-playbook/board-quality/user-flow-board-quality.md), Claude Sonnet 5.5 high on v1.0.13.0, 21 of 22, PASS. The 30-day decision carries the pink outline, the confirmation is the green goal and Contact support sits below the row beside Pick a reason, so the main row runs straight. The point lost is Legibility, where `courier?` stands alone on the last line of the method decision
- [`process-board.png`](process-board.png): laned process, from [FJ-023](../../manual-testing-playbook/board-quality/process-board-quality.md), Claude Sonnet 5.5 high on v1.0.15.0, 22 of 22, FAIL. The board loses no point and both readers read the pink Approve the claim step first. The run fails on its turn 1 intake round, which adds a sentence about the write target after its closing question. The warehouse queue is the Claim queued label on the line from Approve the claim to Book a courier, so every step keeps its lane. It replaced the v1.0.14.0 FJ-023 board, which scored 21 and drew the queue as a store
- [`process-status-lane-board.png`](process-status-lane-board.png): laned process with a status lane and detail cards, the worked example [`process-fernhouse-commission.md`](../examples/process-fernhouse-commission.md) composed once with the v1.0.16.0 composer on 2026-10-29 to check that release, and not graded on the scorecard. Its read-back counted 15 of 15 nodes and 20 of 20 connectors with 0 warnings, taken from a view rendered after the last write. The dotted moves into Confirmed and In the making share one run above the Maker lane, because the check measures crossings on the work alone
- [`architecture-board.png`](architecture-board.png): architecture, from [FJ-024](../../manual-testing-playbook/board-quality/architecture-board-quality.md), Claude Sonnet 5.5 high, 22 of 22, PASS
- [`sequence-board.png`](sequence-board.png): sequence, from [FJ-025](../../manual-testing-playbook/board-quality/sequence-board-quality.md), Claude Sonnet 5.5 high, 22 of 22, PASS
- [`state-board.png`](state-board.png): state diagram, from [FJ-026](../../manual-testing-playbook/board-quality/state-board-quality.md), Claude Sonnet 5.5 high on v1.0.11.0, 22 of 22, PASS. Pending starts on the left, Upcoming and In stay sit inside the Confirmed composite and the three end states stand in one column, with Cancelled in the pink outline as the end state two statuses lead to. The plan follows the board as drawn, and both readers take Cancelled first among the end states
- [`er-board.png`](er-board.png): ER diagram, from [FJ-027](../../manual-testing-playbook/board-quality/er-board-quality.md), Claude Sonnet 5.5 high, 21 of 22, PASS. The point lost is Clarity, because the reader missed that a booking reserves one room. The board carries key columns only, because the driver never supplied the schema note
- [`gantt-board.png`](gantt-board.png): gantt chart, from [FJ-028](../../manual-testing-playbook/board-quality/gantt-board-quality.md), Claude Sonnet 5.5 high, 20 of 22, PASS. It loses one Shared trunks point where two arrowheads crowd into Desktop and iOS integration, and one Clarity point because the reader named the critical chain instead of Integration
- [`state-on-existing-board.png`](state-on-existing-board.png): state diagram written onto a board that already held content, from [FJ-032](../../manual-testing-playbook/board-creation/existing-board-with-content.md) on its second recheck, 22 of 22, drawn again in the design file before v1.0.6.0. The rerun's FJ-032 board scored 19 and failed on Composition and Reply, so this image stays
- [`dense-flow-board.png`](dense-flow-board.png): user flow at the 9-node budget with a three-way decision, from [FJ-036](../../manual-testing-playbook/board-creation/dense-flow-at-budget.md), Claude Sonnet 5.5 high, 21 of 22, FAIL. The drawing keeps both Composition points with no crossing, and the run fails only on its reply, which opened on a cleanup line instead of the board URL. The Picks a room and Yes lines still arrive close together at the price decision, as they did on the older board

---

## 3. RELATED

- [`../../README.md`](../../README.md) shows these boards in its gallery with a caption for each
