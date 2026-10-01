```markdown
# Booking funnel events task clarification

I'll write the task for the booking funnel events in Nadia's tracking plan. Before drafting, I need these decisions in one response.

**0. How should I work this?**

- Quick - a lean pass with smart defaults and minimal back-and-forth
- Deeper - take more time, read more context and apply the full phase flow

**1. Scope - which events this task covers:**

- The client events only, `search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted`, `checkout_complete` and `date_changed`, as one task for iOS, Android and web together
- The client events plus `booking_confirmed`, which `booking-service` sends
- A parent task for the whole funnel with a child task per owner: the client events, `booking_confirmed` in `booking-service`, and the Data team moving the dashboard off `checkout_complete`

**2. Title code:** the conventions title a task `{Discipline} - {Surface} - {Feature code} - {Title}`. For client instrumentation on the Guest app, which do you want?

- `FE - Guest app - TRK - ...`
- `DATA - Guest app - TRK - ...`
- another discipline, surface or code, since the events sit across search, the property page and checkout

**3. `date_changed`:** the plan marks it `proposed`, and it leaves one open point, whether it fires per tap in the picker or once when the new range is applied.

- Include it in this task as a proposed item with the open point named
- Leave it out until Search settles that point

**4. `checkout_complete`:** it keeps firing until its removal date of 2026-11-01, after which `events-collector` drops it.

- This task also keeps it firing beside `booking_confirmed` until 2026-11-01
- This task owns only the new and changed events, and the removal is a separate task

**5. Platforms:** the client events are built on iOS, Android and web together. Android sends `room_selected` once the price call returns rather than on the tap.

- One task covering all three
- One task per platform, following the subtask template

**6. Validation:** what am I likely to assume incorrectly? One point to settle either way is whether the plan's v0.3 content is final for this task now, or whether the task waits for the Booking squad refinement on 2026-09-24.
```

Export-equivalent path: `export/NNN - task-booking-funnel-events-clarification.md`

Quality status: pass. The question carries only the decisions the plan leaves open, so one answer unblocks the task. Scope is first because the plan's three owners cannot sit in one buildable task.

HVR self-scan: 0 hard blockers. Fixed: hyphens used in bullet leads instead of em dashes. Kept with reason: event names, `events-collector`, `booking-service`, status words `proposed` and the 2026-11-01 date, all literal identifiers and supplied values from the tracking plan.

What I read the request as, so you can correct me: Task intent at Standard energy, with `context/roamstay-booking-funnel-tracking-plan.md` as the source for event rows, properties and statuses, and `context/roamstay-context.md` for the title convention and feature codes. The plan holds eight event rows across three owners, so scope and title code are the two decisions I will not guess.

Answer the six points and I'll draft the task next, taking the next number in the task lane.