```markdown
# Booking funnel events task - intake questions

The plan spans events that three different owners build, so I need the scope settled before I draft. Please answer these in one response.

**Scope and owner**

- Which events the task covers: the client events on the Guest app, `booking_confirmed` in `booking-service`, or the whole funnel as a parent task with subtasks
- Which squad picks it up, and the discipline and feature code its title carries under `{Discipline} - {Surface} - {Feature code} - {Title}`
- Whether the Data team's dashboard move off `checkout_complete` belongs in this task

**Events the plan leaves open**

- Is `date_changed` in scope, or does it wait until Search settles one event per tap against one when the new range is applied
- Is the `checkout_complete` removal part of this task, given `events-collector` drops it on 2026-11-01 whatever app version sends it
- Does the plan's draft status hold the work back, with comments closing at the Booking squad refinement on 2026-09-24

**Acceptance**

- What proves the events work: arrival in `events-collector` with the listed properties, revenue adding up in minor units across platforms, or dates arriving as `YYYY-MM-DD`
- Must each platform verify its own events before the task closes

**What I should not assume**

- Which parts of the plan are likely to change before the refinement
- Whether the Android price call, which the app needs before it can send `total_amount_minor`, should block the task
```

Export-equivalent path: `export/001 - task-booking-funnel-events-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: supplied identifiers kept verbatim in backticks, including `booking_confirmed`, `booking-service`, `date_changed`, `checkout_complete`, `events-collector`, `total_amount_minor` and `YYYY-MM-DD`, with the removal date `2026-11-01` and the refinement date `2026-09-24` kept as supplied.

Quality: one consolidated question covering scope, owner, the plan's open events and acceptance, with the draft status and the unsettled `date_changed` trigger raised rather than guessed. The plan is a draft v0.3 that three owners build parts of, and one event has an open question, so scope and acceptance are the fields I could not infer.

What I assumed, so you can strike it: that "booking funnel events" means the events from `search_submitted` through `booking_confirmed`, that one task is wanted rather than a parent task with subtasks, and that the plan's draft status is a real gate on build work.

Once you answer, the task comes next.