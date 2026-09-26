I've written the Data team's task. It covers Nadia's three jobs: checking each funnel event in `events-collector` as a squad ships it, moving the funnel dashboard to `booking_confirmed` before 2026-11-01, and having the collector drop `checkout_complete` on that date.

Path: `export/002 - task-booking-funnel-events.md`
Verified: read-back succeeded; 109 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

The task's first check covers the six agreed events event by event, taking every property, trigger and status word straight from the plan. `date_changed` is listed as out of scope because it's still `proposed` and nobody has agreed when it fires. The client events and `booking_confirmed` aren't built here, as you said.

Quality: every section is filled from the tracking plan, your company conventions or your answer. The plan's "Why we're redoing this" problems each map to a check the task names.

I added some things the plan doesn't say outright. Please remove any you don't want:
- **Title:** `DATA - Guest app - TRK - …`. I picked Guest app because the funnel is the guest's path through the app. None of your three surface options fits a dashboard exactly.
- **`booking_confirmed` checks:**
  - It doesn't fire for a Pay now booking that expires in `payment_pending`.
  - It fires once even if the app closes before the confirmation screen draws.
  - It doesn't fire again when the guest reopens the confirmation from Trips.
- **Web amounts:** a check that the web sends `total_amount_minor` in minor units, not decimals.
- **Dashboard rules:**
  - Revenue is shown per currency and never added up across currencies, because Roamstay doesn't convert currencies.
  - `payment_submitted` is never counted as a booking.
- **Order of the last two jobs:** the collector only drops `checkout_complete` after the dashboard has stopped using it. The note about `date_changed` also says it joins the checks once its trigger is agreed.

One small mismatch: you said refinement closed yesterday (2026-09-25), but the plan dates it 2026-09-24. I left the date out of the task, so nothing depends on which is right.