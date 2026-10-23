```markdown
# Task intake: booking funnel events

The plan splits this work across three owners, so scope comes first. I read `draft v0.3` and the Roamstay context. Answer the five points below in one message and I will draft the task.

**1. Which events does the task cover?**

- What the plan shows: eight rows in the Events table, and a `Who builds what` section that gives the client events to apps and web, `booking_confirmed` to `booking-service` under the Booking squad, and the funnel dashboard to the Data team
- Recommended: the five client events on the funnel path, `search_submitted`, `property_viewed`, `room_selected`, `checkout_started` and `payment_submitted`
- Why: the plan ships those together on iOS, Android and web, and the other three carry different owners

**2. Do `booking_confirmed` and the `checkout_complete` removal belong in the same task?**

- What the plan shows: `booking_confirmed` is a server event from `booking-service`, and `checkout_complete` keeps firing until `2026-11-01`, when `events-collector` drops it
- Recommended: leave both out and cover them as separate Booking and Data tasks
- Why: neither is client work, and one ticket cannot name two signing squads

**3. Is `date_changed` in scope?**

- What the plan shows: status `proposed`, no properties agreed beyond the common ones and the dates, and Nadia's open point on whether it fires per picker tap or when the new range is applied, to settle with Search
- Recommended: leave it out until that trigger question is settled
- Why: a build cannot test an event whose firing rule and property set are both still open

**4. One task, or a parent task with a subtask per platform?**

- Recommended: one task covering iOS, Android and web together, titled `FE - Guest app - TRK - Booking funnel events`
- Why: the plan ships the client events as one change, and `TRK` is the tracking area

**5. How should the task ask QA to verify the events?**

- What the plan shows: events arrive at `events-collector`, and money travels as an integer in minor units with `currency` beside it
- Recommended: acceptance criteria read from the Events and Properties tables, with `events-collector` named as the place QA confirms each event and its properties
- Why: the plan's tables already hold the testable set, so the task does not need to invent criteria
```

Export-equivalent path: `export/NNN - task-booking-funnel-events-clarification.md`
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality: not scored, clarification only | Kind: Task | Energy: Standard

The question has five parts: which events the client task owns, whether the server event and the deprecated event belong in it, whether `date_changed` is included while its trigger is open, the title code, and how QA verifies each event. The task comes next once you answer.

### Open items
None identified

Answer in one message and I'll draft the task.