# Luna and Opus low grades, five-model ranking

These are the grades for 14 runs: FJ-022 to FJ-028 on `luna` (GPT 6 Luna at max effort on the Codex CLI) and `opus-low` (Claude Opus 5.5 at low effort on Claude Code). They are graded on the same 22-point scorecard as the first run. The deepseek, glm and swe totals and verdicts are copied unchanged from `FJ-02N.jsonl`. Each scenario below ranks all five models by total, then pass over fail, then fewer supplementary turns. Where those three still tie, the earlier order is kept or the reason is given.

## Two grading differences

- **One grader.** One grader scored all 14 new runs. The first run's three models were scored by other graders.
- **Clarity.** No fresh readers took part this time. I answered each scenario's three questions from the colour overview render before reading the transcript, and every run's `losses` list says so.

## FJ-022 user flow

1. glm, 109:4426, 22, PASS
2. deepseek, 108:4364, 22, PASS
3. luna, 167:5959, 22, PASS
4. swe, 111:4498, 20, FAIL
5. opus-low, 1:3, 20, FAIL

The top three all score 22 and pass. Luna ranks third because its opening question about a source conflict pushed the write into a supplementary turn. Opus-low ranks below swe on the same total because it resized its composed section for a proposal sticky, drew no zones and gave no `Left out:` line for the proposal. Swe's losses are a reply miscount and one label.

## FJ-023 process

1. deepseek, 116:4717, 20, PASS
2. swe, 114:4602, 20, FAIL
3. opus-low, 1:3, 20, FAIL
4. glm, 112:4566, 17, FAIL
5. luna, 168:6021, 16, FAIL

Deepseek is the only pass. Swe and opus-low tie at 20 on the same two losses: text before the read-back and a temporary model left on disk. Swe goes first because its accent sits on Approve the claim as the scenario names, while opus-low trimmed the composer code before sending it. Luna is last because it never delivered: turn 3 asks to write a corrected board after a clipped label, so the reply lines are missing.

## FJ-024 architecture

1. swe, 117:4812, 22, PASS
2. deepseek, 118:4935, 22, PASS
3. luna, 169:6116 and 169:6297, 22, FAIL
4. opus-low, 1:3, 21, PASS
5. glm, 119:5058, 21, FAIL

Luna's two boards score 22 together, but the run split the request into two diagrams of 5 and 4 lanes instead of cutting file storage. That misses the scenario's 9 of 9 and 6 of 6 count, and luna ranks third only because the rule orders by total before verdict. Opus-low passes with one crossing, which its own reply reports, but it merged the desktop and web clients to keep file storage. Its `Left out:` lines name the fan-out to awake clients and a direct Apple push to iOS connector. The scenario's push path still ends at Apple Push, so that costs it nothing.

## FJ-025 sequence

1. glm, 122:4181, 22, PASS
2. swe, 123:4329 and 124:4477, 22, PASS
3. deepseek, 121:4040, 22, PASS
4. luna, 170:6282 and 170:6516, 21, FAIL
5. opus-low, 1:3 and 2:151, 20, FAIL

Both new models drew the declined card as a second board, as swe did. Each read-back also lacks the start-here clause a two-board delivery needs. Luna also posted its playback and gate as interim messages in turn 1 and added an `Extensions:` line for parts the composer draws. Opus-low also left its model and code in /tmp/fj025 and trimmed the composer code to about 14,000 characters.

## FJ-026 state

1. glm, 126:4597, 22, PASS
2. luna, 171:6550, 20, FAIL
3. swe, 129:4747, 19, FAIL
4. opus-low, 1:3, 18, FAIL
5. deepseek, 131:5009, 16, FAIL

Luna draws the Confirmed composite cleanly but loses Signal for a pink accent on Completed alone and Reply for an `Extensions:` line describing composer parts. Opus-low flattened Confirmed into two plain states, so the composite zone is missing. Its two cancel arrows also merge into Cancelled, its read-back is prose and its temporary model stayed on disk.

## FJ-027 ER

1. swe, 132:5151, 22, PASS
2. glm, 138:5271, 22, PASS
3. luna, 172:6667, 22, PASS
4. opus-low, 1:3, 20, FAIL
5. deepseek, 134:5211, 20, FAIL

Swe, glm and luna tie at 22 with no supplementary turn. Luna is placed third because every attribute type on its board reads unknown. That is honest, since it would not copy the worked example's types as schema facts, but it is harder to read. Opus-low ranks above deepseek on the same total because it wrote nothing before the gate, while deepseek drew its board in turn 1. Opus-low showed keys only and cited a write rule the skill does not have.

## FJ-028 gantt

1. glm, 145:5350, 22, PASS
2. deepseek, 141:5330, 22, PASS
3. swe, 146:5370, 22, PASS
4. opus-low, 175:6806, 20, FAIL
5. luna, 173:6768, 19, FAIL

Both new models drew two sections where the scenario counts three. They also drew dependency arrows that meet at the end of the sync engine bar, which is a composer routing limit. Luna ranks last because an Android sticky call resized the composed section and it marked the whole design chain critical. Opus-low marked only integration and left Android out by name.

## Where I would score the first run differently

- **FJ-022 swe.** I would give Legibility 2, not 1. "Within 30" over "days?" breaks at a word boundary. The run still fails on Reply.
- **FJ-028, all three.** None of the deepseek, glm or swe boards draws a dependency arrow, so Q2 can only be answered from how the bars line up in time. That is not a scored dimension and I would keep the totals.
- **FJ-027 swe and glm.** Their columns and types come from the worked example (`assets/examples/er-roamstay-stays.md`), not from a schema the request supplied. I would note this as sourcing, not score it.
- **Everything else.** After looking at every render, I agree with the other scores.

## Overall

| Model | Total of 154 | Passes | Mean turns |
|---|---|---|---|
| glm | 148 | 5 | 3.00 |
| swe | 147 | 4 | 3.00 |
| deepseek | 144 | 5 | 3.00 |
| luna | 142 | 2 | 3.57 |
| opus-low | 139 | 1 | 3.00 |

Luna's mean comes from 25 turns over seven runs: two adaptive turns on FJ-024, one on FJ-027 and one supplementary turn on FJ-022.

**Best model.** On the ranking rule, glm is the best model overall. It has the highest total at 148 and ties deepseek for the most passes at five, with full marks on five of the seven scenarios.

**Runner-up.** Swe is one point behind with four passes. Like luna and opus-low, it never wrote before a gate's yes and never touched a node it did not draw, which glm and deepseek cannot say.

**The caveat on glm.** Its FJ-024 run deleted ten sections it never created, including two other models' boards. The scorecard prices that at one Hygiene point. Weighed as the harm it is, swe would rank first.

**The two new models.** Luna beats opus-low by three points and one pass. Luna kept to the pinned file, read its sources more deeply and cleaned up its temporary files in six of seven runs. Its losses come from turn shape: stops posted as interim messages, a playback merged into a gate and an undelivered FJ-023. Opus-low held every stop in exactly three turns but lost seven Hygiene points:

- It left a temporary model on disk in six runs.
- It resized one composed section.
- It trimmed the composer code in three runs.
- It repeated a rule that Flow Mode only writes into files it created, which the skill does not contain.

The extra sentence allowing a new file in drafts let opus-low avoid the pinned file in six runs. That costs it no point, but it never needed to.
