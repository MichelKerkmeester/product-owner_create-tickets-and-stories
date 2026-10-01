```markdown
# DATA - Guest app - TRK - Booking funnel event checks and dashboard cutover

## About

---

`checkout_complete` fired when the confirmation screen rendered, so the funnel lost bookings the app closed before the screen drew and counted others twice. Web amounts were decimals while the apps sent minor units, so revenue per step did not add up across platforms. The reworked event table in `Booking funnel tracking plan v0.3` is the agreed baseline for the funnel.

The Data team owns this work: the event checks in `events-collector` as each sending squad ships, the funnel dashboard moving to `booking_confirmed`, and `events-collector` dropping `checkout_complete` on 2026-11-01. The Guest app client events and `booking_confirmed` ship under separate FE and BE tasks.

**References**

---

Changed

- `events-collector`
- `Funnel dashboard`

**Related tasks**

---

- `Guest app client funnel events` (FE task, to be created)
- `booking_confirmed in booking-service` (BE task, to be created)

### Requirements

---

1.  **Check every funnel event in `events-collector`**

---

Every event in the plan's table is checked against its row once its sending squad ships it, covering the trigger, the properties and `source`.

**Checklist**

- [] Each client event fires on its plan trigger, with `room_selected` firing once per pick and again after a changed pick
- [] `booking_confirmed` arrives from `booking-service` with `source` set to `server`
- [] Client and server events join on `session_id`, so one guest journey reads from `search_submitted` to `booking_confirmed`
- [] `check_in` and `check_out` arrive in `YYYY-MM-DD` on every step, replacing the three earlier date formats
- [] Amounts arrive as integers in minor units from the web as well as the apps, with `currency` beside the amount
- [] A booking is counted once, so reopening the confirmation adds no second booking event

> `date_changed` stays `proposed` and sits outside these checks. Its trigger is still open between one event per picker tap and one event when the guest applies the new range, and Search settles that later.

---

2.  **Move the funnel dashboard to `booking_confirmed`**

---

The dashboard counts bookings with `checkout_complete` today, which misses the bookings the confirmation screen never drew and counts reopened confirmations twice. It moves to `booking_confirmed`, the event the plan designates for booking counts, before `checkout_complete` stops firing.

**Checklist**

- [] Every funnel step on the dashboard reads its plan event, with the booking step on `booking_confirmed`
- [] Dashboard booking counts match `booking_confirmed` volume in `events-collector` over the same period
- [] Revenue per step reconciles across web, iOS and Android once amounts arrive in minor units
- [] One funnel reads end to end at `25 results` per search page through to a confirmed booking

---

3.  **Drop `checkout_complete` in `events-collector` on 2026-11-01**

---

`checkout_complete` is `deprecated` and keeps firing next to `booking_confirmed` until its removal date so the dashboards can move over. From 2026-11-01 `events-collector` drops it, whatever app version sends it.

**Checklist**

- [] `events-collector` drops `checkout_complete` from 2026-11-01, from any app version
- [] No dashboard, report or alert still reads `checkout_complete` on that date
```

Export-equivalent path: `export/002 - task-booking-funnel-events.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the event, property, service and status names as literal identifiers the sources supply (`checkout_complete`, `booking_confirmed`, `date_changed`, `room_selected`, `session_id`, `booking-service`, `source`, `server`, `deprecated`, `proposed`), the supplied dates and formats (2026-11-01, `YYYY-MM-DD`), and `25 results` from the conventions.

Quality status: gate passes. Actionability and Mechanism Depth carry it: every checklist item names something observable in `events-collector` or on the dashboard, and the About opens on why the funnel was reworked before what the task does. Scope stays inside the Data team's three changes, and no squad-level build steps leaked in.

Assumptions, each strikeable:

- The title reads `DATA - Guest app - TRK`, with Guest app as the surface because the funnel runs there. `events-collector` also takes events from the services, so say the word if you want a different surface.
- It is a standalone task, since the client events and `booking_confirmed` sit in their own FE and BE tasks. Related tasks names them as plain text because they have no titles or links yet.
- The dashboard is referenced as `Funnel dashboard`, since no name or location came with it. A link would replace that label in place.
- `date_changed` is kept out of the checks and carried in a note beside them, since it is `proposed` with its trigger still open.

Next step: no ClickUp connector is present in this session, so nothing was pushed anywhere. With one connected, say the word and I will offer the task push through its markdown field.