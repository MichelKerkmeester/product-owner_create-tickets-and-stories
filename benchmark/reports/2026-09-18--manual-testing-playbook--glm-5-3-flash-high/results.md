# Product Owner benchmark results: GLM 5.3 Flash through Pi

Run on 2026-09-18 from `benchmark-plan.md` beside this file. Model `llmgateway/glm-5.3-flash` at thinking `high`, served upstream as `consensusprotocol/glm-5.3-flash`, through Pi 0.85.1. 14 scenarios, 28 turns, every declared turn run.

---

## 1. VERDICT

| | Skill | Claude Project |
| --- | ---: | ---: |
| PASS | 6 | 6 |
| PARTIAL | 1 | 1 |
| FAIL or SKIP | 0 | 0 |
| Identity gate | PASS | PASS |
| Twin pairs that disagree | 0 of 7 | |

The best result of the three systems. Both packagings deliver the contract, and they agree on every twin. The one pair that falls short, the doc guide, falls short on both sides for different reasons, so it is uncompared rather than divergent.

---

## 2. THE PAIR THAT FALLS SHORT

`SDK-001` and `PDK-001`, doc guide delivery, both `PARTIAL`.

| Side | What is missing |
| --- | --- |
| Skill | Turn 1 asked "Please paste the engineering notes." and nothing more, so no clarification export and no question on authority, status or shape. The guide then says a requeued notification returns to the failed queue "after attempt six", while its own Boundaries section says the notes do not say whether the count resets |
| Project | Turn 1 asked for the notes and one status question, with no clarification block and no export-equivalent label. The guide's "Boundaries and exceptions" heading carries no divider |

---

## 3. THE CLAUDE RUN'S TWO GAPS DID NOT APPEAR

The Claude Sonnet 5 run's two sampled gaps were both on the Project side and both delivery protocol. Neither reproduced here.

| Scenario | Claude Sonnet 5 Project, sampled | GLM Project, this run |
| --- | --- | --- |
| Clarification turn, `PTK-001` | 1 of 13 | PASS: one question, `Export-equivalent path:` label, no task drafted |
| Bug report block, `PBG-001` | 3 of 9 | PASS: Frequency, Device and `Browser Version \| 126` intact under its export-equivalent label |

This is one run per scenario. Claude's gap needed 13 samples to show, so one GLM pass does not show the gap is absent. It shows only that GLM did not fall into it on the first try.

---

## 4. SPEED, EFFORT AND COST

Per turn, from agent start to agent end, stamped on arrival. Pi startup was 0.21 seconds and is not included.

| | GLM skill | GLM Project | Claude Sonnet 5 skill | Claude Sonnet 5 Project |
| --- | ---: | ---: | ---: | ---: |
| Median turn | 84.2 s | 90.8 s | 32.4 s | 18.9 s |
| Slowest tenth | 147.7 s | 131.1 s | 166.9 s | 35.4 s |
| Output tokens, median | 2,452 | 2,784 | 4,275 | 3,562 |
| Of which reasoning | 2,127 | 2,631 | | |
| Tool calls per turn | 5.5 | 4.0 | 7.0 | 2.8 |
| Cost, whole side | $0.10 | $0.07 | | |

**On GLM the Project is not faster.** The skill runs at 0.93 times the Project's median, where Claude's Project was 1.7 times faster. GLM's Project opens its knowledge documents 4 times per turn, against Claude Project's 2.8, and that reading is what the speed advantage used to skip.

**GLM is about 2.5 to 5 times slower per turn at the median**, with most of its output spent on reasoning. Twelve Pi processes shared the gateway during the main run, so the ratio between twins is the reliable figure and absolute seconds are not.

---

## 5. VOICE

This system's own `lint_replies.py`, the same linter version run on both models' replies.

| | GLM skill | GLM Project | Claude Sonnet 5 skill | Claude Sonnet 5 Project |
| --- | ---: | ---: | ---: | ---: |
| Lint clean | 7 of 14 | 7 of 14 | 3 of 14 | 0 of 14 |

GLM writes cleaner than Sonnet 5 here, but half its replies still break the house rules. The misses are nearly all em dashes, 14 on the Project side and 13 on the skill side, plus semicolons.

---

## 6. OTHER THINGS THE RUN SHOWED

- **Every save was read back, and the reported count was usually wrong.** All 12 skill exports were read after writing. But the line count in `Verified: read-back succeeded; N lines` matched the file, within one line, in only 5 of 13 replies. `SID-001` reported 36 lines for a 53-line file, and `STK-001` reported 36 for 49. The read happens, and the number printed is not the one it returned
- **Nothing was written on the Project side.** The ledger is empty for every Project scenario, and no Project reply claims a save

---

## 7. THE ISOLATION LEAK, AND WHAT IT CHANGED

The first run's sandboxes sat beside each other. `SST-001` used `..` to read two sibling exports, and its PRD then carried a requirement nobody supplied, "Pause is available only for payouts in the pending state", matching a `SID-001` checklist item. `PST-001` grepped every sibling sandbox and the shared session folder.

Both were rerun under an operating-system sandbox that refuses anything outside the scenario's own folder. The profile was proved on a real Pi call, as the plan's section 3 records. The clean `SST-001` no longer carries the copied requirement, which confirms the leak had shaped the first result. Both verdicts stayed `PASS`, and both now rest on clean evidence. The leaked runs are kept in `failed-attempts/`.

No other Product Owner scenario made an out-of-sandbox call, so the remaining 12 stand as run.

---

## 8. NEXT STEPS

1. Sample `PTK-001` and `PBG-001` at five or more runs before concluding GLM's Project avoids the gaps Claude's showed
2. Sample the doc guide pair, the only one that falls short, to see whether its two different misses recur
3. Decide whether the wrong line counts in the read-back line matter. The playbook grades the read, not the number, so today nothing fails on it

---

## 9. FILES

| File | What it holds |
| --- | --- |
| `results.csv` | every verdict, with turns run, the gate flag and one line of quoted evidence |
| `grading-notes.md` | the grader's reasoning per scenario and every ambiguous call |
| `hvr-lint.csv` | the voice lint per reply |
| `skill/`, `claude project/` | per scenario: replies, transcripts, exports, raw events, timing |
| `failed-attempts/` | the two leaked story runs, the intermediate over-blocked rerun, and the verdicts before the rerun |

---

## 10. RE-MEASURED AFTER THE REPAIRS

Commit `9474bd7` made a promised source stop deferring the other Doc intake fields. `SDK-001` and `PDK-001` were rerun three times each on GLM through the sandboxed runner, in `remeasure/run-1` to `run-3`, and graded by a fresh reader in `remeasure/remeasure-grading.md`.

| Scenario | Before | After |
| --- | --- | --- |
| `SDK-001`, skill | PARTIAL, asked for the notes only | 2 PASS, 1 PARTIAL |
| `PDK-001`, Project | PARTIAL, asked for the notes only | 2 PASS, 1 PARTIAL |

No run asked for the notes alone any more.

**What is left:**
- **A rule conflict on shape.** `SDK-001` run 3 decided the shape rather than asking. The scenario's pass line requires turn 1 to ask about shape, while `doc-mode.md` Step 4 and Section 12 say to infer shape when the intended use is clear, so the rules disagree
- **Untraced claims.** The grader passed run 2 of each scenario while noting a claim that does not follow from the engineering notes: "Requeue only works from the failed queue" and "The Requeue action exists only there". The pass line requires every claim to trace to the notes, so read strictly those two runs fail, and the true count is 1 of 3 per side
- **Formatting.** `PDK-001` run 3 left no divider under one heading and added five empty spacer headings
