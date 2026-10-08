```markdown
Thanks. This answers the source, owner and scope. The earlier clarification stands, and I still need the points below in one reply before drafting.

**Confirmed so far:**
- Source: v0.3 stands, since the refinement closed on 2026-10-07 with no change to the event table
- Owner: the Data team, under `TRK`, discipline `DATA`
- Scope: check each event in `events-collector` as the squads ship it, move the funnel dashboard to `booking_confirmed`, and have the collector drop `checkout_complete` on 2026-11-01
- Out of scope: the client events and `booking_confirmed` itself, which get their own FE and BE tasks later

**Date_changed:** The table is unchanged, so `date_changed` is still proposed and its firing rule is still open. Should this task check it, or leave it out? If it is in, which rule applies: one event per tap in the picker, or one when the new range is applied?

**Proposed acceptance criteria:** Confirm, change or add to these:
- Each event that reaches `events-collector` matches its row in the plan for trigger, properties and types
- Dates arrive as `YYYY-MM-DD`, and money arrives as an integer in minor units with `currency` beside it
- `booking_confirmed` arrives with `source` set to `server`, and its `session_id` and `app_version` match the checkout request
- The funnel dashboard counts bookings from `booking_confirmed` only
- `events-collector` drops `checkout_complete` from 2026-11-01, whatever app version sends it

**Surface:** The title would read `DATA - Guest app - TRK - {title}`. Is Guest app the right surface?

**Target date:** The plan requires the dashboard move and the collector drop before 2026-11-01. Is there an earlier date this task must meet?

**Validation:** I am assuming the checks run against what arrives at `events-collector`, not against the apps' code. Is that right?
```

Export-equivalent path: `export/NNN - task-booking-funnel-events-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Your answers settle the owner, scope and source. The draft still waits on the `date_changed` decision, the acceptance criteria, the surface and the target date. The task follows as a new Deliverable Block once you answer.