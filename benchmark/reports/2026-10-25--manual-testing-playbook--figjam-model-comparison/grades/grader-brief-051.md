# Grader brief, gallery rerun on Claude Sonnet 5.5 medium after phase 050 (2026-10-29)

You grade the 10 FigJam gallery scenarios run on v1.0.16.0 by Claude Sonnet 5.5 at medium effort, one after the other: FJ-022, FJ-023, FJ-024, FJ-025, FJ-026, FJ-027, FJ-028, FJ-032, FJ-036 and the new FJ-049. You are the one grader for every run, so every score sits on one scale. You read evidence and write grades. You change no file outside the output paths named below, you call no Figma tool and you open no Figma or <figma-plan-5> board.

## Paths

- System root (call it PO): `/Users/michelkerkmeester/MEGA/Development/AI Systems/AI Systems/Product Owner`
- Run folder (call it RUN): `PO/benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison`
- Work folder (call it WORK): `/private/tmp/claude-501/-Users-michelkerkmeester-MEGA-Development-AI-Systems/cb7f5c8f-ad61-46e0-8985-4b3286150879/scratchpad/r051run`
- Renders: `WORK/shots/full/sonnet-medium-051-<ID>-<node>.png` at 100%, `WORK/shots/ov/...` with its longest edge at 2048 px or less and `WORK/shots/grey/...` in greyscale. Node ids use a dash.
- Playbook root: `PO/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md`, now at the version phase 051 left it. Section 3 is the board scorecard: 22 points, pass at 18 with Composition, Fidelity, Reply and all four Hygiene checks at full marks and no dimension at 0. Each scenario file sits under `PO/sk-create-figjam/manual-testing-playbook/<category>/<slug>.md` and holds the prompt, the turns, the expected signals and the PASS or FAIL line. The run's `meta.json` names its scenario file.
- Skill contract the runs followed: `PO/sk-create-figjam/SKILL.md`, `PO/sk-create-figjam/references/flow-mode.md`, `PO/sk-create-figjam/references/quality-rubric.md`, `PO/sk-create-figjam/references/style-guide.md`, the type references under `PO/sk-create-figjam/references/types/` and the active design `PO/sk-create-figjam/assets/figjam-design.md`.
- Per-run files: `RUN/skill/sonnet-medium-051/<ID> - <slug>/` holds `transcript-turn-N.md`, `export-turn-N.jsonl` (the full Claude Code stream with every tool call), `turn-N.md` (the reply), `meta.json` (inputs, roles, the classifier's `kind` per turn, Figma calls, `boards` and `file_start_sections`) and `commands.json`.
- Readers: each scored board was read by two fresh readers, `WORK/readers/<ID>-<node>-a.md` and `-b.md`, from the colour renders alone. Each reader gave a reading order and answered the scenario's persona questions Q1 to Q3, given word for word without the answers, and a split's readers saw both boards together. Each note ends on one `Order:` line. Score Clarity from reader a's answers against the scenario's answers. Composition is the output of `RUN/run/composition_check.py --plan "<Glance line>" <reader a note> <reader b note>`, where the plan is the last `Glance:` line the run's check printed before the write, read from `export-turn-N.jsonl`. Paste the script's lines into the record's reason, and never read the order by eye. Reader notes and the reader prompt follow `RUN/grades/reader-brief.md`.
- Earlier gallery boards and their scores: `PO/sk-create-figjam/assets/screenshots/README.md` Section 2. The last verdicts: `RUN/grades/sonnet-high-049.jsonl`.

## Rules v1.0.16.0 added

The v1.0.15.0 rules still hold. Phase 050's `spec.md` (`PO/specs/017-figjam-flow-generation/050-figjam-spec-board-learnings/spec.md`) states these as D1 to D6.

- A read-back after any write but the composing call judges a view rendered after that write, taken with `node.screenshot()` inside `use_figma`, and names a stale view.
- Every subtitle names where the flow starts and where it ends.
- A laned process may name one status lane with `%% status:`, declared first, holding two or more statuses in one `-->` chain, each status after the first reached by a dotted `-.->` move from a step, and no status takes the accent. The board draws statuses as white chevrons and the key names `Moves the status`.
- At `%% level: faithful` a step may carry a body from a `%% detail:` line, at most 10 lines of 44 characters, under a one-line Bold label. A laned process with detail cards reads at 18 nodes and 24 connectors.

## Harness facts, not model faults

- Each run's output was redacted as its scenario finished, a key a run created for itself included.
- Every board scenario wrote into its own new FigJam file in drafts of the operator's team plan, created before its first turn. `file_start_sections` in `meta.json` is the number of sections the file held before the first turn: 0 for every new empty file in this rerun and 1 for FJ-032, whose file held a prepared Sprint retro section with six stickies before turn 1, set up by the operator. Each pinned run received exactly one destination, and each run had its own temp folder.
- The driver sends a scenario's own scripted answer straight after an intake reply and the generic "Use your recommended answers." only once the script has none left (role `adaptive`). It sends "Yes, go ahead." after a stop with no board (role `supplementary`) only in a scenario that expects a board. Count driver turns against no model.
- Board URLs, emails and file keys are redacted in the run folder. A redacted URL in first position counts as the URL.

## How to grade

1. For every scenario, read the scenario file and grade every expected signal against the transcript, citing the turn and the line.
2. For every scored board that was composed, fill the full 22-point scorecard. Every point lost names a location (the shape or connector by its label and where it sits in the frame) and a fix. For Crossings, Shared trunks, Label collisions and Legibility say whether the model or the composer caused the loss. Look at the renders yourself and open the full-size file to zoom.
3. Glance order: use the read-back line's `first glance:` when present, else the styled or focus node, else the request's subject, and say which you used.
4. Hygiene: "nothing exported" fails when a file was written to `export/` or a Mermaid, HTML, SVG or PNG file was left behind, except the paired re-save. "No node touched" fails when a call edited a composed node after the compose, except the board section a gated extension widens to hold its notes. "Nothing else changed" fails when a call changed or deleted a node the run did not create.
5. Anything written before the gate's yes fails the scenario. A delete on a reply that does not name the boards fails it too.
6. Verdict per run: PASS, FAIL or NOT RUN per the scenario's PASS line and the root playbook's rule that a board scenario passes only when its scorecard passes and every expected signal is present. Give one sentence of reason. A board scenario that wrote no board fails, with the stop it ended on.
7. Note any behaviour that points at a skill gap rather than a model slip: the rule it touches with its file and section and the evidence. Say for each v1.0.16.0 rule the scenario exercises whether the run shows it working.

## Output

Cite evidence by its run-folder path, never the work folder: `renders/sonnet-medium-051-<ID>-<node>.png` for the full-size render, `grades/sonnet-medium-051/grey/<same name>` for the greyscale copy and `grades/sonnet-medium-051/readers/<ID>-<node>-a.md` for a reader's notes. These copies land in the run folder before the records are committed.

- `RUN/grades/sonnet-medium-051.jsonl`: exactly 10 JSON lines, one per scenario, each with keys `id`, `model` ("sonnet-medium-051"), `boards`, `verdict`, `reason`, `evidence` (relative paths), `scorecard` (an object with `composition`, `crossings`, `shared_trunks`, `label_collisions`, `fidelity`, `legibility`, `signal`, `clarity`, `hygiene_no_node_touched`, `hygiene_no_label_covered`, `hygiene_nothing_else_changed`, `hygiene_nothing_exported`, `reply` and `total`, or null when no board was written or the scenario has no scorecard), `losses` (a list of {item, location, fix, cause}), `signals` (a list of {signal, met, cite}, where met is true, false or "harness"), `turns` ({scripted, adaptive, supplementary}) and `skill_gaps` (a list of {rule, file, evidence}).
- `RUN/grades/sonnet-medium-051.md`: a short summary. A table of the 10 scenarios with the score of the gallery board of the same type beside the new verdict and total, the pass count, then each failure with its cause, model slip or skill gap. End with the skill gaps the rerun shows, most important first.
- No em dashes, no semicolons and no serial comma in anything you write. No file keys, board URLs or plan names.
