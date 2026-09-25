```markdown
# DATA - Guest app - TRK - Booking funnel event checks and dashboard move

### About

---

The booking funnel tracking plan changes how Roamstay counts the path from search to booking. Today `checkout_complete` fires when the confirmation screen renders. A booking is lost when the app closes before the screen draws, and counted twice when the guest reopens the confirmation from Trips. The web sends amounts as decimals while the apps send minor units, and search and property page events carry dates in three formats, so no one can draw one clean funnel.

The squads build the client events and `booking_confirmed` in separate FE and BE tasks. This task is the Data team's part: check each event in `events-collector` as it ships, move the funnel dashboard to `booking_confirmed` and have the collector drop `checkout_complete` on its removal date, 2026-11-01. The event table in draft v0.3 stands as written after the Booking squad refinement on 2026-09-24.

`date_changed` is still proposed and its trigger is undecided, so it stays out of this task.

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
```

Export-equivalent path: `export/002 - task-booking-funnel-event-checks.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality:** The task passes the quality check. It only covers your team's work: checking events, moving the dashboard and dropping `checkout_complete`. What the squads build stays in the FE and BE tasks you mentioned. I named them in About but didn't link them, because they don't exist yet.

**Additions I made:** remove any you don't want.
- **One `booking_confirmed` per booking:** a check that it arrives once per `booking_id`. I based this on the double counting the plan wants to fix.
- **Booking reference:** a check that `booking_id` uses the `RS-` format from your company glossary.
- **Order of steps:** the collector drops `checkout_complete` only after the dashboard has moved. The plan puts both on 2026-11-01 but doesn't say which comes first.

**Still open:** your answer settled the event table but not these two points.
- **`platform` and `locale` on `booking_confirmed`:** the plan disagrees with itself here. I left this as a note in the task instead of choosing an answer.
- **`room_selected` timing:** the task allows the late send on Android only, which is what Nadia agreed to. If iOS and web can also send it once the price is known, that line needs to cover all three platforms.