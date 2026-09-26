# DATA - Guest app - TRK - Booking funnel event checks and dashboard move

## About

---

The tracking plan changes how Roamstay counts bookings. `checkout_complete` fires on the confirmation screen, so a booking is lost when the app closes first and doubled when reopened from Trips. Web sends decimal amounts, the apps minor units, and search and property page events use three date formats.

Separate FE and BE tasks build the client events and `booking_confirmed`, and this is the Data team's part. The draft v0.3 event table stands after the Booking squad refinement on 2026-09-24. `date_changed` stays out, still proposed with an undecided trigger.

**References**

---

Tracking plan

- `Booking funnel tracking plan, draft v0.3`

### Requirements

---

1.  **Check each event in events-collector as it ships**

---

Nadia checks each event against its tracking plan row as it ships, client events on iOS, Android and web.

**Every new or changed event**

- [] `check_in` and `check_out` arrive as `YYYY-MM-DD` dates, with `nights`, `guests` and `rooms` as integers
- [] `source` is `client` on client events and `server` on `booking_confirmed`
- [] Client events carry `app_version`, `session_id`, `platform` and `locale`
- [] `property_id` is on `property_viewed` and every later step

**Client events**

- [] `search_submitted` fires when the guest taps Search with a destination and valid dates, carrying `destination_id`
- [] `search_submitted` and `property_viewed` send dates only as `check_in` and `check_out`, and now carry `nights` and `guests`
- [] `room_selected` fires once per pick, including a new pick after going back
- [] On Android, `room_selected` may arrive after the price call returns, not on the tap
- [] `room_selected`, `checkout_started`, `payment_submitted` and `booking_confirmed` carry `room_type_id`, `rate_plan_id`, `total_amount_minor` and `currency`
- [] `total_amount_minor` is an integer in minor units with city tax included, on every platform
- [] `property_viewed` fires when the property page opens, and `checkout_started` when the checkout screen opens
- [] `payment_submitted` fires when the guest taps Pay now or confirms a Pay at property booking, and carries `payment_option` as `pay_now` or `pay_at_property`

**booking_confirmed**

- [] Fires when a Pay now booking leaves `payment_pending` and when a Pay at property booking is created
- [] Carries `session_id` and `app_version` from the checkout request, joining client events on `session_id`
- [] Carries `payment_option` and `booking_id`, the `RS-` format booking reference
- [] Arrives once per `booking_id`, even when the confirmation is reopened from Trips

> The plan puts `platform` and `locale` on every event, but its `booking_confirmed` note copies only `session_id` and `app_version`. Settle which applies before checking the server event.

---

2.  **Move the funnel dashboard to booking_confirmed**

---

`booking_confirmed` fires when `booking-service` confirms, whether or not the confirmation screen draws.

**Checklist**

- [] The funnel runs `search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted`, `booking_confirmed`
- [] Booking counts use `booking_confirmed`, never `checkout_complete` or `payment_submitted`
- [] Revenue per step reads `total_amount_minor` with its `currency`
- [] The move is live before 2026-11-01, with no `checkout_complete` read left

---

3.  **Drop checkout_complete in events-collector on 2026-11-01**

---

**Checklist**

- [] `events-collector` accepts `checkout_complete` until 2026-11-01
- [] From 2026-11-01, it drops `checkout_complete` from every app version and the web
- [] The drop goes live only after the funnel dashboard reads `booking_confirmed`
