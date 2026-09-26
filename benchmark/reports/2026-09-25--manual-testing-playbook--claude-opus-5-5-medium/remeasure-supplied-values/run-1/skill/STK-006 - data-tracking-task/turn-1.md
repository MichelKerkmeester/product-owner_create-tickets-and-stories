I haven't written the task yet. I have a few questions first, and I saved them here:

Path: `export/001 - task-booking-funnel-events-clarification.md`
Verified: read-back succeeded; 27 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Why I couldn't safely draft it straight from the plan:
- **Who builds it:** Nadia's plan gives the work to three groups. The apps and web build the five client events. The Booking squad builds `booking_confirmed` in `booking-service`. The Data team moves the funnel dashboard. Your title format allows only one discipline code, so one task can't cover all three unless you tell me how to split it.
- **`date_changed`:** This event is only `proposed`. The plan hasn't decided whether it fires on each tap or once the new dates are applied.
- **Plan version:** v0.3 is a draft. Comments closed at the refinement on 2026-09-24, and I can't tell whether anything changed there.
- **`room_selected` timing:** Nadia agreed Android sends it once the price is known. It's unclear whether that applies to iOS and web too.

The question file also asks whether dropping `checkout_complete` is part of this task, which links to include, and whether you want a quick pass or a fuller one. When you answer, the task will be saved as the next number, and the question file stays as it is.