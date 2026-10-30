---
title: "sk-create-figjam - Board Screenshots"
description: "Overview renders of real FigJam boards the skill composed, one per diagram type plus two harder writes, each with the playbook scenario and scorecard result it came from."
trigger_phrases:
  - "figjam board screenshots"
  - "figjam gallery"
  - "sk-create-figjam examples images"
version: 1.0.17.0
---

# sk-create-figjam - Board Screenshots

> Overview renders of boards this skill composed, kept as a reference for what a finished board looks like.

---

## 1. OVERVIEW

The skill composed every board here on a fictional test file, with invented brands such as Roamstay, Loomlist and Fernhouse. Each board was then rendered through the Figma REST API as an overview image with its longest edge at 2048 px or less. Each one was graded on the board scorecard in [`../../manual-testing-playbook/manual-testing-playbook.md`](../../manual-testing-playbook/manual-testing-playbook.md).

The seven type boards and the dense flow come from the [model comparison run](../../../benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/README.md). On 2026-10-26 Claude Sonnet 5.5 high ran again the 31 scenarios its first run did not pass, plus FJ-022, FJ-023 and FJ-028 for the gallery, with the v1.0.6.0 composer and the design file `../figjam-design.md`. One Opus grader scored every board on the 22-point scorecard, and skeptics and an adjudicator checked each verdict. One judge then picked the best board of each type: the type shown most fully and the faster read first, then the total. The process and state images come from failing runs, because no board of either type passed. Each caption names the scenario, the model and the score, and says why a failing run failed. The existing-board image is older, because the rerun's FJ-032 board scored lower. On 2026-10-27 the same model ran the scenarios that still failed again on v1.0.7.0, and the same judge rule replaced only the process image, with the FJ-023 board from that run. On 2026-10-27 it ran them once more on v1.0.8.0, and the same rule replaced only the state image, with that run's FJ-026 board, which scores 21 where the earlier one scored 20. On 2026-10-28 a rerun on v1.0.13.0 replaced the user flow image with that run's FJ-022 board, which passes at the same 21 with the accent on the 30-day decision rather than on the goal. A second rerun that day, on v1.0.14.0, replaced the process image with that run's FJ-023 board, which scores the same 21 and reads straighter. The last rerun, on v1.0.15.0, replaced it again with that run's FJ-023 board, which scores 22 and draws the warehouse queue as a line label. On 2026-10-29 Claude Sonnet 5.5 medium ran the nine gallery scenarios and the new FJ-049 on v1.0.16.0, graded as in [section 8.16 of the run report](../../../benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/README.md). A new board replaced its image only when it scored at least as high, which replaced the sequence, ER, gantt, existing-board and status lane images. On 2026-10-30 the same model ran the gallery scenarios on v1.0.17.0, each with a source excerpt and two source questions that score Substance on a 24-point card, graded as in [section 8.17 of the run report](../../../benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/README.md). Every image but the status lane now comes from that run whatever it scored, so the gallery shows the current design. The status lane image stays, because that run's graded FJ-049 board drew no lane.

---

## 2. IMAGES

- [`user-flow-board.png`](user-flow-board.png): user flow, from [FJ-022](../../manual-testing-playbook/board-quality/user-flow-board-quality.md), Claude Sonnet 5.5 medium on v1.0.17.0, 22 of 24, FAIL. Zone notes and detail cards carry the four return reasons, the 5 nearest drop-off points and the 3 working day pickup window, and Substance scores 2. Composition scores 0 because both readers took the green goal, the orange Contact support exit and the second decision before the planned order reached them
- [`process-board.png`](process-board.png): laned process, from [FJ-023](../../manual-testing-playbook/board-quality/process-board-quality.md), Claude Sonnet 5.5 medium on v1.0.17.0, 24 of 24, PASS. Lane notes carry the help form fields, the one working day CS answer and the 5 working day refund, and two detail cards carry the pickup and the inspection
- [`process-status-lane-board.png`](process-status-lane-board.png): laned process with a status lane and detail cards, from [FJ-049](../../manual-testing-playbook/board-quality/status-lane-board-quality.md), Claude Sonnet 5.5 medium on v1.0.16.0, 19 of 22, FAIL. Composition scores 0 because both readers took the green Claim closed goal and the orange Card charged exit before the planned order reached them, and Legibility loses a point to `days?` alone on the Accept within 7 days? diamond. It replaced the ungraded release-check board of the commission example
- [`architecture-board.png`](architecture-board.png): architecture, from [FJ-024](../../manual-testing-playbook/board-quality/architecture-board-quality.md), Claude Sonnet 5.5 medium on v1.0.17.0, 22 of 24, FAIL. Five detail cards say what each part does and keeps, including 30 days of block history and one wake-up per device per minute, and Substance scores 2. Composition scores 0 because the glance plan left out the three clients and the blocks database, which both readers read early. It is the run's third board, after the database card's body and the key's cylinder samples were fixed
- [`sequence-board.png`](sequence-board.png): sequence, from [FJ-025](../../manual-testing-playbook/board-quality/sequence-board-quality.md), Claude Sonnet 5.5 medium on v1.0.17.0, 22 of 24, FAIL. The run split the declined card into a second board and the image sets the two side by side. Message labels carry the 15 minute hold and what the booking post holds. Composition, scored by hand because a sequence prints no `Glance:` line, is 0
- [`state-board.png`](state-board.png): state diagram, from [FJ-026](../../manual-testing-playbook/board-quality/state-board-quality.md), Claude Sonnet 5.5 medium on v1.0.17.0, 22 of 24, FAIL. Detail cards carry the 15 minute Pending limit, the date change while Upcoming, the 6 hour No-show rule and the first night kept on a late cancel. Composition is 0 because the plan put the focused Cancelled state last and both readers read it first, which the grader traces to the rubric naming the first state as a state board's first glance
- [`er-board.png`](er-board.png): ER diagram, from [FJ-027](../../manual-testing-playbook/board-quality/er-board-quality.md), Claude Sonnet 5.5 medium on v1.0.17.0, 22 of 24, FAIL. Substance scores 1 because the three payment statuses sat in a column comment the composer does not draw, and Fidelity loses a point for the same row
- [`gantt-board.png`](gantt-board.png): gantt chart, from [FJ-028](../../manual-testing-playbook/board-quality/gantt-board-quality.md), Claude Sonnet 5.5 medium on v1.0.17.0, 22 of 24, PASS. Task names carry the sync engine's owner and the integration's platforms. It loses a Shared trunks point where two arrows meet the integration bar and a Clarity point where the critical marking covers three tasks
- [`state-on-existing-board.png`](state-on-existing-board.png): state diagram written onto a board that held a Sprint retro section of six stickies, from [FJ-032](../../manual-testing-playbook/board-creation/existing-board-with-content.md), Claude Sonnet 5.5 medium on v1.0.17.0, 24 of 24, PASS. The image is the whole page, so the untouched retro content shows beside the new section
- [`dense-flow-board.png`](dense-flow-board.png): user flow at the 9-node budget with a three-way decision, from [FJ-036](../../manual-testing-playbook/board-creation/dense-flow-at-budget.md), Claude Sonnet 5.5 medium on v1.0.17.0, 22 of 24, FAIL. Four detail cards carry the open nights, the 3 other rooms, the card on file and the 12 month credit. Composition scores 1 because both readers read the green goal early, and Shared trunks loses a point where two edges enter the price decision at one corner

---

## 3. RELATED

- [`../../README.md`](../../README.md) shows these boards in its gallery with a caption for each
