# Iteration 1: Packet baseline — what sk-create-figjam already enforces

## Focus

Fix the baseline the corpus will be judged against. Read the packet's contract surface: `SKILL.md`, `references/flow-mode.md`, `references/quality-rubric.md`, `references/style-guide.md`, `scripts/flow_check.py`, and the board scorecard in `manual-testing-playbook/manual-testing-playbook.md` Section 3. No corpus repo is opened this iteration; later iterations build on this baseline by name.

## Actions Taken

1. Read `sk-create-figjam/SKILL.md` (routing, resource levels, ALWAYS/NEVER rules, success criteria).
2. Read `references/flow-mode.md` (workflow, type choice, intake, shared rules, write routes, read-back, delivery, recovery).
3. Read `references/quality-rubric.md` and `references/style-guide.md`.
4. Read `scripts/flow_check.py` (check contract, unsupported kinds, self-test, palette re-measurement).
5. Read the board quality scorecard in `manual-testing-playbook/manual-testing-playbook.md` Section 3.

## Findings

1. The packet's strongest asset is a fail-closed pre-write check rather than post-hoc review: `flow_check.py` refuses a Mermaid kind the board generator cannot draw and enforces the shared model rules before any board exists, and its own docstring states why — the generator silently drops much of what Mermaid can say, so a model can promise a reader something the board never shows [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:6], [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:64].
2. The seven types are paired with an explicit nearest-drawable mapping, and the generator's unsupported-kind list is duplicated in prose and in code, so a pie, mindmap, Venn, C4, git graph or requirement request is answered with the nearest type or a plain no instead of a failed tool call [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:93], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:95], [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:63].
3. The shared model rule set is unusually complete for a board generator: no emoji, markup or literal `\n`, labels of at most 40 characters on one line, camelCase ids with a keyword ban, a per-type budget defaulting to 9 nodes and 12 connectors, colour only from the style guide, and a hard prohibition on moving generated nodes [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:159], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:162], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:164].
4. The rubric adds a delete-first judgment pass the script cannot make — the remove test ("a diagram is done when nothing can be removed") plus signal, provenance and reply checks — but it is prose with checkbox state, not a machine-readable record; the only scored artifact is the manual playbook's seven-dimension scorecard with a 12-of-14 pass line [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:33], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:35], [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md:75], [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md:87].
5. Colour handling is grounded in measured contrast and records its own departures: the palette block is the single accepted pair list, two ratio columns are measured against a 4.5:1 text gate and a 3.0:1 mark gate, and seven strokes are explicitly recorded as below the mark gate with the reason they are kept [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:58], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:105], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/style-guide.md:115].
6. `flow_check.py --self-test` re-measures every palette row, proves each rule fails on a planted model, and runs the shipped templates, worked examples and the `claude project/knowledge/` mirrors through the same check, skipping mirrors that are absent in a plugin install rather than counting them as passes [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:181], [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:221], [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:230].
7. The write route is more careful than a one-shot generation: hosted-first, the first call creates a new file and every later diagram or revision passes that `fileKey`, a failed or timed-out call is explicitly not proof that nothing landed, a retry happens only after reading the target, and rollback deletes only nodes this write created [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:183], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:184], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:187].
8. Read-back is honest about its own limits: per-type counts compared with the model, a node-by-node `get_figjam` read on the hosted route and `fj nodes -l` on the desktop route, an explicit `Read-back: not possible` line when the connector has no read tool, and a `, read visually` suffix when only a screenshot could be read [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:209], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:215], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:224].
9. Gap found: extension quality is gated by intent, not by a check. The gate must name any planned extension, but `flow_check.py` reads only Mermaid, so pins, stickies, tints, legend placement and overlap are verified only by the human scorecard's Hygiene and Legibility dimensions on a screenshot [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:67], [SOURCE: AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py:6], [SOURCE: AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md:84].
10. Delivery forbids a file-shaped substitute: when neither route is reachable the packet offers the checked model in the reply and never renders a Mermaid, HTML, SVG or PNG stand-in, and no file may be left in `export/` [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:203], [SOURCE: AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md:230], [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:177].

## Ruled Out

- Judging board visual quality from screenshots or board URLs: the run's constraints forbid opening screenshots or board URLs, so every layout claim must come from documentation, code or the scorecard's written thresholds. Visual scoring is treated as an operator step the packet already defines.
- Treating the packet's seven types as the corpus comparison unit alone: type names differ across projects (flowchart/workflow/architecture/state), so later iterations compare by capability and rule, not by label.

## Dead Ends

- No dead end yet; iteration 1 establishes the baseline. The `manual-testing-playbook` scenario files are numerous and were not needed for the baseline beyond Section 3.

## Edge Cases

- Ambiguous input: none. The packet names its own contract surface and the task names the same files.
- Contradictory evidence: none in this iteration.
- Missing dependencies: none; all packet files were present.
- Partial success: none.

## Sources Consulted

- AI Systems/Product Owner/sk-create-figjam/SKILL.md
- AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md
- AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md
- AI Systems/Product Owner/sk-create-figjam/references/style-guide.md
- AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py
- AI Systems/Product Owner/sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md

## Assessment

- New information ratio: 1.0
- Questions addressed: Q1, Q2, Q3 (baseline evidence only)
- Questions answered: none fully; the baseline is the measuring stick, not the answer.

## Reflection

- What worked and why: reading the check script alongside the prose contract exposed the real gate boundaries — the script owns drawability, labels, ids, budget and palette, while the rubric owns taste and the playbook owns board scoring. Reading all three separately would have blurred that split.
- What did not work and why: nothing failed. The scorecard's line numbers were not in the first `flow-mode` read and needed a targeted grep, which is cheaper than rereading the playbook.
- What I would do differently: fetch the exact scorecard lines before writing the baseline so the assessment can cite the dimension rows directly, as done here.

## Recommended Next Focus

Iteration 2: open the newer `figma__mcp-server-guide` commit and read what changed — the `skills-figquery` folder, `workflow-skills/generate-project-plan` and `figma-power` — then compare its diagram generation guidance and its workflow-skills packaging against this packet's seven types and write routes. Builds on iteration 1's baseline.
