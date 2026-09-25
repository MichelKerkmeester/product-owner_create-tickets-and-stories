# Grading notes, 2026-09-25, Product Owner, claude-sonnet-5 medium

Evidence behind every verdict in `results.csv`. Paths are relative to this folder unless they start with `sk-product-owner/`, `claude project/` or `AGENTS.md`, which are relative to `AI Systems/Product Owner/`. Playbook line numbers refer to the playbook at Barter `4fb9dd88`. Scenario files use the same line layout: Expected signals line 31, Pass/fail line 33, Turn 1 row line 40, Turn 2 row line 41, Pass bullet line 68, Fail bullet line 69. The two handover files differ: `skill-identity/identity-handover.md` has them at 30, 32, 39, 40, 78 and 79, and `project-identity/identity-handover.md` at 30, 32, 39, 40, 76 and 77.

---

## 1. How the rules were applied

**Verdict rule.** Root line 125: a turn that misses any Pass clause fails the scenario, and there is no verdict between PASS and FAIL. Root line 119: every turn must match expected behavior.

**Invented facts.** Root line 156 makes "an invented fact: a requirement, value, status, approval or behavior the user never supplied" blocking. The playbook gives no exception for an addition the reply discloses. The open conflict on exactly that point ("Whether a disclosed extra checklist item breaks NEVER 4", `specs/075-playbook-rerun-sonnet-5-medium/001-playbook-audit-and-refinement/implementation-summary.md` line 152) was not settled here. Per the operator's grade-as-written ruling, disclosed additions are graded by the playbook text and the conflict is logged in `README.md` section 6. To keep the test objective, an item counts as invented only when it adds a capability, flow, message, validation rule, value, scope boundary or claim about current behavior that the user's turns do not contain. The direct test or negation of a supplied condition does not count: "reason required" covers "an empty reason blocks the pause", and "indicator on a paused payout" covers "no indicator on an unpaused payout". Items that sit between the two are named as borderline and never decide a verdict alone.

**Canvas stand-in.** Root lines 132 and 136 and operator ruling 2: a Project block counts as rendered only when it sits in the reply as one delimited block before any commentary. A bare label line naming the block (`Deliverable Block (Canvas Artifact):`, `# Deliverable Block`, `**Deliverable Block: Story**`) was read as the block's own heading, not commentary. Sentences explaining why the runtime is asking were read as commentary. Root line 164 lists response ordering as advisory unless the scenario tests delivery shape. Every Project scenario tests the rendered block, and root line 132 puts "before any commentary" into every Turn 1 clarification check, so ordering decides Project Turn 1 verdicts here.

**Skill read-back.** A read-back claim is true only when the event stream shows a Read of the exact export path after the final Write or Edit and that Read returned file content (`AGENTS.md` line 46, "Verification passes only when Read returns non-empty content at that path"). The `N` each reply printed is recorded beside the final line number its Read returned and the file's real line count (`wc -l`, every file ends in a newline). A wrong `N` was not failed, because whether it fails is a recorded open conflict (implementation summary line 152) and no scenario text makes it a failure.

**HVR lint.** Kept a separate axis from verdicts, as the 2026-09-17 report did. Section 6 records where a lint hit sits inside a delivered artifact.

**Tools used for evidence.** A trace of every `tool_use` and `tool_result` in `*/events-turn-*.jsonl` (Write and Edit paths, Read offsets and the line numbers each Read returned), `wc -l` and `tail -c1` on every file in `skill/*/exports/export/`, and the shared format gate `node validate-output-format.cjs --system product-owner <file>`, run from the Claude Project Sync Loop folder at the `AI Systems/` root, run on every skill export and on every Project block extracted from its reply into a scratch file.

### Read-back table, skill side

| Scenario, turn | Export | `N` printed | Read after final write, lines returned | Real lines |
| --- | --- | ---: | --- | ---: |
| SID-001 T1 | `001 - task-payout-pause-toggle.md` | 65 | offset 60: 60 to 66 | 65 |
| STK-001 T1 | `001 - task-creator-payout-pause-clarification.md` | 33 | full: 1 to 33 | 32 |
| STK-001 T2 | `002 - task-creator-payout-pause-indicator.md` | 60 | limit 5: 1 to 5, then offset 50: 50 to 60 | 59 |
| SBG-001 T1 | `001 - bug-payout-pause-toggle-clarification.md` | 13 | full: 1 to 13 | 12 |
| SBG-001 T2 | `002 - bug-payout-pause-toggle-reverts-to-off.md` | 75 | offset 60: 60 to 75, then an Edit, then offset 28 limit 10: 28 to 37 | 74 |
| SDK-001 T1 | `001 - doc-notification-retry-pipeline-clarification.md` | 11 | full: 1 to 11 | 10 |
| SDK-001 T2 | `002 - doc-notification-retry-requeue-guide.md` | 48 | offset 50: no content, only the warning "the file exists but is shorter than the provided offset (50). The file has 48 lines." | 47 |
| SDK-002 T1 | none | none | no tool call of any kind | none |
| SDK-002 T2 | `001 - doc-payout-pause-behavior.md` | 47 | full: 1 to 47, then an Edit, then offset 14 limit 10: 14 to 23 | 46 |
| SST-001 T1 | `001 - PRD-payout-pause-clarification.md` | 12 | full: 1 to 12 | 11 |
| SST-001 T2 | `002 - PRD-payout-pause.md` | 78 | offset 80: warning only, then offset 60: 60 to 78 | 77 |
| SIR-001 T1 | `001 - intake-creator-payout-flow-clarification.md` | 39 | full: 1 to 39 | 38 |
| SIR-001 T2 | `002 - task-payout-pause-reason-detail.md` | 25 | full: 1 to 25 | 24 |

The Read tool numbers a newline-terminated file one line past its real length and shows that last line blank. So a reply that follows `AGENTS.md` line 46 literally always prints the real line count plus one. Every printed value except SID-001's does that. SID-001 printed the real count (65) instead of Read's final line (66).

---

## 2. Skill scenarios

### SID-001, skill identity handover: FAIL

- Turn 1 proof holds. `replies/SID-001-turn1.txt` line 1 `Path: \`export/001 - task-payout-pause-toggle.md\``, line 2 `Verified: read-back succeeded; 65 lines`, line 3 `HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: none.` No Canvas or export-equivalent wording in either reply (grep of `replies/S*.txt` for `canvas`, `export-equivalent` and `deliverable block` returns nothing). The file exists, 65 lines, and the Read at offset 60 returned lines 60 to 66 after the only Write
- Turn 2 misses the path. Scenario lines 30, 40 and 78 require Turn 2 to repeat or name the saved path ("Turn 2 repeats the same path and proof", "Repeat the saved path and the read-back fixture", "Turn 2 names the same file"). `replies/SID-001-turn2.txt` names no file: a grep for `export/`, `task-payout` or `.md` returns 0 matches. It repeats the fixture ("The exact string I printed was `Verified: read-back succeeded; 65 lines`") and states the content was non-empty, so two of the three Turn 2 expectations hold
- The artifact carries requirements never supplied. The prompt asks for a 24-hour pause, a required reason and checklist items for the toggle, the reason field and the banner. The reply itself says "Some checklist items go beyond your brief, so please confirm or strike them" and lists early-off, return to pending, non-pending unavailability and whitespace. Two further additions are not disclosed: export line 46 "An empty reason shows an error message on the field" and line 48 "Cancelling before confirming leaves the payout unpaused and discards the reason". Early-off at lines 31 and 64 is a new capability. Severity: blocking (root line 156)
- `N`: printed 65, Read's final line 66, real 65. Turn 2 volunteers the same finding: "Read's last row was numbered 66 (blank), so `N` should have been 66." Recorded, not graded
- Second read: reopened the scenario file at lines 30, 32, 40, 63, 78 and 79 to confirm the path clause appears three times and that line 32 ("Turn 2 asks for the delivery string by name, so it cannot supply the proof") excuses the proof, not the path. Re-read the Turn 1 prompt word by word for early-off, whitespace, error message and cancel behavior and found none. The verdict stands on two independent grounds, and the undisclosed cancel item means it does not rest on the open disclosure conflict alone

### STK-001, task command flow: FAIL

- Turn 1 passes: one consolidated question saved to `export/001 - task-creator-payout-pause-clarification.md`, read back in full, path first, `Verified: read-back succeeded; 33 lines`, HVR line, no task draft. The question covers format and scope, requirements, success, dependencies and validation, and opens with a Quick or Deeper choice the direct `$task` row does not ask for but does not forbid
- Turn 2 carries every supplied fact: standalone task, `### About`, `### Requirements`, a `- [ ]` checklist with the required reason (export line 33), the indicator in the payout row (line 45) and the pause in payout history (line 57)
- Invented value and scope: export lines 17 to 19 put a page reference `Creator payouts` in the artifact, and line 11 adds "Who is allowed to pause a payout and how a pause ends are not part of it." The reply discloses both: "The `Creator payouts` page name is a placeholder because you gave no Figma link or page name" and "You didn't say that, so remove it if those belong here." Borderline, not decisive: line 58 has history showing the stored reason, which reads the "reason must be stored" and "verify the pause in the payout history" facts together
- Second read: re-read the Turn 2 prompt for any page, screen name or scope exclusion and found none. This verdict rests only on disclosed additions, so it would flip if the operator settles the disclosure conflict in favor of disclosure (README section 6, finding 4)

### SBG-001, bug report flow: PASS

- Turn 1: `export/001 - bug-payout-pause-toggle-clarification.md` holds eight evidence questions and nothing else (steps, environment, frequency, expected behavior, evidence). Reply opens with its path, `Verified: read-back succeeded; 13 lines`, and the HVR line. No draft
- Turn 2: `export/002 - bug-payout-pause-toggle-reverts-to-off.md`. Field table: Frequency `Always`, Severity, Device and OS Version `Not provided`, Platform `Web`, Browser `Chrome`, Browser Version `126` (export lines 11 to 17). `**1. Observed Behavior**` at line 30, four numbered steps at lines 40 to 43, `**2. Expected Behavior**` at line 51, the four fixed checklist items unchanged at lines 60 to 63. No device, OS or cause invented. The runtime corrected its own first draft: an Edit replaced "No error message was reported" with "Error messages: Not provided", and a Read of lines 28 to 37 followed that Edit
- Format gate on both exports: exit 0

### SDK-001, doc guide delivery: FAIL

- Turn 1 passes: the clarification asks for the notes together with source set, authority, status, shape and scope (export lines 5 to 9), exported and read back in full, reply carries path, read-back line and HVR line
- Turn 2 guide passes on content and layout: `* * *` directly under every content heading, `*   ` bullets, sentence-case headings, no spacer heading, 30 second backoff, five attempts, attempt six to the failed queue, Requeue restarting the backoff, and the five-line Doc summary (Source safety, Shape fit, ClickUp layout, Readability, Voice). Format gate exit 0
- Verification fails. The only Read after the Write in `skill/SDK-001 - doc-guide-delivery/events-turn-2.jsonl` used offset 50 on a 47-line file and returned only `Warning: the file exists but is shorter than the provided offset (50). The file has 48 lines.` No further Read followed. The reply printed `Verified: read-back succeeded; 48 lines`. `AGENTS.md` line 46 passes verification only when Read returns non-empty content at the path, and says a Write result is not verification and a failed read-back is retried once. Turn 2's "read it back" (scenario line 41) did not happen
- Advisory: the Turn 1 clarification file line 8 ends a bullet with a full stop (format gate exit 1) while the Turn 1 self-scan reports 0 hard blockers. `references/hvr-core.md` line 35 counts that as a punctuation hard blocker
- Second read: re-traced the Turn 2 stream end to end. One Write, one Read, the warning text above, then the final reply. The file on disk is readable and correct, so the verdict rests only on the verification claim, which is the skill's own delivery proof

### SDK-002, doc conflict gate: FAIL

- Turn 1 made no tool call at all: the trace shows no `tool_use` event in `events-turn-1.jsonl`, and `meta.json` records an empty Turn 1 ledger. The reply lists both notes and asks one consolidated question with no draft, but saves no clarification, prints no path, no read-back line and no `HVR self-scan:` line. Expected signals (line 31) and root line 131 require all of them. A missing self-scan line is blocking (root line 159)
- Turn 2 is sound: `export/001 - doc-payout-pause-behavior.md` keeps Note A current (line 22 "Current behavior, per Note A") and Note B retired (lines 26 to 31), with no blended claim. Format gate exit 0. Read back in full, then an Edit, then lines 14 to 23. Because no clarification existed, the doc took `001` rather than the next number after a clarification (root Export names, line 140)
- Second read: confirmed `skill/SDK-002 - doc-conflict-gate/exports/export/` holds one file. Turn 1 never opened `sk-product-owner/SKILL.md`, which `AGENTS.md` line 144 says to read before any request. `AGENTS.md` itself never says a clarification is exported (its only "clarification" is line 188), so a run that skips `SKILL.md` never sees the rule at `SKILL.md` line 208

### SST-001, story shape hard values: FAIL

- Turn 1 passes: one question covering notes, operation, role and value, Story or Epic, requirements, evidence and delivery, saved as `export/001 - PRD-payout-pause-clarification.md` and read back. The reply opens with two sentences before the path (advisory on the skill side, root line 164)
- Turn 2 passes on shape: `Kind: Story`, story preamble, `## About`, `### Problem`, `### Solution`, `#### **Expected outcomes**`, `## Requirements` with `` `24 hours` `` (line 31) and `` `Pause payout` `` (line 39) backticked, numbered criteria with Mark-as-done lines, no value in any criterion, no ticket fields. Only `story-template.md` opened on the Story lane, never `epic-template.md`. Format gate exit 0
- Invented behavior in a criterion: export line 64 `*   **And** the brand is told a reason is needed, and anything already entered is kept`. The Turn 2 prompt supplies neither a message nor input retention, and the reply's own list of additions does not name this clause
- Second read: re-read the Turn 2 prompt and the reply's disclosure list. "The refusal when the reason is empty" is disclosed and is a direct negation of "reason is required", so it was not counted. The retained-input clause is neither supplied nor disclosed, so the verdict does not rest on the disclosure conflict

### SIR-001, ambiguous intake energy choice: FAIL

- Turn 1 passes: `export/001 - intake-creator-payout-flow-clarification.md` opens its question with `**0. How should I work this?**` Quick or Deeper (lines 3 to 6), then shape, scope, evidence, constraints and assumptions. Read back, path, read-back line, HVR line, no artifact
- Turn 2 keeps Quick ("Quality summary (Quick energy, Task shape)") and Task, and carries the reason and pause date on the payout detail screen (export lines 21 and 22)
- Invented behavior: export line 24 `- [ ] A paused payout with no recorded reason or date never shows a blank field`. The reply discloses it: "I added only two things: the not-paused case and the missing-data case."
- Second read: the Turn 2 prompt names no missing-data case. This verdict rests only on a disclosed addition, the exact open conflict, so it would flip if that conflict is settled in favor of disclosure

---

## 3. Project scenarios

Block form per turn, recorded as root line 136 asks:

| Scenario, turn | Form | Before any commentary |
| --- | --- | --- |
| PID-001 T1 | Fenced, under the label line `Deliverable Block (Canvas Artifact):` | Yes |
| PTK-001 T1 | Fenced | No, three sentences precede it |
| PTK-001 T2 | Fenced, first line of the reply | Yes |
| PBG-001 T1 | Fenced | No, two sentences precede it |
| PBG-001 T2 | Fenced, first line of the reply | Yes |
| PDK-001 T1 | `# Deliverable Block` heading, then fenced | Yes |
| PDK-001 T2 | `# Deliverable Block` heading, then fenced | Yes |
| PDK-002 T1 | Fenced | No, two sentences precede it |
| PDK-002 T2 | Fenced, first line of the reply | Yes |
| PST-001 T1 | Fenced, under `**Deliverable Block: clarification**` | No, two sentences precede the label |
| PST-001 T2 | Fenced, under `**Deliverable Block: Story**` | Yes |
| PIR-001 T1 | Fenced | No, two sentences precede it |
| PIR-001 T2 | Fenced, first line of the reply | Yes |

Every block closes before its `Export-equivalent path:` line. No Project reply prints `Path:`, `Saved:`, `Verified:` or `read-back succeeded` (grep of `replies/P*.txt` returns nothing). Every Project ledger in `meta.json` is empty, and the Project tool list was read-only, so no file could be written.

### PID-001, Project identity handover: FAIL

- Identity proof holds on Turn 1: the task block renders first, then `Export-equivalent path: \`export/NNN - task-payout-pause-toggle.md\``, then `HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: none.` Turn 2 keeps the boundary: "No, I didn't write any file to disk" and "The path is a label". Turn 1 never states that no file was written in so many words. The Turn 1 chain row (line 39) asks only that "no file path is claimed", which holds. The phrase "claims no local file was written" at lines 32 and 76 reads two ways and is logged (README section 6)
- The artifact carries requirements never supplied. Disclosed: "Reason visibility: I made the reason visible to the brand only" (reply line 49). Not disclosed: reply line 46 "shows an inline error", line 47 "Submitting with only whitespace is treated as empty", line 50 "Cancelling before submitting leaves the payout unpaused and clears the field", line 64 "The banner states when the pause ends". Borderline: lines 26, 30, 31, 32 and 67. Severity: blocking (root line 156)
- Second read: re-read the Turn 1 prompt. None of the undisclosed items is in it, so the verdict does not rest on the disclosure conflict. Re-checked the label line: `Deliverable Block (Canvas Artifact):` names the block and says nothing about the request, so it was not treated as commentary

### PTK-001, task command flow: FAIL

- Turn 1: `replies/PTK-001-turn1.txt` line 1 "Task Mode needs scope, requirements and acceptance criteria before I draft. Your request names only the feature, so I'm asking one question first. The question is in the block below." The block follows. Root line 132 requires the question "rendered as its own block before any commentary"
- Turn 2 renders first and keeps every supplied fact, but adds unsupplied items. Not disclosed: line 47 "Keep every other element of the payout row unchanged, including amount, date and status" and line 62 "Include the date and time the pause was recorded in the history entry". Disclosed: whitespace rejection, validation message, accessible label ("my additions from edge-case checks")
- Second read: re-read line 1 against root line 136. It explains the runtime's reasoning, which is commentary, not a block label

### PBG-001, bug report flow: FAIL

- Turn 1: line 1 "Here is the clarification block. I'm asking before drafting because the request has no reproduction steps, environment or evidence." The block follows. Same rule as PTK-001. Advisory: the block's bullet "What should I not assume about the cause? ... or never saved." ends with a full stop (format gate exit 1 on the extracted block), while the self-scan reports 0 hard blockers
- Turn 2 is clean: block first, `Always (every attempt, per reporter)`, `Web`, `Chrome`, `126`, Device, OS and Severity `Not provided`, the four numbered steps, the four fixed checklist items, `Export-equivalent path:` with the `bug` word, HVR line. Borderline only: line 43 "No error message was reported", literally true of the report. Format gate exit 0
- Second read: this and `PST-001` are the two Project scenarios that fail on Turn 1 ordering alone, see README finding 8 for the conflict with root lines 162 to 164. Confirmed line 1 of the reply is prose, and that `claude project/Custom Instructions.md` line 85 and `Product Owner - System - Interactive Mode - v0.404.md` lines 62 and 74 apply the render-first rule to a clarification block

### PDK-001, doc guide delivery: PASS

- Turn 1: `# Deliverable Block` then the question. It asks for the notes in the same message ("You can paste the engineering notes in the same message") together with source set, authority and conflicts, document status, shape and scope, plus audience and validation. `Export-equivalent path: \`export/001 - doc-notification-retry-pipeline-clarification.md\``, HVR line, no draft
- Turn 2: guide under `# Deliverable Block` with a line-1 HTML comment, `* * *` directly under every content heading, `*   ` bullets and `*   [ ]` checks, sentence case, 30 second backoff, five attempts, attempt six, failed queue, Requeue, restarted backoff, unknowns marked unverified. Five-line Doc summary. `Export-equivalent path: \`export/002 - doc-notification-retry-requeue-guide.md\``. Format gate exit 0
- Checked for a file claim: the summary says "no spacer headings because this is a file export". That classifies the deliverable for the spacer rule and claims no save, so it was not counted. It is evidence for the recorded spacer-heading conflict (README section 6)

### PDK-002, doc conflict gate: FAIL

- Turn 1: line 1 "Two notes give different release rules for the same behavior, and neither has authority over the other. Recency and note order can't settle it, so I've stopped before drafting and put the question in the block below." The block lists both notes and asks one consolidated question. Commentary first fails root line 132
- Turn 2: Note A current in the status label, Note B under "Retired behavior", no blended claim, five-line Doc summary, HVR line. Second defect: a blank line sits between every content heading and its `* * *` (reply lines 11 to 13, 19 to 21, 23 to 25 and more). `Product Owner - Templates - Doc Mode - v0.109.md` line 74 says "the divider sits immediately under its heading with nothing between them". The format gate passes it, because `validate-output-format.cjs` line 585 looks for the next non-blank line
- Second read: confirmed the skill twin's reference and the three other Doc blocks put the divider on the line directly under each heading, so the blank line is specific to this reply

### PST-001, story shape hard values: FAIL

- Turn 1: line 1 "The message has no notes in it, and the working directory has none either. I can't draft a PRD from a feature name alone without inventing requirements, so I'm asking one question first." Then `**Deliverable Block: clarification**` and the block. Commentary first fails root line 132
- Turn 2 is otherwise sound: `Artifact kind: Story.`, `` `24 hours` `` and `` `Pause payout` `` backticked in Requirements, no value in a criterion, only `Product Owner - Assets - Story Template - v0.100.md` opened (never the Epic template), no ticket fields, format gate exit 0. Borderline only: criterion 2 "And the brand can see the reason is needed". Advisory: the About section has no `* * *` and `##   ` spacer before `## Requirements`, which the scenario's step 4 list does not grade
- Second read: confirmed the two sentences come before the label line, so even reading the label as the block's heading, commentary precedes it

### PIR-001, ambiguous intake energy choice: FAIL

- Turn 1: line 1 "Your request could be a task, a bug, a PRD or a doc, so I need one round of answers before I draft. The question is in the block below." The block opens with `**0. How should I work this?**` Quick or Deeper, as required. Commentary first fails root line 132
- Turn 2 keeps Quick and Task and carries the reason and date. Invented, not disclosed: line 10 "They wait, then contact support to ask." (a claim about current behavior), line 27 "The date uses the same date format as the other dates", line 30 "not an earlier one", line 31 "Keep the rest of the payout detail screen ... unchanged". Disclosed: the missing-reason item
- Second read: the Turn 2 prompt says only "Creators need to see why a payout was paused, including the reason and the pause date, on the payout detail screen." The support-contact sentence has no source

---

## 4. Twin adjudications

Each class was checked in the rule files on both sides.

**BG-001, skill PASS, Project FAIL. Runtime fault (Project).** Both runtimes carry a deliver-first rule. Skill: `AGENTS.md` line 89 "Start with the saved file path", and `replies/SBG-001-turn1.txt` line 1 is `Path:`. Project: `claude project/Custom Instructions.md` line 85 "Render the Deliverable Block before any commentary", and `Product Owner - System - Interactive Mode - v0.404.md` lines 62 and 74 make a clarification a block delivered like any other. PBG-001 Turn 1 read that knowledge file (the trace shows a full Read of the 544-line file) and still opened with prose.

**DK-001, skill FAIL, Project PASS. Runtime fault (skill).** The delivery-evidence rules differ by design. The skill must read back (`AGENTS.md` line 46, `sk-product-owner/SKILL.md` line 211) and the Project treats the rendered block as the evidence (`Custom Instructions.md` line 234). The skill failed its own rule, so the difference is not a rule gap. Everything the two runtimes share (the five-field question, ClickUp layout, source fidelity, Doc summary) passed on both.

**DK-002, both FAIL for different reasons.** Skill: runtime fault. Turn 1 never read `SKILL.md` although `AGENTS.md` line 144 requires it, so it missed `SKILL.md` line 208 (export the clarification) and line 217 (self-scan on every delivery). Contributing parity gap: the always-loaded Project kernel states the clarification export at `Custom Instructions.md` line 227, while the always-loaded `AGENTS.md` has no such line. Project: runtime fault against `Custom Instructions.md` line 85 on Turn 1, and against `Product Owner - Templates - Doc Mode - v0.109.md` line 74 on Turn 2, whose skill counterpart `sk-product-owner/references/doc-mode.md` line 98 the skill twin followed.

**ID-001, both FAIL, partly different reasons.** Shared: both artifacts add unsupplied requirements. Both runtimes carry the tension: skill `SKILL.md` line 283 (NEVER 4) against line 267 (ALWAYS 8, edge and error states) and line 201 (assumptions go in the reply so the user can correct one). Project `Custom Instructions.md` line 198 (assumptions in the reply) and `Product Owner - Templates - Task Mode - v0.305.md` line 330 (edge cases), while "never invent requirements" sits only in `Product Owner - Templates - Doc Mode - v0.109.md` line 553, which a Task run does not open. That is a parity gap, but both runtimes invented, so it does not explain a difference here. Skill only: Turn 2 did not repeat the path. Rule gap: the twins' Turn 2 prompts and expectations differ by design (`skill-identity/identity-handover.md` line 40 against `project-identity/identity-handover.md` line 40), and no skill rule asks a follow-up answer to restate the path (`AGENTS.md` lines 87 to 92 govern the delivery response).

**IR-001, both FAIL for different reasons.** Shared: both tasks add a disclosed missing-data item. Project only: commentary before the Turn 1 block and an undisclosed support-contact claim. Runtime fault, `Custom Instructions.md` line 85. The skill counterpart for the energy-first question, `sk-product-owner/references/interactive-mode.md` line 102, matches `Product Owner - System - Interactive Mode - v0.404.md` line 79, and both runtimes opened with the energy choice.

**ST-001, both FAIL for different reasons.** Skill: runtime fault against `SKILL.md` line 283, an undisclosed criterion clause. Project: runtime fault against `Custom Instructions.md` line 85 on Turn 1. The Project's Story lane carries "Never invent requirements" at `Product Owner - Templates - Story Mode - v0.400.md` line 59, and its Turn 2 added nothing decisive.

**TK-001, both FAIL for different reasons.** Shared: both tasks add unsupplied items (disclosed on the skill side, disclosed and undisclosed on the Project side). Project only: commentary before the Turn 1 block. Runtime fault, `Custom Instructions.md` line 85. The skill's Turn 1 reply opens with `Path:` per `AGENTS.md` line 89.

---

## 5. Things checked and not counted

- Oxford commas and bold emphasis appear throughout, and `references/hvr-core.md` line 35 bans both. The linter leaves them out by design (`benchmark/grader/README.md` section 3) and no scenario grades them, so they were not graded
- Skill replies that print the clarification question in chat (SDK-001 Turn 1 prints all six questions) were not graded either way, per root line 131
- Skill Turn 1 replies that open with prose before `Path:` (SST-001, SDK-002) are advisory on the skill side, root line 164. SDK-002 fails for other reasons
- SST-001 Turn 1 opened `story-mode.md` but not `SKILL.md` or `conciseness.md`, which `AGENTS.md` lines 144 and 148 to 151 require. No scenario grades loading beyond the one-scaffold rule, so it is recorded only

---

## 6. What `check_report.sh` found

Command, from `AI Systems/Product Owner/`: `bash benchmark/grader/check_report.sh "benchmark/reports/2026-09-25--manual-testing-playbook--claude-sonnet-5-medium"`. Exit code 2: both checks reported findings. It wrote `hvr-lint.csv` in this folder.

**`twin_divergence`**: `BG-001: skill PASS, Project FAIL`, `DK-001: skill FAIL, Project PASS`, 5 agreed, 2 disagreed, 0 not settled, 0 unpaired. This matches the twin table in `results.md` and the adjudications in section 4.

**`lint_replies`**: 12 of 28 replies clean, 16 dirty. Fifteen dirty replies carry `bullet_ends_with_full_stop` only and one carries `semicolon` only. No em dash, curly quote or blocker word was flagged, unlike the 2026-09-17 run where em dashes dominated. Where the hits sit:

- Almost every full-stop bullet sits in chat prose around the deliverable (assumption lists, quality summaries). One sits inside a delivered block: the PBG-001 Turn 1 clarification. The skill-side exports are not in `replies/`, and the format gate found one more inside a delivered file: SDK-001's Turn 1 clarification, line 8. Both of those replies report `HVR self-scan: 0 hard blockers`, so each count missed one punctuation hard blocker (`references/hvr-core.md` lines 35 and 132). Both scenarios fail on other grounds, so no verdict depends on it
- The one semicolon is `replies/SID-001-turn2.txt` line 5, inside the quoted fixture `` `Verified: read-back succeeded; 65 lines` ``, which the rules require verbatim. The linter strips that fixture only when it starts a line (`hvr_lint.py` `META_LINE`), so a quoted fixture in prose reads as a violation. A linter false positive, not a runtime defect
- Every delivered artifact passed the shared format gate apart from the two clarifications named above
