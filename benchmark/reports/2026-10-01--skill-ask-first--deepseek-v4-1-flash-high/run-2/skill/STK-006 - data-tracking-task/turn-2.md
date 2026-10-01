**Path:** `export/001 - task-booking-funnel-events.md` (refinement keeps the original filename)
**Verified:** read-back succeeded; 86 lines

`HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `deprecated` and `proposed` as supplied status words, backticked identifiers and values (`events-collector`, `booking_confirmed`, `total_amount_minor`, `YYYY-MM-DD`, `2026-11-01`) as literal source values, and the spaced hyphens in the H1 as the required `{Discipline} - {Surface} - {Feature code} - {Title}` separator rather than prose punctuation.`

**Quality summary**
- Scope now matches the Data team's own slice: three requirement groups, event checks in `events-collector`, dashboard move, collector drop
- Accuracy: the client-event and `booking_confirmed` build work is moved out of Requirements into `**Related tasks**`, so no FE or BE build step is claimed as Data's
- Clarity and Actionability: each of the 14 checklist items is a single check Nadia can fail an event on
- Format: canonical Task shape, passed the output-format validator with no advisories, 468 words against the 900 budget

**Summary.** The task is rescoped to the Data team's own work: check every event in `events-collector` against its plan row as the squads ship it, move every booking count in the funnel dashboard to `booking_confirmed`, and have the collector drop `checkout_complete` on `2026-11-01` after the dashboard move finishes. The client events and `booking_confirmed` sit in `**Related tasks**` as planned FE and BE tasks, using your own description of them rather than invented titles. One thing I carried forward that you did not restate: `date_changed` stays a `proposed` row and is marked as unchecked until Search settles its trigger, so it is not read as agreed scope. The supplied sources under `context/` are unchanged.