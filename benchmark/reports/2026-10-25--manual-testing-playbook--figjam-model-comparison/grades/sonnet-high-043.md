# Sonnet high rerun grades on v1.0.9.0

These are the grades for the 7 FigJam scenarios that failed on `sk-create-figjam` v1.0.8.0, run again by Claude Sonnet 5.5 at high effort on v1.0.9.0. One grader scored every run from the replies, the tool calls, the renders and two fresh readers per scored board, so every total sits on one scale. The per-run detail with every signal, cite, loss, location and fix is in `sonnet-high-043.jsonl`.

The rerun passes 1 of the 7. 6 fail. None is NOT RUN. The grading workflow passed FJ-017 too, and the operator's ruling of 2026-10-27 failed it, see Operator ruling.

## How the grades were set

- **Glance order.** The plan is the gate's glance lines and the first glance is the read-back's `first glance:` clause, present on every scored board. The measured order is the reading order at the top of each reader file.
- **Two readers.** A part costs a Composition point only when both readers read it early or out of order, and each part counts on its own. On a state board the states inside a composite are parts. Two parts read in the reverse of the planned order score Composition 0. Items in one glance line carry no order among themselves. The first grading counted a glance-line group as one point, and the skeptic pass moved FJ-026, FJ-029, FJ-031 and FJ-032 to per-part counting, see What the skeptics changed.
- **Legibility.** A label that wraps with one word alone on its last line costs one point, as before.
- **Near-parallel runs.** Under the v1.0.9.0 style-guide rule, runs the composer routes closer than 56 px are not counted against the board (the 24 px check out and missed check-in runs on the state boards and the 16 px arrivals at FJ-036's New price?).
- **Turn shifts.** An intake round that pushes the playback, the gate and the write later is accepted (FJ-029 with two rounds, FJ-031 and FJ-036 with one).
- **Harness.** FJ-009 ran with no Figma server as its precondition says. Board URLs and file keys are redacted in the run folder.
- **Evidence.** Replies, exports and meta files sit under `skill/sonnet-high-043/` and the renders in `renders/`. The reader notes are in `grades/sonnet-high-043/readers/<ID>-<node>-a.md` and `-b.md`, the greyscale renders in `grades/sonnet-high-043/grey/` and the FJ-031 operator note in `grades/sonnet-high-043/operator/`.

## The 7 scenarios

| ID | v1.0.8.0 | v1.0.8.0 total | v1.0.9.0 | v1.0.9.0 total |
|---|---|---|---|---|
| FJ-009 | FAIL | no board | PASS | no board |
| FJ-017 | FAIL | no scorecard | FAIL | no scorecard |
| FJ-026 | FAIL | 21 | FAIL | 20 |
| FJ-029 | FAIL | 19 | FAIL | 19 |
| FJ-031 | FAIL | 18 | FAIL | 19 |
| FJ-032 | FAIL | 21 | FAIL | 20 |
| FJ-036 | FAIL | 20 | FAIL | 19 |

Pass count: 1 of 7, up from 0 of these 7 on v1.0.8.0. Every Reply now scores 2, which was the failure on FJ-029, FJ-031 and FJ-036 last time. Every remaining failure has Composition at 0, on all five scored boards.

## Remaining failures

- **FJ-017, model slip.** No scorecard. The Cancelled note sits right of its node, 64 px under the No-show note, where `references/hybrid-workflow.md` Section 3 sends a second sticky on an adjacent row below or to the left. The `Finding:` line names the placement. It fails under the operator's ruling below.
- **FJ-026, skill gap.** 20 with Composition at 0. The gate plans Cancelled first, Pending with Upcoming and In stay second and the other end states last, as the v1.0.9.0 state rule asks. Both readers read Upcoming and In stay inside the Confirmed box on the top row before the pink-outlined Cancelled and before Pending, two parts at a point each. The composer places the composite there, so the model cannot move it.
- **FJ-029, model slip with a skill gap behind it.** 19 with Composition at 0 and Legibility at 1. The split now holds every signal: `1. Sign up` and `2. Workspace setup` 400 px apart, `start here: 1. Sign up` and the split on a `Left out:` line. The gate plans Code correct? second and Email or Google?, the same yellow diamond, last. Both readers read the row from the left and reach Code correct? after Email or Google? and Enter the email code, two parts at a point each. The board shows seven orphan wraps. The turn 4 gate reply also says board 2 has 3 decisions where the model holds 2, a further FAIL ground.
- **FJ-031, skill gap.** 19 with Composition at 0 and Legibility at 1. The plan follows the v1.0.9.0 revision rule, with Request an exception alone in the second glance. The exemption covers the entry and the decisions, and both readers also read Order detail and Return reasons on the main row before the changed exit drawn below it, two parts at a point each. The revision kept its title, asked the delete on a `Finding:` line, deleted only the tagged older section on its own yes and left the operator sticky alone. The turn 5 playback made no `get_figjam` read, which misses the read step the scenario asks for.
- **FJ-032, skill gap.** 20 with Composition at 0. The gate plans Pending first with no focus line as the state rule asks, and both readers read Upcoming and In stay in the Confirmed band before Pending, two parts at a point each. A `Finding:` line on where the board landed is a model slip against `references/flow-mode.md`, and Reply keeps 2. The retro section kept its count, positions and sizes and the board landed 400 px to its right.
- **FJ-036, model slip.** 19 with Composition at 0 and Legibility at 1. The gate names no glance line for Pick new dates or Room free on those dates?, and both readers take them and See other rooms, planned last, before the three outcomes planned second. The gate turn also ends on a status paragraph after `Write it?`, which misses the turn 2 signal on its own.

## The v1.0.9.0 fixes

- **Reply opens on the URL.** Working on every board reply, including FJ-036, which failed on this last time.
- **Reply after a delete.** Working. FJ-031 turn 8 opens on the URL of the board that stays and repeats the `Left out:` line.
- **Revision keeps the old title.** Working. FJ-031's new board is `Start a return` and the older section was found by its tag write time.
- **Changed end alone as the second glance.** Working in FJ-031's gate and read-back. The board still reads the plain main-row screens first, see gap 2.
- **Split named under `Left out:` and `2. Workspace setup`.** Working on FJ-029.
- **State glance order.** Followed in the FJ-026 and FJ-032 gates. Not shown by either board, see gap 1.
- **Adjacent-row sticky with a `Finding:` line.** The `Finding:` line works on FJ-017. The sticky itself sits right of its node where `references/hybrid-workflow.md` Section 3 sends it below or to the left, a model slip that fails FJ-017 under the operator's ruling.
- **`Label: skipped` with the reason.** Working. Every check run prints it, see gap 3.
- **FJ-009 missing-route gate.** Working. The gate asks `Send the model?` with a Route line in place of Plan and Calls, and turn 3 says the earlier yes covered the model, not a write.
- **56 px rule on the composer's estimate.** Applied. No board lost Shared trunks for a composer run.

## Skill gaps the rerun still shows, most important first

1. **The composite takes the first read on every state board.** `references/types/state.md` Section 5 now plans the inner states second, but the composer draws the composite on the top row, and on FJ-026 and FJ-032 both readers read its states before the planned first glance. A pink focus outline on Cancelled did not change that. The fix sits in the composer placement or in a state rule that plans the inner states where they are drawn.
2. **Main-row order on flows.** `references/quality-rubric.md` Section 3 exempts only the entry and the decisions on a revision, and nothing tells a plan that readers take the main row in path order after the accent. FJ-031's plain screens, FJ-029's split diamonds and FJ-036's unnamed nodes all lose on this. FJ-036's two unnamed nodes are also a plain model slip, because the rubric warns that a part the lines leave out reads early.
3. **The label trace never ran.** `scripts/flow_check.py` printed `Label: skipped` on every run because node fails to load a library on the run machine. The by-eye fallback in `references/style-guide.md` gives no width rule, and orphan wraps cost Legibility on FJ-029, FJ-031 and FJ-036. The run machine's node install needs fixing before the next rerun.
4. **The read-back cannot read connector labels.** `references/flow-mode.md` Section 7 matches labels from `get_figjam`, which returns connector names and no label text, so five replies say the labels were checked on the composing screenshot instead.

## What the skeptics changed

- **FJ-009.** The no-board signal stays met. Its cite now says no reply prints a board URL, because turn 3 prints the hosted MCP server endpoint on its Finding line. PASS stands.
- **FJ-017.** The adjacent-row sticky skill gap is removed and recorded as a model slip: the Cancelled sticky sits right of its node where `references/hybrid-workflow.md` Section 3 sends it below or to the left. PASS stands with no scorecard.
- **FJ-026.** Composition 1 to 0 and total 21 to 20, because Upcoming and In stay are two parts. The loss costs 2 points, the scorecard signal cite reads 20 of 22 with Composition at 0 and the reason is rewritten. FAIL stands.
- **FJ-029.** Composition 1 to 0 and total 20 to 19, because Email or Google? and Enter the email code are two parts. The Legibility loss adds the Google? and correct? orphans for seven in all, and the shared label-trace gap now says seven. The gate signal stays met and records the 3 decisions count misstatement as a further FAIL ground. FAIL stands.
- **FJ-031.** Composition 1 to 0 and total 20 to 19, because Order detail and Return reasons are two parts. The operator sticky signal moves from harness to met. Five omitted signals are added as met: the node and connector counts, the read-back before any delete, the gate's yes covering the compose only, the delete on its own yes and the delete found by its tag. The turn 5 playback signal stays met with a flag for the missed `get_figjam` read. The Legibility loss adds the source line's `review.` orphan. FAIL stands.
- **FJ-032.** Composition 1 to 0 and total 21 to 20, because Upcoming and In stay are two parts. The loss costs 2 points, the scorecard signal cite reads 20 of 22 with Composition at 0 and the reason is rewritten. The landing Finding line skill gap is removed and recorded as a model slip with Reply at 2. FAIL stands.
- **FJ-036.** No ruling. Only its copy of the label-trace gap now says seven orphans. 19 and FAIL stand.

No verdict changed in the skeptic pass, which left the count at 2 of 7.

## Operator ruling

- **FJ-017 fails on the 042 reading of beside (2026-10-27).** The adjudicator kept PASS because the scenario signal asks only that each sticky land beside its node. The operator applied the reading the v1.0.8.0 grade used, under which a second sticky on an adjacent row that sits right of its node and below the row's level is not beside it. The signal is unmet and FJ-017 fails, so the rerun passes 1 of 7.
