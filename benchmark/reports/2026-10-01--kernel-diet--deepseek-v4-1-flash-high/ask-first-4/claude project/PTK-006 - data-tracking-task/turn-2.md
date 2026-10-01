```markdown
# DATA - Guest app - TRK - Booking funnel event verification and checkout_complete retirement

## About

---

No single booking funnel can be drawn today, because the events behind it disagree. `checkout_complete` fires when the confirmation screen renders, so a booking is lost if the app closes early and counted twice if the guest reopens it from Trips. The web sends decimals where the apps send minor units, and date formats differ across events.

This task is the Data team's part: verify each event in `events-collector` as its squad ships it, move the funnel dashboard onto `booking_confirmed`, and retire `checkout_complete` on 2026-11-01. The client events and `booking_confirmed` itself ship under separate `FE` and `BE` tasks, so this task checks what those tasks send.

**References**

---

- `context/roamstay-booking-funnel-tracking-plan.md`, tracking plan draft v0.3, event table unchanged when the Booking refinement closed on 2026-09-24
- `context/roamstay-context.md`, analytics conventions for event names and properties

**Related tasks**

---

- Booking funnel client events, `FE` task, to be raised
- `booking_confirmed` in `booking-service`, `BE` task, to be raised

### Requirements

---

### **Event verification in `events-collector`**

---

1.  **Each event matches its row in the plan**

---

Verification happens as the squads ship, so a funnel step is trusted before the dashboard is built on it. `date_changed` stays `proposed` with no properties agreed beyond the common ones, so it is not checked here.

**Checklist**

- [] Every event in the plan reaches `events-collector` under the name in its row
- [] Each event carries the properties its row lists, and `property_id` reaches `property_viewed` and every later step
- [] Every client event carries `app_version`, `session_id`, `platform` and `locale`, and every event carries `source`
- [] Server events carry the `session_id` of the request that caused them, so client and server events join on it
- [] `check_in` and `check_out` arrive as `YYYY-MM-DD` with `nights` and `guests` on every event in the funnel
- [] Money arrives as an integer in a property whose name ends in `_minor`, with `currency` beside it, from the web as well as the apps
- [] An event that fails its check goes back to the squad that ships it

---

2.  **Behaviour matches the notes per event**

---

The notes carry behaviour the table does not show, and each one changes what a funnel step means.

**Checklist**

- [] `room_selected` fires once per pick, and again when a guest goes back and chooses another room
- [] `room_selected` may arrive after the price call returns, and the delay does not break the funnel order
- [] `payment_submitted` fires on the tap before the payment provider answers, so it says nothing about whether payment went through
- [] `booking_confirmed` arrives with `source` set to `server` when a Pay now booking leaves `payment_pending` and when a Pay at property booking is created
- [] `booking_confirmed` copies `session_id` and `app_version` from the checkout request

---

### **Dashboard and `checkout_complete` retirement**

---

3.  **The funnel dashboard counts bookings from `booking_confirmed`**

---

`booking_confirmed` is sent by `booking-service` at the moment a booking is confirmed, rather than by the screen that draws the confirmation. The dashboard moves off `checkout_complete` before the collector stops accepting it.

**Checklist**

- [] The funnel reads `search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted` and `booking_confirmed`
- [] Booking counts and revenue come from `booking_confirmed` alone
- [] A booking is counted once, including a guest who reopens the confirmation from Trips
- [] No dashboard, report or alert still reads `checkout_complete` on 2026-11-01

---

4.  **`events-collector` drops `checkout_complete` on 2026-11-01**

---

`checkout_complete` keeps firing beside `booking_confirmed` until its removal date, so dashboards have time to move. From 2026-11-01 the collector drops it.

**Checklist**

- [] `checkout_complete` is accepted until 2026-11-01 and dropped from that date in `events-collector`
- [] The drop applies to every app version, including versions that still send the event
```

Export-equivalent path: `export/002 - task-booking-funnel-event-verification.md`

Quality status: Task Mode, canonical standalone task, title in the house `{Discipline} - {Surface} - {Feature code} - {Title}` shape, `- []` checklists inside Requirements, no `[Assumes:]` tags, WHAT and WHY only for the build tasks this one checks.

Scope is the Data team's part you described: verifying events in `events-collector`, moving the funnel dashboard to `booking_confirmed`, and the 2026-11-01 drop of `checkout_complete`. The client events and `booking_confirmed` appear only as named related tasks to be raised.

Three things to check before this hardens. The failing-event loop, where an event that fails its check goes back to the squad that ships it, is mine rather than the plan's. `date_changed` is left out on my reading, because it stays `proposed` with no properties agreed beyond the common ones and it ships with the client events. The surface is read as Guest app and the discipline as `DATA`, since the code comes from the area that changes.

Your item 4 questions do not block: References carries the two context files, and platform coverage is moot here, since this task verifies what reaches the collector rather than shipping an app build.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `checkout_complete`, `booking_confirmed`, `events-collector`, `booking-service`, `payment_pending`, `room_selected`, `_minor` and `total`-style identifiers as the plan's own event, service and property names; `proposed`, `deprecated` and `server` as supplied status words; `2026-09-24` and `2026-11-01` as supplied dates; `- []` checklist markers rather than the ClickUp `*   ` grammar, because this is a task artifact rather than a new Doc.