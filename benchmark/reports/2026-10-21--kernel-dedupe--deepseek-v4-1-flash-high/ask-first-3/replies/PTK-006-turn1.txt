```markdown
# Booking funnel events task, four open decisions

The plan supplies the event names, triggers, properties and statuses, and the conventions supply the platform reading, the title format and the money format. Four things decide what the task covers, and the two sources leave each of them to you.

## 1. Which events the task covers

The plan's "Who builds what" splits this work three ways. Apps and web build the client events, the Booking squad builds `booking_confirmed` in `booking-service`, and the Data team moves the funnel dashboard off `checkout_complete`. The request names none of them.

Recommended: one task for the six client rows on the Guest app across iOS, Android and web, those being `search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted` and the `checkout_complete` window. `booking_confirmed` and the dashboard cutover then become their own tickets.

Reason: one owner builds the client events on three platforms together, so one ticket can carry them without splitting a release.

## 2. Whether `date_changed` is in scope

The row is `proposed`, raised in Tomas's comment, and Nadia's reply leaves the trigger open: one event per tap in the date picker, or one when the new range is applied. She parks the choice until Search weighs in, and comments close at the Booking refinement on 2026-09-24.

Recommended: leave it out of this task and raise it once Search settles the trigger.

Reason: every requirement here needs a trigger it can be tested against, and the source calls this one unsettled.

## 3. How far the `checkout_complete` removal goes

The row is `deprecated`, with removal on 2026-11-01, and from that date `events-collector` drops the event whatever app version sends it.

Recommended: the task makes the client send `booking_confirmed` beside it and adds nothing else, with the cut left to `events-collector` under the Data team.

Reason: the plan puts the drop at the collector, so the client has nothing to switch off on the date, though the event can be removed from the apps and web in a later cleanup ticket.

## 4. The title's discipline code

The conventions title a task `{Discipline} - {Surface} - {Feature code} - {Title}` and give `TRK` to analytics events, owned by Data. They also give `FE` to Guest app screens and `DATA` to tracking work, so either code fits the discipline slot.

Recommended: `FE - Guest app - TRK - Booking funnel client events`.

Reason: the plan hands the client events to the apps and web, which is `FE` work even though the area is `TRK`. Use `DATA` if you want the Data team to own the ticket end to end.
```

Export-equivalent path: `export/001 - task-booking-funnel-events-clarification.md`
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality: not scored, clarification only | Kind: Task | Energy: Standard

The question covers which of the plan's three owners the task follows, whether the `proposed` `date_changed` row can be built yet, how far the `checkout_complete` deprecation reaches, and which discipline code the title takes. The task comes next once you answer.

### Open items
None identified

Answer in one message and I'll draft the task.