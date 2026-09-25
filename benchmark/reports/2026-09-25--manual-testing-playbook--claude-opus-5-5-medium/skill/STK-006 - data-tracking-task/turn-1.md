I haven't written the task yet. Nadia's plan leaves some decisions open and contradicts itself in one place, so I saved seven questions for you to answer in one reply.

Path: `export/001 - task-booking-funnel-events-clarification.md`
Verified: read-back succeeded; 37 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

The main ones:

- **Scope:** the plan gives the work to three owners. Apps and web build the client events, the Booking squad builds `booking_confirmed`, and the Data team moves the dashboard. Your naming convention allows one discipline code per task title, so I need to know whether you want one task or a parent task with a subtask per owner.
- **A contradiction about `booking_confirmed`:** the events table says it fires when the booking becomes confirmed. The notes say it fires when a Pay now booking leaves `payment_pending`. Bookings also leave that state when they expire after 30 minutes, so following the notes would count expired bookings. Since every booking count is meant to use this event, I don't want to pick one wording without checking with you.
- **Plan status:** comments on v0.3 closed at yesterday's refinement (2026-09-24). I need to know whether it passed as written or a newer version is coming.

The other questions ask whether:
- `date_changed` should go in, since it's still a proposal with its trigger unsettled
- iOS and web should follow the Android timing for `room_selected`
- `booking_confirmed` should carry `platform` and `locale`
- `checkout_complete` should get the new properties before it's removed on 2026-11-01

Once you answer, the task will be saved as `export/002 - task-…`.