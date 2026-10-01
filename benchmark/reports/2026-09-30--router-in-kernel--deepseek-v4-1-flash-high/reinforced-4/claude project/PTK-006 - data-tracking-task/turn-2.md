```markdown
# DATA - Guest app - TRK - Booking funnel event verification and dashboard cutover

## About

---

The Data team's own task for the booking funnel tracking plan: verify each event in `events-collector` as the squads ship it, move the funnel dashboard from `checkout_complete` to `booking_confirmed`, and have the collector drop `checkout_complete` on 2026-11-01. The client events and `booking_confirmed` ship under separate FE and BE tasks, and this task checks what the collector receives.

`checkout_complete` fires on the client when the confirmation screen renders, so a booking is lost when the app closes first and counted twice when the guest reopens the confirmation from Trips. Amounts arrive as decimals from the web and minor units from the apps, and dates use three formats across the funnel steps.

**References**

---

- `context/roamstay-booking-funnel-tracking-plan.md`
- `context/roamstay-context.md`

### Requirements

---

1.  **Every shipped event matches its plan row**

---

Nadia checks each shipped event against its row in the tracking plan, which is unchanged since the refinement closed on 2026-09-24, so the trigger and the properties the plan records stay true of what `events-collector` receives.

**Checklist**

- [] `search_submitted` fires on a Search tap with a destination and valid dates, and carries `destination_id`
- [] `property_viewed` fires when the property page opens, and every later step carries `property_id`
- [] `room_selected` fires once per room pick and again on a second pick, after the price call returns so `total_amount_minor` is present
- [] `checkout_started` fires when the checkout screen opens
- [] `payment_submitted` fires on the Pay now tap and on the Pay at property confirmation, before the payment provider answers, and carries no payment outcome
- [] `booking_confirmed` arrives from `booking-service` with `source` set to `server`, on the exit from `payment_pending` or at Pay at property creation
- [] `booking_confirmed` copies `session_id` and `app_version` from the checkout request, and carries `payment_option` and `booking_id`
- [] `date_changed` stays out of the verified set while its row reads `proposed`
- [] `date_changed` is checked once Search ships it, after the open point on picker taps versus applied ranges closes

---

2.  **Properties and formats hold across the funnel**

---

The plan's property table fixes what every event carries, and the analytics conventions fix how money, dates and identifiers travel.

**Checklist**

- [] `app_version`, `session_id`, `platform`, `locale` and `source` arrive on every event
- [] `check_in` and `check_out` arrive as dates in `YYYY-MM-DD`, with `nights`, `guests` and `rooms` beside them
- [] `room_type_id`, `rate_plan_id`, `total_amount_minor` and `currency` arrive from `room_selected` onward
- [] money arrives as an integer in minor units with `currency` beside it, on the web and the apps alike
- [] client and server events join on `session_id`, so one booking runs from `search_submitted` to `booking_confirmed`

---

3.  **The funnel dashboard runs on `booking_confirmed`**

---

The dashboard moves onto the server event before the deprecated event goes, and every booking count comes from `booking_confirmed`.

**Checklist**

- [] every funnel step reads the plan's events, with `checkout_complete` out of the funnel
- [] every booking count in the dashboard uses `booking_confirmed`
- [] a booking counts once, whether the app closed before the confirmation screen drew or the guest reopened it from Trips
- [] the move completes before 2026-11-01, so no report reads `checkout_complete` on its removal date
- [] revenue per step adds up across the web and the apps on `total_amount_minor` and `currency`
- [] date filters run on the single `YYYY-MM-DD` format across the funnel steps

---

4.  **`checkout_complete` leaves `events-collector` on 2026-11-01**

---

The collector keeps accepting the deprecated event until its removal date, so the dashboard can move while both events are live.

**Checklist**

- [] `checkout_complete` keeps firing beside `booking_confirmed` until 2026-11-01
- [] `events-collector` drops `checkout_complete` on 2026-11-01, whatever app version sends it
- [] the drop follows the dashboard move, so no funnel step loses data
```

Export-equivalent path: `export/002 - task-booking-funnel-event-verification.md`

HVR self-scan: 0 hard blockers. Fixed: none carried into the artifact, with one figure of speech, `goes dark`, replaced by plain wording while drafting. Kept with reason: the source identifiers `checkout_complete`, `booking_confirmed`, `payment_pending`, `events-collector` and `YYYY-MM-DD` and the status word `proposed` in backticks, as the tracking plan writes them.

Quality: source fidelity holds, since every event name, property, status and date travels as the plan writes it. The four requirement groups stay testable and within WHAT and WHY, and no event build steps leak in, because the FE and BE work sits outside this task. Roughly 580 words, inside the task budget.

Assumptions you can strike before this hardens:

- The title carries `Guest app` as its surface, since the events and the funnel are guest-facing. `events-collector` and the dashboard are Data team tooling rather than one of the three named surfaces, so say the word if the title should read differently.
- `date_changed` is kept out of the verified set while it is `proposed`, and its picker-tap question is treated as still open because the event table did not change. If the refinement settled that question, that line can go.
- The dashboard move and the collector drop sit together in this task, as you described, and the separate FE and BE tasks are named only as boundaries.
- `2026-11-01` is taken from the plan as the removal date.

Want this split into subtasks, one per event, or with the collector drop held as its own task?