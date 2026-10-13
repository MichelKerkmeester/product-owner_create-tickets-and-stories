# Grades draft: docs batch

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

## SDK-001 (skill), Behavior reference

### Draft row

```csv
SDK-001,skill,claude-opus-5-5-medium,FAIL,2,2,pending,no,"Turn 1 asked no question and saved the full draft export/001 - doc-promotion-stacking.md (turn-1.md line 1 ""I've written the stacking reference as a behavior reference and saved it""; meta.json turn 1 ledger), so no doc-lane clarification exists and Turn 2 edited 001 in place. Turn 2 also misses two Pass clauses: the body is ## Stacking rules, not ## Behavior rules (export line 59), and one discount code per order never appears verbatim (line 71 ""one discount code at a time""); size 267 lines over the 80 to 180 band (advisory)."
```

### Pass clauses

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

### Blocking items hit

- Missed Pass clauses, root line 150: Turn 1 drafted instead of asking, which is the scenario's first Fail example ("Turn 1 drafts")
- Side-effect ledger, root line 106 and acceptance rule line 144: the clarification turn created a doc export where only the `-clarification` export is allowed, and Turn 2 modified that file instead of saving the next number
- Missed Pass clause, root line 150: `## Behavior rules` body absent (renamed `## Stacking rules`). The skill template makes the Overview and the primary body the only mandatory sections (`assets/doc-templates.md` line 115) and lets only optional headings be renamed (line 116)
- Protected fact, root line 188 and brief "every hard value the scenario lists as verbatim must appear verbatim": `one discount code per order` reworded

### Advisory items

- Size band: 267 lines against 80 to 180, over
- Quality summary: four lines with "Readability and voice" merged (`turn-2.md` lines 7 to 11), where `references/doc-mode.md` line 412 asks for one line each. Not a Pass clause
- Cross-reference slip: the precedence row "Gift card in the cart with a code" cites "Current behavior, rule 8" (line 179) while the doc numbers gift cards as rule 9 (line 155)
- Borderline, never decides alone: precedence row line 176 "Staff code on a sale item" with "no automatic promotion applies anywhere in the order" combines rules 3 and 4 (fixture lines 9 and 10) and no naming line covers it. It reads as the direct combination of two supplied rules
- Borderline: the banner wording note (lines 247 to 250) quotes `fernhouse-context.md` line 20 after the user made the context doc background only. It is named at `turn-2.md` line 25
- Both reads after the last write returned a partial range (see table)

### Read-back table

| Turn | Export path | `N` printed | Read after the last Write or Edit, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - doc-promotion-stacking.md` | 267 | Read at event 183 after the only Write at event 153, lines 255 to 267 of totalLines 267 (267 empty) | 266 at the end of Turn 1 (the Write content holds 266 newlines and nothing else wrote the file in Turn 1) |
| 2 | `export/001 - doc-promotion-stacking.md` | 268 | Read at event 72 after the last Edit at event 70, lines 256 to 268 of totalLines 268 (268 empty). The last full Read, event 62, came before the Edits at events 68 and 70 | 267 |

### Realism entry

- `export/001 - doc-promotion-stacking.md` (final Turn 2 state), kind Doc, Behavior reference
- Routed template, skill `assets/doc-templates.md` section 5 (lines 355 to 450): Overview present (line 10). Primary body `## Behavior rules` (template line 400) missing by name, its content sits under `## Stacking rules` (line 59). Optional sections present: Glossary (20), Structure or context as "Where the calculation runs" (32), Combinations and precedence (166), Examples (185), Boundaries as "Boundaries and history" (229), Related references (263)
- Company facts against `benchmark/fixtures/companies/fernhouse/fernhouse-promotions-rules.md`: staff codes `STAFF-`, exclusive, 30% off, sale items included (export lines 104 to 105, fixture line 10) match. Cap `50%` with the code's share cut (125 to 126, fixture 12) match. `0.01` and `half up` (136, fixture 15) match. `€50`/`£45` threshold and €4.95/£3.95 shipping (149 to 152, fixture 13) match. Retired on 2026-05-01 and code path removed 2026-05-04 (256 to 258, fixture 50 and 52) match. Worked example subtotal €137.33 (200, fixture 28) match. `one discount code per order` (fixture 7) reworded at lines 68 and 71
- Placeholder: none
- Body 267 lines against 80 to 180 (advisory, over)
- Discipline code: not applicable, Doc

### Open readings

- The rule text lets a runtime skip the question when the notes settle the reader: `references/doc-mode.md` line 67 asks only when purpose, audience, authority, scope or classification "cannot be established safely", and line 260 says that once the notes are present and make the reader's use clear "the routing above picks the shape without a preference question". `AGENTS.md` line 287 forces the question only for explicit commands. The rules note names its own readers (fixture line 3). Does a no-command Doc request with complete attachments still require the five-field question, as the scenario's section 1 asserts? Graded here by the Pass clause
- Does a renamed primary body (`## Stacking rules`) satisfy the Pass clause's `## Behavior rules`, given that `doc-templates.md` line 116 allows renaming only optional headings and only the Guide carries an explicit rename note (line 232)?
- Is `Automatic promotions first` with a sentence-initial capital verbatim for `automatic promotions first`?
- `N`: 267 and 268 follow the Read's final line (`AGENTS.md` line 45), `wc -l` gives 266 and 267. Which count is graded?

---

## PDK-001 (project), Behavior reference

### Draft row

```csv
PDK-001,project,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 asked no question and rendered the full behavior reference under Export-equivalent path export/001 - doc-promotions-stacking.md (turn-1.md lines 1 to 143), so the doc-lane clarification block the Pass clause needs never exists. Turn 2 meets every other clause (## Behavior rules at turn-2.md line 27, the rule values verbatim, retired label line 130, no file claim); advisory: the format gate flags the em dash after the Related references link (reply line 138)."
```

### Pass clauses

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

### Blocking items hit

- Missed Pass clauses, root line 150: Turn 1 drafted instead of asking, the scenario's first Fail example ("Turn 1 drafts")

### Advisory items

- Format gate on the block copies: turn 1 block lines 138 and 139 (reply lines 139 and 140) and turn 2 block line 137 (reply line 138), `prose em dash`, on the Related references link bullets. The Behavior reference scaffold's Related references line carries no delimiter (Project Doc Templates line 428). The HVR self-scan (`turn-2.md` line 143) says em dashes were kept only in the term bullets and the `Status:` labels. Not a Pass clause here
- `half up` appears verbatim only in the worked example (line 105); the rule line writes "half-up" (line 64)
- Block form: fenced both turns, no commentary before the block
- Five-line Doc summary present both turns (`turn-2.md` lines 145 to 150)
- Size: Turn 2 block 137 lines, inside 80 to 180

### Realism entries

- Turn 1 block (`turn-1.md` lines 2 to 140, copy `blocks/docs/PDK-001-turn1.md`), kind Behavior reference delivered at the clarification turn. Overview (11) and `## Behavior rules` (27) present. Company facts: banner copy `Free shipping on orders over €50` (line 127) against `fernhouse-context.md` line 20 matches, "set up by a merchandiser in Admin" (line 19) against context line 44 matches, `one discount code per order` (37) against rules line 7 matches. Placeholder none. 139 lines against 80 to 180
- Turn 2 block (`turn-2.md` lines 2 to 138, copy `blocks/docs/PDK-001-turn2.md`), kind Behavior reference. Routed template Project `Product Owner - Assets - Doc Templates - v0.107.md` lines 334 to 429: Overview (11) and `## Behavior rules` (27) present. Optional: Glossary (17), Combinations and precedence (76), Examples (92), Open questions (119), retired rule (128), Related references (136). Company facts against `fernhouse-promotions-rules.md`: line 37 one code plus the cart copy "Only one code per order. Your new code has replaced the old one." (fixture 7) match, line 52 `STAFF-` and 30% (fixture 10) match, line 60 the 50% cap (fixture 12) match, line 64 `0.01` (fixture 15) match, lines 130 to 134 2026-05-01 and 2026-05-04 (fixture 50 and 52) match, lines 100 to 103 €137.33 (fixture 25 to 28) match. Placeholder none. 137 lines against 80 to 180. Discipline code not applicable

### Open readings

- Same question as SDK-001 on the Project side: Doc Mode knowledge line 43 ("Ask one consolidated question only when ... cannot be established safely") and line 236 (shape picked "without a preference question" once the notes are present), against `Custom Instructions.md` line 130 ("Before any Doc draft, establish ... purpose, audience ..."). Does the Turn 1 question stay required?
- Is "half-up" in the rule line, with "half up" kept in the example, verbatim for `half up`?
- Is "because this is a file export" a file claim under root line 189? Graded here as no save claim

---

## SDK-002 (skill), Incident runbook

### Draft row

```csv
SDK-002,skill,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 saved the question-only export/001 - doc-payment-webhook-failures-clarification.md (read back lines 1 to 21) and Turn 2 saved export/002 - doc-payment-webhook-failures-runbook.md with the six steps in the notes' order, the pause before the fix (line 54), the resume once the payment_pending count is normal (line 86) and the dual-secret window as a proposal (lines 123, 126). Advisory: the Doc summary is one ""Check:"" line rather than five dimension lines (turn-2.md line 7); borderline INC-0412 generalizations at lines 48 and 74."
```

### Pass clauses

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

### Blocking items hit

None.

### Advisory items

- Doc summary: `turn-2.md` line 7 is one "**Check:**" line with four dot-separated points, with no Readability or Voice line, where `references/doc-mode.md` line 412 asks for five dimension lines. It sits in Expected signals, not in the Pass/fail bullet
- "Proposed" capitalized in the follow-ups table (line 123) against fixture line 76 `proposed`. Named at `turn-2.md` line 18
- Borderline, never decides alone: line 48 "Note the time of the first rejection. It is the start of the window you replay in step 4" adds an instruction the notes do not state (they replay "for the window", fixture lines 26 and 51) and no naming line covers it
- Borderline: line 74 "Within a minute of the fix, the payment provider's retries start landing" states INC-0412's 12:49 to 12:50 sequence (fixture lines 24 and 25) in the present tense after "The logs from the INC-0412 fix show what recovery looks like" (line 67), so it reads either as the incident or as a general retry timing
- Borderline: line 64 turns INC-0412's cause (fixture line 22) into the diagnosis for any "`signature_mismatch` after a secret rotation"
- The clarification file uses hyphen bullets (lines 8 to 10, 17 to 18). It is not a Doc artifact, so the ClickUp contract does not apply
- Size: 126 lines, inside 60 to 150

### Read-back table

| Turn | Export path | `N` printed | Read after the last Write or Edit, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - doc-payment-webhook-failures-clarification.md` | 21 | Read at event 49 after the only Write at event 47, lines 1 to 21 (21 empty) | 20 |
| 2 | `export/002 - doc-payment-webhook-failures-runbook.md` | 127 | Read at event 66 after the last Edit at event 64, lines 120 to 127 (127 empty). The full Read at event 41 came before the five Edits (events 56 to 64) | 126 |

### Realism entries

- `export/001 - doc-payment-webhook-failures-clarification.md`, kind Doc clarification, routed pattern `assets/interactive-response-templates.md` line 129. Fields present: purpose and audience (5), scope (7), status and authority (12), missing operational detail (14), proposals and history (16), shape (20). Company facts: 401 with reason `signature_mismatch` (line 7) against `roamstay-payment-webhook-incident-notes.md` line 17 match, the dual-secret window for 1 hour still proposed (17) against line 76 match, the `payment_pending` expiry job belongs to booking-service (12) against line 49 match. Placeholder none. 20 lines
- `export/002 - doc-payment-webhook-failures-runbook.md`, kind Doc, Guide shaped as a runbook. Routed template skill `assets/doc-templates.md` section 3 (lines 167 to 228): Overview (7) and the procedure body renamed under line 232 (34) present. Optional: Before you start (25), Quality checks (96), Boundaries and exceptions (107). Company facts against the incident notes: alert values (line 27, fixture 74) match, 1,284 in the window, 1,190 recovered, 94 expired (line 11, fixture 10) match, 47 minutes from 12:02 to 12:49 UTC (line 11, fixture 8) match, 8 attempts over 24 hours (line 19, fixture 42) match, psp-reconcile every 15 minutes (line 21, fixture 44) match, paused at 12:36 with 94 expired (line 54, fixture 21) match, 71 refunded at 12:45 and 23 never charged (line 92, fixture 10 and 23) match, room back on sale (line 17, `roamstay-context.md` line 148) match. Placeholder none. 126 lines against 60 to 150. Discipline code not applicable

### Open readings

- Does an INC-0412 observation restated as general runbook guidance (line 74 retry timing, line 64 cause) count as an invented behavior claim or step outcome? Graded borderline here, the same reading as PDK-002 step 1
- The five-dimension Doc summary sits in Expected signals only. Should a missing Readability or Voice line fail a Doc scenario?
- `N` 21 and 127 follow the Read's final line, `wc -l` gives 20 and 126

---

## PDK-002 (project), Incident runbook

### Draft row

```csv
PDK-002,project,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 rendered a fenced six-part question under Export-equivalent path export/001 - doc-payment-webhook-failures-clarification.md (turn-1.md lines 1 to 37) and Turn 2 a fenced runbook with steps 1 to 6 in the notes' order, the pause before the fix (line 44), the resume on a normal payment_pending count (line 79) and the dual-secret window proposed (lines 113, 116), with no file claim. Borderline only: step 1's ""Expected result"" generalizes INC-0412 into ""a single rejection reason"" (line 36) and step 6 adds ""with their booking references"" (line 87), both unnamed."
```

### Pass clauses

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

### Blocking items hit

None.

### Advisory items

- Borderline, never decides alone: line 36 "**Expected result:** a high 4xx rate on `/v2/psp/webhooks` with a single rejection reason." states a general outcome for step 1 that the notes give only for INC-0412 (fixture lines 19 and 17), and line 127 describes the expected results as "from INC-0412 where the notes give one" rather than naming them. Project Doc Templates line 216 asks to mark a step unverified when the source does not supply the outcome
- Borderline: line 89 "nobody was charged twice" as step 6's expected result generalizes the INC-0412 guest-impact line (fixture 59)
- Borderline: line 87 "with their booking references" adds a field to the Guest Support hand-off (fixture line 53 "gave Guest Support the list of expired bookings"), unnamed
- Borderline: line 10 adds Guest Support's report as a trigger, line 102 "Steps 1, 2 and 4 to 6 don't depend on the cause", line 118 "stays Open until it's linked from the Payments / Webhooks dashboard", none named
- Block form: fenced both turns, no commentary before the block. Format gate passed both blocks
- Five-line Doc summary present (`turn-2.md` lines 125 to 130)
- Size: 117 lines, inside 60 to 150

### Realism entries

- Turn 1 block (`turn-1.md` lines 2 to 34, copy `blocks/docs/PDK-002-turn1.md`), kind Doc clarification, routed pattern Project `Product Owner - Assets - Interactive Response Templates - v0.102.md` line 106. Fields present as listed in the Pass table. Company facts: 401 `signature_mismatch` on `/v2/psp/webhooks` (line 11) against incident notes line 17 match, the dual-secret window "1 hour" and "proposed", owner Elif (31) against line 76 match, the 30-minute `payment_pending` expiry (2) against notes 42 and `roamstay-context.md` 168 match. Placeholder none. 33 lines
- Turn 2 block (`turn-2.md` lines 2 to 118, copy `blocks/docs/PDK-002-turn2.md`), kind Doc, Guide as a runbook. Routed template Project Doc Templates lines 146 to 207, with the Process rename at line 211: Overview (8) and the procedure body (30) present. Optional: Before you start (23), Cleanup checks (91), Boundaries and exceptions (100). Company facts: 1,284, 1,190, 94, 71 (line 14, fixture 10) match, 47 minutes from 12:02 to 12:49 UTC (14, fixture 8) match, 8 attempts over 24 hours (19, fixture 42) match, paused at 12:36 with 94 expired (44, fixture 21) match, replay 12:02 to 12:49 at 12:58 (71, fixture 26) match, resumed at 13:15 (79, fixture 28) match. Placeholder none. 117 lines against 60 to 150. Discipline code not applicable

### Open readings

- Does an "Expected result" line that generalizes the single incident (line 36 "a single rejection reason", line 89 "nobody was charged twice") count as an invented step outcome under the Fail clause? Graded borderline here. Read as invented, PDK-002 fails on the "states nothing the two attachments do not" clause, and SDK-002 lines 64 and 74 would need the same reading
- Is "because this is a file export" a file claim? Graded no

---

## SDK-003 (skill), Proposal with a decision owner

### Draft row

```csv
SDK-003,skill,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 saved the question-only export/001 - doc-sync-conflicts-lost-edits-clarification.md covering audience, source set, authority, status, shape and scope (lines 5 to 15), and Turn 2 saved export/002 - doc-sync-conflict-options.md with the Proposal notice under the title (lines 3 to 6), Options A to C as the thread gives them, support for B attributed (lines 94 to 96) and Joana, 2026-10-09, not decided (lines 4 to 5, 108). Borderline only: Joana's interim plan carries the label ""Approved direction"" (line 106); advisory: a four-line Doc summary."
```

### Pass clauses

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

### Blocking items hit

None.

### Advisory items

- Borderline, never decides alone: line 106 "Status: Approved direction" then "interim plan set by the decision owner on 2026-09-22, not a choice between the options". The thread records the spike, the A write-up and v3 unchanged as Joana's stated plan (fixture lines 58 to 60), and the user's Turn 2 says "Nothing is settled". The label keeps every option undecided
- Borderline: line 87 places Selin's "a silently merged paragraph that reads wrong is worse than a visible copy" (fixture line 32, said about B) as a risk of C. It stays attributed
- Doc summary: four lines, "Readability and voice" merged (`turn-2.md` lines 7 to 11)
- Turn 1: after the second Bash `sed -i` at event 59 the only Read, event 61, returned line 11 alone. The full Reads at events 44 and 52 came after the Write but before that edit (see table)
- Size: 148 lines, inside 70 to 160

### Read-back table

| Turn | Export path | `N` printed | Read after the last Write or Edit, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - doc-sync-conflicts-lost-edits-clarification.md` | 16 | Only Write at event 42. Reads at events 44 and 52 returned lines 1 to 16 (16 empty). Bash `sed -i` edits at events 50 and 59, and the last Read, event 61, returned line 11 only | 15 |
| 2 | `export/002 - doc-sync-conflict-options.md` | 149 | Read at event 131 after the last Edit at event 129, lines 99 to 149 (149 empty). Full Read at event 122 came after the Bash `sed -i` at event 120 and before that Edit | 148 |

### Realism entries

- `export/001 - doc-sync-conflicts-lost-edits-clarification.md`, kind Doc clarification, routed pattern `assets/interactive-response-templates.md` line 129. Fields present as listed in the Pass table. Company facts: Marta's 33 of 40 August tickets (line 9) against `loomlist-sync-conflict-thread.md` line 36 match, Tomasz's 3 weeks, 6 to 8 weeks and two quarters (9) against lines 24, 26, 28 match, the decision on 2026-10-09 (11) against line 60 match, the doc `Sync conflicts, options for v3 and after` and frame `Sync / Conflict copy` (7) against lines 22 and 32 match. Placeholder none. 15 lines
- `export/002 - doc-sync-conflict-options.md`, kind Doc, Proposal. Routed template skill `assets/doc-templates.md` section 6 (lines 482 to 571): status notice under the title (3 to 6), Overview (8) and the options body (43) present. Optional: Current state (15), Desired outcome (38), Options and trade-offs (81), decision block (104), Dependencies and risks (119), Open decisions (127), Out of scope (138), Source basis (144). Company facts: block-level last-writer-wins (19, thread 14) match, 0.8% (30, thread 18) match, 58% and 42% (31 to 32, thread 48) match, `Conflicting edit from {device name}` (60, thread 26) match, Joana, 2026-10-09, not decided (4 to 5, thread 66 to 68) match, iOS and Android every two weeks over 7 days (121, `loomlist-context.md` 137) match, Elif and 2026-09-22 (147, context line 3) match. Placeholder: `{device name}` is quoted from the thread, exempt under root line 207. 148 lines against 70 to 160. Discipline code not applicable

### Open readings

- Is the label "Approved direction" on the decision owner's interim plan an invented approval under root line 187, when the thread gives it as Joana's plan and the user said "Nothing is settled"? Graded borderline here and on PDK-003 alike
- `N` 16 and 149 follow the Read's final line, `wc -l` gives 15 and 148

---

## PDK-003 (project), Proposal with a decision owner

### Draft row

```csv
PDK-003,project,claude-opus-5-5-medium,FAIL,2,2,pending,yes,"Turn 1 under $d asked no question and rendered a full status write-up under Export-equivalent path export/001 - doc-sync-conflicts-lost-edits-status.md (turn-1.md lines 1 to 88), so the doc-lane clarification block the Pass clause needs never exists. Turn 2's proposal meets its own clauses (notice line 5, Joana and 2026-10-09 not decided, support for B attributed lines 76 to 82); borderline: line 88 ""Tomasz is running a two-week spike"" while line 103 says the spike has no start date."
```

### Pass clauses

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

### Blocking items hit

- Missed Pass clauses, root line 150: Turn 1 drafted instead of asking, the scenario's first Fail example ("Turn 1 drafts"). `Custom Instructions.md` line 108 says `$doc` "still ask" before drafting, and Doc Mode knowledge line 39 makes `$d` its short alias

### Advisory items

- Borderline, never decides alone: line 88 "Tomasz is running a two-week spike" and "He is also writing down" state work in progress, while the thread gives the plan (fixture line 58) and the block's own line 103 says "no start date"
- Borderline: line 53 "which the member has to reconcile by hand" adds a claim the thread does not make, unnamed
- Borderline: line 86 "Status: Approved direction" on Joana's plan, as on SDK-003
- Turn 1 chat heading at line 92 carries an em dash ("Things I assumed or added" then the delimiter), in commentary outside the block
- Block form: fenced both turns, no commentary before the block. Format gate passed both blocks
- Size: Turn 2 block 115 lines, inside 70 to 160

### Realism entries

- Turn 1 block (`turn-1.md` lines 2 to 85, copy `blocks/docs/PDK-003-turn1.md`), kind Doc status write-up in the Narrative overview register, delivered at the clarification turn. Company facts: "**Status: Not decided.**" and 2026-10-09 (line 5) against thread lines 66 and 68 match, 0.8% (30) against line 18 match, `Conflicting edit from {device name}` (48) against line 26 match, offline edits retried until the app closes (78) against `loomlist-context.md` line 176 match. Placeholder: `{device name}` exempt. 84 lines
- Turn 2 block (`turn-2.md` lines 2 to 116, copy `blocks/docs/PDK-003-turn2.md`), kind Doc, Proposal. Routed template Project Doc Templates lines 461 to 550: notice under the title (5), Overview (8) and the options body (31) present. Optional: Current state (16), Options compared (65), Where the thread landed (74), Risks and dependencies (90), Open decisions (97), Out of scope (105), Source basis (111). Company facts: block-level last-writer-wins (20, thread 14) match, 58% and 42% (26 to 27, thread 48) match, about 3 weeks (44, thread 24) match, 6 to 8 weeks (54, thread 26) match, two quarters (63, thread 28) match, Joana, Engineering Manager, Sync, 2026-10-09 (5, thread 67 to 68) match. Placeholder: `{device name}` exempt. 115 lines against 70 to 160. Discipline code not applicable

### Open readings

- Is "Tomasz is running a two-week spike" an invented status (root line 187, "naming never excuses an invented status")? It does not change this verdict
- The "still ask" sentence names `$doc` but not `$d` on both sides (`AGENTS.md` line 287, `Custom Instructions.md` line 108). Is the alias covered by that sentence? Graded yes, through the alias definitions

---

## SDK-004 (skill), Catalog conflict gate

### Draft row

```csv
SDK-004,skill,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 stopped and saved the question-only export/001 - doc-activity-emails-reference-clarification.md listing the spec's ""08:00 in the recipient's local time"" against the inventory's ""Daily at 07:00 UTC"" without choosing (lines 3 to 7), and Turn 2 saved export/002 - doc-activity-emails-catalog.md with EM-01 at 08:00 in the recipient's local time (line 66), EM-06 at Monday 09:00 (line 84) and the six templates on their own entries. N printed 20 and 166 equals wc -l, not the Read's final lines 21 and 167 (AGENTS.md line 45), recorded only."
```

### Pass clauses

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

### Blocking items hit

None.

### Advisory items

- Borderline, never decides alone: line 40 "those two rule out most of the cases below" is an unsourced judgment, unnamed
- `N`: 20 and 166 match `wc -l` but not the Read's final lines 21 and 167, the reverse of the other three skill scenarios
- Turn 1 `HVR self-scan: 2 hard blockers. Fixed: two Oxford commas.` (`turn-1.md` line 5), a count taken and reported
- Five-line Doc summary present (`turn-2.md` lines 8 to 12)
- Size: 166 lines, inside 80 to 180

### Read-back table

| Turn | Export path | `N` printed | Read after the last Write or Edit, lines returned | Real `wc -l` |
|---|---|---|---|---|
| 1 | `export/001 - doc-activity-emails-reference-clarification.md` | 20 | Write at event 38, Read at event 40 lines 1 to 21, Bash `perl -pi` at event 46, Read at event 48 lines 1 to 21 (21 empty) | 20 |
| 2 | `export/002 - doc-activity-emails-catalog.md` | 166 | Write at event 49, Bash `perl -pi` at event 57, Read at event 65 (result event 69) lines 1 to 167 (167 empty) | 166 |

### Realism entries

- `export/001 - doc-activity-emails-reference-clarification.md`, kind Doc clarification, routed pattern `assets/interactive-response-templates.md` line 129 and the conflict gate in `references/doc-mode.md` lines 184 to 188. Fields present as listed in the Pass table plus purpose and audience (11) and domain and detail (13). Company facts: Lena, edited 2026-07-14 (line 5) against `loomlist-notification-spec.md` lines 3 to 4 match, Mateo, edited 2026-09-11 (6) against `loomlist-email-template-inventory.md` lines 3 to 4 match, the 20-item digest cap and the 14-day invite token (13) against inventory lines 23 and 31 match. Placeholder none. 20 lines
- `export/002 - doc-activity-emails-catalog.md`, kind Doc, Catalog. Routed template skill `assets/doc-templates.md` section 4 (lines 259 to 324): Overview (7) and category bodies with one entry per ID (59, 94) present. Optional: Index (14), shared rules (26), Catalog boundaries (150), Sources (161). Company facts: EM-01 at 08:00 recipient's local time (66, spec 12) match, EM-06 Monday 09:00 (84, spec 17) match, switches for EM-01 to EM-04 and EM-06 on by default (35, spec 26) match, 140-character `excerpt` (105, inventory 25) match, invite token expires after 14 days (145, inventory 31) match, six locales with en-US fallback (31, inventory 19) match. Placeholder none. 166 lines against 80 to 180. Discipline code not applicable

### Open readings

- `N` 20 and 166 equal `wc -l` while `AGENTS.md` line 45 asks for the Read's final line (21 and 167). Which is graded?

---

## PDK-004 (project), Catalog conflict gate

### Draft row

```csv
PDK-004,project,claude-opus-5-5-medium,PASS,2,2,pending,yes,"Turn 1 rendered a fenced question listing the spec's ""every day at 08:00 in the recipient's local time"" against the inventory's ""daily at 07:00 UTC"" with neither chosen (turn-1.md line 7) under Export-equivalent path export/001 - doc-loomlist-activity-emails-clarification.md, and Turn 2 a fenced catalog with EM-01 at 08:00 in the recipient's local time (line 59), EM-06 at Monday 09:00 (line 136), the six templates and no push entry. Advisory: the format gate flags the em dash in the three Sources bullets (block lines 168 to 170), which follow the Catalog scaffold's own Sources line."
```

### Pass clauses

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

### Blocking items hit

None.

### Advisory items

- Format gate on the Turn 2 block copy: lines 168 to 170 (reply lines 169 to 171), `prose em dash`, on the three plain Sources bullets. The Project Catalog scaffold writes its Sources line as a link followed by the same delimiter (Project Doc Templates line 302). Not a Pass clause
- Borderline, never decides alone: line 151 "The version bump matters most, because a job built for the old variables then fails loudly instead of sending a broken email" adds a ranking and an outcome the inventory (line 43) does not give, unnamed
- Block form: fenced both turns, no commentary before the block. Turn 1 block passed the format gate
- Five-line Doc summary present (lines 179 to 183, "Layout" for ClickUp layout)
- Size: Turn 2 block 170 lines, inside 80 to 180

### Realism entries

- Turn 1 block (`turn-1.md` lines 2 to 17, copy `blocks/docs/PDK-004-turn1.md`), kind Doc clarification, routed pattern Project Interactive Response Templates line 106 and the conflict gate at Doc Mode knowledge lines 160 to 164. Company facts: 08:00 recipient's local time against `loomlist-notification-spec.md` line 12 match, 07:00 UTC hand-off by `digest-sender` against `loomlist-email-template-inventory.md` line 23 match, the 20-item cap and 14-day invite token (line 13) against inventory lines 23 and 31 match. Placeholder none. 16 lines
- Turn 2 block (`turn-2.md` lines 2 to 171, copy `blocks/docs/PDK-004-turn2.md`), kind Doc, Catalog. Routed template Project Doc Templates lines 238 to 303: Overview (8) and the category body with one entry per ID (50) present. Optional: Shared vocabulary (15), Index (25), shared rules (38), Catalog boundaries (158), Sources (167). Company facts: EM-01 at 08:00 (59, spec 12) match, EM-06 Monday 09:00 (136, spec 17) match, `tpl_digest_v4` (61, inventory 12) match, 140-character `excerpt` (80, inventory 25) match, invite token 14 days (126, inventory 31) match, guests not billed (20, context 29) match. Placeholder none. 170 lines against 80 to 180. Discipline code not applicable

### Open readings

- Should the format gate's em dash finding on a Sources bullet count against a Catalog that follows its own template's Sources line (Project Doc Templates line 302, skill `doc-templates.md` line 323), given that Doc Mode allows the delimiter only in bold-term definitions and status labels (Project Doc Mode line 80, skill `doc-mode.md` line 104)?
- Is "because this is a file export" a file claim? Graded no

---

## Twin notes

**SDK-001 and PDK-001: agree (FAIL, FAIL).** Both runtimes drafted at Turn 1 on the no-command request and named their assumed audience instead of asking (`skill/.../turn-1.md` line 14, `claude project/.../turn-1.md` line 155). The two packagings carry the same text: skill `AGENTS.md` lines 284 to 285 and `references/doc-mode.md` lines 67, 198, 204 and 260, Project `Custom Instructions.md` lines 108 and 130 and Doc Mode knowledge lines 43, 174, 180 and 236. The shared escape ("Once the notes are present and make the reader's use clear, the routing above picks the shape without a preference question", skill line 260, Project line 236) is where both runtimes and the scenario part ways, so this reads as a rule gap between the scenario and both packagings rather than a runtime fault. The twins differ at Turn 2: the skill renamed the primary body to `## Stacking rules` and reworded `one discount code per order`, the Project kept both. Both templates make `## Behavior rules` mandatory (skill `assets/doc-templates.md` lines 115 and 400, Project Doc Templates lines 94 and 379), so that part is a runtime fault on the skill side.

**SDK-002 and PDK-002: agree (PASS, PASS).** Both asked first, both kept the six steps, the pause and resume conditions and the proposed dual-secret window. Both carry unnamed generalizations of INC-0412 into general guidance (skill lines 64 and 74, Project lines 36 and 89), graded borderline on both. The rule both sides share: skill `assets/doc-templates.md` line 237 and Project Doc Templates line 216 ("mark the step unverified rather than inventing a result"), skill `SKILL.md` line 283 and `Custom Instructions.md` line 104 on unnamed additions. The Project leaned harder on labelled "Expected result" lines, so if the operator reads those as invented step outcomes, the pair would differ as a runtime fault on the Project side.

**SDK-003 and PDK-003: differ (PASS, FAIL).** The skill asked a six-field question under `$d`, the Project drafted a status page. Same rule on both sides: `AGENTS.md` line 287 and `Custom Instructions.md` line 108 both say `$doc` "still ask" (neither names `$d`, and both define it as the alias: `AGENTS.md` line 193, Project Doc Mode line 39), and "Clarification is mandatory when ... Purpose or audience materially changes what belongs in the document" sits at skill `doc-mode.md` line 204 and Project Doc Mode line 180. Cause: runtime fault on the Project side. The two Turn 2 proposals then agree closely, and both label Joana's interim plan "Approved direction" (skill export line 106, Project `turn-2.md` line 86).

**SDK-004 and PDK-004: agree (PASS, PASS).** Both stopped at Turn 1, listed both values with both sources, refused the newer date as authority and asked about the other fields, then applied the user's designation within its scope. Rule lines: skill `references/doc-mode.md` lines 184 to 188, Project Doc Mode knowledge lines 160 to 164. Minor differences are advisory only: the Project's Sources bullets trip the format gate, and the skill printed `N` as `wc -l`.
