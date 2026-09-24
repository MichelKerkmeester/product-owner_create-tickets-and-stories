# Remeasure grading: Product Owner

GLM 5.3 Flash (thinking high) through the Pi CLI. Three runs each of `SDK-001` and `PDK-001`, graded against the scenario files as they stand after the repairs.

How each verdict was reached:

- The verdict comes from the scenario's Pass/fail line and its Pass / fail section. Chain and Expected signals details that neither names are listed as notes, not scored
- PARTIAL means the Pass bullet is unmet while no fail clause fired
- File claims were checked against each turn's `ledger` in `meta.json` and against `exports/`. For the skill runs, every read-back was matched to the path its `write` used
- Guide layout was checked line by line: `* * *` directly under every content heading, `*   ` bullets, no `---` and no hyphen bullets. The supplied values were checked in the guide text
- A Project run breaks its no-file contract only through a save claim or a non-empty ledger

## Results

| ID | Run | Verdict | Evidence |
|---|---|---|---|
| SDK-001 | 1 | PASS | Turn 1 export: "I will treat the audience as the support team and the intent as a Behavior reference (how the pipeline behaves, so support can predict outcomes) unless you say otherwise. No draft until you answer." |
| SDK-001 | 2 | PASS | Turn 1 export: "predict how the pipeline behaves when tickets come in (behavior reference), or follow troubleshooting steps during incidents (guide), or both? This decides the shape" |
| SDK-001 | 3 | PARTIAL | Turn 1 export decides the shape instead of asking it: "Once the notes land, the document will be a behavior reference" |
| PDK-001 | 1 | PASS | Turn 1: "If you'd rather have a troubleshooting guide (ordered steps) instead, say so in the same reply." |
| PDK-001 | 2 | PASS | Turn 1 block, under Shape: "If support also needs troubleshooting steps or an escalation path, a guide fits better. Which should I write?" |
| PDK-001 | 3 | PARTIAL | Turn 2 guide: `### Quality checks` is followed directly by `*   [ ] The notification sits in the failed queue, past attempt six`, with no divider between them |

## Per-scenario summary

### SDK-001: 2 of 3 passed, 1 PARTIAL

Turn 1 coverage, read from each clarification export:

| Run | Notes | Authority | Status | Shape | Scope | Read back | Waited |
|---|---|---|---|---|---|---|---|
| 1 | asked | asked, which source wins | asked | default stated, open to override | asked | yes | yes |
| 2 | asked | put as a confirm item, "These are the governing source" | asked | asked | asked | yes | yes |
| 3 | asked | asked, which one governs | asked | decided, not asked | asked | yes | yes |

- Turn 2 in all three runs saves the guide, reads the same path back and replies with the path, the HVR self-scan line and a Doc quality summary. Every guide has `* * *` under each content heading, `*   ` bullets, sentence-case headings, no `---` and no hyphen bullets. The 30 second backoff, five attempts, attempt six, failed queue and Requeue action all survive
- Run 3 is PARTIAL. No fail clause fired: it did not ask for the notes alone, held no field for a later turn and did not draft early. But the Pass line names shape among the fields the question must cover, and run 3 settled the shape itself and told the user the listed fields were "the only unresolved contract inputs". This matches `doc-mode.md` Step 4 and Section 12, which allow inferring the shape when the intended use is clear. The scenario and the runtime rule disagree on this point, and the run was graded against the scenario
- Source fidelity: no guide adds a timing, state or action the notes lack. Run 2 goes past the notes' wording with "Requeue only works from the failed queue, so this is the one way back into the retry cycle." Runs 2 and 3 also state as fact that a notification can be requeued again, which run 1 lists as a gap: "the notes do not state whether a notification can be requeued more than once". Both read as derivations from the notes' general rules, so they were not scored as invented behavior
- Run 3 brings in "merchant" as a reader in both its clarification and its guide. The notes never mention one
- Not verdict factors: all three name the clarification `001 - doc-notification-retry-pipeline-clarification.md` where the Expected signals show `doc-notification-retry-clarification.md`. All three put the five Doc dimensions on one line where the chain asks for one line per dimension. Runs 1 and 3 print no question text in the Turn 1 reply and point at the export instead

### PDK-001: 2 of 3 passed, 1 PARTIAL

Turn 1 coverage, read from each rendered clarification block:

| Run | Notes | Authority | Status | Shape | Scope | Label | Waited |
|---|---|---|---|---|---|---|---|
| 1 | asked | stated in the question, "they are the governing source" | asked | default stated, open to override in the same reply | asked | yes | yes |
| 2 | asked | stated in the question, "They are the primary source" | asked | asked | asked | yes | yes |
| 3 | asked | asked, "Do the notes govern every claim in the document?" | asked | asked, with inference as the fallback | asked | yes | yes |

- All six ledgers are empty. Every block carries an `Export-equivalent path:` label and no reply prints `Path:` or claims a save. Run 3 also prints each path as a heading line, which is a label, not a save claim
- Runs 1 and 2 render guides that pass the layout check, with every supplied value intact. Run 1 flags the requeue limit as unstated. Run 2 writes "The Requeue action exists only there", the same overreach as SDK-001 run 2
- Run 3 is PARTIAL. Its Turn 1 is the most complete of all six Product Owner runs, but its Turn 2 guide misses the divider under `### Quality checks`. It also renders five empty spacer headings (`###   ` and `##   `) inside an export-equivalent guide, and `doc-templates.md` keeps those for ClickUp-bound content only. Two of them do not match the level of the section they close. The reply still reports the layout as a pass. No fail clause fired: the guide has no `---`, no hyphen bullets and no save claim
