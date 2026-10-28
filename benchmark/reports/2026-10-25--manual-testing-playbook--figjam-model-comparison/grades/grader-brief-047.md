# Grader brief, rerun on Claude Sonnet 5.5 high after phase 047 (2026-10-28)

You grade the 4 FigJam scenarios that failed on `sk-create-figjam` v1.0.12.0, run again on v1.0.13.0 by Claude Sonnet 5.5 at high effort: FJ-017, FJ-022, FJ-023 and FJ-036. You are the one grader for every run, so every score sits on one scale. You read evidence and write grades. You change no file outside the output paths named below, you call no Figma tool and you open no Figma or <figma-plan-5> board.

## Paths

- System root (call it PO): `/Users/michelkerkmeester/MEGA/Development/AI Systems/AI Systems/Product Owner`
- Run folder (call it RUN): `PO/benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison`
- Work folder (call it WORK): `/private/tmp/claude-501/-Users-michelkerkmeester-MEGA-Development-AI-Systems/348b59cb-58a2-4b49-8147-c40143312bc1/scratchpad/r047run`
- Renders: `WORK/shots/full/sonnet-high-047-<ID>-<node>.png` at 100%, `WORK/shots/ov/...` with its longest edge at 2048 px or less and `WORK/shots/grey/...` in greyscale. Node ids use a dash. `sonnet-high-047-FJ-017-page.png` renders FJ-017's whole page, so a sticky outside the board section shows there.
- Playbook root: `PO/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md`, now at the version phase 047 left it. Section 3 is the board scorecard: 22 points, pass at 18 with Composition, Fidelity, Reply and all four Hygiene checks at full marks and no dimension at 0. Each scenario file sits under `PO/sk-create-figjam/manual-testing-playbook/<category>/<slug>.md` and holds the prompt, the turns, the expected signals and the PASS or FAIL line. The run's `meta.json` names its scenario file.
- Skill contract the runs followed: `PO/sk-create-figjam/SKILL.md`, `PO/sk-create-figjam/references/flow-mode.md`, `PO/sk-create-figjam/references/quality-rubric.md`, `PO/sk-create-figjam/references/style-guide.md`, the type references under `PO/sk-create-figjam/references/types/` and the active design `PO/sk-create-figjam/assets/figjam-design.md`.
- Per-run files: `RUN/skill/sonnet-high-047/<ID> - <slug>/` holds `transcript-turn-N.md`, `export-turn-N.jsonl` (the full Claude Code stream with every tool call), `turn-N.md` (the reply), `meta.json` (inputs, roles, the classifier's `kind` per turn, Figma calls, `boards` and `file_start_sections`) and `commands.json`.
- Readers: each scored board was read by two fresh readers, `WORK/readers/<ID>-<node>-a.md` and `-b.md`, from the colour renders alone. Each reader gave a reading order and answered the scenario's persona questions Q1 to Q3, given word for word without the answers, and a split's readers saw both boards together. Score Clarity from reader a's answers against the scenario's answers. For Composition, a part costs a point only when both readers read it early or out of order, as the playbook row says.
- v1.0.12.0 verdicts: `RUN/grades/sonnet-high-046.jsonl`, with its summary in `RUN/grades/sonnet-high-046.md`.

## Rules v1.0.13.0 changed

The v1.0.12.0 rules still hold. These changed on top of them, and phase 047's `spec.md` (`PO/specs/017-figjam-flow-generation/047-figjam-glance-and-row-fixes/spec.md`) states each as D1 to D9.

- The glance plan follows the drawn board. On a user flow or a process `flow_check.py` prints a `Glance:` line, the order a reader meets the nodes: the accent first, then column by column along the flow and down each column, or row by row on a top-down flow, with the goal marked. The second glance names the nodes it prints up to and including the goal in that order, and the last glance names the rest, or the key and the source line when the goal comes last. The playbook Composition row scores against that planned order. Parts a reader names together in one step of their reading order read as a set.
- A `Row:` line, never a failure, names a line between two main-row steps that bends off the row and the node between them, with the move that straightens it on a zoned flow.
- `Sides:` lines name the side and the alignment of each single sticky (top aligned or centred beside the node, left aligned or centred below or above it), and no square further than one sticky width (240 px) from its node is offered. The notes call places each sticky on the side and in the alignment its line named. When that side is taken at the write, it takes the next side in the same order with the same clearance and reach and the reply names the change on a `Finding:` line.
- The gate sketch is the checked model exactly as the check read it, every `%%` and `style` line included, with the `PASSED` line as it printed. A sketch that drops a line misses the gate signal.
- A `Label:` line says `may leave` when only one of the two widths FigJam wraps at strands the word. A label may be reworded in the source's words even where it runs longer, and one no such wording clears is kept and named at the gate. The Legibility row scores 1 for one or more awkward wraps. Say for each run which `Label:` lines it printed.
- The three dials, the detail level, the audience and the reading distance, are asked in the first intake round.
- Text after the question of an intake round the scenario does not name misses the playback signal.

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
7. Note any behaviour that points at a skill gap rather than a model slip: the rule it touches with its file and section and the evidence. Say for each v1.0.13.0 fix the scenario exercises whether the run shows it working.

## Output

- `RUN/grades/sonnet-high-047.jsonl`: exactly 4 JSON lines, one for each of FJ-017, FJ-022, FJ-023 and FJ-036, each with keys `id`, `model` ("sonnet-high-047"), `boards`, `verdict`, `reason`, `evidence` (relative paths), `scorecard` (an object with `composition`, `crossings`, `shared_trunks`, `label_collisions`, `fidelity`, `legibility`, `signal`, `clarity`, `hygiene_no_node_touched`, `hygiene_no_label_covered`, `hygiene_nothing_else_changed`, `hygiene_nothing_exported`, `reply` and `total`, or null when no board was written or the scenario has no scorecard), `losses` (a list of {item, location, fix, cause}), `signals` (a list of {signal, met, cite}, where met is true, false or "harness"), `turns` ({scripted, adaptive, supplementary}) and `skill_gaps` (a list of {rule, file, evidence}).
- `RUN/grades/sonnet-high-047.md`: a short summary. A table of the 4 scenarios with the earlier verdict and total beside the new verdict and total, the pass count, then each remaining failure with its cause, model slip or skill gap. End with the skill gaps the rerun still shows, most important first.
- No em dashes, no semicolons and no serial comma in anything you write. No file keys, board URLs or plan names.
