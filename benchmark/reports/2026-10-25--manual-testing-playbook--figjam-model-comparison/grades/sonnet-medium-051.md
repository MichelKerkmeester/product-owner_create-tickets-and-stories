# Rerun on v1.0.16.0, Claude Sonnet 5.5 medium (sonnet-medium-051)

One grader scored all ten runs on one scale from the transcripts, the tool streams, each render at 100% and in greyscale and two fresh readers per scored board. Composition is the output of `run/composition_check.py` on the last Glance line each run printed before its write for the user flow and process boards (four runs) and the playbook Composition row for the other six. The two readers differ from earlier reruns in one way. Reader a read all ten boards in one session and reader b read all ten in another, each told to treat every board as new. No two boards share a request, so the playbook's rule that a reader has not seen an earlier board of the same request holds.

| Scenario | Gallery board of the type | Verdict | Total | Composition |
|---|---|---|---|---|
| FJ-022 User flow board quality | 21 | FAIL | 20 | 0 |
| FJ-023 Process board quality | 22 | FAIL | 21 | 1 |
| FJ-024 Architecture board quality | 22 | FAIL | 20 | 1 |
| FJ-025 Sequence board quality | 22 | PASS | 22 | 2 |
| FJ-026 State board quality | 22 | FAIL | 20 | 1 |
| FJ-027 ER board quality | 21 | PASS | 22 | 2 |
| FJ-028 Gantt board quality | 20 | FAIL | 20 | 1 |
| FJ-032 Existing board with content | 22 | PASS | 22 | 2 |
| FJ-036 Dense flow at budget | 21 | FAIL | 20 | 1 |
| FJ-049 Status lane board quality | ungraded | FAIL | 19 | 0 |

**Pass count: 3 of 10. Fail count: 7. Not run: 0.**

Nothing was written before a gate's yes in any run. Every delivery reply opens on the board URL and ends on the HVR self-scan line, every read-back count is true against its model and no run loses a Hygiene point. Every one of the seven failures loses Composition, and six of the seven lose it to the Glance line or the playbook row rather than to a model slip. FJ-024 and FJ-026 add one more loss each, FJ-028 and FJ-036 lose a Shared trunks point and FJ-049 loses a Legibility point.

## Failures

- **FJ-022, 20 of 22, skill gap and playbook gap.** Composition is 0 because both readers read the green goal third, the orange exit fourth and the second diamond fifth, where the printed Glance line puts them last, fifth and seventh. The expected three zones are also missing, because the model drew none. The skill makes zones a choice and the scenario fixes three.
- **FJ-023, 21 of 22, skill gap.** Composition is 1 because both readers read the decision Damage clear in the photo? second, next to the pink accent in the CS agent lane, where the line puts it third. The rubric already says some readers do this and the printed line ignores it.
- **FJ-024, 20 of 22, model slip.** Composition is 1 because both readers read the API gateway ahead of sync-service. The gate's three glance lines name three of the nine nodes and leave out the gateway that quality-rubric.md Section 3 says reads right after the accent. Legibility is 1 because Apple's push service wraps with `service` alone on its last line, a wrap the check flagged and the model kept.
- **FJ-026, 20 of 22, skill gap and model slip.** Composition is 1 because both readers read the focus end state Cancelled before Pending. The playbook row does not say whether leading its own glance line is enough. Clarity is 1 because the board lets a guest cancel only from Upcoming. The intake round's recommended answer narrowed the user's 'Pending or Confirmed' and the driver accepted it.
- **FJ-028, 20 of 22, skill gap and composer.** Composition is 1 because both readers read the Release milestone second where the plan puts it last. The rubric lists no milestone among the early-read marks. Shared trunks is 1 where the Sync engine and Conflict screen build arrows crowd into the integration bar. Two arrows also run through bars, which costs no point.
- **FJ-036, 20 of 22, skill gap and composer.** Composition is 1 because both readers read the goal Updated booking third. Shared trunks is 1 where the Yes and Pick a room lines reach the left corner of New price? on one run.
- **FJ-049, 19 of 22, skill gap and composer.** Composition is 0 because both readers read Claim closed and Card charged early and took the status chain as one block, where the printed line interleaves each status with its step. Legibility is 1 because `days?` stands alone on the last line of the Accept within 7 days? diamond.

## Passes

- **FJ-025** passes at 22 on a split. The run drew a happy path and a declined card as two boards because sequence.md splits a failure path unless the user asks in so many words for one diagram. Composition is a judgment, since a sequence prints no Glance line and the Order lines name nodes only. A stricter reading would fail it, and the record says so.
- **FJ-027** passes at 22, one point above its gallery board, because all three reader questions were answered correctly.
- **FJ-032** passes at 22. The new section landed 400 px right of the prepared Sprint retro section with its top level and the six stickies read back unchanged.

## v1.0.16.0 rules, as the rerun shows them

- **Read-back after a later write:** not exercised. No run wrote after its compose and FJ-025's two boards are two composing calls.
- **Subtitle names the start and the end:** working on nine of ten boards. The ER subtitle on FJ-027 names neither, because an ER diagram has no flow and the rule has no ER wording. No point is lost.
- **Status lane (FJ-049):** working as set out. The lane is declared first with four statuses in one chain, each later status is reached by a dotted move the key names Moves the status and no status takes the accent. Three dotted moves cross the Hotel lane and one chevron's arrowhead touches its label.
- **Detail cards (FJ-049):** working. Report damage, Send claim to guest and Review dispute carry a bold label over their lines at Faithful and the board reads 14 nodes and 17 connectors within the 18 and 24 budget. The check refused a body on an end and the model dropped it.

## Skill gaps the rerun shows, most important first

1. **The Glance line against the order readers take** (`sk-create-figjam/references/quality-rubric.md` Section 3 and `sk-create-figjam/scripts/flow_check.py`). All four boards that print a Glance line lose Composition, six points in all. Readers take the filled end marks, the goal and the decision beside the accent before the white steps. On FJ-049 they also take the status chain as one block. The rubric admits this and the line still prints drawn order. Print the goal and ends early or let the playbook read the entry, goal and exits as a set.
2. **Plans for the types that print no Glance line** (the same rubric section). The model writes three short lines, nothing checks that every node sits in one. The milestone is also missing from the early-read marks. FJ-024 and FJ-028 lose Composition for it. Print a Glance line for every type.
3. **Composition rows that are silent** (`sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md` Section 3). A sequence's participants against a message plan and a state board's focus state against its first state have no rule, so FJ-025 rests on a judgment and FJ-026 could score 0 or 1.
4. **Two scenarios against the skill** (`board-quality/user-flow-board-quality.md` and `board-quality/sequence-board-quality.md`). FJ-022 fixes three zones where zones are a choice. FJ-025 expects the declined path cut where the skill splits it.
5. **Composer geometry** (`sk-create-figjam/scripts/compose_board.py`). Gantt arrows run through bars and crowd one corner, two edges join one diamond corner on FJ-036 and the status lane lets dotted moves cross a lane and a chevron's arrowhead touch its label.
6. **Advisory label hint** (`sk-create-figjam/scripts/flow_check.py`). The `Label:` line never refuses, so a flagged wrap ships on FJ-024 and FJ-049. On FJ-049 no reword that keeps the policy's number avoids it.
7. **Intake recommendations that narrow a source** (`sk-create-figjam/references/flow-mode.md` Section 4). FJ-026's recommended answer limited a stated rule and FJ-032's followed it, so the skill allows both.
8. **Small mismatches with no point lost.** The gate's checked sketch shows a light orange accent pair that the composer draws pink (FJ-023), the ER subtitle rule has no ER wording (FJ-027) and the reply is not required to say the prepared content was left alone (FJ-032).
