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

This run asks which model drives Flow Mode to the best FigJam board. The seven board-quality scenarios, FJ-022 to FJ-028, ran once on each of three models against the composer and design file phase 037 shipped. All 21 runs finished and 21 boards were graded by fresh Claude Sonnet 5.5 graders. Every model passed five of seven scenarios on the scenarios' own PASS lines, once one Reply point was reconciled (section 6.2). On 2026-10-26 the same seven scenarios ran on GPT 6 Luna and Claude Opus 5.5 low as well, and neither displaced the first three (section 8).

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

The seven type images in `sk-create-figjam/assets/screenshots/` were the gallery boards above until the v1.0.6.0 rerun replaced them, picked by ADR-004 of phase 038 as amended on 2026-10-26: the most of the 16 points the overview and reading zooms score, then the highest total, then a pass under the current playbook, then fewer supplementary turns, then fewer adaptive turns. FJ-023 and FJ-026 were settled by the board points and FJ-025 by the pass. No run used an extra turn, so the rest fell to the grader's rank: FJ-022, FJ-024 and FJ-027 between two boards and FJ-028 between all three. GLM gives four images and SWE three.

The rule as first written ranked on the total first, so a reply point or a temporary file could decide an image. It gave FJ-023 to DeepSeek's board, which carries the accent on Book a courier pickup. The amendment moved that image to SWE's board, which takes all 16 board points with the accent on Approve the claim, and no other image changed.

After the composer gained gantt arrows and ER end marks, the FJ-027 and FJ-028 images were drawn again from the model the winning run checked, so they are no longer the renders in `renders/`. Their scores are the original boards' scores, and the redraws were not graded.

On 2026-10-26 the gallery moved to v1.0.6.0 boards. One judge picked the best board of each type from the Claude Sonnet 5.5 high rerun and from gallery runs of FJ-022, FJ-023 and FJ-028, on the type shown most fully and the faster read, then the total. Sonnet's boards replaced all seven type images and the dense flow. The process and state images come from failing runs, FJ-034 at 21 and FJ-026 at 20, because no board of either type passed. The existing-board image stays, because the rerun's FJ-032 board scored 20 and failed.

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

## 8. Two more models: GPT 6 Luna and Opus 5.5 low

The operator asked how GPT 6 Luna at max effort and Claude Opus 5.5 at low effort compare on the same seven scenarios with the v1.0.4.0 skill. Neither runs through Devin, so `run/runtimes.py` adds two turn backends behind the same driver: `codex:<model>:<effort>` runs Codex CLI 0.164.0 with the fast service tier and `claude:<model>:<effort>` runs Claude Code 2.1.310. `run/run_more.sh` ran the 14 runs one at a time and one fresh Claude Opus 5.5 medium grader scored all of them.

**Neither new model beats the first three.**

| Model | Total of 154 | Passes | Mean turns | Wall time | Output tokens |
|---|---|---|---|---|---|
| GLM 5.3 Flash Max | 148 | 5 | 3.00 | 57.9 min | 699,669 |
| SWE 2 Max | 148 (147 as graded) | 5 (4 as graded) | 3.00 | 59.5 min | 361,566 |
| DeepSeek V4.1 Flash Max | 144 | 5 | 3.00 | 30.6 min | 474,256 |
| GPT 6 Luna max | 142 | 2 | 3.57 | 120.1 min | 1,197,317 |
| Opus 5.5 low | 139 | 1 | 3.00 | 32.6 min | 227,099 |

| Scenario | GPT 6 Luna | Opus 5.5 low |
|---|---|---|
| FJ-022 user flow | 22 PASS, rank 3 | 20 FAIL, rank 5 |
| FJ-023 process | 16 FAIL, rank 5 | 20 FAIL, rank 3 |
| FJ-024 architecture | 22 FAIL, rank 3 | 21 PASS, rank 4 |
| FJ-025 sequence | 21 FAIL, rank 4 | 20 FAIL, rank 5 |
| FJ-026 state | 20 FAIL, rank 2 | 18 FAIL, rank 4 |
| FJ-027 ER | 22 PASS, rank 3 | 20 FAIL, rank 4 |
| FJ-028 gantt | 19 FAIL, rank 5 | 20 FAIL, rank 4 |

Ranks run 1 to 5 across all five models in a scenario. The grades are `grades/luna-opus-low.jsonl` and the grader's summary is `grades/luna-opus-low.md`.

**What decided it.** Luna draws clean boards, four of them at 21 or 22, but its turns break the stops. It posted the FJ-025 and FJ-026 playback and gate as interim messages with a one-line status as the reply, ended FJ-023 on a second gate instead of a delivery, split FJ-024 into two boards and resized its FJ-028 section after the compose. Opus 5.5 low held every stop in exactly three turns, but it left its temporary model on disk in six runs, resized a drawn section on FJ-022, cut the compose code down before sending it on three runs and said in several replies that Flow Mode writes only into files it created, which the skill does not say. Their failed shell commands, mostly help lookups, touched no board.

### 8.1 How the two runtimes were made to work

- **Luna's first seven runs are void.** Codex applies its own seatbelt, which cannot nest inside the runner's, so every shell command failed with "sandbox_apply: Operation not permitted" and Luna never read the skill. The operator approved running Codex with its own sandbox off inside the runner's seatbelt, and all seven ran again. The void runs are kept in `skill/luna-no-shell/` and `replies/luna-no-shell/`
- **Codex reaches Figma through the account's Figma app**, served as `codex_apps` with tool names prefixed `figma.`. A `use_figma` call is refused while the client's approval policy is `never`, so the isolated Codex home approves app tools
- **Claude Code needed its own temp folder**, because it roots temp files at `/tmp/claude-<uid>`, which the seatbelt denies
- **Opus 5.5 low made new files.** Its first runs made new FigJam files in the account's team plan, past the pin naming the test file, first with `create_new_file` and then with `generate_diagram`. With both withheld it drew nothing and stopped to ask for a plan. The operator then allowed a new file in the drafts of the Barter team plan, so both tools came back and the first turn gained one sentence: "If you need a new file instead, create it in the Barter team plan and leave it in drafts, with no project." Only Opus 5.5 low received it. Six graded runs made one new file in drafts each and FJ-028 wrote into the test file. The earlier runs are kept in `skill/opus-low-new-file/`, `skill/opus-low-blocked-new-file/` and `skill/opus-low-test-file-only/` and are not graded

### 8.2 Grading differences

- One grader scored all 14 runs where the first run used one grader per scenario
- No fresh readers answered these boards, so the grader scored Clarity from the colour renders itself
- The grader left the first run's grades as they were and noted where it would differ: SWE's FJ-022 Legibility at 2 and no FJ-028 board drawing a dependency arrow

### 8.3 The full playbook run on Opus 5.5 medium

After this report the operator chose Claude Opus 5.5 medium to run all 54 FigJam scenarios, to collect a board for every template. `run/run_full.sh` ran them one at a time in playbook order, with the same drafts sentence Opus 5.5 low received. The operator stopped the run after 24 scenarios, so FJ-016 to FJ-045 did not run. None of these runs was graded.

- **20 boards** cover all seven types: four user flows, two processes, three architectures, five sequences, two states, one ER and two gantts. Each went into the test file or one of seven new files in drafts of the Barter team plan, none in a project. Their renders are `renders/opus-medium-*.png`
- **Seven scenarios drew nothing, as they require.** FJ-003 refused a mindmap, FJ-006 refused a pie chart, FJN-001 kept a FigJam task a task, FJH-001 asked for the real order statuses, and FJR-001, FJR-006 and FJR-007 asked for the screenshots, schema note and launch plan their prompts mention but do not carry
- **Every check scenario's first reply was right.** FJ-003, FJ-005, FJ-006, FJ-014 and FJ-015 refused with exit 1 where the scenario asks, and FJ-004's self-tests passed. FJ-004 also reported that the check skipped one Project copy of a template
- **The driver carried six runs past their end point.** When a run ends with no board the driver sends up to three "Yes, go ahead." turns, so FJ-002, FJ-004, FJ-005, FJ-013, FJ-014 and FJ-015 went on to draw a board the scenario does not grade
- **FJ-009 assumes no hosted Figma server.** This harness connects one, so the gantt was drawn

### 8.4 What the full run changed

The transcripts showed five things in the skill that got in the model's way, and phase `039-figjam-run-findings` fixed them with the three driver findings above in `sk-create-figjam` v1.0.5.0.

- **A file the user named.** Flow Mode now lists an existing FigJam file the user named by its link or key as a target, so a model no longer stops to ask for a plan when the prompt already gave the file
- **Scratch files.** Flow Mode gains a clean-up step that deletes the scratch folder of the model and the composed code before the reply
- **Stops mid-turn.** The playback and the gate are each the last message of their turn, so no stop sits in the middle of a turn that goes on working
- **A widened section.** The playbook's hygiene rule exempts the board section a gated extension widens to hold its notes
- **Room for the model.** A call now carries only its own type's builder, so a graph model has about 9,670 characters of room and a sequence or gantt model about 33,000, where every type had about 2,850
- **The driver** sends a follow-up yes only to a scenario whose script answers the write gate, runs FJ-009 on Claude Code with the hosted Figma server left out and skips it on Codex. FJ-044, whose operator sends the composed code directly with no gate, gets no follow-up yes either. FJ-004 now says its SKIP line is expected in a sandbox, which leaves out `claude project/`

### 8.5 The full playbook run on Sonnet 5.5 high

After `sk-create-figjam` v1.0.5.0 shipped, the operator ran all 54 FigJam scenarios on Claude Sonnet 5.5 at high effort, through the Claude Code backend as `claude:claude-sonnet-5-5:high`, to see how the fixed skill holds across the whole playbook.

- **Lanes.** Eight lanes ran side by side with six to eight scenarios each, and each lane wrote into its own pinned test file. The run went from 16:47 to about 17:15 UTC on 2026-10-26, with 153 turns (116 scripted, 33 adaptive and 4 supplementary), 166.4 minutes of turn time summed over the lanes, 1,284,471 output tokens, 97 Figma calls and no retry
- **Grading.** An independent checker read each run's signals first. One Claude Opus grader then scored all 54 runs from `grades/grader-brief-039.md`, and fresh readers answered from the 23 colour renders. Skeptics challenged 37 grades and an adjudicator ruled on every disputed item. Every ruling is folded into `grades/sonnet-high.jsonl`, and `grades/sonnet-high.md` is computed from it
- **Result.** 23 PASS, 29 FAIL and 2 SKIP as first adjudicated, where the grader's first pass gave 33 PASS, 17 FAIL and 4 SKIP. FJ-027 was rescored to PASS once the shared Human Voice card said a kept literal term is not counted, so the record reads 24 PASS, 28 FAIL and 2 SKIP. FJ-018 and FJ-035 are SKIP because the driver never set up the `fj` route they test
- **Boards.** The 20 written boards score 413 of 440 points, from 18 to 22. Ten pass the board scorecard. Six of the ten that fail it drop to Signal 0 in greyscale and the rest lose a Composition point or score Reply 0
- **What the skeptics changed.** Twelve verdicts moved. Ten went from PASS to FAIL, and FJ-044 and FJ-045 went from SKIP to FAIL because the hosted Figma server was connected. Ten board totals fell, from 433 to 411 points. The shipped role palette renders start, goal, exit and the state and system kinds as near identical greys, so six boards lost Signal. Four boards lost a Composition point to their glance order. Signals marked harness that the run could show became missing, such as the short id on FJ-005 and the stale type grep on FJR-001 and FJR-005. One ruling was contested, the FJ-027 Reply 0, and the clarified Human Voice card has since settled it as Reply 2
- **Against the other models.** On FJ-022 to FJ-028 Sonnet passes four of seven, where DeepSeek and GLM pass five, SWE four, GPT 6 Luna two and Opus 5.5 low one. Those grades had no skeptic round
- **Phase 040.** The operator chose to fix every finding group the run produced:
  - **Skill contradictions**, such as one question against one intake round, split against cut on architecture and quick energy against the draw-ready stop. The HVR count of a term kept with reason is settled in the shared card on the operator's yes
  - **Design and composer**, such as the greyscale role palette, neighbouring zones that share a tint, the composite exit leg and two edges on one magnet. The composite exit's label now fits its leg, but its route still crosses one edge and stays open
  - **Playbook fixes**, such as the stale `-> <type>` grep, the FJ-005 defect count and the FJ-011 lane style
  - **Driver and records**, such as the duplicate intake answer, the operator setup steps the driver skips and the pinned file and `/tmp` the lanes share. This run record is part of the group too

### 8.6 The rerun on v1.0.6.0

After `sk-create-figjam` v1.0.6.0 shipped, Claude Sonnet 5.5 high ran again the 28 scenarios that fail on v1.0.5.0, FJ-027, which failed until its rescore, and the 2 that were skipped, through the same Claude Code backend, plus FJ-022, FJ-023 and FJ-028 for the gallery.

- **Lanes.** Eight lanes started at 22:00:39 UTC on 2026-10-26, after the hold the operator set, and the last finished at 22:30:38. The first turn's stream opens at 22:00:50 UTC. Each lane wrote into its own draft file in the operator's team plan, and FJ-017 and FJ-019 each created a new file. The 30 runs made of the 34 recorded took 92 turns (80 scripted and 12 adaptive), 113.4 minutes of turn time summed over the lanes and 873,349 output tokens. Every turn exited 0 and none was retried
- **Grading.** A checker read each run's signals. One Claude Opus grader then scored all 34 records from `grades/grader-brief-040.md`, fresh readers answered from the colour and greyscale renders and a skeptic challenged every grade, with an adjudicator ruling on each dispute. The rulings are folded into `grades/sonnet-high-rerun.jsonl` (31 lines) and `grades/sonnet-high-gallery.jsonl` (3 lines), and `grades/sonnet-high-rerun.md` lists every verdict, ruling and remaining failure
- **Result.** 14 PASS, 13 FAIL and 4 not run, where 28 had failed, FJ-027 had passed on its rescore and 2 had been skipped on v1.0.5.0, so 13 of the 14 passes are new. All three type-choice scenarios, both pre-write checks and both routing scenarios now pass. FJ-018, FJ-035, FJ-044 and FJ-045 did not run, because each is marked operator-only and the driver performs no operator step, so they leave the denominator rather than count as SKIP. The skeptics moved FJ-020 and FJ-034 from PASS to FAIL
- **Boards.** 17 boards were written and 16 rendered, because FJ-031's own scripted turns deleted its first board. The 13 graded rerun boards score 272 of 286 points, from 19 to 22, and none lost a Signal point in greyscale. Six v1.0.5.0 boards scored Signal 0, and the three of them that ran again, FJ-026, FJ-032 and FJ-033, now score Signal 2. The other three belong to operator-only scenarios that did not run. Of the gallery runs FJ-022 passes at 21, FJ-028 passes at 20 and FJ-023 fails at 20 because the run left the claims log off
- **What still fails.** Six failures are model slips alone, such as a reply that opens on a cleanup line (FJ-036) or an inferred step with no assumed mark (FJ-042). The rest trace at least in part to the skill or the playbook. The skill never defines when a user asked for one board, so FJ-029 kept one board where the scenario expects two. A state board's first glance cannot be the group of end states FJ-026 asked about, the heavier goal outline reads before FJ-034's planned second glance and the No route reply skips the playback on FJ-009
- **Findings.** A findings pass over all 34 runs named 24 findings: 13 skill gaps, 4 playbook gaps, 4 harness gaps, 1 Project mirror note and 2 notes on model slips and the fixes that held. The checker and reader files it found missing are now in `grades/sonnet-high-rerun/`, with the greyscale renders the readers saw in its `grey/` folder. A critic then added 11 more, mostly on the records. FJ-029 and FJ-032 claim a visual label read and keep Reply 2 where FJ-026 lost a point for the same claim, eight board records lack the scorecard signal and the driver's file pin and drafts pin give a pinned run three destinations. Phase 041 fixes both sets. It also applied the critic's record corrections: Reply 1 on FJ-029 and FJ-032, the scorecard signal on all eight records, FJ-035 split into its nine signals and the operator-only scenarios recorded as not run, so the boards' total fell from 274 to 272. Gallery FJ-023 rose from 18 to 20 under the new Fidelity row

### 8.7 The rerun on v1.0.7.0

After `sk-create-figjam` v1.0.7.0 shipped, Claude Sonnet 5.5 high ran again every scenario that did not pass on v1.0.6.0: the 13 rerun failures, the gallery FJ-023 and the operator scenarios FJ-044 and FJ-045. FJ-018 and FJ-035 were not run, because they need Figma Desktop and the figma-ds-cli daemon, which this environment does not have.

- **Lanes.** On 2026-10-27 every board scenario wrote into its own new draft file in the operator's team plan, created before its first turn, and `file_start_sections` in each `meta.json` records what the file held. FJ-017 created its own file. FJ-031 paused before its third turn while the operator added a sticky, and FJ-045 ran after the operator broke the design file, which was restored and checked with `git diff --exit-code` after the run. FJ-044 is operator-only: the operator composed the seven shipped examples and sent each unchanged. The 15 driver runs took 50 turns (46 scripted and 4 adaptive), 70.2 minutes of turn time summed over the lanes and 597,987 output tokens. Every turn exited 0 and none was retried
- **Grading.** Fresh readers answered from the colour renders. One Claude Opus grader then scored all 18 scenarios from `grades/grader-brief-041.md`, skeptics challenged the grades and adjudicators ruled on each dispute, and a completeness critic checked the folded records. The rulings and the critic's corrections are folded into `grades/sonnet-high-041.jsonl`, and `grades/sonnet-high-041.md` lists every verdict, ruling and remaining failure
- **Result.** 2 PASS, 14 FAIL and 2 NOT RUN. Of the 14 scenarios run on both versions, only FJ-020 moved to PASS. FJ-044 passed on its first run and FJ-045 failed on its first. The skeptics moved FJ-034 and FJ-042 from PASS to FAIL. So phase 041 misses its own success criterion, more of the scenarios it runs passing than the 14 of 27 of the v1.0.6.0 rerun. Counted over every scenario run on either version, 16 of 29 now pass
- **Boards.** The 9 scored boards score 180 of 198 points, from 16 to 21, as FJ-017 carries no scorecard, and none lost a Signal point in greyscale. Composition is below full marks on 8 of the 9 scored boards, the largest single cause. The seven FJ-044 boards share one title block, key layout and line look and each scores 2 on Matches the active design
- **What still fails.** Most losses are model slips against rules the skill states, such as a glance plan that leaves the goal out (FJ-023, FJ-036) or a reply that opens on a status line (FJ-032). But the plans also copy the shipped examples: the process, architecture and user flow examples leave the goal, the gateway or the entry out of their glance lines, and the state rule plans the composite first where readers read the saturated first state first. Other gaps sit in the skill or the playbook. No rule puts a `Left out:` line on a split board (FJ-029) or a gate reply (FJ-040, FJ-034). The single-sticky rule has no free side when the right holds an end-dot connector (FJ-017). The router lets two runs lie 24 px apart where the style guide sets 56 (FJ-017, FJ-026). The rubric lets a user flow's accent sit on a decision where FJ-045 expects the goal
- **Each failure.** FJ-009 leaves the fj limit out of the reply after the yes. FJ-017 makes an ungated third call and parks a sticky at the board's edge. FJ-023, FJ-026, FJ-031, FJ-033, FJ-036 and FJ-045 each read an unplanned or later part ahead of the planned second glance. FJ-033 also marks its gateway as a layout aid rather than assumed, and FJ-045 puts its accent on a decision. FJ-029 splits the flow but names no split, with Composition and Reply at 0. FJ-032 opens on a status sentence. FJ-034 has no `Left out:` line for the cuts it promised. FJ-038 never says the delete waits for the new board's read-back. FJ-040 names the left-out flows only in its Writes bullets. FJ-042 drops the assumed marks between the playback and the model
- **Findings.** A findings pass named 25 findings: 8 skill gaps, 3 playbook gaps, 3 harness gaps, 2 composer findings, 1 Project mirror note, 7 notes on model slips and 1 note on the fixes that held. The critic added 10 more on the records and the shipped examples. Its record corrections are applied: the reader notes, greyscale renders and operator step files now sit in `grades/sonnet-high-041/`, FJ-033 drops to 21 on the Composition rule FJ-045 was held to and two loss causes are restated. Phase 042 takes the rest
- **Gallery.** The same judge rule replaced only `process-board.png`, with the FJ-023 board. It ties the FJ-034 board it replaced at 21 and fails the same way, but it shows more of the process type

### 8.8 The rerun on v1.0.8.0

After `sk-create-figjam` v1.0.8.0 shipped, Claude Sonnet 5.5 high ran again the 14 scenarios that failed on v1.0.7.0. FJ-020 and FJ-044 passed on v1.0.7.0 and FJ-018 and FJ-035 still need Figma Desktop, so none of the four ran.

- **Lanes.** On 2026-10-27 every board scenario wrote into its own new draft file in the operator's team plan, and each run had its own temp folder. A first launch stopped within three seconds when the disk filled, before any model turn, and the relaunch ran clean. FJ-031 paused before its own first turn while the operator added a sticky beside the first board. FJ-045 ran alone after the others, with the design file broken three ways and restored afterwards, and `git diff --exit-code` on it exited 0. The 14 driver runs took 47 turns (44 scripted and 3 adaptive), 68.6 minutes of turn time summed over the lanes and 579,692 output tokens. Every turn exited 0 and none was retried
- **Grading.** Each fresh reader was given the scenario's persona and its three questions without the answers, and FJ-029's reader saw both boards together. One Claude Opus grader then scored all 14 scenarios from `grades/grader-brief-042.md`, skeptics challenged eleven of the grades and adjudicators ruled on each dispute, and a completeness critic checked the folded records
- **Operator rulings.** The critic found two rules applied unevenly, and the operator ruled on both. Lanes and zones read as frame on every type, like the title block, which gives FJ-023 and FJ-034 back a Composition point. The state rule applies as written, so a reader who takes the states inside a composite before the planned glance costs a point on every state board, which drops FJ-026 to 21. FJ-031 also takes the critic's correction that items in one glance line carry no order
- **Result.** 7 PASS and 7 FAIL, up from 0 of these 14 on v1.0.7.0. FJ-023, FJ-033, FJ-034, FJ-038, FJ-040, FJ-042 and FJ-045 now pass. SC-001 asks for at least 7, so phase 042 meets it, but only under the two rulings: before them the count was 6. Counted over every scenario run on any version, 23 of 29 now pass
- **Boards.** The 9 scored boards score 183 of 198 points, from 18 to 22. Composition is below full marks on 3 of the 9, down from 8 of 9, and every loss is the states inside a composite (FJ-026, FJ-032) or a revision's changed end (FJ-031). No board lost a Signal point in greyscale. Orphan wraps cost Legibility on six boards, and no run printed a `Label:` line
- **What still fails.** FJ-009's gate keeps its Plan and Calls lines where the missing route belongs. FJ-017 shifts both stickies 64 px off level on adjacent rows. FJ-026 and FJ-032 lose Composition to the composite's inner states. FJ-029 titles its second board `2. Setup`, the spelling `assets/flow-templates.md` gives, and names no split under `Left out:`. FJ-031 keeps a numbered title on its revision, so the write-time delete rule never runs, and its delete reply opens on prose. FJ-036 opens its reply on a status sentence above the URL
- **Findings.** A findings pass named 15 findings and the critic 7 more: the split title spelled two ways, the revision's changed end competing with the entry for the second glance, a numbered title on a revision, a reply that does not open on the URL in three runs, two stickies on adjacent rows, no example of a missing-route gate, a `Label:` check that falls silent without node and FigJam elbows that lie 24 px apart. The reader notes, greyscale renders and operator files sit in `grades/sonnet-high-042/`, and every evidence path in the records resolves inside the run folder. Phase 043 takes the rest
- **Gallery.** The same judge rule replaced only `state-board.png`, with the FJ-026 board. It scores 21 where the board it replaced scored 20, and its pink outline leads to an end state with its own key entry. It still fails on Composition

### 8.9 The rerun on v1.0.9.0

After `sk-create-figjam` v1.0.9.0 shipped, Claude Sonnet 5.5 high ran again the 7 scenarios that failed on v1.0.8.0: FJ-009, FJ-017, FJ-026, FJ-029, FJ-031, FJ-032 and FJ-036.

- **Lanes.** On 2026-10-27 every board scenario wrote into its own new draft file in the operator's team plan, FJ-017 created its own file and each run had its own temp folder. FJ-031 paused once while the operator added a sticky beside its first board. The 7 driver runs took 29 turns (25 scripted and 4 adaptive), 43.5 minutes of turn time summed over the lanes and 363,560 output tokens. Every turn exited 0 and none was retried
- **Harness.** The lanes found Homebrew's node, which cannot load its `simdutf` library after an upgrade, so every check printed `Label: skipped, the trace failed` with that reason. The skipped line works as v1.0.9.0 meant, but no run had a label trace. The next rerun pins a working node in the launcher
- **Grading.** Two fresh readers read each scored board from the colour renders, writing their reading order before the scenario's three questions. One Claude Opus grader scored all 7 scenarios from `grades/grader-brief-043.md`, and a Composition point was lost only when both readers read a part early or out of order. Skeptics challenged six of the grades, adjudicators ruled on each dispute, and a completeness critic checked the folded records
- **Operator ruling.** FJ-017 fails on the reading of beside the v1.0.8.0 grade used: its second sticky sits right of Cancelled and 64 px under the No-show sticky, where the new rule sends it below or to the left. The adjudicator had kept it as a pass because the scenario signal asks only for beside
- **Result.** 1 PASS and 6 FAIL. FJ-009 now passes on its missing-route gate. SC-001 asks for at least 5, so phase 043 does not meet it. SC-002 holds, because every Composition point lost was a part both readers read early. Counted over every scenario run on any version, 24 of 29 now pass
- **Boards.** The 5 scored boards score 97 of 110 points, from 19 to 20, and every one has Composition at 0. The reply fixes hold on all five: each opens on the URL, the delete reply opens on the board that stays, the split is spelled `2. Workspace setup` and named under `Left out:`, and the revision keeps its title. Orphan wraps cost Legibility on three boards
- **What still fails.** The composer draws a composite across the top row, so on FJ-026 and FJ-032 both readers read Upcoming and In stay before the planned first glance, a pink focus outline included. On FJ-029, FJ-031 and FJ-036 readers take a flow's main row in path order after the accent, while the plans order nodes by fill and outline: FJ-031's plain screens read before its changed end, FJ-029 splits one kind of diamond across two glance lines and FJ-036 leaves two nodes out of every line. FJ-029's gate also miscounts board 2's decisions, and FJ-036's gate turn ends on a status paragraph after `Write it?`
- **Findings.** A findings pass named 18 findings and the critic 8 more. Beyond the two Composition causes they name the broken node, a by-eye label rule with no width, a read-back that cannot read connector labels, FJ-017 testing the adjacent-row rule only loosely, state readers confused by the composite's inner end dot and scored scenarios that replay the shipped examples. The reader notes, greyscale renders and the FJ-031 operator file sit in `grades/sonnet-high-043/`, and every evidence path in the records resolves inside the run folder. Phase 044 takes the composer placement, the path-order glance rule, the wider revision exemption and the node pin
- **Gallery.** The judge kept every gallery image. No rerun board scores at least as high as the board it would replace

### 8.10 The rerun on v1.0.10.0

After `sk-create-figjam` v1.0.10.0 shipped, Claude Sonnet 5.5 high ran again the 6 scenarios that failed on v1.0.9.0: FJ-017, FJ-026, FJ-029, FJ-031, FJ-032 and FJ-036.

- **Lanes.** On 2026-10-27 every board scenario wrote into its own new draft file in the operator's team plan, FJ-017 created its own file and each run had its own temp folder. FJ-031 paused once while the operator added a sticky beside its first board. The 6 driver runs took 28 turns (22 scripted and 6 adaptive), 40.1 minutes of turn time summed over the lanes and 344,069 output tokens. Every turn exited 0 and none was retried
- **Harness.** The launcher put a working node first on PATH, but the Bash tool inside each Claude Code run rebuilds PATH from the shell profile, where Homebrew's broken node comes first. Every check again printed `Label: skipped, the trace failed`, so no run had a label trace
- **Grading.** Two fresh readers read each scored board, one Claude Opus grader scored all 6 scenarios from `grades/grader-brief-044.md`, skeptics challenged the grades and adjudicators ruled on each dispute. The skeptics turned FJ-031 from FAIL to PASS on the Reply bands and FJ-032 from PASS to FAIL on its intake signal
- **Operator ruling.** FJ-032 passes. Its round 1 left two rows open for a round 2, and `references/flow-mode.md` Section 2 lets a later round ask a row left unasked, though another sentence there says the reply after accepted answers is the playback
- **Result.** 2 PASS and 4 FAIL. FJ-031 passes at 21 on the wider revision exemption and FJ-032 at 22 now that the composite sits after Pending. SC-001 asks for at least 4, so phase 044 does not meet it. SC-002 fails on FJ-026, whose readers take Pending, Upcoming and In stay before the pink-outlined Cancelled. Counted over every scenario run on any version, 26 of 29 now pass
- **Boards.** The 5 scored boards score 101 of 110 points, from 19 to 22. Composition is 0 on FJ-026 and FJ-029, 1 on FJ-036 and full on FJ-031 and FJ-032
- **What still fails.** FJ-017 makes a third `use_figma` call to probe a sticky, and its boxed-in Cancelled sticky lands 688 px out at the board's edge. FJ-026's focused end state is drawn on the bottom row, and its reply opens on a sentence above the URL. FJ-029 plans by kind rather than path order. FJ-036's detour is drawn on the main row
- **Findings.** A findings pass named 15 findings and the critic 6 more. Beyond the four failures they name the read-back that cannot read connector labels, the revision playback that reads nothing first, the second glance missing from the revision reply shape and the two intake sentences. The reader notes, greyscale renders and the FJ-031 operator file sit in `grades/sonnet-high-044/`. The operator closed testing here and sent the findings to the skills
- **Gallery.** The judge kept every gallery image. No rerun board scores at least as high as the board it would replace

### 8.11 The rerun on v1.0.11.0

After `sk-create-figjam` v1.0.11.0 shipped, Claude Sonnet 5.5 high ran again the 4 scenarios that failed on v1.0.10.0: FJ-017, FJ-026, FJ-029 and FJ-036.

- **Lanes.** On 2026-10-27 every board scenario wrote into its own new draft file in the operator's team plan, FJ-017 created its own file and each run had its own temp folder. The 4 driver runs took 14 turns (12 scripted and 2 adaptive), 26.5 minutes of turn time summed over the lanes and 219,762 output tokens. Every turn exited 0 and none was retried
- **Harness.** Homebrew's node was reinstalled before the rerun, so the label trace ran on every run and no check printed `Label: skipped`. `run/redact_run.py` now also redacts plan keys, and it ran over the whole run folder before the commit
- **Grading.** Two fresh readers read each scored board, one Claude Opus grader scored all 4 scenarios from `grades/grader-brief-045.md`, skeptics challenged the grades and adjudicators ruled on each dispute. The skeptics changed citations on FJ-017 and FJ-026 and no verdict or total
- **Result.** 2 PASS and 2 FAIL. FJ-026 passes at 22 now that the plan follows the board as drawn, and FJ-029 at 21 with both boards planned along the drawn main row. SC-003 asks for at least 3, so phase 045 does not meet it. Counted over every scenario run on any version, 28 of 29 now pass
- **What still fails.** FJ-017 found Cancelled boxed in only after the compose. It wrote no notes and asked for pins or a recompose, as the skill's after-compose branch says, but the scenario expects that offer from the Turn 2 gate, and nothing tells the gate how to see a node's sides before the write. FJ-036 put its one accent on the goal at the far right end of the main row and planned it first, so both readers read the whole row before it and Composition scores 0. Its playback and gate also end on a self-scan line after their question
- **Findings.** A findings pass named 11 findings and the critic 7 more. Beyond the two failures they name a label trace that missed FigJam's lone `tip` on FJ-029, a gate that skipped its sketch or critique questions in most runs, and FJ-026's pass resting on a reading the playbook never states, that end states named as one group carry no order. The reader notes and greyscale renders sit in `grades/sonnet-high-045/`
- **Gallery.** The judge replaced the state image with FJ-026's 22-point board and kept every other image

### 8.12 The rerun on v1.0.12.0

After `sk-create-figjam` v1.0.12.0 shipped, Claude Sonnet 5.5 high ran again the 2 scenarios that failed on v1.0.11.0, FJ-017 and FJ-036, and the 2 board-quality scenarios FJ-022 and FJ-023, whose earlier passes predate the current plan rule.

- **Lanes.** On 2026-10-28 every board scenario wrote into its own new draft file in the operator's team plan, FJ-017 created its own file and each run had its own temp folder. The 4 driver runs took 15 turns (12 scripted and 3 adaptive), 23.8 minutes of turn time summed over the lanes and 204,863 output tokens. Every turn exited 0 and none was retried
- **Harness.** The label trace ran on every run. A whole-folder redaction pass rewrote committed files the operator had kept unredacted, so they were restored and the new output was redacted on its own. `run/run_full.sh` now redacts each scenario's own output after it runs, `run/adaptive_compare.py` redacts each run-log row and reads a counted `Read-back:` line or a `use_figma` call as a delivery without asking the classifier, and `run/redact_run.py` takes single files
- **Grading.** Two fresh readers read each scored board, one Claude Opus grader scored all 4 scenarios from `grades/grader-brief-046.md`, skeptics challenged the grades and adjudicators ruled. A record repair then applied the playbook's entry-and-goal clause to FJ-036, which moved it from 20 to 19, and found that FJ-023's gate sketch drops the lane style lines
- **Result.** 0 of 4 pass: FJ-017 FAIL with no scorecard, FJ-022 FAIL at 20, FJ-023 FAIL at 19 and FJ-036 FAIL at 19. SC-003 asks for FJ-017 and FJ-036 to pass, so phase 046 does not meet it. The earlier FJ-022 and FJ-023 passes came from one reader or none under the plan rule that held before v1.0.11.0, so the lower totals are not a regression
- **What still fails.** Three gates show a sketch that drops lines of the checked model, `%%` lines on FJ-017 and FJ-036 and lane style lines on FJ-023. The glance plan puts every off-row node last, while the composer draws Contact support (FJ-022), Send a second photo and the Claims table (FJ-023) and Get credit (FJ-036) where both readers meet them early, so Composition scores 1, 0 and 0. FJ-022's intake round ends on a sentence after its stop line. FJ-017's No-show sticky sits 328 px from its node, past the one sticky width rule, and the Cancelled sticky went below instead of the side its line named. Label wraps cost Legibility on all three boards, and on FJ-022 and FJ-036 no label in the sources' words cleared the check
- **Fixes.** Phase 047 takes every cause: the check prints the drawn reading order on a `Glance:` line that the glance plan follows, a `Row:` line for a main-row line that bends, the alignment on each `Sides:` line and no square past one sticky width, `may leave` for a word only one measure strands, a gate sketch that carries every `%%` and `style` line, a Legibility level for several wraps and the intake round that asks the three dials. The reader notes and greyscale renders sit in `grades/sonnet-high-046/`
- **Gallery.** No board passed, so every image stays

### 8.13 The rerun on v1.0.13.0

After `sk-create-figjam` v1.0.13.0 shipped, Claude Sonnet 5.5 high ran again the 4 scenarios that failed on v1.0.12.0: FJ-017, FJ-022, FJ-023 and FJ-036.

- **Lanes.** On 2026-10-28 every board scenario wrote into its own new draft file in the operator's team plan, FJ-017 created its own file and each run had its own temp folder. The 4 driver runs took 15 turns (12 scripted and 3 adaptive), 23.8 minutes of turn time summed over the lanes and 204,874 output tokens. Every turn exited 0 and none was retried
- **Harness.** Each scenario's output was redacted as it finished. The file FJ-017 created for itself kept its key in two files, because no keys file could name it ahead of time, so `run/redact_run.py` now reads a key from any `file_key` or `fileKey` field and redacts every copy across the batch. A pass over `run-log.jsonl` rewrote older rows, which were restored with only the 15 new rows kept
- **Grading.** Two fresh readers read each scored board, one Claude Opus grader scored all 4 scenarios from `grades/grader-brief-047.md`, skeptics challenged each grade and adjudicators ruled. The rulings dropped FJ-022 from 22 to 21 for `courier?` alone on the method decision and moved FJ-036 from PASS to FAIL on its intake round
- **Result.** 1 PASS and 3 FAIL: FJ-022 PASS at 21, FJ-023 FAIL at 21, FJ-036 FAIL at 22 and FJ-017 FAIL with no scorecard. SC-003 asks for at least 3, so phase 047 does not meet it. Every v1.0.13.0 fix the runs touched worked: each gate showed the checked model whole, both FJ-017 stickies landed on the side and in the alignment their `Sides:` lines named, FJ-022's main row ran straight with Contact support beside Pick a reason and both its readers followed the `Glance:` order
- **What still fails.** FJ-017's reply named neither sticky on a `Finding:` line, which the scenario asks for whenever a sticky sits below or left of its node, while the skill asks for it only when a sticky leaves the side its line named. FJ-036's first intake round ended on a `Why:` line after its last question, because the question template puts the reason last. On FJ-023 both readers read the decision beside the accent in its lane before the entry the `Glance:` line put second, so Composition scores 1. The label check traced the decision diamonds 24 px wider than FigJam draws them and read their text box narrower than FigJam fits it, so it passed `Drop-off point or courier?`, whose last word FigJam stranded
- **A finding kept out of the verdicts.** FJ-022 ran the check in turn 1 with the reader and the dials assumed, before the playback, which the draw-ready threshold in `references/flow-mode.md` does not allow under Standard energy. Its scenario's signals and PASS line held when it was graded, so its PASS stands, and the next release adds the rule to the playbook so later runs are scored on it
- **Fixes.** A fresh Opus recommendation, each cause checked against the files, set the v1.0.14.0 fixes: a decision joined to the accent on its own row reads right after the accent, every intake round ends on one closing question, the FJ-017 Finding follows the sides the gate showed, the label trace matches the diamonds FigJam draws, the playback names the dials, the Composition row says which part of a swapped pair costs the point and turn 1 is an intake round when the reader is unsettled. The reader notes and greyscale renders sit in `grades/sonnet-high-047/`
- **Gallery.** The judge replaced the user flow image with FJ-022's 21-point board, which puts the accent on the 30-day decision rather than on the goal, and kept every other image

### 8.14 The rerun on v1.0.14.0

After `sk-create-figjam` v1.0.14.0 shipped, Claude Sonnet 5.5 high ran FJ-017, FJ-022, FJ-023 and FJ-036 again.

- **Lanes.** On 2026-10-28 FJ-022, FJ-023 and FJ-036 each wrote into its own new draft file in the operator's team plan, FJ-017 created its own file and each run had its own temp folder. A first launch stopped on every scenario's first turn on the account's weekly usage limit, before the model ran, so its output was set aside and the run log restored. The relaunch after the limit reset took 15 turns (13 scripted and 2 adaptive), 21.0 minutes of turn time summed over the lanes and 186,791 output tokens. Every turn exited 0 and none was retried
- **Grading.** Two fresh readers read each scored board, one Claude Opus grader scored all 4 scenarios from `grades/grader-brief-048.md`, a skeptic challenged each grade and an adjudicator ruled on the one dispute. A completeness check on Claude Sonnet 5.5 high then opened every reader note behind the records and found two Composition scores resting on misread reader orders and a Shared trunks loss the style guide does not charge. Each was confirmed against the notes and the style guide before the records changed
- **Result.** 2 PASS and 2 FAIL: FJ-017 PASS with no scorecard, FJ-036 PASS at 21, FJ-022 FAIL at 20 and FJ-023 FAIL at 21. SC-003 asks for at least 3, so phase 048 does not meet it. FJ-017 now passes, its two stickies landing where its `Sides:` lines named with no `Finding:` owed. FJ-036 passes, both intake rounds ending on the closing question and its playback naming the dials
- **What still fails.** FJ-022's delivery reply opens on a sentence announcing itself above the board URL, a slip Claude Sonnet 5.5 high has made in six earlier runs, and both its readers read the Contact support exit last where the `Glance:` line planned it fifth. FJ-023 skipped the turn 1 intake round with the reader unsettled, drew the runbook's warehouse queue as a ninth node its scenario does not count and lost Composition when both readers read the Damage reported entry before the decision the `Glance:` line lifted beside the accent. FJ-036 lost one Legibility point to `old?` alone on its accented price decision, which the label trace passed
- **What the rerun shows.** The closing question, the dials at the playback, the FJ-017 Finding rule and the turn 1 intake held wherever a run met them. The lifted decision did not: on FJ-023 neither reader took the decision right after the accent, so the order the check prints still misplaces entries and exits that readers meet by the main row. The FJ-023 scenario still expects a turn 1 playback and 8 nodes, against the playbook's turn 1 rule and the process reference's queue store. The reader notes and greyscale renders sit in `grades/sonnet-high-048/`
- **Gallery.** The judge replaced the process image with FJ-023's 21-point board, which ties the old image's score, keeps every route in its lane and accents a step rather than the goal, and kept every other image

### 8.15 The rerun on v1.0.15.0

After `sk-create-figjam` v1.0.15.0 shipped, Claude Sonnet 5.5 high ran FJ-022 and FJ-023 again, the two scenarios that failed on v1.0.14.0. The operator ended testing at this rerun, so what still fails stands as a known limitation.

- **Lanes.** On 2026-10-28 the two scenarios ran one after the other, each writing into its own new draft file in the operator's team plan with its own temp folder. FJ-022 took about 6 minutes and FJ-023 about 4 and a half.
- **Grading.** Two fresh readers read each board from the colour renders and closed each note on an `Order:` line. `run/composition_check.py` scored Composition from those lines and the last `Glance:` line each run printed, and one Claude Sonnet 5.5 high grader scored both scenarios from `grades/grader-brief-049.md`. The two FJ-022 readers first wrote their `Order:` line in flow order, against their own reading order lists. Each rewrote only that line from its own list, and `grades/reader-brief.md` now says the line repeats the reading order, not the order the flow runs.
- **Result.** 0 PASS and 2 FAIL, with both boards at 22 of 22. FJ-022 fails because its scenario expects three zones and the model drew two, where the skill makes zones a choice and the prompt names none. FJ-023 fails because its turn 1 intake round adds a sentence about the write target after its closing question, a model slip against the rule that a stop ends on its question.
- **What the rerun shows.** Both replies open on the board URL, which clears the Reply loss FJ-022 carried in six earlier runs. Both `Glance:` lines read the plain order, and both readers of each board read the accent first, so Composition is 2 on both. FJ-023 draws its warehouse queue as the Claim queued label and holds 8 nodes. Neither check printed a `Label:` line, so the glyph-width trace was not exercised.
- **Gallery.** FJ-023's 22-point board replaces the process image, since it scores higher, keeps every step in its lane and draws the queue as a label. The user flow image stays the three-zone FJ-022 board from section 8.13, because this run's miss is the board's own zone count.

---

## 9. Files

| Path | Holds |
|---|---|
| `skill/<model>/<ID> - <slug>/` | Each run's replies, transcripts, full Devin, Codex or Claude Code exports and `meta.json` |
| `replies/<model>/` | The replies alone, one file per turn |
| `stdout/` | The driver's per-turn lines for each run |
| `failed-attempts/` | The attempts a retry replaced |
| `renders/` | Every board at overview zoom, with the Sonnet 5.5 high boards at full size as `sonnet-high-<ID>-<node>.png` and the rerun and gallery boards as `sonnet-high-rerun-<ID>-<node>.png` and `sonnet-high-gallery-<ID>-<node>.png`, the section 8.7 boards as `sonnet-high-041-<ID>-<node>.png` the section 8.8 boards as `sonnet-high-042-<ID>-<node>.png` the section 8.9 boards as `sonnet-high-043-<ID>-<node>.png` the section 8.10 boards as `sonnet-high-044-<ID>-<node>.png` the section 8.11 boards as `sonnet-high-045-<ID>-<node>.png` the section 8.12 boards as `sonnet-high-046-<ID>-<node>.png` the section 8.13 boards as `sonnet-high-047-<ID>-<node>.png` the section 8.14 boards as `sonnet-high-048-<ID>-<node>.png` and the section 8.15 boards as `sonnet-high-049-<ID>-<node>.png` |
| `grades/` | The grader briefs, the special cases, seven grader files, the reader tasks with their answers and key, `luna-opus-low.*` for section 8, `sonnet-high.*` for section 8.5 `sonnet-high-rerun.*` and `sonnet-high-gallery.jsonl` for section 8.6 `sonnet-high-041.*` for section 8.7 `sonnet-high-042.*` for section 8.8 `sonnet-high-043.*` for section 8.9 `sonnet-high-044.*` for section 8.10 `sonnet-high-045.*` for section 8.11 `sonnet-high-046.*` for section 8.12 `sonnet-high-047.*` for section 8.13 `sonnet-high-048.*` for section 8.14 and `sonnet-high-049.*` for section 8.15, with `reader-brief.md` for the reader prompt and `run/composition_check.py` for Composition |
| `grades/sonnet-high/` | The Sonnet 5.5 high checker files in `checks/` and the fresh readers' notes in `readers/` |
| `grades/sonnet-high-rerun/` | The same checker files and reader notes for the section 8.6 rerun and gallery runs, and the greyscale renders the readers saw in `grey/` |
| `grades/sonnet-high-041/` | The section 8.7 reader notes in `readers/`, the greyscale renders in `grey/` and the FJ-044 and FJ-045 operator step files in `operator/` |
| `grades/sonnet-high-042/` | The section 8.8 reader notes in `readers/`, the greyscale renders in `grey/` and the FJ-031 and FJ-045 operator files in `operator/` |
| `grades/sonnet-high-043/` | The section 8.9 notes of two readers per board in `readers/`, the greyscale renders in `grey/` and the FJ-031 operator file in `operator/` |
| `grades/sonnet-high-044/` | The section 8.10 notes of two readers per board in `readers/`, the greyscale renders in `grey/` and the FJ-031 operator file in `operator/` |
| `grades/sonnet-high-045/` | The section 8.11 notes of two readers per board in `readers/` and the greyscale renders in `grey/` |
| `grades/sonnet-high-046/` | The section 8.12 notes of two readers per board in `readers/` and the greyscale renders in `grey/` |
| `grades/sonnet-high-047/` | The section 8.13 notes of two readers per board in `readers/` and the greyscale renders in `grey/` |
| `grades/sonnet-high-048/` | The section 8.14 notes of two readers per board in `readers/` and the greyscale renders in `grey/` |
| `grades/sonnet-high-049/` | The section 8.15 notes of two readers per board in `readers/` and the greyscale renders in `grey/` |
| `results.jsonl` | One row per run of the first three models, rebuilt by `run/aggregate.py`, then one row per Sonnet 5.5 high run built from `grades/sonnet-high.jsonl`. A rerun of `run/aggregate.py` rewrites the file without the Sonnet rows |
| `run/` | The Devin runner, the Codex and Claude Code backends, the adaptive driver, the batch scripts, the redaction script, the aggregator and `finals.json` |
| `batch.log`, `batch-more.log`, `batch-full.log`, `run-log.jsonl` | Each batch's start and exit lines and every turn's log row |
