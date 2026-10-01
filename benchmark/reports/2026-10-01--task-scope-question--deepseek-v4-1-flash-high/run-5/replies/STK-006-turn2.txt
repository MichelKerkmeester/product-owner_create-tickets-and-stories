Path: `export/002 - task-booking-funnel-events.md`
Verified: read-back succeeded; 75 lines

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `events-collector`, `booking-service`, `checkout_complete`, `room_type_id`, `rate_plan_id`, `total_amount_minor`, `session_id`, `app_version` and `2026-11-01` are source literal identifiers carried verbatim, and `- []` is the required checklist form.

Quality summary: Accuracy 9 (every requirement and value traces to the plan or the conventions doc), Completeness 8, Clarity 8, Actionability 8, Relevance 8, Mechanism Depth 8. Both source files were read only and left untouched.

The task scopes to Data's share under `TRK`: verifying each event in `events-collector` as its squad ships it, moving the funnel dashboard to `booking_confirmed` before `2026-11-01`, and retiring `checkout_complete` in the collector on its removal date, with the client events and `booking_confirmed` left to the later FE and BE tasks.

Three things to check, since I chose them rather than you supplying them:

- Surface in the title. I wrote `DATA - Guest app - TRK - Booking funnel events`, since the funnel is the Guest app funnel. Say the word if you want a different surface.
- A blockquoted note that `date_changed` stays `proposed` and its verification waits on the unsettled trigger decision with Search, which the plan leaves open.
- A `Related tasks` block naming the FE and BE tasks by their plan pieces, without invented titles or links.

If any of those look wrong, tell me and I will revise.