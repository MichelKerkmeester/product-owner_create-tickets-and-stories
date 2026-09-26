# Results, 2026-09-25, Product Owner, claude-opus-5-5 medium

Written from `results.csv`. `grading-notes.md` holds the evidence behind each verdict and every row the operator's rulings of 2026-09-25 changed.

## 1. Verdicts

| ID | Runtime | Company | Scenario | Result | Turns | After failed gate | Facts intact |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `SBG-001` | skill | Fernhouse | Quick bug | PASS | 1 of 1 | no | yes |
| `PBG-001` | project | Fernhouse | Quick bug | PASS | 1 of 1 | yes | yes |
| `SBG-002` | skill | Roamstay | Support ticket bug | FAIL | 2 of 2 | no | yes |
| `PBG-002` | project | Roamstay | Support ticket bug | FAIL | 2 of 2 | yes | yes |
| `SBG-003` | skill | Loomlist | Two-platform log bug | PASS | 2 of 2 | no | yes |
| `PBG-003` | project | Loomlist | Two-platform log bug | PASS | 2 of 2 | yes | yes |
| `SDK-001` | skill | Fernhouse | Behavior reference | FAIL | 2 of 2 | no | no |
| `PDK-001` | project | Fernhouse | Behavior reference | FAIL | 2 of 2 | yes | yes |
| `SDK-002` | skill | Roamstay | Incident runbook | PASS | 2 of 2 | no | yes |
| `PDK-002` | project | Roamstay | Incident runbook | PASS | 2 of 2 | yes | yes |
| `SDK-003` | skill | Loomlist | Proposal with a decision owner | PASS | 2 of 2 | no | yes |
| `PDK-003` | project | Loomlist | Proposal with a decision owner | FAIL | 2 of 2 | yes | yes |
| `SDK-004` | skill | Loomlist | Catalog conflict gate | PASS | 2 of 2 | no | yes |
| `PDK-004` | project | Loomlist | Catalog conflict gate | PASS | 2 of 2 | yes | yes |
| `SEP-001` | skill | Roamstay | Epic from strategy brief | FAIL | 2 of 2 | no | yes |
| `PEP-001` | project | Roamstay | Epic from strategy brief | FAIL | 2 of 2 | yes | yes |
| `SEP-002` | skill | Loomlist | Epic natural wording | PASS | 2 of 2 | no | yes |
| `PEP-002` | project | Loomlist | Epic natural wording | FAIL | 2 of 2 | yes | yes |
| `SEP-003` | skill | Fernhouse | Epic quick energy | PASS | 1 of 1 | no | yes |
| `PEP-003` | project | Fernhouse | Epic quick energy | PASS | 1 of 1 | yes | yes |
| `SID-001` | skill | Loomlist | Skill identity handover | PASS | 2 of 2 | no | yes |
| `PID-001` | project | Loomlist | Project identity handover | FAIL | 2 of 2 | no | yes |
| `SIR-001` | skill | Roamstay | Vague intake, kind and energy | PASS | 2 of 2 | no | yes |
| `PIR-001` | project | Roamstay | Vague intake, kind and energy | PASS | 2 of 2 | yes | yes |
| `SIR-002` | skill | Fernhouse | Conflicting commands | PASS | 2 of 2 | no | yes |
| `PIR-002` | project | Fernhouse | Conflicting commands | FAIL | 2 of 2 | yes | yes |
| `SST-001` | skill | Roamstay | Story hard values | PASS | 2 of 2 | no | yes |
| `PST-001` | project | Roamstay | Story hard values | PASS | 2 of 2 | yes | yes |
| `SST-002` | skill | Loomlist | Story forced delivery | FAIL | 2 of 2 | no | no |
| `PST-002` | project | Loomlist | Story forced delivery | FAIL | 2 of 2 | yes | no |
| `SST-003` | skill | Fernhouse | Story refinement | FAIL | 2 of 2 | no | no |
| `PST-003` | project | Fernhouse | Story refinement | FAIL | 2 of 2 | yes | no |
| `SST-004` | skill | Fernhouse | Story with nested tasks | FAIL | 2 of 2 | no | yes |
| `PST-004` | project | Fernhouse | Story with nested tasks | FAIL | 2 of 2 | yes | yes |
| `STK-001` | skill | Fernhouse | Quick copy task | PASS | 1 of 1 | no | yes |
| `PTK-001` | project | Fernhouse | Quick copy task | PASS | 1 of 1 | yes | yes |
| `STK-002` | skill | Roamstay | Design notes FE task | FAIL | 2 of 2 | no | yes |
| `PTK-002` | project | Roamstay | Design notes FE task | FAIL | 2 of 2 | yes | yes |
| `STK-003` | skill | Fernhouse | Long BE integration task | FAIL | 2 of 2 | no | yes |
| `PTK-003` | project | Fernhouse | Long BE integration task | FAIL | 2 of 2 | yes | no |
| `STK-004` | skill | Loomlist | Parent task with subtasks | FAIL | 2 of 2 | no | yes |
| `PTK-004` | project | Loomlist | Parent task with subtasks | FAIL | 2 of 2 | yes | yes |
| `STK-005` | skill | Loomlist | Supplied parent subtask | FAIL | 2 of 2 | no | yes |
| `PTK-005` | project | Loomlist | Supplied parent subtask | FAIL | 2 of 2 | yes | yes |
| `STK-006` | skill | Roamstay | Data tracking task | FAIL | 2 of 2 | no | no |
| `PTK-006` | project | Roamstay | Data tracking task | FAIL | 2 of 2 | yes | no |

## 2. Twins

| Pair | Scenario | Skill | Project | Agree |
| --- | --- | --- | --- | --- |
| `BG-001` | Quick bug | PASS | PASS | yes |
| `BG-002` | Support ticket bug | FAIL | FAIL | yes |
| `BG-003` | Two-platform log bug | PASS | PASS | yes |
| `DK-001` | Behavior reference | FAIL | FAIL | yes |
| `DK-002` | Incident runbook | PASS | PASS | yes |
| `DK-003` | Proposal with a decision owner | PASS | FAIL | no |
| `DK-004` | Catalog conflict gate | PASS | PASS | yes |
| `EP-001` | Epic from strategy brief | FAIL | FAIL | yes |
| `EP-002` | Epic natural wording | PASS | FAIL | no |
| `EP-003` | Epic quick energy | PASS | PASS | yes |
| `ID-001` | Skill identity handover | PASS | FAIL | no |
| `IR-001` | Vague intake, kind and energy | PASS | PASS | yes |
| `IR-002` | Conflicting commands | PASS | FAIL | no |
| `ST-001` | Story hard values | PASS | PASS | yes |
| `ST-002` | Story forced delivery | FAIL | FAIL | yes |
| `ST-003` | Story refinement | FAIL | FAIL | yes |
| `ST-004` | Story with nested tasks | FAIL | FAIL | yes |
| `TK-001` | Quick copy task | PASS | PASS | yes |
| `TK-002` | Design notes FE task | FAIL | FAIL | yes |
| `TK-003` | Long BE integration task | FAIL | FAIL | yes |
| `TK-004` | Parent task with subtasks | FAIL | FAIL | yes |
| `TK-005` | Supplied parent subtask | FAIL | FAIL | yes |
| `TK-006` | Data tracking task | FAIL | FAIL | yes |
