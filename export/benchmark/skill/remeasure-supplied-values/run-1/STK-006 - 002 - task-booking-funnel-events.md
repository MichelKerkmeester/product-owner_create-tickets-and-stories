# DATA - Guest app - TRK - Verify booking funnel events and move the funnel dashboard

### About

---

We can't draw one clean funnel from search to booking today. `checkout_complete` fires when the confirmation screen renders on the client, so a booking is lost when the app closes before the screen draws and counted twice when the guest reopens the confirmation from Trips. The web sends amounts as decimals while the apps send minor units, and search and property page events carry dates in three formats.

The tracking plan fixes this with six funnel events and moves every booking count to `booking_confirmed`, which `booking-service` sends when a booking is confirmed. The squads build the events in separate tasks: the client events in an FE task and `booking_confirmed` in a BE task. This task is the Data team's part. Nadia checks each event in `events-collector` as a squad ships it, moves the funnel dashboard to `booking_confirmed` and has `events-collector` drop `checkout_complete` on its removal date, 2026-11-01.

The plan's event table was confirmed unchanged at the Booking squad refinement.

**References**

---

- `Booking funnel tracking plan, draft v0.3` (Data team space, written by Nadia)

### Requirements

---

1.  **Check each funnel event as it ships**

---

A squad builds an event from its row in the tracking plan, and the dashboard can only move once the events match their rows. Check each event in `events-collector` when its squad ships it. Check client events on iOS, Android and web, because the web is built and released separately from the apps.

Events in scope: `search_submitted` and `property_viewed` (`changed`, live events whose properties change), plus `room_selected`, `checkout_started`, `payment_submitted` and `booking_confirmed` (`new`).

**Every event**

- [ ] Carries the common properties `app_version`, `session_id`, `platform`, `locale` and `source`
- [ ] `source` is `client` on the five client events and `server` on `booking_confirmed`
- [ ] Carries `check_in` and `check_out` as dates in `YYYY-MM-DD`, with `check_in` as the first night and `check_out` as the departure day
- [ ] Carries `nights`, `guests` (adults plus children) and `rooms` as integers
- [ ] Carries `property_id` as an integer from `property_viewed` onward

**`search_submitted`**

- [ ] Fires when the guest taps Search with a destination and valid dates
- [ ] Carries `destination_id` as an integer
- [ ] No longer sends its dates in the old formats

**`property_viewed`**

- [ ] Fires when the property page opens
- [ ] No longer sends its dates in the old formats

**`room_selected`**

- [ ] Fires once per room type and rate plan pick, and again when the guest goes back and picks another room
- [ ] On Android, fires once the price call returns and `total_amount_minor` is known rather than on the tap, as Nadia agreed on 2026-09-15
- [ ] From this event onward, carries `room_type_id` and `rate_plan_id` as integers
- [ ] From this event onward, carries `total_amount_minor` as an integer in minor units with city tax included, with `currency` beside it as an ISO code
- [ ] Web sends `total_amount_minor` in minor units like the apps, so €516.00 arrives as `51600` and never as a decimal

**`checkout_started`**

- [ ] Fires when the checkout screen opens

**`payment_submitted`**

- [ ] Fires when the guest taps Pay now or confirms a Pay at property booking, before the payment provider answers
- [ ] Carries `payment_option` as `pay_now` or `pay_at_property`

**`booking_confirmed`**

- [ ] Fires from `booking-service` when it moves a booking to confirmed, meaning a Pay now booking confirmed after `payment_pending` or a Pay at property booking at creation
- [ ] Does not fire for a Pay now booking that expires in `payment_pending` after 30 minutes
- [ ] Fires once per booking, including when the app closes before the confirmation screen draws, and does not fire again when the guest reopens the confirmation from Trips
- [ ] Carries `payment_option` as `pay_now` or `pay_at_property`
- [ ] Carries `booking_id` as the booking reference, such as `RS-2MF8QD`
- [ ] Carries the `session_id` and `app_version` of the checkout request, so it joins the guest's client events on `session_id`

---

2.  **Move the funnel dashboard to `booking_confirmed`**

---

`booking_confirmed` is the one event that counts each confirmed booking exactly once, so every booking count on the funnel dashboard moves to it. `checkout_complete` keeps firing beside `booking_confirmed` until 2026-11-01 so the dashboard can move over, and the move has to finish before that date.

**Checklist**

- [ ] The dashboard shows the funnel in this order: `search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted`, `booking_confirmed`
- [ ] Every booking count on the dashboard uses `booking_confirmed`, and none uses `checkout_complete`
- [ ] Client and server events join on `session_id`, so a guest's `booking_confirmed` sits in the same funnel as their client events
- [ ] Revenue per step uses `total_amount_minor` and adds up across iOS, Android and web
- [ ] Revenue is shown per `currency` and never summed across currencies, because Roamstay charges in the property's currency with no conversion
- [ ] `payment_submitted` is read as an attempt to pay and never counted as a booking
- [ ] The move is live before 2026-11-01

---

3.  **Drop `checkout_complete` in `events-collector` on 2026-11-01**

---

`checkout_complete` is `deprecated`: it keeps firing until its removal date, then `events-collector` drops it. The drop happens in the collector, so older app versions that still send the event are covered too.

**Checklist**

- [ ] Until 2026-11-01, `events-collector` keeps accepting `checkout_complete` beside `booking_confirmed`
- [ ] From 2026-11-01, `events-collector` drops `checkout_complete` whatever app version sends it
- [ ] The drop goes ahead only after the dashboard no longer reads `checkout_complete`

> `date_changed` is out of scope. It is `proposed`, and the plan hasn't settled whether it fires once per tap in the picker or once when the new range is applied. It joins this check once Search and the Data team agree its trigger and properties
