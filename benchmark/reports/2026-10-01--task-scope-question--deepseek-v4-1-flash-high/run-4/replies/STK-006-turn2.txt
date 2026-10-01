**Path:** `export/002 - task-booking-funnel-events.md`
**Verified:** read-back succeeded; 76 lines
**HVR self-scan:** 0 hard blockers. Fixed: "rather than" rephrased to "not" in two lines (always-cut modifier, not counted). Kept with reason: "iOS, Android and web" and the `room_type_id` / `rate_plan_id` / `total_amount_minor` set, each a source-fixed enumeration rather than a decorative triad.

**Quality summary**
- Artifact kind: Task (not a Story or Epic)
- Structure: `## About` plus `### Requirements`, with three numbered groups and `- []` checklists, `---` dividers per the Task grammar
- Carry-forward: event and property names, `_minor` money rule, `YYYY-MM-DD` dates, `Launched` statuses `new`/`changed`/`deprecated`/`proposed`, the `2026-11-01` removal date and the title convention all travel as the sources write them
- Source handling: the plan and the context were read only and left unchanged

**Summary**
The task scopes the Data team's own `TRK` slice: validating each funnel event in `events-collector` as the `FE` and `BE` tasks ship it, moving every booking count on the funnel dashboard to `booking_confirmed` before `2026-11-01`, and having `events-collector` drop `checkout_complete` on that date. `date_changed` is held out because it stays `proposed` with the tap-versus-range question open, and the `FE` and `BE` tasks are named as dependencies that do not exist yet.

Two additions to confirm or strike: I set the title surface to `Guest app` (the convention allows Guest app, Partner Hub or Back Office, and these are Guest app events), and I did not use `**Parent task**` since none was named. No ClickUp tooling is available in this runtime, so I can only hand you the file.