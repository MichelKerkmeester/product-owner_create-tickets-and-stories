```markdown
# DATA - Guest app - TRK - Booking funnel verification and dashboard cutover

## About

---

The funnel cannot run from search to booking today. `checkout_complete` fires when the confirmation screen renders, so a booking is lost when the app closes early and counted twice when the guest reopens the confirmation from Trips. Revenue per step does not add up across web and apps, because web sends amounts as decimals while the apps send minor units.

This task is the Data team's half of draft v0.3 of the tracking plan, whose event table is unchanged since refinement closed. Nadia checks every event in `events-collector` as the squads ship them, moves the funnel dashboard from `checkout_complete` to `booking_confirmed`, and has the collector drop the old event on its removal date. The client events and `booking_confirmed` itself ship under separate FE and BE tasks.

### Requirements

---

### **Event verification**

---

1.  **Verify each event in `events-collector`**

---

Every event in the plan is checked against its own row once its squad ships it, so a defect reaches that squad before the event reaches a dashboard.

**Checklist**

- [] `search_submitted` carries `destination_id`, `check_in` and `check_out` in `YYYY-MM-DD`
- [] `property_viewed` carries `property_id`, and every later step carries it too
- [] `room_selected` fires once per pick and sends `room_type_id`, `rate_plan_id`, `total_amount_minor` and `currency`
- [] `room_selected` arrives after the price call returns, so its properties are checked on arrival rather than on the tap
- [] `checkout_started` and `payment_submitted` carry `room_type_id`, `rate_plan_id`, `total_amount_minor` and `currency`
- [] `payment_submitted` arrives on the tap, before the payment provider answers, and carries `payment_option` as `pay_now` or `pay_at_property`
- [] `booking_confirmed` arrives from `booking-service` with `source` set to `server`, carrying `booking_id` and `payment_option`
- [] `booking_confirmed` joins to the client events on `session_id`, which it copies from the checkout request
- [] Every event carries `check_in`, `check_out`, `nights`, `guests` and `rooms`
- [] Every event carries `app_version`, `session_id`, `platform`, `locale` and `source`
- [] Every amount arrives as an integer in minor units with `currency` beside it

---

### **Funnel dashboard**

---

2.  **Move the dashboard to `booking_confirmed`**

---

Booking counts move off a client event that loses and repeats bookings, and onto the server event that records the booking as confirmed.

**Checklist**

- [] The funnel runs from `search_submitted` through `property_viewed`, `room_selected`, `checkout_started` and `payment_submitted` to `booking_confirmed`
- [] Every booking count reads `booking_confirmed` and stops reading `checkout_complete`
- [] The cutover lands before `2026-11-01`, so the dashboard reads a live event on the removal date
- [] Revenue per step adds up across iOS, Android and web, since every amount arrives in minor units with `currency`

---

### **`checkout_complete` removal**

---

3.  **Drop `checkout_complete` in `events-collector`**

---

The event keeps firing beside `booking_confirmed` until the removal date, so dashboards have time to move over. From `2026-11-01` the collector drops it, and no app version can send it back into the funnel.

**Checklist**

- [] `events-collector` drops `checkout_complete` from `2026-11-01`, whatever app version sends it
- [] The event keeps firing until `2026-11-01` and is not switched off earlier
```

Export-equivalent path: `export/NNN - task-booking-funnel-verification-and-dashboard-cutover.md`
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality: every floor met | Kind: Task | Energy: Standard

The task gives Nadia three jobs: checking each event and its properties in `events-collector` as the squads ship, moving the funnel dashboard onto `booking_confirmed` before `2026-11-01`, and having the collector drop `checkout_complete` on that date. Every property and date carries the plan's own values. The FE and BE work stays outside it.

### Open items
1. **Title surface**
   - **Situation:** The title grammar wants a surface and this work sits in no product surface, so I used `Guest app` because the funnel is the guest booking funnel
   - **Open:** Send the surface Data tasks carry if it differs
2. **`date_changed` verification**
   - **Situation:** The plan lists it as `proposed`, with its trigger open between per-tap and per-range and no properties agreed, so the task verifies the seven events that are shipping
   - **Open:** Confirm it stays out until the trigger question closes with Search

Want me to change anything?