# Grader brief, three-model comparison after phase 037 (2026-10-25)

You grade finished scenario runs of the Product Owner FigJam skill against its manual testing playbook. Each task gives you one board-quality scenario run on three models. You grade all three runs on one scale and rank them. You read evidence and write grades. You change no file outside the output paths your task names, you call no Figma tool and you open no Figma or Barter board.

## Paths

- System root (call it PO): `/Users/michelkerkmeester/MEGA/Development/AI Systems/AI Systems/Product Owner`
- Run folder (call it RUN): `PO/benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison`
- Renders (call it SHOTS): `/private/tmp/claude-501/-Users-michelkerkmeester-MEGA-Development-AI-Systems/348b59cb-58a2-4b49-8147-c40143312bc1/scratchpad/r038/shots`
- Playbook root: `PO/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md`. Section 3 is the board quality scorecard: 22 points, pass at 18 with Composition, Fidelity, Reply and all four Hygiene checks at full marks and no dimension at 0. Section 4 tells the operator how to answer an intake round. Each scenario file is under `PO/sk-create-figjam/manual-testing-playbook/board-quality/<slug>.md` and holds the prompt, the turns, the expected signals and the PASS or FAIL line.
- Skill contract the runs followed: `PO/sk-create-figjam/SKILL.md`, `PO/sk-create-figjam/references/flow-mode.md` (stops and the reply shape in Section 8), `PO/sk-create-figjam/references/quality-rubric.md`, `PO/sk-create-figjam/references/style-guide.md` and the active design `PO/sk-create-figjam/assets/figjam-design.md`, which Signal reads.

## What changed before this run

Phase 037 moved every board's look into `figjam-design.md` and applied eighteen design fixes: pink out of the zone tints, zone tints that skip member hues and any zone beside them, white sequence participants, one key order per type with the focus last, a key as wide as the diagram, gray connectors except async and the accent, 18 px labels with a 14 px small step, routes kept inside the diagram, step pins beside the sender's lifeline and a balanced subtitle. A `DESIGN` warning in a compose's output becomes a `Finding:` line in the reply. The shipped design file draws with no warning.

## The runs

- Models: `deepseek` is DeepSeek V4.1 Flash Max (`deepseek-v4-1-flash-1017-max`), `glm` is GLM 5.3 Flash Max (`glm-5-3-flash-max`) and `swe` is SWE 2 Max (`swe-2-max`). All three ran through the Devin CLI with Figma's hosted MCP server, one fresh sandbox per run, one run at a time.
- Driver: `RUN/run/adaptive_compare.py` sent the scenario's scripted turns in order. After a reply that was an intake round it first sent "Use your recommended answers." (role `adaptive`, at most twice). When the script ran out with no composed board it sent "Yes, go ahead." (role `supplementary`, at most three times). Each turn's `role` and the classifier's `kind` are in `meta.json`. The kind is a hint and can be wrong. Grade each reply against the stop it actually reached.
- Files per run: `RUN/skill/<model>/<ID> - <slug>/` holds `transcript-turn-N.md` (every tool call, arguments cut at 600 characters and results at 1,500), `export-turn-N.json` (the full Devin export, redacted, which holds every tool call in full), `turn-N.md` (the reply) and `meta.json` (inputs, roles, kinds, Figma calls and `boards`, the board ids each compose returned). A `use_figma` call whose code holds `const MODEL` is a compose.
- Renders: `SHOTS/full/<model>-<ID>-<node>.png` at 100%, `SHOTS/ov/...` with its longest edge at 2048 px or less and `SHOTS/grey/...` in greyscale, where node ids use a dash. Your task lists the board each run left and its files.
- Clarity: three fresh readers each answered one board of every scenario from its colour renders alone, rotated so no reader saw two boards of one scenario. Answers are in `SHOTS/../grades/reader-answers-<n>.md` and the key is in `SHOTS/../grades/reader-key.md`. Score Clarity from those two files.

## Known harness facts, not model faults

- Every run writes to one fictional test FigJam file that already holds boards from earlier runs. A same-title board from an earlier run can look like a revision. Count it against no model. Judge how the run handled it.
- The driver appended a file pin line ("Write the board into the existing FigJam file with key ... rather than a new file.") to every first turn. Writing into that file is correct.
- Board URLs, emails and the file key may be redacted in the run folder. A redacted URL in first position counts as the URL.
- A turn the script does not hold is not a fault on its own. Record how many adaptive and supplementary turns each run needed and where each one stopped.

## How to grade

1. Read the scenario file. Grade every expected signal against each run's transcript, citing the turn and the line.
2. Fill the full 22-point scorecard for each run that wrote a board. Every point lost names a location (the shape or connector by its label and where it sits in the frame) and a fix (a model change composed again after a yes, or a composer limit). For Crossings, Shared trunks, Label collisions and Legibility, say whether the model or the composer caused the loss. Look at the renders yourself and read the full-size file to zoom.
3. Glance order: use the read-back line's `first glance:` when present, else the styled or focus node, else the request's subject, and say which you used.
4. Hygiene: "nothing exported" fails when the transcript shows a file written to `export/` or a Mermaid, HTML, SVG or PNG file left behind. "No node touched" fails when a call edited a composed node after the compose. "Nothing else changed" fails when a call changed or deleted a node the run did not create.
5. Anything written before the gate's yes fails the scenario. A second compose of the same board counts against Hygiene only when it changed a node the first one drew.
6. Verdict per run: PASS, FAIL or SKIP per the scenario's PASS line, with one sentence of reason. A run that wrote no board scores no scorecard and fails, with the stop it ended on.
7. Rank the three boards of your scenario best first, by total, then pass over fail, then fewer supplementary turns, and say in two sentences what separates them.

## Output

Write one JSON line per run to the `.jsonl` path your task names, with keys `id`, `model`, `board`, `verdict`, `reason`, `evidence` (relative paths), `scorecard` (an object with `composition`, `crossings`, `shared_trunks`, `label_collisions`, `fidelity`, `legibility`, `signal`, `clarity`, `hygiene_no_node_touched`, `hygiene_no_label_covered`, `hygiene_nothing_else_changed`, `hygiene_nothing_exported`, `reply` and `total`, or null when no board was written), `losses` (a list of {item, location, fix, cause}), `signals` (a list of {signal, met, cite}), `turns` ({scripted, adaptive, supplementary}) and `rank` (1 to 3). Then write a short markdown summary at the `.md` path your task names: a table of the three runs and a paragraph on what decided the ranking. No em dashes, no semicolons and no serial comma in anything you write.
