# Grader brief, rerun on Claude Sonnet 5.5 high after phase 042 (2026-10-27)

You grade the 14 FigJam scenarios that failed on `sk-create-figjam` v1.0.7.0, run again on v1.0.8.0 by Claude Sonnet 5.5 at high effort: FJ-009, FJ-017, FJ-023, FJ-026, FJ-029, FJ-031, FJ-032, FJ-033, FJ-034, FJ-036, FJ-038, FJ-040, FJ-042 and FJ-045. You are the one grader for every run, so every score sits on one scale. You read evidence and write grades. You change no file outside the output paths named below, you call no Figma tool and you open no Figma or Barter board.

## Paths

- System root (call it PO): `/Users/michelkerkmeester/MEGA/Development/AI Systems/AI Systems/Product Owner`
- Run folder (call it RUN): `PO/benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison`
- Work folder (call it WORK): `/private/tmp/claude-501/-Users-michelkerkmeester-MEGA-Development-AI-Systems/348b59cb-58a2-4b49-8147-c40143312bc1/scratchpad/r042`
- Renders: `WORK/shots/full/sonnet-high-042-<ID>-<node>.png` at 100%, `WORK/shots/ov/...` with its longest edge at 2048 px or less and `WORK/shots/grey/...` in greyscale. Node ids use a dash. The same full-size files are in `RUN/renders/`. `sonnet-high-042-FJ-032-page.png` joins FJ-032's prepared retro section and its new board at their page positions.
- Playbook root: `PO/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md`, now v1.0.7.0. Section 3 is the board scorecard: 22 points, pass at 18 with Composition, Fidelity, Reply and all four Hygiene checks at full marks and no dimension at 0. Each scenario file sits under `PO/sk-create-figjam/manual-testing-playbook/<category>/<slug>.md` and holds the prompt, the turns, the expected signals and the PASS or FAIL line. The run's `meta.json` names its scenario file.
- Skill contract the runs followed: `PO/sk-create-figjam/SKILL.md`, `PO/sk-create-figjam/references/flow-mode.md`, `PO/sk-create-figjam/references/quality-rubric.md`, `PO/sk-create-figjam/references/style-guide.md`, the type references under `PO/sk-create-figjam/references/types/` and the active design `PO/sk-create-figjam/assets/figjam-design.md`.
- Per-run files: `RUN/skill/sonnet-high-042/<ID> - <slug>/` holds `transcript-turn-N.md`, `export-turn-N.jsonl` (the full Claude Code stream with every tool call), `turn-N.md` (the reply), `meta.json` (inputs, roles, the classifier's `kind` per turn, Figma calls, `boards` and `file_start_sections`) and `commands.json`.
- Clarity: `WORK/readers/<ID>-<node>.md` holds a fresh reader's answers from the colour renders alone. Each reader was given the scenario's persona and its Q1 to Q3 word for word, without the answers, and a split's reader saw both boards together. Score Clarity from those answers against the scenario's answers.
- v1.0.7.0 verdicts: `RUN/grades/sonnet-high-041.jsonl`.

## Rules v1.0.8.0 changed in the playbook

- Composition: on a state board a composite section reads as part of the frame, like the title block, and never counts as a part. A part the plan does not name that reads at or before the planned second glance costs one point, as one part read out of order does.
- `references/types/state.md`: with no state named, the first state is planned first, the end states second and the states inside a composite last. With a state named, the focus line marks it first and the first state is planned second.
- `references/quality-rubric.md`: the light blue entry joins the kinds that read right after the accent, and every one the board draws is planned in the second glance line unless the accent sits on it.
- `Left out:` appears in the reply whenever the board does not hold a cut, a split, a later board or a point the sources left open, and the gate carries the same line.
- FJ-009: turn 2 ends on the gate, which names the missing route, and turn 3 is the missing-route reply. FJ-029: the first title is `1. Sign up`. FJ-038: the PASS line asks the reply to say the old section is deleted only on a second yes after the new board's read-back. FJ-045: the goal is light green and not pink, the read-back names the accented node as the first glance and the scenario now names Q1 to Q3.
- A single sticky goes past its node's end dot, takes the side with the shortest clear line when every side is taken and says so on a `Finding:` line, and is never moved without a new yes.
- FJ-017 is a board-write scenario and carries no scorecard. It passes or fails on its own signals. Its `scorecard` is null.

## Harness facts, not model faults

- Every board scenario wrote into its own new FigJam file in drafts of the operator's team plan, created before its first turn. `file_start_sections` in `meta.json` is the number of sections the file held before the first turn: 0 for a new empty file, 1 for FJ-032, whose file held one prepared retro section. Scenarios that write no board shared one file. FJ-017 is a new-file scenario: it ran with no file pin, created its own file and that is correct. Each pinned run received exactly one destination.
- The driver sends a scenario's own scripted answer straight after an intake reply and the generic "Use your recommended answers." only once the script has none left (role `adaptive`). It sends "Yes, go ahead." after a stop with no board (role `supplementary`) only in a scenario that expects a board. FJ-009 ran with no Figma server, as its precondition says. Count driver turns against no model.
- The launch moved earlier runs' fictional-brand scratch files out of `/tmp` before the lanes started, so no run could find another's files.
- FJ-031 paused before its third turn. The operator added one sticky, `Operator note: check return window wording with support`, to the right of the first board, then the run resumed (`operator_paused` true in `meta.json`). That sticky is the operator's node, so any change to it counts against "nothing else changed". FJ-031's first board was deleted by its own scripted turns and has no render.
- FJ-032's prompt placeholder for the prepared board's file was filled with that file, so the run had one destination.
- FJ-045: the operator did steps 1 and 2 before the model turns. The design file was broken with a pink zone tint, a light pink goal and a shadow group, and the design check printed three `DESIGN` lines for `shadow`, `role.goal` and `zone.cycle` and exited 1 (`WORK/fj045/step2.txt`). The driver then ran the model turns (`operator_setup_done` true). After the run the operator restored the design file and `git diff --exit-code` on it exited 0.
- Board URLs, emails and file keys are redacted in the run folder. A redacted URL in first position counts as the URL.

## How to grade

1. For every scenario, read the scenario file and grade every expected signal against the transcript, citing the turn and the line.
2. For every scored board that was composed, fill the full 22-point scorecard. FJ-017 and the other board-write scenarios carry a null scorecard. Every point lost names a location (the shape or connector by its label and where it sits in the frame) and a fix. For Crossings, Shared trunks, Label collisions and Legibility say whether the model or the composer caused the loss. Look at the renders yourself and open the full-size file to zoom.
3. Glance order: use the read-back line's `first glance:` when present, else the styled or focus node, else the request's subject, and say which you used.
4. Hygiene: "nothing exported" fails when a file was written to `export/` or a Mermaid, HTML, SVG or PNG file was left behind, except the paired re-save. "No node touched" fails when a call edited a composed node after the compose, except the board section a gated extension widens to hold its notes. "Nothing else changed" fails when a call changed or deleted a node the run did not create.
5. Anything written before the gate's yes fails the scenario. A delete on a reply that does not name the boards fails it too.
6. Verdict per run: PASS, FAIL or NOT RUN per the scenario's PASS line and the root playbook's rule that a board scenario passes only when its scorecard passes and every expected signal is present. Give one sentence of reason. A board scenario that wrote no board fails, with the stop it ended on.
7. Note any behaviour that points at a skill gap rather than a model slip: the rule it touches with its file and section and the evidence. Say for each v1.0.8.0 fix the scenario exercises whether the run shows it working.

## Output

- `RUN/grades/sonnet-high-042.jsonl`: exactly 14 JSON lines, one for each of FJ-009, FJ-017, FJ-023, FJ-026, FJ-029, FJ-031, FJ-032, FJ-033, FJ-034, FJ-036, FJ-038, FJ-040, FJ-042 and FJ-045, each with keys `id`, `model` ("sonnet-high-042"), `boards`, `verdict`, `reason`, `evidence` (relative paths), `scorecard` (an object with `composition`, `crossings`, `shared_trunks`, `label_collisions`, `fidelity`, `legibility`, `signal`, `clarity`, `hygiene_no_node_touched`, `hygiene_no_label_covered`, `hygiene_nothing_else_changed`, `hygiene_nothing_exported`, `reply` and `total`, or null when no board was written or the scenario has no scorecard), `losses` (a list of {item, location, fix, cause}), `signals` (a list of {signal, met, cite}, where met is true, false or "harness"), `turns` ({scripted, adaptive, supplementary}) and `skill_gaps` (a list of {rule, file, evidence}).
- `RUN/grades/sonnet-high-042.md`: a short summary. A table of the 14 scenarios with the v1.0.7.0 verdict and total beside the new verdict and total, the pass count, then each remaining failure with its cause, model slip or skill gap. End with the skill gaps the rerun still shows, most important first.
- No em dashes, no semicolons and no serial comma in anything you write. No file keys, board URLs or plan names.
