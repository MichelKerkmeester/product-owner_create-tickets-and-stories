```markdown
# Task intake: booking funnel events

## What the plan already settles

I will carry these into the task unless you correct one.

- The client events ship on iOS, Android and web together, since the conventions read Guest app with no platform as all three
- `search_submitted` and `property_viewed` keep firing, and their work is the date format plus `nights` and `guests`
- `room_selected`, `checkout_started` and `payment_submitted` are new client events
- `room_selected` fires after the Android price call returns, per Nadia's reply to Oskar
- `checkout_complete` needs no client change, because `events-collector` drops it on 2026-11-01
- The funnel dashboard move belongs to the Data team, so it stays out of the task

## What I need from you

**1. Scope and owner:**
The plan splits this work three ways. The client events go to the apps and web together, `booking_confirmed` goes into `booking-service` under the Booking squad, and the dashboard goes to the Data team.

I recommend the client events as one task, titled `FE - Guest app - TRK - Booking funnel events`. A title carries one discipline, one surface and one feature code, so the server event cannot share it, and `BOOK` or `PAY` would each name only part of the funnel.

**2. `date_changed`:**
The plan marks it `proposed`, and Nadia's comment leaves its trigger open: one event per picker tap, or one when the new range is applied.

I recommend leaving it out and naming it in the task as waiting on Search, because a requirement with an unsettled trigger cannot be checked off.

**3. Building from a draft:**
The plan is draft v0.3 and comments close at the Booking refinement on 2026-09-24.

I recommend building from the rows as written, because each row already carries its own `new`, `changed`, `deprecated` or `proposed` status.
```

Export-equivalent path: `export/NNN - task-booking-funnel-events-clarification.md`
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality: not scored, clarification only | Kind: Task | Energy: Standard

The question has three parts: which slice of the plan the task covers, whether `date_changed` belongs in it, and whether to build from draft v0.3 now. The scope is the one that blocks the rest, because the plan splits client events, the server event and the dashboard across three owners. Once you answer, the task follows the guest app events with their triggers, properties and statuses intact.

### Open items
None identified

Answer in one message and I'll draft the task.