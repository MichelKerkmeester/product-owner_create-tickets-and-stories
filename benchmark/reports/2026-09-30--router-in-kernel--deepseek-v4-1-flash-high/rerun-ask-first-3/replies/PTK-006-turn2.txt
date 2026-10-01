```markdown
<!-- Mode: Task | Template: Assets - Task Templates v0.103 -->

# DATA - Guest app - TRK - Booking funnel event verification and dashboard move

## About

---

This task covers the Data team's part of the booking funnel tracking plan. Each event is verified in `events-collector` as its squad ships it, the funnel dashboard moves onto `booking_confirmed` and the collector drops `checkout_complete` on 2026-11-01.

The funnel cannot be drawn cleanly today. `checkout_complete` fires when the confirmation screen renders on the client, so a booking is lost when the app closes early and counted twice when the guest reopens the confirmation from Trips. The web sends amounts as decimals while the apps send minor units, and dates arrive in three formats.

The client events on the Guest app and `booking_confirmed` in `booking-service` are separate tasks. `date_changed` stays `proposed`, with no properties agreed and its trigger still open, so no funnel step depends on it.

**References**

---

Plan

- `Booking funnel tracking plan, draft v0.3, Data team space`

**Related tasks**

---

- `FE task for the client events on the Guest app`
- `BE task for booking_confirmed in booking-service`

### Requirements

---

1.  **Verify every funnel event in `events-collector`**

---

Each event in the plan's table is checked against its row as the squads ship it. The check covers the event, its properties and the values it carries, because the dashboard reads them directly.

**Checklist**

- [] Every event in the plan's table arrives in `events-collector` with the common properties `app_version`, `session_id`, `platform`, `locale` and `source`
- [] `check_in` and `check_out` arrive as `YYYY-MM-DD` on every event, with `nights`, `guests` and `rooms` beside them
- [] `search_submitted` carries `destination_id`, and `property_id` arrives on `property_viewed` and on every later step
- [] `room_type_id`, `rate_plan_id`, `total_amount_minor` and `currency` arrive on `room_selected` and on every later step
- [] `total_amount_minor` arrives as an integer in minor units from every platform, so `51600` in `EUR` reads as one total with city tax included
- [] `room_selected` arrives once per room pick and again when the guest goes back and picks another room
- [] On Android, `room_selected` arrives once the price is known rather than on the tap, with `total_amount_minor` filled
- [] `payment_submitted` arrives on the tap before the payment provider answers, and says nothing about whether the payment succeeded
- [] `booking_confirmed` arrives from `booking-service` with `source` set to `server` and with `booking_id`, copying `session_id` and `app_version` from the checkout request
- [] `payment_option` arrives as `pay_now` or `pay_at_property` on `payment_submitted` and `booking_confirmed`
- [] A property or value that differs from the plan's row is raised with the squad that owns the event

---

2.  **Move the funnel dashboard onto `booking_confirmed`**

---

The dashboard reads `checkout_complete` today, which ties a booking to a screen drawing on the client. The move puts every booking count on the server event instead.

**Checklist**

- [] The funnel dashboard draws one funnel from `search_submitted` to `booking_confirmed` before 2026-11-01
- [] Every booking count on the dashboard uses `booking_confirmed`
- [] A booking counts once when the guest reopens the confirmation from Trips, and is not lost when the app closes before the screen draws
- [] Revenue per step adds up across the platforms, because every amount arrives in minor units with its `currency`
- [] The funnel's steps run `search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted` and `booking_confirmed`, in that order
- [] A Pay now booking that expires in `payment_pending` after `30 minutes` never reaches `booking_confirmed`, so it is absent from the counts

---

3.  **Drop `checkout_complete` in `events-collector`**

---

`checkout_complete` keeps firing next to `booking_confirmed` until 2026-11-01, so the dashboard move above is finished before the drop. From that date the collector drops it, whatever app version sends it.

**Checklist**

- [] The dashboard reads `booking_confirmed` before `checkout_complete` stops arriving on 2026-11-01
- [] `events-collector` drops `checkout_complete` from 2026-11-01, whatever app version sends it
- [] Nothing reads `checkout_complete` after that date
- [] An app on an older version that still sends `checkout_complete` changes nothing in the funnel's counts

---
```

Export-equivalent path: `export/002 - task-booking-funnel-event-verification-and-dashboard-move.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the plan's own event, property, service and status names in backticks, which stay as the source writes them, and `proposed` kept beside `date_changed` so its unsourced state is not lost.

Quality: the shape fits a Data-owned verification and cutover task, the three requirement groups are numbered, every box is `- []`, all supplied values travel as the plan writes them, and the About states the out-of-scope tasks rather than their build work.

Three things to check before this hardens, since you supplied two of them only partly.

- I titled it `DATA - Guest app - TRK`. The surface is the one call the conventions force and your answer did not name, and I set it from the plan's guest funnel. Strike it if the dashboard move belongs under another surface.
- The item asking a differing property or value to be raised with the owning squad is my addition, since you described the check but not the mismatch path.
- The `payment_pending` item comes from the conventions doc, which expires such a booking after `30 minutes`. It is the case that tells the funnel's counts apart from the dashboard it replaces.

`date_changed` is named as an exclusion rather than a requirement, because refinement closed with the row still `proposed` and its trigger open. No link was supplied for the plan, so its reference bullet stays backticked plain text, and the two FE and BE tasks you mentioned sit under Related tasks the same way.