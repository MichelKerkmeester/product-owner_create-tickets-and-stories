# Grader brief, rerun on Claude Sonnet 5.5 high after phase 040 (2026-10-26)

You grade the 31 FigJam scenario runs that Claude Sonnet 5.5 at high effort made again on `sk-create-figjam` v1.0.6.0, the 29 that failed and the 2 that were skipped on v1.0.5.0, plus three gallery runs of FJ-022, FJ-023 and FJ-028 that fill the screenshot gallery. You are the one grader for every run, so every score sits on one scale. You read evidence and write grades. You change no file outside the output paths named below, you call no Figma tool and you open no Figma or Barter board.

## Paths

- System root (call it PO): `/Users/michelkerkmeester/MEGA/Development/AI Systems/AI Systems/Product Owner`
- Run folder (call it RUN): `PO/benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison`
- Work folder (call it WORK): `/private/tmp/claude-501/-Users-michelkerkmeester-MEGA-Development-AI-Systems/348b59cb-58a2-4b49-8147-c40143312bc1/scratchpad/r040`
- Renders: `WORK/shots/full/<label>-<ID>-<node>.png` at 100%, `WORK/shots/ov/...` with its longest edge at 2048 px or less and `WORK/shots/grey/...` in greyscale. Node ids use a dash. `WORK/boards.json` lists every board each run composed, with its turn.
- Playbook root: `PO/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md`. Section 3 is the board scorecard: 22 points, pass at 18 with Composition, Fidelity, Reply and all four Hygiene checks at full marks and no dimension at 0. Each scenario file sits under `PO/sk-create-figjam/manual-testing-playbook/<category>/<slug>.md` and holds the prompt, the turns, the expected signals and the PASS or FAIL line. The run's `meta.json` names its scenario file.
- Skill contract the runs followed: `PO/sk-create-figjam/SKILL.md`, `PO/sk-create-figjam/references/flow-mode.md`, `PO/sk-create-figjam/references/quality-rubric.md`, `PO/sk-create-figjam/references/style-guide.md` and the active design `PO/sk-create-figjam/assets/figjam-design.md`.
- Per-run files: `RUN/skill/sonnet-high-rerun/<ID> - <slug>/` and `RUN/skill/sonnet-high-gallery/<ID> - <slug>/` holds `transcript-turn-N.md`, `export-turn-N.jsonl` (the full Claude Code stream with every tool call), `turn-N.md` (the reply) and `meta.json` (inputs, roles, the classifier's `kind` per turn, Figma calls and `boards`).
- Signal checks: `WORK/checks/<ID>.json` holds an independent checker's reading of every expected signal of that scenario, each with a cite. Treat it as a hypothesis: confirm or overturn each item against the transcript.
- Clarity: `WORK/readers/<ID>-<node>.md` holds a fresh reader's answers from the colour renders alone. Score Clarity from them against the scenario's question and the model.

## Harness facts, not model faults

- Eight lanes ran at once, no earlier than 22:00 UTC. Lane 1 wrote into the fictional test file, which already holds boards from earlier runs, and ran FJ-031 and FJ-032 there. Lanes 2 to 8 each wrote into their own new empty FigJam file in drafts of the operator's team plan. Writing into the pinned file is correct. A scenario marked `driver: new-file` ran with no file pin.
- The first turn carried a file pin line and a drafts line that allowed a new file in drafts if one was needed.
- The driver sends a scenario's own scripted answer straight after an intake reply, and the generic "Use your recommended answers." only once the script has none left (role `adaptive`). It sends "Yes, go ahead." after a stop with no board (role `supplementary`) only in a scenario that expects a board. FJ-009 ran with no Figma server, as its precondition says. Count driver turns against no model.
- The driver performs no operator step. FJ-018, FJ-035, FJ-044 and FJ-045 are marked `driver: operator-only` and were skipped: grade each SKIP with that reason. FJ-031 and FJ-032 ran without their operator setup step: grade what the run could do, mark each signal that depends on a missing operator step as `harness` rather than unmet, and say so in the reason. The driver ran each scenario's read-only `Commands` steps afterwards and recorded them in `commands.json`.
- Board URLs, emails and file keys may be redacted in the run folder later. A redacted URL in first position counts as the URL.

## How to grade

1. For every scenario, read the scenario file and grade every expected signal against the transcript, citing the turn and the line. Start from the checker's reading in `WORK/checks/<ID>.json` and say where you overturn it.
2. For every run that composed a board, fill the full 22-point scorecard. Every point lost names a location (the shape or connector by its label and where it sits in the frame) and a fix. For Crossings, Shared trunks, Label collisions and Legibility say whether the model or the composer caused the loss. Look at the renders yourself and open the full-size file to zoom.
3. Glance order: use the read-back line's `first glance:` when present, else the styled or focus node, else the request's subject, and say which you used.
4. Hygiene: "nothing exported" fails when a file was written to `export/` or a Mermaid, HTML, SVG or PNG file was left behind. "No node touched" fails when a call edited a composed node after the compose, except the board section a gated extension widens to hold its notes. "Nothing else changed" fails when a call changed or deleted a node the run did not create.
5. Anything written before the gate's yes fails the scenario. A delete on a reply that does not name the boards fails it too.
6. Verdict per run: PASS, FAIL or SKIP per the scenario's PASS line and the root playbook's rule that a board scenario passes only when its scorecard passes and every expected signal is present. Give one sentence of reason. A board scenario that wrote no board fails, with the stop it ended on.
7. Note any behaviour that points at a skill gap rather than a model slip: the rule it touches, the file and section, and the evidence.

## Output

- `RUN/grades/sonnet-high-rerun.jsonl`: one JSON line for each of the 31 rerun scenarios, and `RUN/grades/sonnet-high-gallery.jsonl`: one line for each of the three gallery runs, each with keys `id`, `model` ("sonnet-high-rerun" or "sonnet-high-gallery"), `boards`, `verdict`, `reason`, `evidence` (relative paths), `scorecard` (an object with `composition`, `crossings`, `shared_trunks`, `label_collisions`, `fidelity`, `legibility`, `signal`, `clarity`, `hygiene_no_node_touched`, `hygiene_no_label_covered`, `hygiene_nothing_else_changed`, `hygiene_nothing_exported`, `reply` and `total`, or null when no board was written), `losses` (a list of {item, location, fix, cause}), `signals` (a list of {signal, met, cite}, where met is true, false or "harness"), `turns` ({scripted, adaptive, supplementary}) and `skill_gaps` (a list of {rule, file, evidence}).
- `RUN/grades/sonnet-high-rerun.md`: a short summary. A table of the 31 reruns with the v1.0.5.0 verdict from `RUN/grades/sonnet-high.jsonl` beside the new verdict and total, the pass count by category, the three gallery runs with their totals against their v1.0.5.0 scores, then each remaining failure with its cause, model slip or skill gap. End with the skill gaps the rerun still shows, most important first.
- No em dashes, no semicolons and no serial comma in anything you write. No file keys, board URLs or plan names.
