```markdown
# Task - Booking funnel tracking events - clarification

I'll create your task. Two things in the plan need your decision first: the work is drafted across three different builders, and one event is still open.

**Format & scope:** Which rows does this task cover?

- The rows divide by builder. The client events go to the apps and web together, `booking_confirmed` goes to the Booking squad in `booking-service`, and the funnel dashboard goes to the Data team. A task carries one discipline code and one squad, so is this one task for the client events, one task per event, or a parent task with subtasks?
- The rows also divide by status: `changed` (`search_submitted`, `property_viewed`), `new` (`room_selected`, `checkout_started`, `payment_submitted`, `booking_confirmed`), `deprecated` (`checkout_complete`, removal on 2026-11-01) and `proposed` (`date_changed`). Does the task cover all four statuses, or only the rows the squads have agreed to build?

**Requirements and done:** What must be true when this task is finished?

- Each event fires on the trigger in its row, carries its listed properties, and is checked in `events-collector`?
- The three problems under "Why we're redoing this" are closed: no booking lost when the app closes before the confirmation screen draws and none counted twice when the guest reopens it from Trips, web amounts sent as minor units, and dates in `YYYY-MM-DD` on every step?
- The funnel dashboard has moved from `checkout_complete` to `booking_confirmed`, and `checkout_complete` stops reaching `events-collector` on 2026-11-01?

**Open decision:** `date_changed` is still `proposed`.

- Nadia's open point on 2026-09-12 is whether it fires once per pick in the date picker or once when the new range is applied, and she left it to settle with Search. Do I leave `date_changed` out until that is settled, or include it with the chosen behaviour written in?
- The plan is draft v0.3 and comments close at the Booking squad refinement on 2026-09-24. Do I write the task against the draft as it stands, or only against rows already agreed?

**Platform and references:** Client events on iOS, Android and web together, as "Who builds what" states? Any existing ticket, parent task or events-collector reference the task should link?

**Dependencies:** `booking_confirmed` is built in `booking-service` by the Booking squad, and the `checkout_complete` removal depends on the dashboard move. Should both sit as dependencies in the task, or does this task wait on either one?

**Validation:** I would otherwise assume all three funnel problems are this task's to fix, that Oskar's answer settles `room_selected` timing on Android (send it once the price call returns), and that the amount fix means the web switches to minor-unit integers. What am I likely to get wrong?
```

Export-equivalent path: `export/001 - task-booking-funnel-tracking-events-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `events-collector`, `booking_confirmed`, `checkout_complete`, `_minor` and `YYYY-MM-DD` kept verbatim as event, service and notation identifiers from the tracking plan, and the two quoted plan headings kept as the source writes them.

Quality status: the intake question meets the Interactive thresholds (clarity, completeness, assumption challenge, perspective diversity, mechanism depth, each 8+). The task itself is not drafted yet, because scope, acceptance criteria and the open `date_changed` decision are unresolved.

Two points drove the question rather than a draft. The plan assigns one funnel to three separate builders, so a single task cannot carry one discipline code without your call on the split. And `date_changed` carries an explicit open point in the comments, so writing it into the task would mean inventing a decision Search has not made.

Answer the points above in one response and the task comes next. If you want a lean pass on the rows you already consider settled, add `$quick` and tell me which rows those are.