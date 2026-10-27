# Sonnet high rerun grades on v1.0.7.0

These are the grades for the 18 FigJam scenarios Claude Sonnet 5.5 at high effort ran again on `sk-create-figjam` v1.0.7.0 after phase 041: the 13 v1.0.6.0 rerun failures, the gallery FJ-023, the operator scenarios FJ-044 and FJ-045 and the Figma Desktop scenarios FJ-018 and FJ-035. One grader scored every run, so every total sits on one scale. The per-run detail with every signal, cite, loss, location and fix is in `sonnet-high-041.jsonl`.

After the skeptic adjudication folded into the records, the rerun passes 2 of the 16 scenarios it ran: FJ-020 and FJ-044. 14 fail. FJ-018 and FJ-035 are NOT RUN, because they need Figma Desktop and the figma-ds-cli daemon, which this environment does not have.

## How the grades were set

- **Adjudication.** A skeptic challenged the grades of eight scenarios and an adjudicator ruled on each point. Every ruling the skeptic won is folded into `sonnet-high-041.jsonl`, and every count and total below is taken from the folded records.
- **Glance order.** Each board's planned order comes from the gate's glance lines and its first glance from the read-back's `first glance:` clause. The measured order is the fresh reader's section 2 in `grades/sonnet-high-041/readers/`, checked against the render. Composition is 2 when the reader's second glance names the planned second element and nothing planned later reads before its place. It is 1 when one part, planned or not, takes the planned second glance or reads ahead of the first. It is 0 when two planned parts read in reverse.
- **Turn shifts.** An intake round that pushes the playback, the gate and the write one turn later is accepted.
- **Clarity.** FJ-017 and FJ-045 name no reader questions, so their three questions were taken from the request and the model, as the record says.
- **Harness.** FJ-031's operator sticky is the operator's node. FJ-044 was graded from the operator's three step files and the seven renders. FJ-045's design break and restore are the operator's and both held.

## The 18 scenarios

| ID | v1.0.6.0 | v1.0.6.0 total | v1.0.7.0 | v1.0.7.0 total |
|---|---|---|---|---|
| FJ-009 | FAIL | no board | FAIL | no board |
| FJ-017 | FAIL | 20 | FAIL | 19 |
| FJ-018 | NOT RUN | no run | NOT RUN | no run |
| FJ-020 | FAIL | no board | PASS | no board |
| FJ-023 | FAIL (gallery) | 20 | FAIL | 21 |
| FJ-026 | FAIL | 20 | FAIL | 19 |
| FJ-029 | FAIL | 20 | FAIL | 16 |
| FJ-031 | FAIL | 21 | FAIL | 21 |
| FJ-032 | FAIL | 19 | FAIL | 20 |
| FJ-033 | FAIL | 21 | FAIL | 21 |
| FJ-034 | FAIL | 21 | FAIL | 20 |
| FJ-035 | NOT RUN | no run | NOT RUN | no run |
| FJ-036 | FAIL | 21 | FAIL | 21 |
| FJ-038 | FAIL | no board | FAIL | no board |
| FJ-040 | FAIL | no board | FAIL | no board |
| FJ-042 | FAIL | no board | FAIL | no board |
| FJ-044 | NOT RUN | no run | PASS | no scorecard |
| FJ-045 | NOT RUN | no run | FAIL | 21 |

Pass count: 2 of 16 run. Of the 14 scenarios run on both versions, only FJ-020 moved to PASS. FJ-044 passed on its first run, and FJ-045 also ran for the first time.

## Remaining failures

- **FJ-009, model slip.** The playback now comes first and nothing was written. The reply to the gate's yes names the missing hosted Figma MCP but not the fj limit, which only the gate states.
- **FJ-017, model slip and skill gap.** 19 with Composition at 0: Pending reads before the two notes planned second. Turn 3 called use_figma three times, the third an ungated move of both stickies. 'Set by the hotel' stands in a second column at the board's right edge, 560 px from No-show, where the single sticky rule has no free side to offer. The gate now arrives in turn 2.
- **FJ-023, model slip and skill gap.** 21 with Composition at 1. The claims table is back, so 8 of 8 nodes, but the green Refund released goal, left out of the plan, reads before Damage clear? planned second. The run copied that plan from the shipped `assets/examples/process-fernhouse-refund.md`, which contradicts `quality-rubric.md` Section 3.
- **FJ-026, model slip.** 19 with Composition at 0. The focus line on Cancelled works, but the plan put Completed and No-show second where `references/types/state.md` Section 5 puts the Confirmed section and Pending, and both read ahead of their place.
- **FJ-029, model slip and skill gap.** The flow is now split into 1. Sign up and 2. Workspace setup 400 px apart. 16 with Composition and Reply at 0: the goal Email verified, planned last, reads before the error step planned second, and no `Left out:` line names the split, which `flow-mode.md` lines 157 and 320 require. Clarity is 1 because no reader answers Q3 and Legibility is 1 for two orphan wraps. The titles read '1. Sign up' where the scenario expects '1. Signup', a spelling the skill gives both ways.
- **FJ-031, model slip and skill gap.** 21 with Composition at 1. The compose, read-back, named delete question and delete all held and the sticky stayed put. The gate planned the changed end Request an exception last where `quality-rubric.md` Section 3 makes it the second glance. The old and new boards carry the same tag key, so the delete found the old one by its returned id.
- **FJ-032, model slip and skill gap.** 20 with Reply at 1 for a status sentence above the URL. Composition is 1 because Pending reads before the Confirmed section the state rule plans first.
- **FJ-033, model slip and skill gap.** 21 with Composition at 1: the unplanned green app pills share the planned second glance with the Change store. The dial words are now named, but the source line reads 'Entry point added for the layout' instead of marking the gateway assumed, and the reader took Entry point for a drawing aid. The shipped `assets/examples/architecture-loomlist-sync.md` names no gateway in its glance lines either.
- **FJ-034, model slip.** 20 with Reply at 0. The colour rule, the lanes and the one accent held, but the reply has no `Left out:` line for the cuts turn 1 promised to name.
- **FJ-036, model slip.** 21 with Composition at 1. The reply now opens on the URL, but the start and goal nodes, left out of the plan, read before the price exits planned second.
- **FJ-038, model slip.** The hand edits, the node and the recompose on a yes are named, but the delete's second yes is never said to come after the new board's read-back.
- **FJ-040, skill gap.** Turn 1 now carries one recommended scope inside the type question and only that scope is modelled. The gate names the rest only in its Writes bullets, with no `Left out:` line, which no rule asks a gate to carry.
- **FJ-042, model slip.** Nothing was written and the gate waits, but the damage-report entry and the generic return path, assumed in the playback, reach the turn 2 model unmarked.
- **FJ-045, model slip and skill gap.** 21 with Composition at 1: the blue Order list, named in no glance line, reads before the planned second glance. Every DESIGN line has its own `Finding:` above the self-scan. The accent went to the 30-day decision, a choice the rubric allows, so the goal is not under the pink outline and is not the first glance as the scenario expects.

## The v1.0.7.0 fixes

- **Composition for a named group.** FJ-026 put the focus line on Cancelled and the reader read it right after the Confirmed section. The fix works. The board failed on the rest of its plan.
- **Revision second glance and Signal.** FJ-031 kept the accent on the goal and Signal scores 2 under the new clause. The Composition clause applied too and cost the board its point, because the gate planned the changed end last instead of second.
- **Fidelity against the run's own model.** Applied on every board. No board lost a Fidelity point.
- **Paired re-save under Hygiene.** Not exercised, because no paired scenario ran.
- **FJ-020 second turn.** Worked: the second reply asked only board facts and wrote nothing.

## Skill gaps the rerun still shows, most important first

1. **Glance plans against what the composer draws.** Composition is below full marks on 9 of the 14 failures. Most are model slips against `references/quality-rubric.md` Section 3, which says to plan a goal second, but two gaps sit in the skill. `references/types/state.md` Section 5 plans the composite first when no state is named, and the FJ-032 reader read the saturated first state first. The rubric names the goal, final state, gateway, error and critical bar as reading right after the accent but not the light blue entry kind, and the FJ-036 and FJ-045 readers read the start early. The shipped example `assets/examples/process-fernhouse-refund.md` plans the decision second and leaves the goal out, and FJ-023 copied it. `assets/examples/architecture-loomlist-sync.md` never names its gateway and `assets/examples/user-flow-fernhouse-return.md` never names its light blue entry, and FJ-033, FJ-036 and FJ-045 read those examples.
2. **Single sticky with no free side.** `references/hybrid-workflow.md` A single sticky gives no place when the right holds the node's own end-dot connector and the sides below are taken, as at FJ-017's Cancelled and No-show.
3. **Composer runs closer than 56 px.** On FJ-017 and FJ-026 the check out and missed check-in connectors run about 24 px apart beside the Confirmed section, against the spacing `references/style-guide.md` Section 7 sets for the router. On FJ-017 the two runs never merge, so the adjudicator kept Shared trunks at 2 and left this as a composer finding.
4. **Left out: on a split.** `references/flow-mode.md` lines 157 and 320 name every split in `Left out:`, while `SKILL.md` step 6, `flow-mode.md` line 432 and `assets/flow-templates.md` line 169 tie the line to dropped items. FJ-029 broke the direct rule, and the conflict contributed.
5. **Left out: at the gate.** No rule in `references/flow-mode.md` Sections 2 or 8 asks the gate for a `Left out:` line, while FJ-040 expects one.
6. **Same tag key on a same-title revision.** `references/flow-mode.md` Section 6 keys the tag by title, so on FJ-031 the old and new boards carry one key and the page-wide filter on line 360 matches both. Only the written time differs, and no rule names it as the selector.
7. **Two spellings of the first title.** `references/flow-mode.md` line 434 uses '1. Signup' and `assets/flow-templates.md` line 113 uses '1. Sign up'.
8. **Accent choice against FJ-045.** `references/quality-rubric.md` Section 3 lets a user flow's accent sit on a decision, while FJ-045 expects the goal under the pink outline with a prompt that names no focus.

## What the skeptics and the critic changed

- **FJ-017, total 18 to 19.** Shared trunks goes from 1 to 2, because the two runs 24 px apart never merge, and the Shared trunks loss is dropped. The sticky signal stays unmet with corrected positions: the guest sticky sits 64 px clear of the Cancelled end dot and the hotel sticky stands 560 px from No-show in a second column at the right edge. The reason now says so. Hygiene stays at 4 of 4, the grader's ruling. Verdict stays FAIL.
- **FJ-023, total stays 21.** The Composition loss cause becomes model and skill gap, and a skill gap records that the shipped example `process-fernhouse-refund.md` plans the second glance against `quality-rubric.md` Section 3. Verdict stays FAIL.
- **FJ-029, total 20 to 16.** Reply goes to 0 for the missing `Left out:` line, Clarity to 1 because no reader answers Q3 and Legibility to 1 for two orphan wraps, each with a new loss. The title and start-here signals are now unmet, a miss caused by the '1. Signup' and '1. Sign up' wording conflict, and the reader signal is unmet. The Composition loss now says board 2 breaks its order too. The `Left out:` skill gap is restated as a model slip with a contributing wording conflict, and the title spelling conflict is added. Verdict stays FAIL.
- **FJ-031, total stays 21.** A skill gap records that a same-title revision gives old and new boards the same tag key. The three disputed signals stand as the grader set them. Verdict stays FAIL.
- **FJ-033, total 22 to 21.** The capability-words signal is now met as contested, and the gateway signal is now unmet because the source line reads 'Entry point added for the layout'. The reader signal becomes harness. The completeness critic then applied the Composition rule as FJ-045 had it: the reader names the unplanned app pills with the Change store at the second glance, so Composition goes to 1 and the glance signal is unmet. Verdict stays FAIL.
- **FJ-034, PASS 22 to FAIL 20.** Reply goes to 0 for the missing `Left out:` line, with a Reply loss, so the scorecard signal is unmet and the verdict becomes FAIL. The turn 1 signal stands as graded.
- **FJ-042, PASS to FAIL, no board.** The turn 2 marking signal is now unmet, because the damage-report entry and the generic return path reach the model unmarked. The turn 1 signal stands as graded.
- **FJ-045, total 22 to 21.** Composition goes to 1, with a loss for the blue Order list reading before the planned second glance, so the scorecard signal is unmet. The reason now names the Composition fail. Two signals are added and met: step 3 ends on the playback and step 4 on the gate, with nothing written. Verdict stays FAIL.
- **FJ-017 and FJ-029 loss causes.** The critic set FJ-017's Clarity loss cause to model and skill gap, naming `references/hybrid-workflow.md` A single sticky, and gave FJ-029's composer Legibility loss a composer fix. Totals unchanged.
- **Evidence.** The reader notes, greyscale renders and operator step files now sit in `grades/sonnet-high-041/`, the FJ-032 page render in `renders/`, and every evidence path in the records resolves inside the run folder.
