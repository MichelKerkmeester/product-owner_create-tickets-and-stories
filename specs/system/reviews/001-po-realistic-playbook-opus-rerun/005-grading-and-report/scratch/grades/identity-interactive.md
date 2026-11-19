# Grades: identity-interactive batch

Run: `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/`. Model `claude-opus-5-5-medium`. Sources read from the working tree: `git -C "AI Systems/Product Owner" status --porcelain -- sk-product-owner "claude project" AGENTS.md benchmark/fixtures` printed nothing, and `git diff --stat 3023c5e HEAD` over the same paths is empty (HEAD `e9edb95` only adds the run), so every source line cited below is the line at `3023c5e`.

## Handover verdicts

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

## Tally

| Runtime | PASS | FAIL | SKIP |
|---|---:|---:|---:|
| skill | 3 (SID-001, SIR-001, SIR-002) | 0 | 0 |
| project | 2 (PID-001, PIR-002) | 1 (PIR-001) | 0 |

Every Project block was fenced (```` ```markdown ```` at reply line 1), with no text before it. Copies for the format gate are in `scratch/grades/blocks/identity-interactive/` and are byte-identical to the collector's copies under `AI Systems/Product Owner/export/benchmark/claude project/`. The skill exports in the run folder are byte-identical to `export/benchmark/skill/`.

---

## SID-001 (skill)

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

## PID-001 (project)

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

## SIR-001 (skill)

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

## PIR-001 (project)

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

## SIR-002 (skill)

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

## PIR-002 (project)

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

## Twin notes

- **SID-001 and PID-001: agree (PASS, PASS).** Both route `$task` to Task Mode and ask once before drafting (`AGENTS.md` line 287, `Custom Instructions.md` line 108), both deliver the clarification in the `task` lane, and both tasks keep every Turn 2 fact with the additions named. Each reply carries only its own runtime's delivery wording. Both extend `Yara has already added` into "no further Data review" (skill export line 43, Project turn-2.md line 52), a shared borderline item.
- **SIR-001 and PIR-001: differ (PASS, FAIL).** Cause: runtime fault. Both packagings carry the same Epic scaffold with `#### **References**` between Solution and Scope (skill `assets/epic-template.md` lines 72 to 78 and `references/story-mode.md` line 206; Project `Product Owner - Assets - Epic Template - v0.100.md` lines 53 to 59 and `Product Owner - Templates - Story Mode - v0.402.md` line 182). The skill kept the heading with `No designs or linked documents yet.` (export lines 37 to 39) and the Project dropped it. Both packagings share a rule gap underneath: the Story templates say `Omit the whole section when none are supplied` (skill `assets/story-template.md` line 66, Project Story Template line 47) and neither Epic template does, which is what leaves PIR-001's reading open. Everything else agrees: energy first, the deliverable type asked, the intake lane, the Epic kind, the numbers verbatim and Pay now only.
- **SIR-002 and PIR-002: agree (PASS, PASS).** Both name the Bug and the Story in one intake question and wait. Both also offer an Epic and lean toward Story in the question (skill clarification line 5, Project turn-1.md line 11) under the same rule on both sides (`references/interactive-mode.md` line 97, Interactive Mode knowledge line 74). Both omit References under the same Story Template omit sentence, and both name the kept-once dedupe as an addition. Differences are illustrative slugs and the skill's two-line overrun of the size band.
