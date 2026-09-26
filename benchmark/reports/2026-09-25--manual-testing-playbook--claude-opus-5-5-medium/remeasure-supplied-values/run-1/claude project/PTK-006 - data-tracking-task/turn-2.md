```markdown
# DATA - Guest app - TRK - Booking funnel event checks and dashboard move

### About

---

The booking funnel can't be drawn in one line from search to booking today. `checkout_complete` fires when the confirmation screen renders. If the app closes before the screen draws, the booking is lost. If the guest reopens the confirmation from Trips, the booking is counted twice. The web sends amounts as decimals while the apps send minor units, so revenue per step doesn't add up across platforms. Search and property page events also carry dates in three different formats.

Nadia's booking funnel tracking plan fixes this with a new set of funnel events, including a server-side `booking_confirmed`. The event table came out of the Booking squad refinement unchanged. This task is the Data team's part of the plan. Nadia checks each event in `events-collector` as the squads ship it and moves the funnel dashboard to `booking_confirmed`. She also has `events-collector` drop `checkout_complete` on its removal date. Building the client events and `booking_confirmed` itself is out of scope, because each has its own `FE` or `BE` task.

### Requirements

---

1.  **Check each event in `events-collector` as it ships**

---

Each event is checked against its row in the tracking plan when the squad that builds it ships it. The apps ship on the two-week release train and the web deploys continuously. Each client event is therefore checked on iOS, Android and web as it arrives on each one.

**Every event**

- [ ] Carries `app_version`, `session_id`, `platform`, `locale` and `source`
- [ ] Carries `check_in` and `check_out` as dates in `YYYY-MM-DD`
- [ ] Carries `nights`, `guests` (adults plus children) and `rooms` as integers
- [ ] `nights` matches the dates, so a Monday `check_in` and a Thursday `check_out` give `3`

**From `room_selected` onward**

- [ ] Carries `property_id`, `room_type_id` and `rate_plan_id` as integers
- [ ] Carries `total_amount_minor` as an integer in minor units with city tax included, and `currency` as an ISO code
- [ ] The web sends `total_amount_minor` in minor units like the apps, so €129.50 arrives as `12950` and never as a decimal

**`search_submitted` and `property_viewed`, status `changed`**

- [ ] Both move their dates to `check_in` and `check_out` in `YYYY-MM-DD` and gain `nights` and `guests`
- [ ] `search_submitted` fires when the guest taps Search with a destination and valid dates, and carries `destination_id` as an integer
- [ ] `property_viewed` fires when the property page opens, and carries `property_id` as an integer

**`room_selected`, status `new`**

- [ ] Fires once per pick of a room type and rate plan, and again when the guest goes back and picks another room
- [ ] On Android, arriving after the price call returns rather than on the tap is accepted, as agreed in the plan comments

**`checkout_started`, status `new`**

- [ ] Fires when the checkout screen opens

**`payment_submitted`, status `new`**

- [ ] Fires when the guest taps Pay now or confirms a Pay at property booking, before the payment provider answers
- [ ] Carries `payment_option` as `pay_now` or `pay_at_property`

**`booking_confirmed`, status `new`**

- [ ] Sent by `booking-service` with `source` set to `server`
- [ ] Fires when a Pay now booking leaves `payment_pending`, or when a Pay at property booking is created
- [ ] Carries `booking_id` as the booking reference, such as `RS-2MF8QD`, and `payment_option`
- [ ] Carries the `session_id` and `app_version` of the checkout request, so it joins the client events of the same session on `session_id`
- [ ] Fires once per `booking_id`, so reopening the confirmation from Trips sends no second event
- [ ] Doesn't fire for a Pay now booking that expires in `payment_pending` after `30 minutes`

> `payment_submitted` shows the guest tried to pay and says nothing about whether the payment went through. Only `booking_confirmed` counts as a booking.

> The plan puts `platform` and `locale` on every event but says `booking-service` copies only `session_id` and `app_version` from the checkout request. The check for `platform` and `locale` on `booking_confirmed` waits until the `BE` task settles whether the event carries them.

> `date_changed` is `proposed`. It has no properties agreed beyond the common ones and the dates. Search still has to decide whether it fires on every tap in the picker or once when the new range is applied. This task doesn't check it until its row is agreed.

2.  **Move the funnel dashboard to `booking_confirmed`**

---

The funnel dashboard counts bookings from `booking_confirmed` instead of `checkout_complete`. A booking then counts once, whether or not the confirmation screen draws. The move has to land before 2026-11-01, while `checkout_complete` still fires next to `booking_confirmed`.

**Checklist**

- [ ] The funnel steps run `search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted` and `booking_confirmed` in that order
- [ ] Every booking count uses `booking_confirmed`, and no chart counts `checkout_complete` or `payment_submitted` as a booking
- [ ] Revenue per step uses `total_amount_minor` and adds up across iOS, Android and web
- [ ] Revenue is split by `currency` and never summed across currencies, since Roamstay has no currency conversion
- [ ] The dashboard reads from `booking_confirmed` before 2026-11-01

3.  **Drop `checkout_complete` in `events-collector` on 2026-11-01**

---

`checkout_complete` is `deprecated`, which means it keeps firing next to `booking_confirmed` until its removal date so dashboards can move over. From 2026-11-01 `events-collector` drops it, whatever app version sends it. Older app versions may keep sending it after that date.

**Checklist**

- [ ] `checkout_complete` keeps arriving in `events-collector` until 2026-11-01
- [ ] From 2026-11-01 `events-collector` drops `checkout_complete` from every app version and from the web
- [ ] The dashboard move in requirement 2 is finished before the drop
```

Export-equivalent path: `export/002 - task-booking-funnel-event-checks-and-dashboard-move.md`

HVR self-scan: 0 hard blockers. Fixed: removed an Oxford comma in the About scope sentence. Kept with reason: none.

**Quality:** The task meets the Task Mode format. It has `### About`, numbered requirement groups with `---` dividers and `- [ ]` checklists, and no checklist item ends with a full stop. Event names, property names, status words, dates and example values are written as they appear in the tracking plan and the Roamstay context.

**What the task covers:** It's the Data team's `TRK` task, with three parts:
- Checking each event as the squads ship it
- Moving the funnel dashboard to `booking_confirmed` before 2026-11-01
- Having `events-collector` drop `checkout_complete` on 2026-11-01

The client events and `booking_confirmed` are left to their own `FE` and `BE` tasks. I didn't write a date for the refinement because the plan says 2026-09-24 and you said yesterday.

**Things I added, so you can remove any of them:**
- **Surface:** I used `Guest app` in the title because every client event starts there.
- **Checks per platform:** each client event is checked separately on iOS, Android and web.
- **Nights check:** `nights` has to match the dates. I took the Monday-to-Thursday example from the glossary.
- **One event per booking:** `booking_confirmed` fires once per `booking_id`. It also doesn't fire when a Pay now booking expires after `30 minutes` in `payment_pending`.
- **Dashboard step order:** the funnel steps follow the order of the event table.
- **Revenue by currency:** revenue is split by `currency` because Roamstay has no currency conversion.

**Open points still in the task:**
- **`room_selected` timing:** the late send is accepted only on Android. You didn't say whether iOS and web get the same allowance.
- **`platform` and `locale` on `booking_confirmed`:** this check waits for the `BE` task.
- **`date_changed`:** not checked while it's `proposed`.

A ClickUp connector isn't available in this session, so I can't push the task. Copy it into ClickUp yourself, with the H1 as the task name.