I've written the Data team's task under TRK. It covers three things:
- **Event checks:** checking each event in `events-collector` as each platform ships it.
- **Dashboard move:** moving the funnel dashboard to `booking_confirmed` before 2026-11-01.
- **Removal:** having the collector drop `checkout_complete` on that date.

Path: `export/002 - task-booking-funnel-events.md`
Verified: read-back succeeded; 122 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality:** the task has five requirement groups, each with a short reason and a checklist. Every event, property, date and value comes from Nadia's plan or your conventions file.

**How I settled the open points:**
- **`booking_confirmed` trigger:** you said the event table didn't change, so the table's wording applies. The event fires when the booking moves to confirmed, and a Pay now booking that expires after 30 minutes sends nothing.
- **`date_changed`:** left out, because it's still only proposed.
- **`room_selected` timing:** the late-send rule (after the price is known) applies to Android only, as Nadia agreed.
- **`checkout_complete`:** it doesn't get the new properties. The task only uses it during the switchover period and then removes it.
- **`platform` and `locale` on `booking_confirmed`:** the plan doesn't say whether they're included. The task flags this as something to agree with the Booking squad before the back-end work ships.

**Things I added that aren't in your sources, so you can remove them:**
- Checking that `nights` matches the gap between `check_in` and `check_out`
- Never adding up revenue across currencies on the dashboard
- No gap in booking counts on the dashboard around 2026-11-01

**Not covered:** other dashboards that may still read `checkout_complete`. The plan says "dashboards", but you only described the funnel dashboard.

The two related tasks for the front-end and back-end work are listed by name without links, since they don't exist yet.