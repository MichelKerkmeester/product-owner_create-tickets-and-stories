# Sonnet high rerun grades on v1.0.6.0

These are the grades for the 31 scenarios Claude Sonnet 5.5 at high effort ran again on `sk-create-figjam` v1.0.6.0, the 29 that failed and the 2 that were skipped on v1.0.5.0, plus three gallery runs of FJ-022, FJ-023 and FJ-028. One grader scored all 34 runs, so every total sits on one scale. The per-run detail with every signal, cite, loss, location and fix is in `sonnet-high-rerun.jsonl` and `sonnet-high-gallery.jsonl`.

The rerun passes 14 of the 27 runs it could grade. 13 fail and 4 are SKIP because the driver performs no operator step. These counts include the skeptic rulings listed under What the skeptics changed.

## How the grades were set

- **Signals.** Each run starts from the checker's reading. Where the grade overturns it, the signal's cite says so.
- **Turn shifts.** An intake round, or the plan question FJ-017 had to ask, that pushes the playback, gate or write one turn later is accepted.
- **Harness.** FJ-018, FJ-035, FJ-044 and FJ-045 are marked `driver: operator-only`, so each is SKIP. FJ-031 ran without its operator setup, so the operator sticky is marked harness. FJ-032 also skipped its setup, but the pinned file already held the prepared retro board, so its signals are graded and only Clarity Q3 is lost to the skipped whole-page screenshot. FJ-031's first board was deleted by its own scripted turns and has no render.
- **Clarity.** Fresh readers answered from the colour and greyscale renders in `renders/`.

## The 31 reruns

| ID | v1.0.5.0 | v1.0.6.0 | Total |
|---|---|---|---|
| FJ-002 | FAIL | PASS | no board |
| FJ-005 | FAIL | PASS | no board |
| FJ-009 | FAIL | FAIL | no board |
| FJ-011 | FAIL | PASS | no board |
| FJ-012 | FAIL | PASS | no board |
| FJ-017 | FAIL | FAIL | 20 |
| FJ-018 | SKIP | SKIP | no run |
| FJ-019 | FAIL | PASS | 22 |
| FJ-020 | FAIL | FAIL | no board |
| FJ-024 | FAIL | PASS | 22 |
| FJ-025 | FAIL | PASS | 22 |
| FJ-026 | FAIL | FAIL | 20 |
| FJ-027 | PASS (rescored) | PASS | 21 |
| FJ-029 | FAIL | FAIL | 21 |
| FJ-031 | FAIL | FAIL | 21 |
| FJ-032 | FAIL | FAIL | 20 |
| FJ-033 | FAIL | FAIL | 21 |
| FJ-034 | FAIL | FAIL | 21 |
| FJ-035 | SKIP | SKIP | no run |
| FJ-036 | FAIL | FAIL | 21 |
| FJ-037 | FAIL | PASS | 22 |
| FJ-038 | FAIL | FAIL | no board |
| FJ-039 | FAIL | PASS | no board |
| FJ-040 | FAIL | FAIL | no board |
| FJ-041 | FAIL | PASS | no board |
| FJ-042 | FAIL | FAIL | no board |
| FJ-043 | FAIL | PASS | no board |
| FJ-044 | FAIL | SKIP | no run |
| FJ-045 | FAIL | SKIP | no run |
| FJR-001 | FAIL | PASS | no board |
| FJR-005 | FAIL | PASS | no board |

## Pass count by category

| Category | Pass | Fail | Skip |
|---|---|---|---|
| type-choice | 3 of 3 | 0 | 0 |
| pre-write-check | 2 of 2 | 0 | 0 |
| intra-routing-recall | 2 of 2 | 0 | 0 |
| board-quality | 3 of 4 | 1 | 2 |
| boundaries | 3 of 7 | 4 | 0 |
| board-write | 1 of 3 | 2 | 1 |
| board-creation | 0 of 6 | 6 | 1 |
| All | 14 of 27 | 13 | 4 |

## Gallery runs

| ID | v1.0.5.0 | v1.0.6.0 | Note |
|---|---|---|---|
| FJ-022 | PASS, 22 | PASS, 21 | Every exit labelled and the goal accented, one Legibility point lost where Order detail (Start a return) wraps inside its parenthesis |
| FJ-023 | PASS, 21 | FAIL, 18 | The claims table log was left off, so 7 of 8 nodes and Fidelity 0, with Composition and Legibility at 1 |
| FJ-028 | PASS, 21 | PASS, 20 | Two crowded arrowheads into the integration bar, a composer limit, and Clarity Q1 missed on the widened critical chain |

## Remaining failures

- **FJ-009, model slip and skill gap.** Turn 1 skipped the playback and showed the checked model with the missing-route report. The reply to the yes never says the fj route cannot draw a gantt. The No route section does not say the playback still comes first.
- **FJ-017, model slip.** 20 with Composition at 0, because Pending, planned last, reads before the two notes planned second and Confirmed reads before Cancelled. The sticky signal is unmet: note:2 sits left of No-show across a connector and note:1 sits at the board's far right edge. The gate signal is unmet as a skill gap, since the plan question pushed the gate to turn 3.
- **FJ-026, skill gap and model slip.** 20 with Composition at 1 and Reply at 1. The request is about the end states, but the first glance must be one element and never a group, so the run planned the Confirmed section and the accent never reaches an end state. The read-back line also claims ', read visually' with no screenshot read.
- **FJ-029, skill gap.** 21. The run kept the ten-step flow on one board, as the budget rule says when the user asked for one board, so the two ordinal boards the scenario expects do not exist. The self-loop it used draws at zero length with its label on the node edge. The model chose it over the split flow_check.py asked for, and it costs no Label collisions point.
- **FJ-031, model slip and skill gap.** 21 with Composition at 1. The revision's changed exit was planned as the last glance where quality-rubric.md rule 67 makes it the second. The accent rightly stays on Return confirmed, so Signal is 2, but the playbook Composition row wants the changed element first, which no compliant board can give. The delete flow itself was correct.
- **FJ-032, model slip.** 20. Pending reads ahead of the exits planned second, and Clarity Q3 is lost to the skipped whole-page screenshot. The prepared retro board was in the pinned file and kept its place.
- **FJ-033, model slip.** 21 with Composition at 1, because the planned second glance on Apple Push does not hold. The three apps stay separate and a Change Store was added, so the capability-words signal is unmet, and no reply names the Executive audience or the Simplified level, the dial words flow-mode sets.
- **FJ-036, model slip.** 21 with Reply at 1. The reply opens on a cleanup line instead of the board URL and reports where the board landed. Composition is 2 and the shared trunk from v1.0.5.0 is gone.
- **FJ-020, model slip.** The first reply's Open item 1 asks the user to confirm the target FigJam file, a board fact the conflict question must leave out.
- **FJ-034, composer styling.** 21 with Composition at 1. The heavy green goal outline on Refund released reads before the Approved exit and the loop planned second.
- **FJ-038, model slip.** It never says the recompose waits on a yes, and it never says the old section is deleted only on a second yes asked after the new board is read back.
- **FJ-040, skill gap.** The first reply asked the type question and recommended one overview of all five areas, so no single flow was read back, and turn 3 shows no Left out: line.
- **FJ-042, model slip.** The checked model draws the inferred Send the item back step with no assumed mark.
- **FJ-023 gallery, model slip.** 18. The claims table log was left off although process.md draws a log write that runs today, and the labels drift from the example model.

## Skill gaps, most important first

1. **The first glance cannot be a group.** `references/quality-rubric.md` Section 3 makes the first glance one node, while Composition scores whether the element the request is about reads first. FJ-026 asked about the end states and lost Composition. FJ-031 is the same family from the other side: quality-rubric.md rule 67 keeps a revision's accent on the goal and makes the changed end the second glance, while the playbook Composition and Signal rows want the changed element first.
2. **One board against a split.** `references/flow-mode.md` Section 3 rung 4 and the Section 5 budget bullet cut and offer the split when the user asked for one board, while FJ-029 expects two boards in one file.
3. **Two first-reply duties collide.** `references/flow-mode.md` Section 2 (a brief across several flows) and Section 3 (two types fit) both claim the first reply, and FJ-040 folded the scope into the type question.
4. **No route skips the playback.** `references/flow-mode.md` Section 6 No route does not say the playback and gate still come first, and FJ-009 went straight to the missing-route reply.
5. **Single sticky with no free side.** `references/hybrid-workflow.md` names right, above or below and gives no place when all three are taken, as at FJ-017's No-show.
6. **Plan question against the gate turn.** `references/flow-mode.md` Section 6 asks one plan question before the gate when whoami returns several plans, while FJ-017 expects the gate in turn 2.
7. **Nothing exported against the paired re-save.** The playbook's Hygiene invariant has no exception for the Story re-save that `references/flow-mode.md` delivery owns and FJ-037 requires.
8. **Self-loops pass the check.** `scripts/flow_check.py` passes a self-loop that `assets/compose-board.js` draws at zero length with its label on the node edge (FJ-029).
9. **Guard labels carry model ids.** `references/types/state.md` and the checks let a guard read `[from InStay]` beside a state labelled In stay (FJ-026, FJ-032).

## What the skeptics changed

Each run's grade was challenged by a skeptic and settled by an adjudicator. These are the changes where the skeptic won, folded into the jsonl records.

- **FJ-022 gallery.** Legibility 2 to 1 for the Order detail (Start a return) wrap, total 22 to 21. The scorecard signal was added as met. PASS holds.
- **FJ-023 gallery.** Composition 2 to 1, Fidelity 2 to 0 for the 7 of 8 count and the label drift and Legibility 2 to 1, total 22 to 18. The non-loss entry was replaced with real losses. FAIL holds.
- **FJ-028 gallery.** Clarity 2 to 1 for the missed Q1, total 21 to 20. The Shared trunks fix now names the 16 px offset in the gantt router. PASS holds.
- **FJ-017.** Composition 1 to 0, total 21 to 20. The sticky signal now names both stickies and the gate signal is unmet as a skill gap. FAIL holds.
- **FJ-018.** One placeholder signal split into the scenario's three harness signals. SKIP holds.
- **FJ-019.** The fallback signal moved from harness to met and the Writes Blocks location was corrected. PASS holds.
- **FJ-020.** The board-free first reply and the later-round signals are unmet. PASS to FAIL.
- **FJ-025.** The reason names the read-back as the glance source. PASS holds.
- **FJ-026.** Reply 2 to 1, total 21 to 20. The scorecard and glance-order signals were added as unmet and the non-loss guard entry was removed. FAIL holds.
- **FJ-027.** Clarity 2 to 1 for the missed Q1, total 22 to 21. The count signal and reason carry the harness note on the missing schema note. PASS holds.
- **FJ-029.** Label collisions 1 to 2, total 20 to 21. The two-board signals were split into separate unmet rows and the scorecard signal added as met. FAIL holds.
- **FJ-031.** Signal 1 to 2, total 20 to 21. The board-count signal is harness, the scorecard signal was added as unmet and the skill gap now cites rule 67. FAIL holds.
- **FJ-032.** The prepared stickies signal moved from harness to met and the reason and Clarity loss now name the skipped screenshot. FAIL holds at 20.
- **FJ-033.** Composition 2 to 1, total 22 to 21. The capability-words signal is unmet. FAIL holds.
- **FJ-034.** Composition 2 to 1, total 22 to 21. The glance-order signal was added as unmet and the reader and lanes signals as met. PASS to FAIL.
- **FJ-036.** Composition 1 to 2 and Reply 2 to 1, total stays 21. The scorecard signal was added as unmet and the glance-order signal as met. FAIL holds.
- **FJ-037.** A skill gap was added for the Hygiene invariant against the Story re-save. PASS holds at 22.
- **FJ-038.** The compose-after-yes signal is unmet and the no-gate signal was added as met. FAIL holds.
- **FJ-044 and FJ-045.** One placeholder signal split into ten and seven harness signals, with the stdout record added to the evidence. SKIP holds.
- **FJR-001.** The rules-load signal is unmet because references/types/user-flow.md was never read. PASS holds.
