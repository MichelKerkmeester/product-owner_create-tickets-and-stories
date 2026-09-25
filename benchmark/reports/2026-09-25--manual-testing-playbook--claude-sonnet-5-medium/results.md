# Results, 2026-09-25, Product Owner, claude-sonnet-5 medium

Both handovers failed: `SID-001` (skill) and `PID-001` (Project). Every other row in both runtimes is graded and carries `after_failed_gate` yes. The identity proof itself held on both sides. Each handover failed on additions its reply never names, and `SID-001` also on its Turn 2, see `README.md` section 1.

The addition rows were regraded on 2026-09-25 after the operator allowed a disclosed addition (root line 156 in the working tree). `STK-001` and `SIR-001` moved from FAIL to PASS. The other six rows read again kept their verdicts then (`grading-notes.md` section 1). Later the same day the operator ruled that a reply naming a criterion as an addition has named every clause inside it (root line 156 at version 1.0.0.3), and `SST-001` moved from FAIL to PASS.

Counts come from `results.csv` by this command, run from this folder:

```bash
python3 -c "import csv,collections as c;r=list(csv.DictReader(open('results.csv')));t=c.Counter((x['runtime'],x['result']) for x in r);[print(k,v) for k,v in sorted(t.items())];print('total',len(r))"
```

Output: `('project', 'FAIL') 4`, `('project', 'PASS') 3`, `('skill', 'FAIL') 3`, `('skill', 'PASS') 4`, `total 14`.

| Runtime | PASS | FAIL | SKIP | Total |
| --- | ---: | ---: | ---: | ---: |
| Skill (`S`) | 4 | 3 | 0 | 7 |
| Project (`P`) | 3 | 4 | 0 | 7 |

---

## All 14 scenarios

| ID | Runtime | Verdict | One-line reason |
| --- | --- | --- | --- |
| PBG-001 | project | PASS | One evidence question as its own block, then a clean bug block with honest `Not provided` fields and the four fixed checklist items. Turn 1 commentary first is advisory |
| PDK-001 | project | PASS | Block first on both turns, all five Doc fields asked with the notes, guide passes the ClickUp gate with every note value |
| PDK-002 | project | FAIL | Turn 2 has a blank line between every heading and its divider. Turn 1 commentary first is advisory |
| PID-001 | project | FAIL | Identity proof holds, but the task adds three items the reply never names (inline error, whitespace rule, cancel flow) |
| PIR-001 | project | FAIL | Turn 2 invents that creators contact support and adds three checklist rules the reply never names. Turn 1 commentary first is advisory |
| PST-001 | project | PASS | One intake question as its own block, then a Story with its kind named, both hard values verbatim in Requirements and its one addition named. Turn 1 commentary first is advisory |
| PTK-001 | project | FAIL | Turn 2 adds two items the reply never names, a keep-the-row-unchanged rule and a history timestamp. Turn 1 commentary first is advisory |
| SBG-001 | skill | PASS | Clarification then bug export, honest `Not provided` fields, `Always`, Chrome 126 and the four fixed checklist items |
| SDK-001 | skill | FAIL | Turn 2 read-back returned no content (offset past the end of the file), yet the reply printed the read-back succeeded line |
| SDK-002 | skill | FAIL | Turn 1 made no tool calls: no clarification export, no path, no read-back line, no HVR self-scan line |
| SID-001 | skill | FAIL | Turn 1 proof holds, but Turn 2 never repeats the saved path and the task adds an error message and a cancel flow the reply never names |
| SIR-001 | skill | PASS | Energy-first intake and Quick task are right, and its one addition, a missing-data checklist item, is named in the reply |
| SST-001 | skill | PASS | Hard values verbatim and kind named. Criterion 2 keeps entered input on refusal, and the reply names criterion 2 as an addition, which names every clause in it |
| STK-001 | skill | PASS | Wait state and facts are right, and the page value `Creator payouts` and the scope-out sentence are both named in the reply as additions |

`facts_intact` is yes on all 14 rows: every user-supplied fact reached the deliverable. The failures are unnamed additions, layout and verification, not lost facts. Five Project rows record Turn 1 commentary before the clarification block as an advisory defect, and it decides none of them (root line 136 at Barter `a6442856`).

---

## Twin table

Pairs and agreement from `results.csv` by:

```bash
python3 -c "import csv;r={x['id']:x['result'] for x in csv.DictReader(open('results.csv'))};[print(s,r[s],'P'+s[1:],r['P'+s[1:]],'agree' if r[s]==r['P'+s[1:]] else 'DIFFER') for s in sorted(k for k in r if k[0]=='S')]"
```

| Pair | Skill | Project | Agreement | Cause of the difference | Class |
| --- | --- | --- | --- | --- | --- |
| BG-001 | PASS | PASS | Agree | None. Project Turn 1 put commentary before its clarification block, recorded as advisory | No verdict difference. Advisory runtime fault (Project) |
| DK-001 | FAIL | PASS | Differ | Skill Turn 2 claimed a read-back whose Read returned no content | Runtime fault |
| DK-002 | FAIL | FAIL | Agree, different reasons | Skill Turn 1 skipped the clarification export and HVR line. Project Turn 2 put a blank line between every heading and its divider | Runtime fault on both sides, plus a contributing parity gap on the skill side |
| ID-001 | FAIL | FAIL | Agree, partly different reasons | Both add an error message and a cancel flow their replies never name. Only the skill misses a Turn 2 expectation (repeat the path) | Shared: runtime fault on both sides, with a contributing parity gap (Project). Skill-only: rule gap |
| IR-001 | PASS | FAIL | Differ | Both add a missing-data item and name it. Only the Project adds items it never names, a support-contact claim among them | Runtime fault (Project), with a contributing parity gap |
| ST-001 | PASS | PASS | Agree | None. Skill criterion 2 keeps entered input on refusal (export line 64), and the reply names criterion 2 as an addition, which names every clause in it. The Project Story names its one addition | No verdict difference |
| TK-001 | PASS | FAIL | Differ | Both add items. The skill names every one, the Project leaves two unnamed | Runtime fault (Project), with a contributing parity gap |

3 pairs disagreed (`DK-001`, `IR-001` and `TK-001`), 4 agreed, 0 unpaired. `IR-001` and `TK-001` agreed on FAIL before the addition regrade of 2026-09-25, and `BG-001` differed and `ST-001` agreed on FAIL before the ordering regrade of the same day. `ST-001` differed from the ordering regrade until the naming regrade, also of 2026-09-25, and now agrees on PASS. Every class is confirmed against both sides' rule files in `grading-notes.md` section 4.
