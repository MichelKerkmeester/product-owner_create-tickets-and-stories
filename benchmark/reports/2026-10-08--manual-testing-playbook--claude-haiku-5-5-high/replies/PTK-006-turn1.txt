```markdown
Before I write the booking funnel task, I need the answers below in one reply.

**Source version:** The plan is v0.3, last edited on 2026-09-15, and its comments closed on 2026-09-24. Is v0.3 the version to build from, or did the Booking refinement change it? If it changed, please share the newer version.

**Scope:** Which events go in this task?
- The six events marked new or changed: `search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted` and `booking_confirmed`
- `date_changed`, which is still proposed. Its firing rule is open in the plan (one event per tap in the picker, or one when the new range is applied), and it has no agreed properties. Include it or leave it out?
- Removing `checkout_complete` from the client before 2026-11-01. In or out?
- Settled in the comments and not asked again: `room_selected` fires once the price is known.

**Split and owner:** The apps and web build the client events. The Booking squad builds `booking_confirmed` in `booking-service`. Should this be one task or one task per squad? Which discipline code applies: `DATA`, `FE` or `BE`?

**Platforms:** iOS, Android and web, or a subset?

**Acceptance criteria:** How will we know each event is done? Each row of the plan (trigger, properties, status), a separate check per event, or both?

**Dates and dashboard:** The plan's only date is the removal of `checkout_complete` on 2026-11-01. Is the funnel dashboard move to `booking_confirmed` part of this task? Is there any other date the task must meet?

**Validation:** I am assuming `booking_confirmed` replaces `checkout_complete` for every booking count, and that a Pay at property booking counts as confirmed when it is created. Should I challenge either of these?
```

Export-equivalent path: `export/NNN - task-booking-funnel-events-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

I have not drafted the task yet. The plan leaves the `date_changed` firing rule open, and the scope, owner and acceptance criteria are not set, so a draft now would invent them. Once you answer, the task follows as a new Deliverable Block.