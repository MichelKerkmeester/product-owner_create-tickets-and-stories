```
<!-- Mode: Task | Template: Canonical Task v0.103 | Energy: Standard -->

# DATA - Guest app - TRK - Booking funnel event checks and dashboard move

## About

---

The Guest app cannot draw one funnel from search to booking today. `checkout_complete` fires when the confirmation screen renders on the client, so a booking is lost when the app closes before the screen draws and counted twice when the guest reopens the confirmation from Trips. The web sends amounts as decimals and the apps send minor units, so revenue per step does not add up across platforms, and search and property page events carry dates in three different formats.

This is the Data team's own task under `TRK`. It checks each funnel event in `events-collector` against its row in the tracking plan as the squad ships it, moves the funnel dashboard from `checkout_complete` to `booking_confirmed` before 2026-11-01, and drops `checkout_complete` at the collector on 2026-11-01.

The plan's comment period closed at the Booking squad refinement on 2026-09-24 with the event table unchanged, so those rows are the baseline for every check. The client events ship under FE tasks and `booking_confirmed` under a BE task, so this task holds the checks and the dashboard move rather than the builds. The `proposed` `date_changed` row is unchanged too, with no agreed trigger or properties, so it has no check yet.

**References**

---

- `Booking funnel tracking plan, draft v0.3`, Data team space, comments closed 2026-09-24

### Requirements

---

### **Event checks**

---

1.  **Every funnel event is checked in `events-collector` against its plan row**

---

The checks run as the squads ship, because the client events, `booking_confirmed` and the collector change arrive at different times. An event that fails its check stays out of the funnel counts until the squad that built it closes the gap.

**Checklist**

- [] `search_submitted` and `property_viewed` arrive with `check_in` and `check_out` in `YYYY-MM-DD`, plus `nights` and `guests`
- [] `room_selected` arrives once per pick of a room type and rate plan, carrying `room_type_id`, `rate_plan_id`, `total_amount_minor` and `currency`
- [] `checkout_started` arrives when the checkout screen opens
- [] `payment_submitted` arrives on the pay tap with `payment_option`, and no check reads it as a completed payment
- [] `booking_confirmed` arrives from `booking-service` when a Pay now booking leaves `payment_pending` and when a Pay at property booking is created
- [] `booking_confirmed` carries `source` as `server`, `payment_option` and `booking_id`, and copies `session_id` and `app_version` from the checkout request
- [] A gap found in a check is raised with the squad that built the event

---

### **Platform consistency**

---

2.  **The funnel counts the same stay the same way on every platform**

---

The three defects the plan sets out are the test: money in one unit, dates in one format, and one booking count from the server event.

**Checklist**

- [] Amounts arrive as an integer in minor units with `currency` beside it from iOS, Android and web
- [] Dates arrive in `YYYY-MM-DD` on every event in the funnel
- [] `check_in`, `check_out`, `nights`, `guests` and `rooms` arrive on every event
- [] `app_version`, `session_id`, `platform`, `locale` and `source` arrive on every event
- [] `property_id` arrives on `property_viewed` and every later step, and `room_type_id`, `rate_plan_id`, `total_amount_minor` and `currency` arrive from `room_selected` onward
- [] A client event and its `booking_confirmed` join on `session_id`
- [] A guest who reopens the confirmation from Trips is counted once

---

### **Funnel dashboard**

---

3.  **The dashboard moves to `booking_confirmed` before 2026-11-01**

---

Every step comes from the plan's rows, and bookings are counted from the event the server sends, so a booking counts once whether or not the confirmation screen drew.

**Checklist**

- [] Each funnel stage on the dashboard is built from the plan's events for that stage
- [] Booking counts read `booking_confirmed`
- [] The dashboard stops reading `checkout_complete` before 2026-11-01
- [] No dashboard step breaks when `checkout_complete` stops arriving

---

### **Collector retirement**

---

4.  **`events-collector` drops the `deprecated` `checkout_complete` on 2026-11-01**

---

The event keeps arriving until its removal date so the dashboard can move over, then the collector drops it whatever app version sends it. No client change retires it.

**Checklist**

- [] `checkout_complete` keeps arriving until 2026-11-01
- [] `events-collector` drops `checkout_complete` from 2026-11-01, whatever app version sends it
- [] No report or dashboard reads `checkout_complete` after 2026-11-01

---
```

Export-equivalent path: `export/001 - task-booking-funnel-event-checks-and-dashboard-move.md`

HVR self-scan: 0 hard blockers. Fixed: em dashes, semicolons and Oxford commas kept out, and one three-item list left as the task's own scope statement rather than spread into a second one nearby. Kept with reason: supplied identifiers and status words verbatim in backticks (`events-collector`, `booking-service`, `total_amount_minor`, `YYYY-MM-DD`, `payment_pending`, `deprecated`, `proposed`), each status with its meaning beside it.

Quality: six-dimension gate passes. Actionability decides a task, and every checklist item names something Nadia can observe in `events-collector` or on the dashboard. Accuracy rests on the plan's rows plus what you supplied about the refinement closing unchanged.

What changed from the earlier block, and what I added on top of your message:

- **Title now reads the Data team's own work.** `DATA - Guest app - TRK - Booking funnel event checks and dashboard move`. The old title described building the events, which is now the FE and BE tasks. Surface stayed `Guest app` because the funnel is the Guest app booking funnel. If Data work in your backlog carries a different surface label, say which and I will swap it.
- **The draft caveat is gone.** About now says the comment period closed at the Booking squad refinement on 2026-09-24 with the event table unchanged, so those rows are the baseline for the checks.
- **Two items I added beyond what you told me.** One, a gap found in a check is raised with the squad that built the event. Two, a guest who reopens the confirmation from Trips is counted once, which is the plan's own double-count case turned into a dashboard check. Strike either if you would rather not carry them.
- **`date_changed` stays out with its `proposed` status kept**, since it still has no agreed trigger or properties and there is nothing to check yet.
- **`checkout_complete` arriving until 2026-11-01 is kept as a check**, because both the collector drop and the dashboard move depend on that date.

No ClickUp connector is attached to this session, so nothing was created or updated outside this Project. Next step, if useful: say the word when the FE and BE scopes land and I will draft them as a linked pair that points back at these checks.