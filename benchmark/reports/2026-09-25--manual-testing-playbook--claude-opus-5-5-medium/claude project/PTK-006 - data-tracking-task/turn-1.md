```markdown
# Booking funnel events task: questions before drafting

Nadia's tracking plan (draft v0.3) covers most of what the task needs. Six decisions change what goes into the task or who owns it. Please answer them in one reply.

**1. One task or one per builder?**
- The plan's "Who builds what" section splits the work three ways. Apps and web build the client events. The Booking squad builds `booking_confirmed` in `booking-service`. The Data team moves the funnel dashboard
- A task title carries one discipline code (`{Discipline} - {Surface} - {Feature code} - {Title}`), so one task can't hold the client and server work cleanly
- Which do you want?
  - (a) `FE - Guest app - TRK - Booking funnel events` for the client events on iOS, Android and web
  - (b) a `BE` task for `booking_confirmed`
  - (c) a parent task linking both, plus the Data dashboard task
  - (d) something else

**2. Is v0.3 the final plan?**
- Comments closed at the Booking squad refinement on 2026-09-24. Was the plan approved there as written?
- If anything changed at that meeting, please send the updated version or list the changes

**3. `date_changed`**
- It is still proposed, and one point is open: fire once per tap in the picker, or once when the new range is applied
- My default is to leave it out of the task. Should it go in, and if so, with which trigger?

**4. When `room_selected` fires**
- Nadia agreed that Android can send `room_selected` once the price call returns, instead of on the tap. The event table still says "The guest picks a room type and rate plan"
- Does "send it once the price is known" apply to iOS and web too, or only to Android?

**5. Common properties on `booking_confirmed`**
- The plan puts `app_version`, `session_id`, `platform`, `locale` and `source` on every event. The note for `booking_confirmed` says `booking-service` copies only `session_id` and `app_version` from the checkout request
- Should `booking_confirmed` also carry `platform` and `locale`, or does it go without them?

**6. `checkout_complete` until 2026-11-01**
- The property table puts `check_in`, `check_out`, `nights`, `guests` and `rooms` on "every event in the table", which includes the deprecated `checkout_complete`
- Should it gain those properties, or keep firing unchanged until `events-collector` drops it?
- Is there a ClickUp link for the tracking plan, or a parent task or epic, that the task should reference?
```

Export-equivalent path: `export/001 - task-booking-funnel-events-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

I haven't written the task yet because six questions in the plan change what it should contain. The biggest one is question 1. The plan splits the build between the apps and web, the Booking squad and the Data team, but a task title can only carry one discipline code. So one task covering everything would clash with your naming conventions in `roamstay-context.md`.

The other questions are gaps or disagreements inside the plan itself:

- **`date_changed`:** its trigger hasn't been agreed yet.
- **`room_selected`:** the table and the comment thread give different times for when it fires.
- **`booking_confirmed`:** it doesn't get all the standard properties that every other event gets.
- **`checkout_complete`:** the plan's wording would add the new date properties to this retired event.

Once you answer, I'll write the task and save it as the next file in the task folder.