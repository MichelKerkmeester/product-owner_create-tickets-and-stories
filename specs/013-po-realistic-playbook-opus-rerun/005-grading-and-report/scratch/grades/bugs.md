# Grades draft: bugs batch

Batch `bugs`: SBG-001, PBG-001, SBG-002, PBG-002, SBG-003, PBG-003. Model `claude-opus-5-5-medium`. Run folder `<RUN>` = `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/`.

Sources: `git -C "AI Systems/Product Owner" status --porcelain -- sk-product-owner "claude project" AGENTS.md benchmark/fixtures` printed nothing and HEAD is `3023c5e`, so every source line below is cited from the working tree at `3023c5e`.

Format gate: `node validate-output-format.cjs --system product-owner <file>` run from the Sync Loop folder on all four skill exports and all five Project block copies under `scratch/grades/blocks/bugs/`. Every run printed `Product Owner output format validation passed across 1 artifact file(s)` with exit 0.

Event numbers below are the 0-based line index of the event in `events-turn-<n>.jsonl`.

---

## SBG-001 (skill), Quick bug

### Draft row

```csv
SBG-001,skill,claude-opus-5-5-medium,PASS,1,1,pending,yes,"Turn 1 asked nothing and saved export/001 - bug-ios-cart-badge-stale-after-remove.md, read back at lines 1 to 75, with Always, Medium, iOS and Not provided cells, the ""3"" badge over 2 units and Expected ""2"" by the unit rule (export lines 11 to 15, 32, 55). Borderline only: the unsourced ""No error message is shown"" (line 33) and a title code FE the reply names as a guess."
```

### Pass clauses

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

### Blocking items hit

None.

### Advisory items

- Size band: 74 lines against 35 to 70, over by 4. The BDD section (lines 67 to 74) is a named addition (`turn-1.md` line 15)
- Borderline, never decides alone: line 33 "No error message is shown" is a claim about current behavior that neither the prompt nor `fernhouse-context.md` contains, and no naming line in `turn-1.md` covers it. The house examples model the same line (`assets/examples/bug/bug-example-frontend-visual.md` line 46) and the checklist asks that error messages be "included or marked as not provided" (`references/bug-mode.md` line 217)
- Borderline, never decides alone: title code `FE`. The reply names it at `turn-1.md` line 12 as "a guess, not a known root cause", and `fernhouse-context.md` line 82 requires one code on every bug
- Named additions, covered: the unit rule source (line 13), the iOS add-updates expectation at export line 57 (line 14, also `fernhouse-context.md` line 140), the BDD scenario (line 15)
- Title carries a discipline code, so the no-code advisory is not hit

### Read-back table

| Turn | Export path | `N` printed | Read after the last Write or Edit, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - bug-ios-cart-badge-stale-after-remove.md` | 75 | Read at event 38 after the only Write at event 32, lines 1 to 75 (line 75 empty) | 74 |

### Realism entry

- `export/001 - bug-ios-cart-badge-stale-after-remove.md`, kind Bug
- Routed template (`assets/bug-report-template.md` lines 63 to 151, order at `references/bug-mode.md` lines 127 to 135): H1, `### About`, field table, References, `### Bug`, Observed, `Steps to Reproduce:`, screen recording, Expected, Checklist all present. Optional BDD present
- Company facts against `benchmark/fixtures/companies/fernhouse/fernhouse-context.md`: iOS `4.8.0` (line 116), Android `4.8.2` (line 117), badge counts units not lines (line 22), `CART` covers the cart badge (line 101), title pattern `{Discipline} - {Surface} - {Feature code} - {Title}` (line 93), `FE` is client work (line 86). All match
- Placeholder: none
- Body 74 lines against 35 to 70 (advisory, over)
- Discipline code: `FE` present

### Open readings

- `N`: the reply printed 75, the Read's final displayed line is 75 (an empty line after the trailing newline) and `wc -l` is 74. `AGENTS.md` line 45 says to use the final line number Read returns. Is `N` graded against that Read line or against `wc -l`?
- Does an unsourced "No error message is shown" line count as an invented behavior claim, given that both packagings' examples model it, or as a filled template slot?

---

## PBG-001 (project), Quick bug

### Draft row

```csv
PBG-001,project,claude-opus-5-5-medium,PASS,1,1,pending,yes,"Turn 1 asked nothing and rendered one fenced bug block, then Export-equivalent path export/NNN - bug-ios-cart-badge-stale-after-remove.md and the HVR line with no file claim, keeping every value and the unit rule (turn-1.md lines 12 to 16, 33, 59, 70, 72). Advisory: the block lowercases the fixed labels Steps to reproduce, OS version and Browser version."
```

### Pass clauses

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

### Blocking items hit

None.

### Advisory items

- Fixed labels changed case: block line 38 "Steps to reproduce:", line 16 "OS version", line 18 "Browser version" against the Project template's "Steps to Reproduce:" (line 88), "OS Version" (line 58) and "Browser Version" (line 60). The HVR line 72 names this as a fix. Each section is present, so no required section is missing
- Design spec reads "Not provided" (line 57) although `fernhouse-context.md` line 22 states the unit rule. The rule is applied at line 59, so the fact is not ignored
- Named addition, covered: "Customer type (guest or signed in) and market used in testing: Not provided" (line 48), named at reply line 84
- Commentary follows the block, so no ordering defect
- Delivery form: fenced block
- Title carries `FE`, built from the context convention (reply line 76)

### Realism entry

- Block `turn-1.md` lines 2 to 67, copy `scratch/grades/blocks/bugs/PBG-001-turn1-bug.md`, kind Bug
- Routed template (`claude project/knowledge/Product Owner - Assets - Bug Report Template - v0.100.md` lines 43 to 131, order at `Product Owner - Templates - Bug Mode - v0.203.md` lines 110 to 118): every required section present, BDD not used
- Company facts against `fernhouse-context.md`: iOS `4.8.0` (line 116), Android `4.8.2` (line 117), units not lines (line 22), `CART` (line 101), signed-in carts follow the customer across surfaces (line 140, used for the named addition). All match
- Placeholder: none. `NNN` in the label is the exempt Project slot
- Body 66 lines, inside 35 to 70
- Discipline code: `FE` present

### Open readings

- Does a changed letter case on a fixed template label (`Steps to Reproduce:`, `OS Version`, `Browser Version`) count against "every required template section", or only a missing section?

---

## SBG-002 (skill), Support ticket bug

### Draft row

```csv
SBG-002,skill,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 asked no question and saved the whole bug as export/001 - bug-android-confirmation-total-missing-city-tax.md (turn-1.md lines 1 to 4, Write at event 56), and Turn 2 edited that file in place instead of saving on the next number. The final bug keeps every ticket amount, the correct charge and the Android 8.12.1 Pay now scope."
```

### Pass clauses

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

### Blocking items hit

- Four Pass clauses unmet, root line 150. An explicit `$bug` asks its mode's question and waits (`AGENTS.md` line 287)
- Side-effect ledger: Turn 1 created a bug where a clarification turn may create only the `-clarification` export (root line 106), so the ledger holds a disallowed change (root line 144)

### Advisory items

- Size band: 113 lines against 60 to 110, over by 3
- Borderline, never decides alone: line 46 "No error message is shown. The screen looks like a normal confirmation with a lower total" appears in neither the turns nor the ticket and is not named
- Borderline, never decides alone: line 52 "checked on 2026-09-25" turns Turn 2's "this morning" into the run date, a value no turn or attachment gives
- Borderline, never decides alone: line 54 "so the number of affected guests can grow from here" projects from ticket line 66 "the Android rollout only reached everyone today"
- Title code `FE` named at `turn-1.md` line 12 with "The cause hasn't been found"
- Turn 1 set Severity from the ticket priority and named it (`turn-1.md` line 14). Turn 2 confirmed High
- Turn 1 read-back proof: the Read at event 65 (lines 1 to 110) came before the last Edit at event 71. After that Edit only a Bash `wc -l` (printed 109) and `sed -n '41p;110p'` ran, no Read. Recorded only, since the verdict already fails

### Read-back table

| Turn | Export path | `N` printed | Read after the last Write or Edit, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - bug-android-confirmation-total-missing-city-tax.md` | 110 | None. Read at event 65 returned lines 1 to 110, then Edit at event 71, then Bash `wc -l` printed 109 | 109 at the end of Turn 1 (Bash output) |
| 2 | same path, modified | 114 | Read at event 27 after the last Edit at event 25, lines 1 to 114 (line 114 empty) | 113 |

### Realism entry

- `export/001 - bug-android-confirmation-total-missing-city-tax.md` (final state after Turn 2), kind Bug
- Routed template (`assets/bug-report-template.md`): every required section present, optional BDD present with two scenarios (named)
- Company facts against `roamstay-context.md`: Android `8.12.1` (line 107), iOS `8.12.0` (line 106), `BOOK` covers the confirmation screen (line 93), `Guest app` as the title surface (line 83), city tax part of the total (line 44), Pay now charges the full total (line 148), staged Android rollout (line 112). Ticket values against `roamstay-support-ticket-58213.md` lines 8, 12 to 16, 42 to 58. All match
- Placeholder: none
- Body 113 lines against 60 to 110 (advisory, over)
- Discipline code: `FE` present

### Open readings

- Does a Bash `wc -l` or `sed` after the last Edit count as read-back, or only a Read tool call? Verdict unaffected here
- Is resolving "this morning" to the runtime's own date (2026-09-25) an invented value or a direct reading?
- `N` as in SBG-001: Turn 2 printed 114, the Read's final line, while `wc -l` is 113

---

## PBG-002 (project), Support ticket bug

### Draft row

```csv
PBG-002,project,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 rendered the whole bug block (turn-1.md lines 1 to 92) under a plain bug label with no -clarification suffix instead of one question-only block, so the ask-first clauses are unmet. The Turn 2 block keeps every amount, the correct charge and the Android 8.12.1 Pay now scope, with no file claim."
```

### Pass clauses

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

### Blocking items hit

- Three Pass clauses unmet, root line 150. The Project packaging says an explicit `$bug` asks and waits (`Custom Instructions.md` line 108)

### Advisory items

- Borderline, never decides alone: `turn-2.md` line 46 "on 2026-09-25" turns "this morning" into the run date
- Turn 2's "nobody on Booking has looked at the code yet" is in the chat (line 113) but not in the block. The block states no cause and keeps "Root cause identified" open, so nothing is altered
- Title code `FE` named as an assumption (`turn-1.md` line 103, `turn-2.md` line 114)
- Device and OS cells write "not known" rather than `Not provided` for the guest's phone (lines 15 and 16), wording only
- Turn 1 set Severity from the ticket priority and named it (`turn-1.md` line 105)
- Commentary follows each block. Delivery form: fenced block on both turns

### Realism entries

- Block `turn-1.md` lines 2 to 91, copy `scratch/grades/blocks/bugs/PBG-002-turn1-bug.md`, kind Bug (delivered early). Every required section present per the Project template, BDD present and named. Facts: Android `8.12.1` (`roamstay-context.md` line 107), iOS `8.12.0` (line 106), `BOOK` (line 93), rollout date (ticket line 66). 90 lines inside 60 to 110. Code `FE`. Placeholder none
- Block `turn-2.md` lines 2 to 95, copy `scratch/grades/blocks/bugs/PBG-002-turn2-bug.md`, kind Bug. Every required section present (`Product Owner - Assets - Bug Report Template - v0.100.md` lines 43 to 131). Facts: `Guest app` surface (`roamstay-context.md` line 83), city tax in the total (line 44), Pay now charges the full total (line 148), ticket values (`roamstay-support-ticket-58213.md` lines 12 to 16, 42 to 58). All match. 94 lines inside 60 to 110. Code `FE`. Placeholder none

### Open readings

- Same "this morning" date question as SBG-002

---

## SBG-003 (skill), Two-platform log bug

### Draft row

```csv
SBG-003,skill,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 saved the question-only export/001 - bug-reminders-late-after-clock-change-clarification.md and drafted nothing, and Turn 2 saved export/002 with Group A and Group B apart, the log verbatim (lines 78 to 88), Severity High and Frequency Not provided. The Group A cause at line 93 is labelled an unverified hypothesis and disclaims Group B, so root line 187 does not count it as invented (see Open readings)."
```

### Pass clauses

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

### Blocking items hit

None.

### Advisory items

- Asking for a fact the turn states: the clarification asks "one bug or two" (lines 5 to 14) though Turn 1 said "write it up as one bug" (root line 211 reading, recorded only)
- Borderline, never decides alone: line 57 "No error message is shown in either group" is in no attachment or turn and is not named
- Borderline, never decides alone: line 54 "Members changed nothing." widens LL-20944's "I did not touch anything" (user reports line 31) to the group
- Borderline, never decides alone: title code `FS - REM` chosen by the runtime after Turn 2 left the code open, named at `turn-2.md` line 13. `FS` means front end and back end changes together (`loomlist-context.md` line 100), which leans on where the fix sits
- Named omission: Marta's known-issue and macro request left out (`turn-2.md` line 17)
- Size: 113 lines inside 80 to 150

### Read-back table

| Turn | Export path | `N` printed | Read after the last Write or Edit, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - bug-reminders-late-after-clock-change-clarification.md` | 19 | Read at event 52 after the Write at event 50, lines 1 to 19 (line 19 empty) | 18 |
| 2 | `export/002 - bug-reminders-late-after-clock-change.md` | 113 | Read at event 37 with offset 100 after the Write at event 28, lines 100 to 114 (line 114 empty). A Bash `wc -l` at event 33 printed 113 | 113 |

### Realism entries

- `export/001 - bug-reminders-late-after-clock-change-clarification.md`, kind Clarification (bug lane). Question-only: no draft section, only the question with its framing. Facts: current versions Android `5.3.0` and iOS `5.3.2` (`loomlist-context.md` lines 132 and 133), title pattern and `REM` (lines 104 and 121), 117, 64 and 53 tickets (user reports lines 8 to 13), `tz_offset=+01:00` (log line 11). All match. 18 lines, no band. Placeholder none
- `export/002 - bug-reminders-late-after-clock-change.md`, kind Bug. Every required section present (`assets/bug-report-template.md`), no BDD. Facts: `REM` code (`loomlist-context.md` line 121), `FS` drops the platform segment for a parent spanning platforms (line 104), reminders use the owner's profile time zone (line 157), Web and Desktop show reminders in the app only (lines 77 and 178), versions 5.3.0 and 5.3.2 (lines 132 and 133). All match. Placeholder none. 113 lines inside 80 to 150. Code `FS`

### Open readings

- The Pass clause says "no root cause for either issue" and its Fail example is the offset-at-creation cause. Root line 187 says a root cause the artifact labels as an unverified hypothesis "is not an invented root cause". Graded Met under root line 187. Should a labelled hypothesis for one issue also satisfy this scenario's "no root cause", or does the scenario forbid even a labelled one?
- `N` for Turn 2 is 113, which matches `wc -l` but not the Read's final line 114 that `AGENTS.md` line 45 names. Turn 1 printed the Read's final line instead. Which count is right?
- Is a clarification that restates the evidence it asks about (lines 5 to 8) still "question-only"? Graded Met, same as PBG-003
- Same "No error message is shown" question as SBG-001

---

## PBG-003 (project), Two-platform log bug

### Draft row

```csv
PBG-003,project,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 rendered one fenced question block labelled export/001 - bug-reminders-late-after-march-clock-change-clarification.md and drafted nothing, and Turn 2 rendered one fenced bug block with the one-off and daily issues as separate observed and expected statements, the log verbatim (turn-2.md lines 73 to 83) and no cause. No file claim on either turn."
```

### Pass clauses

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

### Blocking items hit

None.

### Advisory items

- Asking for a fact the turn states: `turn-1.md` line 12 asks "one report, or one report per group" though Turn 1 asked for one bug (recorded only)
- Chat line 137 "Ruben's planned pull for the iOS tickets never arrived" says more than log excerpt line 32 ("Next I am pulling ...") and Turn 2 (silent on it). Chat only. The block says "There are no log lines for Group B yet" (line 50)
- BDD scenarios named as added (line 135)
- Commentary follows each block. Delivery form: fenced block on both turns

### Realism entries

- Block `turn-1.md` lines 2 to 25, copy `scratch/grades/blocks/bugs/PBG-003-turn1-clarification.md`, kind Clarification (bug lane). Question with an "Evidence so far" framing (lines 6 to 9), no draft section. Facts: Android `5.3.0` and iOS `5.3.2` (`loomlist-context.md` lines 132 and 133), `REM` and the title pattern (lines 104 and 121), `tz_offset=+01:00` and `scheduled_utc=2026-03-30T08:00:00Z` (log line 11), Ruben's planned iOS pull (log line 32). All match. 24 lines, no band. Placeholder none
- Block `turn-2.md` lines 2 to 121, copy `scratch/grades/blocks/bugs/PBG-003-turn2-bug.md`, kind Bug. Every required section present (`Product Owner - Assets - Bug Report Template - v0.100.md` lines 43 to 131), BDD present and named. Facts: owner's time zone (`loomlist-context.md` line 157), Web and Desktop in-app only (line 77), `FS` drops the platform segment (line 104), versions (lines 132 and 133), sample tickets and workspaces (user reports lines 23 to 39). All match. 120 lines inside 80 to 150. Code `FS`. Placeholder none

### Open readings

- Same question-only reading as SBG-003: the block restates evidence (lines 6 to 9) before asking

---

## Twin notes

**SBG-001 and PBG-001: agree (PASS, PASS).** Both skipped intake under `$quick`, kept every value and applied the unit rule. They differ only below the verdict. The skill wrote "No error message is shown" (export line 33) where the Project wrote "Error messages: Not provided" (block line 35), and both packagings carry the same rule (`references/bug-mode.md` line 217, Project `Templates - Bug Mode` line 200) and the same example line (`bug-example-frontend-visual.md` line 46, Project `Examples - Bug - Frontend Visual` line 45), so that is runtime choice. The Project lowercased three fixed labels under its HVR sentence-case pass while the skill kept them, with identical templates on both sides (`assets/bug-report-template.md` lines 78, 80, 108, Project template lines 58, 60, 88): a runtime difference, not a rule or parity gap.

**SBG-002 and PBG-002: agree (FAIL, FAIL).** Both drafted the full bug in Turn 1 from the complete ticket with no question. The two packagings say the same thing twice over: the explicit-command wait (`AGENTS.md` line 287, `Custom Instructions.md` line 108) and the bug-mode exception "Do not create an artifact until the user responds to the comprehensive question unless the request contains enough bug context to proceed" (`references/bug-mode.md` line 61, Project `Templates - Bug Mode` line 44). Both runtimes took the exception over the wait rule. No parity gap, since the texts match, and not a single-runtime fault, since both did it. The shared cause looks like the tension inside each packaging between the command-wait rule and the bug-mode exception. In SBG-003 and PBG-003 both runtimes did ask first, and both replies give the two-issue scope as the reason (`turn-1.md` lines 7 to 11 on the skill side, `turn-1.md` line 34 on the Project side), which fits the same reading: the runtimes ask when bug context looks thin or conflicting, not because `$bug` was typed.

**SBG-003 and PBG-003: agree (PASS, PASS).** Both asked one question first, delivered one bug with the two issues apart, the log verbatim, Severity High, Frequency `Not provided` and `FS - REM` named as a choice. They differ on one item: the skill added a Group A hypothesis labelled unverified that disclaims Group B (export line 93), the Project named no cause. Both packagings allow the labelled form and model it (`assets/examples/bug/bug-example-mobile-crash.md` line 68 and `bug-example-quick.md` line 53, Project `Examples - Bug - Mobile Crash` line 67 and `Quick Bug` line 52) under the same rule (`SKILL.md` line 283, `Custom Instructions.md` line 104). So the difference is runtime choice. The verdicts agree only under the root line 187 reading. If the operator reads this scenario's "no root cause" as barring a labelled hypothesis too, SBG-003 turns FAIL and the pair differs, with the cause a rule gap between the scenario text and root line 187, not a packaging gap.
