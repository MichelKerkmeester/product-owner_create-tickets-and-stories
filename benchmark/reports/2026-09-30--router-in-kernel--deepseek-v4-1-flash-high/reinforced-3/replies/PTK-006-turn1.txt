```markdown
# Task intake for the booking funnel events

I'll create your task. Before drafting, I need the unresolved decisions below in one response:

**Which events:** The plan carries eight rows and three different owners under "Who builds what", so one task cannot cover the whole file. Which set does this task take?

- The client events on iOS, Android and web: `search_submitted`, `property_viewed`, `room_selected`, `checkout_started` and `payment_submitted`
- The same client set plus the `checkout_complete` deprecation path, which keeps firing beside `booking_confirmed` until 2026-11-01 and is dropped by `events-collector` from that date
- The server event `booking_confirmed` in `booking-service`
- All eight rows in one task across the surfaces
- Something else, such as the Data team's dashboard move off `checkout_complete`

**Ownership and title:** Is this one task across iOS, Android and web, or one per platform? Which squad owns it, and which feature code should the conventions' `{Discipline} - {Surface} - {Feature code} - {Title}` form carry: `TRK`, or the area each event changes, `SRCH`, `PROP` and `BOOK`?

**The open decision:** `date_changed` is `proposed` and its trigger is still open between one event per tap in the picker and one when the new range is applied, to be settled with Search before comments close on 2026-09-24. It also has no properties agreed beyond the common ones and the dates. Does the task include `date_changed`, and if it does, which trigger should the acceptance criteria state? Or does it stay out of scope until Search settles it?

**Source state:** The plan is draft v0.3 with comments open until 2026-09-24. Should the task carry the rows as drafted now, or only the rows the comments have settled?

**References and dependencies:** Any epic, parent task, ClickUp ticket or design link to go in References? Is a parent task with subtasks wanted rather than one task, given the three-way split of build work in the plan?

**Validation:** What should I not assume about the source? For example, may I treat the properties table as the final property list and the events table's "Fires when" column as the source of truth for each trigger, including Oskar's question settled in the comments on Android sending `room_selected` once the price call returns?
```

Export-equivalent path: `export/001 - task-booking-funnel-events-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: supplied identifiers, event names and status words (`search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted`, `booking_confirmed`, `checkout_complete`, `date_changed`, `events-collector`, `SRCH`, `PROP`, `BOOK`, `TRK`) kept verbatim as the sources write them.

Quality status: routing gate held and passed for intake. The request routes to Task intent with Standard energy, and a question delivery carries no draft for the six-dimension gate to score. Nothing is blocked on your side beyond the six items above.

Summary: your two sources agree on a lot, and the tracking plan is detailed enough to build from. What it does not settle is this task's boundary. The plan splits its build work across the apps and web, the Booking squad and the Data team, so the events, the owning squad and the title code have to be chosen rather than inferred. The `date_changed` row is the one live decision inside the source, and its trigger stays open until Search comments. Answer the six items in one response and I'll draft the task next in this lane, taking the number after this clarification.