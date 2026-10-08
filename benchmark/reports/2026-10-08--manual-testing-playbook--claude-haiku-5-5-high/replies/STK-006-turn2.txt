Export path: `export/002 - task-booking-funnel-events.md`
Verified: read-back succeeded; 68 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Quality: all six dimensions cleared, and each checklist item traces to a row or line in the plan or to the scope you gave.

The task covers the Data team's three jobs: checking each event in events-collector as it ships, moving the funnel dashboard to `booking_confirmed`, and dropping `checkout_complete` on 2026-11-01. The client events and `booking_confirmed` itself are left to the later FE and BE tasks. The clarification file (`001`) is unchanged.

I made three choices you should confirm or strike:

- **Surface:** I used Guest app in the title, since the funnel is guest-facing. events-collector is a service, not a surface.
- **`date_changed`:** I left it out of the checks while its open point is with Search, and the task says so.
- **Refinement date:** You said refinement closed yesterday, which is 2026-10-07. The plan says the Booking squad refinement was 2026-09-24. I took your word that the table is unchanged and cited it without a date. Tell me if the refinement you mean is a different one.

The `platform` and `locale` question on `booking_confirmed` is still open. The task keeps it as a note that waits on the BE task.