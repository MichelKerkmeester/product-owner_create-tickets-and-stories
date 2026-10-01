```markdown
# DATA - Guest app - TRK - Verify booking funnel events and remove checkout_complete

## About

---

The booking funnel cannot be drawn cleanly from search to booking today. `checkout_complete` fires when the confirmation screen renders on the client, so a booking is lost when the app closes before the screen draws and counted twice when a guest reopens the confirmation from Trips.

Dates arrive in three formats across the search and property page events, and web sends amounts as decimals while the apps send minor units. This task covers the Data team's side of the plan, checking every event in `events-collector` as the squads ship it, moving the funnel dashboard to `booking_confirmed` and having the collector drop `checkout_complete` on 2026-11-01.

**References**

---

- `context/roamstay-booking-funnel-tracking-plan.md`, the booking funnel tracking plan draft v0.3 written by Nadia, Data team
- `context/roamstay-context.md`, the Roamstay company context, for the analytics conventions and the service list

**Related tasks**

---

- The client events task for iOS, Android and web, owned by front end, is separate and not written yet
- The `booking_confirmed` task in `booking-service`, owned by back end, is separate and not written yet

### Requirements

---

### **Event checks in events-collector**

---

1.  **Every event arrives in `events-collector` with its common properties**

---

The analytics conventions put `app_version`, `session_id`, `platform`, `locale` and `source` on every event, so a property that goes missing or changes spelling breaks the join between the client steps and the server event. `booking_confirmed` carries `source` as `server` and copies `session_id` and `app_version` from the checkout request, which is what lets one booking's steps line up.

**Checklist**

- [] Each shipped event arrives in `events-collector` with `app_version`, `session_id`, `platform`, `locale` and `source`
- [] `booking_confirmed` arrives with `source` set to `server`
- [] `booking_confirmed` carries the `session_id` and `app_version` copied from the checkout request
- [] One booking's client events and its `booking_confirmed` row join on `session_id`

---

2.  **Dates, money and the funnel properties arrive as the plan states them**

---

The plan moves the search and property page dates to `check_in` and `check_out` in `YYYY-MM-DD`, and keeps money in one shape, an integer in minor units with `currency` beside it. Web sends decimals and the apps send minor units today, which is why revenue per step does not add up across platforms.

**Checklist**

- [] `search_submitted` and `property_viewed` carry `check_in` and `check_out` as `YYYY-MM-DD` and gain `nights` and `guests`
- [] Every event in the table carries `check_in`, `check_out`, `nights`, `guests` and `rooms`
- [] `search_submitted` carries `destination_id`, and every event from `property_viewed` onward carries `property_id`
- [] Every event from `room_selected` onward carries `room_type_id`, `rate_plan_id`, `total_amount_minor` and `currency`
- [] `total_amount_minor` arrives as an integer in minor units with city tax included
- [] `payment_submitted` and `booking_confirmed` carry `payment_option` as `pay_now` or `pay_at_property`
- [] `booking_confirmed` carries `booking_id` as the booking reference

---

3.  **Event reads match what each event can say**

---

`payment_submitted` fires on the tap before the payment provider answers, so it reports that a guest tried to pay and nothing about whether the payment went through. `room_selected` fires once per pick and Android sends it after the price call returns, so one session can carry it more than once.

**Checklist**

- [] `payment_submitted` is read as a payment attempt and never as a completed payment
- [] `room_selected` is read as one row per pick, and one session can carry it more than once
- [] Android is not failed for sending `room_selected` after the price call returns
- [] `checkout_complete` is not read as a booking count anywhere

---

> `date_changed` stays `proposed`, with no properties agreed beyond the common ones and the dates and its trigger still open between one event per tap in the picker and one when the new range is applied. Its check lands here once Search settles the trigger and the app ships the event.

### **Funnel dashboard**

---

4.  **Every booking count reads `booking_confirmed`**

---

`booking-service` sends `booking_confirmed` when a Pay now booking leaves `payment_pending` or a Pay at property booking is created, so it carries the bookings the business counts. `checkout_complete` misses a booking when the app closes before the confirmation screen draws and adds one when a guest reopens the confirmation from Trips.

**Checklist**

- [] Every booking count on the funnel dashboard reads `booking_confirmed`
- [] No tile, filter or saved view on the dashboard reads `checkout_complete`
- [] A booking whose app closed before the confirmation screen drew counts once
- [] A guest reopening the confirmation from Trips adds no second count

---

5.  **The dashboard moves before `checkout_complete` is dropped**

---

`checkout_complete` keeps firing next to `booking_confirmed` until 2026-11-01 so dashboards can move over. A dependency left behind on that date goes blank.

**Checklist**

- [] The dashboard reads `booking_confirmed` in production before 2026-11-01
- [] The funnel reads end to end from `search_submitted` to `booking_confirmed` after the move
- [] Nothing on the dashboard reads `checkout_complete` on or after 2026-11-01

---

### **`checkout_complete` removal**

---

6.  **`events-collector` drops `checkout_complete` on its removal date**

---

The plan sets removal on 2026-11-01 and puts the drop in the collector, so the event stops whatever app version sends it. An older build still sending `checkout_complete` cannot keep the old count alive.

**Checklist**

- [] From 2026-11-01 `events-collector` drops `checkout_complete` whatever app version sends it
- [] The drop does not wait for the apps to stop sending `checkout_complete`
- [] No `checkout_complete` row is stored from 2026-11-01

---
```

Export-equivalent path: `export/002 - task-booking-funnel-events.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: supplied event, property, service and status identifiers (`search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted`, `booking_confirmed`, `checkout_complete`, `date_changed`, `events-collector`, `booking-service`, `total_amount_minor`, `payment_pending`, `pay_at_property`, `proposed`) and the dates `2026-11-01` and `YYYY-MM-DD` kept verbatim as the sources write them.

Quality status: pass on the six dimensions. Actionability decides a task, and every checklist item names something observable in `events-collector` or on the dashboard. Accuracy holds because each value, status word and date comes from the tracking plan or the conventions as written, and the open `date_changed` decision is carried as open rather than resolved.

Summary: three requirement groups, the event checks in `events-collector`, the dashboard move to `booking_confirmed`, and the collector drop of `checkout_complete` on 2026-11-01. Two things to check before this goes out. The title's surface reads `Guest app`, because the conventions list only Guest app, Partner Hub and Back office and this work is internal to Data, with `TRK` as the code you gave. `date_changed` sits in a note rather than a checklist item, since its trigger and its properties past the common ones are still open with Search and there is no testable check yet. Name either change and I'll reissue the task.