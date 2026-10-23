```markdown
# DATA - Guest app - TRK - Booking funnel event verification and checkout_complete retirement

## About

---

The booking funnel cannot be read end to end today. `checkout_complete` fires when the confirmation screen renders, so a booking is lost when the app closes early and counted twice when the guest reopens it from Trips. The web sends amounts as decimals and the apps send minor units, so revenue per step does not add up.

This task carries the Data team's share of the plan. The client events and `booking_confirmed` ship in their own FE and BE tasks, while this one verifies each as it lands, moves the funnel dashboard onto `booking_confirmed` and retires `checkout_complete` on 2026-11-01. The refinement closed on 2026-09-24 with the event table unchanged.

**References**

---

Source

- `roamstay-booking-funnel-tracking-plan.md`, draft v0.3, Nadia, Data team, 2026-09-15

Changed

- `events-collector` ingestion of `checkout_complete`

Impacted

- The booking funnel dashboard

### Requirements

---

### **Event verification**

---

1.  **Check each shipped event against its plan row**

---

Each `new` and `changed` row is checked as its squad ships it. The check reads the event as it arrives in `events-collector` and compares it with the row's trigger, its properties and its status. `date_changed` stays out of this check, because the plan still marks it `proposed` and its trigger is open with Search.

**Checklist**

- [] `search_submitted` fires when the guest taps Search with a destination and valid dates
- [] `property_viewed` fires when the property page opens
- [] both events keep their current names, so live dashboards read them while their properties change
- [] `search_submitted` carries `destination_id` as an integer
- [] `property_id` is present on `property_viewed` and on every step after it
- [] `check_in` and `check_out` arrive as `YYYY-MM-DD` on every event in the table
- [] `nights`, `guests` and `rooms` are present on every funnel event, with `guests` counting adults plus children
- [] `room_selected` fires once per room type and rate plan pick, and again after the guest picks a different room
- [] `room_selected` carries `room_type_id`, `rate_plan_id`, `total_amount_minor` and `currency`
- [] the Android `room_selected` arrives after the price call returns, with `total_amount_minor` filled
- [] `checkout_started` fires when the checkout screen opens
- [] `payment_submitted` fires on the Pay now tap, before the payment provider answers
- [] `payment_submitted` fires when the guest confirms a Pay at property booking
- [] `payment_option` reads `pay_now` or `pay_at_property` on `payment_submitted` and `booking_confirmed`
- [] `booking_confirmed` arrives from `booking-service` with `source` set to `server`
- [] `booking_confirmed` carries the `session_id` and `app_version` of the checkout request
- [] `booking_confirmed` carries `booking_id` as the `RS-` booking reference
- [] every event carries `app_version`, `session_id`, `platform`, `locale` and `source`
- [] `total_amount_minor` is an integer in minor units with city tax included, and no event sends a decimal amount

---

2.  **Confirm the funnel joins from search to booking**

---

A funnel per step is only readable if the steps join. `search_submitted` and `property_viewed` exist today and gain properties, so this check covers their old and new shape.

**Checklist**

- [] the steps from `search_submitted` to `booking_confirmed` join on `session_id`
- [] a booking is counted once at `booking_confirmed`, and a reopen from Trips adds no second count
- [] each event arrives from iOS, Android and web, on each `app_version` that ships it
- [] a gap between a plan row and what arrives is logged against the event, the platform and the `app_version` for the owning squad

---

### **Funnel cutover**

---

3.  **Drop `checkout_complete` on 2026-11-01**

---

`checkout_complete` fires on client render until its removal date, next to `booking_confirmed`. From 2026-11-01 `events-collector` drops it, whatever app version sends it, so traffic from an app that still sends it never reaches the funnel.

**Checklist**

- [] `events-collector` drops `checkout_complete` from 2026-11-01, whatever app version sends it
- [] nothing downstream of `events-collector` carries `checkout_complete` after 2026-11-01
- [] the drop ships before the removal date, so no funnel day falls between the two

---

4.  **Move the funnel dashboard to `booking_confirmed`**

---

The dashboard reads `checkout_complete` today, and every booking count moves to `booking_confirmed`. The move lands before the removal date, so the funnel keeps counting through the changeover.

**Checklist**

- [] the booking count in every funnel step reads `booking_confirmed` and no longer reads `checkout_complete`
- [] the dashboard moves before 2026-11-01, so no funnel day is empty
- [] revenue per step reads `total_amount_minor` with `currency`, from `room_selected` onward
- [] a booking that expires in `payment_pending` after `30 minutes` is absent from the count
- [] the step counts for `search_submitted` and `property_viewed` match the properties and dates those events now send
```

Export-equivalent path: `export/NNN - task-booking-funnel-event-verification.md`
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: supplied identifiers such as `checkout_complete`, `payment_pending` and `pay_at_property` in backticks, and 2026-11-01 as the plan writes the removal date.
Quality: every floor met | Kind: Task | Energy: Standard

The task covers the Data team's slice: checking each shipped event against its plan row, confirming the steps join on `session_id`, dropping `checkout_complete` on 2026-11-01 and moving the dashboard to `booking_confirmed` before that date. It carries the property types, the `RS-` booking reference, the minor unit rule and the Android price-call timing as the plan writes them, and it leaves the client events and `booking_confirmed` to the FE and BE tasks.

### Open items
1. **Surface in the title**
   - **Situation:** The conventions set surface as Guest app, Partner Hub or Back office, none of which names a Data team task, so I used Guest app because every funnel event starts there
   - **Open:** Confirm the surface or name the one your board uses for Data work
2. **`date_changed` left out**
   - **Situation:** The plan still marks it `proposed` with the trigger open with Search, so verification covers the `new` and `changed` rows only
   - **Open:** Confirm it sits out until Search settles the trigger
3. **`payment_pending` expiry check**
   - **Situation:** I added a dashboard check that a booking expiring in `payment_pending` after `30 minutes` is absent, drawn from `booking_confirmed` firing when a booking leaves that state
   - **Open:** Strike it if the dashboard does not break the funnel down by payment state
4. **Platform and version coverage**
   - **Situation:** I added a check that each event arrives from iOS, Android and web on each `app_version` that ships it, which the plan does not spell out
   - **Open:** Strike it if staged Android rollout coverage is tracked elsewhere

Want me to change anything?