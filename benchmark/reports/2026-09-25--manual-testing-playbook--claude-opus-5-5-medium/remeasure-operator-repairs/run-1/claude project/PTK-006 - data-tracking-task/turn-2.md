```markdown
# DATA - Guest app - TRK - Booking funnel event checks and dashboard move

### About

---

The booking funnel tracking plan replaces `checkout_complete` with a server event, `booking_confirmed`. It also moves every funnel event to one date format and to amounts in minor units. Today there is no single funnel from search to booking. `checkout_complete` misses a booking when the app closes before the confirmation screen draws. It counts a booking twice when the guest reopens the confirmation from Trips. The web also sends amounts in different units from the apps.

This task covers the Data team's part of the plan. That means checking each event in `events-collector` as the squads ship it and moving the funnel dashboard to `booking_confirmed`. It also means having `events-collector` drop `checkout_complete` on its removal date, 2026-11-01. The client events and `booking_confirmed` itself are built in separate FE and BE tasks. `date_changed` is out of scope while it is still a proposal.

**References**

---

- `Booking funnel tracking plan, draft v0.3`

### Requirements

---

1.  **Check each event in events-collector as it ships**

---

Squads build each event from its row in the tracking plan. Checking every event as it arrives catches a wrong trigger or property before the dashboard reads it. The apps ship on the two-week release train and the web deploys continuously, so an event can reach one platform before the others.

**All events**

- [ ] Each event with the status new or changed is checked in `events-collector` once its squad ships it. These are `search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted` and `booking_confirmed`
- [ ] Each client event is checked separately on iOS, Android and web
- [ ] Each event fires on the trigger in its row and carries every property the plan lists for it, with the plan's type
- [ ] Client events carry `app_version`, `session_id`, `platform` and `locale`, with `source` set to `client`
- [ ] `check_in` and `check_out` arrive as `YYYY-MM-DD` on every event, and `nights`, `guests` and `rooms` arrive as integers
- [ ] From `room_selected` onward, `total_amount_minor` is an integer in minor units with city tax included and `currency` beside it. This applies to the web as well as the apps

**Per event**

- [ ] `search_submitted` and `property_viewed` no longer send dates in their old formats
- [ ] `room_selected` fires once per pick, and fires again when the guest goes back and picks another room
- [ ] An Android `room_selected` sent once the price call returns, a few hundred milliseconds after the tap, passes
- [ ] `payment_submitted` fires on the Pay now tap and on confirming a Pay at property booking, before the payment provider answers
- [ ] `booking_confirmed` arrives with `source` set to `server` and carries the `session_id` and `app_version` of the checkout request, so it joins the client events of the same session
- [ ] `booking_confirmed` fires once per booking, when a Pay now booking moves from `payment_pending` to confirmed or when a Pay at property booking is created
- [ ] A Pay now booking that expires in `payment_pending` after 30 minutes sends no `booking_confirmed`
- [ ] Reopening the confirmation from Trips sends no second `booking_confirmed`
- [ ] `booking_id` is the booking reference, as in `RS-2MF8QD`, and `payment_option` is `pay_now` or `pay_at_property`

---

2.  **Move the funnel dashboard to booking_confirmed**

---

Every booking count should use `booking_confirmed`, because it fires when `booking-service` confirms the booking rather than when a screen renders. The dashboard moves before 2026-11-01 so it never depends on an event that has stopped arriving.

**Checklist**

- [ ] The funnel runs through `search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted` and `booking_confirmed`, in that order
- [ ] Every booking count on the dashboard uses `booking_confirmed`
- [ ] No part of the funnel dashboard reads `checkout_complete`
- [ ] Revenue per step uses `total_amount_minor` and is shown per `currency`, since Roamstay has no currency conversion
- [ ] The dashboard runs on `booking_confirmed` before 2026-11-01

---

3.  **Drop checkout_complete on its removal date**

---

`checkout_complete` keeps firing next to `booking_confirmed` until 2026-11-01 so dashboards can move over. The drop happens in `events-collector` rather than in the apps, so it holds whichever app version still sends the event.

**Checklist**

- [ ] `events-collector` accepts `checkout_complete` until 2026-11-01
- [ ] From 2026-11-01, `events-collector` drops `checkout_complete` whatever app version sends it
```

Export-equivalent path: `export/002 - task-booking-funnel-event-checks.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality:** The task passes on scope, structure and voice. It covers only the Data team's three responsibilities, and the checks come from the plan's rows, notes and comments.

**Things I added that you or Nadia may want to remove:**
- **Expired bookings:** A Pay now booking that expires in `payment_pending` sends no `booking_confirmed`. The plan's trigger says the booking "leaves `payment_pending`", and an expired booking also leaves that state without being confirmed.
- **Reopening from Trips:** Reopening the confirmation from Trips sends no second `booking_confirmed`. This comes from the double counting described in the plan's problem statement.
- **Revenue by currency:** The dashboard shows revenue per `currency`, because the company context says there is no currency conversion.
- **Checking each platform:** Each client event gets checked on iOS, Android and web separately, because the three platforms release on their own schedules.
- **`date_changed`:** You didn't say whether to include it, so I left it out while it is still a proposal.

**Still open, and left out of the task on purpose:**
- **`platform` and `locale` on `booking_confirmed`:** The plan says every event carries them, but its note says `booking-service` copies only `session_id` and `app_version`. The task checks only what the note states.
- **`room_selected` timing on iOS and web:** Nadia's reply only covers Android, so the late-send allowance applies to Android alone.

If you settle either point, I'll update the task under the same filename.