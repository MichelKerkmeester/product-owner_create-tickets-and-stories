# Rerun on v1.0.17.0, Claude Sonnet 5.5 medium (sonnet-medium-052)

One grader scored all ten runs on one scale from the transcripts, the tool streams, each render at 100% and in greyscale and two fresh readers per scored board. Composition is the output of `run/composition_check.py` on the last Glance line each run printed before its write for the user flow and process boards (FJ-022, FJ-023, FJ-036 and FJ-049). The other six score Composition by the playbook row, applied by hand to the gate's glance lines and the two readers' Order lines. Every board names Q4 and Q5, so each is out of 24 and passes at 20 with Composition, Fidelity, Reply, Substance and all four Hygiene checks at full marks. The 051 totals were out of 22 with no Substance. Only the run under `skill/sonnet-medium-052/` is graded for the scenarios that ran twice.

| Scenario | 051 verdict | 051 total (of 22) | 052 verdict | 052 total (of 24) | Composition | Substance |
|---|---|---|---|---|---|---|
| FJ-022 User flow board quality | FAIL | 20 | FAIL | 22 | 0 | 2 |
| FJ-023 Process board quality | FAIL | 21 | PASS | 24 | 2 | 2 |
| FJ-024 Architecture board quality | FAIL | 20 | FAIL | 22 | 0 | 2 |
| FJ-025 Sequence board quality | PASS | 22 | FAIL | 22 | 0 | 2 |
| FJ-026 State board quality | FAIL | 20 | FAIL | 22 | 0 | 2 |
| FJ-027 ER board quality | PASS | 22 | FAIL | 22 | 2 | 1 |
| FJ-028 Gantt board quality | FAIL | 20 | PASS | 22 | 2 | 2 |
| FJ-032 Existing board with content | PASS | 22 | PASS | 24 | 2 | 2 |
| FJ-036 Dense flow at budget | FAIL | 20 | FAIL | 22 | 1 | 2 |
| FJ-049 Status lane board quality | FAIL | 19 | FAIL | 22 | 0 | 2 |

**Pass count: 3 of 10. Fail count: 7. Not run: 0.**

Nothing was written before a gate's yes in any run, every delivery reply opens on the board URL and ends on the HVR self-scan line, every read-back count is true against its compose return and no run loses a Hygiene point. Nine of the ten boards score 2 on Substance, because the detail cards and lane notes of v1.0.17.0 now carry the source lines the questions ask for. Nine boards score 2 on Clarity. The one miss is FJ-028 Q1. Six of the seven failures lose Composition, and one of them also loses a Shared trunks point.

## Failures

- **FJ-022, 22 of 24, skill gap.** Composition is 0 because both readers read the green goal second or third and Contact support and the method diamond before the white cards, where the printed Glance line puts the goal last, the exit fourth and the diamond fifth. The board has the three zones with their notes, every detail card and a green goal with no accent. Script: `Composition 0, costing: Contact support, Drop-off or courier pickup?, Confirmation with QR code`.
- **FJ-024, 22 of 24, model slip with a skill gap.** Composition is 0 under the playbook row. The gate's glance lines name five of the nine nodes and leave out the three clients and the Blocks database, which both readers read before the Push worker. Quality-rubric.md Section 3 asks for every node in a line, and an architecture prints no line to check it against.
- **FJ-025, 22 of 24, model slip with a skill gap.** Composition is 0 by a hand count of the row. Both readers read Authorised after the post and the hold on board 1, and the post and the hold before Release the hold and 402 on board 2, where the plan puts the replies second. The 051 rerun passed this scenario on a judgment of 2, so the same kind of board scores 0 or 2 by method. Board 1 alone would score 1 and the verdict holds either way.
- **FJ-026, 22 of 24, skill gap.** Composition is 0 because the gate led with Pending as quality-rubric.md Section 3 says. The playbook row scores a state board 2 only when the focus state leads its glance line, and both readers read the pink Cancelled first. Clarity is now 2, because the intake round no longer narrowed who can cancel and Q2 reads Pending and Confirmed.
- **FJ-027, 22 of 24, composer with a model slip.** Substance is 1 and Fidelity is 1. The three payment statuses sat in a quoted column comment that the composer drops, so both readers answered Q4 with 'the board does not say'. The gate's critique named that risk and asked to write anyway.
- **FJ-036, 22 of 24, skill gap and composer.** Composition is 1 because both readers read the green goal right after the accent (script: `Composition 1, costing: Updated booking, also emailed`). Shared trunks is 1 where the Yes line and the Pick a room line meet at the left corner of New price?.
- **FJ-049, 22 of 24, model choice the skill permits.** The run drew no status lane. The statuses sit in card bodies, no chevron or dotted Moves the status line is drawn and two expected signals are missing. Composition is also 0 (script: `Composition 0, costing: Uphold the claim or drop it?, Charge the card, Closed`), a skill gap.

## Passes

- **FJ-023** passes at 24 with Composition 2 by the script. Lane notes sit under all three lanes, two steps carry detail cards, the Claims table draws as a cylinder and the accent names its reason in the key.
- **FJ-028** passes at 22 with Shared trunks 1 and Clarity 1. Reader a answered Q1 with three critical bars, because the intake round's recommended answer marked the whole chain to integration critical where the request names integration alone. The two arrows from Sync engine and Conflict screen build still meet at one corner of the integration bar, and two arrows run across bars, which costs no point.
- **FJ-032** passes at 24. The new section lands at x 1600, level with the top and 400 px right of the Sprint retro section, and the section and its six stickies read back unchanged. The readers saw only the new board, so their Q3 answer does not test the retro content and the two reads do.

## v1.0.17.0 rules, as the rerun shows them

- **Notes under each zone or lane title:** working on FJ-022 (three zones) and FJ-023 (three lanes). On FJ-049 the model wrote one note, for the Guest lane, and the check passed, so the rule is stated as required but not enforced.
- **Detail cards:** working on every board that exercises them, FJ-022, FJ-023, FJ-024, FJ-026, FJ-032, FJ-036 and FJ-049 (the check refused a body on the stadium goal in FJ-022).
- **Every accent names its reason:** working. FJ-022, FJ-023, FJ-024, FJ-025, FJ-026, FJ-027, FJ-028, FJ-036 and FJ-049 print `In focus: <reason>` in the key.
- **One compact key band:** one row on every board but one. On FJ-025 board 2 the In focus entry wraps to a second row and the band stands near 140 px against 88 px on board 1.
- **16 px card corner and the cylinder sample:** working. The Claims table (FJ-023), the stream and the database (FJ-024) draw as cylinders in the key and on the board.

## Skill gaps the rerun shows, most important first

1. **The Glance line against the order readers take** (`sk-create-figjam/references/quality-rubric.md` Section 3 and `sk-create-figjam/scripts/flow_check.py`). Three of the four boards that print a Glance line lose Composition, five points in all. Readers take the filled goal, the second diamond and the exit before the white steps. Print the goal and the decisions early or let the playbook read the entry, goal and decisions as a set.
2. **Plans for the types that print no Glance line, and a rubric that disagrees with the playbook row** (the same rubric section and `manual-testing-playbook/manual-testing-playbook.md` Section 3). FJ-024 names five of nine nodes, FJ-025 rests on a hand count that gave 2 in the last rerun and 0 now, and FJ-026 follows the rubric into a 0 under the row. Print a line for every type and make the rubric and the row say the same about a state board's first glance.
3. **The ER column comment the composer drops** (`sk-create-figjam/references/types/er.md` Section 3 and `sk-create-figjam/assets/compose-board.js`). The check passes a quoted comment and the board shows none, which cost FJ-027 a Substance point and a Fidelity point. Draw the comment or make the check refuse it.
4. **Optional status lane and unenforced lane notes** (`sk-create-figjam/references/types/process.md` and `sk-create-figjam/scripts/flow_check.py`). FJ-049 skipped the lane when the request asked for the status at each step and wrote one lane note of three.
5. **Intake recommendations that change a stated marking** (`sk-create-figjam/references/flow-mode.md` Section 4). FJ-028's recommended answer widened the critical marking and the driver took it.
6. **Composer geometry** (`sk-create-figjam/assets/compose-board.js`). Two edges join one corner on FJ-036 and FJ-028, and the key wraps to two rows on FJ-025 board 2.
7. **The label hint renames a proper noun** (`sk-create-figjam/scripts/flow_check.py`). FJ-024 turned Apple's push service into Apple push, against the rubric's rule on proper nouns. No point lost.
8. **Harness records.** FJ-036's `meta.json` lists one start section for a file that read back empty. A split's boards share labels, so one Order line cannot tell them apart. FJ-032's readers never see the retro content their Q3 asks about.
