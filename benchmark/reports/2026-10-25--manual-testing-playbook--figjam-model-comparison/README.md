---
title: "Playbook run: FigJam boards on DeepSeek V4.1 Flash Max, GLM 5.3 Flash Max and SWE 2 Max"
description: "The seven board-quality scenarios run on three models through the Devin CLI against the phase 037 design file, every board graded on the 22-point scorecard by a neutral grader, with the best model per type and overall."
trigger_phrases:
  - "figjam model comparison"
  - "deepseek glm swe figjam"
  - "best model for figjam boards"
importance_tier: "important"
contextType: "general"
---

# Playbook run: FigJam boards on DeepSeek V4.1 Flash Max, GLM 5.3 Flash Max and SWE 2 Max

This run asks which model drives Flow Mode to the best FigJam board. The seven board-quality scenarios, FJ-022 to FJ-028, ran once on each of three models against the composer and design file phase 037 shipped. All 21 runs finished and 21 boards were graded by fresh Claude Sonnet 5.5 graders. Every model passed five of seven scenarios on the scenarios' own PASS lines, once one Reply point was reconciled (section 6.2).

---

## 1. Verdict

**GLM 5.3 Flash Max and SWE 2 Max tie on board quality. SWE 2 Max is the safer model and the one to use.**

| Model | Total of 154 | Passes | Strict passes | First places | Gallery boards | Wall time | Output tokens |
|---|---|---|---|---|---|---|---|
| GLM 5.3 Flash Max | 148 | 5 | 5 | 4 | 4 | 57.9 min | 699,669 |
| SWE 2 Max | 148 (147 as graded) | 5 (4 as graded) | 4 | 2 | 3 | 59.5 min | 361,566 |
| DeepSeek V4.1 Flash Max | 144 | 5 | 3 | 1 | 0 | 30.6 min | 474,256 |

- **Passes** follow each scenario's PASS line as it read when the run was graded, the scorecard alone. **Strict passes** add the root playbook's rule that any missing expected signal fails a run. Every board-quality and board-creation PASS line now carries that rule too, so the strict column applies it to the signals as they were graded. FJ-027's end-mark signal and FJ-028's dependency-arrow signal were added after the run and are not scored on it (section 6.3)
- **First places** count the grader's rank 1 in each type. The rank orders the three boards of one scenario on one scale
- **SWE as graded** differs by one Reply point on FJ-022, reconciled in section 6.2

**What decided it.** GLM drew the best boards most often. It won four of seven types, met every expected signal on FJ-025 and proved "nothing else changed" with before and after page reads. It also committed the two worst faults of the batch. On FJ-024 it wrote the board in turn 1 with no gate, then took the script's generic "Yes, go ahead." as a yes to its own offer and deleted ten boards it never created, two of them this batch's other FJ-024 boards. On FJ-023 every `use_figma` call left out the file key, so no compose ran and the board is a bare `generate_diagram` drawing. SWE never wrote before a gate and never changed a node it did not create. Its losses are a reply that opens with prose (FJ-023 and FJ-026), temporary files left in `/tmp` (FJ-023 and FJ-026), a Finding that undercounts earlier boards (FJ-022), an unrequested second board (FJ-025) and em dashes and semicolons in two stop replies (FJ-028). Every SWE loss leaves the user's file as it was, and GLM's delete did not.

The recommendation is judgment, not a measured score. A reader who weights the drawing above conduct would pick GLM, which wins on rank and on the strict rule. Flow Mode now deletes only on a reply that names the boards, which closes the gap GLM's delete showed (section 7). DeepSeek is third on total, strict passes and first places. It is about twice as fast, but it wrote before the gate twice (FJ-026 and FJ-027), edited a composed board by hand (FJ-027) and put the accent on the wrong step (FJ-023).

---

## 2. Run integrity

| Model | Devin model id | Runs | Turns | Retries | Figma calls |
|---|---|---|---|---|---|
| DeepSeek V4.1 Flash Max | `deepseek-v4-1-flash-1017-max` | 7 | 21 | FJ-025 once, an empty reply on turn 1 | 52 |
| GLM 5.3 Flash Max | `glm-5-3-flash-max` | 7 | 21 | FJ-023 twice, an error on turn 3 | 66 |
| SWE 2 Max | `swe-2-max` | 7 | 21 | none | 32 |

- **Runtime.** Devin 3000.11.205 (6dea39440ae3), permission mode `dangerous` inside the runner's seatbelt sandbox, with Figma's hosted MCP server. Every turn's `response_models` names the model the run asked for
- **Order.** One run at a time on one fictional test FigJam file, the three models back to back per scenario with the order rotated per scenario (`run/run_compare.sh`). The batch ran from 2026-10-25 to 2026-10-26 and logged 148.0 minutes of turn time
- **Driver.** `run/adaptive_compare.py` sends the scenario's scripted turns, adds "Use your recommended answers." after an intake round and "Yes, go ahead." when the script ends with no board. No run needed either, so every run used exactly the three scripted turns
- **Failed attempts** are kept in `failed-attempts/` beside the run that replaced them
- **Board ids** come from each compose call's result. Two runs have none in `meta.json`: GLM's FJ-023, which never composed, and DeepSeek's FJ-027, which ran the composer from a call that does not hold `const MODEL` (section 6.5). The driver now reads a board id from any `use_figma` result and finds DeepSeek's board in its export, but the batch ran on the earlier version. `grades/special-cases.md` lists every such fact the graders were given
- **Redaction.** Board URLs, the test file key, emails and plan names are redacted with `run/redact_run.py` before each commit, and a scan over every committed file found none. The runner's own pass, `figma\.com/\S+`, also took the text glued to a URL inside a JSON export, such as an escaped line break and the `Read-back:` after it, and once the closing quote, which left SWE's FJ-028 turn 3 export unparseable. The raw exports of the last run of each scenario were still on disk, so those 21 files were redacted again from raw with `redact_run.py`'s narrower pattern on 2026-10-26. The other 42 exports keep the loss. The replies, transcripts and grades were never affected, because they hold real line breaks the pattern stops at

---

## 3. Results

Each cell is the total of 22, the verdict on the scenario's PASS line and the grader's rank. A dagger marks the strict verdict where it differs.

| Scenario | DeepSeek | GLM | SWE | Gallery board |
|---|---|---|---|---|
| FJ-022 user flow | 22 PASS, 2 | 22 PASS, 1 | 21 PASS, 3 (graded 20 FAIL) | GLM 109:4426 |
| FJ-023 process | 20 PASS, 1 (FAIL†) | 17 FAIL, 3 | 20 FAIL, 2 | SWE 114:4602 |
| FJ-024 architecture | 22 PASS, 2 | 21 FAIL, 3 | 22 PASS, 1 | SWE 117:4812 |
| FJ-025 sequence | 22 PASS, 3 (FAIL†) | 22 PASS, 1 | 22 PASS, 2 (FAIL†) | GLM 122:4181 |
| FJ-026 state | 16 FAIL, 3 | 22 PASS, 1 | 19 FAIL, 2 | GLM 126:4597 |
| FJ-027 ER | 20 FAIL, 3 | 22 PASS, 2 | 22 PASS, 1 | SWE 132:5151 |
| FJ-028 gantt | 22 PASS, 2 | 22 PASS, 1 | 22 PASS, 3 | GLM 145:5350 |

`results.jsonl` holds one row per run with the scorecard, every lost point with its location and fix, every expected signal with its citation, the turns and the evidence paths. `run/aggregate.py` rebuilds it from `grades/`. Each grader's own summary is `grades/<ID>.md`.

**Per type, what separated the three**

- **FJ-022 user flow.** GLM and DeepSeek both score 22. GLM ranks first because a before and after page read proved its write added one section and nothing else. DeepSeek ran its check and compose before the playback was answered, though it wrote nothing then. SWE's "Within 30 days?" diamond wraps between the number and its unit
- **FJ-023 process.** No run is clean. DeepSeek and SWE both score 20, and DeepSeek ranks first only because it passes the PASS line: its accent sits on Book a courier pickup instead of Approve the claim. SWE drew the cleanest board, but its reply opens with prose and it left its model and compose files in `/tmp`. GLM's board has no title, key or kind colours (section 6.5)
- **FJ-024 architecture.** SWE and DeepSeek both score 22. SWE ranks first because it checked only after the playback's yes, showed the checked sketch at the gate and kept the request's labels. DeepSeek shortened two labels and changed the iOS edge from HTTPS to WebSocket after the gate without saying so. GLM wrote in turn 1 and deleted ten boards (section 6.4)
- **FJ-025 sequence.** All three score 22. GLM alone drew the partner hub message as an open-arrow async and named the declined path under `Left out:`. SWE drew a second board for the declined path that the request did not ask for. DeepSeek drew the async message with a closed head
- **FJ-026 state.** GLM alone gated the write, left nothing behind and replied in the shape Flow Mode sets. SWE drew the same board but lost points on reply order, temporary files and its planned first glance. DeepSeek wrote in turn 1 and its turn 3 redraw added an Expired state nobody asked for, which added three crossings and cost a reader an answer
- **FJ-027 ER.** SWE and GLM both score 22. SWE ranks first because its one compose matches the composer's output byte for byte and its claim that every earlier node stayed put was diffed in full. GLM needed three compose sends against a gate that promised one and drew no accent. DeepSeek wrote in turn 1 and moved, deleted and rebuilt nodes of its composed board
- **FJ-028 gantt.** The three boards are the same drawing at 22. GLM ranks first because it proved its write changed nothing else. DeepSeek composed locally before the playback was answered. SWE never read the page before writing and its stop replies carry 17 em dashes and 5 semicolons. The grader notes that weighting efficiency first would put SWE on top, since GLM spent 84,359 output tokens on two failed composes

---

## 4. Clarity

Three fresh Sonnet 5.5 readers each answered three questions on one board of every scenario from its colour render alone, rotated so no reader saw two boards of one scenario. Their answers are in `grades/reader-answers-<n>.md`, their tasks in `grades/reader-<n>-task.md` and the key in `grades/reader-key.md`. Clarity scored full marks on 19 of 21 boards. The two losses are GLM's FJ-023, where the stacked render showed no lane titles or cross-lane connectors, and DeepSeek's FJ-026, where the added Expired state cost the end-state answer.

All three readers named the same three things that slowed them, each on a different model's board, so they belong to the composer rather than a model. No gantt draws a dependency, so what must finish before integration has to be read from the dates. The ER relationship lines carry no end marks, so the direction of a cardinality has to be read from its label. And the state boards' exits from the Confirmed zone leave from its edge, so which inner state a transition starts from is hard to tell.

---

## 5. The gallery

The seven type images in `sk-create-figjam/assets/screenshots/` are the gallery boards above, picked by ADR-004 of phase 038 as amended on 2026-10-26: the most of the 16 points the overview and reading zooms score, then the highest total, then a pass under the current playbook, then fewer supplementary turns, then fewer adaptive turns. FJ-023 and FJ-026 were settled by the board points and FJ-025 by the pass. No run used an extra turn, so the rest fell to the grader's rank: FJ-022, FJ-024 and FJ-027 between two boards and FJ-028 between all three. GLM gives four images and SWE three.

The rule as first written ranked on the total first, so a reply point or a temporary file could decide an image. It gave FJ-023 to DeepSeek's board, which carries the accent on Book a courier pickup. The amendment moved that image to SWE's board, which takes all 16 board points with the accent on Approve the claim, and no other image changed.

---

## 6. Grading notes and deviations

### 6.1 Readers rotated, not one per model

ADR-003 planned one reader per model. The run gave each reader one board of every scenario, rotated across the models, so every reader saw two or three boards of each model. Both designs keep any reader from seeing two boards of one scenario. The rotation also keeps one sharp or slow reader from lifting or sinking one model's Clarity.

### 6.2 One Reply point reconciled

The FJ-022 grader took SWE's Reply point because its Finding says the file held one earlier "Start a return" board when its page read listed ten. The FJ-023 grader scored the same undercount as no loss on DeepSeek's FJ-023 and a looser count on SWE's FJ-023. The scorecard's "every count true" most naturally reads as the measured `Read-back:` counts, and the grader brief counts earlier same-title boards against no model, so the FJ-022 point is reconciled to 2 and SWE's FJ-022 becomes 21 and a pass. `results.jsonl` keeps the grader's own total and verdict under `graded` and the reason under `reconciled`. Without it SWE totals 147 with four passes, and no conclusion above changes.

### 6.3 Two verdict rules

When the run was graded, each board-quality scenario's PASS line judged the scorecard alone. The root playbook's Scenario Acceptance Rules fail a run when any expected signal is missing. The graders followed the PASS line as their brief said, and `results.jsonl` adds `strict_verdict` and `missing_signals` for the root rule. The two disagree on three runs: DeepSeek's FJ-023 and FJ-025 and SWE's FJ-025 fail only under the root rule. GLM's FJ-027 grader added a row the scenario does not hold, and that row is left out of the strict verdict.

The operator chose the root rule on 2026-10-26, so every board-quality and board-creation PASS line now fails a run with an expected signal missing, and `strict_verdict` applies that rule to the signals as they were graded. The runs were not regraded. FJ-027's end-mark signal and FJ-028's dependency-arrow signal were added after the run for composer features no board in it could have, so no run is scored on them.

### 6.4 GLM deleted ten boards on FJ-024

GLM's turn 2 reply said "any of the ten earlier same-named boards is deleted on its own yes". The script's turn 3, "Yes, go ahead.", is the write gate's answer, but GLM had already written and took it as the delete's yes. One call removed ten tagged sections it never created, 345 nodes, among them SWE's 117:4812 and DeepSeek's 118:4935. Both had been rendered before the delete, so no evidence is lost, and Figma's version history holds the file before it. The file is the fictional test file, so no real work was touched.

### 6.5 Harness facts

- **GLM's FJ-023.** All ten `use_figma` calls omitted `fileKey`. Figma's hosted server answers such a call with "Failed to connect to MCP server 'figma'", which reads as an outage. GLM fell back to `generate_diagram`, which drew three lane sections with no outer section, so `renders/glm-FJ-023-112-4566.png` is three lane renders stacked by hand and shows no cross-lane connectors. Its grader scored connectors from the transcript
- **DeepSeek's FJ-027.** It stored the composer in client storage over several calls and ran it from a 5,892 character call, so the driver's `const MODEL` check recorded no board. The board is 134:5211. The driver now reads `boardId` from any `use_figma` result, which finds it
- **Shared `/tmp`.** The sandbox lets a run write to `/tmp`, which outlives the run. Only SWE's FJ-023 and FJ-026 left files there. Files from runs on 2026-10-24 also sit in `/tmp`, and DeepSeek listed some on FJ-027 without using them
- **SWE's FJ-022 page read** overflowed to a Devin temp file outside the run folder. The ten same-title sections the grader cites are in it, and it is not committed because it is an unredacted page dump
- **Renders.** `renders/` holds every board at overview zoom, the longest edge at 2048 px or less. The graders also used 100% and greyscale renders that are not kept here

---

## 7. Findings and their fixes

The run recorded six findings for a later phase. The operator reopened phase 038 on 2026-10-26 to fix all six, and each item names its fix.

1. **A delete needs a yes that names it.** GLM's FJ-024 deleted ten boards on a generic yes. `sk-create-figjam/references/flow-mode.md` Section 6 now runs a delete only on a reply that names the boards, or a yes to a question that names exactly those boards, never on a bare yes or the gate's yes, and a board this conversation did not write is deleted only when the request is about it
2. **The two verdict rules disagreed.** Every board-quality and board-creation PASS line now requires each expected signal as well as the scorecard, and the root playbook Section 3 says so (section 6.3)
3. **The gallery rule ranked on more than the board.** The rule now ranks on the 16 board points first, and FJ-023's image moved to SWE's board (section 5)
4. **The driver missed a composer run through storage.** `run/adaptive_compare.py` now reads `boardId` from any `use_figma` result
5. **A missing file key read as an outage.** `flow-mode.md` Section 9 now has a recovery step: on "Failed to connect to MCP server", check the call for the gate's `fileKey` and retry once with it before calling the route down
6. **Three composer limits slowed every reader.** The composer now draws each gantt `after` as an arrow from the bar it names, and marks both ends of an ER relationship with Figma's crow's-foot cardinality caps. The state reference now says a move that only one inner state takes names that state as its guard, such as `missed check-in [from Upcoming]`, since the checker keeps every transition at its own level

---

## 8. Files

| Path | Holds |
|---|---|
| `skill/<model>/<ID> - <slug>/` | Each run's replies, transcripts, full Devin exports and `meta.json` |
| `replies/<model>/` | The replies alone, one file per turn |
| `stdout/` | The driver's per-turn lines for each run |
| `failed-attempts/` | The attempts a retry replaced |
| `renders/` | Every board at overview zoom |
| `grades/` | The grader brief, the special cases, seven grader files, reader tasks, answers and key |
| `results.jsonl` | One row per run, rebuilt by `run/aggregate.py` |
| `run/` | The Devin runner, the adaptive driver, the batch script, the redaction script, the aggregator and `finals.json` |
| `batch.log`, `run-log.jsonl` | The batch's start and exit lines and every turn's log row |
