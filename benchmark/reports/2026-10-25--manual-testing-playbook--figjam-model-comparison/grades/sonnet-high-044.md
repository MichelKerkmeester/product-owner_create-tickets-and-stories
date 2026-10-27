# Sonnet high rerun grades on v1.0.10.0

These are the grades for the 6 FigJam scenarios that failed on `sk-create-figjam` v1.0.9.0, run again by Claude Sonnet 5.5 at high effort on v1.0.10.0. One grader scored every run from the replies, the tool calls, the renders and two fresh readers per scored board, so every total sits on one scale. Skeptic and adjudicator rulings were then folded into the records, see the last section. The per-run detail with every signal, cite, loss, location and fix is in `sonnet-high-044.jsonl`.

The rerun passes 2 of the 6. 4 fail. None is NOT RUN. The skeptics failed FJ-032 on its intake signal, and the operator's ruling of 2026-10-27 passed it, see Operator ruling.

## How the grades were set

- **Glance order.** The plan is the gate's glance lines and the first glance is the read-back's `first glance:` clause, present on every scored board. The measured order is the reading order at the top of each reader file. A part costs a Composition point only when both readers read it early or out of order.
- **v1.0.10.0 rules applied.** On a user flow the planned order inside a glance line is path order. On FJ-031 the entry, the decisions and the main-row nodes planned last cost nothing when they read before the changed end. The goal and the entry, which the rubric says both read right after the accent, carry no order between them.
- **FJ-017.** Graded on the operator's 2026-10-27 reading of beside. The adjacent-row case did not arise, see below.
- **Label trace.** Every check run printed `Label: skipped, the trace failed (dyld ... libsimdutf ...)`, a harness fact. FJ-017, FJ-026, FJ-029, FJ-032 and FJ-036 show it in their check output. FJ-031 shows it in turns 3 and 7, and its turn 5 and turn 8 runs piped the check through `tail -1`, so the line is not in the export there.
- **Near-parallel runs.** Runs closer than 56 px on the composer's estimate are not counted, as in the v1.0.9.0 grades.
- **Evidence.** Replies, exports and meta files sit under `skill/sonnet-high-044/` and the renders in `renders/`. The reader notes are in `grades/sonnet-high-044/readers/<ID>-<node>-a.md` and `-b.md`, the greyscale renders in `grades/sonnet-high-044/grey/` and the FJ-031 operator step in `grades/sonnet-high-044/operator/`.

## The 6 scenarios

| ID | v1.0.9.0 | v1.0.9.0 total | v1.0.10.0 | v1.0.10.0 total |
|---|---|---|---|---|
| FJ-017 | FAIL | no scorecard | FAIL | no scorecard |
| FJ-026 | FAIL | 20 | FAIL | 19 |
| FJ-029 | FAIL | 19 | FAIL | 19 |
| FJ-031 | FAIL | 19 | PASS | 21 |
| FJ-032 | FAIL | 20 | PASS | 22 |
| FJ-036 | FAIL | 19 | FAIL | 20 |

Pass count: 2 of 6, up from 0 of these 6 on v1.0.9.0. The passes are FJ-031 and FJ-032. Composition is no longer 0 on every board: FJ-031 and FJ-032 score 2 and FJ-036 scores 1.

## The passes

- **FJ-032, 22 of 22, by operator ruling.** The board lands 400 px right of the untouched Sprint retro section with its top level, every count matches and both readers read Pending, then Upcoming and In stay, then the end states as planned. The second intake round asked the two rows round 1 had left open for it, see Operator ruling.
- **FJ-031, 21 of 22.** The v1.0.10.0 revision exemption brings Composition to full, every expected signal holds and the operator sticky never moved. The only point lost is Legibility for the wraps of Request an exception and Drop-off or pickup?. Two contract gaps go to skill gaps and are not counted as model faults: the two delivery replies name only the first glance, since the reply shape in `references/flow-mode.md` Section 8 does not carry the rubric's second-glance clause, and the turn 6 playback reads nothing first, since Section 6 asks for no such read. The delete question names the older board by position and content but not by its write time, a flag that does not change the verdict.

## Remaining failures

- **FJ-017, model slip and skill gap.** No scorecard. Turn 3 makes three `use_figma` calls where the scenario asks for two: a separate probe call creates and deletes a sticky on the page between the compose and the notes call, a write the gate's Calls line did not cover and the notes call's own probe made unneeded. No composed node moved and the reply carries `Extensions: 2 of 2 notes, 0 overlaps`. No-show and Cancelled sit two rows apart this time, so the adjacent-row rule did not bite. The No-show sticky stands 64 px past its end dot, level with it. Every side of Cancelled was taken, and the recipe's shortest-clear-line fallback put its sticky 688 px out at the widened board's far edge, which the model's own `Finding:` line calls not beside the state. The board subtitle also keeps a serial comma the self-scan reports as a kept hard blocker.
- **FJ-026, skill gap with a model slip.** 19 with Composition at 0 and Reply at 1. The composite now sits after Pending, but both readers read Pending, Upcoming and In stay on the top row before the planned first glance Cancelled on the bottom row. The model cannot move the end states. The delivery reply also opens on a sentence above the URL, a model slip.
- **FJ-029, model slip.** 19 with Composition at 0 and Legibility at 1. The split holds every structural signal. The gate plans by kind, putting the off-row Wrong code error second and Sign up and Enter email code last, and the same on board 2 with Teammates' emails, Name the workspace and Pick a template last. That runs against the v1.0.10.0 path-order rule and the user flow example, and both readers take those five nodes before nodes planned second. Three of the five sit on the drawn row but on the Add and Template branches rather than the plain entry to goal path. Five orphan wraps, all named on a `Finding:` line.
- **FJ-036, skill gap.** 20 with Composition at 1 and Legibility at 1. The plan now names every node and the main row in path order, and the gate ends on `Write it?`. The composer drew the detour Choose another room on the main row with Yes routed over the top, so both readers take it before the three outcomes planned second.

## The v1.0.10.0 fixes

- **Composite drawn after the state that enters it.** Working on FJ-017, FJ-026 and FJ-032: Confirmed now sits right of Pending on all three boards, and on FJ-026 and FJ-032, the two with readers, both readers take Pending first. FJ-032 reads exactly as planned and scores 22 of 22 on it. `flow_check.py`'s guard for a composite with no inner `[*]` was not exercised, since every model carried one.
- **Main row in path order.** Working in FJ-031's revision plan and FJ-036's plan. FJ-029 did not apply it, a model slip.
- **Revision exemption for main-row nodes planned last.** Working on FJ-031, which moved Composition from 0 to 2 and now passes.
- **FJ-017 adjacent-row reading.** Applied and not triggered, because the two noted states sit two rows apart.
- **`Label: skipped` with a load error.** Printed on every run, a harness fact.

## Skill gaps the rerun still shows, most important first

1. **A focused end state on a state board reads after the top row.** `references/types/state.md` Section 5 plans the named end state first, but the composer draws end states on the lower rows. On FJ-026 three parts read before the pink-outlined Cancelled. The fix sits in the composer placement or in a state rule that plans the focus where it is drawn.
2. **The main row is not defined as the row the composer draws.** `references/quality-rubric.md` Section 3 plans the main row in path order, but on FJ-036 the composer drew a detour that rejoins later on the row and routed the shorter Yes edge over the top, so a plan that calls it a detour cannot hold.
3. **The single-sticky fallback can park a sticky far from a boxed-in node.** `references/hybrid-workflow.md` Section 3 sends a sticky with no free side to the shortest clear line, which on FJ-017 was 688 px out at the board's edge, against the same section's ban on a sticky parked away from its node.
4. **A revision playback reads nothing first.** `references/flow-mode.md` Section 6 opens a revision on a playback with no `get_figjam` read, and FJ-031 missed the read on both v1.0.9.0 and v1.0.10.0.
5. **The revision's second glance is not in the reply shape.** `references/quality-rubric.md` Section 3 asks the reply to name the changed end as the second glance, and the Read-back line in `references/flow-mode.md` Section 8 lists only the first glance.
6. **The read-back cannot read connector labels.** `references/flow-mode.md` Section 7 matches labels from `get_figjam`, which returns connector names and no label text, so every board reply in this rerun says the labels were checked on the write's own return or the screenshot.
7. **Two intake sentences disagree.** `references/flow-mode.md` Section 2 says the reply after accepted answers is the playback or one round about a gap those answers opened, and a later sentence lets a round ask any row left unasked. FJ-032 passed only by operator ruling.

## What the skeptics changed

- **FJ-017, verdict FAIL stands, no scorecard.** The signal "Turn 3 calls use_figma twice" moved from met to not met. Turn 3 made three `use_figma` calls, and the separate probe created and deleted a page node on a yes that covered only a compose call and a notes call. The reason now names both failed signals.
- **FJ-029, verdict FAIL and total 19 stand.** The Composition loss now counts five parts read early, not four: Pick a template, planned last, is read by both readers before Editor opens, planned second. The reason now says three of the five sit on the drawn row but on the Add and Template branches, not "main-row screens". Composition stays 0.
- **FJ-031, FAIL at 20 became PASS at 21.** Reply moved from 1 to 2, since the Reply bands in the playbook are about lines and every line is present, in order and true. The Reply loss was removed. The signal "The playback reads the board with get_figjam first" was removed from the signals, because it is not in the scenario's expected-signal list, and it stays recorded under skill gaps. The scorecard signal moved to met at 21 of 22. The reason was rewritten.
- **FJ-032, PASS became FAIL, total 22 stands.** The signal "Turn 1 ends on the playback and writes nothing" moved to not met, because the second intake round asked about gaps already listed in round 1 rather than gaps the accepted answers opened. The reason was rewritten.

## Operator ruling

- **FJ-032 passes (2026-10-27).** The adjudicator failed it because the second intake round followed the accepted answers, where `references/flow-mode.md` Section 2 says the next reply is the playback or one round about a gap those answers opened. Round 1 had listed what moves Upcoming to In stay and mid-stay cancelling as still open for round 2, and the same section lets a later round ask a row left unasked, so the operator ruled the round within the rule. The signal is met and FJ-032 passes, so the rerun passes 2 of 6. The two sentences that disagree are recorded as a skill gap.
