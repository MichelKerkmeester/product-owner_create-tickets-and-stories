Path: `export/001 - task-booking-funnel-events-clarification.md`
Verified: read-back succeeded; 26 lines

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `TRK`, `search_submitted`, `checkout_complete`, `date_changed`, `booking-service`, `events-collector` and the `2026-11-01` date are source literal identifiers carried verbatim; `proposed` is the plan's own status word.

Quality summary: Accuracy 9 (every item traces to the plan or the conventions doc), Completeness 8, Clarity 8, Actionability 8, Relevance 8, Mechanism Depth 8. Source files were read only and left untouched.

I did not draft the task yet. Routing is Task Mode ("write a task"), but the tracking plan splits the work three ways in its `Who builds what` section (client events on the Guest app, `booking_confirmed` in `booking-service`, the funnel dashboard in Data) and your request names no slice, so the scope is genuinely unresolved. The exported question asks for one response covering the scope and owner, the title's discipline and feature code, the two open decisions (`date_changed` at `proposed` with its trigger unsettled, and whether the `checkout_complete` removal is in scope), and whether the draft is approved before the `2026-09-24` refinement. Send those and the task takes number 002.