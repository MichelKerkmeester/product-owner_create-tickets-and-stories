```
<!-- Mode: Task | Template: Canonical Task v0.103 | Energy: Standard -->

# DATA - Guest app - TRK - Booking funnel events

## About

---

The Guest app cannot draw one funnel from search to booking today. `checkout_complete` fires when the confirmation screen renders on the client, so a booking is lost when the app closes before the screen draws and counted twice when the guest reopens the confirmation from Trips. The web sends amounts as decimals and the apps send minor units, so revenue per step does not add up across platforms, and search and property page events carry dates in three different formats.

This task updates the client events to draft v0.3 of the booking funnel tracking plan. The two live events move to one date shape and the new events fill the steps between the property page and the payment attempt, with money in minor units at every step. The funnel then joins on `session_id`, compares across iOS, Android and web, and counts each booking once from `booking_confirmed`.

`booking_confirmed` is a server event from `booking-service`, so it belongs to the Booking squad, and the funnel dashboard that moves onto it belongs to the Data team. The plan is a draft, so a row that changes at the Booking squad refinement on 2026-09-24 changes this task with it. The `proposed` `date_changed` event stays out until Search settles whether it fires on every pick in the date picker or once when the new range is applied.

**References**

---

- `Booking funnel tracking plan, draft v0.3`, Data team space, comments close 2026-09-24

### Requirements

---

### **Changed events**

---

1.  **`search_submitted` and `property_viewed` move to the shared date shape**

---

Both events exist today and keep their current client triggers. The plan marks them `changed`: they send `check_in` and `check_out` in `YYYY-MM-DD` instead of the three date formats in use, and they gain `nights` and `guests`.

**Checklist**

- [] `search_submitted` sends `check_in` and `check_out` in `YYYY-MM-DD`
- [] `property_viewed` sends `check_in` and `check_out` in `YYYY-MM-DD`
- [] Both events send `nights` and `guests` alongside the dates
- [] `search_submitted` keeps `destination_id`

---

### **New events**

---

2.  **`room_selected` fires on each pick of a room type and rate plan**

---

The plan marks this event `new`. It fires once per pick, and again when a guest goes back and picks another room, so the count matches the picks a guest makes. The Android app does not know `total_amount_minor` until the price call returns, and sending the event after that call is accepted as a delay of a few hundred milliseconds.

**Checklist**

- [] Fires on each pick of a room type and a rate plan
- [] Fires again when a guest goes back and picks a different room
- [] Android sends it after the price call returns, carrying the price of the room picked

---

3.  **`checkout_started` fires when the checkout screen opens**

---

The plan marks this event `new`. It gives the funnel the point where the guest opens checkout, which no event covers today.

**Checklist**

- [] Fires when the checkout screen opens

---

4.  **`payment_submitted` records the payment attempt**

---

The plan marks this event `new`. It fires on the tap, before the payment provider answers, so it records that the guest tried to pay and nothing about whether the payment went through.

**Checklist**

- [] Fires on the Pay now tap, before the payment provider answers
- [] Fires when the guest confirms a Pay at property booking
- [] Carries `payment_option` as either `pay_now` or `pay_at_property`
- [] No funnel step or report reads `payment_submitted` as a completed payment

---

### **Retired event**

---

5.  **`checkout_complete` is `deprecated` and stops at the collector on 2026-11-01**

---

The event keeps firing next to `booking_confirmed` until 2026-11-01, so the funnel dashboard can move over to the server event. From that date `events-collector` drops `checkout_complete`, whatever app version sends it, which means the client needs no change to retire it.

**Checklist**

- [] `checkout_complete` keeps its current client trigger until 2026-11-01
- [] Bookings are counted from `booking_confirmed`
- [] No dashboard or report counts bookings from `checkout_complete` after 2026-11-01

---

### **Shared properties**

---

6.  **Every event carries the common properties and its step's own properties**

---

The common properties from the analytics conventions go on every event and the plan does not repeat them per event. Coverage then grows along the funnel: `property_id` from `property_viewed` onward, and the room, amount and currency properties from `room_selected` onward.

**Checklist**

- [] Every event carries `app_version`, `session_id`, `platform`, `locale` and `source`
- [] `source` reads `client` on every event in this task
- [] Every event carries `check_in`, `check_out`, `nights`, `guests` and `rooms`
- [] `property_id` travels on `property_viewed` and every later step
- [] `room_type_id`, `rate_plan_id`, `total_amount_minor` and `currency` travel from `room_selected` onward
- [] `total_amount_minor` is an integer in minor units with `currency` beside it on iOS, Android and web, and it includes city tax

---
```

Export-equivalent path: `export/001 - task-booking-funnel-events.md`

HVR self-scan: 0 hard blockers. Fixed: em dashes and semicolons kept out of the draft, a second three-item list merged into prose, and no filler modifiers left standing. Kept with reason: supplied identifiers and values verbatim in backticks (`total_amount_minor`, `YYYY-MM-DD`, `events-collector`, `pay_at_property`) and the plan's own status words `new`, `changed`, `deprecated` and `proposed`, each with what it means beside it.

Quality: six-dimension gate passes. Actionability decides a task, and each checklist item names something a tester can observe. Accuracy rests on the plan's own lines, with the draft status stated rather than treated as approved.

Decisions worth your eye, since you can strike any of them:

- **Title.** The convention gives `{Discipline} - {Surface} - {Feature code} - {Title}`. I used `DATA` because the work is tracking events and the plan is Data-owned, `Guest app` as the surface, and `TRK` because a change takes the code of the area it changes. If the app squads own instrumentation in your backlog, `FE` or `FS` would fit the same work.
- **Scope held to the client events** that ship on iOS, Android and web together, matching the plan's own grouping.
- **`booking_confirmed` and the funnel dashboard are left out**, named in About as the Booking squad's and the Data team's workstreams from the plan's "Who builds what", so the task does not claim work it cannot close.
- **`date_changed` is held out of the requirements** because the plan marks it `proposed` and its granularity is still open with Search. It is named in About with that open point, so it can come in as a group once the comments close.
- **The draft status is stated**, since comments close at the Booking squad refinement on 2026-09-24.

No ClickUp connector is attached to this session, so nothing was created or updated outside this Project. Say the word if you want the sketch recast as a parent task with one subtask per platform.