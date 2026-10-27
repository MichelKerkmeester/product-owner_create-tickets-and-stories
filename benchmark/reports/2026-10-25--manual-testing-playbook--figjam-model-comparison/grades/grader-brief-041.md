# Grader brief, rerun on Claude Sonnet 5.5 high after phase 041 (2026-10-27)

You grade the FigJam scenarios that did not pass on `sk-create-figjam` v1.0.6.0, run again on v1.0.7.0 by Claude Sonnet 5.5 at high effort. They are the 13 v1.0.6.0 rerun failures, the gallery FJ-023 that failed at 20, the two operator scenarios FJ-044 and FJ-045 and the two Figma Desktop scenarios FJ-018 and FJ-035, which were not run. You are the one grader for every run, so every score sits on one scale. You read evidence and write grades. You change no file outside the output paths named below, you call no Figma tool and you open no Figma or Barter board.

## Paths

- System root (call it PO): `/Users/michelkerkmeester/MEGA/Development/AI Systems/AI Systems/Product Owner`
- Run folder (call it RUN): `PO/benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison`
- Work folder (call it WORK): `/private/tmp/claude-501/-Users-michelkerkmeester-MEGA-Development-AI-Systems/348b59cb-58a2-4b49-8147-c40143312bc1/scratchpad/r041`
- Renders: `WORK/shots/full/sonnet-high-041-<ID>-<node>.png` at 100%, `WORK/shots/ov/...` with its longest edge at 2048 px or less and `WORK/shots/grey/...` in greyscale. Node ids use a dash. The same full-size files are in `RUN/renders/`. `sonnet-high-041-FJ-032-page.png` joins FJ-032's prepared retro section and its new board at their page positions.
- Playbook root: `PO/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md`, now v1.0.6.0. Section 3 is the board scorecard: 22 points, pass at 18 with Composition, Fidelity, Reply and all four Hygiene checks at full marks and no dimension at 0. Each scenario file sits under `PO/sk-create-figjam/manual-testing-playbook/<category>/<slug>.md` and holds the prompt, the turns, the expected signals and the PASS or FAIL line. The run's `meta.json` names its scenario file.
- Skill contract the runs followed: `PO/sk-create-figjam/SKILL.md`, `PO/sk-create-figjam/references/flow-mode.md`, `PO/sk-create-figjam/references/quality-rubric.md`, `PO/sk-create-figjam/references/style-guide.md`, the type references under `PO/sk-create-figjam/references/types/` and the active design `PO/sk-create-figjam/assets/figjam-design.md`.
- Per-run files: `RUN/skill/sonnet-high-041/<ID> - <slug>/` holds `transcript-turn-N.md`, `export-turn-N.jsonl` (the full Claude Code stream with every tool call), `turn-N.md` (the reply), `meta.json` (inputs, roles, the classifier's `kind` per turn, Figma calls, `boards` and `file_start_sections`) and `commands.json`.
- Clarity: `WORK/readers/<ID>-<node>.md` holds a fresh reader's answers from the colour renders alone. Score Clarity from them against the scenario's question and the model.
- v1.0.6.0 verdicts: `RUN/grades/sonnet-high-rerun.jsonl` and, for FJ-023, `RUN/grades/sonnet-high-gallery.jsonl`.

## Rules v1.0.7.0 changed in the playbook

- Composition scores 2 when the request names a group and its most telling member, marked by the focus line, comes first. When `quality-rubric.md` Section 3 makes the requested element the second glance, as on a revision that changes an end other than a failure end, the board scores 2 when that element holds the planned second glance.
- Signal accepts an accent that `quality-rubric.md` Section 3 keeps on the goal in that same case.
- Fidelity is scored against the run's own checked model. A count or label the scenario expects and the model left out is an expected-signal miss, not a Fidelity loss.
- Hygiene, nothing exported, allows the paired artifact's own re-save at its existing export path.
- FJ-020 now has a second scripted turn, `The FigJam board.`, after which the reply asks only the board facts the sources leave open, or the type question alone, and writes nothing.

## Harness facts, not model faults

- Every board scenario wrote into its own new FigJam file in drafts of the operator's team plan, created before its first turn. `file_start_sections` in `meta.json` is the number of sections the file held before the first turn: 0 for a new empty file, 1 for FJ-032, whose file held one prepared retro section. Scenarios that write no board shared one file. FJ-017 is a new-file scenario: it ran with no file pin, created its own file and that is correct. Each pinned run received exactly one destination.
- The driver sends a scenario's own scripted answer straight after an intake reply and the generic "Use your recommended answers." only once the script has none left (role `adaptive`). It sends "Yes, go ahead." after a stop with no board (role `supplementary`) only in a scenario that expects a board. FJ-009 ran with no Figma server, as its precondition says. Count driver turns against no model.
- FJ-031 paused before its third turn. The operator added one sticky, `Operator note: check return window wording with support`, to the right of the first board, then the run resumed (`operator_paused` true in `meta.json`). That sticky is the operator's node, so any change to it counts against "nothing else changed". FJ-031's first board was deleted by its own scripted turns and has no render. The sticky's render is `sonnet-high-041-FJ-031-2-66.png`.
- FJ-032's prompt placeholder for the prepared board's file was filled with that file, so the run had one destination.
- FJ-045: the operator did steps 1 and 2 before the model turns. The design file was broken with a pink zone tint, a light pink goal and a shadow group, and the design check printed three `DESIGN` lines for `shadow`, `role.goal` and `zone.cycle` and exited 1 (`WORK/fj045/step2.txt`). The driver then ran the model turns (`operator_setup_done` true). After the run the operator restored the design file and `git diff --exit-code` on it exited 0.
- FJ-044 is operator-only and has no run folder. The operator ran it in full: `WORK/fj044/step1.txt` (design check), `WORK/fj044/step2.txt` (the seven `COMPOSED` lines, and the recomposed files match the sent files byte for byte), `WORK/fj044/step3.txt` (the seven call results) and the seven renders `sonnet-high-041-FJ-044-<node>.png`. Grade it against its scenario file `board-quality/design-family-across-types.md`, scoring `Matches the active design` from `quality-rubric.md` Section 7 on each board from the renders yourself. It has no 22-point scorecard.
- FJ-018 and FJ-035 need Figma Desktop and the figma-ds-cli daemon, which this environment does not have, so they were not run by decision. Give each the verdict `NOT RUN` with a reason that starts `NOT RUN:` and names that blocker.
- Board URLs, emails and file keys are redacted in the run folder. A redacted URL in first position counts as the URL.

## How to grade

1. For every scenario, read the scenario file and grade every expected signal against the transcript, citing the turn and the line.
2. For every run that composed a board, fill the full 22-point scorecard. Every point lost names a location (the shape or connector by its label and where it sits in the frame) and a fix. For Crossings, Shared trunks, Label collisions and Legibility say whether the model or the composer caused the loss. Look at the renders yourself and open the full-size file to zoom.
3. Glance order: use the read-back line's `first glance:` when present, else the styled or focus node, else the request's subject, and say which you used.
4. Hygiene: "nothing exported" fails when a file was written to `export/` or a Mermaid, HTML, SVG or PNG file was left behind, except the paired re-save. "No node touched" fails when a call edited a composed node after the compose, except the board section a gated extension widens to hold its notes. "Nothing else changed" fails when a call changed or deleted a node the run did not create.
5. Anything written before the gate's yes fails the scenario. A delete on a reply that does not name the boards fails it too.
6. Verdict per run: PASS, FAIL or NOT RUN per the scenario's PASS line and the root playbook's rule that a board scenario passes only when its scorecard passes and every expected signal is present. Give one sentence of reason. A board scenario that wrote no board fails, with the stop it ended on.
7. Note any behaviour that points at a skill gap rather than a model slip: the rule it touches, the file and section, and the evidence. Say for each v1.0.7.0 fix the scenario exercises whether the run shows it working.

## Output

- `RUN/grades/sonnet-high-041.jsonl`: exactly 18 JSON lines, one for each of FJ-009, FJ-017, FJ-018, FJ-020, FJ-023, FJ-026, FJ-029, FJ-031, FJ-032, FJ-033, FJ-034, FJ-035, FJ-036, FJ-038, FJ-040, FJ-042, FJ-044 and FJ-045, each with keys `id`, `model` ("sonnet-high-041"), `boards`, `verdict`, `reason`, `evidence` (relative paths), `scorecard` (an object with `composition`, `crossings`, `shared_trunks`, `label_collisions`, `fidelity`, `legibility`, `signal`, `clarity`, `hygiene_no_node_touched`, `hygiene_no_label_covered`, `hygiene_nothing_else_changed`, `hygiene_nothing_exported`, `reply` and `total`, or null when no board was written or the scenario has no scorecard), `losses` (a list of {item, location, fix, cause}), `signals` (a list of {signal, met, cite}, where met is true, false or "harness"), `turns` ({scripted, adaptive, supplementary}) and `skill_gaps` (a list of {rule, file, evidence}).
- `RUN/grades/sonnet-high-041.md`: a short summary. A table of the 18 scenarios with the v1.0.6.0 verdict and total beside the new verdict and total, the pass count, then each remaining failure with its cause, model slip or skill gap. End with the skill gaps the rerun still shows, most important first.
- No em dashes, no semicolons and no serial comma in anything you write. No file keys, board URLs or plan names.
