```markdown
# DATA - Guest app - TRK - Booking funnel event verification and dashboard cutover

## About

---

The booking funnel tracking plan, draft v0.3 in the Data team space, cannot yet draw one clean funnel from search to booking. `checkout_complete` fires on the confirmation screen, so a booking is lost when the app closes before the screen draws and counted twice when the guest reopens the confirmation from Trips, and amounts and dates arrive in mismatched formats across platforms. The plan's refinement on 2026-09-24 closed with its event table unchanged.

This task carries Data's own work on those events: checking each one in `events-collector` against its row as the squads ship it, moving the funnel dashboard to `booking_confirmed`, and having `events-collector` drop `checkout_complete` on `2026-11-01`. The client events and `booking_confirmed` themselves arrive from separate `FE` and `BE` tasks, and `date_changed` stays out of this task until Search settles its open picker question.

### Requirements

---

1.  **Verify each funnel event against its plan row**

---

Each event is checked in `events-collector` as the squad that owns it ships it, across iOS, Android and web. A row fails when a trigger, a source or a property differs from the plan.

**Checklist**

- [] Confirm `search_submitted` fires when the guest taps Search with a destination and valid dates, and carries `destination_id`
- [] Confirm `property_viewed` fires when the property page opens, and carries `property_id`
- [] Confirm `room_selected` fires once per pick and again when the guest goes back and picks another room
- [] Confirm `room_selected` waits for the price call, so `total_amount_minor` is known when it fires
- [] Confirm `checkout_started` fires when the checkout screen opens
- [] Confirm `payment_submitted` fires on the pay tap before the payment provider answers, and carries `payment_option`
- [] Confirm `booking_confirmed` arrives from `booking-service` when a Pay now booking leaves `payment_pending` or a Pay at property booking is created
- [] Confirm `booking_confirmed` carries `booking_id`, `payment_option` and the `session_id` and `app_version` copied from the checkout request, with `source` set to `server`

---

2.  **Verify the properties that travel on every event**

---

The plan's property table decides what each step carries, and today's mismatched formats are what stop revenue from adding up across platforms. Every supplied property travels under the name and unit the plan gives it.

**Checklist**

- [] Confirm `property_id` arrives on `property_viewed` and on every later step
- [] Confirm `check_in`, `check_out`, `nights`, `guests` and `rooms` arrive on every event
- [] Confirm `check_in` is the first night of the stay and `check_out` the departure day, both as `YYYY-MM-DD`
- [] Confirm `room_type_id` and `rate_plan_id` arrive from `room_selected` onward
- [] Confirm `total_amount_minor` arrives as an integer in minor units with city tax included, and that `currency` sits beside it
- [] Confirm the web sends the same integer minor units as the apps, so revenue per step adds up across platforms
- [] Confirm `app_version`, `session_id`, `platform`, `locale` and `source` arrive on every event
- [] Confirm server events carry the `session_id` of the request that caused them

---

3.  **Move the funnel dashboard to `booking_confirmed`**

---

Every booking count reads `booking_confirmed` from now on, and the dashboard has to move before `checkout_complete` disappears so no tile or alert goes blank.

**Checklist**

- [] Confirm every booking step on the funnel dashboard reads `booking_confirmed` rather than `checkout_complete`
- [] Confirm a booking counts once when a Pay now booking leaves `payment_pending` or a Pay at property booking is created
- [] Confirm a booking still counts when the guest reopens the confirmation from Trips
- [] Confirm a booking counts when the app closes before the confirmation screen draws
- [] Confirm each funnel step joins its client and server events on `session_id`
- [] Confirm revenue per step reconciles across iOS, Android and web
- [] Confirm no tile, alert or saved query reads `checkout_complete` by `2026-11-01`

---

4.  **Retire `checkout_complete` in `events-collector`**

---

`checkout_complete` keeps firing beside `booking_confirmed` until `2026-11-01`, so the dashboards have room to move over. From that date `events-collector` drops it.

**Checklist**

- [] Confirm `checkout_complete` keeps arriving beside `booking_confirmed` until `2026-11-01`
- [] Confirm `events-collector` drops `checkout_complete` from `2026-11-01`, whatever app version sends it
- [] Confirm the drop changes no other event's acceptance
- [] Confirm the funnel dashboard needs nothing from `checkout_complete` on the day it is dropped
```

Export-equivalent path: `export/001 - task-booking-funnel-event-verification-and-dashboard-cutover.md`

HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: backticked event names, property names, `YYYY-MM-DD`, `2026-11-01`, `payment_pending` and the `pay_now` and `pay_at_property` wording are carried from the tracking plan and your answer verbatim, and the house `- []` checklist items end without a full stop.

Quality: About states the outcome and the value; four numbered groups carry testable `- []` checks with no build steps; every supplied value, date and status word travels as the source writes it; no `[Assumes: ...]` tags and no unrequested scope. Standard energy, with the Business, Technical, Delivery and Data-consumer perspectives applied. No ClickUp connector is present in this session, so there is nothing to push and no approval to ask for.

Three things I decided, each easy to strike:

- **Surface in the title.** I read it as `Guest app`, since the funnel runs there and the dashboard is internal rather than a Back office tool. Say the word if you want a different surface.
- **One task, not a parent with subtasks.** Your answer puts all three Data jobs in one place, so the four groups sit in one task. I can split the collector drop out as a subtask if you would rather it shipped on its own.
- **`date_changed` left out.** It is still `proposed` with the picker question open for Search, and it is a client event, so no check for it sits in this task. Add a line and I will fold it in.

Summary: the task now covers Data's verification of all seven shipping funnel events plus the shared property and format checks, the dashboard's move to `booking_confirmed`, and the `2026-11-01` drop of `checkout_complete`. The seven events are checked as the owning squads ship them, so the FE and BE tasks can land on their own schedules without changing this one.