I'll write the task for the booking funnel events. Before I draft it, please answer the questions below in one reply:

**0. How should I work this?**
- Quick: a short pass using sensible defaults
- Deeper: a close read of both files and a fuller checklist

**1. Scope and owner:**
The plan splits the build between three owners. Apps and web build the client events. The Booking squad builds `booking_confirmed` in `booking-service`. The Data team moves the funnel dashboard to `booking_confirmed` before 2026-11-01. Which of these do you want?
- One task that covers all three owners
- A parent task with one subtask per owner
- One owner's part only, and if so, whose

**2. Title:**
Titles follow `{Discipline} - {Surface} - {Feature code} - {Title}`. Tracking work is `TRK`. Which discipline code and surface should the task use? For example, `DATA - Guest app - TRK - ...` for a single task, or `FE` and `BE` for subtasks

**3. Plan status:**
The file is draft v0.3. Comments closed at the Booking squad refinement on 2026-09-24. Is v0.3 the agreed version, or did that refinement change anything the task should include?

**4. `date_changed`:**
It is `proposed`, and one question is still open with Search: does it fire on every tap in the picker, or once when the new range is applied? Should the task include it, include it as blocked until that is decided, or leave it out?

**5. `room_selected` timing:**
Nadia agreed that Android can send it after the price call returns. Does the same apply to iOS and web?

**6. Common properties on `booking_confirmed`:**
The plan puts `app_version`, `session_id`, `platform`, `locale` and `source` on every event. It also says `booking-service` copies only `session_id` and `app_version` from the checkout request. Should `booking_confirmed` also carry `platform` and `locale`?

**7. `checkout_complete` retirement:**
Should the task cover the `deprecated` period, when it fires alongside `booking_confirmed` until `events-collector` drops it on 2026-11-01, or is that the Data team's work?

**8. Links:**
Is there a ClickUp link for the tracking plan, an epic or related tickets? If not, I'll name them without a link
