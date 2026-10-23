```markdown
# DATA - Guest app - TRK - Booking funnel event verification and dashboard cutover

## About

---

The funnel cannot be drawn from search to booking today. `checkout_complete` fires when the confirmation screen renders, so an app closed before the screen draws loses the booking and a reopened confirmation counts it twice. Amounts and dates also disagree across platforms.

This is the Data team's task under `TRK`. Nadia checks each event in `events-collector` as the squads ship it, moves the funnel dashboard to `booking_confirmed` and has the collector drop `checkout_complete` on 2026-11-01. The client events and `booking_confirmed` arrive as separate FE and BE tasks, so nothing here instruments an event.

**References**

---

- `Booking funnel tracking plan`, draft v0.3, Data team space, written by Nadia, last edited 2026-09-15
- `Roamstay company context`, maintained by Leila, last reviewed 2026-09-18
- `events-collector`, Data team
- Funnel dashboard, Data team, reading `checkout_complete` today

### Requirements

---

1.  **Check each event as its build ships**

---

Each row is read in `events-collector` once the build behind it ships, and compared with the trigger, properties and value format its row sets. A row is checked only after its event arrives, so these checks trail the FE and BE work.

**Checklist**

- [] Every event in the table carries `check_in`, `check_out`, `nights`, `guests` and `rooms`, with both dates in `YYYY-MM-DD`
- [] Every event carries `app_version`, `session_id`, `platform`, `locale` and `source`
- [] `search_submitted` carries `destination_id`, and `property_viewed` and every later step carry `property_id`
- [] `room_selected` carries `room_type_id`, `rate_plan_id`, `total_amount_minor` and `currency`
- [] `room_selected` fires again when a guest goes back and picks another room
- [] `checkout_started` arrives when the checkout screen opens, with the stay properties
- [] `payment_submitted` carries `payment_option` as `pay_now` or `pay_at_property`, and fires on the tap before the payment provider answers
- [] `booking_confirmed` comes from `booking-service` with `source` set to `server`, carrying `booking_id`, `payment_option` and the stay properties
- [] `booking_confirmed` copies `session_id` and `app_version` from the checkout request
- [] An event short of its row goes back to the owning squad as a ticket naming the event and the missing property

---

2.  **Hold one money format and one date format**

---

Revenue per step has to add up across iOS, Android and web, and the funnel has to line up on one date format. The web sends decimals where the apps send minor units, and search and property page events carry dates in three formats.

**Checklist**

- [] Every amount is an integer in minor units under a name ending `_minor`, so €129.50 is sent as `12950`
- [] `currency` sits beside every amount and holds `EUR`, `GBP`, `USD`, `CHF` or `SEK`
- [] `total_amount_minor` includes city tax
- [] `nights` agrees with the gap between `check_in` and `check_out`, so a Monday to Thursday stay counts as 3 nights

---

3.  **Count bookings on `booking_confirmed`**

---

`booking_confirmed` is the only event that states a booking happened, and `booking-service` sends it server-side, so a guest who closes the app before the confirmation screen renders still counts once. The funnel dashboard moves to it before `checkout_complete` is dropped.

**Checklist**

- [] The funnel dashboard counts a booking from `booking_confirmed` and never from `checkout_complete`
- [] The client steps join the booking on `session_id`
- [] A booking whose app closed before the confirmation screen rendered appears once
- [] Reopening a confirmation from Trips does not count a second time
- [] `payment_submitted` reads as an attempt to pay and never as a completed payment
- [] The dashboard is off `checkout_complete` before 2026-11-01

---

4.  **Drop `checkout_complete` on 2026-11-01**

---

The event keeps firing beside `booking_confirmed` so dashboards can move over. From its removal date the collector drops it, whatever app version sends it.

**Checklist**

- [] `checkout_complete` keeps firing beside `booking_confirmed` until 2026-11-01
- [] `events-collector` drops `checkout_complete` on 2026-11-01, whatever app version sends it
- [] A client still sending it after that date leaves no row in the collector

---

5.  **Leave `date_changed` unchecked until its trigger is settled**

---

The row is `proposed` and has no properties agreed beyond the common ones and the dates. Its trigger is open between one event per tap in the picker and one when the new range is applied, and the 2026-09-24 refinement closed with the event table unchanged.

**Checklist**

- [] `date_changed` stays out of the funnel until Search settles whether it fires per tap or per applied range
- [] When it ships, it carries the common properties and the stay properties and nothing else
```

Export-equivalent path: `export/002 - task-booking-funnel-event-verification.md`
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality: every floor met | Kind: Task | Energy: Standard

The task covers the Data team's side of the booking funnel: event checks in `events-collector` as each build ships, one money and date format, booking counts on `booking_confirmed`, and the collector drop on 2026-11-01. `date_changed` sits outside the funnel until Search settles its trigger.

### Open items
1. **Surface in the title**
   - **Situation:** The conventions allow Guest app, Partner Hub or Back office, and this work spans the Guest app funnel, `booking-service` and `events-collector`
   - **Open:** Confirm Guest app or name the surface you want
2. **Failed check route**
   - **Situation:** I added a checklist item that sends an event short of its row back to the owning squad as a ticket, which the tracking plan does not name
   - **Open:** Strike it or name the route the Data team uses
3. **FE and BE tasks left unnamed**
   - **Situation:** The client event and `booking_confirmed` tasks have no titles yet, so About names them by discipline and the task carries no `Related tasks` block
   - **Open:** Send the titles once they exist and I'll link them

Want me to change anything?