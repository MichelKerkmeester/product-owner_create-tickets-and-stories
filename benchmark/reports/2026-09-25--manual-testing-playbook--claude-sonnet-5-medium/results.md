# Results, 2026-09-25, Product Owner, claude-sonnet-5 medium

Both handovers failed: `SID-001` (skill) and `PID-001` (Project). Every other row in both runtimes is graded and carries `after_failed_gate` yes. The identity proof itself held on both sides. Each handover failed on its task artifact, see `README.md` section 1.

Counts come from `results.csv` by this command, run from this folder:

```bash
python3 -c "import csv,collections as c;r=list(csv.DictReader(open('results.csv')));t=c.Counter((x['runtime'],x['result']) for x in r);[print(k,v) for k,v in sorted(t.items())];print('total',len(r))"
```

Output: `('project', 'FAIL') 6`, `('project', 'PASS') 1`, `('skill', 'FAIL') 6`, `('skill', 'PASS') 1`, `total 14`.

| Runtime | PASS | FAIL | SKIP | Total |
| --- | ---: | ---: | ---: | ---: |
| Skill (`S`) | 1 | 6 | 0 | 7 |
| Project (`P`) | 1 | 6 | 0 | 7 |

---

## All 14 scenarios

| ID | Runtime | Verdict | One-line reason |
| --- | --- | --- | --- |
| PBG-001 | project | FAIL | Turn 1 puts two sentences of commentary before the clarification block. Turn 2 bug block is clean |
| PDK-001 | project | PASS | Block first on both turns, all five Doc fields asked with the notes, guide passes the ClickUp gate with every note value |
| PDK-002 | project | FAIL | Turn 1 puts commentary before the clarification block. Turn 2 has a blank line between every heading and its divider |
| PID-001 | project | FAIL | Identity proof holds, but the task adds requirements never supplied (reason visible to the brand, whitespace rule, cancel flow) |
| PIR-001 | project | FAIL | Turn 1 puts commentary before the block. Turn 2 invents that creators contact support and adds unsupplied checklist rules |
| PST-001 | project | FAIL | Turn 1 puts commentary before the clarification block. Turn 2 Story is otherwise sound |
| PTK-001 | project | FAIL | Turn 1 puts commentary before the clarification block. Turn 2 adds unsupplied items such as a history timestamp |
| SBG-001 | skill | PASS | Clarification then bug export, honest `Not provided` fields, `Always`, Chrome 126 and the four fixed checklist items |
| SDK-001 | skill | FAIL | Turn 2 read-back returned no content (offset past the end of the file), yet the reply printed the read-back succeeded line |
| SDK-002 | skill | FAIL | Turn 1 made no tool calls: no clarification export, no path, no read-back line, no HVR self-scan line |
| SID-001 | skill | FAIL | Turn 1 proof holds, but Turn 2 never repeats the saved path and the task carries requirements the reply admits go beyond the brief |
| SIR-001 | skill | FAIL | Energy-first intake and Quick task are right, but the task adds a missing-data checklist item the user never supplied |
| SST-001 | skill | FAIL | Hard values verbatim and kind named, but criterion 2 adds unsupplied behavior (the brand is told, entered input is kept) |
| STK-001 | skill | FAIL | Wait state and facts are right, but the task invents a page value `Creator payouts` and a scope-out sentence |

`facts_intact` is yes on all 14 rows: every user-supplied fact reached the deliverable. The failures are additions, ordering and verification, not lost facts.

---

## Twin table

Pairs and agreement from `results.csv` by:

```bash
python3 -c "import csv;r={x['id']:x['result'] for x in csv.DictReader(open('results.csv'))};[print(s,r[s],'P'+s[1:],r['P'+s[1:]],'agree' if r[s]==r['P'+s[1:]] else 'DIFFER') for s in sorted(k for k in r if k[0]=='S')]"
```

| Pair | Skill | Project | Agreement | Cause of the difference | Class |
| --- | --- | --- | --- | --- | --- |
| BG-001 | PASS | FAIL | Differ | Project Turn 1 put commentary before its clarification block | Runtime fault |
| DK-001 | FAIL | PASS | Differ | Skill Turn 2 claimed a read-back whose Read returned no content | Runtime fault |
| DK-002 | FAIL | FAIL | Agree, different reasons | Skill Turn 1 skipped the clarification export and HVR line. Project Turn 1 put commentary first | Runtime fault on both sides, plus a contributing parity gap on the skill side |
| ID-001 | FAIL | FAIL | Agree, partly different reasons | Both add unsupplied requirements. Only the skill misses a Turn 2 expectation (repeat the path) | Shared: open rule conflict. Skill-only: rule gap |
| IR-001 | FAIL | FAIL | Agree, different reasons | Both add a disclosed missing-data item. Only the Project put commentary first and invented a support-contact claim | Runtime fault (Project) |
| ST-001 | FAIL | FAIL | Agree, different reasons | Skill criterion 2 adds unsupplied behavior. Project Turn 1 put commentary first | Runtime fault on both sides |
| TK-001 | FAIL | FAIL | Agree, different reasons | Both add unsupplied items. Only the Project put commentary first | Runtime fault (Project) |

2 pairs disagreed, 5 agreed, 0 unpaired. Every class is confirmed against both sides' rule files in `grading-notes.md` section 4.
