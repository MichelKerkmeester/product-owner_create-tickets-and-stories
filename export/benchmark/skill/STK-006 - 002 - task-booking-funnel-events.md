# DATA - Guest app - TRK - Booking funnel events and dashboard move

## About

---

Today the booking funnel can't be drawn cleanly from search to booking. `checkout_complete` fires when the confirmation screen renders on the client, so a booking is lost when the app closes before the screen draws, and counted twice when the guest reopens the confirmation from Trips. Amounts also differ between web and apps, and search and property page events carry dates in three formats.

This task covers the Data team's part of the fix. It checks each event in events-collector as the squads ship it, moves the funnel dashboard to `booking_confirmed` and has events-collector drop `checkout_complete` on its removal date. The client events and `booking_confirmed` itself get their own FE and BE tasks later. The outcome is one funnel from search to booking, where every booking count uses `booking_confirmed`, the event the plan says the server sends.

**References**

---

- `Booking funnel tracking plan, draft v0.3, Data team space. The event table is unchanged after refinement`

### Requirements

---

1.  **Event checks in events-collector**

---

As each squad ships a booking funnel event, the Data team checks it in events-collector against its row in the plan. The row sets the trigger, the properties and the status, so the check compares the shipped event with the row.

**Checklist**

- [] Each event is checked in events-collector as its squad ships it
- [] `search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted` and `booking_confirmed` are each checked against their plan row
- [] `check_in`, `check_out`, `nights`, `guests` and `rooms` arrive on every event in the table, with dates as `YYYY-MM-DD`
- [] Money arrives as an integer in `total_amount_minor`, with `currency` beside it, on every event from `room_selected` onward
- [] Each client event carries `app_version`, `session_id`, `platform`, `locale` and `source`, with `source` set to `client`
- [] `booking_confirmed` arrives with `source` set to `server`, `session_id` and `app_version` copied from the checkout request, and `payment_option` and `booking_id` set

> The plan lists `platform` and `locale` on every event but names only `session_id` and `app_version` as copied onto `booking_confirmed`. The plan does not say whether `booking_confirmed` carries `platform` and `locale`. That check waits on the `booking_confirmed` BE task.

> `date_changed` is proposed, and its open point is still with Search: one event per tap in the date picker, or one when the new range is applied. This task leaves it out of the checks until the plan settles that point and the row changes status.

---

2.  **Funnel dashboard on booking_confirmed**

---

The plan says every booking count should use `booking_confirmed`, and the dashboard moves before `checkout_complete` is removed.

**Checklist**

- [] Every booking count on the funnel dashboard reads `booking_confirmed`
- [] No booking count on the funnel dashboard reads `checkout_complete`
- [] The funnel dashboard draws one funnel from search to booking
- [] The dashboard move is live before 2026-11-01

---

3.  **checkout_complete removal**

---

The plan gives `checkout_complete` the status `deprecated`, with removal on 2026-11-01. From that date events-collector drops it, whatever app version sends it.

**Checklist**

- [] `checkout_complete` keeps firing next to `booking_confirmed` until 2026-11-01
- [] events-collector drops `checkout_complete` from 2026-11-01, whatever app version sends it
- [] The dashboard move in requirement 2 is complete before the drop takes effect
