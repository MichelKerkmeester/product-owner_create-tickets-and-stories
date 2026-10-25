---
title: "Playbook run: first glance and routing on Claude Sonnet 5.5 high"
description: "The 18 Flow scenarios rerun on the skill after its first-glance and routing pass, through the Claude Code CLI with an operator driver that answers intake rounds as the playbook says."
trigger_phrases:
  - "first glance and routing playbook run"
  - "figjam rerun after first glance fixes"
importance_tier: "normal"
contextType: "general"
---

# Playbook run: first glance and routing on Claude Sonnet 5.5 high

The same 18 Flow scenarios as the rerun in `../2026-10-24--manual-testing-playbook--swe-2-max-composed-boards/` Section 10, run on 2026-10-25 against the skill after its first-glance and routing pass. 11 pass and 7 fail, against 2 pass and 16 fail in that rerun. No scenario moved down.

---

## 1. How it ran

- **Model and runtime:** `claude-sonnet-5-5` at effort high through the Claude Code CLI, with Figma's hosted MCP server and one fresh sandbox per scenario, three scenarios at a time (`run/run_adaptive_batch.sh`)
- **Driver:** `run/adaptive_scenario.py` sends each scenario's scripted turns in order. When a reply is an intake round it first sends "Use your recommended answers.", at most twice, as each scenario's command list and playbook Section 4 tell the operator to. A small classifier labels each reply's stop, kept as `kind` in `meta.json`, and the label is a hint that graders checked against the reply
- **Supplementary turns:** FJ-036 stopped at each proposal of the outline pass, so after its scripted turns the operator sent "Yes, go ahead." four more times to reach the write (`turn-supplementary-1.md` to `turn-supplementary-4.md`, `run/extra_turn.py`)
- **Test file:** one fictional FigJam file shared by every scenario and not cleared between them. FJ-031 deleted its own setup board after its own yes
- **Evidence:** per scenario under `skill/<ID> - <slug>/` (transcript, events, reply and `meta.json` per turn) and `replies/`. Board screenshots were rendered through the Figma REST API after the run and are not kept here

---

## 2. Grading

Three Sonnet 5.5 high graders read the evidence and the screenshots against the current scenario files and the skill contract (`grades/grader-brief-035.md`), six scenarios each. A fresh reader answered each board's questions from the colour screenshots alone (`grades/r035-reader-answers.md`, key `grades/r035-reader-answer-key.txt`). A fourth Sonnet 5.5 high pass scored Composition alone from the overview and greyscale images (`grades/g8-035-composition-second-lens.md`). Every row is in `results.jsonl` with its scorecard, losses, signals, the change against the earlier grade and the second Composition score.

| Scenario | Verdict | Total | Before | What decided it |
| --- | --- | --- | --- | --- |
| FJ-017 | PASS | unscored | PASS | Stops held and two `use_figma` calls wrote the board and its stickies |
| FJ-019 | PASS | unscored | PASS | Stops held and every part sits in its lane |
| FJ-022 | PASS | 21 | FAIL 21 | Composition now full, the goal reads first under the pink outline |
| FJ-023 | FAIL | 21 | FAIL 20 | The reply opens with a sentence before the board URL |
| FJ-024 | PASS | 19 | FAIL 20 | The accent is on the sync service, one crossing remains |
| FJ-025 | FAIL | 19 | FAIL 20 | The Mermaid model and two composed scripts were left in a temporary folder |
| FJ-026 | FAIL | 19 | FAIL 17 | The gate planned three gray end states as the first glance, the blue first state reads first |
| FJ-027 | PASS | 20 | FAIL 17 | The ER board reads in its planned order |
| FJ-028 | PASS | 21 | FAIL 21 | The reply now ends on the self-scan |
| FJ-029 | PASS | 20 | FAIL 19 | Both split boards landed with ordinal titles |
| FJ-030 | FAIL | 20 | FAIL 20 | The blue stickies and pins read before the green goal |
| FJ-031 | PASS | 21 | FAIL 21 | The revision opens with a playback and deletes the old board on its own yes |
| FJ-032 | FAIL | 19 | FAIL 19 | The same gray end state plan as FJ-026 |
| FJ-033 | FAIL | 19 | FAIL unscored | A board now exists, but Apple's push service was dropped and Clarity is 0 |
| FJ-034 | PASS | 21 | FAIL 20 | Colour stays with kind, three lanes and one accent |
| FJ-036 | PASS | 20 | FAIL 17 | No crossing and every exit label reads, written after the gate's own yes |
| FJ-039 | PASS | unscored | FAIL | Three intake rounds inside the cap, then a gate that waits |
| FJ-041 | FAIL | unscored | FAIL | The first reply asked three questions where the type mismatch comes first and alone |

---

## 3. What the run found and what changed after it

The findings below were checked against the files before anything changed. Each change landed in the skill source and in its Project mirror where one exists, and the composer self-test (815 of 815), the flow check self-test (158 of 158) and the 15 benchmark gates pass after them.

- **A bend on another line went unseen.** On FJ-019 and FJ-024 the dashed edge out of the event stream runs down the very line where the store edge bends, so it reads as a crossing. Both the router and the geometry check compared runs strictly, so a corner exactly on another line passed. A touch now counts as a crossing unless both edges end there or merge into one magnet, and the two boards recompose with no crossing
- **The key drew `In focus` as a pink fill.** The accent is a pink outline over the node's own kind, so on a green goal or a white entity the key and the board disagreed. The key sample is now drawn as the marked node is
- **The outline pass contradicted itself.** It said each proposal waits for a yes and also that an unanswered proposal never stops the run, and FJ-036 stopped at all four. The outline, framings and look now ride in the playback and the sketch is the model the gate shows, so the stops stay intake, playback and gate
- **The gate could come before the playback.** Section 8 said the reply to an intake answer is the gate whenever the gate had not been shown. It is now the playback until the playback has its answer
- **A first glance could be a group.** FJ-026 and FJ-032 planned three end states as the first glance with no focus line. The rubric and the style guide now say a first glance is one node, marked with a `%% focus:` line when the layout would show another first
- **The cleanup rule had two strengths.** `SKILL.md` said no Mermaid file in the repository, while `flow-mode.md` deletes the temporary model once the reply is sent. `SKILL.md` now says the same as `flow-mode.md`
- **Scenario text had gone stale.** FJ-019 named the old lane order, FJ-023 a violet focus step, FJ-022, FJ-030 and FJ-031 exactly 9 nodes where the remove test may cut, and FJ-029 one read-back line per diagram. Each now matches the skill

Model misses, with no contract change: FJ-023's opening sentence, FJ-025's leftover files and its declined path drawn as a board, FJ-033 letting a context page override the user's own statement and FJ-041's three questions.

---

## 4. Open

- **The ER detour on FJ-027.** "is booked under" leaves the top of Booking and runs about 1,600 pixels round both zones, because Booking's four magnets are each taken and a departing edge may not share one. It costs no scorecard point, so it is recorded as a composer limit rather than changed on inference
- **The recheck on the changed skill** (`recheck/`, graded in `grades/g9-035-recheck.md`) reran the six scenarios the changes touched: FJ-019, FJ-024, FJ-026, FJ-027 and FJ-036 pass, each scored board at Composition 2, and FJ-036 reached its write with no supplementary turn. FJ-032 still fails at 20 with Composition 1, because the gray end states read before the event labels the gate planned second. Clarity in the recheck was read by its grader from the screenshots, not by a fresh reader. FJ-023, FJ-025, FJ-030, FJ-033 and FJ-041 were not rerun
- **The second recheck** (`recheck2/`, graded in `grades/g10-035-fj032.md` and `grades/g11-035-fj030.md`, reader answers in `grades/r032-reader-answers.md` and `grades/r030-reader-answers.md`) ran after a further round of contract fixes: the gate now plans the end states second, a multi-word state takes its readable name, the read-back compares nodes that were on the file before the write, and the ER and existing-board scenarios match the skill. FJ-032 passes at 22 of 22. FJ-030 still fails at 21 with Composition 1, because the wide orange Request the return zone and its yellow diamonds read before the pink-ringed Return confirmed in the narrow Done zone. Its grader called that close to a tie on one reader, and the second lens of the main run had scored the same plan 2, so the operator waived it in the phase's decision record rather than change the zone tints on every zoned board. Tinting only the first-glance zone stays a candidate for a later pass
- **Redaction:** board URLs, the file key, plan names and emails in this folder are redacted with `run/redact_run.py` before any commit
