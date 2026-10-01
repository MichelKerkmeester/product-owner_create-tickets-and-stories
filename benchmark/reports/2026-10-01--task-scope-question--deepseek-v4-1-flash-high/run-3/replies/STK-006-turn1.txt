**Path:** `export/001 - task-booking-funnel-events-clarification.md`

**Verified:** read-back succeeded; 24 lines

**HVR self-scan:** 0 hard blockers. Fixed: none. Kept with reason: literal event, service and property identifiers (`search_submitted`, `booking_confirmed`, `date_changed`, `events-collector`, `session_id`) and the status word `proposed`, each preserved as the supplied tracking plan writes it.

**Quality summary:** This is an intake clarification rather than a draft. It pinpoints the one blocking gap the plan creates: the funnel work is split across three owners (Guest app client events, `booking-service`, Data team) and the request names none of them, so scope cannot be chosen for you. It adds the three other unresolved decisions in the same question, the `date_changed` open point, the plan's draft status ahead of the 2026-09-24 refinement, and the definition of done, so a single reply unblocks the task.

The plan describes eight events, but they do not belong to one squad: five client events ship together on iOS, Android and web, `booking_confirmed` is built by the Booking squad in `booking-service`, and the `checkout_complete` removal plus the dashboard move sit with the Data team. I also flagged `date_changed`, which the plan carries as `proposed` with no agreed properties and an open granularity question from Nadia.

Answer the four points in one reply and the task comes next as `export/002 - task-...`, scoped to the owner you pick.