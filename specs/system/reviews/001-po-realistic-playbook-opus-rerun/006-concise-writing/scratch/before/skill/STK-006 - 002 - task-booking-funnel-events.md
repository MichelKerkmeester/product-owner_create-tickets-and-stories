# DATA - Guest app - TRK - Booking funnel event checks and dashboard move

### About

---

Today the funnel from search to booking can't be drawn cleanly. `checkout_complete` fires when the confirmation screen renders, so a booking is lost when the app closes before the screen draws and counted twice when the guest reopens the confirmation from Trips. The web sends amounts as decimals while the apps send minor units, and search and property page events carry dates in three formats. The booking funnel tracking plan fixes this with new and changed events, and every booking count moves to `booking_confirmed`, which `booking-service` sends from the server.

This task is the Data team's part of that plan. The FE and BE tasks build the events. This task checks each event in `events-collector` as the squads ship it, moves the funnel dashboard to `booking_confirmed` before 2026-11-01 and has `events-collector` drop `checkout_complete` on that date. `date_changed` stays out of scope because it is still proposed and its trigger isn't agreed.

**References**

---

- Booking funnel tracking plan, draft v0.3, by Nadia (Data team), event table unchanged at the Booking squad refinement on 2026-09-24

**Related tasks**

---

- `FE task for the booking funnel client events on iOS, Android and web (not created yet)`
- `BE task for booking_confirmed in booking-service (not created yet)`

### Requirements

---

### **Event checks in events-collector**

---

1.  **Client events match the tracking plan**

---

Each client event has to arrive exactly as its tracking plan row describes it, or the funnel steps won't join. iOS, Android and web ship on separate schedules, so each platform is checked when its release goes out. That means the web on deploy, and iOS and Android on their release train.

**Checklist**

- [ ] `search_submitted` fires when the guest taps Search with a destination and valid dates
- [ ] `property_viewed` fires when the property page opens
- [ ] `room_selected` fires once per pick, and fires again when the guest goes back and picks another room
- [ ] On Android, `room_selected` arrives after the price call returns and carries `total_amount_minor`
- [ ] `checkout_started` fires when the checkout screen opens
- [ ] `payment_submitted` fires on the Pay now tap, before the payment provider answers, and when the guest confirms a Pay at property booking
- [ ] Every client event carries `source` set to `client`
- [ ] Every event above is checked separately on iOS, Android and web

2.  **Properties match the tracking plan**

---

The properties fix the date and amount mismatches, so every platform has to send them in the same format.

**Checklist**

- [ ] Every event carries `app_version`, `session_id`, `platform`, `locale` and `source`
- [ ] `check_in` and `check_out` arrive as `YYYY-MM-DD` on every event, including `search_submitted` and `property_viewed`, which drop their old date formats
- [ ] `nights`, `guests` (adults plus children) and `rooms` arrive as integers on every event
- [ ] `nights` equals the nights between `check_in` and `check_out`, so a Monday check-in and Thursday check-out gives 3
- [ ] `destination_id` arrives as an integer on `search_submitted`
- [ ] `property_id` arrives as an integer on `property_viewed` and every later step
- [ ] `room_type_id`, `rate_plan_id`, `total_amount_minor` and `currency` arrive on `room_selected` and every later step
- [ ] `total_amount_minor` is an integer in minor units with city tax included, on web as well as the apps, so €516.00 arrives as `51600`
- [ ] `currency` is an ISO code matching the property's currency
- [ ] `payment_option` is `pay_now` or `pay_at_property` on `payment_submitted` and `booking_confirmed`

3.  **booking_confirmed matches the tracking plan**

---

`booking_confirmed` becomes the only source for booking counts, so it must fire exactly once for each booking that reaches confirmed and never for one that doesn't.

**Checklist**

- [ ] `booking_confirmed` fires when `booking-service` moves a booking to confirmed, with `source` set to `server`
- [ ] A Pay now booking sends it when the payment provider confirms and the booking leaves `payment_pending` for confirmed
- [ ] A Pay at property booking sends it when the booking is created
- [ ] A Pay now booking that expires in `payment_pending` after 30 minutes sends no `booking_confirmed`
- [ ] `session_id` and `app_version` match the checkout request, so the event joins the guest's client events
- [ ] `booking_id` carries the booking reference, `RS-` followed by six letters and digits

> The plan doesn't say whether `booking_confirmed` carries `platform` and `locale`. The note on the event lists only `session_id` and `app_version` as copied from the checkout request. Agree this with the Booking squad before the BE task ships, and check the event against that answer.

---

### **Funnel dashboard**

---

4.  **Funnel dashboard reads booking_confirmed**

---

`checkout_complete` keeps firing next to `booking_confirmed` until 2026-11-01 so the dashboard can move over while both events exist. The dashboard has to be off `checkout_complete` before the collector stops accepting it.

**Checklist**

- [ ] The funnel runs `search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted`, `booking_confirmed`
- [ ] Every booking count on the dashboard uses `booking_confirmed`
- [ ] No part of the funnel dashboard reads `checkout_complete` before 2026-11-01
- [ ] Revenue per step uses `total_amount_minor` with its `currency`, and amounts in different currencies are never summed, because Roamstay does no currency conversion
- [ ] Client and server steps join on `session_id`

---

### **checkout_complete removal**

---

5.  **events-collector drops checkout_complete on 2026-11-01**

---

Older app versions will keep sending `checkout_complete` after the removal date, so the drop happens in `events-collector` rather than depending on the apps.

**Checklist**

- [ ] From 2026-11-01, `events-collector` drops `checkout_complete` from every app version and the web
- [ ] Before that date, `checkout_complete` keeps arriving next to `booking_confirmed`
- [ ] The funnel dashboard shows no gap in booking counts across 2026-11-01
