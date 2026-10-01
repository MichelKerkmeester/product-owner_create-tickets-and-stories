**Path:** `export/001 - task-booking-funnel-events.md`

Verified: read-back succeeded; 102 lines

HVR self-scan: 0 hard blockers. Fixed: no blocked terms survived the pass; "rides on" became "is sent with" and a vague "the problems above" cross-reference was cut, both conciseness edits and so not counted. Kept with reason: backticked supplied identifiers and status words (`total_amount_minor`, `_minor`, `pay_now`, `pay_at_property`, `payment_pending`, `RS-2MF8QD`, `changed`, `new`, `deprecated`, `proposed`) stay verbatim because the plan supplies them.

**Quality summary**

| Dimension | Reading |
| --- | --- |
| Completeness | Every plan row ready to build is covered, in five numbered requirement groups |
| Accuracy | Each event, trigger, property, status and date traces to the plan or the context file |
| Actionability | Each item is a checkable statement with its supplied value |
| Clarity | One reading per item, no build steps |
| Relevance | Scoped to the plan's funnel rows and its three stated problems |
| Mechanism depth | The About states why the rebuild exists, so unlisted cases follow from it |

**Summary.** The task covers the plan's `changed` and `new` events and the `deprecated` retirement of `checkout_complete`, as five requirement groups, with the event contract stated once and the date, amount and platform problems fixed across it. Client events are scoped to iOS, Android and web together, and `booking_confirmed` to `booking-service`, matching the plan's own build split.

**Judgment calls you may want to change**

- Title: I read the work as one full-stack change, so the title uses `FS - Guest app - TRK -`, the plan being the tracking-plan area. Say the word if you want the `BOOK`, `SRCH` or `DATA` discipline instead
- `date_changed` is held out of the requirements and named in a note, because the plan carries it as `proposed` with unagreed properties and an open trigger question to settle with Search
- The "expires in `payment_pending` after `30 minutes`" item comes from the Roamstay context file's checkout section, not the plan's tables. It is the boundary that keeps an expired booking from being expected in the counts
- The plan is a draft, with comments closing at the Booking squad refinement on `2026-09-24`, so the rows are worth re-checking before the build starts

No ClickUp tooling is available in this runtime, so nothing was pushed anywhere. Want me to re-cut the scope to client events only, or to split the server and dashboard work into sibling tasks?