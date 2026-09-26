```markdown
# DATA - Guest app - TRK - Booking funnel tracking rollout

### About

---

Right now the booking funnel can't be drawn as one line from search to booking. `checkout_complete` fires when the confirmation screen renders. If the app closes before the screen draws, the booking is lost, and it's counted twice when the guest reopens the confirmation from Trips. On top of that, the web sends amounts as decimals while the apps send minor units, and search and property page events carry dates in three different formats.

The booking funnel tracking plan fixes this with new and changed events, and refinement closed with no change to its event table. This task is the Data team's part. It covers three pieces of work: check each event in `events-collector` as the squads ship it, move the funnel dashboard to `booking_confirmed`, and have the collector drop `checkout_complete` on its removal date, 2026-11-01. After this, every booking count comes from one server event, and revenue per step adds up across iOS, Android and web.

The client events and `booking_confirmed` are built in separate FE and BE tasks. `date_changed` is still proposed in the plan, so it stays out of this task until Search and Data agree on its trigger and properties.

**References**

---

- `Booking funnel tracking plan, draft v0.3`

### Requirements

---

1.  **Validate each event as it ships**

---

An event counts as validated only when what arrives in `events-collector` matches its row in the tracking plan on every platform that sends it. iOS, Android and web ship separately, and the apps follow a two-week release train. So each event is checked per platform as that platform ships it.

**Every event**

- [ ] Carries `app_version`, `session_id`, `platform`, `locale` and `source`
- [ ] `source` is `client` on client events and `server` on `booking_confirmed`
- [ ] `check_in` and `check_out` arrive as `YYYY-MM-DD`, and `nights`, `guests` and `rooms` arrive as integers
- [ ] `nights` equals the number of nights between `check_in` and `check_out`, so check-in on a Monday and check-out on a Thursday sends `3`
- [ ] Any mismatch goes back to the squad that built the event, and the event is checked again after their fix

**By step**

- [ ] `search_submitted` carries `destination_id`
- [ ] `search_submitted` and `property_viewed` stop sending dates in their old formats
- [ ] `property_id` is present on `property_viewed` and every later step
- [ ] `room_type_id`, `rate_plan_id`, `total_amount_minor` and `currency` are present from `room_selected` onward
- [ ] `total_amount_minor` is an integer in minor units with city tax included, on web as well as on the apps
- [ ] `room_selected` arrives once per pick, so a guest who goes back and picks another room sends it again
- [ ] On Android, `room_selected` arrives after the price call returns and carries `total_amount_minor`
- [ ] `payment_submitted` carries `payment_option` as `pay_now` or `pay_at_property`, and is read as an attempt to pay, never as a completed payment

**booking_confirmed**

- [ ] Arrives when a Pay now booking leaves `payment_pending`, or when a Pay at property booking is created
- [ ] A Pay now booking that expires in `payment_pending` after 30 minutes sends no `booking_confirmed`
- [ ] Arrives once per booking, and reopening the confirmation from Trips sends nothing new
- [ ] Carries `booking_id` as the booking reference, `RS-` followed by six letters and digits
- [ ] Carries `payment_option`
- [ ] Carries the `session_id` and `app_version` of the checkout request, so it joins the client events from the same session

2.  **Move the funnel dashboard to booking_confirmed**

---

The funnel dashboard counts bookings from `checkout_complete` today. It moves to `booking_confirmed` before 2026-11-01, while both events still fire side by side, so the two counts can be compared before the old event stops. The move starts once `booking_confirmed` passes its checks under Validate each event as it ships.

**Checklist**

- [ ] Every booking count on the dashboard uses `booking_confirmed`
- [ ] The funnel runs `search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted` and `booking_confirmed`, with steps joined on `session_id`
- [ ] Revenue per step comes from `total_amount_minor` and is shown per `currency`, because Roamstay doesn't convert between currencies
- [ ] No part of the dashboard reads `checkout_complete` after 2026-10-31

3.  **Drop checkout_complete on 2026-11-01**

---

`checkout_complete` keeps firing next to `booking_confirmed` until its removal date, which gives dashboards time to move over. From 2026-11-01 `events-collector` drops it, whatever app version sends it, so older app versions that still send it don't bring the double count back.

**Checklist**

- [ ] `events-collector` accepts `checkout_complete` up to and including 2026-10-31
- [ ] From 2026-11-01 `events-collector` drops `checkout_complete` from every app version and from the web
- [ ] Every other booking funnel event keeps arriving after the drop
- [ ] The dashboard move under Move the funnel dashboard to booking_confirmed is finished before the drop
```

Export-equivalent path: `export/002 - task-booking-funnel-tracking-rollout.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

I wrote the task as the Data team's own TRK work, split into three groups: checking each event as it ships, moving the dashboard, and dropping `checkout_complete`. It's ready for review.

**Choices I made where you didn't answer:**
- **Surface:** The title uses Guest app as the surface because the funnel runs there. The task itself is Data team work.
- **`date_changed`:** Left out, with one line in About saying why.
- **`room_selected` timing:** The "arrives after the price call" check is limited to Android. That's the only platform the plan's comment agreed on. If iOS and web should wait for the price too, that line should cover all three.
- **References:** The tracking plan is named in plain text because no link was supplied. There's no Related tasks block yet because the FE and BE tasks don't have titles. Both can be added once the links and titles exist.
- **Refinement date:** You said refinement closed yesterday, which would be 2026-09-25. The plan says 2026-09-24. I left the date out of the task.

**Checks I added that aren't in the plan (remove any you don't want):**
- `nights` matches the dates
- Any mismatch goes back to the owning squad and gets checked again
- A Pay now booking that expires in `payment_pending` sends no `booking_confirmed`
- One `booking_confirmed` per booking, and reopening from Trips sends nothing new
- Revenue per step is shown per currency
- Other events keep arriving after `checkout_complete` is dropped
- The dashboard move waits until `booking_confirmed` has passed its checks

**Quality:** Clarity, completeness and actionability are strong because every check comes from the plan or from a named addition. The weak spot is the Android-only timing check, which is waiting on your answer.