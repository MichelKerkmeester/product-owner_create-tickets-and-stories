# Grades draft: tasks batch

Batch `tasks`, twelve scenarios in six twin pairs: `STK-001..STK-006` (skill) and `PTK-001..PTK-006` (Project). Model `claude-opus-5-5-medium`. Graded read-only against the brief `scratch/grading-brief.md` and `scratch/root-at-run.md`.

## Conventions used in this draft

- `<RUN>` is `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/`. Skill evidence sits under `<RUN>/skill/<ID> - <slug>/`, Project evidence under `<RUN>/claude project/<ID> - <slug>/`. Every `replies/<ID>-turn<n>.txt` is byte-identical to its `turn-<n>.md` (checked with `diff -q`, no differences).
- "call N" means the Nth tool call in that turn's `events-turn-<n>.jsonl`, counted in stream order.
- `git -C "AI Systems/Product Owner" status --porcelain -- sk-product-owner "claude project" AGENTS.md benchmark/fixtures` printed nothing, so source and fixture lines are cited from the working tree, which equals `3023c5e`.
- Skill export line numbers are the file as it stands in `exports/export/`. Project line numbers are `turn-<n>.md` reply lines. Block copies for the format gate sit in `scratch/grades/blocks/tasks/<ID>-turn<n>-block<k>.md`, holding the text between the fence lines, so a block copy's line = reply line minus 1.
- Format gate: `node validate-output-format.cjs --system product-owner "<file>"` from the `AI Systems/z*Sync Loop` folder the brief names. All 11 skill export files and all 15 Project block copies printed `Product Owner output format validation passed across 1 artifact file(s)`.
- The Read tool counts the empty line after a trailing newline, so on every export in this batch the Read `totalLines` equals `wc -l` plus 1 (see OR-2).
- Every Project conversation had only `read`, `ls`, `grep`, `find` tools (meta.json), made no Write or Edit call, and every Project turn ledger is empty.

## Shared open readings

- **OR-1, the intake question on an explicit `$task` with full attachments.** `references/task-mode.md` line 50 opens "Ask one comprehensive question unless the request already contains enough direction" before "`$task` and `$bug` still ask their context-specific question and wait", and line 55 repeats the "unless the request already contains enough direction" clause. The Project mirror `Product Owner - Templates - Task Mode` line 30 carries the same sentence. `AGENTS.md` line 287 and `Custom Instructions.md` line 108 state the stricter reading only. The skill runtime cited the looser clause in its own narration: STK-004 turn 1 "Direction is sufficient from the brief and board page, so I'll draft rather than ask", STK-005 turn 1 "the parent gives enough to draft the Android subtask without asking first". PTK-004 turn 1 call 11 grepped `enough direction|already contains`. Graded by each scenario's Pass clause (Turn 1 asks and drafts no task). Question for the operator: does the "unless the request already contains enough direction" clause ever let an explicit `$task` skip its question, or is the scenario reading (an explicit command always asks) the intended one?
- **OR-2, which line count is `N`.** `AGENTS.md` line 46 and `SKILL.md` line 211 set `N` to "the final line number returned by Read". The Read tool reports one more line than `wc -l` on every file here. Most replies printed the Read total, STK-005 printed `wc -l`. No Pass clause in this batch makes the count a condition, so no verdict rests on it. Question: is `N` graded against the Read total or against `wc -l`?
- **OR-3, verbatim versus same value in other words.** STK-003 export line 34 writes "retries up to 5 more times, after 1 min, 5 min, 15 min, 1 h and 6 h" where the Pass clause asks for `5 attempts` and `1 min, 5 min, 15 min, 1 h, 6 h` verbatim. Graded by the text as Unmet. Question: does a hard value restated with the same numbers in different words count as verbatim?
- **OR-4, the `deprecated` status label.** STK-006 and PTK-006 describe the deprecation (fires until 2026-11-01, then `events-collector` drops it) but never print the plan's status word `deprecated`. The Pass clause says "`checkout_complete` marked `deprecated`" and Expected signals say the task "carries the plan's event names, statuses and properties verbatim". Graded by the text as Unmet, which alone decides both 006 verdicts. Question: does stating the status's definition count as marking it `deprecated`, or must the label appear?

---

## STK-001 | Quick copy task (skill)

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

## STK-002 | Design notes FE task (skill)

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

## STK-003 | Long BE integration task (skill)

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

## STK-004 | Parent task with subtasks (skill)

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

## STK-005 | Supplied parent subtask (skill)

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

## STK-006 | Data tracking task (skill)

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

## PTK-001 | Quick copy task (Project)

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

## PTK-002 | Design notes FE task (Project)

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

## PTK-003 | Long BE integration task (Project)

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

## PTK-004 | Parent task with subtasks (Project)

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

## PTK-005 | Supplied parent subtask (Project)

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

## PTK-006 | Data tracking task (Project)

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

## Twin notes

| Pair | Skill | Project | Agree or differ | Cause and rule lines |
|---|---|---|---|---|
| STK-001 / PTK-001 | PASS | PASS | Agree | Both skipped intake under `$quick` (`AGENTS.md` line 289 and `references/interactive-mode.md` line 126; `Custom Instructions.md` line 108 and Interactive Mode knowledge line 103). Minor difference, recorded only: skill chose `FS`, Project `FE`, both with no surface and both named. |
| STK-002 / PTK-002 | FAIL | FAIL | Agree | Both drafted on Turn 1. Both packagings say `$task` asks and waits: `AGENTS.md` line 287, `references/task-mode.md` line 50, `references/interactive-mode.md` line 124; `Custom Instructions.md` line 108, Task Mode knowledge line 30, Interactive Mode knowledge line 101. Same text on both sides, both runtimes missed it, so a runtime fault on both, with the shared wording tension in OR-1. |
| STK-003 / PTK-003 | FAIL | FAIL | Agree on the verdict | Same Turn 1 cause as above. Secondary differences are runtime faults, not packaging gaps: STK-003 has no Read after its last Edit (`AGENTS.md` line 46 requires one; the Project has no read-back rule), and PTK-003 drops the retry schedule and the Fulfilment board, which both runtimes received from the same attachments and turn. |
| STK-004 / PTK-004 | FAIL | FAIL | Agree | Same Turn 1 cause. The skill runtime cited the "enough direction" clause of `references/task-mode.md` line 50; PTK-004 grepped for it (call 11). Both went on to a parent plus four subtasks, saved as five files on the skill side and rendered as five blocks on the Project side, then reduced to the parent alone on Turn 2. |
| STK-005 / PTK-005 | FAIL | FAIL | Agree | Same Turn 1 cause; STK-005 stated "No clarification was needed" (`turn-1.md` line 1). Both link the supplied parent as backticked plain text (`assets/task-templates.md` line 159, Task Mode knowledge line 113) without rewriting it. |
| STK-006 / PTK-006 | FAIL | FAIL | Agree | Both asked correctly on Turn 1 and delivered on Turn 2, and both fail only on the `deprecated` label (OR-4). The status is in the same attachment for both (plan line 25), and neither packaging has a rule on status labels in tasks, so this reads as a scenario-strictness question rather than a rule, parity or runtime gap. Differences, recorded only: STK-006 leaves Nadia out as the checker where PTK-006 keeps her (line 30); PTK-006 promises a save in Turn 1 commentary. |

Tally: skill 1 PASS, 5 FAIL; Project 1 PASS, 5 FAIL. If the operator reads OR-4 as met, STK-006 turns on the Nadia question and PTK-006 on the save-promise question, and both could move to PASS.
