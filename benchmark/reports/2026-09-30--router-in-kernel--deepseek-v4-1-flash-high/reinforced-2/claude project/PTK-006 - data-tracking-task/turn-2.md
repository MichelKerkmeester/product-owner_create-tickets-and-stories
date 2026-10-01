```markdown
# DATA - Guest app - TRK - Booking funnel event verification and dashboard migration

## About

---

The funnel cannot be drawn from search to booking as one line. `checkout_complete` fires on the client when the confirmation screen renders, so a booking is lost when the app closes first and counted twice when the guest reopens the confirmation from Trips. Amounts arrive as decimals on the web and as minor units on the apps, and the dates on the search and property page events arrive in three formats.

This task covers the Data team's part of the fix, under `TRK`. Nadia verifies each event in `events-collector` as the squads ship it, moves the funnel dashboard onto `booking_confirmed` before `2026-11-01`, and has `events-collector` drop `checkout_complete` on its removal date.

**References**

---

Impacted

- `events-collector`
- The funnel dashboard

**Related tasks**

---

- Client funnel events, a separate FE task for iOS, Android and web
- `booking_confirmed`, a separate BE task in `booking-service`

### Requirements

---

1.  **Verify each funnel event as it ships**

---

Every event gets checked against its own row in the tracking plan, once the squads ship it. The row's name, trigger, properties and status are the standard the event is held to.

**Checklist**

- [] Each shipped event reaches `events-collector` under the name and status its tracking plan row gives
- [] Every event carries `app_version`, `session_id`, `platform`, `locale` and `source`
- [] Every event carries `check_in`, `check_out`, `nights`, `guests` and `rooms`
- [] `check_in` and `check_out` arrive as `YYYY-MM-DD`, with the other date formats gone
- [] `property_id` sits on `property_viewed` and every later step
- [] `room_selected` fires once per pick, and again when the guest picks another room
- [] `room_selected` onward carries `room_type_id`, `rate_plan_id`, `total_amount_minor` and `currency`
- [] `total_amount_minor` is an integer in minor units, city tax included
- [] Android sends `room_selected` after the price call returns, so `total_amount_minor` is always populated
- [] `payment_submitted` carries `payment_option` as `pay_now` or `pay_at_property`, and fires before the payment provider answers
- [] `booking_confirmed` arrives from `booking-service` with `source` set to `server`, plus `payment_option` and `booking_id`
- [] `booking_confirmed` copies `session_id` and `app_version` from the checkout request, so client and server events join on `session_id`

> `date_changed` stays `proposed`, so it is not verified here. Search still has to settle whether it fires per tap in the picker or once when the new range is applied.

2.  **Move the funnel dashboard onto `booking_confirmed`**

---

The dashboard reads a booking from `checkout_complete` today, so it carries both the lost booking and the double count. It has to sit on `booking_confirmed` before the collector drops the old event.

**Checklist**

- [] The funnel reads from search to booking as one line, built from the plan's events
- [] Every booking count on the dashboard uses `booking_confirmed`
- [] No funnel step, tile or saved query reads `checkout_complete` after the move
- [] The dashboard is live on `booking_confirmed` before `2026-11-01`
- [] Revenue per step adds up across iOS, Android and web from the minor-unit amounts
- [] A booking whose confirmation screen never draws is counted, and one reopened from Trips is counted once

3.  **Retire `checkout_complete` in `events-collector`**

---

`checkout_complete` keeps firing beside `booking_confirmed` until its removal date, which gives the dashboards a window to move over. From that date `events-collector` drops it, whatever app version sends it.

**Checklist**

- [] `events-collector` keeps accepting `checkout_complete` until `2026-11-01`
- [] From `2026-11-01` `events-collector` drops `checkout_complete` from every app version that sends it
- [] The removal date stays `2026-11-01`, as the tracking plan gives it
- [] No dashboard, alert or saved query reads `checkout_complete` on that date
```

Export-equivalent path: `export/NNN - task-booking-funnel-event-verification-and-dashboard-migration.md`

Quality status: pass on all six dimensions. Every event name, property, status and date is carried as the tracking plan writes it, and each checklist item is something a verifier can observe in `events-collector` or on the dashboard.

HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: `events-collector`, `booking-service`, `events-collector`, `booking_confirmed`, `checkout_complete`, `date_changed`, `TRK`, the property names and the `2026-11-01` date are literal identifiers and supplied values, and `proposed` is the plan's own status word, named with what it means rather than replaced.

Two calls I made, so you can correct them:

- Title reads `DATA - Guest app - TRK - ...`, taking Guest app as the surface because the funnel events are Guest app events. The task itself changes `events-collector` and the dashboard, so tell me if you title it differently.
- The blockquote after the first checklist is my addition. It keeps `date_changed` out of the verification checks and names its open point, which is the plan's current state. Strike it if you would rather the task say nothing about that event.

Client events and `booking_confirmed` are named under Related tasks as separate later work, so the task verifies them without claiming to build them.