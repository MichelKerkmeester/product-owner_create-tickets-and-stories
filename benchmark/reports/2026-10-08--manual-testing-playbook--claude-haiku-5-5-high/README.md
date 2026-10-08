---
title: "Playbook run: Claude Haiku 5.5 high on kernel v1.1.0 and Skill v1.1.0.0"
description: "The full 46-scenario playbook on Haiku 5.5 at high effort after the Story and Epic changes, with the new Story rules checked on every Story and Epic deliverable and the turn-2 asks sampled against HEAD."
trigger_phrases:
  - "haiku 5.5 playbook run"
  - "story problem and rule check"
importance_tier: "normal"
contextType: "general"
---

# Playbook run: Claude Haiku 5.5 high on kernel v1.1.0 and Skill v1.1.0.0

This run checks whether a model follows the Story and Epic changes in kernel v1.1.0 and Skill v1.1.0.0: no intro lines, `## Problem` in three to five sentences, one outcome per Then or And line, and no Delivery helper sentences. Every new Story and Epic followed all four. Three scenarios asked again on Turn 2 instead of drafting, and HEAD samples show that is mostly Haiku's behavior on both versions.

---

## 1. Verdict on the new rules

Fifteen new Stories and Epics were checked: eight skill exports and seven Project replies, the PST-004 bundle Story among them.

- **No intro lines** in any of them
- **Every Story opens on `## Problem`**, three or four sentences, and every Epic keeps `## About`
- **No Then or And line joins a second outcome with ", and"**, out of 136 Then and And lines. Thirteen of the lines outside PST-004 carry a plain "and", all noun pairs or one subject doing two linked things, such as "turns the filter off and reruns the same search". None has the screenshot's shape, where ", and" opens a second outcome with a new subject
- **No Delivery helper sentence** anywhere

The refinement scenarios produced no Story to check, because they asked again on Turn 2 (section 3).

---

## 2. Run integrity

- The first runner process stopped after 31 of 46 scenarios when the session ended. The other 15 ran in `resume-1/` against the same unchanged working tree, HEAD `ac57adb`
- `combined/` holds the 31 finished scenario folders from the first process and the 15 from `resume-1/`, the 46-scenario `manifest.json`, and a `run-status.json` built from the per-scenario status lines both processes printed
- `python3 run/check_run.py combined --model claude-haiku-5-5 --effort high` exits 0: 46 scenarios, 86 declared turns, 86 event streams read, 0 findings

---

## 3. Turn 2 asked again instead of drafting

SST-003, PST-003 and PEP-002 each asked a second question on Turn 2, which fails their pass line. Each ran three times on v1.1.0 and three times on HEAD, using a `git archive` copy of HEAD:

- **PST-003:** asked in 3 of 3 on v1.1.0 and 3 of 3 on HEAD
- **SST-003:** asked in 3 of 3 on v1.1.0 and 2 of 3 on HEAD
- **PEP-002:** asked in 1 of 3 on v1.1.0 and 0 of 3 on HEAD

On both versions Haiku asks again on the refinement scenarios, so v1.1.0 did not introduce the behavior. Three samples per side cannot rule out a small shift. The samples are in `sample-new-2/`, `sample-new-3/`, `baseline-head/`, `sample-head-2/` and `sample-head-3/`, and each passes `check_run.py` apart from the scenarios it was not asked to run.

---

## 4. Voice and format

- `benchmark/grader/lint_replies.py combined` reports 44 of 86 replies with a Human Voice hard blocker, 201 of them a bullet ending in a full stop. The 2026-09-25 runs on the same lint had 78 of 86 (Opus 5.5) and 16 of 28 (Sonnet 5)
- The format gate over every skill deliverable fails on one file, the SBG-003 bug, with 15 bullets ending in a full stop. No deliverable gets the joined-outcome advice

---

## 5. Exports

`run/collect_exports.py combined ../../../export/benchmark --force` wrote 43 deliverables over the earlier set, on the operator's choice. Opus files with no Haiku counterpart stay beside them. The collector in `run/` was corrected before collecting: it checked the clarification suffix after adding the `(turn 2)` suffix, so a second-round clarification would have been published. It now checks first, and `export/benchmark/` holds no clarification file.

---

## 6. Criterion numbering, added after the main run

The operator then asked for criteria numbered `1 ) **{Title}**`. `ac-numbering/` reran SST-001, PST-001, SEP-003 and PEP-003 on the updated sources. All 22 criteria across the four deliverables open `N ) **`, none uses an older form and none joins outcomes with ", and". `check_run.py` reports no finding beyond the 42 scenarios that folder did not run. Those four deliverables replaced their copies in `export/benchmark`. The other Story and Epic deliverables there still show `1\.`, because they predate the rule.

`ac-numbering-2/` then reran the remaining twelve Story and Epic scenarios. The ten that drafted carry 51 criteria, all opening `N ) **`, with no ", and" join, no intro line, no helper sentence and every Story on a three-to-five-sentence Problem. SEP-002 and PEP-002 asked again on Turn 2, so the natural-wording Epic has now asked again in 2 of 4 v1.1.0 Project runs. Collecting this batch exposed a second clarification-naming gap: the Project runtime named a second round `-clarification-2.md`, the collector published it, and it was removed by hand. The collector now treats any `-clarification` or `-clarification-N` name as a clarification.

---

## 7. Not done

No per-scenario PASS or FAIL verdict was graded for the 43 other scenarios, so there is no `results.csv`. Sections 1 to 4 cover what this change touches.
