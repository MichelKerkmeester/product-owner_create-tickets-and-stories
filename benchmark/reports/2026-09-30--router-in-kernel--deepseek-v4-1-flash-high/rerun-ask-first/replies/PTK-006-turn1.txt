```markdown
I'll create the task. Before I draft, confirm the points below in one reply.

**1. Which events**

The plan lists eight events. Which of them does this task cover?

- `search_submitted` and `property_viewed`, changed, live today
- `room_selected`, `checkout_started` and `payment_submitted`, new, sent from the client
- `booking_confirmed`, new, sent by `booking-service`, and the event every booking count should use
- `checkout_complete`, deprecated, dropped by `events-collector` on 2026-11-01
- `date_changed`, proposed, with its trigger left open with Search, one event per pick or one when the range is applied

**2. How it splits**

The plan's Who builds what puts the client events with the apps and web, `booking_confirmed` with the Booking squad in `booking-service`, and the funnel dashboard move with the Data team. Is this one task, one parent task with those as subtasks, or a task for the client events only?

**3. Title, discipline and code**

House titles read `{Discipline} - {Surface} - {Feature code} - {Title}`. Should this one carry `TRK`, since analytics events and the tracking plan sit there, or the code of the area each event changes, `SRCH`, `PROP`, `BOOK` or `PAY`? Confirm the discipline and the surface as well.

**4. Draft status**

The plan is draft v0.3, and comments stay open until the Booking squad refinement on 2026-09-24, so an event row or a property can move. Do I write the task against the draft as it stands, or wait until the comments close?

**5. Validation**

Beyond the values the plan fixes, what must QA check before this is done, and which squad picks the task up? Tell me too what I am likely to assume wrongly about the scope or the owner.
```

Export-equivalent path: `export/001 - task-booking-funnel-tracking-events-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: still, just (always-cut modifiers). Kept with reason: the source's event names, status words and dates in backticks, and its own Who builds what label, all carried as the plan writes them.

Quality status: routed to the task lane at Standard energy and held at Interactive intake. The escalation is about scope rather than source quality. The tracking plan is internally consistent and dated, but it fixes eight events across three owners, marks one `proposed` with an open trigger question and one `deprecated` with a removal date, and gives no boundary for a single task.

I did not decide the scope, the owner split or the title code, and I left `date_changed` out of any draft rather than promote a `proposed` row into agreed work. Two related notes: the date picker design notes record that date selection is not tracked and that work adds nothing, and the free cancellation notes record no tracking plan change, so neither belongs in this task.

Answer the five points and the task itself comes next as its own deliverable.