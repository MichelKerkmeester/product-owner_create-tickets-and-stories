**Path:** `export/001 - task-booking-funnel-events.md`
**Verified:** read-back succeeded; 131 lines

`HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `deprecated` and `proposed` as supplied status words, `pay_now` / `pay_at_property` and the other backticked identifiers as literal source values, and the spaced hyphens in the ticket title as the required `{Discipline} - {Surface} - {Feature code} - {Title}` separator rather than prose punctuation.`

**Quality summary**
- Accuracy: every event, property, service and date traces to the plan as written, including the `new`, `changed`, `deprecated` and `proposed` status words
- Completeness: all seven buildable rows plus the dashboard move are covered, with `booking-service`, `events-collector` and the `2026-11-01` removal date named rather than generalized
- Clarity and Actionability: six numbered groups, each requirement a single `- []` item a build can fail
- Relevance: scoped to the plan's events, no adjacent work pulled in
- Format: canonical Task shape (`## About` → `### Requirements` → numbered groups), passed the output-format validator with no advisories

**Summary.** The task is titled `DATA - Guest app - TRK - Booking funnel events` and covers the plan's client events, the `booking_confirmed` server event, the `checkout_complete` retirement and the dashboard move, in six numbered requirement groups. Two judgement calls you may want to strike: I scoped it to the whole event table rather than the client events alone, since the plan's "Who builds what" splits the work across apps and web, Booking and Data, and `date_changed` is carried as a `proposed` group that gates the build until Search settles whether it fires per tap or per applied range rather than being treated as agreed scope. The plan is named as draft v0.3 with comments closing at the 2026-09-24 refinement, so no row is presented as approved.