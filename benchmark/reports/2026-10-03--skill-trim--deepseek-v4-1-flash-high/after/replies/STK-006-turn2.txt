**Path:** `export/002 - task-booking-funnel-tracking.md`
**Verified: read-back succeeded; 71 lines**

**HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason:** the event, property and service identifiers (`search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted`, `booking_confirmed`, `checkout_complete`, `date_changed`, `booking-service`, `events-collector`), the status words `deprecated` and `proposed`, the `2026-11-01` and `2026-09-24` dates, and the `_minor` / `YYYY-MM-DD` notation, all as the sources write them; three-item lists kept because the plan enumerates three funnel problems and you named three Data-owned jobs, so neither shortens without dropping a real item.

**Quality summary:** Completeness 9, Clarity 9, Actionability 9, Accuracy 9, Relevance 9, Mechanism Depth 9. Canonical Task structure, `- []` checklists inside Requirements, `---` dividers where the template requires them, roughly 470 words.

**Summary:** The task now covers only the Data team's TRK work, so the client events and `booking_confirmed` appear as things verified as they land under separate FE and BE tasks, not as work this task builds. It carries the full event table state the plan closed refinement with, including the deprecated `checkout_complete` removal on 2026-11-01 and the proposed `date_changed` held back. One addition to note: the title's surface reads `Guest app`, since the `{Discipline} - {Surface} - {Feature code} - {Title}` convention needs one and the funnel runs through the guest flow; say the word and I will retitle it.

The clarification file `export/001 - task-booking-funnel-events-clarification.md` stays untouched, and I can offer ClickUp delivery once you approve.