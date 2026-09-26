# Manual testing playbook run, 2026-09-25, Product Owner, claude-opus-5-5 medium

## 1. Handover status, read this first

**The Project handover failed, and the skill handover passed.**

- **Skill, `SID-001`: PASS.** Both replies name a real export path, print `Verified: read-back succeeded` with a line count and the `HVR self-scan:` line, and the event stream shows a Read of each file after its last write. The task keeps every Turn 2 fact, and the reply names each of its additions
- **Project, `PID-001`: FAIL.** The block, the `Export-equivalent path:` line and the `HVR self-scan:` line are all right, and no reply says a file was saved. But Turn 1 ends: "When you reply, I'll write the task as `export/002 - task-due-today-filter-chip.md`" (`replies/PID-001-turn1.txt` line 44). The operator ruled on 2026-09-25 that a promise to write a file is a file claim, which root line 189 blocks on the Project side

So the other 22 Project rows carry `after_failed_gate` yes. Each scenario ran in its own fresh session, so the handover changed nothing a later scenario could do (root line 175). The doubt is about the Project runtime's habits. Kernel line 101 at the run's commit forbade only claiming that a file was saved, so the promise slipped past the kernel's own wording. Two repairs followed (section 3). `PID-001` failed again in the first remeasure round and passes in the second, on kernel v1.16.0 (section 4), so the Project handover holds on the repaired sources.

---

## 2. Verdict counts

Every count below comes from `results.csv` by this command, run from this folder:

```bash
python3 -c "
import csv,collections as c
r=list(csv.DictReader(open('results.csv')))
for k,v in sorted(c.Counter((x['runtime'],x['result']) for x in r).items()): print(k[0],k[1],v)
print('facts_intact yes',sum(x['facts_intact']=='yes' for x in r),'of',len(r))
print('after_failed_gate yes',sum(x['after_failed_gate']=='yes' for x in r))
d={x['id']:x['result'] for x in r}
print('twin pairs differing',sum(d[k]!=d['P'+k[1:]] for k in d if k[0]=='S'),'of',sum(k[0]=='S' for k in d))
"
```

Output: `project FAIL 15`, `project PASS 8`, `skill FAIL 11`, `skill PASS 12`, `facts_intact yes 38 of 46`, `after_failed_gate yes 22`, `twin pairs differing 4 of 23`.

| Runtime | PASS | FAIL | SKIP | Total |
| --- | ---: | ---: | ---: | ---: |
| Skill (`S`) | 12 | 11 | 0 | 23 |
| Project (`P`) | 8 | 15 | 0 | 23 |

The passes are `SID-001`, `STK-001`, `SBG-001`, `SBG-003`, `SDK-002`, `SDK-003`, `SDK-004`, `SST-001`, `SEP-002`, `SEP-003`, `SIR-001` and `SIR-002` on the skill side, and `PTK-001`, `PBG-001`, `PBG-003`, `PDK-002`, `PDK-004`, `PST-001`, `PEP-003` and `PIR-001` on the Project side.

The 26 failures come from three causes:

- **Drafting on Turn 1 instead of asking, 20 rows.** `STK-002` to `STK-005`, `PTK-002` to `PTK-005`, `SBG-002`, `PBG-002`, `SST-002` to `SST-004`, `PST-002` to `PST-004`, `SEP-001` and `PDK-003` came with an explicit command and rich attachments, and the runtime wrote the artifact at once. Each scenario's Pass clause asks for one question first, as `AGENTS.md` line 287 and kernel line 108 require. The Bug, Story and Doc Mode intake lines let enough context stand in for the question, and `task-mode.md` line 50, which already said `$task` still asks, was misread the same way. `SDK-001` and `PDK-001` carry no command. For them the operator ruled the scenario wrong, since no rule required the question
- **A file promised on the Project side, 4 rows.** `PID-001`, `PIR-002`, `PEP-001` and `PEP-002` each say, in Turn 1, that the next turn will write or save a file (section 1)
- **A status word left out, 2 rows.** `STK-006` and `PTK-006` never mark `checkout_complete` as `deprecated`, which the tracking plan and the Pass clause both state. `PTK-006` also promises a file

Every delivered artifact is recognisably company work. The realism review read every export against its fixtures and found no placeholder content, no wrong artifact word and no company fact contradicted. The value misses are omissions or rewordings, graded through the Pass clauses. Every Story export uses `Story-`, the Story bundle kept its folder on both sides, and the refinement kept its source name. The only realism item that decided a verdict, a missing `#### **References**` in the Project Epics, was ruled optional when no link is supplied, which turned `PEP-003` and `PIR-001` to PASS.

`results.md` has the table of all 46 and the twin table. `grading-notes.md` has the rulings, the report checker output, the twin causes and each grader's evidence.

---

## 3. Findings and decisions

Every finding that could move a verdict went to the operator on 2026-09-25, and each answer is below. Repairs were made only where the operator chose one.

| # | Finding | Decision | Repair |
| --- | --- | --- | --- |
| 1 | An explicit command drafted on Turn 1 whenever the attachments were rich (20 rows) | The command always asks first | Bug, Story and Doc Mode intake lines carry the exception Task Mode had, `$epic` and every short alias join `AGENTS.md` line 287 and kernel line 108, on both sides |
| 2 | The Project Epics left out `#### **References**` with no link supplied | Optional when no link is supplied, as for a Story | Epic template, its mirror, kernel line 140 and the six Epic scenarios |
| 3 | The Project promised a file in `PID-001`, `PIR-002`, `PEP-001`, `PEP-002` and `PTK-006` | A promise is a file claim | Kernel line 101 and root lines 179 and 189 name it |
| 4 | `SDK-001` and `PDK-001` expected a question no rule requires | The scenario is wrong | Both expect a direct draft on Turn 1, and Turn 2 is a follow-up change |
| 5 | `SBG-003` gives one issue a cause labelled as an unverified hypothesis, against "no root cause" | Allowed | Both twins say no cause stated as fact |
| 6 | The skill bugs write "No error message is shown" with no source | Advisory | The bug template's error slot reads `Not provided` or is left out |
| 7 | The runbooks turn incident details into general "Expected result" lines | Allowed | None |

The repairs are Product Owner `39bcd29` and Barter `df2de5f0`: skill 1.11.0, kernel v1.15.0 with seven knowledge files renamed, playbook 2.1.0.0. The format gate, the playbook validator (46 scenarios, 0 violations) and the run selftest passed on the working tree, and `validate_parity.py product-owner` (38 of 38 pairs) and `run_residency.sh product-owner` passed on the commit. The review of kernel v1.15.0 is pending the operator, and the seven renamed files are not on claude.ai until then.

The first remeasure round showed the ask-first repair working on both sides and the file-promise repair failing on the Project side (section 4). The operator chose one more repair, Product Owner `b591571` and Barter `e9eec279`. Kernel line 101 now says the Project never says it saved, verified, read back, pushed, will write, will save or will update a file, and a reply names only the export-equivalent label of the block it renders. It no longer quotes a forbidden example. Kernel line 228 and the Interactive Mode files on both sides say a clarification reply names the artifact as coming next without its path or file, and root lines 179 and 189 count a forecast path as a file claim. That makes skill 1.12.0, kernel v1.16.0, Interactive Mode mirror v0.407 and playbook 2.1.1.0. The review of kernel v1.16.0 is pending the operator as well.

Findings that moved no verdict are in `grading-notes.md` section 4. Among them: `Verified:` lines printed with no Read after the last write, in `SBG-002` Turn 1 and both `STK-003` turns. And `N` is printed as `wc -l` in seven turns, where `AGENTS.md` line 46 names the Read's final line number, one more.

---

## 4. Remeasure rounds

The main run's 46 rows in `results.csv` stay the verdicts of record for playbook 2.0.0.0 at `3023c5e`. Two rounds then reran a subset on the repaired sources, to see whether each repair changes what the runtimes do. Each round keeps its own `results.csv` and `grading-notes.md` under `remeasure-*/run-1/`, and its deliverables sit in `export/benchmark/<side>/<round>/run-1/`.

| Round | Sources | Scenarios | Skill | Project | Cost |
| --- | --- | --- | --- | --- | ---: |
| `remeasure-operator-repairs/run-1` | Product Owner `39bcd29`, Barter `df2de5f0`: skill 1.11.0, kernel v1.15.0, playbook 2.1.0.0 | 26: both twins of `TK-002` to `TK-005`, `BG-002`, `DK-001`, `DK-003`, `ST-002` to `ST-004` and `EP-001`, plus `PID-001`, `PEP-002`, `PTK-006` and `PIR-002` | 7 PASS, 4 FAIL | 3 PASS, 12 FAIL | USD 37.36 |
| `remeasure-file-forecast/run-1` | Product Owner `b591571`, Barter `e9eec279`: skill 1.12.0, kernel v1.16.0, playbook 2.1.1.0 | 8 Project: `PID-001`, `PBG-002`, `PTK-005`, `PTK-006`, `PST-003`, `PST-004`, `PEP-001` and `PEP-002` | Not run | 5 PASS, 3 FAIL | USD 10.38 |

**Round one: the ask-first repair worked.** Every scenario with an explicit command now asks one question in its lane on Turn 1 and drafts on Turn 2 on the next number. `TK-002` and `TK-004` on both sides, `SBG-002`, `SST-003`, `SST-004`, `SEP-001` and `PIR-002` pass where the main run failed them.

**Round one: the file-promise repair did not hold on the Project side.** Eight Project rows still named a path or a file for the artifact still to come, several in nearly the words of the example kernel line 101 then quoted as forbidden. `PID-001` failed again ("Once you answer, the task will be `export/002 - task-due-today-filter-chip.md`"), so the other 14 Project rows of that round carry `after_failed_gate` yes. The operator chose one more repair (section 3).

**Round two: the handover passes.** None of the eight replies attaches an `export/` path to the next artifact. `PID-001`, `PBG-002`, `PTK-005`, `PEP-001` and `PEP-002` pass, and no row of the round carries `after_failed_gate` yes. Three still fail:

- **`PST-003`**, on the operator's ruling. Turn 1 says "I'll keep the draft's original filename", graded a file claim. The Project's own naming rules give a refinement the source's file name as its label (kernel line 229), so the sentence may only restate that convention. Every other clause is met. The operator ruled on 2026-09-26 that it is a claim
- **`PST-004`**. Turn 1 settles the six-task split from the brief instead of asking for it, which Story Mode knowledge line 382 requires, and Turn 2 then follows the four named tasks
- **`PTK-006`**. The task still never marks `checkout_complete` as `deprecated`, and no longer names `booking-service`

**Still failing on content after round one.** These rows fail on a value, not on the repaired rules, and were not rerun in round two:

| Rows | Miss |
| --- | --- |
| `STK-003`, `PTK-003` | None of `HMAC-SHA256`, `5 attempts` or `1 min, 5 min, 15 min, 1 h, 6 h`, and the Fulfilment board left out of the task |
| `STK-005` | `1 to 99` restated as "below 1 or above 99" |
| `SDK-001` | The mandatory body named `## Stacking rules` instead of `## Behavior rules` |
| `PDK-001` | `one discount code per order` written as "One code per order" |
| `PDK-003` | `block-level last-writer-wins` written as "last-writer-wins at the block level" |
| `SST-002`, `PST-002` | The open question `Do sub-pages inherit the link?` reworded |

Backticked Pass-clause values are graded word for word in every round, as in the main run.

| Measure | Round one | Round two |
| --- | --- | --- |
| Claude Code | `2.1.283` | `2.1.283` |
| Turns | 52, skill 22 and Project 30 | 16, all Project |
| Turn time | 3,634 s | 993 s |
| Models in the streams | `claude-opus-5-5` only | `claude-opus-5-5` only |
| Scenarios `ok` on the first attempt | 26 of 26 | 8 of 8 |
| Collected | 59 files: skill 25, Project 34 | 20 Project files |

Each round ran from this folder as `python3 run/playbook_runner.py --system ../../.. --out <round>/run-1 --engine claude --model claude-opus-5-5 --effort medium --jobs 4 --ids <ids>`. `run/check_run.py <round>/run-1 --model claude-opus-5-5` reports no finding for any scenario the round ran. Its only findings name the scenarios the round left out, as "no readable meta.json". `run/collect_exports.py . ../../../export/benchmark` filed each round under its own folder, and `export/benchmark/` now holds 177 files: 98 from the main run and 79 from the two rounds.

---

## 5. Next steps

- **Kernel review and deployment.** The operator's kernel review has been pending since v1.13.0, and the text to review is now v1.16.0. It is recorded as a dated note in `SYNC.md` only once confirmed. The renamed knowledge files reach claude.ai only after that, with a deployment receipt and a smoke check
- **`PST-004`.** Story Mode says a split the request does not name is asked for, in the skill at `references/story-mode.md` line 406 and in the Project at knowledge line 382. The skill twin asked in round one, and the Project read the brief's six tasks as the split in both rounds. It is recorded as a runtime fault, and no repair is proposed
- **Content misses.** The rows in the table above miss a value the rules already protect. No repair is proposed, and a future run shows whether they recur

---

## Run record

### Sources and harness

| Item | Value |
| --- | --- |
| Playbook | Version 2.0.0.0, 46 scenarios, 23 skill and 23 Project, each twinned, 86 turns |
| Product Owner repo | `3023c5ecbdd418e41cdc0a1454dad6826becc2c0`, sources clean before and after the run |
| Barter repo | `c15c05e947a063b7fa831d9c7d31002156ef8b6f`, the same before and after |
| Operator approval | The scenario plan was approved on 2026-09-25 at 19:31 UTC, before any scenario ran |
| Claude Code | `2.1.282` |
| Engine, model, effort | `claude`, `claude-opus-5-5`, `medium` (`manifest.json`) |
| Parallel sessions | `--jobs 4` |
| `run/playbook_runner.py` | sha256 `868cad2739c77675c4fb829e927a4a719503d12de29e83d1b38d1087fff4ed92` |
| `run/collect_exports.py` | sha256 `34427b7cc79d7af97068c3a444b1b01a5199dd4d18926e60e76ff83cea20c737` |
| `run/check_run.py` | sha256 `4bc16f13ef663f05e0a0266388815747ce73b79741b75f6f85b300baab527faa` |
| `run/selftest.py` | sha256 `5e79b00f41c0b52ce4572a197aae8a934c7ed1511b6f0f696c3000700dd503cb` |

Command, from this folder:

```bash
python3 run/playbook_runner.py --system ../../.. --out . --engine claude --model claude-opus-5-5 --effort medium --jobs 4
```

### Smoke run

`SID-001` and `PID-001` ran first on their own, outside this folder, with `--jobs 2`. Both finished on their first attempt with 2 of 2 turns, and every assistant event in their four streams names `claude-opus-5-5` alone, so `check_run.py` kept its single expected model and no allowed-model option was added.

### The run

| Measure | Value |
| --- | --- |
| Event time | 19:35:44 UTC to 20:06:05 UTC, about 30 minutes |
| Runner exit | 0 |
| Scenarios | 46 of 46 `ok` on the first attempt, 0 retried, 0 failed attempts |
| Turns | 86 of 86 run: 40 scenarios at 2 of 2 and 6 at 1 of 1 (`run-status.json`) |
| Models in the streams | `claude-opus-5-5` only, in all 86 |
| Cost | USD 71.36: skill 40.18 over 43 turns, Project 31.19 over 43 turns |
| Turn time | 6,744 s in all: skill 3,768 s, Project 2,977 s |
| Longest turns | `STK-004` Turn 1, 352 s. `SST-004` Turn 1, 334 s. `PST-004` Turn 1, 213 s |
| Run defects | None |

`python3 run/check_run.py . --model claude-opus-5-5` exits 0: `46 scenarios, 86 declared turns, 86 event streams read, 0 finding(s), expected claude claude-opus-5-5 at effort medium`.

The smoke estimate was USD 49 and 13 minutes, and it said it was a floor. The run cost 46% more and took more than twice as long. The handover turns are short, while the bundle, parent task and long task turns read three attachments and write several files.

### Collection

`python3 run/collect_exports.py . ../../../export/benchmark` collected 98 files into `AI Systems/Product Owner/export/benchmark/`, which held 0 files before. That's the same 98 lines as the dry run, with no warning about a changed attachment.

| Side | Files | How each was checked |
| --- | ---: | --- |
| Skill | 41 | Byte-identical to the file the runtime wrote under `skill/<ID> - <slug>/exports/export/` |
| Project | 57 | Each block's text found verbatim in its `replies/<ID>-turn<n>.txt` |

Each Story bundle kept its folder: `skill/SST-004 - 001 - Story-order-tracking/` and `claude project/PST-004 - NNN - Story-order-tracking-timeline/`. The refinement kept its source name on both sides, `fernhouse-save-card-draft.md`. The Project folder holds the blocks of both `PST-004` turns, since both turns rendered blocks under the same folder name.

### What is tracked

Tracked here: this README, `results.csv`, `results.md`, `grading-notes.md`, `hvr-lint.csv`, `manifest.json`, `run-status.json`, `replies/`, each scenario's `meta.json` and `turn-<n>.md`, and `run/`. Each `remeasure-*/run-1/` folder is tracked the same way, with its own `results.csv` and `grading-notes.md`. Kept local by `.gitignore`: the event streams and `run-log.jsonl`, stderr, transcripts, the progress file and each scenario's `exports/` copy. The deliverables themselves are tracked in `export/benchmark/`.

### Project extraction review

Each collected Project file set beside its reply: the file's text is found verbatim in the reply named here, as the block that reply rendered.

| Collected file | Found in |
| --- | --- |
| `PBG-001 - NNN - bug-ios-cart-badge-stale-after-remove.md` | `replies/PBG-001-turn1.txt` |
| `PBG-002 - NNN - bug-android-confirmation-total-missing-city-tax (turn 2).md` | `replies/PBG-002-turn2.txt` |
| `PBG-002 - NNN - bug-android-confirmation-total-missing-city-tax.md` | `replies/PBG-002-turn1.txt` |
| `PBG-003 - 001 - bug-reminders-late-after-march-clock-change-clarification.md` | `replies/PBG-003-turn1.txt` |
| `PBG-003 - 002 - bug-reminders-late-after-march-clock-change.md` | `replies/PBG-003-turn2.txt` |
| `PDK-001 - 001 - doc-promotions-stacking (turn 2).md` | `replies/PDK-001-turn2.txt` |
| `PDK-001 - 001 - doc-promotions-stacking.md` | `replies/PDK-001-turn1.txt` |
| `PDK-002 - 001 - doc-payment-webhook-failures-clarification.md` | `replies/PDK-002-turn1.txt` |
| `PDK-002 - 002 - doc-payment-webhook-failures-runbook.md` | `replies/PDK-002-turn2.txt` |
| `PDK-003 - 001 - doc-sync-conflicts-lost-edits-status.md` | `replies/PDK-003-turn1.txt` |
| `PDK-003 - 002 - doc-sync-conflict-options-proposal.md` | `replies/PDK-003-turn2.txt` |
| `PDK-004 - 001 - doc-loomlist-activity-emails-clarification.md` | `replies/PDK-004-turn1.txt` |
| `PDK-004 - 002 - doc-loomlist-activity-emails.md` | `replies/PDK-004-turn2.txt` |
| `PEP-001 - 001 - Epic-partner-hub-self-onboarding-clarification.md` | `replies/PEP-001-turn1.txt` |
| `PEP-001 - 002 - Epic-partner-hub-self-onboarding.md` | `replies/PEP-001-turn2.txt` |
| `PEP-002 - 001 - Epic-offline-mode-clarification.md` | `replies/PEP-002-turn1.txt` |
| `PEP-002 - 002 - Epic-offline-mode.md` | `replies/PEP-002-turn2.txt` |
| `PEP-003 - 001 - Epic-self-serve-returns.md` | `replies/PEP-003-turn1.txt` |
| `PID-001 - 001 - task-due-today-filter-chip-clarification.md` | `replies/PID-001-turn1.txt` |
| `PID-001 - 002 - task-due-today-filter-chip.md` | `replies/PID-001-turn2.txt` |
| `PIR-001 - 001 - intake-guest-loyalty-points-clarification.md` | `replies/PIR-001-turn1.txt` |
| `PIR-001 - 002 - Epic-guest-loyalty-points.md` | `replies/PIR-001-turn2.txt` |
| `PIR-002 - 001 - intake-wishlist-across-devices-clarification.md` | `replies/PIR-002-turn1.txt` |
| `PIR-002 - 002 - Story-customer-wishlist-account-wishlist-in-apps.md` | `replies/PIR-002-turn2.txt` |
| `PST-001 - NNN - Story-free-cancellation-filter-clarification.md` | `replies/PST-001-turn1.txt` |
| `PST-001 - NNN - Story-free-cancellation-filter.md` | `replies/PST-001-turn2.txt` |
| `PST-002 - NNN - Story-member-sharing-view-only-links (turn 2).md` | `replies/PST-002-turn2.txt` |
| `PST-002 - NNN - Story-member-sharing-view-only-links.md` | `replies/PST-002-turn1.txt` |
| `PST-003 - fernhouse-save-card-draft (turn 2).md` | `replies/PST-003-turn2.txt` |
| `PST-003 - fernhouse-save-card-draft.md` | `replies/PST-003-turn1.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN - Story-order-tracking-timeline (turn 2).md` | `replies/PST-004-turn2.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN - Story-order-tracking-timeline.md` | `replies/PST-004-turn1.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN.1 - task-ios-tracking-timeline.md` | `replies/PST-004-turn2.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN.1 - task-tracking-webhook.md` | `replies/PST-004-turn1.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN.2 - task-android-tracking-timeline.md` | `replies/PST-004-turn2.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN.2 - task-packed-status.md` | `replies/PST-004-turn1.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN.3 - task-web-tracking-timeline (turn 2).md` | `replies/PST-004-turn2.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN.3 - task-web-tracking-timeline.md` | `replies/PST-004-turn1.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN.4 - task-ios-tracking-timeline.md` | `replies/PST-004-turn1.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN.4 - task-tracking-webhook.md` | `replies/PST-004-turn2.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN.5 - task-android-tracking-timeline.md` | `replies/PST-004-turn1.txt` |
| `PST-004 - NNN - Story-order-tracking-timeline/NNN.6 - task-tracking-timeline-events.md` | `replies/PST-004-turn1.txt` |
| `PTK-001 - NNN - task-free-shipping-banner-copy.md` | `replies/PTK-001-turn1.txt` |
| `PTK-002 - 001 - task-date-picker-stay-limits (turn 2).md` | `replies/PTK-002-turn2.txt` |
| `PTK-002 - 001 - task-date-picker-stay-limits.md` | `replies/PTK-002-turn1.txt` |
| `PTK-003 - 001 - task-label-webhook-duplicates-and-late-labels (turn 2).md` | `replies/PTK-003-turn2.txt` |
| `PTK-003 - 001 - task-label-webhook-duplicates-and-late-labels.md` | `replies/PTK-003-turn1.txt` |
| `PTK-004 - NNN - task-recurring-todos (turn 2).md` | `replies/PTK-004-turn2.txt` |
| `PTK-004 - NNN - task-recurring-todos-android.md` | `replies/PTK-004-turn1.txt` |
| `PTK-004 - NNN - task-recurring-todos-be.md` | `replies/PTK-004-turn1.txt` |
| `PTK-004 - NNN - task-recurring-todos-ios.md` | `replies/PTK-004-turn1.txt` |
| `PTK-004 - NNN - task-recurring-todos-web.md` | `replies/PTK-004-turn1.txt` |
| `PTK-004 - NNN - task-recurring-todos.md` | `replies/PTK-004-turn1.txt` |
| `PTK-005 - NNN - task-android-recurring-todos (turn 2).md` | `replies/PTK-005-turn2.txt` |
| `PTK-005 - NNN - task-android-recurring-todos.md` | `replies/PTK-005-turn1.txt` |
| `PTK-006 - 001 - task-booking-funnel-events-clarification.md` | `replies/PTK-006-turn1.txt` |
| `PTK-006 - 002 - task-booking-funnel-event-checks.md` | `replies/PTK-006-turn2.txt` |
