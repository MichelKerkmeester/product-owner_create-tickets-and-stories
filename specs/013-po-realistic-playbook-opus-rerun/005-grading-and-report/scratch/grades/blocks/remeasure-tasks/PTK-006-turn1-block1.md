I'll write the task from Nadia's tracking plan (draft v0.3). The plan leaves some decisions open. Please answer them in one reply:

**Split and title:**
- The plan gives the work to three owners. The apps and web own the client events on iOS, Android and web. The Booking squad owns `booking_confirmed` in `booking-service`. The Data team owns the dashboard move
- The title convention allows one discipline code, so which of these should this task be?
  - The client events, as `FE - Guest app - TRK - ...`
  - The server event, as `BE - ...`
  - A parent task with one subtask per owner
  - Another split

**Plan status:**
- Comments closed at the Booking squad refinement on 2026-09-24, but my copy is still draft v0.3 from 2026-09-15. Did that refinement change anything, or should the team build v0.3 as written?

**`date_changed`:**
- It is still marked proposed. Its trigger (one event per tap, or one when the new range is applied) and its properties are both open. Should I leave it out, or include it as blocked until Search decides?

**Details the plan doesn't settle:**
- `room_selected` timing: Nadia agreed that Android sends the event once the price is known. Does that also apply to iOS and web, or does the tap stay the trigger there?
- `booking_confirmed` properties: the plan says every event carries `platform` and `locale`. Its note says `booking-service` copies only `session_id` and `app_version` from the checkout request. Should the server event carry `platform` and `locale`?
- `checkout_complete`: the plan says the date and guest properties go on "every event in the table". Should the deprecated event gain `check_in`, `check_out`, `nights`, `guests` and `rooms` before it is removed on 2026-11-01, or stay as it is?

**Links and dependencies:**
- Should the task link the tracking plan, an epic or parent task, or any related tickets?

**Validation:**
- What am I likely to get wrong about this work?
