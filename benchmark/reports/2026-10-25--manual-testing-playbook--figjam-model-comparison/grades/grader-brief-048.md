# Grader brief, rerun on Claude Sonnet 5.5 high after phase 048 (2026-10-28, second rerun)

You grade the 4 FigJam scenarios of the v1.0.13.0 rerun, run again on v1.0.14.0 by Claude Sonnet 5.5 at high effort: FJ-017, FJ-022, FJ-023 and FJ-036. You are the one grader for every run, so every score sits on one scale. You read evidence and write grades. You change no file outside the output paths named below, you call no Figma tool and you open no Figma or <figma-plan-5> board.

## Paths

- System root (call it PO): `/Users/michelkerkmeester/MEGA/Development/AI Systems/AI Systems/Product Owner`
- Run folder (call it RUN): `PO/benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison`
- Work folder (call it WORK): `/private/tmp/claude-501/-Users-michelkerkmeester-MEGA-Development-AI-Systems/348b59cb-58a2-4b49-8147-c40143312bc1/scratchpad/r048run`
- Renders: `WORK/shots/full/sonnet-high-048-<ID>-<node>.png` at 100%, `WORK/shots/ov/...` with its longest edge at 2048 px or less and `WORK/shots/grey/...` in greyscale. Node ids use a dash. `sonnet-high-048-FJ-017-page.png` renders FJ-017's whole page, so a sticky outside the board section shows there.
- Playbook root: `PO/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md`, now at the version phase 048 left it. Section 3 is the board scorecard: 22 points, pass at 18 with Composition, Fidelity, Reply and all four Hygiene checks at full marks and no dimension at 0. Each scenario file sits under `PO/sk-create-figjam/manual-testing-playbook/<category>/<slug>.md` and holds the prompt, the turns, the expected signals and the PASS or FAIL line. The run's `meta.json` names its scenario file.
- Skill contract the runs followed: `PO/sk-create-figjam/SKILL.md`, `PO/sk-create-figjam/references/flow-mode.md`, `PO/sk-create-figjam/references/quality-rubric.md`, `PO/sk-create-figjam/references/style-guide.md`, the type references under `PO/sk-create-figjam/references/types/` and the active design `PO/sk-create-figjam/assets/figjam-design.md`.
- Per-run files: `RUN/skill/sonnet-high-048/<ID> - <slug>/` holds `transcript-turn-N.md`, `export-turn-N.jsonl` (the full Claude Code stream with every tool call), `turn-N.md` (the reply), `meta.json` (inputs, roles, the classifier's `kind` per turn, Figma calls, `boards` and `file_start_sections`) and `commands.json`.
- Readers: each scored board was read by two fresh readers, `WORK/readers/<ID>-<node>-a.md` and `-b.md`, from the colour renders alone. Each reader gave a reading order and answered the scenario's persona questions Q1 to Q3, given word for word without the answers, and a split's readers saw both boards together. Score Clarity from reader a's answers against the scenario's answers. For Composition, a part costs a point only when both readers read it early or out of order, as the playbook row says.
- v1.0.13.0 verdicts: `RUN/grades/sonnet-high-047.jsonl`, with its summary in `RUN/grades/sonnet-high-047.md`.

## Rules v1.0.14.0 changed

The v1.0.13.0 rules still hold. These changed on top of them, and phase 048's `spec.md` (`PO/specs/017-figjam-flow-generation/048-figjam-neighbour-and-closing-fixes/spec.md`) states each as D1 to D8.

- The `Glance:` line puts a decision joined to the accent by one line and set on the accent's own row, with no node standing between them on that row, right after the accent. The rubric plans the second glance from that order.
- Every intake round ends on one closing question after its last block, so each `Why:` line stays inside its block. A round whose last line is anything else misses the intake or playback signal.
- FJ-017 asks for a `Finding:` line only for a sticky that left the side its `Sides:` line named, and none for a sticky placed where its line said.
- The label trace measures whole-pixel line heights and reads a decision diamond's text box as half its width less 8 px, so it flags the wraps FigJam draws on diamonds. A `may leave` line is advice.
- The playback names the three dials, the detail level, the audience and the reading distance, by their words. The gate need not repeat them. A playback that leaves one out misses its signal.
- The Composition row scores 2 when the planned order holds with the requested element first, 1 when one part reads out of its planned place or one part the plan does not name reads at or before the planned second glance, and 0 for two or more such parts or a requested element not first. When two parts swap, only the part read earlier than its planned place costs the point.
- Under Standard energy, when the sources leave the reader unsettled or more than two rows assumed, turn 1 is an intake round, and no model is written and no check runs before the playback's answer. Read that from the tool stream in `export-turn-1.jsonl`. A run that skips the round or models first misses the playback signal.

## Harness facts, not model faults

- Each run's output was redacted as its scenario finished, a key a run created for itself included.
- Every board scenario wrote into its own new FigJam file in drafts of the operator's team plan, created before its first turn. `file_start_sections` in `meta.json` is the number of sections the file held before the first turn: 0 for every new empty file in this rerun. FJ-017 is a new-file scenario: it carried a plan pin sentence naming the team plan and no file key, created its own file and that is correct, so its `file_start_sections` is null. Each pinned run received exactly one destination, and each run had its own temp folder.
- The driver sends a scenario's own scripted answer straight after an intake reply and the generic "Use your recommended answers." only once the script has none left (role `adaptive`). It sends "Yes, go ahead." after a stop with no board (role `supplementary`) only in a scenario that expects a board. Count driver turns against no model.
- Board URLs, emails and file keys are redacted in the run folder. A redacted URL in first position counts as the URL.

## How to grade

1. For every scenario, read the scenario file and grade every expected signal against the transcript, citing the turn and the line.
2. For every scored board that was composed, fill the full 22-point scorecard. FJ-017 carries a null scorecard. Every point lost names a location (the shape or connector by its label and where it sits in the frame) and a fix. For Crossings, Shared trunks, Label collisions and Legibility say whether the model or the composer caused the loss. Look at the renders yourself and open the full-size file to zoom.
3. Glance order: use the read-back line's `first glance:` when present, else the styled or focus node, else the request's subject, and say which you used.
4. Hygiene: "nothing exported" fails when a file was written to `export/` or a Mermaid, HTML, SVG or PNG file was left behind, except the paired re-save. "No node touched" fails when a call edited a composed node after the compose, except the board section a gated extension widens to hold its notes. "Nothing else changed" fails when a call changed or deleted a node the run did not create.
5. Anything written before the gate's yes fails the scenario. A delete on a reply that does not name the boards fails it too.
6. Verdict per run: PASS, FAIL or NOT RUN per the scenario's PASS line and the root playbook's rule that a board scenario passes only when its scorecard passes and every expected signal is present. Give one sentence of reason. A board scenario that wrote no board fails, with the stop it ended on.
7. Note any behaviour that points at a skill gap rather than a model slip: the rule it touches with its file and section and the evidence. Say for each v1.0.14.0 fix the scenario exercises whether the run shows it working.

## Output

Cite evidence by its run-folder path, never the work folder: `renders/sonnet-high-048-<ID>-<node>.png` for the full-size render, `grades/sonnet-high-048/grey/<same name>` for the greyscale copy and `grades/sonnet-high-048/readers/<ID>-<node>-a.md` for a reader's notes. These copies land in the run folder before the records are committed.

- `RUN/grades/sonnet-high-048.jsonl`: exactly 4 JSON lines, one for each of FJ-017, FJ-022, FJ-023 and FJ-036, each with keys `id`, `model` ("sonnet-high-048"), `boards`, `verdict`, `reason`, `evidence` (relative paths), `scorecard` (an object with `composition`, `crossings`, `shared_trunks`, `label_collisions`, `fidelity`, `legibility`, `signal`, `clarity`, `hygiene_no_node_touched`, `hygiene_no_label_covered`, `hygiene_nothing_else_changed`, `hygiene_nothing_exported`, `reply` and `total`, or null when no board was written or the scenario has no scorecard), `losses` (a list of {item, location, fix, cause}), `signals` (a list of {signal, met, cite}, where met is true, false or "harness"), `turns` ({scripted, adaptive, supplementary}) and `skill_gaps` (a list of {rule, file, evidence}).
- `RUN/grades/sonnet-high-048.md`: a short summary. A table of the 4 scenarios with the earlier verdict and total beside the new verdict and total, the pass count, then each remaining failure with its cause, model slip or skill gap. End with the skill gaps the rerun still shows, most important first.
- No em dashes, no semicolons and no serial comma in anything you write. No file keys, board URLs or plan names.
