# Grader brief, rerun after phase 035 (2026-10-25)

You grade finished scenario runs of the Product Owner FigJam skill against its manual testing playbook. You read evidence and write grades. You change no file outside the output path your task names, you call no Figma tool and you open no Figma or Barter board.

## Paths

- System root (call it PO): `/Users/michelkerkmeester/MEGA/Development/AI Systems/AI Systems/Product Owner`
- Run folder (call it RUN): `PO/benchmark/reports/2026-10-25--manual-testing-playbook--first-glance-and-routing`
- Scratchpad (call it SP): `/private/tmp/claude-501/-Users-michelkerkmeester-MEGA-Development-AI-Systems/348b59cb-58a2-4b49-8147-c40143312bc1/scratchpad`
- Playbook root: `PO/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md`. Section 3 is the board quality scorecard (22 points, pass at 18 with Composition, Fidelity, Reply and all four Hygiene checks at full marks and no dimension at 0). Section 4 tells the operator how to answer an intake round. Each scenario file is under `PO/sk-create-figjam/manual-testing-playbook/<group>/<slug>.md` and holds the prompt, the turns, the expected signals and the PASS or FAIL line. Read the current files, which are the versions this run used.
- Skill contract the run followed: `PO/sk-create-figjam/SKILL.md`, `PO/sk-create-figjam/references/flow-mode.md` (stops, the outline pass under Section 2, the reply shape in Section 8), `PO/sk-create-figjam/references/quality-rubric.md` and `PO/sk-create-figjam/references/style-guide.md` (the single pink accent and the `%% focus:` line).

## What changed before this run

Phase 035 changed the skill and its composer: a user flow and a process need exactly one `style` line on the first-glance node, the other types may name it with `%% focus:`, the accent is an 8 px pink outline on top of the node's own kind colour, architecture lanes run client, gateway, service, async, datastore and external, no edge runs along a zone border or through a zone it does not join, and the reply carries one `Finding:` line per finding or question with the self-scan last. The previous grades of the same 18 scenarios (rerun after phase 034) are in `SP/grade/g4-rerun-a.jsonl`, `g4-rerun-b.jsonl` and `g4-rerun-c.jsonl`, with the Composition second lens in `SP/grade/g6-composition-second-lens.md`. Name every scenario whose verdict or score changed and why.

## Evidence per scenario

- Runtime: all 18 scenarios ran on 2026-10-25 through the Claude Code CLI (`claude -p`, model `claude-sonnet-5-5` at effort high) with Figma's hosted MCP server, one fresh sandbox per scenario. Tool names look like `mcp__figma-remote__use_figma`.
- Driver: `RUN/run/adaptive_scenario.py` sends the scenario's scripted turns in order. When a reply was an intake round it first sent "Use your recommended answers." (at most twice per scenario), as each scenario's command list and playbook Section 4 tell the operator to. A small classifier labelled each reply's stop, recorded as `kind` per turn in `meta.json`. The label is a hint and is sometimes wrong (a delivery labelled PLAYBACK). Grade each reply against the stop it actually reached, not the label.
- Files: `RUN/skill/<ID> - <slug>/transcript-turn-N.md` (full transcript per turn with every tool call), `events-turn-N.jsonl`, `meta.json` (turn inputs, kinds, Figma calls) and `RUN/replies/<ID>-turnN.txt` (the reply text).
- Supplementary turns: FJ-036 stopped at four proposals of the outline pass (outline, framings, sketch, look) before its gate, so after its scripted turns the operator sent "Yes, go ahead." four more times. They are `turn-supplementary-1.md` to `turn-supplementary-4.md`, `events-turn-supplementary-N.jsonl`, `RUN/replies/FJ-036-turn-supplementary-N.txt` and `supplementary_turns` in its `meta.json`. Grade FJ-036's stop discipline on the scripted turns and its board and delivery on the supplementary turns. Check `PO/sk-create-figjam/references/flow-mode.md` "The outline pass": it says each proposal waits for a yes and also that "An unanswered proposal never stops the run". Say whether the run followed the contract and whether the contract or the scenario is the defect.
- Screenshots: full size at 100% in `SP/shots035/full/<node>.png`, overview (longest edge 2048 px) in `SP/shots035/ov/<node>.png`, greyscale in `SP/shots035/grey/<node>.png`. Node ids use a dash in file names, so board 88:2284 is `88-2284.png`. All were rendered through the Figma REST API after the run.
- Clarity: a fresh reader answered each scored board's questions from the colour screenshots only. Answers in `SP/grade/r035-reader-answers.md`, key in `SP/grade/r035-reader-answer-key.txt` (one line per scenario with its set letter). Score Clarity from those two files.

## Boards on the test file

FJ-017 88:2099, FJ-019 88:2397, FJ-022 88:2284, FJ-023 90:2620, FJ-024 90:2398, FJ-025 91:2621 and 92:2769, FJ-026 93:2889, FJ-027 93:3130, FJ-028 94:3122, FJ-029 95:3255 and 96:3259, FJ-030 95:3142, FJ-031 96:3371 (setup board, deleted by the run after its own yes, so it has no screenshot) and 98:3478 (the revision), FJ-032 97:3363, FJ-033 99:3478, FJ-034 100:3529, FJ-036 101:3599. FJ-039 and FJ-041 end at a gate by design and wrote nothing.

## Known harness facts, not model faults

- All boards share one test file, and it was not cleared between scenarios. A same-title board from an earlier scenario of this run can look like a revision, and a delete turn can find several same-title sections. Count neither against the model. Judge how it handled them.
- The runner appended a file pin line ("Write the board into the existing FigJam file with key ... rather than a new file.") to every first turn.
- Board URLs, emails, plan names the operator owns and the file key are redacted in the run folder only after grading. A redacted URL in first position counts as the URL.
- A `Finding:` line saying the `figma-use` skills could not be loaded is a sandbox fact. Judge whether the line is a useful finding, not whether the skills loaded.
- Operator observation to check, not truth: the key on several boards shows `In focus` as a light pink filled swatch with the pink outline, while the board's accent is the pink outline on a node that keeps its own kind colour (a green goal, a white entity). Decide whether that is a Signal or Legibility loss on each board where it shows.

## How to grade

1. Read the scenario file. Grade every expected signal against the transcript, citing the turn and the line.
2. For a scored board, fill the full 22-point scorecard. Every point lost names a location (the shape or connector by its label and where it sits in the frame) and a fix (a model change composed again after a yes, or a composer limit). For Crossings, Shared trunks, Label collisions and Legibility, say whether the model or the composer caused the loss. Look at the screenshots yourself and read the full-size file to zoom.
3. Glance order: use the read-back line's `first glance:` when present, else the styled or focus node, else the request's subject, and say which you used.
4. Hygiene: "nothing exported" fails when the transcript shows a file written to `export/` or a Mermaid, HTML, SVG or PNG file left behind. "No node touched" fails when a tool call edited a composed node after the compose. "Nothing else changed" fails when a call changed or deleted a node the run did not create, except a delete the scenario asks for after its own yes.
5. Verdict: PASS, FAIL or SKIP per the scenario's PASS line, with one sentence of reason. A verdict without evidence is not allowed.

## Output

Write one JSON line per scenario to the output file your task names, with keys `id`, `set` (always `rerun-035`), `verdict`, `reason`, `evidence` (relative paths), `scorecard` (object with the 13 scored items and `total`, or null when the scenario has no scored board), `losses` (list of {item, location, fix, cause}), `signals` (list of {signal, met, cite}) and `change` (one sentence on what changed against the phase 034 grade of the same scenario). Then write a short markdown summary next to it with the same file name and `.md`. No em dashes, no semicolons and no serial comma in anything you write.
