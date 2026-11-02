# Booking funnel events task: questions before drafting

I'll write the task from Nadia's tracking plan (draft v0.3) and the Roamstay conventions. The plan leaves a few decisions open, and two of its lines disagree, so please answer the points below in one reply.

**1. Scope and split**

The plan hands the build to three owners: Apps and web build the client events on iOS, Android and web, the Booking squad builds `booking_confirmed` in `booking-service`, and the Data team moves the funnel dashboard off `checkout_complete` before 2026-11-01. A task title takes one discipline and one surface, so which of these do you want?

- A parent task under `TRK` with one subtask per owner (client events, `booking_confirmed`, dashboard move)
- One task for the client events only, such as `DATA - Guest app - TRK - Booking funnel client events`
- One task for `booking_confirmed` only
- Something else, with the discipline code you want in the title

**2. `booking_confirmed` trigger**

The events table says it fires when `booking-service` moves the booking to confirmed. The notes say it fires when a Pay now booking leaves `payment_pending`. A Pay now booking also leaves `payment_pending` when it expires after 30 minutes, so the note would count expired bookings. Should the table's wording govern, or do you want to check with Nadia first?

**3. `date_changed`**

It is marked proposed, and Nadia and the Search squad haven't settled whether it fires on every tap in the picker or once when the new range is applied. Should the task leave it out, or carry it as a blocked item waiting on that decision?

**4. `room_selected` timing**

Nadia agreed that Android sends `room_selected` once the price call returns, because `total_amount_minor` isn't known on the tap. Should iOS and web follow the same rule, or does it apply to Android only?

**5. Common properties on the server event**

The plan puts `app_version`, `session_id`, `platform`, `locale` and `source` on every event. The conventions list `platform` and `locale` for client events only, and the note says `booking_confirmed` copies `session_id` and `app_version` from the checkout request. Should `booking_confirmed` also carry `platform` and `locale`?

**6. `checkout_complete` until removal**

The date, `nights`, `guests` and `rooms` properties apply to "every event in the table", which includes `checkout_complete`. Should it gain them for its last weeks, or stay unchanged until `events-collector` drops it on 2026-11-01?

**7. Plan status and links**

Comments on v0.3 closed at the Booking squad refinement on 2026-09-24. Did the plan pass as written, or is a newer version coming? Also send any epic, parent task or tracking plan link the task should reference.
