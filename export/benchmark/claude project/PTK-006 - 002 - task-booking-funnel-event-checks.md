# DATA - Guest app - TRK - Booking funnel event checks and dashboard move

### About

---

The tracking plan changes how Roamstay counts its booking funnel. `checkout_complete` fires when the confirmation screen renders, so a booking is lost when the app closes first and counted twice when reopened from Trips. Web sends decimal amounts and the apps minor units, and search and property page events use three date formats, so no clean funnel can be drawn.

The squads build the client events and `booking_confirmed` in separate FE and BE tasks, and this task is the Data team's part. The draft v0.3 event table stands unchanged after the Booking squad refinement on 2026-09-24. `date_changed` is still proposed and its trigger is undecided, so it stays out of this task.

**References**

---

Tracking plan

- `Booking funnel tracking plan, draft v0.3`

### Requirements

---

1.  **Check each event in events-collector as it ships**

---

Nadia checks every event against its row in the tracking plan when the squad that builds it ships it. Client events ship on iOS, Android and web together, so each one is checked on all three. A wrong trigger or property is caught here, before the dashboard depends on it.

**Every new or changed event**

- [ ] `check_in` and `check_out` arrive as `YYYY-MM-DD` dates, with `nights`, `guests` and `rooms` as integers
- [ ] `source` is `client` on client events and `server` on `booking_confirmed`
- [ ] Client events carry `app_version`, `session_id`, `platform` and `locale`
- [ ] `property_id` is present on `property_viewed` and every later step

**Client events**

- [ ] `search_submitted` fires when the guest taps Search with a destination and valid dates, and carries `destination_id`
- [ ] `search_submitted` and `property_viewed` send their dates only as `check_in` and `check_out`, and now carry `nights` and `guests`
- [ ] `property_viewed` fires when the property page opens
- [ ] `room_selected` fires once per pick, and again when the guest goes back and picks another room
- [ ] On Android, `room_selected` may arrive after the price call returns rather than on the tap
- [ ] `room_selected`, `checkout_started`, `payment_submitted` and `booking_confirmed` carry `room_type_id`, `rate_plan_id`, `total_amount_minor` and `currency`
- [ ] `total_amount_minor` is an integer in minor units with city tax included, on web as well as iOS and Android
- [ ] `checkout_started` fires when the checkout screen opens
- [ ] `payment_submitted` fires when the guest taps Pay now or confirms a Pay at property booking, and carries `payment_option` as `pay_now` or `pay_at_property`

**booking_confirmed**

- [ ] Fires when a Pay now booking leaves `payment_pending` and when a Pay at property booking is created
- [ ] Carries `session_id` and `app_version` copied from the checkout request, so it joins the client events on `session_id`
- [ ] Carries `payment_option` and `booking_id`, the booking reference in the `RS-` format
- [ ] Arrives once per `booking_id`, including when the guest reopens the confirmation from Trips

> The plan puts `platform` and `locale` on every event, but its note for `booking_confirmed` copies only `session_id` and `app_version` from the checkout request. Settle which one applies before checking the server event.

---

2.  **Move the funnel dashboard to booking_confirmed**

---

Booking counts move to the server event, which fires when `booking-service` confirms the booking, whether or not the confirmation screen draws. The move finishes while `checkout_complete` still fires beside `booking_confirmed`.

**Checklist**

- [ ] The funnel runs `search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted`, `booking_confirmed`
- [ ] Every booking count uses `booking_confirmed`, never `checkout_complete` or `payment_submitted`
- [ ] Revenue per step reads `total_amount_minor` with its `currency`
- [ ] The dashboard no longer reads `checkout_complete`, and the move is live before 2026-11-01

---

3.  **Drop checkout_complete in events-collector on 2026-11-01**

---

`checkout_complete` keeps firing until its removal date so dashboards can move over. From 2026-11-01, `events-collector` drops it, whatever app version sends it.

**Checklist**

- [ ] `events-collector` accepts `checkout_complete` until 2026-11-01
- [ ] From 2026-11-01, `events-collector` drops `checkout_complete` from every app version and from the web
- [ ] The drop goes live only after the funnel dashboard reads `booking_confirmed`
