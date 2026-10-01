```markdown
# DATA - Guest app - TRK - Booking funnel event verification and dashboard cutover

## About

---

The plan's event table closes the three gaps that stop one clean funnel from search to booking. `checkout_complete` fires when the confirmation screen renders, so a booking is lost when the app closes first and counted twice when the guest reopens it from Trips. Dates arrive in three formats and money in two units.

This is the Data team's own `TRK` work. Nadia verifies each funnel event in `events-collector` as its squad ships it, moves the funnel dashboard to `booking_confirmed` and drops `checkout_complete` on its removal date. The client events and `booking_confirmed` ship under separate `FE` and `BE` tasks, and `date_changed` stays `proposed` until Search settles it.

**References**

---

Changed

- `Booking funnel tracking plan, draft v0.3, event table as agreed at the 2026-09-24 Booking squad refinement`

Impacted

- `Funnel dashboard, Data team space`

### Requirements

---

1.  **Verify each funnel event in `events-collector` as its squad ships it**

---

Each event is checked against its row once the owning squad ships it, so a step that reaches the collector with the wrong trigger or a missing property is caught before a dashboard reads it.

**Checklist**

- [] Each of `search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted` and `booking_confirmed` reaches `events-collector` on the trigger its row lists
- [] Every event carries the properties its row lists
- [] `room_type_id`, `rate_plan_id`, `total_amount_minor` and `currency` arrive from `room_selected` onward
- [] `payment_option` arrives on `payment_submitted` and `booking_confirmed`, and `booking_id` on `booking_confirmed`
- [] `check_in` and `check_out` arrive in `YYYY-MM-DD` on every step, with `nights` and `guests` beside them
- [] Every amount arrives as an integer in a `_minor` property with `currency` beside it, so a web step and an app step add up
- [] Client events carry `app_version`, `session_id`, `platform` and `locale`, and `booking_confirmed` joins them on `session_id` with `source` set to `server`
- [] A booking counts once from `booking_confirmed` alone, and reopening the confirmation from Trips adds no second count

---

2.  **Move the funnel dashboard to `booking_confirmed`**

---

Booking counts read `booking_confirmed` so the funnel has one booking step that survives an app closing before the confirmation screen draws. The move lands before `checkout_complete` stops reaching the collector.

**Checklist**

- [] Every booking count in the funnel dashboard reads `booking_confirmed` instead of `checkout_complete`
- [] Each step from `search_submitted` to `booking_confirmed` reports its count and the drop to the next step
- [] Revenue per step reports one total across iOS, Android and web
- [] The dashboard reads `booking_confirmed` before 2026-11-01
- [] Historic counts stay readable while the source moves, so a past date does not go blank

---

3.  **Drop `checkout_complete` in `events-collector` on 2026-11-01**

---

From the removal date the collector drops the event whatever app version sends it, so an app that has not updated cannot put a second booking count into a dashboard. The drop ships behind the dashboard move.

**Checklist**

- [] `events-collector` drops `checkout_complete` from 2026-11-01, whatever app version sends it
- [] The drop is live only after the dashboard reads `booking_confirmed`
- [] No dashboard, report or alert still reads `checkout_complete` after the drop
- [] An app below the current release sends `checkout_complete` without an error once the drop is live
```

Export-equivalent path: `export/002 - task-booking-funnel-verification-and-dashboard-cutover.md`

HVR self-scan: 0 hard blockers. Fixed: one em dash and one semicolon drafted in the About, rewritten as separate sentences, and the always-cut modifier "just" removed from the second checklist group. Kept with reason: `checkout_complete`, `booking_confirmed`, `events-collector`, `YYYY-MM-DD`, `_minor` and `proposed` kept verbatim as identifiers and status words from the tracking plan, and the plan's own "counted twice" wording.

Quality status: all six dimensions at 8+. Source fidelity holds every event, property and date the table supplies, and the scope boundary that keeps the client events, `booking_confirmed` and `date_changed` out of this task.

Two things to check before this goes out. The surface in the title is my call, since `TRK` spans all three surfaces and the funnel is guest-facing, so change Guest app if the Data team files under a different one. The requirement that historic dashboard counts stay readable through the move is my addition, not something you or the plan supplied, and you can strike it if the funnel only reads forward.

Next step: send the ClickUp push approval if you want this created, or tell me the two changes above and I will reissue the block.