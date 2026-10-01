```markdown
<!-- Mode: Task · Energy: Standard · Template: Task Templates v0.103 · Score: 8/10 -->

# DATA - Guest app - TRK - Booking funnel event checks and dashboard move

## About

---

No single funnel runs from search to booking today. `checkout_complete` fires when the confirmation screen renders, so a booking is lost when the app closes before that screen draws and counted twice when the guest reopens the confirmation from Trips. Amounts leave web as decimals and the apps as minor units, and the search and property page events carry dates in three formats.

This task is the Data team's own work under `TRK`. It checks each funnel event in `events-collector` as the squads ship it, and it moves the funnel dashboard from `checkout_complete` to `booking_confirmed` before 2026-11-01, when `events-collector` drops the old event. The client events and `booking_confirmed` are built under separate FE and BE tasks, so the checks start as each of those lands. `date_changed` stays `proposed` and sits outside this scope.

**References**

---

- Booking funnel tracking plan, draft v0.3, Data team space, with the event table unchanged when comments closed at the Booking squad refinement on 2026-09-24
- Roamstay company context, for the analytics conventions and the `TRK` feature code

**Related tasks**

---

- The FE task for the client funnel events, not yet written
- The BE task for `booking_confirmed` in `booking-service`, not yet written

### Requirements

---

1.  **Check each funnel event as it ships**

---

The Data team checks every funnel event in `events-collector` against the plan's row for it, as the client events and `booking_confirmed` ship under the related tasks. The plan's own problems set what the checks look for.

**Checklist**

- [] Each event in the plan arrives in `events-collector` once per action, carrying the properties its row sets
- [] `check_in` and `check_out` arrive as `YYYY-MM-DD` on every event, with `nights`, `guests` and `rooms` as integers
- [] `destination_id` arrives on `search_submitted`, and `property_id` arrives on `property_viewed` and travels on every later step
- [] `room_selected` and every later step arrive with `room_type_id`, `rate_plan_id`, `total_amount_minor` and `currency`
- [] Amounts arrive in minor units from web and from both apps, so revenue per step adds up across platforms
- [] `room_selected` arrives once per pick, sent when the price is known, and repeats when a guest picks another room
- [] `payment_submitted` arrives on the guest's tap with `payment_option`, before the payment provider answers
- [] `booking_confirmed` arrives from `booking-service` with `source` set to `server`, with `payment_option` and `booking_id`, and with `session_id` and `app_version` copied from the checkout request
- [] Every event carries `app_version`, `session_id`, `platform`, `locale` and `source`

> `date_changed` stays `proposed`, with its trigger open between one event per pick and one when the new range is applied, so it is checked once Search settles that.

---

2.  **Move the funnel dashboard to `booking_confirmed`**

---

The dashboard reads `checkout_complete` today and moves to `booking_confirmed`, the event the plan says every booking count should use. The new event comes from `booking-service` once per confirmed booking, not once per screen render.

**Checklist**

- [] Every booking count on the funnel dashboard reads `booking_confirmed`
- [] The funnel runs from `search_submitted` to `booking_confirmed` as one path, joined on `session_id` between client and server events
- [] A booking counts once, including when the guest reopens the confirmation from Trips
- [] Revenue per step reads `total_amount_minor` in minor units with its `currency`
- [] Steps read one date format, from `check_in` and `check_out`
- [] The move lands before 2026-11-01

---

3.  **Retire `checkout_complete`**

---

`checkout_complete` keeps firing beside `booking_confirmed` until 2026-11-01, which is the window the dashboards use to move over. From that date `events-collector` drops it, whatever app version sends it.

**Checklist**

- [] `checkout_complete` keeps firing until 2026-11-01, so the dashboards have time to move
- [] From 2026-11-01 `events-collector` drops `checkout_complete`, from every app version that sends it
- [] The drop needs no client release, because it happens in `events-collector`
- [] No dashboard, report or alert reads `checkout_complete` after the removal date
```

Export-equivalent path: `export/002 - task-booking-funnel-event-checks-and-dashboard-move.md`

HVR self-scan: 0 hard blockers. Fixed: still, just (always-cut modifiers cut during drafting). Kept with reason: the plan's event, property and service names, its `proposed`, `deprecated` and `changed` status words, and the 2026-11-01 date, all carried as the source writes them.

Quality status: Task lane, Standard energy, standalone task. All six floors pass, 8/10. Actionability carried it, since every checklist item names something a tester can see in `events-collector` or on the dashboard. Accuracy held at 9, because each value, status and date comes from the plan or from your answer, with no invented ship dates or owners.

Two choices you can strike if I read them wrong. The title's surface reads Guest app, since the plan's events all come from that surface, and I left the client events and `booking_confirmed` builds out as related FE and BE work rather than closing them into this task. `date_changed` is noted as out until Search settles its trigger, which is the one row the refinement left open.

Next: send me the FE and BE task details once they exist, so the check timing in group 1 lines up with their ship dates.