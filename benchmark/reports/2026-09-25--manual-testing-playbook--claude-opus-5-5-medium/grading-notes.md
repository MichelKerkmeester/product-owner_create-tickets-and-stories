# Grading notes, 2026-09-25, Product Owner, claude-opus-5-5 medium

Evidence behind every verdict in `results.csv`. Paths are relative to this folder unless they start with `sk-product-owner/`, `claude project/`, `AGENTS.md` or `benchmark/fixtures/`, which are relative to `AI Systems/Product Owner/`. Every source line cited refers to the Product Owner repo at `3023c5e`, the commit the run read, and root line numbers refer to the playbook root at that commit, version 2.0.0.0. Six Opus 5.5 graders drafted the evidence, one batch per folder group with both twins in the same batch. The orchestrator checked every draft against its evidence and read every FAIL a second time. Sections 5 to 10 are the graders' drafts: each draft row there shows the first reading, with `after_failed_gate` still unset, and `results.csv` holds the final row. Section 1 lists every row the operator's rulings changed.

---

## 1. How the rules were applied

**Verdict rule.** Root line 150: a turn that misses any Pass clause fails the scenario, even when no Fail example names the miss, and there is no verdict between `PASS` and `FAIL`. The scenario file's `- Pass/fail:` bullet is the fullest statement of the Pass clauses, and every clause in it was graded.

**Attachments are sources.** Anything an attached fixture states is supplied, exactly like anything the turns state (root section 2, Company context and attachments). An item counts as an addition only when it adds a capability, flow, message, validation rule, value, scope boundary or claim about current behavior that neither the turns nor the attachments contain. It counts as invented only when no naming line in the chat response covers it (root line 187). Items between the two readings are named as borderline and never decide a verdict alone.

**Skill read-back.** `AGENTS.md` line 46: verification passes only when Read returns non-empty content at the export path, and `N` is the final line number that Read returned. A Read of a line range after the last write counts, since it returns content. The Read tool numbers the empty line after a file's final newline, so a correct `N` is one more than `wc -l`. The runtimes printed either figure, and no verdict turns on it: the root fails no wrong count and no Pass clause asks for one (section 4).

**Project delivery.** Root line 163: a block counts as rendered when it sits in the reply as one delimited block. Commentary before a block is advisory except in `PID-001`.

**Format gate.** `node validate-output-format.cjs --system product-owner <file>`, run from the Claude Project Sync Loop folder on every skill export and on every Project block copied out of its reply. A gate finding decides a verdict only through a Pass clause or the Ticket realism item for a missing required section.

### Operator rulings of 2026-09-25 and the regrade

The graders' first reading gave skill 12 PASS and 11 FAIL, Project 8 PASS and 15 FAIL. The operator then ruled on every reading that could move a verdict. Each ruling below names the rows it changed. The counts in the README come from `results.csv` after these changes.

| Ruling | Rows changed |
| --- | --- |
| An explicit command (`$task`, `$bug`, `$doc`, `$story`, `$epic` and their aliases) always asks its question first. `AGENTS.md` line 287 and kernel line 108 win over `bug-mode.md` line 61, `story-mode.md` line 64 and `doc-mode.md` line 67, which get the exception `task-mode.md` line 50 already carries | None. The 18 early-draft FAILs stand, and the repaired sources are remeasured |
| `#### **References**` is optional in an Epic when no link is supplied, as the Story templates already say | `PEP-003` FAIL to PASS, `PIR-001` FAIL to PASS. `PEP-001` and `PEP-002` stay FAIL on the next ruling |
| A promise to write or save a file is a file claim on the Project side (root line 189, "any file claim at all") | `PID-001` PASS to FAIL (turn 1 line 44, "I'll write the task as `export/002 - task-due-today-filter-chip.md`"), `PIR-002` PASS to FAIL (turn 1 line 56, "will be a new file with the next number"). `PEP-001` (turn 1 line 37), `PEP-002` (turn 1 line 31) and `PTK-006` (turn 1 line 50) gain it as a reason. With `PID-001` failed, the other 22 Project rows carry `after_failed_gate` yes. `PBG-003` turn 1 line 34, "the bug report will take the next number in the bug lane", names no file and is recorded as borderline |
| `SDK-001` and `PDK-001` expected a Turn 1 question no rule requires, since the request carries no command and `doc-mode.md` line 67 asks only when purpose, audience, authority or scope cannot be established | None. Both stay FAIL against the scenario as it ran. The scenario is rewritten and both are remeasured |
| A cause labelled as an unverified hypothesis does not break "no root cause for either issue" | None. `SBG-003` stays PASS, and the scenario wording is clarified |
| "No error message is shown", written into the bug template's error slot with no source, is advisory | None. The template slot is repaired to read `Not provided` or be left out |
| A runbook's general "Expected result" lines drawn from incident INC-0412 are allowed | None. `SDK-002` and `PDK-002` stay PASS |

One reading was settled from the evidence without a ruling. `SDK-003` and `PDK-003` label Joana's interim plan `Status: Approved direction`. That is one of Doc Mode's own status classes, "accepted product direction that is not established as shipped behavior" (`sk-product-owner/references/doc-mode.md` line 146), and the thread shows Joana setting that plan while leaving the choice between the options open (`benchmark/fixtures/companies/loomlist/loomlist-sync-conflict-thread.md` lines 56 to 60). It is not an invented approval, so `SDK-003` stays PASS.

---

## 2. Report checker

`bash benchmark/grader/check_report.sh "benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium"`, run from `AI Systems/Product Owner/`, exits 2: both of its checks reported findings, and neither was unable to run.

**Reply lint** (`hvr-lint.csv`): 8 of 86 replies are clean and 78 carry a hard violation. The lint reads the whole reply, the delivered block included, and stays a separate axis from the verdicts, as in the earlier reports.

| Violation | Count | Replies |
| --- | ---: | ---: |
| `bullet_ends_with_full_stop` | 422 | 78 |
| `more_than_one_ellipsis` | 16 | 6 |
| `em_dash` | 14 | 5 |
| `copula:acts as` | 2 | 2 |
| `semicolon` | 2 | 2 |
| `copula:stands as` | 1 | 1 |

The ellipsis hits sit in Project Story and Epic replies, where Story Mode's fixed `TBD...` token in the three Delivery slots is exempt from the card. The em dashes sit in `PDK-001`, `PDK-003`, `PDK-004` and `SIR-001`. Most are the dash in a `**Term**` definition bullet or inside a `Status:` label, both of which kernel line 142 allows (`claude project/Custom Instructions.md`), and the rest follow links in Related references and Sources bullets, the way the Project Catalog template writes them.

**Twin divergence** after the regrade: 19 pairs agree and 4 differ, `DK-003`, `EP-002`, `ID-001` and `IR-002` (section 3).

---

## 3. Twins

Each disagreement was checked in the rule files on both sides.

| Pair | Skill | Project | Cause |
| --- | --- | --- | --- |
| `DK-003` | PASS | FAIL | Runtime fault. Both packagings say `$doc` and its alias still ask (`AGENTS.md` line 287, kernel line 108). The skill asked, and the Project wrote a status page on `$d` without asking |
| `ID-001` | PASS | FAIL | Rule gap on the Project side, now repaired. Kernel line 101 forbade claiming a file was saved but not promising one, and `PID-001` promised one |
| `IR-002` | PASS | FAIL | The same gap. `PIR-002` promised "a new file with the next number" |
| `EP-002` | PASS | FAIL | The same gap. `PEP-002` promised to "write the epic as the next file" |

Pairs that agree on FAIL share their cause:

- **`TK-002` to `TK-005`**: runtime fault in both. `task-mode.md` line 50 and its mirror already say `$task` still asks, yet both runtimes read "unless the request already contains enough direction" as leave to draft
- **`BG-002`, `ST-002` to `ST-004`**: rule gap in both packagings. The Bug and Story Mode lines let enough context stand in for the question and never carve out an explicit command
- **`EP-001`**: different causes. `SEP-001` drafted on `$epic`, which `AGENTS.md` line 287 did not list, and `PEP-001` asked but promised a file
- **`DK-001`**: scenario defect, per the ruling above
- **`TK-006`**: runtime fault in both. Neither task carries the plan's status word `deprecated` for `checkout_complete`, which the Pass clause lists verbatim

---

## 4. Findings recorded without a verdict change

| Finding | Where | Note |
| --- | --- | --- |
| `Verified:` printed with no Read of the file after its last write | `SBG-002` turn 1, `STK-003` both turns | Only `wc -l` or `sed` ran after the last edit. Both rows fail on Turn 1 drafting already |
| `N` printed as `wc -l` instead of the Read's final line number | `SBG-003` turn 2, `SDK-004`, `SEP-002` turn 2, `SEP-003`, `SIR-001` turn 2, `SIR-002` turn 2, `STK-005` | `AGENTS.md` line 46 names the Read's final line. No rule fails a wrong count |
| Turn 2 edited the Turn 1 file in place | The skill side of every early-draft FAIL | A consequence of drafting early: the file that should have been a clarification was already the artifact |
| "This morning" turned into `2026-09-25` | `SBG-002`, `PBG-002` | A date no turn or attachment gives. Both rows fail on Turn 1 drafting already |
| The sub-page open question reworded | `SST-002`, `PST-002` | The `**Open:**` line paraphrases `Do sub-pages inherit the link?`. Both fail on Turn 1 drafting already |
| The save-card draft stores the card brand, which `fernhouse-context.md` line 153 forbids | `SST-003`, `PST-003` | Both kept the company rule and marked the brand as open, so `facts_intact` is `no` for the draft's value. Both fail on Turn 1 already |
| The retry schedule dropped or reworded | `PTK-003` drops `1 min, 5 min, 15 min, 1 h, 6 h`, `STK-003` rewords `5 attempts` | Both fail on Turn 1 already |
| Size band exceeded | `SEP-001` 152 lines against 90 to 150, `SIR-002` 102 against 50 to 100 | Advisory |
| Format gate: prose connective density | `PEP-003` | 3.4 per 1000 words. Advisory |
| Format gate: em dashes after links and sources | `PDK-001` both turns, `PDK-004` turn 2 | No Pass clause covers them. Advisory |

---

## 5. Identity and interactive routing batch, grader draft

Run: `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/`. Model `claude-opus-5-5-medium`. Sources read from the working tree: `git -C "AI Systems/Product Owner" status --porcelain -- sk-product-owner "claude project" AGENTS.md benchmark/fixtures` printed nothing, and `git diff --stat 3023c5e HEAD` over the same paths is empty (HEAD `e9edb95` only adds the run), so every source line cited below is the line at `3023c5e`.

### Handover verdicts

- **SID-001 (skill handover): PASS**
- **PID-001 (Project handover): PASS**

Identity split greps, run from the workspace root against the Product Owner tree (both handover files expect exactly these):

| Grep | Expected | Observed |
|---|---|---|
| `grep -c "read-back succeeded" AGENTS.md` | `2`, exit `0` | `2`, exit `0` (lines 47 and 91) |
| `grep -c "read-back succeeded" "claude project/Custom Instructions.md"` | `0`, exit `1` | `0`, exit `1` |
| `grep -c "Canvas Artifact" AGENTS.md` | `0`, exit `1` | `0`, exit `1` |
| `grep -c "Canvas Artifact" "claude project/Custom Instructions.md"` | `4`, exit `0` | `4`, exit `0` (lines 76, 181, 221, 235) |

Neither handover reply carries the other runtime's wording: the SID-001 replies print `Path:` and `Verified: read-back succeeded` and never `Export-equivalent path:`, and the PID-001 replies print `Export-equivalent path:` and never `Path:`, `Saved:` or `Verified:` (root line 179).

### Tally

| Runtime | PASS | FAIL | SKIP |
|---|---:|---:|---:|
| skill | 3 (SID-001, SIR-001, SIR-002) | 0 | 0 |
| project | 2 (PID-001, PIR-002) | 1 (PIR-001) | 0 |

Every Project block was fenced (```` ```markdown ```` at reply line 1), with no text before it. Copies for the format gate are in `scratch/grades/blocks/identity-interactive/` and are byte-identical to the collector's copies under `AI Systems/Product Owner/export/benchmark/claude project/`. The skill exports in the run folder are byte-identical to `export/benchmark/skill/`.

---

### SID-001 (skill)

**Draft row**

```csv
SID-001,skill,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Handover PASS: both replies print Path:, the Verified: read-back succeeded line and HVR self-scan (turn-1.md lines 3 to 5, turn-2.md lines 3 to 5), each path has a Read after its last write, and the task keeps every Turn 2 fact with its additions named at turn-2.md lines 13 to 18. Advisory: the printed N sits one above wc -l on both files because Read numbered the empty line after the final newline."
```

**Pass clauses** (scenario line 35)

| Clause | Result | Evidence |
|---|---|---|
| Both replies name a readable `export/` path | Met | turn-1.md line 3 `export/001 - task-due-today-filter-chip-clarification.md`; turn-2.md line 3 `export/002 - task-due-today-filter-chip.md`; both files exist in `exports/export/` and each has a Read after its last write (read-back table) |
| Both print the `Verified: read-back succeeded` line | Met | turn-1.md line 4 `Verified: read-back succeeded; 16 lines`; turn-2.md line 4 `Verified: read-back succeeded; 50 lines` |
| Both print the `HVR self-scan:` line | Met | turn-1.md line 5, turn-2.md line 5 |
| Turn 1 file holds only the question under a `task` lane `-clarification` name | Met | name `001 - task-due-today-filter-chip-clarification.md`; file lines 1 to 15 are an H1, one framing sentence and six question paragraphs, no draft |
| Turn 2 file is a `task` on the next number | Met | `002 - task-due-today-filter-chip.md`, ledger in meta.json shows only this file created on turn 2 |
| Carries its H1, `### About` and `### Requirements` | Met | export line 1 `# FE - Web - TODO - Due today filter chip`, line 3 `### About`, line 13 `### Requirements` |
| Turn 2 facts intact | Met | Web only, apps out of scope (line 9); directly after Overdue (line 25); not checked off, due today in the to-do owner's time zone (line 27); sorted by due date (line 29); one chip active at a time (line 30); `filter_selected` with `filter` set to `due_today` (line 47); Yara and the tracking plan (line 43); no Figma, existing chip (line 21) |
| No invented fact or unfilled slot | Met | additions named in turn-2.md lines 13 to 18 (empty list, six locales, other-zone note, existing values, same look); `All` default from loomlist-context.md line 163, event properties from line 187, owner-zone display from line 157; no slot in the task |
| Fail: `Export-equivalent path:`, Canvas Artifact, or a no-file claim | Not hit | neither reply carries any of them |
| Fail: Turn 1 drafts the task | Not hit | turn-1.md line 1 `I haven't written the task yet` and the file is questions only |
| Fail: iOS or Android scoped, "Due today" renamed, owner's time zone dropped | Not hit | line 9 puts iOS and Android out of scope; label `Due today` throughout; owner's time zone at lines 11 and 27 |

**Blocking items hit:** None.

**Advisory items**

- Turn 1 reply also prints the questions in chat (turn-1.md lines 9 to 14). Not graded either way (root line 156).
- Borderline, not decisive: export line 43 `so client work can start without another Data review` extends the supplied `which Yara has already added to the tracking plan` against loomlist-context.md line 191. It could read as an approval status the turns do not state.

**Read-back table**

| Turn | Export path | N printed | Read after the last write, lines returned | Real `wc -l` |
|---|---|---:|---|---:|
| 1 | `export/001 - task-due-today-filter-chip-clarification.md` | 16 | Write at events-turn-1.jsonl line 28, Read at line 34, result line 35: lines 1 to 16, totalLines 16 | 15 |
| 2 | `export/002 - task-due-today-filter-chip.md` | 50 | Write line 18, Read line 20 (1 to 48), Edit line 25 (last write), Read line 27 offset 34, result line 28: lines 34 to 50, totalLines 50 | 49 |

N matches the final line number Read returned on both turns, as `AGENTS.md` line 46 defines it. Line 16 and line 50 are the empty line after the trailing newline.

**Realism entries**

- `export/001 - task-due-today-filter-chip-clarification.md`, task-lane clarification. Required content is the question alone (`references/interactive-mode.md` line 97): present. Facts checked: chips All, Assigned to me and Overdue, one active, All default (line 3 vs loomlist-context.md line 163); todos-service owns the To-dos view queries (line 9 vs line 69); six shipped locales with en-US fallback (line 11 vs line 155); `filter_selected` values and the Data team review before client work (line 13 vs lines 189 and 191). Placeholder: `{Title}` inside the quoted title pattern `FE - Web - TODO - {Title}` (line 5), which is the pattern from loomlist-context.md line 104, inside a question. 15 lines, no size band. Format gate: passed.
- `export/002 - task-due-today-filter-chip.md`, task. Title, `### About`, `### Requirements` (task-mode.md lines 72 to 78): all present. Facts checked: Desktop gets a web change with no Desktop release (line 9 vs loomlist-context.md line 18); Overdue and due dates use the owner's time zone (line 11 vs line 157); event carries `workspace_id`, `user_id`, `platform`, `app_version`, `plan` (line 48 vs line 187); six locales, en-US fallback (line 33 vs line 155); `TODO` is the feature code (line 1 vs line 120). Placeholder: none. 49 lines against the 30 to 70 band: inside. Discipline code: `FE`. Format gate: passed.

**Open readings**

1. Is `N` the final line number Read returns even when that line is the empty line after a trailing newline (16 and 50 here), or the file's line count (`wc -l` 15 and 49)? The verdict does not depend on it.
2. Does `so client work can start without another Data review` (export line 43) count as an invented approval, or as a direct reading of the Turn 2 sentence plus loomlist-context.md line 191? Recorded as borderline, it did not decide the verdict.

---

### PID-001 (project)

**Draft row**

```csv
PID-001,project,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Handover PASS: both replies open with a fenced block, then Export-equivalent path: in the task lane (turn-1.md line 30 with the -clarification name, turn-2.md line 61) and the HVR self-scan line, with no Path:, Saved: or Verified: line and no save claim, and the task keeps every Turn 2 fact. Advisory: turn-1.md line 44 says ""I'll write the task as"" the next export-equivalent name, a forward statement rather than a save claim."
```

**Pass clauses** (scenario line 35)

| Clause | Result | Evidence |
|---|---|---|
| Both replies open with their rendered block | Met | turn-1.md line 1 and turn-2.md line 1 open ```` ```markdown ````; closing fences at turn-1.md line 28 and turn-2.md line 59. Form: fenced, nothing before it |
| Report `Export-equivalent path:` with a `task` lane name | Met | turn-1.md line 30 `export/001 - task-due-today-filter-chip-clarification.md`; turn-2.md line 61 `export/002 - task-due-today-filter-chip.md` |
| `-clarification` name on Turn 1 | Met | turn-1.md line 30 |
| Print the `HVR self-scan:` line | Met | turn-1.md line 32, turn-2.md line 63 |
| Neither reply claims a file was saved, written or read back | Met | no `Path:`, `Saved:`, `Verified:` or read-back wording in either reply; meta.json ledger empty on both turns; turn-1.md line 36 `I read context/loomlist-context.md` is a read of the attachment, not a delivery claim; turn-1.md line 44 is forward tense (Open readings) |
| Turn 1 block holds only the question | Met | turn-1.md lines 2 to 27: the Task Format Question sections (Format & scope, Requirements, Design & platform, Analytics, Dependencies, Validation), no draft |
| Turn 2 task carries its H1, `### About` and `### Requirements` | Met | turn-2.md line 2 `# FE - Web - TODO - Due today filter chip`, line 4 `### About`, line 12 `### Requirements` |
| Turn 2 facts intact | Met | Web, apps later and out of scope (line 10); directly after Overdue (line 24); not checked off, due today in the owner's time zone (line 41); sorted by due date (line 43); one chip active at a time (line 26); `filter_selected` with `filter` set to `due_today` (line 56); existing chip (lines 20 and 25) |
| No invented fact or unfilled slot | Met | additions named at turn-2.md lines 77 to 84 (user-value line, empty list, translations, Desktop check, no due date, event properties); hashed `user_id` and web build as `app_version` from loomlist-context.md lines 188 and 139; no slot |
| Fail: `Path:`, `Saved:`, `Verified: read-back succeeded`, any local save claim | Not hit | as above |
| Fail: a block missing or following other text | Not hit | both blocks start at line 1 |
| Fail: Turn 1 renders the task | Not hit | turn-1.md line 36 `$task still needs its intake answers before I draft anything` |
| Fail: iOS or Android scoped, "Due today" renamed, owner's time zone dropped | Not hit | line 10 puts iOS and Android out of scope; `Due today` throughout; owner's time zone at lines 10, 37 and 41 |

**Blocking items hit:** None.

**Advisory items**

- Commentary after the blocks is within the kernel's shape (label, HVR line, quality status, summary). No commentary precedes either block, so the PID-001 delivery-shape exception (root line 163) is not triggered.
- Asking for a fact an attachment states (root line 211), recorded only: turn-1.md line 14 asks whether the one-active-chip rule stays, which loomlist-context.md line 163 states.
- Borderline, not decisive: turn-2.md line 52 `so the client work does not wait on a Data review`, the same extension as SID-001 export line 43.

**Realism entries**

- Block `PID-001-turn1-block.md` (turn-1.md lines 2 to 27), task-lane clarification. Question alone: present. Facts checked: chips All, Assigned to me and Overdue (line 12 vs loomlist-context.md line 163); Overdue uses the to-do owner's time zone (line 10 vs line 157); todos-service owns the view queries (line 6 vs line 69); locales `en-US, de-DE, fr-FR, es-ES, ja-JP and pt-BR` (line 18 vs line 155); personas Dana, Theo, Mireille (line 9 vs lines 40 to 42). Placeholder: none. 26 lines, no band. Format gate: passed.
- Block `PID-001-turn2-block.md` (turn-2.md lines 2 to 58), task. Title, `### About`, `### Requirements` (Project Task Mode knowledge lines 52 to 58): all present. Facts checked: Desktop picks up web changes with no Desktop release (line 29 vs loomlist-context.md line 18); owner's time zone, not the viewer's (line 37 vs line 157); event properties with hashed `user_id` (line 57 vs lines 187 and 188); web build number in place of a version (line 57 vs line 139); en-US fallback (line 28 vs line 155). Placeholder: none (`TODO` is the feature code, line 120). 57 lines against 30 to 70: inside. Discipline code: `FE`. Format gate: passed.

**Open readings**

1. turn-1.md line 44 `When you reply, I'll write the task as export/002 - task-due-today-filter-chip.md`: does a forward-tense statement naming a concrete export number count as a file claim under `Custom Instructions.md` lines 101 and 233? Graded as not a claim, because nothing is claimed as saved, written or read back.
2. Same Data review extension as SID-001 (turn-2.md line 52).

---

### SIR-001 (skill)

**Draft row**

```csv
SIR-001,skill,claude-opus-5-5-medium,PASS,2,2,pending,yes,"An energy-first intake question saved and read back as 001 - intake-guest-loyalty-points-clarification.md, then 002 - Epic-guest-loyalty-points.md with every Epic section including References, the four child stories, 19%, 25%, 12 months and 2027 intact, Pay now only and the additions named at turn-2.md lines 11 to 15. Advisory: the format gate flags clarification line 17 (importance assertion), and the Turn 2 reply printed N 103 where its last Read ended at line 104."
```

**Pass clauses** (scenario line 35)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question whose first item is the energy choice | Met | clarification lines 5 to 7 `**0. How should I work this?**` Quick / Deeper, first item |
| Asks for the deliverable type | Met | clarification lines 9 to 15: Doc (Proposal), Epic, Story, or a smaller discovery task |
| Saves it alone under an `intake` `-clarification` name | Met | `001 - intake-guest-loyalty-points-clarification.md`; body is the question only |
| Reads it back | Met | Read at events-turn-1.jsonl line 59 after the last Edit at line 57, lines 1 to 35 |
| Turn 2 saves an `Epic` on the next number | Met | `002 - Epic-guest-loyalty-points.md`; turn-2.md line 1 names the kind Epic |
| About, Problem, Goal, Solution, Scope and Acceptance criteria | Met | export lines 4, 9, 18, 27, 41, 63 (References at line 37 as well) |
| The four child stories | Met | lines 47, 51, 55, 59, plain text in Story H1 shape |
| The answer's numbers verbatim | Met | `19%` and `12 months` (line 11), `19%`, `25%`, `12 months`, `end of 2027` (line 20) |
| Spending limited to Pay now | Met | line 33; criterion 4 lines 94 to 99 |
| No invented fact or unfilled slot | Met | additions named at turn-2.md lines 11 to 15 (signed-in joining, cancelled stay, same membership across platforms, spent points in history); point value and funding left undecided (line 35); no slot |
| Fail: Turn 1 picks a kind or drafts | Not hit | four options offered, no draft (turn-1.md line 1) |
| Fail: export skipped, second round, export word not `Epic` | Not hit | both exports present; Turn 2 asks nothing |
| Fail: point value or funding source stated; balance, tiers or member-only prices described as current | Not hit | line 11 states Roamstay has no scheme, tiers or member-only prices, as roamstay-context.md line 170 does |

Kind and energy on Turn 2: kind Epic, as picked. The Deeper choice is not stated in the reply, and the Epic carries no energy header (correct under root line 191). It is written with every section and no Delivery close (not asked for), which fits a Deeper pass. The Pass clause does not grade energy.

**Blocking items hit:** None.

**Advisory items**

- Format gate on the clarification: `001 - intake-guest-loyalty-points-clarification.md:17: importance assertion, the sentence says only that something matters`, the heading `**2. Why it matters**`. That is a conciseness cut rule (`references/conciseness.md` line 73), not an HVR hard blocker, so the reply's `0 hard blockers` count is not contradicted. The Comprehensive Question template itself asks `Why does this matter?` (`assets/interactive-response-templates.md` line 73). It touches no Pass clause.
- Commentary: turn-2.md line 7 reports that the sync loop gate directory is missing from the sandbox and the format was checked by hand. This is true of the sandbox, noise in a delivery reply.
- Borderline, not decisive: export line 15 `81% of guests do not book a second stay on Roamstay within 12 months` is the complement of the supplied `19%`, not a stated number. Criterion 4 line 98 `the total charged and their balance both reflect it` reads as a direct test of spending at checkout.

**Read-back table**

| Turn | Export path | N printed | Read after the last write, lines returned | Real `wc -l` |
|---|---|---:|---|---:|
| 1 | `export/001 - intake-guest-loyalty-points-clarification.md` | 35 | Write line 41, Read line 43, Edits lines 53, 55, 57 (last), Read line 59, result line 60: lines 1 to 35, totalLines 35 | 34 |
| 2 | `export/002 - Epic-guest-loyalty-points.md` | 103 | Write line 40, Read line 42 (1 to 104), Edits lines 49 and 51 (last), Bash `wc -l` line 53 printed 103, Read line 55 offset 95, result line 56: lines 95 to 104, totalLines 104 | 103 |

Turn 2 printed the `wc -l` count (103), not the final line number Read returned (104), which is the value `AGENTS.md` line 46 names. Recorded, not failed.

**Realism entries**

- `export/001 - intake-guest-loyalty-points-clarification.md`, intake clarification. Question alone: present, energy first. Facts checked: no loyalty or points scheme, no tiers or member-only prices (line 11 vs roamstay-context.md line 170); booking with an email address only (line 24 vs line 27); payout after commission (line 25 vs line 50); five currencies (line 26 vs line 118); epic title shape `Epic - Guest - Loyalty` (line 13 vs line 85). Placeholder: none. 34 lines, no band. Format gate: failed, 1 error at line 17 (above).
- `export/002 - Epic-guest-loyalty-points.md`, Epic. Skill Epic scaffold (`assets/epic-template.md` lines 40 to 113, `references/story-mode.md` line 206): About, Problem with issues, Goal with `Direct user/Roamstay benefits`, Solution, References, Scope, Acceptance criteria all present; Added Later is optional and Delivery opt-in, both absent. Facts checked: Guest app on iOS, Android and web (line 6 vs roamstay-context.md lines 13 and 17); no scheme, tiers or member-only prices (line 11 vs line 170); Pay now and Pay at property (lines 33, 97 to 99 vs lines 45 and 46); epic title shape (line 1 vs line 85); child story titles in story shape (lines 47 to 59 vs line 85). Placeholder: none. 103 lines against 60 to 120: inside. No discipline code applies. Format gate: passed.

**Open readings**

1. Turn 2 N is 103 while the last Read ended at line 104. Is a count taken from `wc -l` an acceptable `N`, given `AGENTS.md` line 46 names the Read's final line number?
2. Should the format gate's importance-assertion rule fire on a clarification heading that follows the template's own `Why does this matter?` wording? Only evidence here.

---

### PIR-001 (project)

**Draft row**

```csv
PIR-001,project,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 and every Pass clause are met, but the Epic block drops the #### **References** heading, which the Project Epic Template (lines 53 to 59) and Story Mode knowledge line 182 carry without marking it optional: a required-section miss under Ticket realism (root line 205). Open reading: if {Supplied links only.} lets an Epic omit References when no links were supplied, this row is PASS."
```

**Pass clauses** (scenario line 35)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question whose first item is the energy choice | Met | turn-1.md lines 6 to 8 `**0. How should I work this?**`, first item |
| Asks for the deliverable type | Met | turn-1.md lines 10 to 14: Doc (proposal shape), Epic, Story, something else |
| Renders it alone as its own block | Met | fenced, turn-1.md lines 1 to 44, nothing before it; question only |
| `Export-equivalent path:` under an `intake` `-clarification` name | Met | turn-1.md line 46 `export/001 - intake-guest-loyalty-points-clarification.md` |
| Turn 2 renders an `Epic` block with its label | Met | fenced, turn-2.md lines 1 to 96; line 98 `export/002 - Epic-guest-loyalty-points.md`; line 102 `This is an Epic` |
| About, Problem, Goal, Solution, Scope and Acceptance criteria | Met | turn-2.md lines 5, 10, 19, 28, 38, 54 |
| The four child stories | Met | lines 44, 45, 49, 50 |
| The answer's numbers verbatim | Met | `19%` and `12 months` (line 12); `12 months`, `19%`, `25%`, `end of 2027` (line 21) |
| Spending limited to Pay now | Met | line 34; criterion 4 lines 86 to 91 |
| No invented fact or unfilled slot | Met | additions named at turn-2.md lines 110 to 114; point value and funding undecided (line 36); borderline items below; no slot |
| No file claim on either turn | Met | no `Path:`, `Saved:` or `Verified:`; ledger empty; turn-1.md line 56 `the draft will be numbered 002` claims no file |
| Fail: kind picked or artifact rendered before the answer, block skipped, second round, label word not `Epic`, saved file claimed | Not hit | as above |
| Fail: point value or funding source stated; balance, tiers or member-only prices described as current | Not hit | line 12 states there is no scheme, no tiers and no member-only prices |

Kind and energy on Turn 2: kind Epic, as picked; turn-2.md line 102 `drafted in full depth` acknowledges the Deeper choice. No energy header in the block.

**Blocking items hit**

- **A required section of the routed template missing** (Ticket realism, root line 205). The Project Epic Template scaffold carries `#### **References**` between Solution and Scope (`Product Owner - Assets - Epic Template - v0.100.md` lines 53 to 59, slot text `{Supplied links only.}`), and `Product Owner - Templates - Story Mode - v0.402.md` line 182 lists it in the Epic shape: `### Problem`, `### Goal` (with direct benefits), `### Solution`, `#### **References**`, then `## Scope`. Neither marks it optional. The template marks only `#### Added Later` optional (Notes line 99) and the Delivery close opt-in (line 108). The block goes from Solution (turn-2.md lines 28 to 36) straight to `## Scope` (line 38). By contrast, the Project Story Template says `Omit the whole section when none are supplied` (line 47), and the Epic Template has no such sentence. The runtime read the Epic Template on this turn (events-turn-2.jsonl line 5) and the reply acknowledges the gap: `There are no reference links because you didn't send any` (line 102). This item decides the verdict; the scenario's own Pass clause does not list References (Open readings).

**Advisory items**

- Borderline, not decisive: Problem line 16 `Neither Account nor checkout recognises a returning guest, so a repeat booking looks and costs the same as a first one` is a claim about current behavior that roamstay-context.md line 170 supports only in part (no tiers or member-only prices). Solution line 31 and criterion 1 line 61 `signed-in guest` are not named as an addition (the skill twin names it). History of points `earned and spent` (lines 33 and 81) is also unnamed but follows from the supplied spending.
- Asking for a fact an attachment states: none found.

**Realism entries**

- Block `PIR-001-turn1-block.md` (turn-1.md lines 2 to 43), intake clarification. Question alone: present, energy first. Facts checked: no scheme, tiers or member-only prices (line 4 vs roamstay-context.md line 170); email-only booking (line 31 vs line 27); five currencies with no conversion (line 32 vs line 118); free cancellation deadline (line 33 vs line 42); Partner Hub and Back office surfaces (line 28 vs lines 14 and 15); no loyalty feature code (line 38 vs lines 89 to 98). Placeholder: none. 42 lines, no band. Format gate: passed.
- Block `PIR-001-turn2-block.md` (turn-2.md lines 2 to 95), Epic. Project Epic Template sections: About, Problem, Goal with `Direct user/Roamstay benefits`, Solution, Scope, Acceptance criteria present; **`#### **References**` missing**; Added Later optional, Delivery opt-in, both absent. Facts checked: Guest app on iOS, Android and web (line 7 vs roamstay-context.md line 13); no scheme, tiers or member-only prices (line 12 vs line 170); Pay at property guests pay the property (line 34 vs line 46); epic title shape (line 2 vs line 85); child story titles in story shape (lines 44 to 50 vs line 85). Placeholder: none. 94 lines against 60 to 120: inside. No discipline code applies. Format gate: passed (the gate does not check Epic sections).

**Open readings**

1. **Decisive.** Is `#### **References**` required in an Epic when no links were supplied? The Epic Template slot reads `{Supplied links only.}` with no omit sentence, and Story Mode knowledge line 182 lists it in the Epic shape. The Story Template says `Omit the whole section when none are supplied`, and the scenario's Pass clause (line 35) and Expected step 4 (line 62) list the Epic sections without References. Graded by the template text as required, so FAIL. If the operator reads the slot as permission to omit, PIR-001 is PASS.
2. Does Problem line 16 (`Neither Account nor checkout recognises a returning guest`) count as a claim about current behavior that no attachment supplies? Borderline, not decisive.

---

### SIR-002 (skill)

**Draft row**

```csv
SIR-002,skill,claude-opus-5-5-medium,PASS,2,2,pending,yes,"One consolidated intake question naming the Bug and the Story, saved and read back, then a Story on 002 with preamble, About, Problem, Solution, Expected outcomes, Requirements and Acceptance criteria, 50 items and the keep-the-50-most-recent rule verbatim, the device and account facts as attached, and the dedupe addition named at turn-2.md line 9. Advisory: the body is 102 lines against the 50 to 100 band, and N 102 differs from the Read's final line 103."
```

**Pass clauses** (scenario line 35)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question that names both detected deliverables and asks for one | Met | clarification line 3 `I detected two deliverables, a Bug ($bug) and a Story ($story). Please choose one`; line 11 `**1. Deliverable:** Story, Epic or Bug?`; fields per choice at lines 13 to 21 |
| Saves it alone under an `intake` `-clarification` name | Met | `001 - intake-wishlist-cross-device-clarification.md`; no draft. Line 5 states a lean (Open readings) |
| Reads it back | Met | Read at events-turn-1.jsonl line 45 after the last Edit at line 43, lines 1 to 25 |
| Turn 2 saves a `Story` on the next number | Met | `002 - Story-wishlist-saved-to-account-in-apps.md`; turn-2.md line 1 names the kind Story |
| Preamble, About, Problem, Solution, Expected outcomes, Requirements, Acceptance criteria | Met | export lines 4 to 5, 7, 13, 28, 32, 39, 61 |
| Turn 2 values verbatim | Met | signed-in customers on iOS and Android (line 41); account list web shows (line 44); first sign-in move (line 48); `50 items` and the `50` most recently added (line 49); limit unchanged (line 53); no-account device wishlist as today (line 57) |
| Device and account facts as the attachments state them | Met | line 15 `In the apps the wishlist is saved on the device, and on web it is saved to the account` (fernhouse-context.md line 146); line 11 `a change to how the apps were built, not a defect fix` |
| No invented fact or unfilled slot | Met | dedupe named at turn-2.md line 9; CS numbers from fernhouse-wishlist-feedback.md lines 7, 11 to 17, 21 and 35; Lotte as Head of Product from fernhouse-context.md line 3; borderline items below; no slot |
| Fail: Turn 1 picks or drafts, export skipped, second round, word not `Story` | Not hit | as above |
| Fail: a Turn 2 value dropped or changed; apps ever saved to the account; web changed; device-only wishlist called a defect | Not hit | all values present; web keeps the account list (line 44); line 11 says not a defect |

Kind and energy on Turn 2: kind Story, as picked. The Quick choice is not stated in the reply, and the Story has no energy header. It stays in the lean Story shape with no Delivery close. The Pass clause does not grade energy.

**Blocking items hit:** None.

**Advisory items**

- Size band: 102 lines against 50 to 100, two over (root line 209).
- Borderline, not decisive: line 36 `373 of the 412` is the sum of three supplied counts and not itself supplied. Line 11 `signed off the direction on 2026-09-24` resolves the supplied `yesterday` against the session date. The reply mentions the date (turn-2.md line 7) but does not say it was worked out.
- Criterion blocks omit the `* * *` above each Mark-as-done checkbox that the template shows (`assets/story-template.md` line 100). This is not a section, and the format gate passed.
- References is absent, as the Story Template directs when no links are supplied (`assets/story-template.md` line 66). Not a miss.

**Read-back table**

| Turn | Export path | N printed | Read after the last write, lines returned | Real `wc -l` |
|---|---|---:|---|---:|
| 1 | `export/001 - intake-wishlist-cross-device-clarification.md` | 25 | Write line 35, Read line 38, Edit line 43 (last), Read line 45, result line 46: lines 1 to 25, totalLines 25 | 24 |
| 2 | `export/002 - Story-wishlist-saved-to-account-in-apps.md` | 102 | Write line 26, Edit line 32 (last), Read line 42 offset 95, result line 43: lines 95 to 103, totalLines 103 | 102 |

Turn 2 printed 102, not the final line number Read returned (103). Recorded, not failed.

**Realism entries**

- `export/001 - intake-wishlist-cross-device-clarification.md`, intake clarification. Question alone: present, conflict line and per-choice fields. Facts checked: app on device, web on account (line 5 vs fernhouse-context.md line 146); Teun on 2026-09-22, nothing changed in 4.8.0 or 4.8.2 (line 5 vs fernhouse-wishlist-feedback.md lines 43 to 45); Lotte has not decided (line 5 vs feedback line 51); `50 items` (line 17 vs context line 146 and feedback line 21); `wishlist_item_added` (line 24 vs context line 161). Placeholder: none. 24 lines, no band. Format gate: passed.
- `export/002 - Story-wishlist-saved-to-account-in-apps.md`, Story. Skill Story scaffold (`assets/story-template.md` lines 40 to 104): preamble, About, Problem, Solution, Expected outcomes, Requirements (mandatory with hard values, line 113), Acceptance criteria present; References omitted as line 66 directs. Facts checked: `412`, `2026-07-01` to `2026-09-20`, third biggest tag after WISMO and returns (line 17 vs feedback line 7); 118 in July to 155 in September (line 17 vs feedback line 17); 171, 138, 64, 39 (lines 21 to 24 vs feedback lines 11 to 14); 23 with a complaint tag (line 17 vs feedback line 35); Lotte, Head of Product (line 11 vs context line 3); story title shape `Customer - Wishlist - ...` (line 1 vs context line 95). Placeholder: none. 102 lines against 50 to 100: two over (advisory). No discipline code applies. Format gate: passed.

**Open readings**

1. Clarification line 5 (`That makes the 412 contacts a gap in the design rather than a defect, so a bug report would have no expected behavior to cite`): is a stated lean inside the question file an answer to its own question (`references/interactive-mode.md` line 97) or a pick under the Fail clause? Graded Met, because the file still offers Story, Epic and Bug and waits.
2. Turn 2 N is 102 while the last Read ended at line 103 (same question as SIR-001).
3. Is a date resolved from `yesterday` against the session date (line 11) a derived value or an addition that needs naming?

---

### PIR-002 (project)

**Draft row**

```csv
PIR-002,project,claude-opus-5-5-medium,PASS,2,2,pending,yes,"A fenced intake block naming both deliverables with an intake -clarification label, then a Story block with every required section, the Turn 2 values verbatim, the device and account facts as the attachments state them, the named additions at turn-2.md lines 112 to 114 and no file claim. Advisory: Turn 1 leans toward Story while still asking (turn-1.md lines 11 and 52)."
```

**Pass clauses** (scenario line 35)

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question that names both detected deliverables and asks for one | Met | turn-1.md line 2 `You sent both $bug and $story. I can only produce one primary deliverable, so the first choice is which one.`; lines 18 to 22 Bug, Story, Epic with per-choice fields |
| Renders it alone as its own block | Met | fenced, turn-1.md lines 1 to 44, nothing before it; no draft. Line 11 states a lean (Open readings) |
| `Export-equivalent path:` under an `intake` `-clarification` name | Met | turn-1.md line 46 `export/001 - intake-wishlist-across-devices-clarification.md` |
| Turn 2 renders a `Story` block with its label | Met | fenced, turn-2.md lines 1 to 102; line 104 `export/002 - Story-customer-wishlist-account-wishlist-in-apps.md`; line 108 `I wrote this as a **Story**` |
| Preamble, About, Problem, Solution, Expected outcomes, Requirements, Acceptance criteria | Met | turn-2.md lines 5 to 6, 8, 14, 20, 24, 32, 56 |
| Turn 2 values verbatim | Met | `iOS` and `Android` (line 36); signed in (line 40); same list web shows (line 41); `50 items` (line 42); first sign-in move (line 46); `50` most recently added (line 47); no-account device wishlist as today (line 52) |
| Device and account facts as the attachments state them | Met | line 12 `The apps have saved the wishlist on the device since it first shipped, and web has always saved it to the account.` (fernhouse-wishlist-feedback.md line 45) |
| No invented fact or unfilled slot | Met | additions named at turn-2.md lines 112 to 114 (kept once, CS numbers and Teun's note, the sign-off date worked out from `yesterday`); all numbers match the feedback file; no slot |
| No file claim on either turn | Met | no `Path:`, `Saved:` or `Verified:`; ledger empty; turn-1.md line 56 is forward tense (Open readings) |
| Fail: an artifact picked or rendered, block skipped, second round, label word not `Story`, saved file claimed | Not hit | as above |
| Fail: a Turn 2 value dropped or changed; apps ever saved to the account; web changed; device-only wishlist called a defect | Not hit | line 12 `This is a change to how the product works, not a fix`; web unchanged |

Kind and energy on Turn 2: kind Story, as picked. Quick is not stated in the reply; no energy header. The Pass clause does not grade energy.

**Blocking items hit:** None.

**Advisory items**

- Turn 1 lean: turn-1.md line 11 `So far both sources describe the wishlist working as built` and line 52 `That makes this a change to how the product works, not a bug`. The block still offers Bug with its conditions and waits.
- Borderline, not decisive: line 12 `Nothing broke in 4.8.0 or 4.8.2` rewords Teun's `Nothing about it changed in 4.8.0 or 4.8.2` (feedback line 45). It does not contradict the source, and the reply names the note as taken from Teun's reply (line 114).
- References is absent, as the Project Story Template directs when no links are supplied (line 47). Not a miss.

**Realism entries**

- Block `PIR-002-turn1-block.md` (turn-1.md lines 2 to 43), intake clarification. Question alone: present, conflict line and per-choice fields. Facts checked: web on account with sign-in, app on device, 50 items (line 6 vs fernhouse-context.md line 146); Maud on 2026-09-21 with 412, 171, 138, 64, 39 (line 7 vs fernhouse-wishlist-feedback.md lines 3, 7, 11 to 14); Teun on 2026-09-22 (line 8 vs feedback line 43); Lotte has not answered (line 9 vs feedback line 51); accounts-service holds the web wishlist (line 43 vs context line 66). Placeholder: none. 42 lines, no band. Format gate: passed.
- Block `PIR-002-turn2-block.md` (turn-2.md lines 2 to 101), Story. Project Story Template sections (lines 21 to 85): preamble, About, Problem, Solution, Expected outcomes, Requirements (mandatory with hard values, line 94), Acceptance criteria present; References omitted as line 47 directs. Facts checked: `412`, `2026-07-01`, `2026-09-20`, third biggest after WISMO and returns (line 18 vs feedback line 7); 118, 139, 155 by month (line 18 vs feedback line 17); 171, 138, 64, 39 (line 18 vs feedback lines 11 to 14); 23 with a complaint tag (line 18 vs feedback line 35); Lotte, Head of Product (line 10 vs context line 3); story title shape (line 2 vs context line 95). Placeholder: none. 100 lines against 50 to 100: inside, at the top. No discipline code applies. Format gate: passed.

**Open readings**

1. turn-1.md line 56 `After you answer, the Bug, Story or Epic will be a new file with the next number`: is a forward-tense mention of a file a file claim on the Project side (`Custom Instructions.md` lines 101 and 233)? Graded as not a claim.
2. Turn 1 lean (lines 11 and 52), the same question as SIR-002 reading 1.

---

### Twin notes

- **SID-001 and PID-001: agree (PASS, PASS).** Both route `$task` to Task Mode and ask once before drafting (`AGENTS.md` line 287, `Custom Instructions.md` line 108), both deliver the clarification in the `task` lane, and both tasks keep every Turn 2 fact with the additions named. Each reply carries only its own runtime's delivery wording. Both extend `Yara has already added` into "no further Data review" (skill export line 43, Project turn-2.md line 52), a shared borderline item.
- **SIR-001 and PIR-001: differ (PASS, FAIL).** Cause: runtime fault. Both packagings carry the same Epic scaffold with `#### **References**` between Solution and Scope (skill `assets/epic-template.md` lines 72 to 78 and `references/story-mode.md` line 206; Project `Product Owner - Assets - Epic Template - v0.100.md` lines 53 to 59 and `Product Owner - Templates - Story Mode - v0.402.md` line 182). The skill kept the heading with `No designs or linked documents yet.` (export lines 37 to 39) and the Project dropped it. Both packagings share a rule gap underneath: the Story templates say `Omit the whole section when none are supplied` (skill `assets/story-template.md` line 66, Project Story Template line 47) and neither Epic template does, which is what leaves PIR-001's reading open. Everything else agrees: energy first, the deliverable type asked, the intake lane, the Epic kind, the numbers verbatim and Pay now only.
- **SIR-002 and PIR-002: agree (PASS, PASS).** Both name the Bug and the Story in one intake question and wait. Both also offer an Epic and lean toward Story in the question (skill clarification line 5, Project turn-1.md line 11) under the same rule on both sides (`references/interactive-mode.md` line 97, Interactive Mode knowledge line 74). Both omit References under the same Story Template omit sentence, and both name the kept-once dedupe as an addition. Differences are illustrative slugs and the skill's two-line overrun of the size band.

---

## 6. Tasks batch, grader draft

Batch `tasks`, twelve scenarios in six twin pairs: `STK-001..STK-006` (skill) and `PTK-001..PTK-006` (Project). Model `claude-opus-5-5-medium`. Graded read-only against the brief `scratch/grading-brief.md` and `scratch/root-at-run.md`.

### Conventions used in this draft

- `<RUN>` is `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/`. Skill evidence sits under `<RUN>/skill/<ID> - <slug>/`, Project evidence under `<RUN>/claude project/<ID> - <slug>/`. Every `replies/<ID>-turn<n>.txt` is byte-identical to its `turn-<n>.md` (checked with `diff -q`, no differences).
- "call N" means the Nth tool call in that turn's `events-turn-<n>.jsonl`, counted in stream order.
- `git -C "AI Systems/Product Owner" status --porcelain -- sk-product-owner "claude project" AGENTS.md benchmark/fixtures` printed nothing, so source and fixture lines are cited from the working tree, which equals `3023c5e`.
- Skill export line numbers are the file as it stands in `exports/export/`. Project line numbers are `turn-<n>.md` reply lines. Block copies for the format gate sit in `scratch/grades/blocks/tasks/<ID>-turn<n>-block<k>.md`, holding the text between the fence lines, so a block copy's line = reply line minus 1.
- Format gate: `node validate-output-format.cjs --system product-owner "<file>"` from the `AI Systems/z*Sync Loop` folder the brief names. All 11 skill export files and all 15 Project block copies printed `Product Owner output format validation passed across 1 artifact file(s)`.
- The Read tool counts the empty line after a trailing newline, so on every export in this batch the Read `totalLines` equals `wc -l` plus 1 (see OR-2).
- Every Project conversation had only `read`, `ls`, `grep`, `find` tools (meta.json), made no Write or Edit call, and every Project turn ledger is empty.

### Shared open readings

- **OR-1, the intake question on an explicit `$task` with full attachments.** `references/task-mode.md` line 50 opens "Ask one comprehensive question unless the request already contains enough direction" before "`$task` and `$bug` still ask their context-specific question and wait", and line 55 repeats the "unless the request already contains enough direction" clause. The Project mirror `Product Owner - Templates - Task Mode` line 30 carries the same sentence. `AGENTS.md` line 287 and `Custom Instructions.md` line 108 state the stricter reading only. The skill runtime cited the looser clause in its own narration: STK-004 turn 1 "Direction is sufficient from the brief and board page, so I'll draft rather than ask", STK-005 turn 1 "the parent gives enough to draft the Android subtask without asking first". PTK-004 turn 1 call 11 grepped `enough direction|already contains`. Graded by each scenario's Pass clause (Turn 1 asks and drafts no task). Question for the operator: does the "unless the request already contains enough direction" clause ever let an explicit `$task` skip its question, or is the scenario reading (an explicit command always asks) the intended one?
- **OR-2, which line count is `N`.** `AGENTS.md` line 46 and `SKILL.md` line 211 set `N` to "the final line number returned by Read". The Read tool reports one more line than `wc -l` on every file here. Most replies printed the Read total, STK-005 printed `wc -l`. No Pass clause in this batch makes the count a condition, so no verdict rests on it. Question: is `N` graded against the Read total or against `wc -l`?
- **OR-3, verbatim versus same value in other words.** STK-003 export line 34 writes "retries up to 5 more times, after 1 min, 5 min, 15 min, 1 h and 6 h" where the Pass clause asks for `5 attempts` and `1 min, 5 min, 15 min, 1 h, 6 h` verbatim. Graded by the text as Unmet. Question: does a hard value restated with the same numbers in different words count as verbatim?
- **OR-4, the `deprecated` status label.** STK-006 and PTK-006 describe the deprecation (fires until 2026-11-01, then `events-collector` drops it) but never print the plan's status word `deprecated`. The Pass clause says "`checkout_complete` marked `deprecated`" and Expected signals say the task "carries the plan's event names, statuses and properties verbatim". Graded by the text as Unmet, which alone decides both 006 verdicts. Question: does stating the status's definition count as marking it `deprecated`, or must the label appear?

---

### STK-001 | Quick copy task (skill)

**Draft row**

```csv
STK-001,skill,claude-opus-5-5-medium,PASS,1,1,pending,yes,"Turn 1 asked nothing and saved export/001 - task-free-shipping-banner-copy.md, read back by call 12 after the only Write (lines 1-40), with both new strings at export lines 23-24 against the current strings at line 7, thresholds at line 26 and Web, iOS and Android at line 25. Advisory: FS title with no surface segment, named at turn-1.md line 12, and N 40 against wc -l 39."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks no question | Met | `turn-1.md` lines 1-17 carry no question; T1 ledger created only `export/001 - task-free-shipping-banner-copy.md`, no clarification |
| Saves one task export under the `task` word | Met | meta.json T1 ledger `created: ["export/001 - task-free-shipping-banner-copy.md"]` |
| Read back | Met | call 11 Write, call 12 Read of the same path returned lines 1-40 |
| Reported with its path, the `Verified:` line and the `HVR self-scan:` line | Met | `turn-1.md` line 3 `Path:`, line 4 `Verified: read-back succeeded; 40 lines`, line 5 `HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.` |
| H1, `### About`, `### Requirements`, `**Checklist**` of `- [ ]` items | Met | export line 1 H1, line 3 `### About`, line 11 `### Requirements`, lines 21-27 and 35-39 `**Checklist**` with `- [ ]` items |
| Both new strings verbatim against the two current strings | Met | export line 7 quotes `Free shipping on orders over €50` and `Free shipping on orders over £45`; lines 23-24 quote `Free shipping over €50` and `Free shipping over £45` for the same markets (see Open readings) |
| Thresholds, markets and surfaces as `fernhouse-context.md` states | Met | line 26 "The threshold amounts stay €50 and £45"; line 23 NL, BE, DE, FR and line 24 UK; line 25 "Web, iOS and Android"; line 7 top of every web page and above the cart; fixture lines 20 and 126-132 |
| No character limit, date, tracking event or threshold logic without naming; no template slot or `figma-url` | Met | none in the export; the translation group (lines 29-39) is named at `turn-1.md` line 13 |

**Blocking items hit**: None.

**Advisory items**

- Title `FS - PROMO - Shorten the free-shipping banner copy` uses `FS` with no surface. `fernhouse-context.md` line 89 defines `FS` as one change across client and service, line 86 gives client work `FE`, and line 93 lets only back-end and data work drop the surface. The reply names the choice at `turn-1.md` line 12. Title codes are recorded, not graded (root line 212).
- Borderline unnamed claim: export line 7 "which pushes the page or cart content down and splits the one message customers need to read at a glance" is an inference from the supplied two-line wrap, not in `fernhouse-context.md`. Listed as borderline, decides nothing.
- Commentary after the path block is within bounds (root line 195).

**Read-back table**

| Turn | Export path | N printed | Read after last Write or Edit, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - task-free-shipping-banner-copy.md` | 40 | call 12 after Write call 11, lines 1-40 of 40 | 39 |

**Realism entry**

- `export/001 - task-free-shipping-banner-copy.md`, Quick Task (`assets/task-templates.md` line 260). Required core from `references/task-mode.md` lines 76-78: Title, `### About`, `### Requirements`, all present (lines 1, 3, 11). Two groups numbered `1.` and `2.` as line 292 requires.
- Company facts: current strings (line 7) match `fernhouse-context.md` line 20; banner placement (line 7) matches line 20; locales `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR` (line 37) match lines 128-131; English via the language switcher with the market currency (line 19) matches line 134; `PROMO` (line 1) matches line 103.
- Placeholders: none. Body 39 lines, inside the 20 to 45 band. Discipline code `FS` present, see Advisory.

**Open readings**

- The Pass clause says "both new strings appear verbatim against the two current strings", Expected signals read it as "as the replacements for", and section 3 Expected says "a `**Checklist**` whose `- [ ]` items quote" the new strings "against" the current ones. STK-001 has the current strings in About (line 7) and the new ones in the checklist (lines 23-24), paired by market. Graded Met on the Expected signals reading. Question: must each old and new pair sit in the same checklist item?
- OR-2 applies (N 40, `wc -l` 39).

---

### STK-002 | Design notes FE task (skill)

**Draft row**

```csv
STK-002,skill,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 drafted and saved export/001 - task-date-picker-stay-limits.md with no question (turn-1.md line 1, T1 ledger) and Turn 2 edited that file in place instead of saving on the next number. The limits, the five copy strings and every Turn 2 fact are intact at export lines 43-47, 77-91, 9, 13 and 180-182; advisory: 182 body lines against the 70 to 150 band."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question | Unmet | `turn-1.md` line 1 "I've written the FE task for the date picker stay limits and saved it" |
| Turn 1 saves it under a `task` lane `-clarification` name with path, `Verified:` and `HVR self-scan:` | Unmet | T1 ledger created only `export/001 - task-date-picker-stay-limits.md`; no `-clarification` file exists |
| Turn 1 drafts no task | Unmet | T1 call 9 Write of the full task, 165 lines |
| Turn 2 saves one `task` export on the next number | Unmet | T2 ledger `modified: ["export/001 - task-date-picker-stay-limits.md"]`, nothing created; `turn-2.md` line 1 "in the same file" |
| Read back and reported the same way | Met | T2 call 5 last Edit, call 6 Read of the same path returned lines 166-183; `turn-2.md` lines 3-5 |
| H1, `### About`, `### Requirements` with checklisted groups | Met | export lines 1, 3, 27; groups 1-9 each with `**Checklist**` (lines 41 to 178) |
| Stay limits exactly as the notes give them | Met | lines 43-47 (1 night, 30 nights, past days, 365 days check-in only, check-out may land past it), lines 54 and 61 (1 night to 14 nights, property page only at 59), line 48 and 60 (config and property details, never hard-coded); notes lines 15-20, 61 |
| Five copy strings exactly | Met | line 77 `Select check-in date`, 78 `Select check-out date`, 79 `Show prices`, 90 `Stays can be up to 30 nights`, 91 `This property has a 3-night minimum`; notes lines 24-28, 43 |
| Every Turn 2 fact | Met | line 9 one FE task for iOS, Android and web, Search squad, 8.13.0 train; line 13 search-service unchanged with its 30-night backstop; lines 180-182 QA on iOS, Android and web in `en-GB` and `en-US`; no parent block |
| No hard-coded limits, 365 on check-out, changed value, unnamed tracking, search-service or flexible-dates addition, invented frame link or template slot | Met | line 48, 60, 112 no hard-coding; line 47 check-out exempt; line 13 flexible dates, prices and tracking out; line 21 frame as plain text; `{max}`, `{n}`, `{count}` at lines 106-108 and 113 are quoted from notes lines 39-41 (exempt, root line 207) |

**Blocking items hit**

- Pass clauses missed on Turn 1 (asked nothing, drafted the task, no clarification) and on Turn 2 (no new number), root line 150. Side-effect ledger: Turn 1 created a task file where only a `-clarification` export is allowed (root line 106).

**Advisory items**

- Size band: 182 body lines against 70 to 150.
- Turn 2 addition "on desktop and on mobile web" (line 182) is named at `turn-2.md` line 9.
- Commentary after the path is within bounds.

**Read-back table**

| Turn | Export path | N printed | Read after last Write or Edit, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - task-date-picker-stay-limits.md` | 165 | last edit call 12 (Bash `sed -i`), call 13 Read returned lines 150-165 of 165 | not recoverable, file edited in Turn 2 (Read total 165) |
| 2 | `export/001 - task-date-picker-stay-limits.md` | 183 | last Edit call 5, call 6 Read returned lines 166-183 of 183 | 182 |

**Realism entry**

- `export/001 - task-date-picker-stay-limits.md` (final state), Canonical Task (`assets/task-templates.md` line 38). Title, `### About`, `### Requirements` present (lines 1, 3, 27).
- Company facts: 23 chats in August (line 7) match notes line 11; `SRCH` (line 1) matches `roamstay-context.md` line 91; en-GB fallback (line 115) matches context line 124; de-DE about 30% longer (line 116) matches context line 126; 3 nights Monday to Thursday (line 80) matches context line 38.
- Placeholders: none beyond the exempt copy-key slots. Body 182 lines against 70 to 150 (advisory). Discipline code `FE`.

**Open readings**: OR-1, OR-2.

---

### STK-003 | Long BE integration task (skill)

**Draft row**

```csv
STK-003,skill,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 drafted and saved the task with no question (turn-1.md line 1, T1 ledger) and Turn 2 edited export/001 in place. Neither turn Read the file after its last Edit (T1 call 10, T2 call 8), and `5 attempts` and the retry schedule are restated rather than verbatim at export line 34."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question | Unmet | `turn-1.md` line 1 "I've written the BE task for Joris" |
| Turn 1 saves a `task` lane `-clarification` with path, `Verified:` and `HVR self-scan:` | Unmet | T1 ledger created only `export/001 - task-label-webhook-fix.md` |
| Turn 1 drafts no task | Unmet | T1 call 7 Write, 125 lines |
| Turn 2 saves one `task` export on the next number | Unmet | T2 ledger modified `export/001 - task-label-webhook-fix.md`, nothing created |
| Read back and reported the same way | Unmet | T1: call 9 Read (lines 1-125) came before call 10 Edit; after it only call 11 Bash `wc -l` and `sed -n 83p`. T2: call 7 Read (lines 1-124) came before call 8 Edit; after it only call 9 Bash `sed -n '112,124p'` and `awk`. Reply lines 3-5 print path, `Verified:` and HVR on both turns |
| H1, About, Requirements with a checklisted group for each of the five points | Met | groups at lines 30, 48, 63, 80, 98, each with `**Checklist**` |
| Carrier values verbatim | Unmet | `event_id` lines 52, 56; `X-Carrier-Signature` and `HMAC-SHA256` line 38; `5 seconds` line 42. `5 attempts` absent, line 34 reads "retries up to 5 more times"; `1 min, 5 min, 15 min, 1 h, 6 h` absent, line 34 reads "after 1 min, 5 min, 15 min, 1 h and 6 h" (OR-3) |
| Thread values verbatim | Met | `7 days` line 57, `10 minutes` line 88, `30 minutes` and `#fulfilment-alerts` line 106, `more than 5` line 108 |
| Polling only kept out | Met | line 11 |
| Every Turn 2 fact | Met | line 13 no parent task, Fulfilment board, live before the November peak; line 41 warehouse call moved out, 8-second timeout kept; lines 122-123 the done definition word for word |
| No idempotency claim, `reference` dedupe, changed retry step, polling, answered open question, unnamed queue or vendor, invented cause, placeholder link | Met | line 67 no idempotency key, planned header with no date (notes line 18); line 76 carrier question kept open (notes line 72); causes match thread lines 21-27 |

**Blocking items hit**

- Pass clauses missed on Turn 1 (no question, task drafted), Turn 2 (no new number), read-back after the last edit, and two carrier values not verbatim, root line 150. Side-effect ledger: Turn 1 created a task file where only a `-clarification` is allowed (root line 106).

**Advisory items**

- Additions named at `turn-1.md` lines 10-17 (storage failure, repeat 200, open shipment definition, concurrent failures, GET path, rate limit, alert fields, verification group).
- Borderline: References lines 19-20 are markdown links to `../context/fernhouse-carrier-label-thread.md` and `../context/fernhouse-carrier-label-api-notes.md`, real files in the sandbox but paths no ClickUp reader can open.
- Size band: 123 lines, inside 110 to 220.

**Read-back table**

| Turn | Export path | N printed | Read after last Write or Edit, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - task-label-webhook-fix.md` | 125 | none: last Read call 9 (lines 1-125) precedes last Edit call 10; call 11 Bash printed `124` and line 83 | 124 at the time (call 11) |
| 2 | `export/001 - task-label-webhook-fix.md` | 124 | none: last Read call 7 (lines 1-124) precedes last Edit call 8; call 9 Bash printed lines 112-124 and `123` | 123 |

**Realism entry**

- `export/001 - task-label-webhook-fix.md`, Canonical Task. Title, About, Requirements present (lines 1, 3, 26).
- Company facts: 37 duplicate labels 14:10 to 15:50 (line 7) match thread line 9; €0.42 per label (line 9) matches thread line 17; 20 requests per second and 14 a second at cut-off (line 11) match thread line 45 and notes line 68; 7 hours 21 minutes (line 52) matches notes line 59; `FH-2291834-1` (line 71) matches notes line 16; `SHIP` and no surface match `fernhouse-context.md` lines 93 and 104.
- Placeholders: none. Body 123 lines, inside 110 to 220. Discipline code `BE`.

**Open readings**

- Does a Bash `sed -n` or `wc -l` after the last Edit count as the read-back the brief requires ("a Read of that exact export path")? Graded by the brief's text as not proven.
- OR-1, OR-2, OR-3.

---

### STK-004 | Parent task with subtasks (skill)

**Draft row**

```csv
STK-004,skill,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 saved a parent and four subtask files, 001 to 005, with no question (T1 ledger, turn-1.md line 1), and Turn 2 rewrote 001 in place while 002 to 005 stay in export/. The Turn 2 parent keeps every shared-rule value and Turn 2 fact (export lines 39-111, 121-151); advisory: 151 lines against the 60 to 130 band."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question | Unmet | `turn-1.md` line 1 "I wrote a parent task for recurring to-dos plus four subtasks" |
| Turn 1 saves a `task` lane `-clarification` with path, `Verified:` and `HVR self-scan:` | Unmet | T1 ledger created 001 to 005, all tasks, no clarification |
| Turn 1 drafts no task | Unmet | T1 calls 12-16 Write five task files |
| Turn 2 saves one parent `task` export on the next number | Unmet | T2 ledger modified `export/001 - task-recurring-todos-parent.md`, nothing created |
| Read back and reported the same way | Met | T2 call 1 Write, call 2 Read returned lines 140-152; `turn-2.md` lines 3-6 |
| H1, About, Requirements with one numbered entry each for iOS, Android, web and back end in plain text | Met | lines 121-151, entries 6 to 9 with backticked titles at lines 125, 133, 141, 149 |
| Shared rules with the brief's values | Met | table lines 39-45 (`Daily`, `Weekdays`, `Weekly`, `Monthly`, `Custom`, `1 to 99`); line 52 `Never`, `On date`, `After`; line 54 `365`; line 66 `Skip this one`; lines 95-96 `500` and the sheet copy; line 102 `recurring_todos`; lines 93-94 `Plus`; line 78 "to-do owner's time zone" (contains `owner's time zone`) |
| Every Turn 2 fact | Met | line 9 leads write their own subtasks, rules stated once and numbered; lines 102, 107, 127, 135 iOS and Android 5.4.0; lines 102, 143, 151 web and BE ship dark before it |
| No Desktop or Support console subtask, no invented link or `(url)` slot, no Repeat on Free, no changed range or copy, no check-off-date repeat or per-weekday time, activity question kept open | Met | line 143 Desktop through the web client; final parent has no links; line 94 Plus badge on Free; line 13 out of scope; line 115 still open |

**Blocking items hit**

- Pass clauses missed on Turn 1 (no question, parent and four subtasks saved) and Turn 2 (no new number), root line 150. Side-effect ledger: Turn 1 created five task files where only a `-clarification` is allowed (root line 106), and they remain after Turn 2 (`turn-2.md` line 16).

**Advisory items**

- File order and links: Turn 1 saved 001 parent, 002 iOS, 003 Android, 004 Web, 005 BE, in the prompt's order. The Turn 1 parent (call 12 content lines 116-138) linked each subtask file, and each subtask links the parent `<001 - task-recurring-todos-parent.md>` (002 to 004 line 25, 005 line 15) plus siblings (002 links only 005; 003 and 004 link 002 and 005; 005 links 002 to 004). All link targets exist. Turn 2 replaced the parent's links with plain titles, and now lists `BE - TODO - Recurring to-dos` (line 149) while the stale file 005 carries the H1 `BE - TODO - Recurring to-do occurrences, Ends and workspace limit`.
- Additions named at `turn-1.md` lines 25-26 (two BE edge cases in 005 lines 42-43, "to-do owner" wording). Borderline: 005 line 91 "Setting Repeat on another to-do in a workspace at 500 is refused" states server enforcement the brief implies (brief line 56, BE owns the 500 limit) but does not spell out.
- Size band: parent 151 lines against 60 to 130.

**Read-back table**

| Turn | Export path | N printed | Read after last Write or Edit, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - task-recurring-todos-parent.md` | 139 | last edit call 18 (Bash `sed -i`), call 19 Read lines 1-139 of 139 | 138 at the time (call 17); file rewritten in Turn 2 |
| 1 | `export/002 - task-recurring-todos-ios.md` | 100 | last edit call 18, call 20 Read lines 95-100 of 100 | 99 |
| 1 | `export/003 - task-recurring-todos-android.md` | 101 | last edit call 18, call 21 Read lines 96-101 of 101 | 100 |
| 1 | `export/004 - task-recurring-todos-web.md` | 102 | last edit call 18, call 22 Read lines 97-102 of 102 | 101 |
| 1 | `export/005 - task-recurring-todos-be.md` | 115 | last Write call 16, call 23 Read lines 110-115 of 115 | 114 |
| 2 | `export/001 - task-recurring-todos-parent.md` | 152 | Write call 1, call 2 Read lines 140-152 of 152 | 151 |

**Realism entries**

- `export/001 - task-recurring-todos-parent.md` (Turn 2 state), Parent Task (`assets/task-templates.md` line 165). Title, About, Requirements present (lines 1, 3, 25). Facts: 212 requests and 38 Plus workspaces (line 7) match brief line 8; 10% at 8 weeks (line 11) match brief line 47; three frames (lines 21-23) match brief line 58; mobile local notifications and in-app Web reminders (lines 82-83) match `loomlist-context.md` line 77; event properties (line 111) match context line 187; `FS` for a parent spanning platforms matches context lines 100 and 104. Placeholders none. 151 lines against 60 to 130. Code `FS`.
- `export/002 - task-recurring-todos-ios.md`, Subtask (line 214). Title, About, Requirements present (lines 1, 3, 33). Facts: hint `Add a due date to repeat` (line 46) matches brief line 12; 1 to 99 and 1 to 365 (lines 47, 49) match brief lines 20 and 27; local notification from the UTC time reminders-service hands over (line 84) matches context line 77; sheet copy (line 75) matches brief line 35. Placeholders none. 99 lines. Code `FE`, surface `iOS`.
- `export/003 - task-recurring-todos-android.md`, Subtask. Title, About, Requirements present (lines 1, 3, 34). Facts: scope "same as iOS" (line 7) matches brief line 54; frames (lines 17-19) match brief line 58; flag `recurring_todos` (line 9) matches brief line 45. Placeholders none. 100 lines. Code `FE`, surface `Android`.
- `export/004 - task-recurring-todos-web.md`, Subtask. Title, About, Requirements present (lines 1, 3, 34). Facts: Desktop gets it on next load with no Desktop release (line 7) matches context line 18; scope same as iOS (line 7) matches brief line 55; flag (line 9) matches brief line 45. Placeholders none. 101 lines. Code `FE`, surface `Web`.
- `export/005 - task-recurring-todos-be.md`, Subtask. Title, About, Requirements present (lines 1, 3, 25). Facts: reminders-service holds UTC due time and hands it to every device (line 99) matches context line 71; 500 not-ended series (line 89) matches brief line 35; owner's zone after reassign (line 79) matches brief line 39; After counts skips (line 66) matches brief line 31. Placeholders none. 114 lines. Code `BE`.

**Open readings**: OR-1, OR-2. Also: the FAIL list names "Turn 2 saves subtask files as well"; here Turn 1 saved them and Turn 2 left them in `export/`. Question: should subtask files surviving from an early Turn 1 draft count against the Turn 2 clause too? It does not change this verdict.

---

### STK-005 | Supplied parent subtask (skill)

**Draft row**

```csv
STK-005,skill,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 drafted and saved the Android subtask, saying no clarification was needed (turn-1.md line 1), and Turn 2 edited export/001 in place. The subtask names the supplied parent as plain text at export line 27 without rewriting it and keeps every value and Turn 2 fact; advisory: 164 lines against the 60 to 130 band."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question | Unmet | `turn-1.md` line 1 "No clarification was needed because the parent already names this subtask and its title" |
| Turn 1 saves a `task` lane `-clarification` with path, `Verified:` and `HVR self-scan:` | Unmet | T1 ledger created only `export/001 - task-android-recurring-todos-subtask.md` |
| Turn 1 drafts no task | Unmet | T1 call 11 Write, 162 lines |
| Turn 2 saves one `task` export on the next number | Unmet | T2 ledger modified 001, nothing created |
| Read back and reported the same way | Met | T2 calls 1-5 Edit, call 6 Read lines 1-165; `turn-2.md` lines 3-5 |
| H1, About, Requirements with checklisted groups | Met | lines 1, 3, 37; groups 1-9 each with `**Checklist**` |
| Parent named as `FS - TODO - Recurring to-dos` | Met | line 27 `` - `FS - TODO - Recurring to-dos` `` under `**Parent task**`, the no-link form of `assets/task-templates.md` line 159; `context/` untouched in both ledgers |
| Shared rules as the parent gives them | Met | line 55 `Daily`, `Weekdays`, `Weekly`, `Monthly`, `Custom`; line 67 `1 to 99`; lines 77-79 `Never`, `On date`, `After`, `365`; lines 108-110 `Skip this one`; lines 120 and 125 `500` and the sheet copy; lines 9 and 137 `recurring_todos`; line 9 "the owner's time zone" |
| Android as the only client in scope | Met | lines 7 and 9; iOS and Web appear only under Related tasks (lines 33-34) |
| Every Turn 2 fact | Met | line 7 phones and tablets, line 56 picker on both; line 9 Oskar's team, 5.4.0; line 11 BE builds the engine in parallel, the app shows the date BE returns and never works one out; lines 93-94, 109, 152 |
| No dropped or invented parent link, no iOS, web, Desktop or engine work, no device-side date logic, no changed option or copy, no unnamed Android addition, no template slot | Met | additions named at `turn-1.md` lines 12-16 and `turn-2.md` line 13 |

**Blocking items hit**

- Pass clauses missed on Turn 1 (no question, subtask drafted) and Turn 2 (no new number), root line 150. Side-effect ledger: Turn 1 created a task file where only a `-clarification` is allowed (root line 106).

**Advisory items**

- Borderline: line 97 pins the parent's "starts on the 31st" example to "31 March", a specialisation of parent line 69.
- Size band: 164 lines against 60 to 130.

**Read-back table**

| Turn | Export path | N printed | Read after last Write or Edit, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - task-android-recurring-todos-subtask.md` | 161 | Write call 11, call 13 Read lines 155-162 of 162 (call 12 Bash printed `161`) | 161 at the time |
| 2 | `export/001 - task-android-recurring-todos-subtask.md` | 164 | last Edit call 5, call 6 Read lines 1-165 of 165 | 164 |

**Realism entry**

- `export/001 - task-android-recurring-todos-subtask.md`, Subtask (`assets/task-templates.md` line 214). Title, About, Requirements present (lines 1, 3, 37).
- Facts: parent title (line 27) matches `loomlist-recurring-todos-parent-task.md` line 1; `BE - TODO - Recurrence engine` (line 35) matches parent line 49; Yara reviewed 2026-09-16 (line 158) matches parent line 109; phones and tablets (line 7) match `loomlist-context.md` line 15; event properties and `user_id` hashing (line 164) match context lines 187-188.
- Placeholders none. 164 lines against 60 to 130. Code `FE`, surface `Android`.

**Open readings**: OR-1, OR-2 (N 161 is `wc -l`, the Read total was 162).

---

### STK-006 | Data tracking task (skill)

**Draft row**

```csv
STK-006,skill,claude-opus-5-5-medium,FAIL,2,2,pending,no,"Turn 1 asked one consolidated question saved as export/001 - task-booking-funnel-events-clarification.md and Turn 2 saved 002 on the next number, both read back, but the task never marks `checkout_complete` as `deprecated`, only its 2026-11-01 removal (export lines 95, 111, 119). Borderline: Nadia is not named as the one who checks the events (export line 9)."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 routes to Task Mode | Met | clarification saved in the `task` lane, `export/001 - task-booking-funnel-events-clarification.md` |
| Turn 1 asks one question | Met | one consolidated clarification with seven numbered points (clarification lines 1-36), `AGENTS.md` line 283 |
| Saves it under a `task` lane `-clarification` name, reported with path, `Verified:` and `HVR self-scan:` | Met | call 11 Write, call 12 Read lines 1-37; `turn-1.md` lines 3-5 |
| Turn 1 drafts no task | Met | T1 ledger created only the clarification; the file holds questions only |
| Turn 2 saves one `task` export on the next number | Met | T2 ledger created `export/002 - task-booking-funnel-events.md`; clarification untouched |
| Read back and reported the same way | Met | Write call 1; call 2 Read at offset 125 returned no content; call 3 Read returned lines 110-122; `turn-2.md` lines 6-8 |
| H1, About, Requirements with checklisted groups | Met | lines 1, 3, 24; groups 1-5 each with `**Checklist**` |
| Six funnel events as the plan names them | Met | line 99 `search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted`, `booking_confirmed`; plan lines 19-24 |
| `booking_confirmed` from `booking-service` with `source` set to `server` | Met | line 76 |
| `total_amount_minor` in minor units | Met | line 64, city tax included, `51600` |
| `checkout_complete` marked `deprecated` with its removal on `2026-11-01` | Unmet | removal date at lines 95, 111, 119-120, but the word `deprecated` appears nowhere in the export (grep, no match); plan line 25 status `deprecated, removal on 2026-11-01` (OR-4) |
| `date_changed` kept `proposed` and unbuilt | Met | line 9 "stays out of scope because it is still proposed" |
| Every Turn 2 fact | Met, borderline | line 1 and 9 Data team's own task under `TRK`; line 9 checks in `events-collector` as the squads ship, dashboard move, collector drop on the removal date; lines 21-22 FE and BE tasks later; line 15 event table unchanged at the 2026-09-24 refinement. Nadia appears only as plan author (line 15), not as the one who checks |
| No `date_changed` build, no early or late `checkout_complete` drop, no booking count from `payment_submitted` or `checkout_complete`, no client `booking_confirmed`, no decimals, no FE or BE build inside the task, no slot | Met | lines 9, 100, 119-120, 64, 21-22 |

**Blocking items hit**

- Pass clause missed: `checkout_complete` not marked `deprecated`, root line 150, read under OR-4.

**Advisory items**

- Additions named at `turn-2.md` lines 20-22 (nights check line 60, no cross-currency sums line 102, no count gap line 121).
- `turn-2.md` line 13 settles the `booking_confirmed` trigger by the table's wording and says so; the task keeps plan line 55's Pay now and Pay at property triggers (lines 77-78). Not silent, not blocking.
- Clarification asks for no fact an attachment states. The reply does not print the question text in full, which is not graded (root line 156).
- Size band: 121 lines, inside 60 to 140.

**Read-back table**

| Turn | Export path | N printed | Read after last Write or Edit, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - task-booking-funnel-events-clarification.md` | 37 | Write call 11, call 12 Read lines 1-37 of 37 | 36 |
| 2 | `export/002 - task-booking-funnel-events.md` | 122 | Write call 1, call 3 Read lines 110-122 of 122 | 121 |

**Realism entries**

- `export/001 - task-booking-funnel-events-clarification.md`, task-lane clarification (`SKILL.md` line 208). Question only, no draft. Facts: draft v0.3 (line 3) matches plan line 1; refinement on 2026-09-24 (line 36) matches plan line 5; Pay now expiry after 30 minutes (line 16) matches `roamstay-context.md` line 148; three owners (line 7) match plan lines 75-77. Placeholders none. 36 lines, no band. No title code expected.
- `export/002 - task-booking-funnel-events.md`, Canonical Task. Title, About, Requirements present (lines 1, 3, 24). Facts: `RS-` plus six letters and digits (line 81) matches context line 47; `51600` (line 64) matches plan line 45; no currency conversion (line 102) matches context line 118; join on `session_id` (line 103) matches context line 181; `DATA` and `TRK` match context lines 80 and 97. Placeholders none. 121 lines, inside 60 to 140. Code `DATA`.

**Open readings**

- OR-4 decides this verdict.
- The Turn 2 fact is "Nadia checks every event in events-collector"; the task writes "This task checks each event" (line 9). Question: must the task name Nadia as the checker for that fact to survive?
- OR-2.

---

### PTK-001 | Quick copy task (Project)

**Draft row**

```csv
PTK-001,project,claude-opus-5-5-medium,PASS,1,1,pending,yes,"Turn 1 asked nothing and rendered one fenced task block (turn-1.md lines 1-29) with Export-equivalent path at line 31 and HVR at line 33, both string pairs in checklist lines 22-23, thresholds at line 28 and all three surfaces at line 24, and no file claim. Advisory: FE title with no surface segment, named at line 40; borderline unnamed scope item on position and styling at line 28."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks no question | Met | `turn-1.md` lines 1-43 carry no question |
| Renders one task block | Met | one fenced block, lines 1-29 (form: fenced ```` ```markdown ````), before any commentary |
| Reported with `Export-equivalent path:` under the `task` word | Met | line 31 `` Export-equivalent path: `export/NNN - task-free-shipping-banner-copy.md` `` (`NNN` as `Custom Instructions.md` line 223 writes it) |
| `HVR self-scan:` line | Met | line 33 |
| Claims no file | Met | no `Path:`, `Saved:`, `Verified:` or save claim in lines 31-43; empty ledger |
| H1, About, Requirements with `**Checklist**` of `- [ ]` items | Met | lines 2, 4, 10, 20-28 |
| Both new strings verbatim against the two current strings | Met | line 22 replace "Free shipping on orders over €50" with "Free shipping over €50"; line 23 the `£45` pair |
| Thresholds, markets and surfaces as the context states | Met | line 28 thresholds kept; lines 22-23 NL, BE, DE, FR and UK; line 24 web, iOS and Android; line 8 top of every web page and above the cart |
| No unnamed limit, date, event or threshold logic, no slot or `figma-url` | Met | additions named at lines 41-42 |

**Blocking items hit**: None.

**Advisory items**

- Title `FE - PROMO - Shorten the free-shipping banner copy` has no surface although `fernhouse-context.md` line 93 lets only back-end and data work drop it; named at line 40.
- Borderline unnamed items: line 28 "the banner's position and styling unchanged" adds a scope boundary the turn implies (copy change only) but does not state; line 8 "so the banner takes less space above the cart" is an inference. Neither decides a verdict.
- Commentary after the block within bounds.

**Realism entry**

- Block `blocks/tasks/PTK-001-turn1-block1.md` (reply lines 2-28), Quick Task (`Product Owner - Assets - Task Templates` line 241). Required core from Task Mode knowledge lines 54-58 present (lines 2, 4, 10). One unnumbered group as line 273 requires.
- Facts: current strings (lines 22-23) match `fernhouse-context.md` line 20; banner placement (line 8) matches line 20; locales (line 25) match lines 128-131; English via the switcher (line 26) matches line 134; `PROMO` matches line 103.
- Placeholders none. 27 lines, inside 20 to 45. Code `FE`.

**Open readings**: None beyond the STK-001 "against" question, which PTK-001 meets either way.

---

### PTK-002 | Design notes FE task (Project)

**Draft row**

```csv
PTK-002,project,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 rendered the full task block (turn-1.md lines 1-118) with no question and no -clarification label. The Turn 2 block keeps every limit, the five copy strings and every Turn 2 fact (turn-2.md lines 11-13, 41-58, 72-89, 121-130)."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question as its own block | Unmet | `turn-1.md` lines 1-118 are the task, no question |
| Under an export-equivalent `task` lane `-clarification` label with `HVR self-scan:` | Unmet | line 120 `export/001 - task-date-picker-stay-limits.md`, no `-clarification`; HVR at line 122 |
| Turn 1 renders no task | Unmet | lines 1-118 |
| Turn 2 renders one task block under an export-equivalent `task` label with `HVR self-scan:` and no file claim | Met | fenced block lines 1-131, line 133 `export/001 - task-date-picker-stay-limits.md`, line 135 HVR, no file claim (line 142 only says the filename is kept) |
| H1, About, Requirements with checklisted groups | Met | lines 3, 5, 25; groups 1-7 each with `**Checklist**` |
| Stay limits exactly as the notes give them | Met | lines 41-43, 53-58 |
| Five copy strings exactly | Met | lines 72, 73, 74, 85, 86 |
| Every Turn 2 fact | Met | line 11 one task for iOS, Android and web, Search squad, 8.13.0; line 13 search-service unchanged with its backstop; lines 129-130 QA in `en-GB` and `en-US`; no parent section |
| No hard-coding, 365 on check-out, changed value, unnamed tracking, search-service or flexible-dates addition, invented frame link or slot | Met | lines 37, 43; line 55; line 13; line 23 plain-text frame; `{max}` and `{n}` at line 43 quoted from notes lines 39-40 (exempt) |

**Blocking items hit**

- Pass clauses missed on Turn 1 (task rendered, no question, no `-clarification` label), root line 150.

**Advisory items**

- Block line 2 is `<!-- Mode: Task | Template: Task Templates v0.102 -->`, the sanctioned line-1 HTML comment (`Custom Instructions.md` line 96), not process material.
- en-GB fallback (line 119) named at `turn-1.md` line 128.
- Size band: 129 lines, inside 70 to 150.

**Realism entries**

- Block `PTK-002-turn1-block1.md` (reply lines 2-117), Canonical Task. Title, About, Requirements present. Facts: 23 chats (line 9) match notes line 11; 1 to 14 nights (line 40) match notes line 19; week start except `en-US` (line 116) matches notes line 57; `SRCH` matches `roamstay-context.md` line 91. Placeholders none beyond exempt keys. 116 lines. Code `FE`.
- Block `PTK-002-turn2-block1.md` (reply lines 2-130), Canonical Task. Title, About, Requirements present (lines 3, 5, 25). Facts: 23 chats (line 9) match notes line 11; design-system calendar on iOS and Android (line 115) matches notes line 55; en-GB fallback (line 119) matches context line 124; Guest app means iOS, Android and web (line 11) matches context line 17. Placeholders none beyond exempt keys. 129 lines, inside 70 to 150. Code `FE`.

**Open readings**: OR-1.

---

### PTK-003 | Long BE integration task (Project)

**Draft row**

```csv
PTK-003,project,claude-opus-5-5-medium,FAIL,2,2,pending,no,"Turn 1 rendered the full task with no question (turn-1.md lines 1-104). The Turn 2 block drops `5 attempts` and the whole retry schedule `1 min, 5 min, 15 min, 1 h, 6 h` (turn-2.md line 36 says only up to 5 more times over 7 hours 21 minutes) and moves the Fulfilment board out of the task into a ClickUp field (line 139)."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question as its own block | Unmet | `turn-1.md` lines 1-104 are the task |
| Under an export-equivalent `task` lane `-clarification` label with `HVR self-scan:` | Unmet | line 106 `export/001 - task-label-webhook-duplicates-and-late-labels.md`, no `-clarification`; HVR line 108 |
| Turn 1 renders no task | Unmet | lines 1-104 |
| Turn 2 renders one task block under an export-equivalent `task` label with `HVR self-scan:` and no file claim | Met | fenced block lines 1-119, line 121, line 123; no file claim |
| H1, About, Requirements with a checklisted group for each of the five points | Met | groups at lines 32, 48, 61, 79, 92, each with `**Checklist**` |
| Carrier values verbatim | Unmet | `event_id` line 48, `X-Carrier-Signature` and `HMAC-SHA256` line 40, `5 seconds` line 41 present; `5 attempts` absent (line 36 "retries up to 5 more times"); `1 min, 5 min, 15 min, 1 h, 6 h` absent from both blocks (only "6 h after the fourth" at line 10) |
| Thread values verbatim | Met | `7 days` lines 52, 56; `10 minutes` line 87; `30 minutes` and `#fulfilment-alerts` line 100; `more than 5` line 102 |
| Polling only kept out | Met | line 14 |
| Every Turn 2 fact | Unmet | no parent (no parent section), November peak (line 12), done definition (lines 117-118), 8-second timeout kept and moved out (lines 36, 44) present; "it goes on the Fulfilment board" absent from the block, line 139 calls it a ClickUp field to set by hand |
| No idempotency claim, `reference` dedupe, changed retry step, polling, answered open question, unnamed queue or vendor, invented cause, placeholder link | Met | line 12, line 73 open question kept, causes match thread lines 21-27 |

**Blocking items hit**

- Pass clauses missed on Turn 1 (task rendered), two carrier values absent and one Turn 2 fact outside the block, root line 150.

**Advisory items**

- Additions named at `turn-1.md` lines 115-120 and `turn-2.md` lines 134-135. Line 103 "Exactly 5 stuck shipments post to the channel but do not page on-call" is the direct test of `more than 5`, not an addition.
- Size band: 117 lines, inside 110 to 220.

**Realism entries**

- Block `PTK-003-turn1-block1.md` (reply lines 2-103), Canonical Task. Title, About, Requirements present. Facts: 37 duplicates and 12 late orders (line 8) match thread lines 9 and 13; €0.42 (line 8) matches thread line 17; `FH-2291834-1` matches notes line 16; `SHIP` with no surface matches `fernhouse-context.md` lines 93 and 104. Placeholders none. 102 lines. Code `BE`.
- Block `PTK-003-turn2-block1.md` (reply lines 2-118), Canonical Task. Title, About, Requirements present (lines 2, 4, 24). Facts: 20 requests per second shared by POST and GET, 14 at cut-off (line 14) match notes line 68 and thread line 45; label usually within a minute (line 83) matches `fernhouse-context.md` line 143; integration guide version 3.2 (line 22) matches notes line 3; 7 hours 21 minutes (line 52) matches notes line 59. Placeholders none. 117 lines, inside 110 to 220. Code `BE`.

**Open readings**

- The block leaves out the board because the reply treats it as a ClickUp field (`turn-2.md` line 139). Question: does a Turn 2 fact moved to the chat as a field to set by hand count as dropped from the deliverable?
- OR-1, OR-3 (here the schedule is absent, not restated).

---

### PTK-004 | Parent task with subtasks (Project)

**Draft row**

```csv
PTK-004,project,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 rendered a parent and four subtask blocks with no question (turn-1.md lines 1-570). The Turn 2 parent block lists the four subtasks as plain text (turn-2.md lines 44-68) and keeps every shared-rule value and Turn 2 fact; advisory: 198 block lines against the 60 to 130 band."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question as its own block | Unmet | `turn-1.md` lines 1-183 parent, 187-278 iOS, 282-374 Android, 378-471 Web, 475-568 BE |
| Under an export-equivalent `task` lane `-clarification` label with `HVR self-scan:` | Unmet | lines 185, 280, 376, 473, 570 carry task labels, no `-clarification`; HVR line 572 |
| Turn 1 renders no task | Unmet | five task blocks |
| Turn 2 renders one parent task block under an export-equivalent `task` label with `HVR self-scan:` and no file claim | Met | fenced block lines 1-200, line 202 `export/NNN - task-recurring-todos.md`, line 204; no file claim |
| H1, About, Requirements with one numbered entry each for iOS, Android, web and back end in plain text | Met | lines 40-70, backticked titles at 44, 52, 60, 68 |
| Shared rules with the brief's values | Met | table lines 86-90 (`Daily` to `Custom`, `1 to 99`); lines 104-106 `Never`, `On date`, `After`, `365`; lines 112, 120 `Skip this one`; line 128 `500` and the sheet copy; line 158 `recurring_todos`; line 146 `Plus`; line 136 "to-do owner's time zone" |
| Every Turn 2 fact | Met | line 10 only the parent, leads write their own subtasks and point at numbered rules; lines 12, 46, 54 5.4.0; lines 12, 62, 70, 158, 162 web and BE ship dark before it |
| No subtask blocks in Turn 2, no Desktop or Support console subtask, no link or `(url)` slot, no Repeat on Free, no changed range or copy, no check-off-date repeat or per-weekday time, activity question kept open | Met | one block only; line 10 Desktop via web; no links; line 146; lines 194-197; line 199 still open |

**Blocking items hit**

- Pass clauses missed on Turn 1 (parent and four subtasks rendered, no question), root line 150.

**Advisory items**

- Block order and links: Turn 1 put the parent first and the four subtasks in the prompt's order, each with its own `Export-equivalent path:` and one HVR line for the set. Parent and siblings are backticked plain text (iOS block lines 21-31 of the copy: parent `FS - TODO - Recurring to-dos`, related `BE - TODO - Recurring to-dos`; the BE block names all three clients), no links invented.
- Additions named at `turn-2.md` lines 214-217.
- Size band: 198 lines against 60 to 130.

**Realism entries**

- Block `PTK-004-turn1-block1.md` (reply lines 2-182), Parent Task (`Product Owner - Assets - Task Templates` line 146). Title, About, Requirements present. Facts: 212 and 38 (line 8) match brief line 8; 10% at 8 weeks (line 12) matches brief line 47; subtask titles follow `loomlist-context.md` line 104. Placeholders none. 181 lines. Code `FS`.
- Block `PTK-004-turn1-block2.md` (reply lines 188-277), Subtask. Title, About, Requirements present. Facts: hint, frames and local notifications match brief lines 12, 58 and context line 77. Placeholders none. 90 lines. Code `FE`, `iOS`.
- Block `PTK-004-turn1-block3.md` (reply lines 283-373), Subtask. Title, About, Requirements present. Facts: scope same as iOS (brief line 54), flag (brief line 45), local notifications (context line 77). Placeholders none. 91 lines. Code `FE`, `Android`.
- Block `PTK-004-turn1-block4.md` (reply lines 379-470), Subtask. Title, About, Requirements present. Facts: Desktop through the web client (context line 18), in-app reminders on Web and Desktop (context line 77), scope same as iOS (brief line 55). Placeholders none. 92 lines. Code `FE`, `Web`.
- Block `PTK-004-turn1-block5.md` (reply lines 476-567), Subtask. Title, About, Requirements present. Facts: reminders-service handover (context line 71), 500 limit (brief line 35), owner's zone (brief line 39). Placeholders none. 92 lines. Code `BE`.
- Block `PTK-004-turn2-block1.md` (reply lines 2-199), Parent Task. Title, About, Requirements present (lines 2, 4, 32). Facts: reminder delivery per surface (line 118) matches context line 77; to-do owner definition (line 138) matches context line 55; standard event properties (line 180) match context line 187; out-of-scope list (lines 194-197) matches brief lines 66-69. Placeholders none. 198 lines against 60 to 130. Code `FS`.

**Open readings**: OR-1.

---

### PTK-005 | Supplied parent subtask (Project)

**Draft row**

```csv
PTK-005,project,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 rendered the full Android subtask with no question (turn-1.md lines 1-173). The Turn 2 block names the supplied parent `FS - TODO - Recurring to-dos` as plain text (turn-2.md line 26) and keeps every value and Turn 2 fact; advisory: 171 block lines against the 60 to 130 band."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question as its own block | Unmet | `turn-1.md` lines 1-173 are the subtask |
| Under an export-equivalent `task` lane `-clarification` label with `HVR self-scan:` | Unmet | line 175 `export/NNN - task-android-recurring-todos.md`; HVR line 177 |
| Turn 1 renders no subtask | Unmet | lines 1-173 |
| Turn 2 renders one subtask block under an export-equivalent `task` label with `HVR self-scan:` and no file claim | Met | fenced block lines 1-173, line 175, line 177; line 198 says it cannot push, no file claim |
| H1, About, Requirements with checklisted groups | Met | lines 2, 4, 36; groups 1-8 each with `**Checklist**` |
| Parent named as `FS - TODO - Recurring to-dos` | Met | line 26 under `**Parent task**`, plain text as Task Mode knowledge line 113 requires; the parent is not re-rendered or rewritten |
| Shared rules as the parent gives them | Met | line 52 `Daily` to `Custom`; line 54 `1 to 99`; line 65 `Never`, `On date`, `After`; line 71 `365`; lines 95-105 `Skip this one`; lines 135, 139 `500` and the sheet copy; lines 10, 148, 154 `recurring_todos`; line 113 "the owner's time zone" |
| Android as the only client in scope | Met | lines 8-10; iOS and Web only under Related tasks (lines 33-34) |
| Every Turn 2 fact | Met | line 8 phones and tablets, Oskar's team, 5.4.0; line 57 picker on both; line 10 BE builds the engine at the same time, Android never works a date out; lines 55, 89, 104, 122 |
| No dropped or invented parent link, no iOS, web, Desktop or engine work, no device-side date logic, no changed option or copy, no unnamed Android addition, no slot | Met | additions named at `turn-1.md` lines 182-188 and `turn-2.md` lines 187-191 |

**Blocking items hit**

- Pass clauses missed on Turn 1 (subtask rendered, no question), root line 150.

**Advisory items**

- Size band: 171 lines against 60 to 130.
- Line 105 "so skipping the last allowed occurrence ends the series" is a consequence of parent line 85, named at `turn-1.md` line 186, not re-listed in Turn 2.

**Realism entries**

- Block `PTK-005-turn1-block1.md` (reply lines 2-172), Subtask (`Product Owner - Assets - Task Templates` line 195). Title, About, Requirements present. Facts: parent title matches parent fixture line 1; frames match parent lines 19-21; flag matches parent line 103. Placeholders none. 171 lines. Code `FE`, `Android`.
- Block `PTK-005-turn2-block1.md` (reply lines 2-172). Title, About, Requirements present. Facts: `BE - TODO - Recurrence engine` (line 32) matches parent line 49; six app locales with `en-US` fallback (line 56) match `loomlist-context.md` line 155; Mobile Platform team under Oskar (line 8) matches context line 89; Yara reviewed 2026-09-16 (line 166) matches parent line 109. Placeholders none. 171 lines against 60 to 130. Code `FE`, `Android`.

**Open readings**: OR-1.

---

### PTK-006 | Data tracking task (Project)

**Draft row**

```csv
PTK-006,project,claude-opus-5-5-medium,FAIL,2,2,pending,no,"Turn 1 rendered one clarification block labelled export/001 - task-booking-funnel-events-clarification.md and Turn 2 one task block, but the task never marks `checkout_complete` as `deprecated`, only its removal (turn-2.md lines 81-86). Borderline: turn-1.md line 50 promises to ""save it as the next file in the task folder""."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 routes to Task Mode | Met | task-lane clarification label at line 37 |
| Asks one question rendered as its own block | Met | fenced block lines 1-35, one consolidated clarification with six numbered points |
| Under an export-equivalent `task` lane `-clarification` label with `HVR self-scan:` | Met | line 37 `` `export/001 - task-booking-funnel-events-clarification.md` ``, line 39 HVR |
| Turn 1 renders no task | Met | block holds questions only |
| Turn 2 renders one task block under an export-equivalent `task` label with `HVR self-scan:` and no file claim | Met | fenced block lines 1-88, line 90 `export/002 - task-booking-funnel-event-checks.md`, line 92 HVR, no file claim in Turn 2 |
| H1, About, Requirements with checklisted groups | Met | lines 2, 4, 22; group 1 carries `- [ ]` items under three bold labels (lines 32, 39, 51) in place of `**Checklist**`, groups 2-3 use `**Checklist**` |
| Six funnel events as the plan names them | Met | line 70 |
| `booking_confirmed` from `booking-service` with `source` set to `server` | Met | line 35 `server` on `booking_confirmed`; line 66 fires when `booking-service` confirms |
| `total_amount_minor` in minor units | Met | line 47 |
| `checkout_complete` marked `deprecated` with its removal on `2026-11-01` | Unmet | removal at lines 10, 81, 85-86; `deprecated` absent from the task block (grep, no match); the Turn 1 clarification line 32 did say "the deprecated `checkout_complete`" (OR-4) |
| `date_changed` kept `proposed` and unbuilt | Met | line 12 |
| Every Turn 2 fact | Met | line 2 `DATA`, `TRK`; line 30 "Nadia checks every event"; lines 62-73 dashboard move; lines 77-86 collector drop; line 10 separate FE and BE tasks, table stands after the 2026-09-24 refinement |
| No `date_changed` build, no early or late drop, no booking count from `payment_submitted` or `checkout_complete`, no client `booking_confirmed`, no decimals, no FE or BE build inside the task, no slot | Met | lines 12, 85-86, 71, 35, 47, 10 |

**Blocking items hit**

- Pass clause missed: `checkout_complete` not marked `deprecated`, root line 150, read under OR-4.

**Advisory items**

- Borderline file claim: `turn-1.md` line 50 "Once you answer, I'll write the task and save it as the next file in the task folder." It is a promise, not a claim that a file was saved (root line 189, `Custom Instructions.md` line 101).
- Group 1 has no `**Checklist**` label (lines 32-56). Task Mode knowledge lines 84-89 make the label a "should" pattern, and lines 54-58 require only Title, About and Requirements, so it is not a missing required section.
- Additions named at `turn-2.md` lines 97-99. Line 46 lists `booking_confirmed` among properties under the "Client events" label, a layout slip only; line 35 keeps it `server`.
- Size band: 86 lines, inside 60 to 140.

**Realism entries**

- Block `PTK-006-turn1-block1.md` (reply lines 2-34), task-lane clarification (`Custom Instructions.md` line 228). Question only. Facts: draft v0.3 (line 4) matches plan line 1; refinement 2026-09-24 (line 16) matches plan line 5; title pattern (line 8) matches `roamstay-context.md` line 83; Android `room_selected` timing (line 24) matches plan lines 67-71. Placeholders: the title pattern `{Discipline} - {Surface} - {Feature code} - {Title}` at line 8 is quoted from context line 83 (exempt). 33 lines, no band.
- Block `PTK-006-turn2-block1.md` (reply lines 2-87), Canonical Task. Title, About, Requirements present (lines 2, 4, 22). Facts: city tax inside `total_amount_minor` (line 47) matches plan line 45; `payment_option` values (line 49) match plan line 47; `RS-` reference (line 55) matches context line 47; drop "whatever app version sends it" (line 81) matches plan line 56. Placeholders none. 86 lines, inside 60 to 140. Code `DATA`.

**Open readings**

- OR-4 decides this verdict.
- Does a Turn 1 promise to "save it as the next file" count as a file claim on the Project side?

---

### Twin notes

| Pair | Skill | Project | Agree or differ | Cause and rule lines |
|---|---|---|---|---|
| STK-001 / PTK-001 | PASS | PASS | Agree | Both skipped intake under `$quick` (`AGENTS.md` line 289 and `references/interactive-mode.md` line 126; `Custom Instructions.md` line 108 and Interactive Mode knowledge line 103). Minor difference, recorded only: skill chose `FS`, Project `FE`, both with no surface and both named. |
| STK-002 / PTK-002 | FAIL | FAIL | Agree | Both drafted on Turn 1. Both packagings say `$task` asks and waits: `AGENTS.md` line 287, `references/task-mode.md` line 50, `references/interactive-mode.md` line 124; `Custom Instructions.md` line 108, Task Mode knowledge line 30, Interactive Mode knowledge line 101. Same text on both sides, both runtimes missed it, so a runtime fault on both, with the shared wording tension in OR-1. |
| STK-003 / PTK-003 | FAIL | FAIL | Agree on the verdict | Same Turn 1 cause as above. Secondary differences are runtime faults, not packaging gaps: STK-003 has no Read after its last Edit (`AGENTS.md` line 46 requires one; the Project has no read-back rule), and PTK-003 drops the retry schedule and the Fulfilment board, which both runtimes received from the same attachments and turn. |
| STK-004 / PTK-004 | FAIL | FAIL | Agree | Same Turn 1 cause. The skill runtime cited the "enough direction" clause of `references/task-mode.md` line 50; PTK-004 grepped for it (call 11). Both went on to a parent plus four subtasks, saved as five files on the skill side and rendered as five blocks on the Project side, then reduced to the parent alone on Turn 2. |
| STK-005 / PTK-005 | FAIL | FAIL | Agree | Same Turn 1 cause; STK-005 stated "No clarification was needed" (`turn-1.md` line 1). Both link the supplied parent as backticked plain text (`assets/task-templates.md` line 159, Task Mode knowledge line 113) without rewriting it. |
| STK-006 / PTK-006 | FAIL | FAIL | Agree | Both asked correctly on Turn 1 and delivered on Turn 2, and both fail only on the `deprecated` label (OR-4). The status is in the same attachment for both (plan line 25), and neither packaging has a rule on status labels in tasks, so this reads as a scenario-strictness question rather than a rule, parity or runtime gap. Differences, recorded only: STK-006 leaves Nadia out as the checker where PTK-006 keeps her (line 30); PTK-006 promises a save in Turn 1 commentary. |

Tally: skill 1 PASS, 5 FAIL; Project 1 PASS, 5 FAIL. If the operator reads OR-4 as met, STK-006 turns on the Nadia question and PTK-006 on the save-promise question, and both could move to PASS.

---

## 7. Bugs batch, grader draft

Batch `bugs`: SBG-001, PBG-001, SBG-002, PBG-002, SBG-003, PBG-003. Model `claude-opus-5-5-medium`. Run folder `<RUN>` = `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/`.

Sources: `git -C "AI Systems/Product Owner" status --porcelain -- sk-product-owner "claude project" AGENTS.md benchmark/fixtures` printed nothing and HEAD is `3023c5e`, so every source line below is cited from the working tree at `3023c5e`.

Format gate: `node validate-output-format.cjs --system product-owner <file>` run from the Sync Loop folder on all four skill exports and all five Project block copies under `scratch/grades/blocks/bugs/`. Every run printed `Product Owner output format validation passed across 1 artifact file(s)` with exit 0.

Event numbers below are the 0-based line index of the event in `events-turn-<n>.jsonl`.

---

### SBG-001 (skill), Quick bug

#### Draft row

```csv
SBG-001,skill,claude-opus-5-5-medium,PASS,1,1,pending,yes,"Turn 1 asked nothing and saved export/001 - bug-ios-cart-badge-stale-after-remove.md, read back at lines 1 to 75, with Always, Medium, iOS and Not provided cells, the ""3"" badge over 2 units and Expected ""2"" by the unit rule (export lines 11 to 15, 32, 55). Borderline only: the unsourced ""No error message is shown"" (line 33) and a title code FE the reply names as a guess."
```

#### Pass clauses

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks no question | Met | `turn-1.md` lines 1 to 17 hold no question. Line 17 "Next step: if you send the phone models, iOS versions or a screen recording, I'll add them" is an offer after delivery |
| Saves one bug export under the `bug` word | Met | `meta.json` turn 1 ledger created only `export/001 - bug-ios-cart-badge-stale-after-remove.md`, no `-clarification` file |
| Read back and reported with its path, the `Verified:` line and the `HVR self-scan:` line | Met | Write at `events-turn-1.jsonl` event 32, then Read of the same path at event 38 returning lines 1 to 75. `turn-1.md` line 3 path, line 4 "Verified: read-back succeeded; 75 lines", line 5 "HVR self-scan: 0 hard blockers. ..." |
| Every required template section | Met | Export line 1 H1, line 3 `### About`, lines 9 to 17 field table, line 19 References, line 23 `### Bug`, line 27 `**1. Observed Behavior**`, line 37 `Steps to Reproduce:`, line 46 screen recording, line 50 `**2. Expected Behavior**`, lines 59 to 63 the four Checklist items. Format gate passed |
| Field table reads `Always`, `Medium`, `iOS`, `Not provided` for Device and OS Version | Met | Export line 11 "Always (every attempt on both iOS test phones, per reporter)", line 12 "Medium", line 13 "iOS (app 4.8.0)", line 14 "Not provided (two iOS test phones, models not given)", line 15 "Not provided" |
| Body keeps iOS `4.8.0`, the "3" badge over 2 units and the restart | Met | Line 7 "In the iOS app 4.8.0", line 32 "removing the single-unit line leaves 2 units in the cart and the badge still reads "3"", line 34 "shows the correct count only after the app is restarted" |
| Calls neither Android `4.8.2` nor web affected | Met | Line 35 "Android 4.8.2 and web show the new count on the badge as soon as the item is removed" |
| Expected Behavior has the badge show "2", the unit count, right after the removal | Met | Line 54 "shows the new unit count as soon as an item is removed from the cart, without a restart", line 55 "the badge counts units in the cart, not lines, so removing the 1-unit line from a 3-unit cart leaves the badge on "2"" |

Fail list checked: no phone model, no iOS version and no root cause in the artifact, units counted rather than lines, no Android or web widening, no unfilled slot.

#### Blocking items hit

None.

#### Advisory items

- Size band: 74 lines against 35 to 70, over by 4. The BDD section (lines 67 to 74) is a named addition (`turn-1.md` line 15)
- Borderline, never decides alone: line 33 "No error message is shown" is a claim about current behavior that neither the prompt nor `fernhouse-context.md` contains, and no naming line in `turn-1.md` covers it. The house examples model the same line (`assets/examples/bug/bug-example-frontend-visual.md` line 46) and the checklist asks that error messages be "included or marked as not provided" (`references/bug-mode.md` line 217)
- Borderline, never decides alone: title code `FE`. The reply names it at `turn-1.md` line 12 as "a guess, not a known root cause", and `fernhouse-context.md` line 82 requires one code on every bug
- Named additions, covered: the unit rule source (line 13), the iOS add-updates expectation at export line 57 (line 14, also `fernhouse-context.md` line 140), the BDD scenario (line 15)
- Title carries a discipline code, so the no-code advisory is not hit

#### Read-back table

| Turn | Export path | `N` printed | Read after the last Write or Edit, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - bug-ios-cart-badge-stale-after-remove.md` | 75 | Read at event 38 after the only Write at event 32, lines 1 to 75 (line 75 empty) | 74 |

#### Realism entry

- `export/001 - bug-ios-cart-badge-stale-after-remove.md`, kind Bug
- Routed template (`assets/bug-report-template.md` lines 63 to 151, order at `references/bug-mode.md` lines 127 to 135): H1, `### About`, field table, References, `### Bug`, Observed, `Steps to Reproduce:`, screen recording, Expected, Checklist all present. Optional BDD present
- Company facts against `benchmark/fixtures/companies/fernhouse/fernhouse-context.md`: iOS `4.8.0` (line 116), Android `4.8.2` (line 117), badge counts units not lines (line 22), `CART` covers the cart badge (line 101), title pattern `{Discipline} - {Surface} - {Feature code} - {Title}` (line 93), `FE` is client work (line 86). All match
- Placeholder: none
- Body 74 lines against 35 to 70 (advisory, over)
- Discipline code: `FE` present

#### Open readings

- `N`: the reply printed 75, the Read's final displayed line is 75 (an empty line after the trailing newline) and `wc -l` is 74. `AGENTS.md` line 45 says to use the final line number Read returns. Is `N` graded against that Read line or against `wc -l`?
- Does an unsourced "No error message is shown" line count as an invented behavior claim, given that both packagings' examples model it, or as a filled template slot?

---

### PBG-001 (project), Quick bug

#### Draft row

```csv
PBG-001,project,claude-opus-5-5-medium,PASS,1,1,pending,yes,"Turn 1 asked nothing and rendered one fenced bug block, then Export-equivalent path export/NNN - bug-ios-cart-badge-stale-after-remove.md and the HVR line with no file claim, keeping every value and the unit rule (turn-1.md lines 12 to 16, 33, 59, 70, 72). Advisory: the block lowercases the fixed labels Steps to reproduce, OS version and Browser version."
```

#### Pass clauses

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks no question | Met | `turn-1.md` holds no intake question. Line 88 "Next step: tell me the device models and iOS versions, or attach a recording" is an offer after delivery |
| Renders one bug as its own block | Met | One fenced block, `turn-1.md` lines 1 to 68 (```` ```markdown ```` to ```` ``` ````), closed before the label |
| `Export-equivalent path:` under the `bug` word | Met | Line 70 "Export-equivalent path: `export/NNN - bug-ios-cart-badge-stale-after-remove.md`" |
| `HVR self-scan:` line | Met | Line 72 |
| Claims no file | Met | No save, write, read-back or verified claim in lines 70 to 88 (grep of `replies/PBG-001-turn1.txt` for saved, wrote, written, read back, verified: none) |
| Every required template section | Met | Block line 2 H1, line 4 `### About`, lines 10 to 18 field table, line 20 References, line 24 `### Bug`, line 28 Observed, line 38 steps label, line 46 screen recording, line 52 Expected, lines 61 to 65 Checklist. Format gate passed. Label case noted under Advisory |
| Field table `Always`, `Medium`, `iOS`, `Not provided` for Device and OS Version | Met | Line 12 "Always (every time on two iOS test phones, per reporter)", line 13 "Medium", line 14 "iOS (app 4.8.0)", line 15 "Not provided (two iOS test phones, models not given)", line 16 "Not provided" |
| Body keeps iOS `4.8.0`, the "3" badge over 2 units and the restart | Met | Line 8 "In the Fernhouse iOS app 4.8.0", line 33 "The cart holds 2 units but the badge still reads "3"", line 34 "The badge stays on "3" until the app is restarted" |
| Calls neither Android `4.8.2` nor web affected | Met | Line 36 "On Android 4.8.2 and web, the badge updates straight away after the same removal" |
| Expected Behavior has the badge show "2", the unit count, right after the removal | Met | Line 56 "should show the new unit count straight away", line 59 "the badge shows the number of units in the cart, so after this removal it reads "2" without restarting the app" |

Fail list checked: no clarification rendered, no file claim, no phone model, iOS version or cause (reply line 74 "I added no root cause"), units not lines, no widening, no unfilled slot.

#### Blocking items hit

None.

#### Advisory items

- Fixed labels changed case: block line 38 "Steps to reproduce:", line 16 "OS version", line 18 "Browser version" against the Project template's "Steps to Reproduce:" (line 88), "OS Version" (line 58) and "Browser Version" (line 60). The HVR line 72 names this as a fix. Each section is present, so no required section is missing
- Design spec reads "Not provided" (line 57) although `fernhouse-context.md` line 22 states the unit rule. The rule is applied at line 59, so the fact is not ignored
- Named addition, covered: "Customer type (guest or signed in) and market used in testing: Not provided" (line 48), named at reply line 84
- Commentary follows the block, so no ordering defect
- Delivery form: fenced block
- Title carries `FE`, built from the context convention (reply line 76)

#### Realism entry

- Block `turn-1.md` lines 2 to 67, copy `scratch/grades/blocks/bugs/PBG-001-turn1-bug.md`, kind Bug
- Routed template (`claude project/knowledge/Product Owner - Assets - Bug Report Template - v0.100.md` lines 43 to 131, order at `Product Owner - Templates - Bug Mode - v0.203.md` lines 110 to 118): every required section present, BDD not used
- Company facts against `fernhouse-context.md`: iOS `4.8.0` (line 116), Android `4.8.2` (line 117), units not lines (line 22), `CART` (line 101), signed-in carts follow the customer across surfaces (line 140, used for the named addition). All match
- Placeholder: none. `NNN` in the label is the exempt Project slot
- Body 66 lines, inside 35 to 70
- Discipline code: `FE` present

#### Open readings

- Does a changed letter case on a fixed template label (`Steps to Reproduce:`, `OS Version`, `Browser Version`) count against "every required template section", or only a missing section?

---

### SBG-002 (skill), Support ticket bug

#### Draft row

```csv
SBG-002,skill,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 asked no question and saved the whole bug as export/001 - bug-android-confirmation-total-missing-city-tax.md (turn-1.md lines 1 to 4, Write at event 56), and Turn 2 edited that file in place instead of saving on the next number. The final bug keeps every ticket amount, the correct charge and the Android 8.12.1 Pay now scope."
```

#### Pass clauses

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question | Unmet | `turn-1.md` holds no question. Line 1 "I've written the bug report from Maren's ticket and saved it." |
| Saves it as a question-only clarification under the `bug` word with its path, `Verified:` and `HVR self-scan:` lines | Unmet | Turn 1 ledger created only `export/001 - bug-android-confirmation-total-missing-city-tax.md`. No `-clarification` file exists in `exports/export/` |
| Drafts nothing | Unmet | Full bug written at `events-turn-1.jsonl` event 56 |
| Turn 2 saves one bug under the `bug` word on the next number | Unmet | Turn 2 ledger created nothing and modified `export/001 - bug-android-confirmation-total-missing-city-tax.md`. `turn-2.md` line 3 reports that same path |
| Read back | Met (Turn 2) | Read at `events-turn-2.jsonl` event 27 after the last Edit at event 25, lines 1 to 114 |
| Every required template section | Met | Export line 1 H1, line 3 About, lines 9 to 17 field table, lines 19 to 32 References, line 36 Bug, line 40 Observed, line 69 `Steps to Reproduce:`, line 79 screen recording, line 83 Expected, lines 93 to 97 Checklist. Format gate passed |
| Ticket `58213`, `RS-7Q4K2M`, Android `8.12.1`, `Pay now` | Met | Lines 22, 23, 13 and 7 |
| "Total €387.00" against `€405.00` charged and the `€18.00` city tax | Met | Line 45 "saw `Total €387.00` on the confirmation screen and was charged €405.00, a gap of €18.00", lines 60 to 62 the Back office table |
| Severity `High` | Met | Line 12 "High" |
| No device model | Met | Line 14 "Guest's phone: Not provided. Guest Support test phone: model not provided" |
| Every other amount exactly as the ticket gives it and adding up | Met | Lines 49, 50 and 74 carry €270.00, €258.00, €12.00, €135.00, €129.00 and €6.00 as ticket lines 55 and 56 do. 387 + 18 = 405, 258 + 12 = 270, 129 + 6 = 135 |
| Charge described as correct, Android confirmation total as the defect | Met | Line 47 "which matches the charge", line 48 "it is the only charge on the card", line 87 "The confirmation screen total equals the amount charged", line 90 the product rule |
| Scope held to Android `8.12.1` Pay now stays of 2 nights or more, no claim that 1 night, iOS `8.12.0` or web is wrong | Met | Line 50 1 night right, line 51 iOS "`Total €405.00`", line 52 web right, line 65 Pay at property "Whether ... show the same lower total" |

Fail list checked: Pay at property left unknown (line 65), Frequency rests on the escalation (line 11) and not on the 14 chats, no device model, no cause stated (line 66 "The cause. Nobody on the Booking squad has looked at the code yet"). Repro step 6 (line 75, cancelling the test booking) is named at `turn-1.md` line 15 and sourced from ticket line 58.

#### Blocking items hit

- Four Pass clauses unmet, root line 150. An explicit `$bug` asks its mode's question and waits (`AGENTS.md` line 287)
- Side-effect ledger: Turn 1 created a bug where a clarification turn may create only the `-clarification` export (root line 106), so the ledger holds a disallowed change (root line 144)

#### Advisory items

- Size band: 113 lines against 60 to 110, over by 3
- Borderline, never decides alone: line 46 "No error message is shown. The screen looks like a normal confirmation with a lower total" appears in neither the turns nor the ticket and is not named
- Borderline, never decides alone: line 52 "checked on 2026-09-25" turns Turn 2's "this morning" into the run date, a value no turn or attachment gives
- Borderline, never decides alone: line 54 "so the number of affected guests can grow from here" projects from ticket line 66 "the Android rollout only reached everyone today"
- Title code `FE` named at `turn-1.md` line 12 with "The cause hasn't been found"
- Turn 1 set Severity from the ticket priority and named it (`turn-1.md` line 14). Turn 2 confirmed High
- Turn 1 read-back proof: the Read at event 65 (lines 1 to 110) came before the last Edit at event 71. After that Edit only a Bash `wc -l` (printed 109) and `sed -n '41p;110p'` ran, no Read. Recorded only, since the verdict already fails

#### Read-back table

| Turn | Export path | `N` printed | Read after the last Write or Edit, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - bug-android-confirmation-total-missing-city-tax.md` | 110 | None. Read at event 65 returned lines 1 to 110, then Edit at event 71, then Bash `wc -l` printed 109 | 109 at the end of Turn 1 (Bash output) |
| 2 | same path, modified | 114 | Read at event 27 after the last Edit at event 25, lines 1 to 114 (line 114 empty) | 113 |

#### Realism entry

- `export/001 - bug-android-confirmation-total-missing-city-tax.md` (final state after Turn 2), kind Bug
- Routed template (`assets/bug-report-template.md`): every required section present, optional BDD present with two scenarios (named)
- Company facts against `roamstay-context.md`: Android `8.12.1` (line 107), iOS `8.12.0` (line 106), `BOOK` covers the confirmation screen (line 93), `Guest app` as the title surface (line 83), city tax part of the total (line 44), Pay now charges the full total (line 148), staged Android rollout (line 112). Ticket values against `roamstay-support-ticket-58213.md` lines 8, 12 to 16, 42 to 58. All match
- Placeholder: none
- Body 113 lines against 60 to 110 (advisory, over)
- Discipline code: `FE` present

#### Open readings

- Does a Bash `wc -l` or `sed` after the last Edit count as read-back, or only a Read tool call? Verdict unaffected here
- Is resolving "this morning" to the runtime's own date (2026-09-25) an invented value or a direct reading?
- `N` as in SBG-001: Turn 2 printed 114, the Read's final line, while `wc -l` is 113

---

### PBG-002 (project), Support ticket bug

#### Draft row

```csv
PBG-002,project,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 rendered the whole bug block (turn-1.md lines 1 to 92) under a plain bug label with no -clarification suffix instead of one question-only block, so the ask-first clauses are unmet. The Turn 2 block keeps every amount, the correct charge and the Android 8.12.1 Pay now scope, with no file claim."
```

#### Pass clauses

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question | Unmet | `turn-1.md` lines 1 to 92 are a complete bug and lines 94 to 108 ask nothing |
| Renders it as its own question-only block with `Export-equivalent path:` under the `bug` word and the `-clarification` suffix and the `HVR self-scan:` line | Unmet | Line 94 "Export-equivalent path: `export/NNN - bug-android-confirmation-total-missing-city-tax.md`" carries no `-clarification` suffix. The HVR line is present at line 96 |
| Drafts nothing | Unmet | `turn-1.md` lines 2 to 91 are the full bug |
| Turn 2 renders one bug as its own block | Met | `turn-2.md` lines 1 to 96, one fenced block |
| `Export-equivalent path:` under the `bug` word | Met | `turn-2.md` line 98 |
| `HVR self-scan:` line | Met | `turn-2.md` line 100 |
| Claims no file on either turn | Met | Grep of both reply files for saved, wrote, written, read back, verified: no claim |
| Every required template section | Met | `turn-2.md` line 2 H1, line 4 About, lines 10 to 18 field table, line 20 References, line 31 Bug, line 35 Observed, line 51 `Steps to Reproduce:`, line 58 screen recording, line 70 Expected, lines 80 to 84 Checklist. Format gate passed |
| Ticket `58213`, `RS-7Q4K2M`, Android `8.12.1`, `Pay now` | Met | Lines 23, 24, 39 and 40 |
| "Total €387.00" against `€405.00` and the `€18.00` city tax | Met | Line 40 "showed Total €387.00 and the card was charged €405.00", line 41 "The €18.00 difference is the property's city tax", lines 64 to 66 |
| Severity `High` | Met | Line 13 |
| No device model | Met | Line 15 "Guest's phone: not known. Guest Support Android test phone: model not provided" |
| Every other amount exact and adding up | Met | Lines 43, 44 and 56 match ticket lines 55 and 56 |
| Charge correct, Android confirmation total the defect | Met | Line 42 "The charge is correct." |
| Scope held, no claim that 1 night, iOS or web is wrong | Met | Lines 44, 45, 46, and line 49 leaves Pay at property "not known" |

Fail list checked: Frequency rests on Guest Support's statement (line 12), not the 14 chats. No device, cause or invented step.

#### Blocking items hit

- Three Pass clauses unmet, root line 150. The Project packaging says an explicit `$bug` asks and waits (`Custom Instructions.md` line 108)

#### Advisory items

- Borderline, never decides alone: `turn-2.md` line 46 "on 2026-09-25" turns "this morning" into the run date
- Turn 2's "nobody on Booking has looked at the code yet" is in the chat (line 113) but not in the block. The block states no cause and keeps "Root cause identified" open, so nothing is altered
- Title code `FE` named as an assumption (`turn-1.md` line 103, `turn-2.md` line 114)
- Device and OS cells write "not known" rather than `Not provided` for the guest's phone (lines 15 and 16), wording only
- Turn 1 set Severity from the ticket priority and named it (`turn-1.md` line 105)
- Commentary follows each block. Delivery form: fenced block on both turns

#### Realism entries

- Block `turn-1.md` lines 2 to 91, copy `scratch/grades/blocks/bugs/PBG-002-turn1-bug.md`, kind Bug (delivered early). Every required section present per the Project template, BDD present and named. Facts: Android `8.12.1` (`roamstay-context.md` line 107), iOS `8.12.0` (line 106), `BOOK` (line 93), rollout date (ticket line 66). 90 lines inside 60 to 110. Code `FE`. Placeholder none
- Block `turn-2.md` lines 2 to 95, copy `scratch/grades/blocks/bugs/PBG-002-turn2-bug.md`, kind Bug. Every required section present (`Product Owner - Assets - Bug Report Template - v0.100.md` lines 43 to 131). Facts: `Guest app` surface (`roamstay-context.md` line 83), city tax in the total (line 44), Pay now charges the full total (line 148), ticket values (`roamstay-support-ticket-58213.md` lines 12 to 16, 42 to 58). All match. 94 lines inside 60 to 110. Code `FE`. Placeholder none

#### Open readings

- Same "this morning" date question as SBG-002

---

### SBG-003 (skill), Two-platform log bug

#### Draft row

```csv
SBG-003,skill,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 saved the question-only export/001 - bug-reminders-late-after-clock-change-clarification.md and drafted nothing, and Turn 2 saved export/002 with Group A and Group B apart, the log verbatim (lines 78 to 88), Severity High and Frequency Not provided. The Group A cause at line 93 is labelled an unverified hypothesis and disclaims Group B, so root line 187 does not count it as invented (see Open readings)."
```

#### Pass clauses

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question | Met | Clarification line 3 "Please answer all three in one reply", one consolidated question over scope, code and severity, and current versions (lines 5 to 18) |
| Saves it as a question-only clarification under the `bug` word with its path, `Verified:` and `HVR self-scan:` lines | Met | `export/001 - bug-reminders-late-after-clock-change-clarification.md`. Write at `events-turn-1.jsonl` event 50, Read at event 52, lines 1 to 19. `turn-1.md` lines 3 to 5 |
| Drafts nothing | Met | Turn 1 ledger created only the clarification |
| Turn 2 saves one bug under the `bug` word on the next number | Met | Turn 2 ledger created only `export/002 - bug-reminders-late-after-clock-change.md` |
| Read back | Met | Read at `events-turn-2.jsonl` event 37 (offset 100) after the only Write at event 28, lines 100 to 114 |
| Every required template section | Met | Line 1 H1, line 3 About, lines 11 to 19 field table, lines 21 to 32 References, line 36 Bug, line 40 Observed, lines 59 and 66 `Steps to Reproduce` per group, line 73 screen recording, line 97 Expected, lines 107 to 111 Checklist. Format gate passed |
| Android `5.2.3` one-off 09:00 to 10:00 and iOS `5.2.4` daily 07:30 to 08:30 as two separate observed and expected pairs | Met | Observed: line 46 "Group A, Android 5.2.3, one-off reminders, 64 tickets", line 47 "A reminder set for 09:00 arrives at 10:00", line 52 "Group B, iOS 5.2.4, daily reminders, 53 tickets", line 53 "set for 07:30 arrives at 08:30". Expected: Group A step line 63 "Expected: the reminder shows at 09:00 local. Actual: it shows at 10:00 local" and line 101 "whether it was set before or after a clock change". Group B step line 70 and line 103 "A daily reminder keeps its local time across a clock change without the member opening it and saving it again" |
| Log evidence for the Android issue with `rem_8f31c2` and `Europe/Amsterdam` | Met | Lines 75 to 91. Lines 78 to 88 diff clean against `loomlist-reminders-dst-log-excerpt.md` lines 11 to 21 |
| Edit-and-save workaround for the iOS issue | Met | Line 56 "until the member opens the reminder and taps Save with no change. It arrives at 07:30 again from the next day", step line 71 |
| Every ticket ID, count, offset, UTC time and date exactly as the attachments give it | Met | Lines 24 to 30 (2026-04-07, 2026-09-16, LL-20931, LL-20944, LL-20958, 2026-04-02), line 44 (117, 2026-03-29, 2026-04-05), lines 46 and 52 (64, 53), line 91 (`tz_offset=+01:00`, `tz_offset=+02:00`), line 9 (2026-10-25), all matching `loomlist-reminders-dst-user-reports.md` lines 3 to 39 and the log excerpt lines 3 to 28 |
| Severity `High` | Met | Line 14 |
| No device model or OS version | Met | Lines 16 and 17 "Not provided" |
| No root cause for either issue | Met under root line 187 | Line 93 "Hypothesis for Group A, unverified: the UTC due time may be fixed when the reminder is created, using the offset in force that day. Ruben has not read the scheduling code, so this is not a confirmed root cause, and it says nothing about Group B." Labelled as an unverified hypothesis, given to one issue only, not stated as fact. The same labelled form as `assets/examples/bug/bug-example-mobile-crash.md` line 68. Named in chat at `turn-2.md` line 8. See Open readings |

Fail list checked: one bug file, no merged symptom, no swapped platform, version or kind. Frequency `Not provided` (line 13). Line 9 "Nobody has checked the current Android 5.3.0 and iOS 5.3.2 apps" claims neither affected nor fixed. The October date and "when the clocks go back one hour" come from user reports line 49 and predict nothing about reminders. Steps are marked "not yet reproduced by QA" (lines 59, 66) and line 44 says "QA has not reproduced either group yet". Log lines kept to Group A (line 75 "Group A only ... No log lines exist yet for Group B").

#### Blocking items hit

None.

#### Advisory items

- Asking for a fact the turn states: the clarification asks "one bug or two" (lines 5 to 14) though Turn 1 said "write it up as one bug" (root line 211 reading, recorded only)
- Borderline, never decides alone: line 57 "No error message is shown in either group" is in no attachment or turn and is not named
- Borderline, never decides alone: line 54 "Members changed nothing." widens LL-20944's "I did not touch anything" (user reports line 31) to the group
- Borderline, never decides alone: title code `FS - REM` chosen by the runtime after Turn 2 left the code open, named at `turn-2.md` line 13. `FS` means front end and back end changes together (`loomlist-context.md` line 100), which leans on where the fix sits
- Named omission: Marta's known-issue and macro request left out (`turn-2.md` line 17)
- Size: 113 lines inside 80 to 150

#### Read-back table

| Turn | Export path | `N` printed | Read after the last Write or Edit, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - bug-reminders-late-after-clock-change-clarification.md` | 19 | Read at event 52 after the Write at event 50, lines 1 to 19 (line 19 empty) | 18 |
| 2 | `export/002 - bug-reminders-late-after-clock-change.md` | 113 | Read at event 37 with offset 100 after the Write at event 28, lines 100 to 114 (line 114 empty). A Bash `wc -l` at event 33 printed 113 | 113 |

#### Realism entries

- `export/001 - bug-reminders-late-after-clock-change-clarification.md`, kind Clarification (bug lane). Question-only: no draft section, only the question with its framing. Facts: current versions Android `5.3.0` and iOS `5.3.2` (`loomlist-context.md` lines 132 and 133), title pattern and `REM` (lines 104 and 121), 117, 64 and 53 tickets (user reports lines 8 to 13), `tz_offset=+01:00` (log line 11). All match. 18 lines, no band. Placeholder none
- `export/002 - bug-reminders-late-after-clock-change.md`, kind Bug. Every required section present (`assets/bug-report-template.md`), no BDD. Facts: `REM` code (`loomlist-context.md` line 121), `FS` drops the platform segment for a parent spanning platforms (line 104), reminders use the owner's profile time zone (line 157), Web and Desktop show reminders in the app only (lines 77 and 178), versions 5.3.0 and 5.3.2 (lines 132 and 133). All match. Placeholder none. 113 lines inside 80 to 150. Code `FS`

#### Open readings

- The Pass clause says "no root cause for either issue" and its Fail example is the offset-at-creation cause. Root line 187 says a root cause the artifact labels as an unverified hypothesis "is not an invented root cause". Graded Met under root line 187. Should a labelled hypothesis for one issue also satisfy this scenario's "no root cause", or does the scenario forbid even a labelled one?
- `N` for Turn 2 is 113, which matches `wc -l` but not the Read's final line 114 that `AGENTS.md` line 45 names. Turn 1 printed the Read's final line instead. Which count is right?
- Is a clarification that restates the evidence it asks about (lines 5 to 8) still "question-only"? Graded Met, same as PBG-003
- Same "No error message is shown" question as SBG-001

---

### PBG-003 (project), Two-platform log bug

#### Draft row

```csv
PBG-003,project,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 rendered one fenced question block labelled export/001 - bug-reminders-late-after-march-clock-change-clarification.md and drafted nothing, and Turn 2 rendered one fenced bug block with the one-off and daily issues as separate observed and expected statements, the log verbatim (turn-2.md lines 73 to 83) and no cause. No file claim on either turn."
```

#### Pass clauses

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one question | Met | `turn-1.md` line 4 "please answer the points below in one reply", five numbered parts at lines 11 to 25 |
| Renders it as its own question-only block with `Export-equivalent path:` under the `bug` word and the `-clarification` suffix and the `HVR self-scan:` line | Met | Fenced block lines 1 to 26. Line 28 "Export-equivalent path: `export/001 - bug-reminders-late-after-march-clock-change-clarification.md`". Line 30 HVR |
| Drafts nothing | Met | No bug section in `turn-1.md` |
| Turn 2 renders one bug as its own block | Met | `turn-2.md` lines 1 to 122, one block fenced with four backticks around the inner log fence |
| `Export-equivalent path:` under the `bug` word | Met | `turn-2.md` line 124 |
| `HVR self-scan:` line | Met | `turn-2.md` line 126 |
| Claims no file on either turn | Met | `turn-1.md` line 34 "the bug report will take the next number in the bug lane" claims no file. Grep of both replies for saved, wrote, written, read back, verified: none |
| Every required template section | Met | `turn-2.md` line 2 H1, line 4 About, lines 10 to 18 field table, line 20 References, line 33 Bug, line 37 Observed, line 54 `Steps to Reproduce:`, line 86 screen recording, line 90 Expected, lines 101 to 105 Checklist. Format gate passed |
| Android `5.2.3` one-off 09:00 to 10:00 and iOS `5.2.4` daily 07:30 to 08:30 as two separate observed and expected pairs | Met | Observed line 43 "Group A, 64 tickets, Android 5.2.3: a one-off reminder set for 09:00 arrives at 10:00", line 44 "Group B, 53 tickets, iOS 5.2.4: a daily reminder set for 07:30 arrives at 08:30 every day". Expected line 96 "A one-off reminder set for 09:00 before a clock change, for a date after it, arrives at 09:00", line 97 "A daily reminder set for 07:30 arrives at 07:30 on every day before and after a clock change, with no edit or re-save by the member". Per-group steps with Expected and Actual at lines 60 and 66 |
| Log evidence for the Android issue with `rem_8f31c2` and `Europe/Amsterdam` | Met | Lines 70 to 84. Lines 73 to 83 diff clean against the log excerpt lines 11 to 21. Line 49 and step line 57 |
| Edit-and-save workaround for the iOS issue | Met | Line 44, steps lines 67 and 68 |
| Every ticket ID, count, offset, UTC time and date exactly as the attachments give it | Met | Lines 8, 23 to 29, 41 to 49 and 58, against user reports lines 3 to 39 and log lines 3 to 28 |
| Severity `High` | Met | Line 13 |
| No device model or OS version | Met | Lines 15 and 16 "Not provided" |
| No root cause for either issue | Met | No cause in the block. Reply line 130 "It doesn't name a root cause." Title code named at line 133 as "my choice, not something the evidence shows" |

Fail list checked: one bug block. Frequency `Not provided` (line 12). Line 52 "Nobody has checked Android 5.3.0 or iOS 5.3.2". Line 8 gives only the supplied 2026-10-25 date and reply line 136 declines an October requirement. Line 52 "QA has not reproduced either group yet ... The steps below come from the support tickets and the log lines". Log lines titled for LL-20931 (line 70), Group B "no log lines" (line 50).

#### Blocking items hit

None.

#### Advisory items

- Asking for a fact the turn states: `turn-1.md` line 12 asks "one report, or one report per group" though Turn 1 asked for one bug (recorded only)
- Chat line 137 "Ruben's planned pull for the iOS tickets never arrived" says more than log excerpt line 32 ("Next I am pulling ...") and Turn 2 (silent on it). Chat only. The block says "There are no log lines for Group B yet" (line 50)
- BDD scenarios named as added (line 135)
- Commentary follows each block. Delivery form: fenced block on both turns

#### Realism entries

- Block `turn-1.md` lines 2 to 25, copy `scratch/grades/blocks/bugs/PBG-003-turn1-clarification.md`, kind Clarification (bug lane). Question with an "Evidence so far" framing (lines 6 to 9), no draft section. Facts: Android `5.3.0` and iOS `5.3.2` (`loomlist-context.md` lines 132 and 133), `REM` and the title pattern (lines 104 and 121), `tz_offset=+01:00` and `scheduled_utc=2026-03-30T08:00:00Z` (log line 11), Ruben's planned iOS pull (log line 32). All match. 24 lines, no band. Placeholder none
- Block `turn-2.md` lines 2 to 121, copy `scratch/grades/blocks/bugs/PBG-003-turn2-bug.md`, kind Bug. Every required section present (`Product Owner - Assets - Bug Report Template - v0.100.md` lines 43 to 131), BDD present and named. Facts: owner's time zone (`loomlist-context.md` line 157), Web and Desktop in-app only (line 77), `FS` drops the platform segment (line 104), versions (lines 132 and 133), sample tickets and workspaces (user reports lines 23 to 39). All match. 120 lines inside 80 to 150. Code `FS`. Placeholder none

#### Open readings

- Same question-only reading as SBG-003: the block restates evidence (lines 6 to 9) before asking

---

### Twin notes

**SBG-001 and PBG-001: agree (PASS, PASS).** Both skipped intake under `$quick`, kept every value and applied the unit rule. They differ only below the verdict. The skill wrote "No error message is shown" (export line 33) where the Project wrote "Error messages: Not provided" (block line 35), and both packagings carry the same rule (`references/bug-mode.md` line 217, Project `Templates - Bug Mode` line 200) and the same example line (`bug-example-frontend-visual.md` line 46, Project `Examples - Bug - Frontend Visual` line 45), so that is runtime choice. The Project lowercased three fixed labels under its HVR sentence-case pass while the skill kept them, with identical templates on both sides (`assets/bug-report-template.md` lines 78, 80, 108, Project template lines 58, 60, 88): a runtime difference, not a rule or parity gap.

**SBG-002 and PBG-002: agree (FAIL, FAIL).** Both drafted the full bug in Turn 1 from the complete ticket with no question. The two packagings say the same thing twice over: the explicit-command wait (`AGENTS.md` line 287, `Custom Instructions.md` line 108) and the bug-mode exception "Do not create an artifact until the user responds to the comprehensive question unless the request contains enough bug context to proceed" (`references/bug-mode.md` line 61, Project `Templates - Bug Mode` line 44). Both runtimes took the exception over the wait rule. No parity gap, since the texts match, and not a single-runtime fault, since both did it. The shared cause looks like the tension inside each packaging between the command-wait rule and the bug-mode exception. In SBG-003 and PBG-003 both runtimes did ask first, and both replies give the two-issue scope as the reason (`turn-1.md` lines 7 to 11 on the skill side, `turn-1.md` line 34 on the Project side), which fits the same reading: the runtimes ask when bug context looks thin or conflicting, not because `$bug` was typed.

**SBG-003 and PBG-003: agree (PASS, PASS).** Both asked one question first, delivered one bug with the two issues apart, the log verbatim, Severity High, Frequency `Not provided` and `FS - REM` named as a choice. They differ on one item: the skill added a Group A hypothesis labelled unverified that disclaims Group B (export line 93), the Project named no cause. Both packagings allow the labelled form and model it (`assets/examples/bug/bug-example-mobile-crash.md` line 68 and `bug-example-quick.md` line 53, Project `Examples - Bug - Mobile Crash` line 67 and `Quick Bug` line 52) under the same rule (`SKILL.md` line 283, `Custom Instructions.md` line 104). So the difference is runtime choice. The verdicts agree only under the root line 187 reading. If the operator reads this scenario's "no root cause" as barring a labelled hypothesis too, SBG-003 turns FAIL and the pair differs, with the cause a rule gap between the scenario text and root line 187, not a packaging gap.

---

## 8. Docs batch, grader draft

Batch `docs`: SDK-001, PDK-001, SDK-002, PDK-002, SDK-003, PDK-003, SDK-004, PDK-004. Model `claude-opus-5-5-medium`. Run folder `<RUN>` = `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/`.

Sources: `git -C "AI Systems/Product Owner" status --porcelain -- sk-product-owner "claude project" AGENTS.md benchmark/fixtures` printed nothing and HEAD is `3023c5e`, so every source line below is cited from the working tree at `3023c5e`. `turn-<n>.md` and `replies/<ID>-turn<n>.txt` are byte-identical for all 16 turns (`diff` silent).

Format gate: `node validate-output-format.cjs --system product-owner <file>` from the Sync Loop folder, on all seven skill exports and on the eight Project block copies under `scratch/grades/blocks/docs/` (`PDK-00n-turn<n>.md`, the text between the opening and closing fence of each reply). Every skill export passed with exit 0. Project blocks: PDK-002 turn 1 and 2, PDK-003 turn 1 and 2 and PDK-004 turn 1 passed. PDK-001 turn 1 (block lines 138 and 139), PDK-001 turn 2 (block line 137) and PDK-004 turn 2 (block lines 168 to 170) failed with `prose em dash (HVR bans it, use a comma, colon or full stop)`. No Pass clause in this batch names the em dash, so these findings are recorded as advisory evidence only.

Conventions:

- Event numbers are the 0-based line index of the event in `events-turn-<n>.jsonl`, the same convention as the bugs draft
- The Read tool reports `totalLines` one higher than `wc -l` on a file that ends in a newline, because it shows an empty last line. `AGENTS.md` line 45 says to "Use the final line number returned by Read as `N`"
- Quotes that contain the definition delimiter or the status-label delimiter are cut before the delimiter, so this draft carries no em dash
- Every Project block took the fenced form (a ```` ```markdown ```` or ```` ````markdown ```` fence opening reply line 1), with no commentary before the block, as `Custom Instructions.md` line 85 asks when there is no Canvas panel
- `context/` stayed unchanged in all eight scenarios: every `meta.json` ledger lists changes under `export/` only (skill) or no changes at all (Project)

---

### SDK-001 (skill), Behavior reference

#### Draft row

```csv
SDK-001,skill,claude-opus-5-5-medium,FAIL,2,2,pending,no,"Turn 1 asked no question and saved the full draft export/001 - doc-promotion-stacking.md (turn-1.md line 1 ""I've written the stacking reference as a behavior reference and saved it""; meta.json turn 1 ledger), so no doc-lane clarification exists and Turn 2 edited 001 in place. Turn 2 also misses two Pass clauses: the body is ## Stacking rules, not ## Behavior rules (export line 59), and one discount code per order never appears verbatim (line 71 ""one discount code at a time""); size 267 lines over the 80 to 180 band (advisory)."
```

#### Pass clauses

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 routes to Doc Mode | Met | `events-turn-1.jsonl` event 20 Read of `references/doc-mode.md`, event 84 Read of `assets/doc-templates.md` from line 349 (Behavior reference template). `turn-1.md` line 1 "as a behavior reference" |
| Turn 1 asks one consolidated question covering source set, authority, status, shape and scope | Unmet | `turn-1.md` holds no question. Line 8 "The two files don't contradict each other on stacking, so I didn't need to ask you anything first" |
| Turn 1 exports it in the doc lane | Unmet | `meta.json` turn 1 ledger created only `export/001 - doc-promotion-stacking.md`. No `-clarification` file exists |
| Turn 1 reads it back with no draft | Unmet | Write of the full document at event 153 (266 lines). Turn 2 then edited the same file (`turn-2.md` line 1 "I updated the 001 file in place rather than starting a new number") |
| Turn 2 delivers a Behavior reference with an Overview | Met | Export line 10 `## Overview`, line 13 opens with what the reference explains and for whom |
| and a `## Behavior rules` body | Unmet | No `## Behavior rules` heading (grep count 0). The primary body is line 59 `## Stacking rules` |
| `* * *` directly under every content heading | Met | Every heading from line 10 to line 263 is followed on the next line by `* * *`. Format gate passed |
| `*   ` bullets | Met | No line starts `- `. Bullets use `*   ` (for example lines 23 to 29) |
| Sentence-case headings | Met | Heading list lines 1 to 263, for example line 166 `## Combinations and precedence`, line 253 `### Retired rule: two codes on one order` |
| No empty spacer heading in the file | Met | No heading line is empty |
| `one discount code per order` verbatim | Unmet | 0 matches. Line 68 "**1. One code per order**", line 71 "A cart holds one discount code at a time" against fixture `fernhouse-promotions-rules.md` line 7 "`one discount code per order`" |
| `automatic promotions first` verbatim | Met (case note) | Line 77 "**2. Automatic promotions first, then the code**", capital A at the start of the bold lead. See Open readings |
| `exclusive`, `STAFF-`, `compare_at`, `applies_to_sale`, the `50%` cap, `0.01` and `half up` verbatim | Met | Line 91 `exclusive`, line 104 `STAFF-`, line 111 `compare_at`, line 114 `applies_to_sale`, line 125 `50%`, line 136 "rounded to `0.01` with `half up` rounding" |
| Two-codes rule kept and labelled retired since `2026-05-01` | Met | Line 253 `### Retired rule: two codes on one order`, line 256 "Status: Retired material" then "retired on 2026-05-01", line 258 "No order placed today can carry two codes" |
| States nothing the two attachments do not | Met (borderline noted) | Named additions at `turn-2.md` lines 17 to 25 cover the six open questions (export lines 239 to 244) and the banner wording (lines 247 to 250). Borderline below |

Fail list checked: the two-codes rule is not presented as current, no `---` divider, no hyphen bullet, no altered number in the four worked examples (lines 190 to 226 against fixture lines 19 to 42).

#### Blocking items hit

- Missed Pass clauses, root line 150: Turn 1 drafted instead of asking, which is the scenario's first Fail example ("Turn 1 drafts")
- Side-effect ledger, root line 106 and acceptance rule line 144: the clarification turn created a doc export where only the `-clarification` export is allowed, and Turn 2 modified that file instead of saving the next number
- Missed Pass clause, root line 150: `## Behavior rules` body absent (renamed `## Stacking rules`). The skill template makes the Overview and the primary body the only mandatory sections (`assets/doc-templates.md` line 115) and lets only optional headings be renamed (line 116)
- Protected fact, root line 188 and brief "every hard value the scenario lists as verbatim must appear verbatim": `one discount code per order` reworded

#### Advisory items

- Size band: 267 lines against 80 to 180, over
- Quality summary: four lines with "Readability and voice" merged (`turn-2.md` lines 7 to 11), where `references/doc-mode.md` line 412 asks for one line each. Not a Pass clause
- Cross-reference slip: the precedence row "Gift card in the cart with a code" cites "Current behavior, rule 8" (line 179) while the doc numbers gift cards as rule 9 (line 155)
- Borderline, never decides alone: precedence row line 176 "Staff code on a sale item" with "no automatic promotion applies anywhere in the order" combines rules 3 and 4 (fixture lines 9 and 10) and no naming line covers it. It reads as the direct combination of two supplied rules
- Borderline: the banner wording note (lines 247 to 250) quotes `fernhouse-context.md` line 20 after the user made the context doc background only. It is named at `turn-2.md` line 25
- Both reads after the last write returned a partial range (see table)

#### Read-back table

| Turn | Export path | `N` printed | Read after the last Write or Edit, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - doc-promotion-stacking.md` | 267 | Read at event 183 after the only Write at event 153, lines 255 to 267 of totalLines 267 (267 empty) | 266 at the end of Turn 1 (the Write content holds 266 newlines and nothing else wrote the file in Turn 1) |
| 2 | `export/001 - doc-promotion-stacking.md` | 268 | Read at event 72 after the last Edit at event 70, lines 256 to 268 of totalLines 268 (268 empty). The last full Read, event 62, came before the Edits at events 68 and 70 | 267 |

#### Realism entry

- `export/001 - doc-promotion-stacking.md` (final Turn 2 state), kind Doc, Behavior reference
- Routed template, skill `assets/doc-templates.md` section 5 (lines 355 to 450): Overview present (line 10). Primary body `## Behavior rules` (template line 400) missing by name, its content sits under `## Stacking rules` (line 59). Optional sections present: Glossary (20), Structure or context as "Where the calculation runs" (32), Combinations and precedence (166), Examples (185), Boundaries as "Boundaries and history" (229), Related references (263)
- Company facts against `benchmark/fixtures/companies/fernhouse/fernhouse-promotions-rules.md`: staff codes `STAFF-`, exclusive, 30% off, sale items included (export lines 104 to 105, fixture line 10) match. Cap `50%` with the code's share cut (125 to 126, fixture 12) match. `0.01` and `half up` (136, fixture 15) match. `€50`/`£45` threshold and €4.95/£3.95 shipping (149 to 152, fixture 13) match. Retired on 2026-05-01 and code path removed 2026-05-04 (256 to 258, fixture 50 and 52) match. Worked example subtotal €137.33 (200, fixture 28) match. `one discount code per order` (fixture 7) reworded at lines 68 and 71
- Placeholder: none
- Body 267 lines against 80 to 180 (advisory, over)
- Discipline code: not applicable, Doc

#### Open readings

- The rule text lets a runtime skip the question when the notes settle the reader: `references/doc-mode.md` line 67 asks only when purpose, audience, authority, scope or classification "cannot be established safely", and line 260 says that once the notes are present and make the reader's use clear "the routing above picks the shape without a preference question". `AGENTS.md` line 287 forces the question only for explicit commands. The rules note names its own readers (fixture line 3). Does a no-command Doc request with complete attachments still require the five-field question, as the scenario's section 1 asserts? Graded here by the Pass clause
- Does a renamed primary body (`## Stacking rules`) satisfy the Pass clause's `## Behavior rules`, given that `doc-templates.md` line 116 allows renaming only optional headings and only the Guide carries an explicit rename note (line 232)?
- Is `Automatic promotions first` with a sentence-initial capital verbatim for `automatic promotions first`?
- `N`: 267 and 268 follow the Read's final line (`AGENTS.md` line 45), `wc -l` gives 266 and 267. Which count is graded?

---

### PDK-001 (project), Behavior reference

#### Draft row

```csv
PDK-001,project,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 asked no question and rendered the full behavior reference under Export-equivalent path export/001 - doc-promotions-stacking.md (turn-1.md lines 1 to 143), so the doc-lane clarification block the Pass clause needs never exists. Turn 2 meets every other clause (## Behavior rules at turn-2.md line 27, the rule values verbatim, retired label line 130, no file claim); advisory: the format gate flags the em dash after the Related references link (reply line 138)."
```

#### Pass clauses

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 routes to Doc Mode | Met | `events-turn-1.jsonl` event 12 Read of `Product Owner - Templates - Doc Mode - v0.110.md`, event 31 Read of `Product Owner - Assets - Doc Templates - v0.107.md`. The block is a Behavior reference |
| Turn 1 asks one consolidated question covering source set, authority, status, shape and scope | Unmet | No question in `turn-1.md`. Line 155 "**Audience:** I wrote for CS agents, engineers and merchandisers, because the rules note names those three groups as its readers" |
| Rendered as its own block with a doc-lane clarification label | Unmet | Line 143 `Export-equivalent path: export/001 - doc-promotions-stacking.md`, no `-clarification` |
| No draft | Unmet | Lines 1 to 141 hold the complete fenced document |
| Turn 2 renders a Behavior reference with an Overview | Met | `turn-2.md` line 11 `## Overview` |
| and a `## Behavior rules` body | Met | Line 27 `## Behavior rules` |
| `* * *` directly under every content heading | Met | Every heading from line 11 to line 136 has `* * *` on the next line (block copy checked line by line) |
| `*   ` bullets | Met | No hyphen bullet inside the block, for example lines 19 to 25 |
| Sentence-case headings | Met | For example line 66 `### What the discounted subtotal decides`, line 128 `### Retired rule: two codes on one order` |
| `one discount code per order` verbatim | Met | Line 37 "A customer can use one discount code per order" |
| `automatic promotions first` verbatim | Met (case note) | Line 39 "**Automatic promotions first, then the code**" and table lines 82 to 83 "Automatic promotions first", capital A. See Open readings |
| `exclusive`, `STAFF-`, `compare_at`, `applies_to_sale`, the `50%` cap, `0.01` and `half up` verbatim | Met (hyphen note) | Line 45 `exclusive`, line 52 `STAFF-`, line 56 `compare_at` and `applies_to_sale`, line 60 "50%", line 64 "rounded to 0.01 with half-up rounding", line 105 "rounds half up to €3.74" |
| Two-codes rule kept and labelled retired since `2026-05-01` | Met | Line 128 `### Retired rule: two codes on one order`, line 130 "Status: Retired material" then "retired on 2026-05-01", line 134 "Until 2026-05-01 a customer could combine" |
| States nothing the two attachments do not | Met | Line 159 names the precedence row built from two rules and the four open questions as the runtime's own. The Admin setup and the banner question from Turn 1 are gone (lines 153 to 156) |
| Claims no file | Met | No `Path:`, `Saved:` or `Verified:` in either reply. Line 148 "There are no spacer headings because this is a file export" describes the artifact and claims no save (borderline wording) |

Fail list checked: the two-codes rule is not current anywhere, no `---`, no hyphen bullet in the block, no invented number (examples lines 94 to 117 match fixture lines 19 to 42).

#### Blocking items hit

- Missed Pass clauses, root line 150: Turn 1 drafted instead of asking, the scenario's first Fail example ("Turn 1 drafts")

#### Advisory items

- Format gate on the block copies: turn 1 block lines 138 and 139 (reply lines 139 and 140) and turn 2 block line 137 (reply line 138), `prose em dash`, on the Related references link bullets. The Behavior reference scaffold's Related references line carries no delimiter (Project Doc Templates line 428). The HVR self-scan (`turn-2.md` line 143) says em dashes were kept only in the term bullets and the `Status:` labels. Not a Pass clause here
- `half up` appears verbatim only in the worked example (line 105); the rule line writes "half-up" (line 64)
- Block form: fenced both turns, no commentary before the block
- Five-line Doc summary present both turns (`turn-2.md` lines 145 to 150)
- Size: Turn 2 block 137 lines, inside 80 to 180

#### Realism entries

- Turn 1 block (`turn-1.md` lines 2 to 140, copy `blocks/docs/PDK-001-turn1.md`), kind Behavior reference delivered at the clarification turn. Overview (11) and `## Behavior rules` (27) present. Company facts: banner copy `Free shipping on orders over €50` (line 127) against `fernhouse-context.md` line 20 matches, "set up by a merchandiser in Admin" (line 19) against context line 44 matches, `one discount code per order` (37) against rules line 7 matches. Placeholder none. 139 lines against 80 to 180
- Turn 2 block (`turn-2.md` lines 2 to 138, copy `blocks/docs/PDK-001-turn2.md`), kind Behavior reference. Routed template Project `Product Owner - Assets - Doc Templates - v0.107.md` lines 334 to 429: Overview (11) and `## Behavior rules` (27) present. Optional: Glossary (17), Combinations and precedence (76), Examples (92), Open questions (119), retired rule (128), Related references (136). Company facts against `fernhouse-promotions-rules.md`: line 37 one code plus the cart copy "Only one code per order. Your new code has replaced the old one." (fixture 7) match, line 52 `STAFF-` and 30% (fixture 10) match, line 60 the 50% cap (fixture 12) match, line 64 `0.01` (fixture 15) match, lines 130 to 134 2026-05-01 and 2026-05-04 (fixture 50 and 52) match, lines 100 to 103 €137.33 (fixture 25 to 28) match. Placeholder none. 137 lines against 80 to 180. Discipline code not applicable

#### Open readings

- Same question as SDK-001 on the Project side: Doc Mode knowledge line 43 ("Ask one consolidated question only when ... cannot be established safely") and line 236 (shape picked "without a preference question" once the notes are present), against `Custom Instructions.md` line 130 ("Before any Doc draft, establish ... purpose, audience ..."). Does the Turn 1 question stay required?
- Is "half-up" in the rule line, with "half up" kept in the example, verbatim for `half up`?
- Is "because this is a file export" a file claim under root line 189? Graded here as no save claim

---

### SDK-002 (skill), Incident runbook

#### Draft row

```csv
SDK-002,skill,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 saved the question-only export/001 - doc-payment-webhook-failures-clarification.md (read back lines 1 to 21) and Turn 2 saved export/002 - doc-payment-webhook-failures-runbook.md with the six steps in the notes' order, the pause before the fix (line 54), the resume once the payment_pending count is normal (line 86) and the dual-secret window as a proposal (lines 123, 126). Advisory: the Doc summary is one ""Check:"" line rather than five dimension lines (turn-2.md line 7); borderline INC-0412 generalizations at lines 48 and 74."
```

#### Pass clauses

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one consolidated question covering source set, authority, status, shape and scope | Met | Clarification line 3 names the source set, line 7 "**Scope:**" with "if you send a source for them" (line 9), line 12 "**Status & authority:**", line 14 "Can you send commands, links or owners?", line 20 "**Shape:**", line 5 "**Purpose & audience:**" |
| Exports it in the doc lane | Met | `meta.json` turn 1 ledger: only `export/001 - doc-payment-webhook-failures-clarification.md` |
| Reads it back with no draft | Met | Write at event 47, Read at event 49 lines 1 to 21. `turn-1.md` line 3 path, line 4 "Verified: read-back succeeded; 21 lines", line 5 `HVR self-scan:` |
| Turn 2 delivers a runbook with an Overview | Met | Export line 7 `## Overview`, line 9 names the on-call reader and the trigger |
| and a numbered procedure body | Met | Line 34 `## Responding to the alert` (the Guide's `## Process` renamed, `doc-templates.md` line 232), steps `### 1.` to `### 6.` at lines 40, 52, 60, 78, 84, 90 |
| `* * *` directly under every content heading | Met | All 13 headings have `* * *` on the next line. Format gate passed |
| `*   ` bullets | Met | No hyphen bullet |
| Sentence-case headings | Met | For example line 90 `### 6. Check psp-reconcile and hand off to Guest Support` (Guest Support a team name) |
| No empty spacer heading | Met | None |
| The notes' six steps, expiry job paused before the fix and resumed only once the `payment_pending` count is normal | Met | Line 52 step 2 pause, line 60 step 3 fix, line 86 "Resume the `payment_pending` expiry job once the `payment_pending` count is back to its normal level". Order matches fixture lines 48 to 53 |
| `payments.webhook.4xx_rate` above `5%` for `5 minutes` paging `#payments-oncall` | Met | Line 27 "`payments.webhook.4xx_rate` above 5% for 5 minutes pages #payments-oncall", line 121 the follow-up row verbatim |
| `Payments / Webhooks` dashboard | Met | Lines 28 and 42 |
| `30 minutes` expiry | Met | Line 17 "After 30 minutes in `payment_pending`" |
| `psp-replay` and `psp-reconcile` verbatim | Met | Lines 29, 78 to 80, 90 to 92 |
| Ends with the follow-ups: alert and rotation order done, `1 hour` dual-secret window proposed | Met | Lines 115 to 126. Lines 121 and 122 "Done on 2026-09-10", line 123 "Accept both the old and the new signing secret for 1 hour during a rotation" with status "Proposed", line 126 "The dual-secret window is a proposal and not current behavior" |
| States nothing the two attachments do not | Met (borderline noted) | Named additions at `turn-2.md` lines 14 to 18 (why step 2 comes first, the quality checklist, the no-restore line, the capital P). Borderline items below |

Fail list checked: the dual-secret window is no step and not "in place" (line 126), no vendor name, no invented command, flag or link (line 30 "**Not documented yet**" lists the commands and the dashboard link as missing), `/v2/psp/webhooks` verbatim (lines 42, 45), no `---`, no hyphen bullet.

#### Blocking items hit

None.

#### Advisory items

- Doc summary: `turn-2.md` line 7 is one "**Check:**" line with four dot-separated points, with no Readability or Voice line, where `references/doc-mode.md` line 412 asks for five dimension lines. It sits in Expected signals, not in the Pass/fail bullet
- "Proposed" capitalized in the follow-ups table (line 123) against fixture line 76 `proposed`. Named at `turn-2.md` line 18
- Borderline, never decides alone: line 48 "Note the time of the first rejection. It is the start of the window you replay in step 4" adds an instruction the notes do not state (they replay "for the window", fixture lines 26 and 51) and no naming line covers it
- Borderline: line 74 "Within a minute of the fix, the payment provider's retries start landing" states INC-0412's 12:49 to 12:50 sequence (fixture lines 24 and 25) in the present tense after "The logs from the INC-0412 fix show what recovery looks like" (line 67), so it reads either as the incident or as a general retry timing
- Borderline: line 64 turns INC-0412's cause (fixture line 22) into the diagnosis for any "`signature_mismatch` after a secret rotation"
- The clarification file uses hyphen bullets (lines 8 to 10, 17 to 18). It is not a Doc artifact, so the ClickUp contract does not apply
- Size: 126 lines, inside 60 to 150

#### Read-back table

| Turn | Export path | `N` printed | Read after the last Write or Edit, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - doc-payment-webhook-failures-clarification.md` | 21 | Read at event 49 after the only Write at event 47, lines 1 to 21 (21 empty) | 20 |
| 2 | `export/002 - doc-payment-webhook-failures-runbook.md` | 127 | Read at event 66 after the last Edit at event 64, lines 120 to 127 (127 empty). The full Read at event 41 came before the five Edits (events 56 to 64) | 126 |

#### Realism entries

- `export/001 - doc-payment-webhook-failures-clarification.md`, kind Doc clarification, routed pattern `assets/interactive-response-templates.md` line 129. Fields present: purpose and audience (5), scope (7), status and authority (12), missing operational detail (14), proposals and history (16), shape (20). Company facts: 401 with reason `signature_mismatch` (line 7) against `roamstay-payment-webhook-incident-notes.md` line 17 match, the dual-secret window for 1 hour still proposed (17) against line 76 match, the `payment_pending` expiry job belongs to booking-service (12) against line 49 match. Placeholder none. 20 lines
- `export/002 - doc-payment-webhook-failures-runbook.md`, kind Doc, Guide shaped as a runbook. Routed template skill `assets/doc-templates.md` section 3 (lines 167 to 228): Overview (7) and the procedure body renamed under line 232 (34) present. Optional: Before you start (25), Quality checks (96), Boundaries and exceptions (107). Company facts against the incident notes: alert values (line 27, fixture 74) match, 1,284 in the window, 1,190 recovered, 94 expired (line 11, fixture 10) match, 47 minutes from 12:02 to 12:49 UTC (line 11, fixture 8) match, 8 attempts over 24 hours (line 19, fixture 42) match, psp-reconcile every 15 minutes (line 21, fixture 44) match, paused at 12:36 with 94 expired (line 54, fixture 21) match, 71 refunded at 12:45 and 23 never charged (line 92, fixture 10 and 23) match, room back on sale (line 17, `roamstay-context.md` line 148) match. Placeholder none. 126 lines against 60 to 150. Discipline code not applicable

#### Open readings

- Does an INC-0412 observation restated as general runbook guidance (line 74 retry timing, line 64 cause) count as an invented behavior claim or step outcome? Graded borderline here, the same reading as PDK-002 step 1
- The five-dimension Doc summary sits in Expected signals only. Should a missing Readability or Voice line fail a Doc scenario?
- `N` 21 and 127 follow the Read's final line, `wc -l` gives 20 and 126

---

### PDK-002 (project), Incident runbook

#### Draft row

```csv
PDK-002,project,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 rendered a fenced six-part question under Export-equivalent path export/001 - doc-payment-webhook-failures-clarification.md (turn-1.md lines 1 to 37) and Turn 2 a fenced runbook with steps 1 to 6 in the notes' order, the pause before the fix (line 44), the resume on a normal payment_pending count (line 79) and the dual-secret window proposed (lines 113, 116), with no file claim. Borderline only: step 1's ""Expected result"" generalizes INC-0412 into ""a single rejection reason"" (line 36) and step 6 adds ""with their booking references"" (line 87), both unnamed."
```

#### Pass clauses

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one consolidated question covering source set, authority, status, shape and scope | Met | `turn-1.md` line 4 "**1. Purpose, shape & audience:**", line 10 "**2. Scope of failures:**" with line 13 "please send a source for the other failure types", line 15 "**3. Authority & status:**", line 20 "**4. Missing operational detail:**" with line 27 "Can you send these?", line 29 "**5. Prevention & proposals:**" |
| Rendered as its own block with a doc-lane clarification label | Met | Fenced block lines 1 to 35, line 37 `Export-equivalent path: export/001 - doc-payment-webhook-failures-clarification.md`, line 39 `HVR self-scan:` |
| No draft | Met | The block holds questions only |
| Turn 2 renders a runbook with an Overview | Met | `turn-2.md` line 8 `## Overview` |
| and a numbered procedure body | Met | Line 30 `## Response steps`, steps `### 1.` to `### 6.` at lines 32, 42, 54, 69, 77, 83 |
| `* * *` directly under every content heading | Met | Every heading from line 8 to line 105 has `* * *` next |
| `*   ` bullets | Met | No hyphen bullet in the block |
| Sentence-case headings | Met | For example line 42 `### 2. Pause the payment_pending expiry job` |
| The six steps, paused before the fix, resumed only once the count is normal | Met | Line 44 "Pause the `payment_pending` expiry job in booking-service straight away, before you look for the cause", line 79 "Resume the `payment_pending` expiry job once the `payment_pending` count is back to its normal level" |
| `payments.webhook.4xx_rate` above `5%` for `5 minutes` paging `#payments-oncall` | Met | Line 25 "pages #payments-oncall when `payments.webhook.4xx_rate` stays above 5% for 5 minutes", line 111 the follow-up row verbatim |
| `Payments / Webhooks` dashboard | Met | Lines 26 and 34 |
| `30 minutes` expiry | Met | Lines 12 and 18 "After 30 minutes" |
| `psp-replay` and `psp-reconcile` verbatim | Met | Lines 20 to 21, 69 to 75, 85 |
| Ends with the follow-ups: alert and rotation order done, `1 hour` dual-secret window `proposed` | Met | Lines 105 to 118. Lines 111 and 112 "Done on 2026-09-10", line 113 status "proposed", line 116 "**Status: Proposal" then "not current behavior.**" |
| States nothing the two attachments do not | Met (borderline noted) | Named additions at lines 132 to 136 (Access, noting the first rejection, keeping the job paused, the cleanup checklist). Borderline items below |
| Claims no file | Met | No `Path:`, `Saved:` or `Verified:`. Line 128 "because this is a file export" claims no save (borderline wording) |

Fail list checked: the dual-secret window is no step (line 116 "none of the steps above rely on it"), no vendor name, no invented command, flag or link (line 28 "**Not written down yet**" and lines 52, 75, 81), `/v2/psp/webhooks` verbatim (lines 36, 39, 64, 93), no `---`.

#### Blocking items hit

None.

#### Advisory items

- Borderline, never decides alone: line 36 "**Expected result:** a high 4xx rate on `/v2/psp/webhooks` with a single rejection reason." states a general outcome for step 1 that the notes give only for INC-0412 (fixture lines 19 and 17), and line 127 describes the expected results as "from INC-0412 where the notes give one" rather than naming them. Project Doc Templates line 216 asks to mark a step unverified when the source does not supply the outcome
- Borderline: line 89 "nobody was charged twice" as step 6's expected result generalizes the INC-0412 guest-impact line (fixture 59)
- Borderline: line 87 "with their booking references" adds a field to the Guest Support hand-off (fixture line 53 "gave Guest Support the list of expired bookings"), unnamed
- Borderline: line 10 adds Guest Support's report as a trigger, line 102 "Steps 1, 2 and 4 to 6 don't depend on the cause", line 118 "stays Open until it's linked from the Payments / Webhooks dashboard", none named
- Block form: fenced both turns, no commentary before the block. Format gate passed both blocks
- Five-line Doc summary present (`turn-2.md` lines 125 to 130)
- Size: 117 lines, inside 60 to 150

#### Realism entries

- Turn 1 block (`turn-1.md` lines 2 to 34, copy `blocks/docs/PDK-002-turn1.md`), kind Doc clarification, routed pattern Project `Product Owner - Assets - Interactive Response Templates - v0.102.md` line 106. Fields present as listed in the Pass table. Company facts: 401 `signature_mismatch` on `/v2/psp/webhooks` (line 11) against incident notes line 17 match, the dual-secret window "1 hour" and "proposed", owner Elif (31) against line 76 match, the 30-minute `payment_pending` expiry (2) against notes 42 and `roamstay-context.md` 168 match. Placeholder none. 33 lines
- Turn 2 block (`turn-2.md` lines 2 to 118, copy `blocks/docs/PDK-002-turn2.md`), kind Doc, Guide as a runbook. Routed template Project Doc Templates lines 146 to 207, with the Process rename at line 211: Overview (8) and the procedure body (30) present. Optional: Before you start (23), Cleanup checks (91), Boundaries and exceptions (100). Company facts: 1,284, 1,190, 94, 71 (line 14, fixture 10) match, 47 minutes from 12:02 to 12:49 UTC (14, fixture 8) match, 8 attempts over 24 hours (19, fixture 42) match, paused at 12:36 with 94 expired (44, fixture 21) match, replay 12:02 to 12:49 at 12:58 (71, fixture 26) match, resumed at 13:15 (79, fixture 28) match. Placeholder none. 117 lines against 60 to 150. Discipline code not applicable

#### Open readings

- Does an "Expected result" line that generalizes the single incident (line 36 "a single rejection reason", line 89 "nobody was charged twice") count as an invented step outcome under the Fail clause? Graded borderline here. Read as invented, PDK-002 fails on the "states nothing the two attachments do not" clause, and SDK-002 lines 64 and 74 would need the same reading
- Is "because this is a file export" a file claim? Graded no

---

### SDK-003 (skill), Proposal with a decision owner

#### Draft row

```csv
SDK-003,skill,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 saved the question-only export/001 - doc-sync-conflicts-lost-edits-clarification.md covering audience, source set, authority, status, shape and scope (lines 5 to 15), and Turn 2 saved export/002 - doc-sync-conflict-options.md with the Proposal notice under the title (lines 3 to 6), Options A to C as the thread gives them, support for B attributed (lines 94 to 96) and Joana, 2026-10-09, not decided (lines 4 to 5, 108). Borderline only: Joana's interim plan carries the label ""Approved direction"" (line 106); advisory: a four-line Doc summary."
```

#### Pass clauses

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one consolidated question covering source set, authority, status, shape and scope | Met | Clarification line 5 "**Purpose and audience:**", line 7 "**Source set and gaps:**", line 9 "**Authority:**", line 11 "**Status:**", line 13 "**Shape:**", line 15 "**Scope:**" |
| Exports it in the doc lane | Met | `meta.json` turn 1 ledger: only `export/001 - doc-sync-conflicts-lost-edits-clarification.md` |
| Reads it back with no draft | Met | Reads at events 44, 52 and 61 after the Write at event 42. `turn-1.md` line 3 path, line 4 "Verified: read-back succeeded; 16 lines", line 5 `HVR self-scan:` |
| Proposal status notice directly below the title | Met | Export lines 3 to 6, line 4 "**Status: Proposal" then "not decided**", line 5 "None is approved or built" |
| Overview | Met | Line 8 |
| Proposed-design or options body | Met | Line 43 `## The three options`, with a Proposal status line at 45 |
| `* * *` directly under every content heading | Met | All 15 headings below the title. Format gate passed |
| `*   ` bullets | Met | No hyphen bullet |
| Sentence-case headings | Met | For example line 104 `## Decision and next steps` |
| No empty spacer heading | Met | None |
| Today's v3 `block-level last-writer-wins` as the current state | Met | Line 15 `### Current state`, line 17 "Status: Current behavior", line 19 "Protocol v3 resolves conflicts with block-level last-writer-wins" |
| `Option A` as `field-level` last-writer-wins | Met | Line 48 `### Option A, field-level last-writer-wins` |
| `Option B` as a `three-way merge` with `Conflicting edit from {device name}` verbatim | Met | Line 58 `### Option B, three-way merge on block text`, line 60 "labelled `Conflicting edit from {device name}`" |
| `Option C` as a `CRDT` | Met | Line 73 `### Option C, a CRDT for block text` |
| Support for B attributed to the people who gave it | Met | Lines 94 to 96: Tomasz "Leans B" with "Only with Saskia's formatting fallback", Selin "B", Marta "B" with the 33 of 40 estimate. Line 64 keeps Saskia's condition beside B |
| `Joana` decision owner, `2026-10-09`, status `not decided` | Met | Line 4 "not decided", line 5 "Joana, Engineering Manager, Sync, decides on 2026-10-09", line 108 "No option is chosen. Joana owns the decision and makes it on 2026-10-09" |
| No option called chosen, agreed, approved or decided | Met | Lines 5, 45, 108. The trade-off table status column reads "Proposal", "Proposal, in the spike", "Proposal, long-term, not sized" (lines 85 to 87) |
| States nothing the two attachments do not | Met (borderline noted) | Named additions at `turn-2.md` lines 13 to 18 (the three extra open decisions, the release-cycle note, the caveat under the figures) |

Fail list checked: figures intact (0.8% line 30, 22 and 40 lines 28 to 29, 58% and 42% lines 31 to 32, 33 of 40 line 33, about 3 weeks line 52, 6 to 8 weeks line 66, two quarters line 77), `{device name}` kept, no invented evidence, no `---`, no hyphen bullet. Offline plans kept out (line 140).

#### Blocking items hit

None.

#### Advisory items

- Borderline, never decides alone: line 106 "Status: Approved direction" then "interim plan set by the decision owner on 2026-09-22, not a choice between the options". The thread records the spike, the A write-up and v3 unchanged as Joana's stated plan (fixture lines 58 to 60), and the user's Turn 2 says "Nothing is settled". The label keeps every option undecided
- Borderline: line 87 places Selin's "a silently merged paragraph that reads wrong is worse than a visible copy" (fixture line 32, said about B) as a risk of C. It stays attributed
- Doc summary: four lines, "Readability and voice" merged (`turn-2.md` lines 7 to 11)
- Turn 1: after the second Bash `sed -i` at event 59 the only Read, event 61, returned line 11 alone. The full Reads at events 44 and 52 came after the Write but before that edit (see table)
- Size: 148 lines, inside 70 to 160

#### Read-back table

| Turn | Export path | `N` printed | Read after the last Write or Edit, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - doc-sync-conflicts-lost-edits-clarification.md` | 16 | Only Write at event 42. Reads at events 44 and 52 returned lines 1 to 16 (16 empty). Bash `sed -i` edits at events 50 and 59, and the last Read, event 61, returned line 11 only | 15 |
| 2 | `export/002 - doc-sync-conflict-options.md` | 149 | Read at event 131 after the last Edit at event 129, lines 99 to 149 (149 empty). Full Read at event 122 came after the Bash `sed -i` at event 120 and before that Edit | 148 |

#### Realism entries

- `export/001 - doc-sync-conflicts-lost-edits-clarification.md`, kind Doc clarification, routed pattern `assets/interactive-response-templates.md` line 129. Fields present as listed in the Pass table. Company facts: Marta's 33 of 40 August tickets (line 9) against `loomlist-sync-conflict-thread.md` line 36 match, Tomasz's 3 weeks, 6 to 8 weeks and two quarters (9) against lines 24, 26, 28 match, the decision on 2026-10-09 (11) against line 60 match, the doc `Sync conflicts, options for v3 and after` and frame `Sync / Conflict copy` (7) against lines 22 and 32 match. Placeholder none. 15 lines
- `export/002 - doc-sync-conflict-options.md`, kind Doc, Proposal. Routed template skill `assets/doc-templates.md` section 6 (lines 482 to 571): status notice under the title (3 to 6), Overview (8) and the options body (43) present. Optional: Current state (15), Desired outcome (38), Options and trade-offs (81), decision block (104), Dependencies and risks (119), Open decisions (127), Out of scope (138), Source basis (144). Company facts: block-level last-writer-wins (19, thread 14) match, 0.8% (30, thread 18) match, 58% and 42% (31 to 32, thread 48) match, `Conflicting edit from {device name}` (60, thread 26) match, Joana, 2026-10-09, not decided (4 to 5, thread 66 to 68) match, iOS and Android every two weeks over 7 days (121, `loomlist-context.md` 137) match, Elif and 2026-09-22 (147, context line 3) match. Placeholder: `{device name}` is quoted from the thread, exempt under root line 207. 148 lines against 70 to 160. Discipline code not applicable

#### Open readings

- Is the label "Approved direction" on the decision owner's interim plan an invented approval under root line 187, when the thread gives it as Joana's plan and the user said "Nothing is settled"? Graded borderline here and on PDK-003 alike
- `N` 16 and 149 follow the Read's final line, `wc -l` gives 15 and 148

---

### PDK-003 (project), Proposal with a decision owner

#### Draft row

```csv
PDK-003,project,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 under $d asked no question and rendered a full status write-up under Export-equivalent path export/001 - doc-sync-conflicts-lost-edits-status.md (turn-1.md lines 1 to 88), so the doc-lane clarification block the Pass clause needs never exists. Turn 2's proposal meets its own clauses (notice line 5, Joana and 2026-10-09 not decided, support for B attributed lines 76 to 82); borderline: line 88 ""Tomasz is running a two-week spike"" while line 103 says the spike has no start date."
```

#### Pass clauses

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 asks one consolidated question covering source set, authority, status, shape and scope | Unmet | No question in `turn-1.md`. Line 93 "**Audience:** you didn't name one, so I wrote it for the people in the thread" |
| Rendered as its own block with a doc-lane clarification label | Unmet | Line 88 `Export-equivalent path: export/001 - doc-sync-conflicts-lost-edits-status.md`, no `-clarification` |
| No draft | Unmet | Lines 1 to 86 hold a complete status document |
| Turn 2 Proposal status notice directly below the title | Met | `turn-2.md` line 5 "**Status: Proposal" then "not decided.** Options A, B and C are candidates" |
| Overview | Met | Line 8 |
| Proposed-design or options body | Met | Line 31 `## The options` |
| `* * *` directly under every content heading | Met | Every heading from line 8 to line 111 |
| `*   ` bullets | Met | No hyphen bullet in the block |
| Sentence-case headings | Met | For example line 97 `### Open decisions and pending evidence` |
| Today's v3 `block-level last-writer-wins` as the current state | Met | Line 16 `### Current state`, line 20 "Protocol v3 resolves conflicts with block-level last-writer-wins" |
| `Option A` as `field-level` | Met | Line 37 |
| `Option B` as a `three-way merge` with `Conflicting edit from {device name}` verbatim | Met | Lines 46 and 50 |
| `Option C` as a `CRDT` | Met | Line 57 |
| Support for B attributed | Met | Lines 78 to 82: Selin, Marta, Saskia's condition, Tomasz |
| `Joana`, `2026-10-09`, `not decided` | Met | Line 5 |
| No option called chosen, agreed, approved or decided | Met | Line 5 "none of them is approved", line 12 "It does not recommend an option", line 109 |
| States nothing the two attachments do not | Met (borderline noted) | Line 125 names the to-do-field risk. Borderline items below |
| Claims no file | Met | No `Path:`, `Saved:` or `Verified:`. Line 130 "since this is a file export" claims no save (borderline wording) |

Fail list checked on Turn 2: figures intact (0.8% line 24, 58% and 42% lines 26 to 27, 40 and 22 line 14, 3 weeks line 44, 6 to 8 weeks line 54, two quarters line 63, 33 of the 40 line 52), `{device name}` kept, no `---`.

#### Blocking items hit

- Missed Pass clauses, root line 150: Turn 1 drafted instead of asking, the scenario's first Fail example ("Turn 1 drafts"). `Custom Instructions.md` line 108 says `$doc` "still ask" before drafting, and Doc Mode knowledge line 39 makes `$d` its short alias

#### Advisory items

- Borderline, never decides alone: line 88 "Tomasz is running a two-week spike" and "He is also writing down" state work in progress, while the thread gives the plan (fixture line 58) and the block's own line 103 says "no start date"
- Borderline: line 53 "which the member has to reconcile by hand" adds a claim the thread does not make, unnamed
- Borderline: line 86 "Status: Approved direction" on Joana's plan, as on SDK-003
- Turn 1 chat heading at line 92 carries an em dash ("Things I assumed or added" then the delimiter), in commentary outside the block
- Block form: fenced both turns, no commentary before the block. Format gate passed both blocks
- Size: Turn 2 block 115 lines, inside 70 to 160

#### Realism entries

- Turn 1 block (`turn-1.md` lines 2 to 85, copy `blocks/docs/PDK-003-turn1.md`), kind Doc status write-up in the Narrative overview register, delivered at the clarification turn. Company facts: "**Status: Not decided.**" and 2026-10-09 (line 5) against thread lines 66 and 68 match, 0.8% (30) against line 18 match, `Conflicting edit from {device name}` (48) against line 26 match, offline edits retried until the app closes (78) against `loomlist-context.md` line 176 match. Placeholder: `{device name}` exempt. 84 lines
- Turn 2 block (`turn-2.md` lines 2 to 116, copy `blocks/docs/PDK-003-turn2.md`), kind Doc, Proposal. Routed template Project Doc Templates lines 461 to 550: notice under the title (5), Overview (8) and the options body (31) present. Optional: Current state (16), Options compared (65), Where the thread landed (74), Risks and dependencies (90), Open decisions (97), Out of scope (105), Source basis (111). Company facts: block-level last-writer-wins (20, thread 14) match, 58% and 42% (26 to 27, thread 48) match, about 3 weeks (44, thread 24) match, 6 to 8 weeks (54, thread 26) match, two quarters (63, thread 28) match, Joana, Engineering Manager, Sync, 2026-10-09 (5, thread 67 to 68) match. Placeholder: `{device name}` exempt. 115 lines against 70 to 160. Discipline code not applicable

#### Open readings

- Is "Tomasz is running a two-week spike" an invented status (root line 187, "naming never excuses an invented status")? It does not change this verdict
- The "still ask" sentence names `$doc` but not `$d` on both sides (`AGENTS.md` line 287, `Custom Instructions.md` line 108). Is the alias covered by that sentence? Graded yes, through the alias definitions

---

### SDK-004 (skill), Catalog conflict gate

#### Draft row

```csv
SDK-004,skill,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 stopped and saved the question-only export/001 - doc-activity-emails-reference-clarification.md listing the spec's ""08:00 in the recipient's local time"" against the inventory's ""Daily at 07:00 UTC"" without choosing (lines 3 to 7), and Turn 2 saved export/002 - doc-activity-emails-catalog.md with EM-01 at 08:00 in the recipient's local time (line 66), EM-06 at Monday 09:00 (line 84) and the six templates on their own entries. N printed 20 and 166 equals wc -l, not the Read's final lines 21 and 167 (AGENTS.md line 45), recorded only."
```

#### Pass clauses

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 stops with no catalog content | Met | `meta.json` turn 1 ledger: only the clarification file. `turn-1.md` line 1 "I haven't written the reference page yet" |
| Lists the `EM-01` conflict as `08:00` recipient's local time (spec) against `07:00 UTC` (inventory) | Met | Clarification line 5 `loomlist-notification-spec.md` "every day at 08:00 in the recipient's local time", line 6 `loomlist-email-template-inventory.md` "Daily at 07:00 UTC" |
| Asks which source governs it | Met | Line 3 "Which should the page state?" |
| Covers source set, status, shape and scope in the same question | Met | Line 15 "**Source set:**", line 9 "**Document status:**", lines 17 to 20 "**Scope & shape:**" with scope (19) and shape (20) |
| Settles nothing itself | Met | Line 7 offers three options and says "The newer edit date doesn't settle it on its own" |
| Exports the question in the doc lane with a read-back | Met | Read at event 48 lines 1 to 21 after the last modification (Bash `perl -pi` at event 46). `turn-1.md` lines 3 to 5 path, `Verified:`, `HVR self-scan:` |
| Turn 2 Catalog with an Overview | Met | Export line 7 |
| One entry per email under a category body | Met | Line 59 `## Scheduled emails` (EM-01, EM-06), line 94 `## Event emails` (EM-02 to EM-05) |
| `* * *` directly under every content heading | Met | All 15 headings below the title. Format gate passed |
| `*   ` bullets | Met | No hyphen bullet |
| Sentence-case headings | Met | Email names keep their own capitals, for example line 62 `### EM-01: Daily digest` |
| No empty spacer heading | Met | None |
| `EM-01` to `EM-06` named `Daily digest`, `Mentioned in a page`, `Comment reply`, `Page shared with you`, `Workspace invite`, `Weekly summary` | Met | Lines 62, 97, 111, 125, 137, 80 |
| `EM-01` at `08:00` in the recipient's local time | Met | Line 66 "Every day at 08:00 in the recipient's local time", index line 19 |
| `EM-06` at `Monday 09:00` in the recipient's local time | Met | Line 84 |
| Templates on their own entries | Met | `tpl_digest_v4` line 69, `tpl_mention_v2` 104, `tpl_comment_reply_v2` 118, `tpl_page_shared_v3` 132, `tpl_workspace_invite_v5` 144, `tpl_weekly_summary_v1` 87 |
| No push notification entry | Met | No entry. Line 154 lists push under Catalog boundaries as not covered, named at `turn-2.md` line 20 |
| Nothing the three attachments do not state | Met (borderline noted) | Named additions at `turn-2.md` lines 14 to 20 |

Fail list checked: `07:00 UTC` appears only as stale (lines 78 and 165), no blended time, names, IDs and templates exact, `Settings > Notifications` kept (lines 34 to 35, 143), EM-05 without a switch (lines 35, 143), no `---`.

#### Blocking items hit

None.

#### Advisory items

- Borderline, never decides alone: line 40 "those two rule out most of the cases below" is an unsourced judgment, unnamed
- `N`: 20 and 166 match `wc -l` but not the Read's final lines 21 and 167, the reverse of the other three skill scenarios
- Turn 1 `HVR self-scan: 2 hard blockers. Fixed: two Oxford commas.` (`turn-1.md` line 5), a count taken and reported
- Five-line Doc summary present (`turn-2.md` lines 8 to 12)
- Size: 166 lines, inside 80 to 180

#### Read-back table

| Turn | Export path | `N` printed | Read after the last Write or Edit, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - doc-activity-emails-reference-clarification.md` | 20 | Write at event 38, Read at event 40 lines 1 to 21, Bash `perl -pi` at event 46, Read at event 48 lines 1 to 21 (21 empty) | 20 |
| 2 | `export/002 - doc-activity-emails-catalog.md` | 166 | Write at event 49, Bash `perl -pi` at event 57, Read at event 65 (result event 69) lines 1 to 167 (167 empty) | 166 |

#### Realism entries

- `export/001 - doc-activity-emails-reference-clarification.md`, kind Doc clarification, routed pattern `assets/interactive-response-templates.md` line 129 and the conflict gate in `references/doc-mode.md` lines 184 to 188. Fields present as listed in the Pass table plus purpose and audience (11) and domain and detail (13). Company facts: Lena, edited 2026-07-14 (line 5) against `loomlist-notification-spec.md` lines 3 to 4 match, Mateo, edited 2026-09-11 (6) against `loomlist-email-template-inventory.md` lines 3 to 4 match, the 20-item digest cap and the 14-day invite token (13) against inventory lines 23 and 31 match. Placeholder none. 20 lines
- `export/002 - doc-activity-emails-catalog.md`, kind Doc, Catalog. Routed template skill `assets/doc-templates.md` section 4 (lines 259 to 324): Overview (7) and category bodies with one entry per ID (59, 94) present. Optional: Index (14), shared rules (26), Catalog boundaries (150), Sources (161). Company facts: EM-01 at 08:00 recipient's local time (66, spec 12) match, EM-06 Monday 09:00 (84, spec 17) match, switches for EM-01 to EM-04 and EM-06 on by default (35, spec 26) match, 140-character `excerpt` (105, inventory 25) match, invite token expires after 14 days (145, inventory 31) match, six locales with en-US fallback (31, inventory 19) match. Placeholder none. 166 lines against 80 to 180. Discipline code not applicable

#### Open readings

- `N` 20 and 166 equal `wc -l` while `AGENTS.md` line 45 asks for the Read's final line (21 and 167). Which is graded?

---

### PDK-004 (project), Catalog conflict gate

#### Draft row

```csv
PDK-004,project,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 rendered a fenced question listing the spec's ""every day at 08:00 in the recipient's local time"" against the inventory's ""daily at 07:00 UTC"" with neither chosen (turn-1.md line 7) under Export-equivalent path export/001 - doc-loomlist-activity-emails-clarification.md, and Turn 2 a fenced catalog with EM-01 at 08:00 in the recipient's local time (line 59), EM-06 at Monday 09:00 (line 136), the six templates and no push entry. Advisory: the format gate flags the em dash in the three Sources bullets (block lines 168 to 170), which follow the Catalog scaffold's own Sources line."
```

#### Pass clauses

| Clause | Result | Evidence |
|---|---|---|
| Turn 1 stops with no catalog content | Met | Block lines 1 to 18 hold questions only. Line 24 "I haven't started the page yet" |
| Lists the `EM-01` conflict as `08:00` recipient's local time (spec) against `07:00 UTC` (inventory) | Met | Line 7 names "Lena's spec (Product, 2026-07-14)" with "every day at 08:00 in the recipient's local time" and "Mateo's inventory (notifications-service, 2026-09-11)" with "daily at 07:00 UTC" |
| Asks which source governs it | Met | Line 7 "Which one should the page state?" |
| Covers source set, status, shape and scope in the same question | Met | Line 4 "**Source set:**", line 9 "**Document status:**", line 15 "**Scope & shape:**" |
| Settles nothing itself | Met | Line 7 "Neither page says it overrides the other, and the newer date does not settle it", then options only |
| Rendered as its own block with a doc-lane clarification label | Met | Fenced lines 1 to 18, line 20 `Export-equivalent path: export/001 - doc-loomlist-activity-emails-clarification.md`, line 22 `HVR self-scan:` |
| Turn 2 Catalog with an Overview | Met | `turn-2.md` line 8 |
| One entry per email under a category body | Met | Line 50 `## Activity emails`, entries at lines 53, 71, 87, 103, 117, 130 |
| `* * *` directly under every content heading | Met | Every heading from line 8 to line 167 |
| `*   ` bullets | Met | No hyphen bullet in the block |
| Sentence-case headings | Met | Email names keep their capitals, for example line 53 `### EM-01 Daily digest` |
| Names `Daily digest` to `Weekly summary` on `EM-01` to `EM-06` | Met | Lines 53, 71, 87, 103, 117, 130 |
| `EM-01` at `08:00` in the recipient's local time | Met | Line 59, index line 30 |
| `EM-06` at `Monday 09:00` in the recipient's local time | Met | Line 136 |
| Templates on their own entries | Met | Lines 61, 79, 95, 111, 125, 138 |
| No push notification entry | Met | Line 12 "Push notifications are out of scope too", line 164 under Catalog boundaries |
| Nothing the three attachments do not state | Met (borderline noted) | Named additions at lines 187 to 191. The guest definition (line 20) and the mention wording (line 73 "typed @ and their name") trace to `loomlist-context.md` lines 29 and 62 |
| No file claim | Met | No `Path:`, `Saved:` or `Verified:`. Line 181 "because this is a file export" claims no save (borderline wording) |

Fail list checked: `07:00 UTC` appears only as out of date (lines 160 and 170), no blended time, names, IDs and templates exact, no `---`.

#### Blocking items hit

None.

#### Advisory items

- Format gate on the Turn 2 block copy: lines 168 to 170 (reply lines 169 to 171), `prose em dash`, on the three plain Sources bullets. The Project Catalog scaffold writes its Sources line as a link followed by the same delimiter (Project Doc Templates line 302). Not a Pass clause
- Borderline, never decides alone: line 151 "The version bump matters most, because a job built for the old variables then fails loudly instead of sending a broken email" adds a ranking and an outcome the inventory (line 43) does not give, unnamed
- Block form: fenced both turns, no commentary before the block. Turn 1 block passed the format gate
- Five-line Doc summary present (lines 179 to 183, "Layout" for ClickUp layout)
- Size: Turn 2 block 170 lines, inside 80 to 180

#### Realism entries

- Turn 1 block (`turn-1.md` lines 2 to 17, copy `blocks/docs/PDK-004-turn1.md`), kind Doc clarification, routed pattern Project Interactive Response Templates line 106 and the conflict gate at Doc Mode knowledge lines 160 to 164. Company facts: 08:00 recipient's local time against `loomlist-notification-spec.md` line 12 match, 07:00 UTC hand-off by `digest-sender` against `loomlist-email-template-inventory.md` line 23 match, the 20-item cap and 14-day invite token (line 13) against inventory lines 23 and 31 match. Placeholder none. 16 lines
- Turn 2 block (`turn-2.md` lines 2 to 171, copy `blocks/docs/PDK-004-turn2.md`), kind Doc, Catalog. Routed template Project Doc Templates lines 238 to 303: Overview (8) and the category body with one entry per ID (50) present. Optional: Shared vocabulary (15), Index (25), shared rules (38), Catalog boundaries (158), Sources (167). Company facts: EM-01 at 08:00 (59, spec 12) match, EM-06 Monday 09:00 (136, spec 17) match, `tpl_digest_v4` (61, inventory 12) match, 140-character `excerpt` (80, inventory 25) match, invite token 14 days (126, inventory 31) match, guests not billed (20, context 29) match. Placeholder none. 170 lines against 80 to 180. Discipline code not applicable

#### Open readings

- Should the format gate's em dash finding on a Sources bullet count against a Catalog that follows its own template's Sources line (Project Doc Templates line 302, skill `doc-templates.md` line 323), given that Doc Mode allows the delimiter only in bold-term definitions and status labels (Project Doc Mode line 80, skill `doc-mode.md` line 104)?
- Is "because this is a file export" a file claim? Graded no

---

### Twin notes

**SDK-001 and PDK-001: agree (FAIL, FAIL).** Both runtimes drafted at Turn 1 on the no-command request and named their assumed audience instead of asking (`skill/.../turn-1.md` line 14, `claude project/.../turn-1.md` line 155). The two packagings carry the same text: skill `AGENTS.md` lines 284 to 285 and `references/doc-mode.md` lines 67, 198, 204 and 260, Project `Custom Instructions.md` lines 108 and 130 and Doc Mode knowledge lines 43, 174, 180 and 236. The shared escape ("Once the notes are present and make the reader's use clear, the routing above picks the shape without a preference question", skill line 260, Project line 236) is where both runtimes and the scenario part ways, so this reads as a rule gap between the scenario and both packagings rather than a runtime fault. The twins differ at Turn 2: the skill renamed the primary body to `## Stacking rules` and reworded `one discount code per order`, the Project kept both. Both templates make `## Behavior rules` mandatory (skill `assets/doc-templates.md` lines 115 and 400, Project Doc Templates lines 94 and 379), so that part is a runtime fault on the skill side.

**SDK-002 and PDK-002: agree (PASS, PASS).** Both asked first, both kept the six steps, the pause and resume conditions and the proposed dual-secret window. Both carry unnamed generalizations of INC-0412 into general guidance (skill lines 64 and 74, Project lines 36 and 89), graded borderline on both. The rule both sides share: skill `assets/doc-templates.md` line 237 and Project Doc Templates line 216 ("mark the step unverified rather than inventing a result"), skill `SKILL.md` line 283 and `Custom Instructions.md` line 104 on unnamed additions. The Project leaned harder on labelled "Expected result" lines, so if the operator reads those as invented step outcomes, the pair would differ as a runtime fault on the Project side.

**SDK-003 and PDK-003: differ (PASS, FAIL).** The skill asked a six-field question under `$d`, the Project drafted a status page. Same rule on both sides: `AGENTS.md` line 287 and `Custom Instructions.md` line 108 both say `$doc` "still ask" (neither names `$d`, and both define it as the alias: `AGENTS.md` line 193, Project Doc Mode line 39), and "Clarification is mandatory when ... Purpose or audience materially changes what belongs in the document" sits at skill `doc-mode.md` line 204 and Project Doc Mode line 180. Cause: runtime fault on the Project side. The two Turn 2 proposals then agree closely, and both label Joana's interim plan "Approved direction" (skill export line 106, Project `turn-2.md` line 86).

**SDK-004 and PDK-004: agree (PASS, PASS).** Both stopped at Turn 1, listed both values with both sources, refused the newer date as authority and asked about the other fields, then applied the user's designation within its scope. Rule lines: skill `references/doc-mode.md` lines 184 to 188, Project Doc Mode knowledge lines 160 to 164. Minor differences are advisory only: the Project's Sources bullets trip the format gate, and the skill printed `N` as `wc -l`.

---

## 9. Stories batch, grader draft

Batch: `SST-001..SST-004` (skill) and `PST-001..PST-004` (Project), run `2026-09-25--manual-testing-playbook--claude-opus-5-5-medium`, Product Owner commit `3023c5e`.

`<RUN>` below is `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/`. Scenario files are `AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/{skill,project}-story-modes/<slug>.md`, and every Pass/fail bullet sits on line 35 of its file. `git -C "AI Systems/Product Owner" status --porcelain -- sk-product-owner "claude project" AGENTS.md benchmark/fixtures` printed nothing, so sources were read from the working tree.

Format gate: `node validate-output-format.cjs --system product-owner <file>` from the Sync Loop folder, no `--write`. Every skill export and every Project block copy printed `Product Owner output format validation passed across 1 artifact file(s)` with exit code 0. Project block copies are in `scratch/grades/blocks/stories/`, named `<ID>-turn<n>-block<k>.md`.

Read-back note for every skill row: each export ends in a newline, so `wc -l` is one lower than the `totalLines` the Read tool reports. The rule (`SKILL.md` line 211, `AGENTS.md` line 46) takes `N` from the final line number Read returns, so the Read figure is the one `N` is checked against.

Shared finding behind six of the eight verdicts: in `SST-002..SST-004` and `PST-002..PST-004`, Turn 1 drafted the artifact without the one Story question the Pass clause requires. `AGENTS.md` line 287 and `Custom Instructions.md` line 108 both say `$story` still asks and waits. Twin notes and Open readings cover why both runtimes skipped it.

---

### SST-001 (skill) Story hard values

**Draft row**

```csv
SST-001,skill,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 saved only the Story-lane question (turn-1.md line 3, read back by Read #12) and Turn 2 saved 002 - Story-free-cancellation-filter.md with all eight hard values in Requirements (export lines 48, 51, 56, 61, 67) and both Guest Support asks as constraints (lines 43, 50). Advisory: 143 file lines against the 70 to 130 band."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| T1 asks one consolidated Story question that asks for the Guest Support asks | Met | `turn-1.md` lines 7 to 14, item 1 line 9 `please paste both exactly as Guest Support sent them`. Clarification export line 5 |
| T1 saves only that question in the Story lane | Met | `export/001 - Story-free-cancellation-filter-clarification.md`, 13 lines of question only. `meta.json` turn 1 ledger creates only that file |
| T1 reads it back | Met | `events-turn-1.jsonl` Write #9, Edit #11, then Read #12 of that path returned lines 1 to 14 of 14 |
| T1 replies with path, `Verified:` line and `HVR self-scan:` line | Met | `turn-1.md` lines 3, 4 (`Verified: read-back succeeded; 14 lines`), 5 |
| T1 writes no draft | Met | `turn-1.md` line 1 `I haven't written the Story yet`. No other file in the turn 1 ledger |
| T2 saves one Story on the next number | Met | `export/002 - Story-free-cancellation-filter.md`, turn 2 ledger creates only it. Clarification untouched (no Write or Edit to it in `events-turn-2.jsonl`) |
| T2 reads it back | Met | Last Edit #12, then Read #13 (offset 100) returned lines 100 to 144 of 144 |
| T2 names the Story kind | Met | `turn-2.md` line 1 `as a **Story**` |
| T2 carries the `HVR self-scan:` line | Met | `turn-2.md` line 5 |
| About, Problem, Solution, Expected outcomes, Requirements, numbered Given/When/Then criteria each closed by Mark-as-done | Met | Export lines 7, 13, 17, 21, 27, 80. Criteria 1 to 7 at lines 84 to 141, Mark-as-done lines 91, 100, 108, 117, 125, 133, 141 |
| `Free cancellation until 14 Oct`, `d MMM`, `No stays with free cancellation for these dates`, `Clear filter`, `filter_applied`, `filter_name`, `free_cancellation`, `8.13.0` verbatim in Requirements | Met | Export lines 48, 51, 56 (string and `Clear filter`), 61 (the three tracking values), 67 |
| `312 stays` and `14 days` verbatim or named as left out | Met | Line 38 ``` `312` stays ``` (backticks around the number only, see Open readings), line 49 `14 days before check-in` |
| Both Guest Support asks as constraints | Met | Line 50 `The deadline is the property's local date`, line 43 `The filter stays on when the guest opens a property and goes back to the results` |

**Blocking items hit:** None.

**Advisory items**

- Size band: 143 file lines (Read 144) against 70 to 130.
- Named additions, all covered by `turn-2.md` lines 13 to 16: criterion 6, criterion 7 (`events-collector`), the two expected outcomes.
- Borderline, not decisive: line 38 calls the Lisbon search `Reference search at the kickoff`. The notes say `Our test search` and were written after the kickoff (notes lines 4 and 20), so "at the kickoff" is a light inference.

**Read-back table**

| Turn | Export path | `N` printed | Read after last write, lines returned | `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - Story-free-cancellation-filter-clarification.md` | 14 | Read #12, lines 1 to 14 of 14 (after Edit #11) | 13 |
| 2 | `export/002 - Story-free-cancellation-filter.md` | 144 | Read #13, lines 100 to 144 of 144 (after Edit #12) | 143 |

**Realism entries**

- `export/001 - Story-free-cancellation-filter-clarification.md`, Story-lane clarification. No template sections apply, question only, no draft. Facts: names Tomas's notes of 2026-09-18 (notes line 4), the four exclusions (notes lines 47 to 50). No placeholder. 13 lines. Gate passed.
- `export/002 - Story-free-cancellation-filter.md`, Story. Required sections (skill `assets/story-template.md` lines 40 to 103): preamble, About, Problem, Solution, Expected outcomes, Requirements, Acceptance criteria all present. References omitted with no links supplied (template note, allowed). No `**Open:**` line, no Delivery, correct. Company facts: H1 `Guest - Search - Free cancellation filter` follows `roamstay-context.md` line 85. `filter_applied` with `filter_name` matches line 179. Filter sheet holds Price and Star rating today, line 138. `search-service` owned by Search, line 56. `events-collector`, line 184. No placeholder. 143 lines against 70 to 130 (advisory). Gate passed.

**Open readings**

- Does ``` `312` stays ``` (number backticked, word outside) satisfy "keeps `312 stays` verbatim"? Graded Met because the rendered text reads `312 stays`.
- The Turn 2 read-back was a partial Read (lines 100 to 144). The rule asks for a Read of the exact path that returns non-empty content, which it did. Should a partial Read count as the read-back?

---

### PST-001 (Project) Story hard values

**Draft row**

```csv
PST-001,project,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 rendered one fenced Story-lane question block asking for the Guest Support asks with its clarification label (turn-1.md lines 1 to 17) and no draft, and Turn 2 rendered the Story block with every hard value in Requirements (turn-2.md lines 44, 47, 52, 58, 63) and both asks (lines 39, 46), claiming no file. Advisory: block body 131 lines, one over the 70 to 130 band."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| T1 asks one consolidated Story question that asks for the Guest Support asks | Met | Block `turn-1.md` lines 2 to 14, line 6 `Paste both asks as Guest Support wrote them` |
| T1 renders it as its own block | Met | Fenced ` ```markdown ` block, lines 1 to 15, at the very start of the reply |
| T1 `Export-equivalent path:` in the Story lane | Met | Line 17 `export/NNN - Story-free-cancellation-filter-clarification.md` |
| T1 `HVR self-scan:` line | Met | Line 19 |
| T1 renders no draft | Met | Line 21 `I've held off drafting until the two Guest Support asks arrive` |
| T2 renders one Story block with its `Export-equivalent path:` | Met | Fenced block lines 1 to 133, line 135 `export/NNN - Story-free-cancellation-filter.md` |
| T2 names the Story kind | Met | Line 139 `I wrote this as a **Story**` |
| T2 `HVR self-scan:` line | Met | Line 137 |
| T2 claims no file | Met | No saved, written, read-back or file wording outside the block in either turn |
| About, Problem, Solution, Expected outcomes, Requirements, numbered Given/When/Then criteria each closed by Mark-as-done | Met | Block lines 8, 12, 16, 20, 28, 76. Criteria 1 to 6 at lines 80 to 130, Mark-as-done lines 87, 96, 104, 113, 122, 130 |
| Eight hard values verbatim in Requirements | Met | Lines 44 (`Free cancellation until 14 Oct`), 47 (`d MMM`), 52 (empty-state string and `Clear filter`), 58 (`filter_applied`, `filter_name`, `free_cancellation`), 63 (`8.13.0`) |
| `312 stays` and `14 days` | Met | Line 37 ``` `312` stays ```, line 45 `` `14 days` `` |
| Both Guest Support asks as constraints | Met | Line 46 `The deadline is the date at the property's location, not the date on the guest's device`, line 39 `The filter stays on when the guest opens a property and goes back to the results` |

**Blocking items hit:** None.

**Advisory items**

- Size band: block body 131 lines against 70 to 130.
- Block form: fenced in both turns. No commentary before either block.
- Named additions, covered by `turn-2.md` lines 150 to 153: expected outcomes 2 and 3, the `And` line of criterion 2, criterion 3.
- Borderline, not decisive: criterion 2 (line 93) says `written in the guest's language` where the notes say locale. Requirements line 47 keeps the notes' `d MMM` in the guest's locale, and the reply asks about it (line 142).
- Line 46 adds `not the date on the guest's device`, which is the direct negation of the supplied ask and so not an addition (brief section 2).

**Realism entries**

- Block `PST-001-turn1-block1.md`, Story-lane clarification, fenced. Question only. Facts: the notes' exclusions (notes lines 47 to 50), the filter persistence rule (notes line 21), Ines's frames (notes line 52). No placeholder. 13 lines. Gate passed.
- Block `PST-001-turn2-block1.md`, Story. Required sections (Project `Product Owner - Assets - Story Template - v0.100.md`, scaffold identical to the skill asset): preamble, About, Problem, Solution, Expected outcomes, Requirements, Acceptance criteria present, References omitted with no links, no Delivery. Company facts: H1 matches `roamstay-context.md` line 85, `filter_applied`/`filter_name` line 179, Price and Star rating line 138, `search-service` line 56. No placeholder. 131 lines against 70 to 130 (advisory). Gate passed.

**Open readings**

- Same `312 stays` reading as `SST-001`.

---

### SST-002 (skill) Story forced delivery

**Draft row**

```csv
SST-002,skill,claude-opus-5-5-medium,FAIL,2,2,pending,no,"Turn 1 drafted and saved export/001 - Story-view-only-share-links.md with no Story question (turn-1.md lines 1 and 7: ""I didn't ask a question first""), so no clarification exists and Turn 2 edited 001 in place instead of saving on the next number. The **Open:** line also rewords `Do sub-pages inherit the link?` (export line 36). Advisory: 179 lines against 90 to 170, and N 176 printed against Read's 177."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| T1 asks one consolidated Story question | Unmet | `turn-1.md` line 7 `I didn't ask a question first because the notes already give the role, the value and every requirement` |
| T1 saves only that question in the Story lane | Unmet | Turn 1 ledger creates `export/001 - Story-view-only-share-links.md`, a full Story. No `-clarification` file exists |
| T1 reads it back | Unmet | No clarification to read. Read #12 read back the Story |
| T1 replies with path, `Verified:` and `HVR self-scan:` for the question | Unmet | The lines at 3 to 5 belong to the Story, not a question |
| T1 no draft | Unmet | `turn-1.md` line 1 `I've written the Story from Kofi's notes and saved it` |
| T2 saves one Story on the next number | Unmet | Turn 2 ledger modifies `export/001 - Story-view-only-share-links.md` only (Edits #2 to #5). No new number |
| T2 reads it back | Met | Read #6, lines 1 to 180 of 180, after the last Edit #5 |
| T2 names the Story kind | Met | `turn-2.md` line 1 `It's still a Story` |
| T2 `HVR self-scan:` line | Met | `turn-2.md` line 5 |
| About, Problem, Solution, Expected outcomes, Requirements, criteria with Mark-as-done, closing `## Delivery` with Estimation, Rabbit holes, No-gos in order | Met | Export lines 7, 13, 19, 23, 32, 79. Criteria 1 to 8 at lines 85 to 156, each closed by Mark-as-done. Delivery line 160, Estimation 162, Rabbit holes 168, No-gos 174 |
| Requirements carry `Anyone with the link can view`, `Never`, `7 days`, `30 days`, `60 seconds`, `3 active links`, `Free`, `Plus`, `Team`, `noindex`, `Duplicate` | Met | Lines 44, 47 and 48, 50 and 51, 59 (``` `3` active links ```) and 63 (`3 active links` inside the limit string), 59 to 62, 74, 72 |
| `**Open:**` line carries `Do sub-pages inherit the link?` and names Lena | Unmet (string) / Met (Lena) | Line 36 `**Open:** whether a link on a page also opens its sub-pages is not decided` rewords the backticked question from `loomlist-view-only-links-design-notes.md` line 46. Lena named on line 36 |
| Rabbit holes repeat that question | Met in substance | Line 172 `Sub-page inheritance is not decided`, reworded |
| No acceptance criterion asserts how sub-pages behave | Met | Criteria at lines 85 to 156 never mention sub-pages |

**Blocking items hit**

- Pass clauses missed in Turn 1 and Turn 2 (drafted in Turn 1, no Story-lane clarification, no next number): root line 150, with `AGENTS.md` line 287.
- Side-effect ledger: a clarification turn may create only the `-clarification` export (root line 106). Turn 1 created the Story.
- Protected fact: `Do sub-pages inherit the link?` is a hard value the Pass clause lists verbatim and it was reworded (brief section 2, root line 188).

**Advisory items**

- Size band: 179 file lines (Read 180) against 90 to 170.
- Wrong `N` in Turn 1: printed 176 (`turn-1.md` line 4), Read #12 returned final line 177. Recorded only.
- Named additions, covered by `turn-1.md` lines 13 to 17.
- Borderline, not decisive: line 38 `until the open question is settled it opens that page only` and Rabbit holes line 172 `Build against a single page until then`. Fixture line 54 says the frames show a single page until then, so this may be source-backed, or it may be the Fail example "settles the sub-page question either way".

**Read-back table**

| Turn | Export path | `N` printed | Read after last write, lines returned | `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - Story-view-only-share-links.md` | 176 | Read #12 (offset 160), lines 160 to 177 of 177, after Write #10 | Not on disk in this state (edited in Turn 2) |
| 2 | `export/001 - Story-view-only-share-links.md` | 180 | Read #6, lines 1 to 180 of 180, after Edit #5 | 179 |

**Realism entries**

- `export/001 - Story-view-only-share-links.md`, Story. Required sections present: preamble, About, Problem, Solution, Expected outcomes, Requirements, Acceptance criteria, and Delivery, which the `**Open:**` line forces (`story-template.md` section 3, `story-mode.md` line 74). Company facts: H1 `Member - Sharing - View-only links` follows `loomlist-context.md` line 112. Problem `Pages are shared by invite only` matches line 179. Lena as PM of Sharing and Notifications, line 88. Plan names Free, Plus, Team, lines 35 to 37. No placeholder beyond the exempt `TBD...` Delivery slots. 179 lines against 90 to 170 (advisory). Gate passed.

**Open readings**

- Does rewording `Do sub-pages inherit the link?` in the `**Open:**` line miss the clause, when the backticked question is otherwise carried in substance? Graded Unmet.
- Is "build against a single page until then" (lines 38, 172) settling the sub-page question, given fixture line 54?
- Wrong `N` (176 against Read's 177), listed per the brief.

---

### PST-002 (Project) Story forced delivery

**Draft row**

```csv
PST-002,project,claude-opus-5-5-medium,FAIL,2,2,pending,no,"Turn 1 rendered the full Story with no Story question, saying Kofi's notes ""gave enough to draft it without asking you anything first"" (turn-1.md line 187), so every Turn 1 clause is missed. The **Open:** line also rewords `Do sub-pages inherit the link?` (turn-2.md line 34). Advisory: block body 180 lines against 90 to 170."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| T1 asks one consolidated Story question | Unmet | `turn-1.md` line 187 `Kofi's notes gave enough to draft it without asking you anything first` |
| T1 renders it as its own block with its Story-lane `Export-equivalent path:` and HVR line | Unmet | The block at lines 1 to 181 is a full Story. Line 183 labels `export/NNN - Story-member-sharing-view-only-links.md`, not a `-clarification` name |
| T1 renders no draft | Unmet | Lines 1 to 181 |
| T2 renders one Story block with its `Export-equivalent path:` | Met | Fenced block lines 1 to 182, path line 184 |
| T2 names the Story kind | Met | Line 188 `I've updated the **Story**` |
| T2 `HVR self-scan:` line | Met | Line 186 |
| T2 claims no file | Met with a borderline line | Line 188 `It replaces the previous version under the same filename`. No save, write or read-back claim. See Open readings |
| Sections through a closing `## Delivery` with Estimation, Rabbit holes, No-gos in order | Met | Block lines 8, 12, 16, 20, 30, 71. Criteria 1 to 9 at lines 77 to 158, each closed by Mark-as-done. Delivery 162, Estimation 164, Rabbit holes 170, No-gos 176 |
| Eleven values verbatim in Requirements | Met | Lines 36, 39, 41 and 42, 49 and 54, 49 to 51, 66, 64 and 65 |
| `**Open:**` line carries `Do sub-pages inherit the link?` and names Lena | Unmet (string) / Met (Lena) | Line 34 `It is not decided whether a link on a page also opens its sub-pages`. Lena named on line 34 |
| Rabbit holes repeat that question | Met in substance | Line 174 `Sub-page inheritance is still open` |
| No criterion asserts sub-page behavior | Met | Criteria at lines 77 to 158 never mention sub-pages |

**Blocking items hit**

- Turn 1 Pass clauses missed (drafted before asking): root line 150, with `Custom Instructions.md` line 108.
- Protected fact: `Do sub-pages inherit the link?` reworded (brief section 2, root line 188).

**Advisory items**

- Size band: block body 180 lines against 90 to 170.
- Block form: fenced in both turns, no commentary before a block.
- Named additions, covered by `turn-1.md` lines 191 to 195: criteria 2 and 3, the Duplicate reading.

**Realism entries**

- Block `PST-002-turn1-block1.md`, Story (superseded in Turn 2). Same sections as below. 179 lines. Gate passed.
- Block `PST-002-turn2-block1.md`, Story. Required sections present, Delivery forced by the `**Open:**` line. Company facts: H1 follows `loomlist-context.md` line 112, Problem matches line 179 and line 167, Lena line 88, plans lines 35 to 37. Agencies on Plus from Turn 2. No placeholder beyond exempt `TBD...`. 180 lines against 90 to 170 (advisory). Gate passed.

**Open readings**

- Same rewording question as `SST-002`.
- Does `It replaces the previous version under the same filename` (line 188) count as a file claim under root line 189? Graded not a claim, since it says nothing was saved, written or read back.

---

### SST-003 (skill) Story refinement

**Draft row**

```csv
SST-003,skill,claude-opus-5-5-medium,FAIL,2,2,pending,no,"Turn 1 skipped the Story question and saved the refinement at once (turn-1.md line 1, events-turn-1 Write #12), so no Story-lane clarification exists. Turn 2 otherwise met the refinement name, shape and values under export/fernhouse-save-card-draft.md with the source untouched. facts_intact is no because the draft's stored brand became an **Open:** line (export line 42, see Open readings). Advisory: 151 lines against 70 to 130."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| T1 asks one consolidated Story question | Unmet | `turn-1.md` line 1 `I've rebuilt Priya's draft as a house-format **Story**` |
| T1 saves only that question in the Story lane | Unmet | Turn 1 ledger creates `export/fernhouse-save-card-draft.md`. No `-clarification` file |
| T1 reads it back, replies with path, `Verified:`, HVR for the question | Unmet | Lines 3 to 5 report the refinement, not a question |
| T1 no draft | Unmet | `events-turn-1.jsonl` Write #12 of the refinement |
| T2 saves the refinement as `export/fernhouse-save-card-draft.md` | Met | Turn 2 ledger modifies that path, no number, no artifact word |
| T2 reads it back | Met | Last Edit #7, then Read #8 (offset 140), lines 140 to 152 of 152 |
| T2 names the Story kind | Met | `turn-2.md` line 1 `the **Story**` |
| T2 `HVR self-scan:` line | Met | `turn-2.md` line 5 |
| Leaves `context/fernhouse-save-card-draft.md` unchanged | Met | No Write, Edit or write-capable Bash touches `context/` in either stream (the only context commands are `cat`). Ledgers list no context change. Staged sha256 `c39e2440...` equals the fixture's |
| H1 with no `PRD -` prefix | Met | Export line 1 `# Customer - Checkout - Save card for next time` |
| No `**Checklist**` and no `- [ ]` build item in Requirements | Met | Requirements lines 26 to 67 hold none. The only `- [ ]` lines are Mark-as-done |
| Checklist content carried as bold-lead constraint groups | Met | Line 37 sixth card refused, line 44 stored fields, line 60 `Remove this card?`, line 64 the three events, line 30 platforms |
| `## Acceptance criteria` of numbered Given/When/Then each closed by Mark-as-done | Met | Line 69, criteria 1 to 6 at lines 75 to 128 |
| Every supplied value verbatim | Met | `Save this card for next time` 31, `unchecked by default` 32, `You can save up to 5 cards` 36, `Card ending 7031` and `Expires 08/28` 49, `CVC` and `€150` 51, `£130` 52, `Account > Payment methods` 58, `Remove this card?` 60, `guest checkout` 34 (as `Guest checkout`), Turn 2 copy 54, order-total rule 51 and 52 |

**Blocking items hit**

- Turn 1 Pass clauses missed: root line 150, with `AGENTS.md` line 287 (`$s` is the `$story` alias, `story-mode.md` line 59).
- Side-effect ledger: Turn 1 created the refinement where only a `-clarification` export is allowed (root line 106).

**Advisory items**

- Size band: 151 file lines (Read 152) against 70 to 130.
- Named additions, covered by `turn-1.md` lines 21 to 26 and `turn-2.md` line 14: all criteria, the `7031`/`08/28` format line, the NL, BE, DE and FR scope of `€150`, the tracking-plan rule, the named deciders, criterion 4.
- `turn-1.md` line 28 offers to push the Story "as a task". The kind named on line 1 is Story, so this reads as the ClickUp object and is not graded as a wrong artifact word.

**Read-back table**

| Turn | Export path | `N` printed | Read after last write, lines returned | `wc -l` |
|---|---|---|---|---|
| 1 | `export/fernhouse-save-card-draft.md` | 146 | Read #14 (offset 140), lines 140 to 146 of 146, after Write #12 | Not on disk in this state (edited in Turn 2) |
| 2 | `export/fernhouse-save-card-draft.md` | 152 | Read #8 (offset 140), lines 140 to 152 of 152, after Edit #7 (a `sed -i` Bash #5 also wrote it earlier) | 151 |

**Realism entries**

- `export/fernhouse-save-card-draft.md`, Story refinement. Required sections present: preamble, About, Problem, Solution, Expected outcomes, Requirements, Acceptance criteria, and Delivery forced by the brand `**Open:**` line. Figures 17%, 9%, 68% unaltered (line 13). Company facts: H1 follows `fernhouse-context.md` line 95. Card-data rule, line 153, raised as a conflict at line 42. Tracking-plan rule, line 164, at line 65. Web, iOS, Android from the draft, line 11. No placeholder beyond exempt `TBD...`. 151 lines against 70 to 130 (advisory). Gate passed.

**Open readings**

- The draft stores `token, brand, last four and expiry only` (draft line 48) and `fernhouse-context.md` line 153 allows only token, last four and expiry. The runtime kept the context rule in the requirement (line 44) and marked brand `**Open:**` (line 42). Is that correct handling of a conflict between two attachments, or a supplied draft value altered? The scenario's Expected signals expect brand stored. Not decisive here.
- Does `Guest checkout` at the start of a sentence (line 34) satisfy the verbatim `guest checkout`? Graded Met.

---

### PST-003 (Project) Story refinement

**Draft row**

```csv
PST-003,project,claude-opus-5-5-medium,FAIL,2,2,pending,no,"Turn 1 rendered the refined Story with no Story question (turn-1.md lines 1 to 162, line 168 ""I rebuilt Priya's draft""), so every Turn 1 clause is missed. Turn 2 carried every listed value and the order-total rule under Export-equivalent path export/fernhouse-save-card-draft.md (turn-2.md line 171). facts_intact is no for the same brand-storage handling as SST-003. Advisory: block body 167 lines against 70 to 130."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| T1 asks one consolidated Story question | Unmet | `turn-1.md` line 168 `I rebuilt Priya's draft in the house format` |
| T1 renders it as its own block with a Story-lane `Export-equivalent path:` and HVR line | Unmet | Line 164 labels `export/fernhouse-save-card-draft.md`, the refinement, not a `-clarification` name |
| T1 renders no draft | Unmet | Block lines 1 to 162 is the full refinement |
| T2 renders one refined Story block with `Export-equivalent path: export/fernhouse-save-card-draft.md` | Met | Fenced (four backticks) block lines 1 to 169, path line 171 |
| T2 names the Story kind | Met | Line 175 `**Artifact kind:** Story` |
| T2 `HVR self-scan:` line | Met | Line 173 |
| T2 claims no file | Met | No save, write or read-back wording |
| H1 with no `PRD -` prefix | Met | Block line 2 |
| No `**Checklist**` and no `- [ ]` build item in Requirements | Met | Requirements lines 28 to 64 hold none |
| Checklist content as bold-lead constraint groups | Met | Lines 37, 57, 51, 61 and 62, 34 |
| `## Acceptance criteria` of numbered Given/When/Then each closed by Mark-as-done | Met | Line 66, criteria 1 to 8 at lines 72 to 145 |
| Every supplied value verbatim | Met | Lines 32, 33, 36, 43 (`Card ending 7031`, `Expires 08/28`), 44 (`CVC`, `€150`, `£130`, order-total rule), 50, 51, 35 (`Guest checkout`), 46 (Turn 2 copy) |

**Blocking items hit**

- Turn 1 Pass clauses missed: root line 150, with `Custom Instructions.md` line 108.

**Advisory items**

- Size band: block body 167 lines against 70 to 130.
- Block form: fenced with four backticks in both turns, no commentary before a block.
- Named additions, covered by `turn-1.md` lines 187 to 191 and `turn-2.md` line 182.

**Realism entries**

- Block `PST-003-turn1-block1.md`, Story refinement (superseded). Two `**Open:**` lines, Delivery forced. 160 lines. Gate passed.
- Block `PST-003-turn2-block1.md`, Story refinement. Required sections present, Delivery forced by the brand `**Open:**` line (line 55). Figures 17%, 9%, 68% unaltered (line 14). Company facts: H1 follows `fernhouse-context.md` line 95, card-data rule line 153 at line 55, tracking-plan rule line 164 at line 62, draft surfaces line 11. No placeholder beyond exempt `TBD...`. 167 lines against 70 to 130 (advisory). Gate passed.

**Open readings**

- Same brand-storage reading and `Guest checkout` reading as `SST-003`.

---

### SST-004 (skill) Story with nested tasks

**Draft row**

```csv
SST-004,skill,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 asked nothing and saved a seven-file bundle with six tasks, including 001.2 - task-packed-status.md and 001.6 - task-tracking-timeline-events.md (turn-1.md lines 1 to 22), so no Story-lane clarification exists. Turn 2 repaired the folder in place to the named four with correct Tasks and Story blocks. Advisory: Story 195 lines against 80 to 150."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| T1 asks one consolidated Story question in the Story lane | Unmet | `turn-1.md` line 1 `Hamid's brief already names the task split ... so I wrote it without asking you anything first` |
| T1 saves only the question as `export/[###] - Story-[description]-clarification.md` at the top of `export/` | Unmet | Turn 1 ledger creates seven files in `export/001 - Story-order-tracking/`. No clarification |
| T1 reads it back, replies with path, `Verified:`, HVR | Unmet | Lines 3 to 24 report the bundle |
| T1 no draft and no folder | Unmet | Writes #15 to #21 in `events-turn-1.jsonl` |
| T2 saves one folder on the next number | Unmet | The folder `001 - Story-order-tracking/` was created in Turn 1. With no clarification there is no next number |
| Folder holds the Story and exactly four tasks `.1` to `.4` for FE iOS, FE Android, FE web, BE webhook in order | Met (final state) | `001.1 - task-ios-tracking-timeline.md`, `001.2 - task-android-tracking-timeline.md`, `001.3 - task-web-tracking-timeline.md`, `001.4 - task-tracking-webhook.md` |
| T2 reads every file back | Met | Reads #19 to #23, each after that file's last write (see table) |
| T2 replies with every path, Story first, each with its own `Verified:` line | Met | `turn-2.md` lines 3 to 16 |
| One `HVR self-scan:` line for the bundle | Met | `turn-2.md` line 18 |
| Names the Story kind | Met | `turn-2.md` line 26 `the Story has no Open lines left`, every path carries `Story-` |
| Leaves the clarification untouched outside the folder | Unmet | No clarification was ever saved |
| Story holds About, Problem, Solution, Expected outcomes, `#### **Tasks**` inside About with one bullet per task in order linking `(<[###].[n] - task-...md>)`, Requirements, numbered criteria with Mark-as-done | Met | Story lines 7, 11, 17, 21, 26 to 31 (four bullets in n order), 34, 104. Criteria 1 to 7 at lines 108 to 165 |
| Each task holds `### About`, a `**Story**` block linking `(<001 - Story-order-tracking.md>)`, no `**Parent task**`, `### Requirements` | Met | FE tasks lines 3, 9 to 13, 23. Webhook lines 3, 11 to 15, 25. `grep` finds no `Parent task` in the folder |
| Bundle carries the six statuses, five codes and every listed value verbatim | Met | Story line 38 (statuses), 41 to 44 (codes), 53 (`Arriving Thursday 1 October`, `Between 10:00 and 14:00`), 65 (`90 days`), 69 (`30 kg`, `120 cm`), 84, 85, 87, 90, 48, 54, 89 (`5 attempts`, `1 min, 5 min, 15 min, 1 h, 6 h`). Webhook task lines 7, 37 to 40 |

**Blocking items hit**

- Turn 1 Pass clauses missed: root line 150, with `AGENTS.md` line 287 and `story-mode.md` line 406 (no split in the request means the question asks for it).
- Fail example hit in Turn 1: `adds a Packed or DATA task` (scenario line 35). Turn 1 wrote `001.2 - task-packed-status.md` and `001.6 - task-tracking-timeline-events.md` (turn 1 ledger), deleted in Turn 2.
- Side-effect ledger: Turn 1 created a folder where only a `-clarification` export is allowed (root line 106).

**Advisory items**

- Size band: Story 195 file lines (Read 196) against 80 to 150. Tasks 72, 72, 72 and 84 lines, inside 35 to 90.
- Discipline codes present on all task titles (`FE - iOS - TRACK - ...`, `BE - TRACK - ...`), following `fernhouse-context.md` line 93.
- Delivery kept after both `**Open:**` lines were settled. The reply names it and asks (`turn-2.md` line 28). No-gos hold the brief's list plus the two Turn 2 exclusions, so it is not all placeholder.
- Named additions, covered by `turn-2.md` line 28 and `turn-1.md` lines 32 to 39: three Rabbit holes.
- Borderline, not decisive: FE tasks translate `Status and estimate text` (task line 72). The brief says `Status text is translated` (brief line 44), and PST-004 asked about the estimate lines instead.

**Read-back table**

| Turn | Export path | `N` printed | Read after last write, lines returned | `wc -l` |
|---|---|---|---|---|
| 1 | `001 - Story-order-tracking/001 - Story-order-tracking.md` | 205 | Read #26 (offset 195), 195 to 205 of 205, after Edit #24 | Superseded |
| 1 | `001.1 - task-tracking-webhook.md` | 86 | Read #27, 80 to 86 of 86 | Superseded (renamed) |
| 1 | `001.2 - task-packed-status.md` | 36 | Read #28, 30 to 36 of 36 | Deleted in Turn 2 |
| 1 | `001.3 - task-web-tracking-timeline.md` | 75 | Read #29, 70 to 75 of 75 | Superseded |
| 1 | `001.4 - task-ios-tracking-timeline.md` | 74 | Read #30, 70 to 74 of 74 | Superseded (renamed) |
| 1 | `001.5 - task-android-tracking-timeline.md` | 74 | Read #31, 70 to 74 of 74 | Superseded (renamed) |
| 1 | `001.6 - task-tracking-timeline-events.md` | 39 | Read #32, 34 to 39 of 39 | Deleted in Turn 2 |
| 2 | `001 - Story-order-tracking/001 - Story-order-tracking.md` | 196 | Read #19, 1 to 196 of 196, after Edit #10 | 195 |
| 2 | `001.1 - task-ios-tracking-timeline.md` | 73 | Read #20, 68 to 73 of 73, after Write #14 | 72 |
| 2 | `001.2 - task-android-tracking-timeline.md` | 73 | Read #21, 68 to 73 of 73, after Write #15 | 72 |
| 2 | `001.3 - task-web-tracking-timeline.md` | 73 | Read #22, 68 to 73 of 73, after Write #16 | 72 |
| 2 | `001.4 - task-tracking-webhook.md` | 85 | Read #23, 80 to 85 of 85, after Write #17 | 84 |

**Realism entries**

- `001 - Story-order-tracking.md`, Story. Required sections present. References omitted with no links. Tasks block placed after Expected outcomes, which the rule allows when References is absent. Company facts: H1 `Customer - Order page - Order tracking` follows `fernhouse-context.md` line 95. `Packed` via orders-service matches line 72. Pallet carrier sends no tracking events, line 74 and line 150. Six locales match lines 128 to 132. No placeholder beyond exempt `TBD...`. 195 lines against 80 to 150 (advisory). Gate passed.
- `001.1 - task-ios-tracking-timeline.md`, Task. `### About`, `**Story**`, `**Related tasks**`, `### Requirements` present, no `**Parent task**`. Facts: `TRACK` code, line 105. Title pattern, line 93. Frame name from Turn 2. 72 lines inside 35 to 90. Code `FE`. Gate passed.
- `001.2 - task-android-tracking-timeline.md`, Task. Same shape and facts as `001.1`, 72 lines, code `FE`. Gate passed.
- `001.3 - task-web-tracking-timeline.md`, Task. Same shape, web layout in the same frame per Turn 2 (line 7), 72 lines, code `FE`. Gate passed.
- `001.4 - task-tracking-webhook.md`, Task. `### About`, `**Story**`, `**Related tasks**`, `### Requirements`, no `**Parent task**`. Facts: shipping-service owns tracking intake, `fernhouse-context.md` line 65. `TRACK`, line 105. BE drops the surface segment, line 93. Every API value from `fernhouse-carrier-tracking-api-facts.md` lines 7, 43 to 46. 84 lines inside 35 to 90. Code `BE`. Gate passed.
- The two Turn 1 files deleted in Turn 2 (`001.2 - task-packed-status.md`, `001.6 - task-tracking-timeline-events.md`) are not on disk, so the gate could not run on them.

**Open readings**

- Does a task list inside an attached brief (`fernhouse-order-tracking-pm-brief.md` lines 54 to 61) count as "a split the request names" under `SKILL.md` line 252 and `story-mode.md` line 406? The scenario says the request names none. Graded by the scenario. The `$story` ask-first rule (`AGENTS.md` line 287) applies either way.

---

### PST-004 (Project) Story with nested tasks

**Draft row**

```csv
PST-004,project,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Confirmed from turn-1.md: Turn 1 rendered seven fenced blocks, a Story plus six tasks including BE - TRACK - Packed status from the warehouse system (line 28) and DATA - TRACK - Tracking timeline events (line 32), with no Story question. That misses the Turn 1 clauses and hits the Fail example of a Packed or DATA task. Turn 2 rendered the correct five-block bundle. Advisory: Story block 178 lines against 80 to 150."
```

**Pass clauses**

| Clause | Result | Evidence |
|---|---|---|
| T1 asks one consolidated Story question in the Story lane | Unmet | `turn-1.md` line 600 `I wrote a **Story** ... plus six tasks following the split in Hamid's brief`. No question anywhere in the reply |
| T1 renders it as its own block with its `Export-equivalent path:` outside any folder and the HVR line | Unmet | Seven artifact blocks, labels at lines 194, 277, 314, 394, 475, 556, 596, all inside `export/NNN - Story-order-tracking-timeline/` |
| T1 renders no draft | Unmet | Story block lines 1 to 193, then six task blocks. Tasks block lines 25 to 32 lists six tasks |
| T2 renders one Deliverable Block per file, Story first | Met | Fenced blocks at lines 1 to 180, 183 to 252, 255 to 324, 327 to 396, 399 to 478 |
| Exactly four task blocks for FE iOS, FE Android, FE web, BE webhook in that order | Met | Block H1s at lines 184, 256, 328, 400 |
| Each followed by its own `Export-equivalent path:` inside `export/[NNN] - Story-[description]/` | Met | Lines 181, 253, 325, 397, 479 |
| One `HVR self-scan:` line for the set | Met | Line 481 |
| Names the Story kind | Met | Line 483 `I updated the **Story**` |
| Claims no file | Met with a borderline line | Line 483 `this set replaces the earlier seven files`. No save, write or read-back claim. See Open readings |
| Story holds About, Problem, Solution, Expected outcomes, `#### **Tasks**` inside About with one bullet per task in order linking `(<[NNN].[n] - task-...md>)`, Requirements, criteria with Mark-as-done | Met | Block lines 8, 12, 16, 20, 25 to 30, 34, 89. Criteria 1 to 7 at lines 93 to 151 |
| Each task holds `### About`, a `**Story**` block linking `(<NNN - Story-order-tracking-timeline.md>)`, no `**Parent task**`, `### Requirements` | Met | FE iOS lines 186, 200 to 204, 214. FE Android 258, 272 to 276, 286. FE web 330, 344 to 348, 358. BE 402, 408 to 412, 422. No `Parent task` in the reply |
| Set carries the statuses, codes and every listed value verbatim | Met | Story lines 39, 42 and 43, 54, 55, 63, 64, 70, 72, 75, 57, 53, 74 |

**Blocking items hit**

- Turn 1 Pass clauses missed: root line 150, with `Custom Instructions.md` line 108 and Project `Product Owner - Templates - Story Mode - v0.402.md` line 382.
- Fail example hit in Turn 1: `adds a Packed or DATA task` (scenario line 35), at `turn-1.md` lines 28, 32, 280 and 559.

**Advisory items**

- Size band: Story block 178 lines against 80 to 150. Task blocks 68, 68, 68, 78 inside 35 to 90.
- Block form: fenced in both turns. Each block's `Export-equivalent path:` follows its closing fence with no blank line. No commentary before the first block.
- Discipline codes present on every task title.
- Delivery kept after both open questions were settled. Named, with a question to the user, at line 493.

**Realism entries**

| Block | Kind | Sections | Facts checked | Lines (band) | Code | Gate |
|---|---|---|---|---|---|---|
| `PST-004-turn1-block1.md` | Story (superseded) | All present, two `**Open:**` lines, Delivery forced | H1 line 95, `TRACK` line 105, locales lines 128 to 132 | 191 (80 to 150) | n/a | Passed |
| `PST-004-turn1-block2.md` | Task, BE webhook | About, Story, Related tasks, Requirements | shipping-service line 65, API facts lines 43 to 46 | 79 | BE | Passed |
| `PST-004-turn1-block3.md` | Task, BE Packed (the Fail example) | About, Story, Related tasks, Requirements | warehouse reports packed line 72 | 33 (under 35) | BE | Passed |
| `PST-004-turn1-block4.md` | Task, FE web | About, References, Story, Related tasks, Requirements | frame name brief line 30 | 76 | FE | Passed |
| `PST-004-turn1-block5.md` | Task, FE iOS | Same | Same | 77 | FE | Passed |
| `PST-004-turn1-block6.md` | Task, FE Android | Same | Same | 77 | FE | Passed |
| `PST-004-turn1-block7.md` | Task, DATA (the Fail example) | About, Story, Related tasks, Requirements | tracking-plan rule line 164, event properties line 162 | 36 | DATA | Passed |
| `PST-004-turn2-block1.md` | Story | All present, Tasks block after Expected outcomes (no References), Delivery kept | H1 `Customer - Order tracking - Order page timeline` line 95, `Packed` via orders-service line 72, pallet no tracking lines 74 and 150, locales lines 128 to 132 | 178 (80 to 150) | n/a | Passed |
| `PST-004-turn2-block2.md` | Task, FE iOS | About, References, Story, Related tasks, Requirements, no Parent task | `TRACK` line 105, title pattern line 93, frame from Turn 2 | 68 | FE | Passed |
| `PST-004-turn2-block3.md` | Task, FE Android | Same | Same | 68 | FE | Passed |
| `PST-004-turn2-block4.md` | Task, FE web | Same, web layout in the same frame (line 334) | Same | 68 | FE | Passed |
| `PST-004-turn2-block5.md` | Task, BE webhook | About, Story, Related tasks, Requirements, no Parent task | shipping-service line 65, BE drops surface line 93, API facts lines 7 and 43 to 46 | 78 | BE | Passed |

Placeholders: only the exempt `TBD...` and the Project `NNN` slot, which the links inside the blocks also use.

**Open readings**

- Do `They're one folder with seven files` (`turn-1.md` line 600) and `this set replaces the earlier seven files` (`turn-2.md` line 483) count as file claims under root line 189? Graded not claims, since neither says anything was saved, written or read back. Not decisive here.
- Same brief-named split reading as `SST-004`.

---

### Twin notes

| Pair | Verdicts | Agree or differ | Notes |
|---|---|---|---|
| `SST-001` / `PST-001` | PASS / PASS | Agree | Both asked one Story question for the promised Guest Support asks and waited, then delivered every hard value in Requirements. The promised-input rule is stated on both sides (`AGENTS.md` line 283, `Custom Instructions.md` line 108). |
| `SST-002` / `PST-002` | FAIL / FAIL | Agree | Both drafted in Turn 1 on `$story` without the Story question, and both reworded `Do sub-pages inherit the link?` in the `**Open:**` line. Small difference: the skill Story adds an interim single-page build rule (export lines 38 and 172), and the Project Story does not. |
| `SST-003` / `PST-003` | FAIL / FAIL | Agree | Both refined at once on `$s` without the Story question. Both then met the refinement name, shape and values, and both raised the brand-storage conflict with `fernhouse-context.md` line 153 as an `**Open:**` line. |
| `SST-004` / `PST-004` | FAIL / FAIL | Agree | Both treated the brief's six-task list as the named split and delivered six tasks, Packed and DATA included, in Turn 1. Both repaired to the named four in Turn 2 with correct Tasks and Story blocks. |

Cause shared by the three failing pairs. The twins agree, so no divergence needs classifying. The shared cause is a conflict each packaging carries identically, so it is neither a parity gap nor a split between runtimes:

- Ask first on an explicit command: `AGENTS.md` line 287 and `Custom Instructions.md` line 108 (`$story` still asks and waits).
- Ask only when unclear: `sk-product-owner/references/story-mode.md` line 64 and Project `Product Owner - Templates - Story Mode - v0.402.md` line 41 (`Ask one consolidated question only when role, value, requirement shape or artifact kind cannot be established safely`). `sk-product-owner/references/interactive-mode.md` line 172 and Project `Product Owner - System - Interactive Mode - v0.405.md` line 149 (`if_kind_and_scope_inferable: processing`).
- Both runtimes followed the Story Mode and Interactive gate reading in all three pairs, each saying the attachments supplied enough to draft (`SST-002` turn-1.md line 7, `PST-002` turn-1.md line 187, `SST-004` turn-1.md line 1, `PST-004` turn-1.md line 600).
- For the bundle pair, `story-mode.md` line 406 and Project Story Mode line 382 add a second ambiguity: whether a split listed in an attached brief counts as one the request names.

### Open readings for the operator (batch summary)

1. Which rule governs Turn 1 on `$story` or `$s` with complete attachments: the ask-first command rule (`AGENTS.md` line 287, kernel line 108) or Story Mode's ask-only-when-unclear rule (`story-mode.md` line 64, `interactive-mode.md` line 172 and their Project mirrors)? Six FAILs rest on the Pass clause text, which follows the first.
2. Does a task split listed in an attached brief count as one "the request names" (`SKILL.md` line 252, `story-mode.md` line 406)?
3. Must the `**Open:**` line carry `Do sub-pages inherit the link?` word for word, or is the question in substance enough (`SST-002`, `PST-002`)?
4. Is "build against a single page until then" (`SST-002` export lines 38 and 172) settling the sub-page question, given fixture line 54?
5. Save card: is keeping the context card-data rule and marking the draft's stored brand `**Open:**` correct conflict handling, or an altered draft value (`SST-003` line 42, `PST-003` line 55)? This set `facts_intact` to `no` on both.
6. Do `312 stays` with only the number backticked, and `Guest checkout` capitalized at the start of a sentence, count as verbatim?
7. Should a partial Read (for example lines 100 to 144 of 144) count as the read-back? Full-file Reads happened only in `SST-001` Turn 1, `SST-002` Turn 2 and the `SST-004` Turn 2 Story. Every other skill read-back in this batch returned only a tail range.
8. Wrong `N`: `SST-002` Turn 1 printed 176 where Read returned 177.
9. Project wording such as "replaces the previous version under the same filename" and "one folder with seven files": are these file claims under root line 189?

---

## 10. Epics batch, grader draft

Run folder `<RUN>`: `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/`. Sources read from the working tree, which is clean for `sk-product-owner`, `claude project`, `AGENTS.md` and `benchmark/fixtures` (the `git status --porcelain` check printed nothing), so every source line below stands as at `3023c5e`. Event citations are line numbers inside the named `events-turn-<n>.jsonl`. Project block copies sit under `scratch/grades/blocks/epics/`.

Format gate results, one per export or block:

| File | Result |
|---|---|
| `skill/SEP-001 .../exports/export/001 - Epic-partner-self-onboarding.md` | passed |
| `skill/SEP-002 .../exports/export/001 - Epic-offline-mode-clarification.md` | passed |
| `skill/SEP-002 .../exports/export/002 - Epic-offline-mode.md` | passed |
| `skill/SEP-003 .../exports/export/001 - Epic-self-serve-returns.md` | passed |
| `blocks/epics/PEP-001-turn1 - Epic-partner-hub-self-onboarding-clarification.md` | passed |
| `blocks/epics/PEP-001-turn2 - Epic-partner-hub-self-onboarding.md` | passed |
| `blocks/epics/PEP-002-turn1 - Epic-offline-mode-clarification.md` | passed |
| `blocks/epics/PEP-002-turn2 - Epic-offline-mode.md` | passed |
| `blocks/epics/PEP-003-turn1 - Epic-self-serve-returns.md` | failed, 1 error: "prose connectives 3.4 per 1000 across 293 prose words, connective stripping leaves the reader guessing the relation" |

The gate does not check the required heading set, so a pass says nothing about `#### **References**`.

---

### SEP-001 (skill), Epic from strategy brief

**Draft row**

```csv
SEP-001,skill,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 drafted and saved the Epic (events-turn-1.jsonl line 86 Write of export/001 - Epic-partner-self-onboarding.md, reply turn-1.md lines 1 to 9) instead of asking one Epic question, so the Pass clause ""Turn 1 asks one Epic question in the Epic lane and drafts nothing"" is unmet and no -clarification export exists. The final Epic's shape, six stages and brief values are otherwise correct; advisory: 152 lines against the 90 to 150 band."
```

**Pass clauses**

| Clause | Met / Unmet | Evidence |
|---|---|---|
| Turn 1 asks one Epic question in the Epic lane | Unmet | `turn-1.md` lines 1 to 20 deliver an Epic, not a question. Run ledger `meta.json` turn 1: created `export/001 - Epic-partner-self-onboarding.md` only, no `-clarification` file |
| Turn 1 drafts nothing | Unmet | `events-turn-1.jsonl` line 86 Write of the Epic, line 85 thinking: "I'll draft the Epic now, flagging the release cut as open since it's not yet agreed" |
| Turn 2 saves one Epic | Met, with a caveat | Turn 2 edited the Turn 1 file in place (`events-turn-2.jsonl` lines 19 to 31, seven Edits); ledger turn 2 `modified`, not a new file on the next number |
| `# Epic - ` H1, no story preamble | Met | Export line 1 `# Epic - Partner - Self-onboarding`, line 3 `* * *`, line 4 `## About` |
| `## About` with Problem, Goal, Solution, References | Met | Export lines 8, 19, 31, 38 |
| `## Scope` names exactly six first-release child stories, one per stage name verbatim, as plain text | Met | Export lines 50, 54, 55, 56, 60, 64 carry `Sign-up and verification`, `Property profile and photos`, `Rooms and rates setup`, `Policies and city tax`, `Payout details and identity checks`, `Go-live review queue`; line 46 "All six stages ship in the first release" |
| `#### Added Later` holds the channel manager connection | Met | Export lines 66 to 71, `**Channel manager connection**` |
| Release-level `## Acceptance criteria` in `1\.` blocks each closed by Mark-as-done | Met | Export lines 80, 88, 95, 103, 111, 118, Mark-as-done at 86, 93, 101, 109, 116, 124 |
| No `## Requirements`, ticket header fields, story points or INVEST notes | Met | None in the export |
| Names the kind | Met | `turn-1.md` line 5 "I wrote this as an **Epic**", `turn-2.md` line 1 "I updated the Epic" |
| `11 business days`, `38%`, `3 business days`, `1,500`, `2027-06-30` verbatim | Met | Export lines 13, 14, 21, 23 |
| Invents no link | Met | Export lines 38 to 42 name two sources as plain text, no URL |
| No chains, over-40-room or channel manager properties in first-release scope | Met | Export lines 36, 111 to 116, 149 |
| No estimate the brief never gave, no unfilled slot | Met | Export lines 130 to 134, `TBD...` (exempt Delivery slot) |

**Blocking items hit**

- Pass clause "Turn 1 asks one Epic question in the Epic lane and drafts nothing" unmet, and the Fail clause "drafts in Turn 1" named in the scenario (root line 150, scenario acceptance at root line 144). Source rules: `AGENTS.md` line 283 (ask when scope is missing), line 287 (an explicit command does not supply direction), `SKILL.md` line 252 and line 284 rule 5
- Export names, skill-side order (root line 167): no clarification in the Epic lane, so the artifact is not on the number after it. Side-effect ledger (root line 106): the Turn 1 clarification turn created an Epic, not a `-clarification` export

**Advisory items**

- Size band: 152 lines against 90 to 150
- A `## Delivery` close was written; the scenario accepts it (scenario line 68)

**Read-back table**

| Turn | Export path | N printed | Read after last write | Lines returned | Real `wc -l` |
|---|---|---|---|---|---|
| 1 | `export/001 - Epic-partner-self-onboarding.md` | 148 | `events-turn-1.jsonl` line 99 (after Write line 86 and Bash perl edit line 97), result line 100 | 1 to 148 of 148 | Not recoverable, the file changed in Turn 2 (Read total implies 147) |
| 2 | `export/001 - Epic-partner-self-onboarding.md` | 153 | `events-turn-2.jsonl` line 33 (after last Edit line 31), result line 35 | 1 to 153 of 153 | 152 |

**Realism entry**

- `export/001 - Epic-partner-self-onboarding.md`, Epic. Required sections from `assets/epic-template.md` lines 41 to 112: H1, `## About`, `### Problem`, `### Goal`, `### Solution`, `#### **References**`, `## Scope`, `## Acceptance criteria` all present; `#### Added Later` present; optional `## Delivery` present
- Facts checked: `11 business days` export line 13 = brief line 10; `38%` with 813 of 2,140 export line 14 = brief line 11; up to 40 rooms and `3 business days` export line 21 = brief line 19; `1,500` by `2027-06-30` and 18,000 export line 23 = brief line 21; `8` photos, `20 MB` export line 54 = brief line 28; `1 business day` export line 64 = brief line 32; only an Owner changes payout details export line 60 = `roamstay-context.md` line 28; Europe and the United States export line 141 = context line 5; Bram, Ops Lead export line 46 = brief line 59
- Named additions: criterion 4 resubmit, squad split, Owner payout rule, three Rabbit holes (`turn-1.md` lines 11 to 18, `turn-2.md` lines 15 to 22)
- Borderline: criterion 5 (export lines 113 to 115) puts channel manager properties on "assisted onboarding with a partner manager", while the brief gives the partner manager only to over-40-room properties and chains (line 37) and says channel manager partners "stay on assisted onboarding for now" (line 38)
- Placeholder: none beyond the exempt `TBD...` at line 134
- Body 152 lines against 90 to 150 (advisory). H1 carries no discipline code, as the Epic H1 rule requires

**Open readings**

- `AGENTS.md` line 287 and `Custom Instructions.md` line 108 list `$task`, `$bug`, `$doc` and `$story` as commands that still ask, and neither names `$epic`. The story intake gate (`references/interactive-mode.md` lines 169 to 173) evaluates `child_stories` but has no release-cut field, and the brief supplies the six stages (brief line 63). Is an unagreed first release cut "scope missing" under `AGENTS.md` line 283 when the child-story set is supplied? The verdict follows the scenario's Pass clause either way
- `N` convention: `SKILL.md` line 211 says "Use the final line number Read returns as N". The Read tool reports one more line than `wc -l` for a file ending in a newline. Turn 2 printed 153 (Read) against `wc -l` 152. Which count is meant?

---

### PEP-001 (project), Epic from strategy brief

**Draft row**

```csv
PEP-001,project,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 asked one Epic-lane question and drafted nothing, but the Turn 2 Epic block has no #### **References** (turn-2.md Solution at lines 37 to 46 runs straight into ## Scope at line 47), a Pass clause and a required slot of the Project Epic Template (line 53) and kernel line 140. Advisory: Turn 1 asks for facts the brief states (turn-1.md lines 11 and 28)."
```

**Pass clauses**

| Clause | Met / Unmet | Evidence |
|---|---|---|
| Turn 1 asks one Epic question in the Epic lane | Met | `turn-1.md` lines 1 to 29 one fenced question block, line 31 `Export-equivalent path: export/001 - Epic-partner-hub-self-onboarding-clarification.md`, line 33 HVR line |
| Turn 1 drafts nothing | Met | `turn-1.md` line 37 "I haven't drafted it yet" |
| `# Epic - ` H1, no story preamble | Met | `turn-2.md` line 2 `# Epic - Partner Hub - Self-onboarding`, line 4 `* * *`, line 5 `## About` |
| `## About` with Problem, Goal, Solution and `#### **References**` | Unmet | Problem line 9, Goal line 20, Solution line 37; no References heading before `## Scope` at line 47. `turn-1.md` line 25 "If not, I'll leave References out" |
| `## Scope` names exactly six child stories, stage names verbatim, plain text | Met | `turn-2.md` lines 55 to 59 and 65; line 49 "all six ship in the first release" |
| `#### Added Later` holds the channel manager connection | Met | `turn-2.md` lines 67 to 72 |
| Release-level criteria in `1\.` blocks with Mark-as-done | Met | Lines 81, 90, 99, 109, 117; Mark-as-done 88, 97, 107, 115, 124 |
| No `## Requirements`, header fields, story points, INVEST | Met | None in the block |
| Consults only the Epic scaffold | Met | `events-turn-1.jsonl` line 21 Read of `Product Owner - Assets - Epic Template - v0.100.md`; no Story Template read; Turn 2 made no tool calls |
| Names the kind | Met | `turn-1.md` line 37 "This will be an Epic", `turn-2.md` line 155 "The Epic has" |
| `11 business days`, `38%`, `3 business days`, `1,500`, `2027-06-30` verbatim | Met | `turn-2.md` lines 14, 15, 22, 24 |
| Invents no link | Met | No link in the block |
| Claims no file | Met in Turn 2, borderline in Turn 1 | `turn-2.md` line 151 `Export-equivalent path:` only. `turn-1.md` line 37 "leave this question file unchanged" (see Open readings) |

**Blocking items hit**

- Pass clause: `## About` holding `#### **References**` unmet (root line 150)
- Ticket realism, "A required section of the routed template missing" (root line 205): the Project Epic Template mirror carries `#### **References**` at line 53 with no optional marker, and `Custom Instructions.md` line 140 says an Epic "opens with a `## About` umbrella carrying `### Problem`, `### Goal`, `### Solution` and `#### **References**`"

**Advisory items**

- Asking for a fact an attachment already states (root line 211): `turn-1.md` line 11 asks whether the Goal should use the brief's targets as written, line 28 asks whether any brief number changed since 2026-09-22
- Block form: fenced (```` ```markdown ````), at the very start of both replies, no commentary before it

**Realism entries**

- Turn 1 clarification block (`blocks/epics/PEP-001-turn1 - Epic-partner-hub-self-onboarding-clarification.md`, 27 lines), question only. Facts checked: `1,500` by `2027-06-30` line 11 = brief line 21; hotels, guesthouses and apartment buildings line 6 = brief line 36; 8 photos, 20 MB, 40 rooms, 1 business day line 28 = brief lines 28, 36, 32; `2026-09-22` line 28 = brief line 4. No placeholder
- Turn 2 Epic block (`blocks/epics/PEP-001-turn2 - Epic-partner-hub-self-onboarding.md`, 147 lines, band 90 to 150, in band). Required sections from the Project Epic Template lines 22 to 93: `#### **References**` missing; every other scaffold section present; optional `## Delivery` present (line 128), named in `turn-2.md` line 162. Facts checked: `11 business days` line 14 = brief line 10; `38%`, 813 of 2,140 line 15 = brief line 11; 40 rooms and `3 business days` line 22 = brief line 19; `1,500`, `2027-06-30`, 18,000 line 24 = brief line 21; about 4.5 hours line 16 = brief line 12; `1 business day` lines 99 and 103 = brief line 32; Bram, Ops Lead line 45 = brief line 59. Placeholder: only the exempt `TBD...` at line 134. H1 carries no discipline code
- Borderline: `turn-2.md` line 157 says Freya's Goal and target "are copied word for word", but line 24 reads "The target is 1,500 ... Roamstay has 18,000 properties live today" where the brief reads "Target: 1,500 ... For scale, Roamstay has 18,000" (line 21); the values are intact. Line 140 says Ops Tools sizes the queue "with the Partner squad", where the brief says "with us" (line 52), written by the Director of Partner Growth

**Open readings**

- Should an Epic's `#### **References**` be omitted when no link is supplied, as `assets/story-template.md` line 66 and the Project Story Template line 47 say for a Story ("Omit the whole section when none are supplied")? The Epic template (skill line 74, Project line 55) says only "{Supplied links only.}", and `Custom Instructions.md` line 140 lists References in the Epic About. If the operator reads References as optional in an Epic, this grader found no other unmet clause here except the Turn 1 file reading below
- Is `turn-1.md` line 37, "leave this question file unchanged", a file claim under root line 189? It claims no save, write or read-back, but it speaks of a question file

---

### SEP-002 (skill), Epic natural wording

**Draft row**

```csv
SEP-002,skill,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 asked one Epic-lane question and saved only export/001 - Epic-offline-mode-clarification.md; Turn 2 saved export/002 - Epic-offline-mode.md in the house shape with the four areas verbatim, 23% and 31%, Web out and conflict handling left open on 2026-10-09. The Turn 2 read-back was a partial Read (lines 78 to 107) and N=106 against Read's 107, both listed as open readings."
```

**Pass clauses**

| Clause | Met / Unmet | Evidence |
|---|---|---|
| Turn 1 resolves the Epic kind from wording alone | Met | `turn-1.md` line 7 "This is an Epic"; export word `Epic` in `001 - Epic-offline-mode-clarification.md` |
| Turn 1 asks one Epic question in the Epic lane | Met | Clarification file lines 1 to 17, one consolidated question; `turn-1.md` line 3 path, line 4 `Verified:` line, line 5 HVR line |
| Turn 1 drafts nothing | Met | Ledger turn 1 created only the clarification; file holds no draft |
| `# Epic - ` H1, no story preamble | Met | Export line 1 `# Epic - Member - Offline mode`, line 3 `* * *`, line 4 `## About` |
| `## About` with Problem, Goal, Solution, References | Met | Export lines 9, 20, 33, 49 |
| `## Scope` names exactly the four areas verbatim as plain text, each across iOS, Android and Desktop | Met | Export lines 63, 64, 70, 71; line 57 "for iOS, Android and Desktop"; line 7 "Each story covers iOS, Android and Desktop together" |
| Release-level criteria in `1\.` blocks with Mark-as-done | Met | Lines 80, 88, 97; Mark-as-done 86, 95, 104 |
| No `## Requirements`, header fields, story points, INVEST | Met | None in the export |
| Names the kind | Met | `turn-2.md` line 1 "I've written the epic" |
| `23%` and `31%` verbatim | Met | Export lines 14 and 15 |
| Web out of every child story and criterion | Met | Child stories lines 63 to 71 and criteria lines 80 to 104 name no Web; line 41 and line 44 exclude it |
| Conflict handling a dependency on the `2026-10-09` decision | Met | Export lines 61, 66, 68 |
| No plan limit, no altered brief value, no invented link | Met | Line 6 "every plan, Free included"; values checked below; References lines 51 to 53 plain text |

**Blocking items hit**

None.

**Advisory items**

- `turn-1.md` lines 11 to 14 repeat part of the question in chat, which root line 156 leaves ungraded
- Size band: 106 lines, inside 80 to 140

**Read-back table**

| Turn | Export path | N printed | Read after last write | Lines returned | Real `wc -l` |
|---|---|---|---|---|---|
| 1 | `export/001 - Epic-offline-mode-clarification.md` | 18 | `events-turn-1.jsonl` line 49 (after Edit line 47), result line 50 | 1 to 18 of 18 | 17 |
| 2 | `export/002 - Epic-offline-mode.md` | 106 | `events-turn-2.jsonl` line 56 (after last Edit line 50), result line 57 | 78 to 107 of 107, a partial Read with `offset` 78 | 106 |

**Realism entries**

- `export/001 - Epic-offline-mode-clarification.md`, clarification, question only. Facts checked: `2026-10-09` lines 7 and 13 = brief line 32; Desktop wraps the web client and a web change reaches Desktop with no release, line 9 = `loomlist-context.md` lines 12 and 18; a protocol change needs every client on a new version, line 15 = context line 177; "a member" line 17 = brief line 14. No placeholder
- `export/002 - Epic-offline-mode.md`, Epic. Required sections from `assets/epic-template.md` lines 41 to 112 all present; no `#### Added Later`, which the template marks optional (line 118); no Delivery. Facts checked: `23%` line 14 and `31%` line 15 = brief line 8; block-level last-writer-wins on protocol v3 line 17 = brief line 26 and context line 70; Q1 2027 line 6 = brief line 36; "drops by half within 8 weeks of release" line 29 = brief line 40; out-of-scope list lines 44 to 47 = brief lines 45 to 48; Joana, Engineering Manager, Sync, `2026-10-09` line 68 = brief line 32; shared on 2026-09-23 line 52 = brief line 4. No placeholder. H1 carries no discipline code
- Named additions: `turn-2.md` lines 13 to 16 (drafting before the decision, the open Web client question, members only)
- Borderline: criterion 2 (export lines 90 to 93) says every offline change "reaches the workspace ... and teammates see it", which restates the brief Goal (line 14) but could be read as a conflict outcome; export line 68 raises whether a Web client protocol update belongs to the epic as undecided, named at `turn-2.md` line 15. The label `**Direct user/Loomlist benefits:**` (line 24) replaces the template's fixed `Direct user/Barter benefits:`

**Open readings**

- Does a read-back pass when the only Read after the last Edit is partial (`offset` 78, lines 78 to 107 of 107)? The brief's test ("returned file content") is met
- `N` convention (`SKILL.md` line 211): Turn 2 printed 106, the real `wc -l`, where the final line number the Read returned was 107. Turn 1 printed Read's 18 against `wc -l` 17. Which count is meant?

---

### PEP-002 (project), Epic natural wording

**Draft row**

```csv
PEP-002,project,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Every clause holds except the house shape: the Epic block omits #### **References** (turn-2.md Solution lines 29 to 38 run into ## Scope at line 39, and line 119 says it was left out), which the Pass clause, the Project Epic Template line 53 and kernel line 140 require."
```

**Pass clauses**

| Clause | Met / Unmet | Evidence |
|---|---|---|
| Turn 1 resolves the Epic kind from wording alone | Met | `turn-1.md` line 24 "I'm treating this as an Epic" |
| Turn 1 asks one Epic question in the Epic lane, drafts nothing | Met | `turn-1.md` lines 1 to 18 fenced question block, line 20 `Export-equivalent path: export/001 - Epic-offline-mode-clarification.md`, line 22 HVR line, line 24 "I haven't drafted it yet" |
| `# Epic - ` H1, no story preamble | Met | `turn-2.md` line 2 `# Epic - Member - Offline mode`, line 4 `* * *`, line 5 `## About` |
| `## About` with Problem, Goal, Solution and `#### **References**` | Unmet | Problem line 9, Goal line 18, Solution line 29, then `## Scope` at line 39; line 119 "I left out that section because you haven't shared any links yet" |
| `## Scope` names exactly the four areas verbatim, each across iOS, Android and Desktop | Met | Lines 47, 48, 52, 53; line 41 "covers iOS, Android and Desktop together" |
| Release-level criteria in `1\.` blocks with Mark-as-done | Met | Lines 69, 77, 86, 94; Mark-as-done 75, 84, 92, 101 |
| No `## Requirements`, header fields, story points, INVEST | Met | None in the block |
| Consults only the Epic scaffold | Met | `events-turn-1.jsonl` line 14 Read of the Epic Template; Turn 2 read the Epic example and Conciseness only; no Story Template read |
| Names the kind | Met | `turn-2.md` line 110 "The epic is ready" |
| `23%` and `31%` verbatim | Met | `turn-2.md` line 11 |
| Web out of every child story and criterion | Met | Web only under `#### Out of scope`, line 57; criteria name iOS, Android or Desktop |
| Conflict handling a dependency on `2026-10-09` | Met | Lines 43, 45, 50; criterion 2 line 82 limits itself to changes "that did not conflict" |
| No plan limit, no altered value, no invented link, claims no file | Met | Line 7 "every plan, including Free"; values below; no link; line 106 `Export-equivalent path:` only |

**Blocking items hit**

- Pass clause: `## About` holding `#### **References**` unmet (root line 150)
- Ticket realism, "A required section of the routed template missing" (root line 205): Project Epic Template line 53, `Custom Instructions.md` line 140

**Advisory items**

- Block form: fenced, at the start of both replies, no commentary before it
- Size band: 102 lines, inside 80 to 140

**Realism entries**

- Turn 1 clarification block (`blocks/epics/PEP-002-turn1 - Epic-offline-mode-clarification.md`, 16 lines), question only. Facts checked: `2026-10-09` line 5 = brief line 32; Desktop wraps the web client, line 6 = context line 12; `FE - iOS - OFFL - ...` pattern line 7 = context lines 104 and 125; every client needs the new protocol line 11 = context line 177. No placeholder
- Turn 2 Epic block (`blocks/epics/PEP-002-turn2 - Epic-offline-mode.md`, 102 lines). Required sections from the Project Epic Template: `#### **References**` missing, the rest present. Facts checked: `23%`, `31%` line 11 = brief line 8; 500 pages, blocks, inline databases, to-dos, 1 GB line 32 = brief line 22; within 30 seconds, oldest first line 35 = brief line 26; Joana, `2026-10-09`, #sync-eng line 43 = brief line 32; Q1 2027 line 7 = brief line 36; 8 weeks line 25 = brief line 40; out-of-scope list lines 57 to 60 = brief lines 18 and 45 to 48. No placeholder. H1 carries no discipline code
- Borderline: line 43 "a device that was offline for a day" where the brief says "a phone" (line 26); the label `**Direct user/Loomlist benefits:**` (line 22) replaces the fixed template line and is not named in the reply

**Open readings**

- The same References question as PEP-001: is `#### **References**` optional in an Epic when no link is supplied? The runtime read the Epic example (`events-turn-2.jsonl` line 6), which carries References at its line 45. If the operator reads it as optional, this grader found no other unmet clause here

---

### SEP-003 (skill), Epic quick energy

**Draft row**

```csv
SEP-003,skill,claude-opus-5-5-medium,PASS,1,1,pending,yes,"One turn, no question, one Epic at export/001 - Epic-self-serve-returns.md in the house shape with the four child stories, guest returns under Added Later, pallet items with CS and 60%, Q1 2027, 1,900, 6 days and 30 days as supplied. Borderline: a References link to ../context/fernhouse-context.md and criterion 3's ""as it does today"", both named in the reply."
```

**Pass clauses**

| Clause | Met / Unmet | Evidence |
|---|---|---|
| The one turn asks nothing | Met | `turn-1.md` lines 1 to 17 hold no question; ledger created only the Epic |
| Saves one Epic | Met | Ledger turn 1 `created: export/001 - Epic-self-serve-returns.md` |
| `# Epic - ` H1, no story preamble | Met | Export line 1 `# Epic - Customer - Self-serve returns`, line 3 `* * *`, line 4 `## About` |
| `## About` with Problem, Goal, Solution, References | Met | Export lines 8, 18, 27, 36 |
| `## Scope` names exactly the four prompt child stories as plain text | Met | Export lines 47, 48, 52, 53 |
| `#### Added Later` holds guest returns | Met | Export lines 55 to 60 |
| Release-level criteria in `1\.` blocks with Mark-as-done | Met | Lines 69, 78, 87; Mark-as-done 76, 85, 94 |
| No `## Requirements`, header fields, story points, INVEST | Met | None in the export |
| Names the kind | Met | `turn-1.md` line 1 "I've written the Epic" |
| `60%` and `Q1 2027` verbatim | Met | Export line 20 |
| Context numbers exactly as `fernhouse-context.md` | Met | `1,900` and `6 days` export line 10 = context line 145; `30 days` lines 30, 71, 89 = context line 53 |
| No guest returns or pallet items in first-release scope | Met | Lines 34, 43, 87 to 94 |
| No invented return fee, carrier name or link | Met, borderline on the link | No fee, no carrier; line 39 links `../context/fernhouse-context.md`, the supplied attachment, named at `turn-1.md` line 15 |

**Blocking items hit**

None.

**Advisory items**

- Size band: 96 lines, inside 60 to 110
- `turn-1.md` line 7 notes `validate-output-format.cjs` is not in the sandbox, a true statement about the sandbox copy

**Read-back table**

| Turn | Export path | N printed | Read after last write | Lines returned | Real `wc -l` |
|---|---|---|---|---|---|
| 1 | `export/001 - Epic-self-serve-returns.md` | 96 | `events-turn-1.jsonl` line 44 (after Write line 33 and Bash `sed -i` edit line 39), result line 45 | 1 to 97 of 97 | 96 |

**Realism entry**

- `export/001 - Epic-self-serve-returns.md`, Epic. Required sections from `assets/epic-template.md` lines 41 to 112 all present; no Delivery, as Quick never opts it in. Facts checked: `1,900` a month and `6 days` export line 10 = context line 145; CS agent creates the return in Admin and emails a label, export line 10 = context line 145; `30 days` window line 30 = context line 53; web, iOS and Android line 6 = context lines 13 to 15; a guest has no order history, line 60 = context line 35; `60%`, Q1 2027 line 20 = the prompt. No placeholder. H1 carries no discipline code
- Named additions: `turn-1.md` lines 12 to 15 (Problem bullets from context, criterion 3, the "Returns" segment, the References link)
- Borderline: criterion 3 (export lines 89 to 92) says a return past `30 days` "goes through CS as it does today", which the context does not state (line 145 gives only the 30-day window); named at `turn-1.md` line 13. Problem line 15 says the customer cannot see where a return stands, named at line 12 and supported indirectly by context line 144. The label `**Direct customer and Fernhouse benefits:**` (line 22) replaces the fixed template line

**Open readings**

- Is a relative link to a supplied attachment (`[Fernhouse company context](<../context/fernhouse-context.md>)`, export line 39) an invented link under the Fail clause, given `references/story-mode.md` line 163 ("Links appear only when supplied") and the template slot "{Supplied links only.}" (`epic-template.md` line 74)? It resolves to the staged file and the reply names it
- `N` convention (`SKILL.md` line 211): printed 96, the real `wc -l`, where the Read's final line number was 97

---

### PEP-003 (project), Epic quick energy

**Draft row**

```csv
PEP-003,project,claude-opus-5-5-medium,FAIL,1,1,pending,yes,"No question and a fenced Epic block with the four child stories, guest returns under Added Later and pallet items with CS, but #### **References** is missing (turn-1.md Solution lines 32 to 39 run into ## Scope at line 40, reply line 123), a Pass clause and a required Project Epic Template slot. The format gate also flags prose connective density 3.4 per 1000."
```

**Pass clauses**

| Clause | Met / Unmet | Evidence |
|---|---|---|
| The one turn asks nothing | Met | `turn-1.md` holds one Epic block and no question |
| Renders one Epic | Met | `turn-1.md` lines 1 to 112 fenced block, line 114 `Export-equivalent path: export/001 - Epic-self-serve-returns.md` |
| `# Epic - ` H1, no story preamble | Met | Line 2 `# Epic - Customer - Self-serve returns`, line 4 `* * *`, line 5 `## About` |
| `## About` with Problem, Goal, Solution and `#### **References**` | Unmet | Problem line 10, Goal line 21, Solution line 32, then `## Scope` at line 40; line 123 "No References block ... I left the block out" |
| `## Scope` names exactly the four prompt child stories as plain text | Met | Lines 46, 47, 51, 52 |
| `#### Added Later` holds guest returns | Met | Lines 54 to 59 |
| Release-level criteria in `1\.` blocks with Mark-as-done | Met | Lines 68, 77, 85, 94, 103; Mark-as-done 75, 83, 92, 101, 109 |
| No `## Requirements`, header fields, story points, INVEST | Met | None in the block |
| Consults only the Epic scaffold | Met | `events-turn-1.jsonl` line 8 Read of the Epic Template; no Story Template read |
| Names the kind | Met | Line 118 "**Artifact kind:** Epic" |
| `60%` and `Q1 2027` verbatim | Met | Line 23 |
| Context numbers exactly as the context | Met | `1,900`, `6 days` lines 12 and 15 = context line 145; `30 days` lines 7, 70, 79 = context line 53 |
| No guest returns or pallet items in first-release scope | Met | Lines 42, 54 to 59, 103 to 107 |
| No invented fee, carrier or link; claims no file | Met | None; line 114 `Export-equivalent path:` only |

**Blocking items hit**

- Pass clause: `## About` holding `#### **References**` unmet (root line 150)
- Ticket realism, "A required section of the routed template missing" (root line 205): Project Epic Template line 53, `Custom Instructions.md` line 140

**Advisory items**

- Format gate finding on the block: prose connective density 3.4 per 1000 across 293 prose words (evidence only, no Pass clause names it)
- Block form: fenced, at the start of the reply, no commentary before it
- Size band: 110 lines, at the top of 60 to 110

**Realism entry**

- Epic block (`blocks/epics/PEP-003-turn1 - Epic-self-serve-returns.md`, 110 lines). Required sections from the Project Epic Template: `#### **References**` missing, the rest present; no Delivery. Facts checked: `1,900` and `6 days` line 12 = context line 145; the order page stops at `Shipped`, line 18 = context line 144; `30 days` window lines 7, 70, 79 = context line 53; a guest has no order history, line 59 = context line 35; `60%`, Q1 2027 line 23 = the prompt. No placeholder. H1 carries no discipline code
- Named addition: criterion 2, `turn-1.md` line 125

**Open readings**

- The same References question as PEP-001. If the operator reads Epic References as optional when no link is supplied, this grader found no other unmet clause here

---

### Twin notes

**SEP-001 / PEP-001: differ in why each fails.** The skill drafted in Turn 1; the Project asked first and then dropped References in Turn 2.

- Turn 1 behavior, a runtime fault over a shared rule gap. Both packagings say the same thing: `AGENTS.md` line 283 and `Custom Instructions.md` line 108 both ask one question when scope is missing, and both then list `$task`, `$bug`, `$doc` and `$story` (not `$epic`) as commands that still ask (`AGENTS.md` line 287, `Custom Instructions.md` line 108). The story intake gate matches on both sides (`references/interactive-mode.md` lines 169 to 173, Project Interactive Mode lines 146 to 150) and has no release-cut field. The Project asked and the skill did not, from identical text
- References, a runtime fault. Both sides carry References in the Epic scaffold (`assets/epic-template.md` lines 72 to 78, Project Epic Template lines 53 to 59) and in the Epic draft order (`references/story-mode.md` line 206, Project Story Mode line 182), and the kernel names it (`Custom Instructions.md` line 140). The skill kept it (export line 38); the Project left it out

**SEP-002 / PEP-002: differ.** The skill passes. The Project matches it on every clause but drops `#### **References**`. The rule lines are the ones above and read the same on both sides, so this is a runtime fault. A shared ambiguity may feed it: both Story templates say to omit References when no link is supplied (`assets/story-template.md` line 66, Project Story Template line 47), while both Epic templates leave the slot as "{Supplied links only.}" with no omission rule (`assets/epic-template.md` line 74, Project Epic Template line 55)

**SEP-003 / PEP-003: differ.** The skill passes. The Project drops References and says so (`turn-1.md` line 123). This is the same runtime fault as the two pairs above, with the same rule lines on both sides. All three Project Epics omit References, and all three skill Epics keep it: the skill with plain-text sources (SEP-001, SEP-002) or a link to the context file (SEP-003). The pattern holds for every Project Epic, so the orchestrator may want to raise the Epic References reading once, not three times
