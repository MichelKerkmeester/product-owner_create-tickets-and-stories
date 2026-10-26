---
title: "sk-create-figjam - Board Screenshots"
description: "Overview renders of real FigJam boards the skill composed, one per diagram type plus two harder writes, each with the playbook scenario and scorecard result it came from."
trigger_phrases:
  - "figjam board screenshots"
  - "figjam gallery"
  - "sk-create-figjam examples images"
version: 1.0.3.0
---

# sk-create-figjam - Board Screenshots

> Overview renders of boards this skill composed, kept as a reference for what a finished board looks like.

---

## 1. OVERVIEW

The skill composed every board here on a fictional test file, with invented brands such as Roamstay, Loomlist and Fernhouse. Each board was then rendered through the Figma REST API as an overview image with its longest edge at 2048 px or less. Each one was graded on the 22-point board scorecard in [`../../manual-testing-playbook/manual-testing-playbook.md`](../../manual-testing-playbook/manual-testing-playbook.md).

The seven type boards come from the [three-model comparison](../../../benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/README.md), which ran each board-quality scenario on DeepSeek V4.1 Flash Max, GLM 5.3 Flash Max and SWE 2 Max with the design file `../figjam-design.md`. Each image is the best of the three: the most of the 16 points the two zooms score, then the highest total, then a pass, then the grader's rank. Four images were drawn again on 2026-10-26 from the model their best run checked, with the v1.0.4.0 composer and the shipped design file. The gantt and ER boards now show the dependency arrows and the end marks the run's composer lacked, and the last two boards came from earlier runs drawn before the design file. Each caption keeps the score its run gave the original board, and no grader scored the redraws.

---

## 2. IMAGES

- [`user-flow-board.png`](user-flow-board.png): user flow, from [FJ-022](../../manual-testing-playbook/board-quality/user-flow-board-quality.md), GLM 5.3 Flash Max, 22 of 22
- [`process-board.png`](process-board.png): laned process, from [FJ-023](../../manual-testing-playbook/board-quality/process-board-quality.md), SWE 2 Max, 20 of 22. The board takes all 16 points of the two zooms, the most of any FJ-023 board. The run itself fails its PASS line on two points that are not the drawing: its reply opens with prose before the board URL and it left its model and compose files in the temporary folder
- [`architecture-board.png`](architecture-board.png): architecture, from [FJ-024](../../manual-testing-playbook/board-quality/architecture-board-quality.md), SWE 2 Max, 22 of 22
- [`sequence-board.png`](sequence-board.png): sequence, from [FJ-025](../../manual-testing-playbook/board-quality/sequence-board-quality.md), GLM 5.3 Flash Max, 22 of 22
- [`state-board.png`](state-board.png): state diagram, from [FJ-026](../../manual-testing-playbook/board-quality/state-board-quality.md), GLM 5.3 Flash Max, 22 of 22
- [`er-board.png`](er-board.png): ER diagram, from [FJ-027](../../manual-testing-playbook/board-quality/er-board-quality.md), SWE 2 Max, 22 of 22, drawn again with its end marks
- [`gantt-board.png`](gantt-board.png): gantt chart, from [FJ-028](../../manual-testing-playbook/board-quality/gantt-board-quality.md), GLM 5.3 Flash Max, 22 of 22, drawn again with its dependency arrows
- [`state-on-existing-board.png`](state-on-existing-board.png): state diagram written onto a board that already held content, from [FJ-032](../../manual-testing-playbook/board-creation/existing-board-with-content.md) on its second recheck, 22 of 22, drawn again in the design file
- [`dense-flow-board.png`](dense-flow-board.png): user flow at the 9-node budget with a three-way decision, from [FJ-036](../../manual-testing-playbook/board-creation/dense-flow-at-budget.md) on its recheck, 21 of 22. Drawn again in the design file after two changes the current check asks for: the one accent stays on the price decision and the credit label is shortened to Difference back as credit (automatic). The point the recheck lost is the Pick a room line joining the Yes line just before the price decision, which the redraw keeps

---

## 3. RELATED

- [`../../README.md`](../../README.md) shows these boards in its gallery with a caption for each
