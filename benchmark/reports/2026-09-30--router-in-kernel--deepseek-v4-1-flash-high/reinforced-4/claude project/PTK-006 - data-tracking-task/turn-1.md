```markdown
I'll create your task. Quick questions:

**Scope:** Of the plan's eight events, which are in this task: the seven client ones, `booking_confirmed` in `booking-service`, or the Data dashboard move?

**One task or several:** One task for the whole set, or a parent task with a subtask per event, platform or squad?

**Proposed and deprecated rows:** Is `date_changed` in scope while `proposed`, and does the task cover removing `checkout_complete` on 2026-11-01?

**Title and owner:** Which squad takes this, and does the title carry `TRK` or the code of each surface it changes?

**Requirements and acceptance:** Do the plan's three named problems define the acceptance bar, and is anything else required when this ships?

**Dependencies:** Anything to link for the `booking_confirmed` change, the dashboard migration, or comments closing at the 2026-09-24 refinement?

**Validation:** Is the plan approved to build from at draft v0.3, and does "booking funnel" cover the guest-facing steps only?
```

Export-equivalent path: `export/001 - task-booking-funnel-events-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the intake question's bold-header bullets, which the interactive intake template fixes as its shape; the source identifiers `booking_confirmed`, `date_changed`, `checkout_complete`, `TRK` and the status word `proposed` in backticks, as the tracking plan writes them.

Quality: every unresolved field for the task is asked once in one question, with the five Interactive dimensions checked on the question itself. No draft attempted, so the task gate and voice pass have not run yet.

Two things held the draft back. The plan's eight events split across three builders, so "a task" could be one task, a parent with subtasks, or the client events alone, and guessing that wrong wastes the artifact. And `date_changed` still carries `proposed` status with no agreed properties while its open point on tap versus applied range sits with Search.

I read your request as covering the plan's event set rather than the client events only, and I treated the draft as input rather than an approved spec. Correct me on either and the scope answer changes.

Answer the questions and the task comes next as a new block in this lane, taking the next number.