```markdown
# DATA - Guest app - TRK - Booking funnel events

## About

---

`checkout_complete` fires when the confirmation screen renders, so a booking is lost when the app closes early and counted twice when the guest reopens the confirmation from Trips. Web sends amounts as decimals while the apps send minor units, and search and property page events carry dates in three formats.

This task covers the Data team's side of the tracking plan: verifying each funnel event in `events-collector` as its squad ships it, moving the dashboard onto `booking_confirmed`, and dropping `checkout_complete` on its removal date. The client events and `booking_confirmed` are built under separate FE and BE tasks, and `date_changed` stays `proposed`, so none of them sits here.

**References**

---

- `context/roamstay-booking-funnel-tracking-plan.md`, the tracking plan this task verifies against

Changed

- `events-collector`
- Funnel dashboard, Data team space

**Related tasks**

---

- Client events on iOS, Android and web, under a separate FE task
- `booking_confirmed` in `booking-service`, under a separate BE task

### Requirements

---

1.  **Verify each funnel event in `events-collector`**

---

The plan lists `search_submitted` and `property_viewed` as `changed` and the steps from `room_selected` onward as `new`. Each event is checked as its squad ships it, so the funnel can be read end to end and revenue per step adds up across the platforms.

**Checklist**

- [] Confirm each event arrives in `events-collector` as its squad ships it
- [] Confirm `search_submitted` carries `destination_id`
- [] Confirm `search_submitted` and `property_viewed`, which are `changed`, move their dates to `check_in` and `check_out` in `YYYY-MM-DD` and gain `nights` and `guests`
- [] Confirm `property_viewed` and every later step carry `property_id`
- [] Confirm `check_in`, `check_out`, `nights`, `guests` and `rooms` on every event
- [] Confirm `room_selected` onward carries `room_type_id`, `rate_plan_id`, `total_amount_minor` and `currency`
- [] Confirm amounts arrive as an integer in minor units from web, iOS and Android, so revenue per step adds up across platforms
- [] Confirm `payment_submitted` and `booking_confirmed` carry `payment_option`, and `booking_confirmed` carries `booking_id`
- [] Confirm `booking_confirmed` arrives from `booking-service` with `source` set to `server`, copying `session_id` and `app_version` from the checkout request
- [] Confirm the common properties `app_version`, `session_id`, `platform`, `locale` and `source` on every event
- [] Confirm client and server events join on `session_id` from `search_submitted` through to `booking_confirmed`
- [] Treat `room_selected` as arriving after the price call returns, which the plan allows, so a late event is not read as a missing one
- [] Read `payment_submitted` as an attempt to pay only, never as a completed payment
- [] Leave `date_changed` out while it stays `proposed`, since it has no agreed properties beyond the common ones and the dates

---

2.  **Move the funnel dashboard onto `booking_confirmed`**

---

The dashboard counts bookings from `checkout_complete`, which fires when the confirmation screen renders. Counting from `booking_confirmed` gives one booking per booking, and the move has to finish before the old event is dropped.

**Checklist**

- [] Take every booking count from `booking_confirmed`
- [] Draw the funnel from `search_submitted` through `booking_confirmed`
- [] Confirm revenue per step adds up across iOS, Android and web in the property's currency
- [] Confirm a booking still appears in the funnel when the app closed before the confirmation screen drew
- [] Finish the move before `2026-11-01`, ahead of the `checkout_complete` removal
- [] Confirm no tile still reads `checkout_complete` on the removal date

---

3.  **Drop `checkout_complete` on `2026-11-01`**

---

`checkout_complete` is `deprecated` and keeps firing next to `booking_confirmed` until its removal date, so the dashboards can move over. From `2026-11-01`, `events-collector` drops it whatever app version sends it.

**Checklist**

- [] Keep `checkout_complete` flowing to `events-collector` until `2026-11-01`
- [] Have `events-collector` drop `checkout_complete` on `2026-11-01`, whatever app version sends it
- [] Confirm `checkout_complete` no longer reaches `events-collector` after the removal date
- [] Confirm the funnel dashboard stays correct once the event is dropped
```

Export-equivalent path: `export/002 - task-booking-funnel-events.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `carries` kept as the plan's own verb for event properties, the platform list `web`, `iOS` and `Android` kept as a fixed source enumeration, and every supplied event, property, status and date kept verbatim in backticks.

Quality: outcome and value open About, scope is bounded to the Data team's three workstreams, the statuses `changed`, `new`, `deprecated` and `proposed` travel with what each one means, and every checklist line is checkable from `events-collector` or the dashboard.

Two things I chose rather than read: the title surface is Guest app, because the funnel runs there and the house format needs a surface, and the title wording is mine. I also read the refinement closing with no change to the event table as the plan being settled for this work, and read "as the squads ship them" as verification per event rather than one pass at the end. The FE and BE tasks have no titles yet, so I described them in `Related tasks` rather than naming them.

Tell me what to change, and the FE and BE tasks can follow whenever you want them.