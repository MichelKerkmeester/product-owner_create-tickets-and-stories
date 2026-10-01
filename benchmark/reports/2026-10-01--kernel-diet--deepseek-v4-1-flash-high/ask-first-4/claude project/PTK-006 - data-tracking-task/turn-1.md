```markdown
# Booking funnel events, task clarification

## What I need before drafting

---

I can write this from Nadia's tracking plan once the points below are settled, because each one changes the task's scope or its checklist.

**1. What the task covers**

The plan splits the work across three owners. The client events run on iOS, Android and web together, so the apps and web are one front end change. `booking_confirmed` is server side in `booking-service`, while the funnel dashboard and the retirement of `checkout_complete` sit with the Data team.

The client events are `search_submitted` and `property_viewed`, both changed, plus the new `room_selected`, `checkout_started` and `payment_submitted`.

- Does one task cover the client events alone?
- Does it cover the whole funnel, client and server events together?
- Is it a parent task with a subtask per owner, and if so which children?
- Does the retirement of `checkout_complete` on 2026-11-01 belong here or in a task of its own?

The title also needs a discipline and a feature code. I read two candidates in the conventions, `TRK` for tracking events and `BOOK` for the checkout funnel, since a piece of work takes the code of the area it changes. Which applies?

**2. The plan's own open points**

The plan is draft v0.3, shared with the Booking and Search squads for comments that close on 2026-09-24.

One event is unsettled: `date_changed` is `proposed`, and whether it fires per tap in the picker or once when the range is applied is still open with Search. `checkout_complete` is `deprecated` and keeps firing beside `booking_confirmed` until 2026-11-01.

- Is the task built from the draft as it stands?
- Is `date_changed` in scope, and how should the task carry the open decision?
- Or should I wait until the refinement closes on 2026-09-24?

**3. Acceptance criteria**

What tells you the task is done? These are the checks I would write from the plan, so correct any that are wrong:

- Every event in scope fires with the properties the plan lists for it
- `total_amount_minor` and `currency` travel from all three platforms, replacing the web's decimals
- `check_in` and `check_out` travel as `YYYY-MM-DD` on every event in the funnel, with `nights` and `guests`
- `room_selected` may fire once the price call returns, as Nadia confirmed on 2026-09-15, rather than on the tap
- `checkout_complete` is no longer depended on before 2026-11-01

**4. References and platform coverage**

The task would name the tracking plan in References, so tell me what else to carry:

- Any dashboard, ticket or Figma links?
- All three platforms in one release, or does the web ship on its own?
- Which related tickets sit in the Booking, Search and Data squads?
- What am I likely to assume incorrectly about the guest flow this funnel follows?
```

Export-equivalent path: `export/001 - task-booking-funnel-events-clarification.md`

Routed as Task Mode from clear task framing, with `context/roamstay-booking-funnel-tracking-plan.md` as the source and `context/roamstay-context.md` for conventions. No task is drafted yet, because the request leaves scope, acceptance criteria and the plan's own unresolved points open. The plan is draft v0.3, `date_changed` is `proposed` with an unanswered question about when it fires, and the eight events span three owners, so a single task cannot cover them without a decision from you. Answer the questions above in one reply and the task follows next in the task lane.

Assumptions I made, so you can correct them: this is a new task rather than a refinement of an existing one, and the source is the draft v0.3 file you named.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `proposed` and `deprecated` as the plan's own status words for `date_changed` and `checkout_complete`; `check_in`, `check_out`, `total_amount_minor`, `currency`, `YYYY-MM-DD`, `2026-09-24` and `2026-11-01` as supplied identifiers, values and dates; `-` bullets rather than the ClickUp `*   ` grammar, because this is a task-lane clarification and not a new Doc.