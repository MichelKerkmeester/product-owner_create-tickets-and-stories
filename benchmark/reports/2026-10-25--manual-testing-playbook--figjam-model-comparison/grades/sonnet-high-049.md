# Rerun on v1.0.15.0, Claude Sonnet 5.5 high (sonnet-high-049)

One grader scored both runs on one scale from the transcripts, the tool streams, each render at 100% and in greyscale and two fresh readers per scored board. Both boards score 22 of 22 on the playbook scorecard. Both scenarios still fail, each on one expected signal the scorecard does not count.

| Scenario | v1.0.14.0 verdict | v1.0.14.0 total | v1.0.15.0 verdict | v1.0.15.0 total |
|---|---|---|---|---|
| FJ-022 User flow board quality | FAIL | 20 | FAIL | 22 |
| FJ-023 Process board quality | FAIL | 21 | FAIL | 22 |

**Pass count: 0 of 2. Fail count: 2. Not run: 0.**

Nothing was written before a gate's yes in either run. Every board reads back 8 of 8 nodes and 8 of 8 connectors, both replies open on the board URL with nothing before it and neither board loses a point to a crossing, a shared trunk, a label collision or a hygiene check. Composition is 2 on both, taken from `run/composition_check.py` on the last `Glance:` line each run printed before its write. Neither run printed a `Label:` line.

## Harness fact: the FJ-022 reader notes

The two FJ-022 readers first wrote their `Order:` line in flow order, which contradicted their own numbered reading order. Each reader was then asked to rewrite only that line to repeat its own reading-order list, as `grades/reader-brief.md` prescribes, and the reader brief's wording was tightened. This is a harness fact and no model fault. The FJ-023 readers got the tightened wording from the start. The scores here use the rewritten lines.

Evidence paths in `sonnet-high-049.jsonl` point into the run folder: `renders/sonnet-high-049-<ID>-1-3.png` for the full-size renders, `grades/sonnet-high-049/grey/` for the greyscale copies and `grades/sonnet-high-049/readers/` for the reader notes. FJ-022 ran one extra intake round, so its turns are the prompt, two intake answers (the second sent as role adaptive), the playback yes and the gate yes.

## Remaining failures

**FJ-022, one missing expected signal, a model choice and a playbook gap.** The scenario expects the board left to right in three zones. The model drew two, Check the order and Request the return, in the playback, at the gate and on the board. The skill makes zones a choice with no count (`references/flow-mode.md` Section 2 and `references/types/user-flow.md` Section 5) and the prompt names none, so the miss follows the model's choice against a scenario that fixes three. The board itself is clean: the 30-day decision carries the one accent, the goal is light green, Contact support is a light orange dashed exit and all three reader questions are answered correctly. Composition is 2 by the script. Both readers did read Contact support last where the plan puts it fifth, but reader b also read Confirmation with QR code early, so no part is out of place for both.

**FJ-023, one missing expected signal, a model slip.** Turn 1 is the scripted intake round and it opens correctly with nothing modelled or checked. It then adds a paragraph about the write target after the closing question. `references/flow-mode.md` Section 8 ends an intake round on the closing question and playbook Section 5 counts any text after it as a turn that did not end there. The fix is to hold the target statement for the gate. The pinned destination in the driver's message may have prompted the sentence, but the rule leaves no room for it.

## v1.0.15.0 fixes, as the rerun shows them

- **D1, the plain Glance order:** working on both. FJ-022's line reads the accent, then Order list, Order detail, Start a return, Contact support and the rest by column. FJ-023's reads the accent, then Damage reported and the decision, with no decision lifted beside the accent. Both readers of FJ-023 read the accent first.
- **D2, the reply opens on the URL:** working on both. Each delivery reply starts on the URL with no sentence before it, which clears the Reply loss that sat on FJ-022 in six earlier runs.
- **D3, FJ-023's intake round and the handoff queue as a connector label:** the queue works on FJ-023. The playback names it and the board draws Claim queued on the Approve the claim to Book a courier line, so the board holds 8 nodes and 8 connectors as the scenario counts.
- **D5, the glyph-width diamond label trace:** not exercised. Neither check printed a `Label:` line and every diamond label wraps evenly on the render.
- **D6, the dials are not assumed rows:** working. Both turn 1 rounds open on the reader, which no source names, and carry the dials as their own question.
- **D7, the reader Order line and the Composition script:** applied on both boards, level 2 each.
- **D3, the FJ-023 scripted intake round:** working in its shape. The round opens before any model or check and the playback waits for its own answer. Its one flaw is the trailing sentence above.
- **D4, the examples that model intake, and D8, the release:** not graded by this rerun.
- **The `Row:` line:** FJ-022's first check printed one and the model made the move it named and disclosed it at the gate under 'One change from the playback'.

## Skill gaps the rerun still shows, most important first

1. `sk-create-figjam/manual-testing-playbook/board-quality/user-flow-board-quality.md` against `references/flow-mode.md` Section 2 and `references/types/user-flow.md` Section 5: the scenario fixes three zones while the skill calls zones a choice and sets no count, so a source-faithful two-zone board fails a signal the request never asked for. FJ-022 fails on this alone. Either the scenario drops the count or the skill names how many zones a user flow draws.
2. `sk-create-figjam/scripts/flow_check.py` `Row:` hint with `references/flow-mode.md` Section 2 step 5: the hint moved Contact support into the zone beside its target, away from the decision it leaves. Both FJ-022 readers flagged the placement as odd though it costs no point. This is a minor gap with no scoring effect.

FJ-023's failure is a model slip against a rule that already exists, so it adds no skill gap. This is the last rerun, so both failures stand as known limitations.
