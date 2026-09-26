# Manual testing playbook run, 2026-09-25, Product Owner, claude-opus-5-5 medium

## 1. Handover status, read this first

**The skill handover passed, and the Project handover failed.**

- **Skill `SID-001`, PASS:** both replies give a real export path, a `Verified: read-back succeeded` line with a count, and the `HVR self-scan:` line
- The event stream shows a Read of each file after its last write, and the task keeps every Turn 2 fact and names its additions
- **Project `PID-001`, FAIL:** the block, the `Export-equivalent path:` line and the `HVR self-scan:` line are right, and no reply claims a save
- But Turn 1 ends "When you reply, I'll write the task as `export/002 - task-due-today-filter-chip.md`" (`replies/PID-001-turn1.txt` line 44)
- The operator ruled on 2026-09-25 that a promise to write a file is a file claim, which root line 189 blocks on the Project side

So the other 22 Project rows carry `after_failed_gate` yes. Each scenario ran in its own fresh session, so the handover changed nothing a later scenario could do (root line 175).

Kernel line 101 at the run's commit forbade only claiming a save, so the promise slipped past it. Two repairs followed (section 3). `PID-001` failed again in round one and passed in round two on kernel v1.16.0, so the handover holds on the repaired sources (section 4).

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

| Cause | Rows | Scenarios | Why |
| --- | ---: | --- | --- |
| Drafted on Turn 1 instead of asking | 20 | `STK-002` to `STK-005`, `PTK-002` to `PTK-005`, `SBG-002`, `PBG-002`, `SST-002` to `SST-004`, `PST-002` to `PST-004`, `SEP-001`, `PDK-003`, `SDK-001`, `PDK-001` | An explicit command with rich attachments drafted at once. The Pass clause asks one question first, as `AGENTS.md` line 287 and kernel line 108 require |
| A file promised on the Project side | 4 | `PID-001`, `PIR-002`, `PEP-001`, `PEP-002` | Turn 1 says the next turn will write or save a file (section 1) |
| A status word left out | 2 | `STK-006`, `PTK-006` | Neither marks `checkout_complete` as `deprecated`, as the tracking plan and the Pass clause state. `PTK-006` also promises a file |

The Bug, Story and Doc Mode intake lines let enough context stand in for the question, and `task-mode.md` line 50 was misread the same way, though it already said `$task` still asks. `SDK-001` and `PDK-001` carry no command, and the operator ruled those two scenarios wrong because no rule required the question.

Every delivered artifact reads as real company work. The realism review read each export against its fixtures and found no placeholder content, no wrong artifact word and no contradicted company fact. The value misses are omissions or rewordings, graded through the Pass clauses.

Every Story export uses `Story-`, the Story bundle kept its folder on both sides, and the refinement kept its source name. One realism item decided verdicts: the Project Epics left out `#### **References**`, ruled optional when no link is supplied. That turned `PEP-003` and `PIR-001` to PASS.

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

The repairs are Product Owner `39bcd29` and Barter `df2de5f0`: skill 1.11.0, kernel v1.15.0 with seven knowledge files renamed, and playbook 2.1.0.0. The format gate, the playbook validator (46 scenarios, 0 violations) and the run selftest passed on the working tree.

`validate_parity.py product-owner` (38 of 38 pairs) and `run_residency.sh product-owner` passed on the commit. The kernel v1.15.0 review is pending the operator, and the seven renamed files are not on claude.ai until then.

Round one showed the ask-first repair working on both sides and the file-promise repair failing on the Project side (section 4). The operator chose one more repair, Product Owner `b591571` and Barter `e9eec279`:

- Kernel line 101: the Project never says it saved, verified, read back, pushed, will write, will save or will update a file
- A reply names only the export-equivalent label of the block it renders, and line 101 no longer quotes a forbidden example
- Kernel line 228 and the Interactive Mode files on both sides say a clarification reply names the next artifact without its path or file
- Root lines 179 and 189 count a forecast path as a file claim

That makes skill 1.12.0, kernel v1.16.0, Interactive Mode mirror v0.407 and playbook 2.1.1.0. The kernel v1.16.0 review is pending the operator as well.

Rows that still dropped or reworded a supplied value after round one went to a read-only investigation. One Opus 5.5 investigator per group traced each miss to its source, the rules for and against it, and one cause class. It found these causes:

- Task Mode had no rule that a supplied value travels into a task unchanged, since every such rule was written for a Story
- Doc Templates never protected the Behavior reference heading or a backticked rule phrase
- Story Mode told the runtime to rewrite source prose, with no exception for an open question
- Five misses failed only under the unstated convention that every backticked Pass-clause value is graded word for word

On 2026-09-26 the operator chose four changes:

- The root grades a backticked value word for word only where the source backticks it, defines it as a label, or the clause says verbatim
- Task Mode carries a supplied value, name or status word as the source writes it
- Doc Templates keep `## Behavior rules` and a backticked source phrase word for word, and Story Mode quotes an open question the source words itself
- The long integration task no longer demands the carrier's retry count and schedule word for word

That is Product Owner `b50f0a0` and Barter `7396d79e`: skill 1.13.0, Task Mode v0.306, Doc Templates v0.108, Story Mode v0.404 and playbook 2.2.0.0. The kernel stayed at v1.16.0, since every new rule lives in a document it already routes to. Every edit stayed on its own line, so no line a scenario cites moved.

Findings that moved no verdict are in `grading-notes.md` section 4. Two examples: `Verified:` lines with no Read after the last write in `SBG-002` Turn 1 and both `STK-003` turns, and `N` printed as `wc -l` in seven turns, one lower than the Read's final line number `AGENTS.md` line 46 names.

---

## 4. Remeasure rounds

The main run's 46 rows in `results.csv` stay the verdicts of record for playbook 2.0.0.0 at `3023c5e`. Three rounds then reran a subset on the repaired sources, to see whether each repair changes what the runtimes do. Each round keeps its own `results.csv`, `grading-notes.md` and `replies/` under `remeasure-*/run-1/`.

| Round | Sources | Scenarios | Skill | Project | Cost |
| --- | --- | --- | --- | --- | ---: |
| `remeasure-operator-repairs/run-1` | Product Owner `39bcd29`, Barter `df2de5f0`: skill 1.11.0, kernel v1.15.0, playbook 2.1.0.0 | 26: both twins of `TK-002` to `TK-005`, `BG-002`, `DK-001`, `DK-003`, `ST-002` to `ST-004` and `EP-001`, plus `PID-001`, `PEP-002`, `PTK-006` and `PIR-002` | 7 PASS, 4 FAIL | 3 PASS, 12 FAIL | USD 37.36 |
| `remeasure-file-forecast/run-1` | Product Owner `b591571`, Barter `e9eec279`: skill 1.12.0, kernel v1.16.0, playbook 2.1.1.0 | 8 Project: `PID-001`, `PBG-002`, `PTK-005`, `PTK-006`, `PST-003`, `PST-004`, `PEP-001` and `PEP-002` | Not run | 5 PASS, 3 FAIL | USD 10.38 |
| `remeasure-supplied-values/run-1` | Product Owner `b50f0a0`, Barter `7396d79e`: skill 1.13.0, kernel v1.16.0, playbook 2.2.0.0 | 12: both twins of `TK-003`, `TK-005`, `TK-006`, `DK-001`, `DK-003` and `ST-002` | 6 PASS, 0 FAIL | 6 PASS, 0 FAIL | USD 18.90 |

**Round one: the ask-first repair worked.** Every scenario with an explicit command now asks one question in its lane on Turn 1 and drafts on Turn 2 on the next number. `TK-002` and `TK-004` on both sides, `SBG-002`, `SST-003`, `SST-004`, `SEP-001` and `PIR-002` pass where the main run failed them.

**Round one: the file-promise repair did not hold on the Project side.** Eight Project rows still named a path or file for the next artifact, several echoing the forbidden example kernel line 101 then quoted. `PID-001` failed again ("Once you answer, the task will be `export/002 - task-due-today-filter-chip.md`"), so the round's other 14 Project rows carry `after_failed_gate` yes.

**Round two: the handover passes.** No reply attaches an `export/` path to the next artifact, and `PID-001`, `PBG-002`, `PTK-005`, `PEP-001` and `PEP-002` pass with no row carrying `after_failed_gate` yes.

Three still fail:

| Row | Why it still fails |
| --- | --- |
| `PST-003` | Turn 1 says "I'll keep the draft's original filename". The operator ruled on 2026-09-26 that this is a file claim, though kernel line 229 gives a refinement the source's file name as its label. Every other clause is met |
| `PST-004` | Turn 1 settles the six-task split from the brief instead of asking for it, as Story Mode knowledge line 382 requires. Turn 2 then follows the four named tasks |
| `PTK-006` | The task still never marks `checkout_complete` as `deprecated`, and no longer names `booking-service` |

**Still failing on content after round one.** These rows failed on a value, not on the repaired rules, and were not rerun in round two:

| Rows | Miss |
| --- | --- |
| `STK-003`, `PTK-003` | None of `HMAC-SHA256`, `5 attempts` or `1 min, 5 min, 15 min, 1 h, 6 h`, and the Fulfilment board left out of the task |
| `STK-005` | `1 to 99` restated as "below 1 or above 99" |
| `SDK-001` | The mandatory body named `## Stacking rules` instead of `## Behavior rules` |
| `PDK-001` | `one discount code per order` written as "One code per order" |
| `PDK-003` | `block-level last-writer-wins` written as "last-writer-wins at the block level" |
| `SST-002`, `PST-002` | The open question `Do sub-pages inherit the link?` reworded |

Rounds one and two graded every backticked Pass-clause value word for word, as the main run did. Round three grades by root line 150 as it now stands (section 3).

**Round three: the content repair held.** All 12 rows pass on both sides, and every value above is present:

- `HMAC-SHA256` in the signature check and `99` in the Custom range
- `checkout_complete` marked `deprecated` beside its removal, `date_changed` kept `proposed`, and `booking-service` as the sender
- `## Behavior rules` as the Behavior reference body, and `one discount code per order` in the sentence stating the rule
- Block-level last-writer-wins as today's state, and `Do sub-pages inherit the link?` quoted in the `**Open:**` line

`remeasure-supplied-values/run-1/grading-notes.md` section 1 cites each on both sides.

One reading decides a verdict: `PDK-003` states `not decided` in other words. The thread's pinned `Status: not decided` is neither backticked nor a status-key word, so other words meet the clause. The operator ruled so on 2026-09-26, and the row stays PASS.

| Measure | Round one | Round two | Round three |
| --- | --- | --- | --- |
| Claude Code | `2.1.283` | `2.1.283` | `2.1.283` |
| Turns | 52, skill 22 and Project 30 | 16, all Project | 24, skill 12 and Project 12 |
| Turn time | 3,634 s | 993 s | 1,660 s |
| Models in the streams | `claude-opus-5-5` only | `claude-opus-5-5` only | `claude-opus-5-5` only |
| Scenarios `ok` on the first attempt | 26 of 26 | 8 of 8 | 12 of 12 |
| Collected | 59 files: skill 25, Project 34 | 20 Project files | 23 files: skill 11, Project 12 |

Each round ran from this folder as `python3 run/playbook_runner.py --system ../../.. --out <round>/run-1 --engine claude --model claude-opus-5-5 --effort medium --jobs 4 --ids <ids>`. `run/check_run.py <round>/run-1 --model claude-opus-5-5` reports findings only for the scenarios the round left out, as "no readable meta.json".

The collector filed the rounds' 102 deliverables under their own folders in `export/benchmark/`. The operator removed them on 2026-09-26, and then the main run's 20 clarifications, so `export/benchmark/` holds the main run's 78 deliverables. Each round's evidence stays in its `replies/` and `results.csv`, and its exports in git history at Product Owner `3fdce37` and Barter `d214c160`.

---

## 5. Next steps

- **Kernel review:** the operator confirmed v1.17.0 on 2026-09-26, and v1.18.0, which adds the word budget, awaits review
- **Deployment:** the renamed knowledge files and kernel v1.18.0 reach claude.ai only with a deployment receipt and a smoke check
- **`PST-004`:** the skill twin asked for the split, as Story Mode requires at `references/story-mode.md` line 406 and Project knowledge line 382
- The Project took the brief's six tasks as the split in both rounds, recorded as a runtime fault with no repair proposed
- **Length caps and word budget:** the rules gained both on 2026-09-26 without a rerun, so no run has measured whether the runtimes follow them

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
| Skill | 41 | Byte-identical at collection to the file the runtime wrote under `skill/<ID> - <slug>/exports/export/` |
| Project | 57 | At collection, each block's text was found verbatim in its `replies/<ID>-turn<n>.txt` |

Each Story bundle kept its folder: `skill/SST-004 - 001 - Story-order-tracking/` and `claude project/PST-004 - NNN - Story-order-tracking-timeline/`. The refinement kept its source name on both sides, `fernhouse-save-card-draft.md`. The Project folder holds the blocks of both `PST-004` turns, since both turns rendered blocks under the same folder name.

### Edited after grading

On 2026-09-26 the operator had the exports edited by hand to the new length caps, after grading. Every verdict and every export line a grader cites refers to the graded originals, not to the edited files. The originals are in git history at Product Owner `e9edb95` and Barter `7652158c`, and each Project block is also in its `replies/` file.

Five Opus 5.5 agents edited 80 of the 98 files and left the other 18 unchanged. A script checked each file against its graded snapshot: headings, labels, Given/When/Then lines, tables, backticked values, numbers and links unchanged, no new em dash or nested list, the caps met and the format gate passing.

Three readers then compared every changed hunk for a dropped, changed or added fact. They found seven, all repaired: four hedges or conditions stated flatly, one added claim, one dropped qualifier and one dropped attribution.

Over-cap lines fell from 623 in 78 files to 7 in 7 files, and words from 82,830 to 81,502. The 7 are task About openings kept past two paragraphs, since cutting them would drop a fact the body does not repeat.

No scenario reran, so the caps are unmeasured on the runtimes. `run/collect_exports.py` now keeps an edited export unless `--force` is given and collects rounds only with `--rounds`. That version's sha256 was `161169269678cc0e0dac2c725722713c6c3aa6c923663c36f500d52451790e5f`, with `run/selftest.py` at `f657ab6f2092f53813b90e4637105160a1cf1d3de64a754d08f022a0323fbd8c`.

### Clarifications removed

On 2026-09-26 the operator removed the 20 clarification files from `export/benchmark/`, 10 skill and 10 Project, and every git-ignored local copy under `exports/`. A clarification is the question a scenario asked before drafting, not a deliverable. `export/benchmark/` now holds 78 files, 31 skill and 47 Project, and the counts above describe all 98 as collected and edited.

The questions stay in the evidence. Each Project one is in its `replies/<ID>-turn1.txt`, and each skill one is summarized in its `turn-1.md` and quoted in its git-ignored transcript. All 20 are in git history at Product Owner `1fc3657` and Barter `e324ecdf` as edited, and at `e9edb95` and `7652158c` as graded.

`run/collect_exports.py` now skips any file named `*-clarification.md` and prints a skip line for it, so a new collection cannot put one back. A dry run over this folder prints 20 skip lines and writes no clarification. Its sha256 is now `7d06baa5023c7cbf849581573888bc5d9ee61c792f6627dec3da5634a5f6f213`, and `run/selftest.py` is `10608ab9ff3bd9fdab3c7efb5ebe2e2e61cb5c6a1d17507f895d5e5805866ad6`.

### Second edit

Later on 2026-09-26 the operator found the exports still long, since the first edit split lines and cut 1.6% of the words. Seven Opus 5.5 agents cut the 78 files again in two rounds. Words outside code fell from 73,942 to 57,138, or 22.7%.

A script held every heading, label, template line, table header, backticked value, number and link. Seven fact reviewers then read each file against its snapshot. They found 81 lost or changed facts: 75 were restored, and 6 were color or a subtask restating its parent, which the operator's chosen depth allows.

The word budget in the rules comes from these files, and 68 of the 78 fit it. No scenario reran, so the budget is unmeasured on the runtimes, and the verdicts still cite the graded originals. The Doc label and Status dashes stay, since the Doc template prescribes them.

### What is tracked

Tracked here: this README, `results.csv`, `results.md`, `grading-notes.md`, `hvr-lint.csv`, `manifest.json`, `run-status.json`, `replies/`, each scenario's `meta.json` and `turn-<n>.md`, and `run/`. Each `remeasure-*/run-1/` folder is tracked the same way.

Kept local by `.gitignore`: the event streams and `run-log.jsonl`, stderr, transcripts, the progress file and each scenario's `exports/` copy. The deliverables themselves are tracked in `export/benchmark/`.

### Project extraction review

Each Project file still published, beside its reply. At collection, each file's text was found verbatim in the reply named here, as the block that reply rendered. The hand edit under Edited after grading changed the files, so the match now holds for the graded originals.

| Collected file | Found in |
| --- | --- |
| `PBG-001 - NNN - bug-ios-cart-badge-stale-after-remove.md` | `replies/PBG-001-turn1.txt` |
| `PBG-002 - NNN - bug-android-confirmation-total-missing-city-tax (turn 2).md` | `replies/PBG-002-turn2.txt` |
| `PBG-002 - NNN - bug-android-confirmation-total-missing-city-tax.md` | `replies/PBG-002-turn1.txt` |
| `PBG-003 - 002 - bug-reminders-late-after-march-clock-change.md` | `replies/PBG-003-turn2.txt` |
| `PDK-001 - 001 - doc-promotions-stacking (turn 2).md` | `replies/PDK-001-turn2.txt` |
| `PDK-001 - 001 - doc-promotions-stacking.md` | `replies/PDK-001-turn1.txt` |
| `PDK-002 - 002 - doc-payment-webhook-failures-runbook.md` | `replies/PDK-002-turn2.txt` |
| `PDK-003 - 001 - doc-sync-conflicts-lost-edits-status.md` | `replies/PDK-003-turn1.txt` |
| `PDK-003 - 002 - doc-sync-conflict-options-proposal.md` | `replies/PDK-003-turn2.txt` |
| `PDK-004 - 002 - doc-loomlist-activity-emails.md` | `replies/PDK-004-turn2.txt` |
| `PEP-001 - 002 - Epic-partner-hub-self-onboarding.md` | `replies/PEP-001-turn2.txt` |
| `PEP-002 - 002 - Epic-offline-mode.md` | `replies/PEP-002-turn2.txt` |
| `PEP-003 - 001 - Epic-self-serve-returns.md` | `replies/PEP-003-turn1.txt` |
| `PID-001 - 002 - task-due-today-filter-chip.md` | `replies/PID-001-turn2.txt` |
| `PIR-001 - 002 - Epic-guest-loyalty-points.md` | `replies/PIR-001-turn2.txt` |
| `PIR-002 - 002 - Story-customer-wishlist-account-wishlist-in-apps.md` | `replies/PIR-002-turn2.txt` |
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
| `PTK-006 - 002 - task-booking-funnel-event-checks.md` | `replies/PTK-006-turn2.txt` |
