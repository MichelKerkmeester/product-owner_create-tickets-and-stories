# Manual testing playbook run, 2026-09-25, Product Owner, claude-sonnet-5 medium

## 1. Handover status, read this first

**Both handovers failed.** `SID-001` (skill) and `PID-001` (Project) are FAIL, so every other verdict in both runtimes is in question, and those twelve rows carry `after_failed_gate` yes in `results.csv`.

- **Skill, `SID-001`.** The identity proof held on Turn 1: a real path, `Verified: read-back succeeded; 65 lines` and the HVR self-scan line, with no Project wording in either reply. It failed on two other grounds. Turn 2 never repeats the saved path, which the scenario asks for three times (`skill-identity/identity-handover.md` lines 30, 40 and 78). The task also carries checklist items the user never supplied, and the reply admits it: "Some checklist items go beyond your brief"
- **Project, `PID-001`.** The identity proof held: the task block rendered before any commentary, `Export-equivalent path:`, the HVR line, and on Turn 2 "No, I didn't write any file to disk." It failed because the task adds requirements the user never supplied, several of them undisclosed (a whitespace rule, a cancel flow, an inline error, banner copy about when the pause ends)

So the runtimes identified themselves correctly. What failed is the artifact each handover produced, under the playbook's invented-fact rule (root line 156). Each scenario ran in its own fresh session, so neither handover changed what a later scenario could do (root line 144). The doubt the playbook asks for is about the runtime's habits, not about the later sessions' setup.

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
a=[x for x in r if x['runtime']=='project' and 'Advisory: Turn 1 commentary' in x['note']]
print('project rows with advisory Turn 1 commentary',len(a),'PASS among them',sum(x['result']=='PASS' for x in a))
d={x['id']:x['result'] for x in r}
print('twin pairs differing',sum(d[k]!=d['P'+k[1:]] for k in d if k[0]=='S'),'of',sum(k[0]=='S' for k in d))
"
```

Output: `project FAIL 4`, `project PASS 3`, `skill FAIL 6`, `skill PASS 1`, `facts_intact yes 14 of 14`, `after_failed_gate yes 12`, `project rows with advisory Turn 1 commentary 5 PASS among them 2`, `twin pairs differing 2 of 7`.

| Runtime | PASS | FAIL | SKIP | Total |
| --- | ---: | ---: | ---: | ---: |
| Skill (`S`) | 1 | 6 | 0 | 7 |
| Project (`P`) | 3 | 4 | 0 | 7 |

The passes are `SBG-001`, `PBG-001`, `PDK-001` and `PST-001`. Every supplied fact reached every deliverable. The failures come from three sources:

- **Additions the user never supplied**, in `SID-001`, `STK-001`, `SST-001`, `SIR-001`, `PID-001`, `PTK-001` and `PIR-001`. `STK-001` and `SIR-001` fail only on additions the reply disclosed, which is the open conflict in section 6, finding 1
- **Doc layout**: `PDK-002` Turn 2 puts a blank line between every heading and its divider (`Product Owner - Templates - Doc Mode - v0.109.md` line 74)
- **Skill delivery proof**: `SDK-001` printed a read-back line for a Read that returned no content, and `SDK-002` Turn 1 made no tool call, so it exported no clarification and printed no self-scan line

Five Project Turn 1 replies, `PTK-001`, `PBG-001`, `PDK-002`, `PST-001` and `PIR-001`, put commentary before the clarification block. Each row records it as an advisory defect, and it decides none of them. The operator ruled that the advisory ordering rule wins, and Barter `a6442856` wrote that into root line 136: commentary before a block fails only a scenario that tests delivery shape, which in this set is `PID-001` alone, and `PID-001` put its block first. The regrade turned `PBG-001` and `PST-001` from FAIL to PASS on 2026-09-25 (`grading-notes.md` section 1).

`results.md` has the table of all 14 and the twin table. `grading-notes.md` has the quotes, the read-back table and a second-read note for every FAIL.

---

## 3. How the run was made

- Runner `run/playbook_runner.py`, hash `a0315dcd5b`, the same hash the implementation summary records. Engine `claude`, Claude Code `2.1.282`, model `claude-sonnet-5`, effort `medium` (`manifest.json`, every `meta.json`). Every assistant event in all 28 streams reports `claude-sonnet-5`
- Two parallel sessions. Event timestamps show at most two scenarios running at once, in the five waves of root section 6, with `SID-001` and `PID-001` first (10:22:28 UTC) and `SIR-001` and `PIR-001` last (ending 10:27:52 UTC)
- Playbook at Barter `4fb9dd88`. 14 scenarios, 7 skill and 7 Project, each twinned, 28 turns, every scenario completed on its first attempt with `turns_run` 2 of 2 (`run-status.json`)
- Skill side: a disposable sandbox per scenario that kept its `export/` folder across both turns, tools Bash, Edit, Glob, Grep, Read and Write. Each scenario's written files are under `skill/<ID - slug>/exports/export/`
- Project side: `claude project/Custom Instructions.md` as the system prompt plus the runner's retrieval note, the knowledge folder beside it, read-only tools (Glob, Grep, Read). No Canvas panel, so the block stand-in of root line 136 applied. Every Project ledger is empty
- Grading: every reply, every event stream, every written file and the shared format gate, run over each skill export and each Project block extracted from its reply. Method and evidence are in `grading-notes.md` section 1. The Project ordering rows were regraded against Barter `a6442856`, which rewrote root lines 132 and 136 and moved no line number

---

## 4. Comparison with 2026-09-17

**Not comparable, all 14 scenarios.** Barter `4fb9dd88` changed the criteria of every scenario in this playbook, and the 2026-09-17 run also used a different harness (`run_packaging.sh`, which rebuilt the scratch tree on every turn and gave the Project runtime write tools). What changed:

- Root, affecting all 14: new Clarification turns, Rendering without a Canvas panel, Export names and Handovers in an automated run sections, and the rule that there is no verdict between PASS and FAIL (root lines 125 to 144)
- `SID-001`: proof graded on Turn 1, Turn 2 must name the same file, `N` recorded
- `STK-001`, `SBG-001`, `SDK-002`, `SST-001`, `SIR-001`: the Turn 1 reply must now carry the path, the read-back line and the HVR line
- `SDK-001` and `PDK-001`: the five-field minimum replaced the purpose and audience fields. `SDK-001` now fails spacer headings and `PDK-001` does not grade them. `PDK-001` Turn 2 now needs the Doc summary and HVR line
- `PID-001`: the words `Canvas Artifact` are no longer required, and the rendered block plus label on Turn 1 is what is graded
- `PTK-001`, `PBG-001`, `PDK-002`, `PST-001`, `PIR-001`: the Turn 1 question must render as its own block with the HVR line. `PDK-002` Turn 2 now needs the Doc summary. `PST-001` now fails on opening both scaffolds

Verdicts side by side, for reference only, from both `results.csv` files by:

```bash
python3 -c "import csv;a={x['id']:x['result'] for x in csv.DictReader(open('../2026-09-17--manual-testing-playbook--claude-sonnet-5-medium/results.csv'))};b={x['id']:x['result'] for x in csv.DictReader(open('results.csv'))};[print(k,a[k],b[k]) for k in sorted(b)]"
```

| ID | 2026-09-17 | 2026-09-25 | Comparable |
| --- | --- | --- | --- |
| PBG-001 | FAIL | PASS | No |
| PDK-001 | FAIL | PASS | No |
| PDK-002 | PASS | FAIL | No |
| PID-001 | PASS | FAIL | No |
| PIR-001 | FAIL | FAIL | No |
| PST-001 | FAIL | PASS | No |
| PTK-001 | FAIL | FAIL | No |
| SBG-001 | PASS | PASS | No |
| SDK-001 | FAIL | FAIL | No |
| SDK-002 | PASS | FAIL | No |
| SID-001 | PASS | FAIL | No |
| SIR-001 | FAIL | FAIL | No |
| SST-001 | FAIL | FAIL | No |
| STK-001 | PASS | FAIL | No |

Behavior that can be described without comparing verdicts:

- The 2026-09-17 Turn 1 gate skips on no-token requests (`SDK-001`, `SST-001`, `PDK-001`, `PST-001`) did not recur. All four asked the consolidated question this time
- The 2026-09-17 energy-order miss (`SIR-001`, `PIR-001`) did not recur. Both opened with the Quick or Deeper choice
- On 2026-09-17, `PTK-001` and `PBG-001` Turn 1 rendered no block, label or self-scan. This run every Project Turn 1 carries all three, but five put commentary before the block, an advisory defect since Barter `a6442856`
- The 2026-09-17 disk write by `PST-001` cannot recur, because the Project tool list is now read-only
- HVR lint: 25 of 28 replies dirty with 24 em dash hits on 2026-09-17, 16 of 28 dirty with 0 em dash hits now (`python3 -c "import csv,sys;r=list(csv.DictReader(open(sys.argv[1]+'/hvr-lint.csv')));print(sum(x['clean']=='False' for x in r),len(r),sum('em_dash' in x['violations'] for x in r))" <folder>` on each folder)

---

## 5. Divergence summary

2 of 7 pairs disagreed, both runtime faults on the skill side, and each is confirmed in both sides' rule files in `grading-notes.md` section 4:

- **DK-001, skill FAIL, Project PASS.** The skill printed a read-back line although its only Read returned no content (`AGENTS.md` line 46, `sk-product-owner/SKILL.md` line 211). The Project has no read-back step by design (`Custom Instructions.md` line 234). Everything the two share passed on both sides
- **ST-001, skill FAIL, Project PASS.** The skill's criterion 2 adds a clause nobody supplied or disclosed, "anything already entered is kept" (`SST-001` export line 64). Both runtimes carry the same Story-lane ban, "Never invent requirements, evidence or links" (`sk-product-owner/references/story-mode.md` line 82, `claude project/knowledge/Product Owner - Templates - Story Mode - v0.400.md` line 59), and the same "edges that matter" allowance (`sk-product-owner/assets/story-template.md` line 116, `Product Owner - Assets - Story Template - v0.100.md` line 97). The skill also has the ban always loaded (`AGENTS.md` line 106, `SKILL.md` line 283). No rule difference explains it, and the Project followed the shared rule

`BG-001` agrees on PASS. It disagreed before the regrade, when the Project's Turn 1 commentary decided `PBG-001`. That commentary is still a runtime fault against `Custom Instructions.md` line 85, recorded as advisory.

Four pairs agree on FAIL. `DK-002` fails for different reasons on each side: the skill's Turn 1 skipped the clarification export, and the Project's Turn 2 broke the heading-to-divider layout. `IR-001` and `TK-001` fail under the same invented-fact rule on both sides with different standing: each skill reply disclosed every addition that decides its verdict, so the skill side rests on the open conflict of finding 1, while each Project reply also added items it never disclosed. If finding 1 is settled in favor of disclosure, `SIR-001` and `STK-001` pass while `PIR-001` and `PTK-001` still fail, and both pairs diverge. `ID-001` fails for a shared reason (unsupplied requirements on both sides) plus a skill-only Turn 2 miss that no runtime rule asks for, a rule gap between the two twins' Turn 2 prompts.

---

## 6. Follow-up findings

### Recorded conflicts this run touched

1. **Disclosed additions against the invented-fact rule.** Touched by `SID-001`, `STK-001`, `SIR-001`, `PID-001`, `PTK-001` and `PIR-001`. The playbook makes any requirement, value or behavior the user never supplied blocking, with no exception for disclosure (`manual-testing-playbook.md` line 156). The skill forbids inventing requirements (`sk-product-owner/SKILL.md` line 283) but asks for edge, error and empty states (line 267) and puts assumptions in the reply "so the user can correct one" (line 201). The Project carries the same pair (`Custom Instructions.md` line 198, `Product Owner - Templates - Task Mode - v0.305.md` line 330). Graded as written here. `STK-001` and `SIR-001` rest on this conflict alone and would pass if it is settled in favor of disclosure, which would make the `TK-001` and `IR-001` twins diverge (section 5)
2. **The read-back count `N`.** Touched by `SID-001`: printed 65, Read's final line 66, the file 65 lines (`skill-identity/identity-handover.md` line 63 records it and no text fails it). `AGENTS.md` line 46 and `SKILL.md` line 211 define `N` as Read's final line number. The Read tool numbers a newline-terminated file one past its length, so a correct `N` is always the real count plus one, and every skill reply except `SID-001` printed exactly that (read-back table, `grading-notes.md` section 1). Not graded
3. **Spacer headings in a rendered Doc block.** Touched by `PDK-001` and `PDK-002`. Both Project replies left spacers out "because this is a file export", so the runtime settled the rule's silence itself. `Product Owner - Templates - Doc Mode - v0.109.md` line 73 and `Custom Instructions.md` line 137 allow spacers only in ClickUp-bound content and never in a file export, and neither says which a rendered block is. Skill side: `sk-product-owner/references/doc-mode.md` line 97
4. **Printing a clarification question in chat.** Touched by `SDK-001` Turn 1, which printed all six questions beside the file, and `SDK-002` Turn 1, which printed them only in chat. `sk-product-owner/references/interactive-mode.md` line 122 asks the user the question, and `AGENTS.md` line 92 keeps the full artifact out of chat. Not graded (root line 131)

### New findings

5. **The Project Task lane cannot see "never invent requirements".** The kernel's NEVER list sends documentation prohibitions to Doc Mode knowledge (`Custom Instructions.md` lines 94 and 98), which is where NEVER 4 sits (`Product Owner - Templates - Doc Mode - v0.109.md` line 553). Task Mode knowledge has the edge-case rule (line 330) and no invention ban. On the skill side the ban is always loaded, twice (`AGENTS.md` line 106 and `SKILL.md` line 283). `PID-001`, `PTK-001` and `PIR-001` opened Task Mode knowledge, never Doc Mode, and carried the most undisclosed additions. Parity gap
6. **`AGENTS.md` never says a clarification is exported.** Its only clarification line is line 188, about conflicting commands. The export rule lives in `SKILL.md` line 208 and `interactive-mode.md` line 85, while the always-loaded Project kernel states it at `Custom Instructions.md` line 227. `SDK-002` Turn 1 made no tool call, never opened `SKILL.md` (which `AGENTS.md` line 144 requires) and exported nothing. Parity gap in the always-loaded layer
7. **Read-back accepts a partial or empty read.** `AGENTS.md` line 46 requires non-empty content at the path but not the whole file. `SID-001` read lines 60 to 66 only, and its Turn 2 says "I never confirmed the top of the file". `SDK-001`'s only Read returned a warning with no content, and the reply still printed the fixture. After an Edit, "the final line number returned by Read" has two readings: `SBG-001` printed 75 from the read before its Edit, while its last Read returned lines 28 to 37. The check can pass without checking the file
8. **Project Turn 1 puts commentary first.** Five of seven Project Turn 1 replies explain themselves before the clarification block, while every Project Turn 2 delivery renders first. `Custom Instructions.md` line 85 states render-first for "the Deliverable Block", and that a clarification is such a block is said in knowledge (`Product Owner - System - Interactive Mode - v0.404.md` lines 62 and 74) and implied by kernel line 227, not beside line 85. A runtime fault, recorded as an advisory defect, with a wording gap worth closing in the kernel. The playbook conflict this finding first recorded is resolved. At Barter `4fb9dd88`, root lines 132 and 136 counted a clarification block only when it came before any commentary, while root lines 162 to 164 made response ordering advisory unless the scenario tests delivery shape. The operator ruled that the advisory rule wins, and Barter `a6442856` (Product Owner public repo `33cb3b5`) removed "before any commentary" from root line 132 and made root line 136 record commentary before a block as a response-ordering defect that fails only a scenario testing delivery shape, naming `PID-001` as one. Regraded on that text, `PBG-001` and `PST-001` pass and the Project reads 3 PASS and 4 FAIL. `PDK-002`, `PTK-001` and `PIR-001` still fail, on layout and on undisclosed additions
9. **The format gate misses heading-to-divider adjacency.** The shared format gate `validate-output-format.cjs` (in the Claude Project Sync Loop folder at the `AI Systems/` root) at line 585 skips blank lines when it looks for the divider under a heading, while `doc-mode.md` line 98 and Doc Mode knowledge line 74 say nothing sits between them. `PDK-002` Turn 2 passed the gate with a blank line under every heading
10. **Self-scan counts miss full-stop bullets in clarifications.** The `SDK-001` Turn 1 file (line 8) and the `PBG-001` Turn 1 block each end one bullet with a full stop and report `0 hard blockers` (`references/hvr-core.md` lines 35 and 132). Both were graded advisory: root line 159 fails a count that was never taken, a wrong count is not evidence that none was taken, and no Pass clause grades count accuracy. Since the regrade `PBG-001` passes with this defect, which makes the reading decisive. If a wrong zero counts as a count never taken, `PBG-001` fails again, and `Custom Instructions.md` line 242 says a zero with no terms named is valid only when the artifact has none
11. **Linter false positive on the quoted fixture.** `benchmark/grader/hvr_lint.py` line 112 strips `Verified:` only at the start of a line, so `SID-001` Turn 2 quoting `` `Verified: read-back succeeded; 65 lines` `` mid-sentence counts as a semicolon
12. **Playbook wording.** `project-identity/identity-handover.md` lines 32 and 76 say "claims no local file was written", which reads as either stating it or making no file claim, while the Turn 1 row (line 39) asks only that no path is claimed. `skill-identity/identity-handover.md` lines 30, 40 and 78 ask Turn 2 to repeat the path, which no runtime rule asks of a follow-up answer (`AGENTS.md` lines 87 to 92). The ordering conflict this item also listed is resolved, see finding 8

---

## 7. What `check_report.sh` found

`bash benchmark/grader/check_report.sh "benchmark/reports/2026-09-25--manual-testing-playbook--claude-sonnet-5-medium"`, run from `AI Systems/Product Owner/` after the regrade of 2026-09-25, exited **2**: both checks reported findings. The exit code counts checks with findings, not a crash. It rewrote `hvr-lint.csv` in this folder with the same content as before, the same way the 2026-09-17 folder produced its own.

- **`twin_divergence`**: `DK-001: skill FAIL, Project PASS`, `ST-001: skill FAIL, Project PASS`, 5 agreed, 2 disagreed, 0 not settled, 0 run on one runtime only. Matches section 5. Before the regrade it named `BG-001` in place of `ST-001`
- **`lint_replies`**: 12 of 28 replies clean, 16 dirty. Fifteen carry `bullet_ends_with_full_stop` only, and `SID-001-turn2.txt` carries one `semicolon`, the quoted fixture of finding 11. Almost every full-stop bullet sits in chat prose around the deliverable, such as assumption lists and quality summaries. One sits inside a delivered block (`PBG-001` Turn 1, now a PASS), and the format gate found one more inside a delivered file (`SDK-001` Turn 1), finding 10. Lint stays a separate axis from the verdicts, as on 2026-09-17

---

## 8. Files in this folder

| File | What it is |
| --- | --- |
| `results.csv` | All 14 scenarios, `id,runtime,model,result,turns_run,turns_declared,after_failed_gate,facts_intact,note` |
| `results.md` | Verdict table and twin table |
| `grading-notes.md` | Evidence, quotes, read-back table, block forms, second reads and twin adjudications |
| `hvr-lint.csv` | Written by `check_report.sh`, one row per reply |
| `replies/` | The final reply of every turn, 28 files |
| `skill/`, `claude project/` | Per-scenario turns, transcripts, event streams and `meta.json`, plus each skill scenario's written files |
| `manifest.json`, `run-status.json`, `run-log.jsonl` | The runner's own records |
| `run/` | The runner, the collector and the run check at the hash above |

---

## Next steps

1. Settle finding 1, whether a disclosed addition is an invented fact. It decides `STK-001` and `SIR-001` outright and bears on five other scenarios. Then write the answer into root line 156 and into the Task Mode rules on both sides
2. Close the two parity gaps: add the clarification export to `AGENTS.md` Section 2 (finding 6), and put NEVER 4 where the Project Task lane reads it, in the kernel or in Task Mode knowledge (finding 5)
3. Settle whether a self-scan zero that misses a hard blocker is a count never taken (root line 159, finding 10). `PBG-001` passes only on the reading that it is not, so write the answer into root line 159 either way
4. Tighten the Project render-first wording so it names the clarification block beside `Custom Instructions.md` line 85 (finding 8). Ordering now decides only `PID-001`, so this is a runtime-quality fix: re-run the five Project scenarios whose Turn 1 put commentary first and record the ordering as advisory
5. Tighten `AGENTS.md` line 46 so a read-back must return content, and say which Read sets `N` after an Edit (findings 2 and 7). Make `validate-output-format.cjs` check heading-to-divider adjacency without skipping blank lines (finding 9)
6. Re-run `SID-001` and `PID-001` after steps 1 and 2, since both handovers failed on their artifact rather than their identity proof, and grade the rest of each set against a passing handover
