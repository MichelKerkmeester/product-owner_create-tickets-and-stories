# Grader brief, rerun on Claude Sonnet 5.5 high after phase 044 (2026-10-27)

You grade the 6 FigJam scenarios that failed on `sk-create-figjam` v1.0.9.0, run again on v1.0.10.0 by Claude Sonnet 5.5 at high effort: FJ-017, FJ-026, FJ-029, FJ-031, FJ-032 and FJ-036. You are the one grader for every run, so every score sits on one scale. You read evidence and write grades. You change no file outside the output paths named below, you call no Figma tool and you open no Figma or Barter board.

## Paths

- System root (call it PO): `/Users/michelkerkmeester/MEGA/Development/AI Systems/AI Systems/Product Owner`
- Run folder (call it RUN): `PO/benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison`
- Work folder (call it WORK): `/private/tmp/claude-501/-Users-michelkerkmeester-MEGA-Development-AI-Systems/348b59cb-58a2-4b49-8147-c40143312bc1/scratchpad/r044`
- Renders: `WORK/shots/full/sonnet-high-044-<ID>-<node>.png` at 100%, `WORK/shots/ov/...` with its longest edge at 2048 px or less and `WORK/shots/grey/...` in greyscale. Node ids use a dash. The same full-size files are in `RUN/renders/`. `sonnet-high-044-FJ-032-page.png` joins FJ-032's prepared retro section and its new board at their page positions.
- Playbook root: `PO/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md`, now v1.0.9.0. Section 3 is the board scorecard: 22 points, pass at 18 with Composition, Fidelity, Reply and all four Hygiene checks at full marks and no dimension at 0. Each scenario file sits under `PO/sk-create-figjam/manual-testing-playbook/<category>/<slug>.md` and holds the prompt, the turns, the expected signals and the PASS or FAIL line. The run's `meta.json` names its scenario file.
- Skill contract the runs followed: `PO/sk-create-figjam/SKILL.md`, `PO/sk-create-figjam/references/flow-mode.md`, `PO/sk-create-figjam/references/quality-rubric.md`, `PO/sk-create-figjam/references/style-guide.md`, the type references under `PO/sk-create-figjam/references/types/` and the active design `PO/sk-create-figjam/assets/figjam-design.md`.
- Per-run files: `RUN/skill/sonnet-high-044/<ID> - <slug>/` holds `transcript-turn-N.md`, `export-turn-N.jsonl` (the full Claude Code stream with every tool call), `turn-N.md` (the reply), `meta.json` (inputs, roles, the classifier's `kind` per turn, Figma calls, `boards` and `file_start_sections`) and `commands.json`.
- Readers: each scored board was read by two fresh readers, `WORK/readers/<ID>-<node>-a.md` and `-b.md`, from the colour renders alone. Each reader gave a reading order and answered the scenario's persona questions Q1 to Q3, given word for word without the answers, and a split's readers saw both boards together. Score Clarity from reader a's answers against the scenario's answers. For Composition, a part costs a point only when both readers read it early or out of order, as the playbook row says.
- v1.0.9.0 verdicts: `RUN/grades/sonnet-high-043.jsonl`.

## Rules v1.0.10.0 changed

The v1.0.9.0 rules still hold. These changed on top of them.

- The composer lays out an edge to or from a composite state against the composite's inner start, so the composite is drawn after the state that enters it whatever order the model declares its lines in. `scripts/flow_check.py` fails a composite with no inner `[*]` before the write.
- `references/quality-rubric.md`: on a user flow or a process a reader takes the rest of the main row, the path from the entry to the goal, in path order whatever its fills. So every node the board draws sits in one of the three glance lines, the main-row nodes the outlined kinds and the entry leave are named in path order with those nearest the entry in the earlier line and two decisions share a line. A revision plans the entry, the decisions and the rest of the main row in the last glance line.
- Playbook Composition row: on a revision the entry, the decisions and every other main-row node the rubric plans last cost no point when they read before the changed end. On a user flow or a process the planned order inside a glance line is path order.
- FJ-017: when the two noted nodes sit on adjacent rows, the second sticky sits below or to the left of its node, and the reply may name it on a `Finding:` line. This is the reading the operator applied on 2026-10-27: a second sticky on an adjacent row that sits right of its node, or off its node's level, is not beside it and the signal is unmet. Grade FJ-017 on that reading.
- The run launcher pinned a node that loads, but the Bash tool inside each run rebuilds PATH from the shell profile, so a run may still print `Label: skipped` with a library load error. That is a harness fact, not a model fault. Say for each run which line it printed.
- The user flow and process examples plan their glances in path order.

## Harness facts, not model faults

- Every board scenario wrote into its own new FigJam file in drafts of the operator's team plan, created before its first turn. `file_start_sections` in `meta.json` is the number of sections the file held before the first turn: 0 for a new empty file, 1 for FJ-032, whose file held one prepared retro section. FJ-017 is a new-file scenario: it ran with no file pin, created its own file and that is correct. Each pinned run received exactly one destination, and each run had its own temp folder.
- The driver sends a scenario's own scripted answer straight after an intake reply and the generic "Use your recommended answers." only once the script has none left (role `adaptive`). It sends "Yes, go ahead." after a stop with no board (role `supplementary`) only in a scenario that expects a board. Count driver turns against no model.
- FJ-031 paused before its third turn. The operator added one sticky, `Operator note: check return window wording with support`, to the right of the first board, then the run resumed (`operator_paused` true in `meta.json`). That sticky is the operator's node, so any change to it counts against "nothing else changed".
- FJ-032's prompt placeholder for the prepared board's file was filled with that file, so the run had one destination.
- Board URLs, emails and file keys are redacted in the run folder. A redacted URL in first position counts as the URL.

## How to grade

1. For every scenario, read the scenario file and grade every expected signal against the transcript, citing the turn and the line.
2. For every scored board that was composed, fill the full 22-point scorecard. FJ-017 and the other board-write scenarios carry a null scorecard. Every point lost names a location (the shape or connector by its label and where it sits in the frame) and a fix. For Crossings, Shared trunks, Label collisions and Legibility say whether the model or the composer caused the loss. Look at the renders yourself and open the full-size file to zoom.
3. Glance order: use the read-back line's `first glance:` when present, else the styled or focus node, else the request's subject, and say which you used.
4. Hygiene: "nothing exported" fails when a file was written to `export/` or a Mermaid, HTML, SVG or PNG file was left behind, except the paired re-save. "No node touched" fails when a call edited a composed node after the compose, except the board section a gated extension widens to hold its notes. "Nothing else changed" fails when a call changed or deleted a node the run did not create.
5. Anything written before the gate's yes fails the scenario. A delete on a reply that does not name the boards fails it too.
6. Verdict per run: PASS, FAIL or NOT RUN per the scenario's PASS line and the root playbook's rule that a board scenario passes only when its scorecard passes and every expected signal is present. Give one sentence of reason. A board scenario that wrote no board fails, with the stop it ended on.
7. Note any behaviour that points at a skill gap rather than a model slip: the rule it touches with its file and section and the evidence. Say for each v1.0.10.0 fix the scenario exercises whether the run shows it working.

## Output

- `RUN/grades/sonnet-high-044.jsonl`: exactly 6 JSON lines, one for each of FJ-017, FJ-026, FJ-029, FJ-031, FJ-032 and FJ-036, each with keys `id`, `model` ("sonnet-high-044"), `boards`, `verdict`, `reason`, `evidence` (relative paths), `scorecard` (an object with `composition`, `crossings`, `shared_trunks`, `label_collisions`, `fidelity`, `legibility`, `signal`, `clarity`, `hygiene_no_node_touched`, `hygiene_no_label_covered`, `hygiene_nothing_else_changed`, `hygiene_nothing_exported`, `reply` and `total`, or null when no board was written or the scenario has no scorecard), `losses` (a list of {item, location, fix, cause}), `signals` (a list of {signal, met, cite}, where met is true, false or "harness"), `turns` ({scripted, adaptive, supplementary}) and `skill_gaps` (a list of {rule, file, evidence}).
- `RUN/grades/sonnet-high-044.md`: a short summary. A table of the 6 scenarios with the v1.0.9.0 verdict and total beside the new verdict and total, the pass count, then each remaining failure with its cause, model slip or skill gap. End with the skill gaps the rerun still shows, most important first.
- No em dashes, no semicolons and no serial comma in anything you write. No file keys, board URLs or plan names.
