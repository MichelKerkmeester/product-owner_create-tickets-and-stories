# DATA - Guest app - TRK - Booking funnel event checks and dashboard move

## About

---

The search-to-booking funnel can't be drawn cleanly: `checkout_complete` fires when the confirmation screen renders, so an early app close loses the booking and a Trips reopen counts it twice. Web amounts are decimals, app amounts minor units, and search and property page dates use three formats, which the booking funnel tracking plan fixes.

This is the Data team's part, as FE and BE tasks build the events: check each event in `events-collector` as squads ship it, move the funnel dashboard to `booking_confirmed` before 2026-11-01 and have `events-collector` drop `checkout_complete` that day. `date_changed` is out of scope because it is proposed and its trigger isn't agreed.

**References**

---

- Booking funnel tracking plan, draft v0.3, by Nadia (Data team), event table unchanged at Booking squad refinement on 2026-09-24

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

Client events must match their tracking plan rows exactly, or funnel steps won't join. Each platform is checked at release: web on deploy, iOS and Android on their train.

**Checklist**

- [] `search_submitted` fires on Search with a destination and valid dates
- [] `property_viewed` fires when the property page opens
- [] `room_selected` fires once per pick, including after going back
- [] On Android, `room_selected` arrives after the price call returns, with `total_amount_minor`
- [] `checkout_started` fires as checkout opens
- [] `payment_submitted` fires on the Pay now tap, before the payment provider answers, and on Pay at property confirm
- [] Every client event has `source` = `client`
- [] Each event is checked on iOS, Android and web separately

2.  **Properties match the tracking plan**

---

The properties fix the date and amount mismatches, so every platform uses one format.

**Checklist**

- [] Every event has `app_version`, `session_id`, `platform`, `locale` and `source`
- [] `check_in` and `check_out` are `YYYY-MM-DD` on every event, replacing old formats on `search_submitted` and `property_viewed`
- [] `nights`, `guests` (adults plus children) and `rooms` are integers on every event
- [] `nights` is the nights between `check_in` and `check_out`, so Monday to Thursday is 3
- [] `destination_id` is an integer on `search_submitted`
- [] `property_id` is an integer on `property_viewed` onward
- [] `room_type_id`, `rate_plan_id`, `total_amount_minor` and `currency` are on `room_selected` onward
- [] `total_amount_minor` is integer minor units including city tax, on web and apps, so €516.00 is `51600`
- [] `currency` is the property's ISO currency code
- [] `payment_option` is `pay_now` or `pay_at_property` on `payment_submitted` and `booking_confirmed`

3.  **booking_confirmed matches the tracking plan**

---

`booking_confirmed` becomes the only booking count source, so it fires exactly once per confirmed booking and never otherwise.

**Checklist**

- [] `booking_confirmed` fires when `booking-service` confirms a booking, with `source` = `server`
- [] Pay now sends it when the payment provider confirms and the booking leaves `payment_pending`
- [] Pay at property sends it on booking creation
- [] A Pay now booking expiring in `payment_pending` after 30 minutes sends none
- [] `session_id` and `app_version` match the checkout request, joining the guest's client events
- [] `booking_id` is the reference, `RS-` plus six letters and digits

> The plan doesn't say whether `booking_confirmed` carries `platform` and `locale`, and its note copies only `session_id` and `app_version` from checkout. Agree it with the Booking squad before the BE task ships, then check against it.

---

### **Funnel dashboard**

---

4.  **Funnel dashboard reads booking_confirmed**

---

`checkout_complete` fires beside `booking_confirmed` until 2026-11-01, so the dashboard must move over before the collector stops accepting it.

**Checklist**

- [] The funnel runs `search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted`, `booking_confirmed`
- [] Every dashboard booking count uses `booking_confirmed`
- [] No dashboard part reads `checkout_complete` before 2026-11-01
- [] Revenue per step uses `total_amount_minor` with `currency`, never summed across currencies, because Roamstay does no conversion
- [] Client and server steps join on `session_id`

---

### **checkout_complete removal**

---

5.  **events-collector drops checkout_complete on 2026-11-01**

---

Old app versions will keep sending `checkout_complete`, so `events-collector` drops it rather than the apps.

**Checklist**

- [] From 2026-11-01, `events-collector` drops `checkout_complete` from every app version and web
- [] Until then, `checkout_complete` arrives beside `booking_confirmed`
- [] Dashboard booking counts show no gap across 2026-11-01
