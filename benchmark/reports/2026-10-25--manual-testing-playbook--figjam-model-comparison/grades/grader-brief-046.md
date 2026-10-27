# Grader brief, rerun on Claude Sonnet 5.5 high after phase 046 (2026-10-27)

You grade 4 FigJam scenarios run on `sk-create-figjam` v1.0.12.0 by Claude Sonnet 5.5 at high effort: FJ-017 and FJ-036, which failed on v1.0.11.0, and FJ-022 and FJ-023, whose gallery boards accented the goal before this release. You are the one grader for every run, so every score sits on one scale. You read evidence and write grades. You change no file outside the output paths named below, you call no Figma tool and you open no Figma or <figma-plan-5> board.

## Paths

- System root (call it PO): `/Users/michelkerkmeester/MEGA/Development/AI Systems/AI Systems/Product Owner`
- Run folder (call it RUN): `PO/benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison`
- Work folder (call it WORK): `/private/tmp/claude-501/-Users-michelkerkmeester-MEGA-Development-AI-Systems/348b59cb-58a2-4b49-8147-c40143312bc1/scratchpad/r046run`
- Renders: `WORK/shots/full/sonnet-high-046-<ID>-<node>.png` at 100%, `WORK/shots/ov/...` with its longest edge at 2048 px or less and `WORK/shots/grey/...` in greyscale. Node ids use a dash. When FJ-017 wrote no sticky, a `sonnet-high-046-FJ-017-page.png` render shows its whole page.
- Playbook root: `PO/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md`, now at the version phase 046 left it. Section 3 is the board scorecard: 22 points, pass at 18 with Composition, Fidelity, Reply and all four Hygiene checks at full marks and no dimension at 0. Each scenario file sits under `PO/sk-create-figjam/manual-testing-playbook/<category>/<slug>.md` and holds the prompt, the turns, the expected signals and the PASS or FAIL line. The run's `meta.json` names its scenario file.
- Skill contract the runs followed: `PO/sk-create-figjam/SKILL.md`, `PO/sk-create-figjam/references/flow-mode.md`, `PO/sk-create-figjam/references/quality-rubric.md`, `PO/sk-create-figjam/references/style-guide.md`, the type references under `PO/sk-create-figjam/references/types/` and the active design `PO/sk-create-figjam/assets/figjam-design.md`.
- Per-run files: `RUN/skill/sonnet-high-046/<ID> - <slug>/` holds `transcript-turn-N.md`, `export-turn-N.jsonl` (the full Claude Code stream with every tool call), `turn-N.md` (the reply), `meta.json` (inputs, roles, the classifier's `kind` per turn, Figma calls, `boards` and `file_start_sections`) and `commands.json`.
- Readers: each scored board was read by two fresh readers, `WORK/readers/<ID>-<node>-a.md` and `-b.md`, from the colour renders alone. Each reader gave a reading order and answered the scenario's persona questions Q1 to Q3, given word for word without the answers, and a split's readers saw both boards together. Score Clarity from reader a's answers against the scenario's answers. For Composition, a part costs a point only when both readers read it early or out of order, as the playbook row says.
- Earlier Claude Sonnet 5.5 high verdicts: FJ-017 and FJ-036 on v1.0.11.0 in `RUN/grades/sonnet-high-045.jsonl`, FJ-022 in `RUN/grades/sonnet-high-gallery.jsonl` and FJ-023 in `RUN/grades/sonnet-high-042.jsonl`.

## Rules v1.0.12.0 changed

The v1.0.11.0 rules still hold. These changed on top of them, and phase 046's `spec.md` (`PO/specs/017-figjam-flow-generation/046-figjam-gate-and-accent-fixes/spec.md`) states each as D1 to D7.

- Notes sides at the gate: a model whose board carries single stickies names their nodes on a `%% notes: <id>, <id>` line, which moves the key down by one sticky and its gap. `flow_check.py <model> --notes <id>,<id>` prints one `Sides:` line per noted node, naming the side its sticky takes or saying the node is boxed in, with the sides chosen for all noted nodes together. The gate names each side, or offers pins with a legend or a model change for a boxed-in node, and the notes call places each sticky on the side its line named. On the layout of the shipped state example NoShow is genuinely boxed in, so a gate that offers pins there is following the rule. FJ-017's scenario file states the signals.
- The goal never takes the accent on a user flow or a process. A `%% goal: <id>` line names the goal, and the one `style` accent goes to a decision, a failure end or the one step in focus. FJ-022 expects the confirmation named on a goal line and the accent on the 30-day decision.
- A stop ends on its question: an intake round, the playback and the gate carry no `HVR self-scan:` line or any other text after their question. The playbook's Section 5 acceptance rules make a turn that does not end on its stop's question miss that stop's signal.
- The gate always shows the sketch, the checked model with the check's result, and answers the four critique questions `flow-mode.md` step 7 names (where the eye goes first, what it reads second, what a reader could miss and which node the remove test would cut next), unless the user already settled them. A gate without them misses its signal under the same Section 5 rule.
- A group the request names as one, such as the end states, reads as a set whose member order is not scored.
- The label trace reads at the normal and the narrow character measure. Say for each run which `Label:` line it printed.

## Harness facts, not model faults

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
7. Note any behaviour that points at a skill gap rather than a model slip: the rule it touches with its file and section and the evidence. Say for each v1.0.12.0 fix the scenario exercises whether the run shows it working.

## Output

- `RUN/grades/sonnet-high-046.jsonl`: exactly 4 JSON lines, one for each of FJ-017, FJ-022, FJ-023 and FJ-036, each with keys `id`, `model` ("sonnet-high-046"), `boards`, `verdict`, `reason`, `evidence` (relative paths), `scorecard` (an object with `composition`, `crossings`, `shared_trunks`, `label_collisions`, `fidelity`, `legibility`, `signal`, `clarity`, `hygiene_no_node_touched`, `hygiene_no_label_covered`, `hygiene_nothing_else_changed`, `hygiene_nothing_exported`, `reply` and `total`, or null when no board was written or the scenario has no scorecard), `losses` (a list of {item, location, fix, cause}), `signals` (a list of {signal, met, cite}, where met is true, false or "harness"), `turns` ({scripted, adaptive, supplementary}) and `skill_gaps` (a list of {rule, file, evidence}).
- `RUN/grades/sonnet-high-046.md`: a short summary. A table of the 4 scenarios with the earlier verdict and total beside the new verdict and total, the pass count, then each remaining failure with its cause, model slip or skill gap. End with the skill gaps the rerun still shows, most important first.
- No em dashes, no semicolons and no serial comma in anything you write. No file keys, board URLs or plan names.
