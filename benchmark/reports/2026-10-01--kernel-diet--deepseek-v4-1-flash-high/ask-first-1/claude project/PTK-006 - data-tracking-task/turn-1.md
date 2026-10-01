```markdown
# Booking funnel events task - clarification

I will draft the task once five points are settled. The plan carries eight events across three builders, and one of them is still an open decision, so scope is the one I cannot infer.

**Scope - which events the task carries:**
The plan's "Who builds what" puts the eight events with three different owners.
- Client, built by apps and web together on iOS, Android and web - `search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted`
- Server, built by Booking squad in `booking-service` - `booking_confirmed`
- Deprecated, dropped by `events-collector` on `2026-11-01` - `checkout_complete`
- Proposed, with no properties agreed yet - `date_changed`
- Which set does the task cover, and is it one task or a parent task with a subtask per builder?

**Title and surface:**
Titles read `{Discipline} - {Surface} - {Feature code} - {Title}`, one discipline and one surface each.
- Discipline - `DATA`, `FE`, `FS` or `BE`?
- Surface - Guest app, Back office for the dashboard move, or both?
- Feature code - `TRK`?
- What title should it carry?

**Open decisions in the plan:**
- `date_changed` is still open on one event per picker tap versus one when the new range is applied.
- Include it, with the behavior Search settles, or leave it out of this task?
- Does the task cover the `2026-11-01` removal of `checkout_complete` and Data's dashboard move to `booking_confirmed`?
- Is the draft approved to build from, or does the task wait for comments closing at the Booking refinement on `2026-09-24`?

**Requirements and acceptance:**
The plan already gives each event's trigger, its properties and its status.
- Beyond those events firing with the listed properties and the common properties, what does success look like?
- Anything to exclude, and any property to treat as fixed for a later change?

**References and dependencies:**
- Any parent task, related ticket, Figma link or ClickUp link to carry in References?
- Anything I should not assume about sequencing between the client events and `booking_confirmed`?

Answer these in one reply and the task comes next.
```

Export-equivalent path: `export/001 - task-booking-funnel-events-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: the `**Header:**` intake lines and the multi-line bullet structure follow the Task Format Question in Assets - Interactive Response Templates, which sanctions that shape; the backticked event names, property names, dates and status words are carried from the tracking plan verbatim.

Quality: clarification clarity, completeness, assumption challenge, perspective diversity and mechanism depth all sit at or above the 8 threshold. Detected Task Mode from the request's own `write a task` framing, and routed to Interactive Mode's Task Format Question before drafting, because scope, title and acceptance conditions are not resolvable from the plan alone.

Summary: the tracking plan is rich on per-event detail, but a single task cannot be titled or scoped from it as written. Its eight events sit with three builders (`booking-service` for the server event, apps and web for the client events, Data for the dashboard), the house title carries one discipline code and one surface, `date_changed` is still `proposed` with an open decision Nadia is holding for Search, and `checkout_complete` is `deprecated` rather than build work. The block above asks for all of it in one reply, so no second round is needed. The task itself takes the next number in the lane once you answer.