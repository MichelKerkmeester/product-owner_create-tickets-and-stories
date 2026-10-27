---
title: "sk-create-figjam - Board Screenshots"
description: "Overview renders of real FigJam boards the skill composed, one per diagram type plus two harder writes, each with the playbook scenario and scorecard result it came from."
trigger_phrases:
  - "figjam board screenshots"
  - "figjam gallery"
  - "sk-create-figjam examples images"
version: 1.0.6.0
---

# sk-create-figjam - Board Screenshots

> Overview renders of boards this skill composed, kept as a reference for what a finished board looks like.

---

## 1. OVERVIEW

The skill composed every board here on a fictional test file, with invented brands such as Roamstay, Loomlist and Fernhouse. Each board was then rendered through the Figma REST API as an overview image with its longest edge at 2048 px or less. Each one was graded on the 22-point board scorecard in [`../../manual-testing-playbook/manual-testing-playbook.md`](../../manual-testing-playbook/manual-testing-playbook.md).

The seven type boards and the dense flow come from the [model comparison run](../../../benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/README.md). On 2026-10-26 Claude Sonnet 5.5 high ran again the 31 scenarios its first run did not pass, plus FJ-022, FJ-023 and FJ-028 for the gallery, with the v1.0.6.0 composer and the design file `../figjam-design.md`. One Opus grader scored every board on the 22-point scorecard, and skeptics and an adjudicator checked each verdict. One judge then picked the best board of each type: the type shown most fully and the faster read first, then the total. The process and state images come from failing runs, because no board of either type passed. Each caption names the scenario, the model and the score, and says why a failing run failed. The existing-board image is older, because the rerun's FJ-032 board scored lower.

---

## 2. IMAGES

- [`user-flow-board.png`](user-flow-board.png): user flow, from [FJ-022](../../manual-testing-playbook/board-quality/user-flow-board-quality.md), Claude Sonnet 5.5 high, 21 of 22, PASS. The point lost is Legibility, where Order detail (Start a return) wraps inside its parenthesis
- [`process-board.png`](process-board.png): laned process, from [FJ-034](../../manual-testing-playbook/board-creation/colour-every-team-restraint.md), Claude Sonnet 5.5 high, 21 of 22, FAIL. The run fails on Composition, because the green Refund released goal reads before the Approved exit and the second-photo loop it planned as the second glance. The FJ-023 board scored 18
- [`architecture-board.png`](architecture-board.png): architecture, from [FJ-024](../../manual-testing-playbook/board-quality/architecture-board-quality.md), Claude Sonnet 5.5 high, 22 of 22, PASS
- [`sequence-board.png`](sequence-board.png): sequence, from [FJ-025](../../manual-testing-playbook/board-quality/sequence-board-quality.md), Claude Sonnet 5.5 high, 22 of 22, PASS
- [`state-board.png`](state-board.png): state diagram, from [FJ-026](../../manual-testing-playbook/board-quality/state-board-quality.md), Claude Sonnet 5.5 high, 20 of 22, FAIL. All three state boards the rerun drew scored 20, and this one reads fastest, with a composite Confirmed state and no crossing. The run fails on two points: no accent leads to the end states the request asked about, and its read-back line claimed a visual read that never ran
- [`er-board.png`](er-board.png): ER diagram, from [FJ-027](../../manual-testing-playbook/board-quality/er-board-quality.md), Claude Sonnet 5.5 high, 21 of 22, PASS. The point lost is Clarity, because the reader missed that a booking reserves one room. The board carries key columns only, because the driver never supplied the schema note
- [`gantt-board.png`](gantt-board.png): gantt chart, from [FJ-028](../../manual-testing-playbook/board-quality/gantt-board-quality.md), Claude Sonnet 5.5 high, 20 of 22, PASS. It loses one Shared trunks point where two arrowheads crowd into Desktop and iOS integration, and one Clarity point because the reader named the critical chain instead of Integration
- [`state-on-existing-board.png`](state-on-existing-board.png): state diagram written onto a board that already held content, from [FJ-032](../../manual-testing-playbook/board-creation/existing-board-with-content.md) on its second recheck, 22 of 22, drawn again in the design file before v1.0.6.0. The rerun's FJ-032 board scored 19 and failed on Composition and Reply, so this image stays
- [`dense-flow-board.png`](dense-flow-board.png): user flow at the 9-node budget with a three-way decision, from [FJ-036](../../manual-testing-playbook/board-creation/dense-flow-at-budget.md), Claude Sonnet 5.5 high, 21 of 22, FAIL. The drawing keeps both Composition points with no crossing, and the run fails only on its reply, which opened on a cleanup line instead of the board URL. The Picks a room and Yes lines still arrive close together at the price decision, as they did on the older board

---

## 3. RELATED

- [`../../README.md`](../../README.md) shows these boards in its gallery with a caption for each
