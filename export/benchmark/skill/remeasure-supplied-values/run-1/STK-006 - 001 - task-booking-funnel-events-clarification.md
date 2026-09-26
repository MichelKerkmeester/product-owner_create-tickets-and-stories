# Booking funnel events: questions before the task

I'll write the task from Nadia's tracking plan (draft v0.3). A few answers first, all in one reply:

**0. How should I work this?**
- Quick: a lean pass with smart defaults
- Deeper: a full read with every edge case the plan raises

**1. Scope and split:** The plan's "Who builds what" names three builders. Which should the task cover?
- One task for the client events on iOS, Android and web: `search_submitted` and `property_viewed` (changed), plus `room_selected`, `checkout_started` and `payment_submitted` (new)
- One task for `booking_confirmed` in `booking-service` (Booking squad)
- One task for moving the funnel dashboard from `checkout_complete` to `booking_confirmed` (Data team)
- A parent task with one subtask per builder
- Something else

**2. Title:** Titles follow `{Discipline} - {Surface} - {Feature code} - {Title}`. For the client events I'd use `FE - Guest app - TRK - Booking funnel events`. Is `FE` right, or should it be `DATA`? If `booking_confirmed` is in scope, which discipline and surface should its title use?

**3. `date_changed`:** It is `proposed`, and the plan still leaves open whether it fires on each tap in the picker or once when the new range is applied. Should I leave it out, list it as out of scope, or include it with a trigger you give me?

**4. Plan status:** Comments closed at the Booking squad refinement on 2026-09-24. Is v0.3 the version to build, or did that refinement change any event, property or date?

**5. `room_selected` timing:** Nadia agreed that Android sends `room_selected` once `total_amount_minor` is known, not on the tap. Should that rule apply to iOS and web too, or to Android only?

**6. `checkout_complete` removal:** `events-collector` drops it from 2026-11-01. Is that drop part of this task, or should the task only mention it as a dependency?

**7. Links:** Should the task link an epic, ClickUp tickets or the tracking plan itself? If so, please send the links
