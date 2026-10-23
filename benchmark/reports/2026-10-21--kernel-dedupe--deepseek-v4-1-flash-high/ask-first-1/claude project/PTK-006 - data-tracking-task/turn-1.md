```markdown
# Booking funnel tracking events: intake

Nadia's plan already settles the triggers, the property names and types, and the status of all eight event rows, so the acceptance basis is there. Four things decide the task's scope, and I need them in one reply.

**1. Scope and build owner**
The plan splits the work three ways: client events on iOS, Android and web, `booking_confirmed` in `booking-service` for the Booking squad, and the dashboard move for Data.
Recommendation: one task for the five client events, `search_submitted`, `property_viewed`, `room_selected`, `checkout_started` and `payment_submitted`, titled `FE - Guest app - TRK - Booking funnel tracking events`. Those five are the funnel a guest walks, and the plan puts every client event on the three surfaces together, so one task carries one acceptance basis. `booking_confirmed` and the dashboard move sit as linked dependencies.
Say so instead if you want the server event inside the task, or one task per surface.

**2. `date_changed`**
Tomas asked for the event and Nadia added the row as `proposed`, with the trigger still open: one event per tap in the picker, or one when the new range is applied. The plan agrees no properties for it beyond the common ones and the dates.
Recommendation: leave it out of this task, because a `proposed` row with an unsettled trigger and no agreed properties means inventing both. It becomes its own task once Search picks the trigger.

**3. Properties on the two live events**
The property table puts `check_in`, `check_out`, `nights`, `guests` and `rooms` on every event, while the notes say `search_submitted` and `property_viewed` gain `nights` and `guests`.
Recommendation: apply the table, so both events send all five, because the table is the list a squad builds from and QA needs one answer. Tell me if `rooms` is already live on both and should stay out of the change.

**4. Cut-over and app version floor**
`checkout_complete` keeps firing until `2026-11-01`, when `events-collector` drops it. The apps ship on a two-week train, Android rolls out over 5 days, and versions down to `8.6.0` stay live until the forced update screen hits.
Recommendation: hold the removal as a Data dependency with `2026-11-01` as the constraint, and make the task state the lowest app version that carries the new events so the funnel can filter on it. Without that floor, a client that has not updated still sends the old date formats.
```

Export-equivalent path: `export/001 - task-booking-funnel-tracking-events-clarification.md`
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality: not scored, clarification only | Kind: Task | Energy: Standard

The question has four parts: which events and which squad the task owns, whether `date_changed` waits, which of the five stay properties the two live events send, and how the `checkout_complete` cut-over and the app version floor are set. Everything else the task needs is already in the plan, including the `_minor` money convention and the common-property list.

### Open items
None identified

Answer in one message and I'll draft the task.