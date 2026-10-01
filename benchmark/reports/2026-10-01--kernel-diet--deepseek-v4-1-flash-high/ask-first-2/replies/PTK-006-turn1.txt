```markdown
# Booking funnel events - task clarification

I'll draft the task once one response settles the scope below.

**Event scope:**

- Which rows of the plan's event table this task covers: all eight, the five client funnel events, or the client events plus `booking_confirmed`
- Whether `checkout_complete` is in scope for its removal on 2026-11-01, or out of scope because it only keeps firing until that date

**Ownership and shape:**

- One task, a parent task with a subtask per owner, or three separate tickets for the owners in the plan's `Who builds what` section
- Which discipline, surface and feature code the title carries, since the client events span iOS, Android and web and `booking_confirmed` comes from `booking-service`
- Whether one task covers iOS, Android and web together or splits per platform

**Data fixes:**

- Whether the web amount format moving from decimals to integer minor units is part of this task
- Whether `search_submitted` and `property_viewed` move their dates to `check_in` and `check_out` in `YYYY-MM-DD` in this task

**Dashboard:**

- Whether the funnel dashboard moving from `checkout_complete` to `booking_confirmed` before 2026-11-01 sits in this task or stays with the Data team

**`date_changed`:**

- The row is `proposed`, with the trigger still open between one event per picker tap and one event when the new range is applied
- Whether the task carries it with that decision open, holds it until Search settles it, or leaves it out

**Plan status:**

- The plan is draft v0.3, with comments closing at the Booking squad refinement on 2026-09-24
- Whether that draft is the agreed baseline for the task or the task waits for the refinement

**Validation:**

- What am I likely to assume incorrectly about which squad picks up this work and what follows it
```

Export-equivalent path: `export/001 - task-booking-funnel-events-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the event, property and status names (`checkout_complete`, `booking_confirmed`, `date_changed`, `search_submitted`, `property_viewed`, `check_in`, `check_out`) as literal identifiers the plan and the conventions supply, and the supplied dates 2026-09-24 and 2026-11-01.

Quality status: one consolidated question, every unresolved scope field covered in a single response, no draft and no self-answered point.

Routed: Task Mode, held at intake. The plan puts these events under three owners, so a single task cannot carry one honest discipline and feature code until you choose the shape. Two rows also arrive unfinished: `date_changed` is proposed with its trigger still open, and `checkout_complete` is deprecated with a removal date. The task comes next once you answer, and my assumptions are plain here so you can strike one: "the booking funnel events" means the plan's event table, and the plan is a draft rather than an agreed baseline.