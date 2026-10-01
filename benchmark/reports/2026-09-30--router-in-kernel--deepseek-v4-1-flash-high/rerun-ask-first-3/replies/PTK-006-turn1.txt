```markdown
# Booking funnel tracking events - clarification

Please settle the decisions below in one reply and I'll write the task from your answers.

**1. Scope and owner lane**

The plan splits the work three ways: the client events for iOS, Android and web, `booking_confirmed` in `booking-service` for the Booking squad, and the funnel dashboard move off `checkout_complete` for the Data team before 2026-11-01.

- Which lane should this task carry, or does it need one task per lane?
- Should it be one task, or a parent task with a subtask per lane or per platform?

**2. Event set**

Two rows are not settled work:

- `date_changed` is `proposed`, has no properties agreed yet beyond the common ones and the dates, and the open point is whether it fires once per tap in the picker or once when the new range is applied
- `checkout_complete` is `deprecated`, keeps firing next to `booking_confirmed` until 2026-11-01, and `events-collector` drops it from that date

- Do both belong in the task, or should the task name them as an exclusion?

**3. Title lane**

The title convention is `{Discipline} - {Surface} - {Feature code} - {Title}`.

- Which discipline and which feature code should the title take once the lane above is set?

**Validation**

- What should I not assume about the lanes, the event set or the platform split?
```

Export-equivalent path: `export/001 - task-booking-funnel-tracking-events-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the backticked event, service and status names, which the source supplies and which stay written as it writes them.

Quality status: one consolidated question, every unresolved decision listed once, no draft or partial artifact rendered ahead of your answer.

Why this came back as a question rather than a task. The plan's own "Who builds what" assigns the funnel work to three owners, so the task's lane, its surface and the discipline in its title depend on a decision I should not make for you. Two event rows also cannot become requirements as they stand, because `date_changed` is `proposed` with its trigger still open with Search, and `checkout_complete` is a `deprecated` event whose removal belongs to the Data team's `events-collector` on 2026-11-01. The plan is also a draft v0.3 with comments open until the Booking squad refinement on 2026-09-24.

If you would rather I choose, say so and I will take the client lane for iOS, Android and web, name those two rows as exclusions, and title the task for that lane. Answer the three fields in one reply and the task comes next.