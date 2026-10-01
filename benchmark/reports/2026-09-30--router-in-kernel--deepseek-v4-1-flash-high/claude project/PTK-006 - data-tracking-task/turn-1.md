```markdown
# FE - Guest app - TRK - Booking funnel events

## About

---

The funnel from search to booking cannot be drawn cleanly today. `checkout_complete` fires when the confirmation screen renders, so a booking is lost when the app closes before the screen draws and counted twice when the guest reopens the confirmation from Trips. The web sends decimals while the apps send minor units, and the search and property page events carry dates in three formats.

This task builds the client events in Nadia's tracking plan draft v0.3 on iOS, Android and web. `booking_confirmed` is server work in `booking-service` for the Booking squad, and the funnel dashboard move belongs to the Data team, so neither is in scope here.

**References**

---

Source

- `roamstay-booking-funnel-tracking-plan.md`, booking funnel tracking plan draft v0.3, Nadia, Data team

### Requirements

---

### **Event set**

---

1.  **Update `search_submitted` and `property_viewed`**

---

Both rows are `changed`, meaning live events whose properties change. They move their dates to `check_in` and `check_out` in `YYYY-MM-DD` and gain `nights` and `guests`, which is what ends the three date formats.

**Checklist**

- [] `search_submitted` fires when the guest taps Search with a destination and valid dates
- [] `search_submitted` carries `destination_id`
- [] `property_viewed` fires when the property page opens
- [] Both events carry `check_in` and `check_out` in `YYYY-MM-DD`
- [] Both events carry `nights` and `guests`

---

2.  **Add the new step events**

---

`room_selected`, `checkout_started` and `payment_submitted` are `new` rows, and each one marks a step the funnel cannot see today.

**Checklist**

- [] `room_selected` fires once per room type and rate plan pick, and again when the guest picks another room
- [] `room_selected` carries `property_id`, `room_type_id`, `rate_plan_id`, `total_amount_minor` and `currency`
- [] Android may send `room_selected` once the price call returns instead of on the tap, a few hundred milliseconds later
- [] `checkout_started` fires when the checkout screen opens
- [] `payment_submitted` fires when the guest taps Pay now or confirms a Pay at property booking
- [] `payment_submitted` carries `payment_option`, set to `pay_now` or `pay_at_property`
- [] `payment_submitted` records that the guest tried to pay, never that the payment went through

---

3.  **Retire `checkout_complete` and hold `date_changed`**

---

`checkout_complete` is `deprecated` and keeps firing next to `booking_confirmed` until 2026-11-01, when `events-collector` drops it whatever app version sends it. `date_changed` stays `proposed` until Search settles its granularity.

**Checklist**

- [] `checkout_complete` keeps firing until `2026-11-01` so dashboards can move over
- [] No booking count reads `checkout_complete`
- [] `date_changed` fires when the guest changes dates on the property page
- [] `date_changed` carries the common properties plus `check_in` and `check_out` only
- [] Whether the picker sends one event per tap or one when the new range is applied stays open with Search

---

### **Properties**

---

4.  **Send the common properties on every event**

---

The common set from our analytics conventions goes on every event, so no client event needs a local variant.

**Checklist**

- [] Every event carries `app_version`, `session_id`, `platform`, `locale` and `source`
- [] `source` reads `client` on every event here
- [] Every event carries `check_in`, `check_out`, `nights`, `guests` and `rooms`
- [] `guests` counts adults plus children
- [] `property_id` sits on `property_viewed` and every later step
- [] `room_type_id`, `rate_plan_id`, `total_amount_minor` and `currency` sit on `room_selected` and every later step

---

5.  **Send money as minor units with its currency**

---

The web sends decimals and the apps send minor units, so revenue per step does not add up across platforms. Every amount travels as an integer in minor units, in a property whose name ends in `_minor`, with `currency` beside it.

**Checklist**

- [] `total_amount_minor` sends as an integer in minor units, so `EUR 516.00` sends as `51600`
- [] `currency` carries the property's ISO code, for example `EUR`
- [] `total_amount_minor` includes city tax
- [] The web converts to minor units before sending
- [] One booking reports the same `total_amount_minor` and `currency` from all three platforms

---

### **Verification**

---

6.  **Confirm the funnel holds across platforms and joins to the server**

---

The client steps and `booking_confirmed` form one funnel, and the dashboard moves onto `booking_confirmed` before the cutover.

**Checklist**

- [] One test booking on iOS, Android and web sends the same event names and properties
- [] One test booking shows every step from `search_submitted` through to `booking_confirmed`
- [] A booking whose app closes before the confirmation screen draws still reaches the funnel on `booking_confirmed`
- [] Reopening the confirmation from Trips adds no second booking
- [] Client events and `booking_confirmed` join on `session_id` for one booking
```

Export-equivalent path: `export/001 - task-booking-funnel-events.md`

Quality: PASS on all six floors. Completeness 8, Clarity 8, Actionability 9, Accuracy 9, Relevance 8, Mechanism Depth 8. Actionability and Accuracy carry it, since every checklist item names something a tester can watch in `events-collector`.

HVR self-scan: 0 hard blockers. Fixed: no banned terms or punctuation survived the pass. Kept with reason: backticked plan values such as `pay_at_property`, `total_amount_minor`, `2026-11-01` and `proposed`, which are supplied identifiers and a supplied lifecycle status.

Routed to Task Mode, standard energy. The plan splits the work by owner, so this is scoped to the client events on iOS, Android and web, which is the unit the plan itself assigns to the apps and web together. Three scope decisions are mine rather than the plan's, and you can overrule any of them: `booking_confirmed` and the dashboard move sit outside this task because the plan gives them to the Booking squad and the Data team, `date_changed` is carried with its `proposed` status and its open granularity question intact rather than committed, and the `checkout_complete` row is handled as a retirement constraint rather than as new client work.

Next step: say the word and I will draft the two sibling tasks, `booking_confirmed` in `booking-service` and the dashboard move onto it before 2026-11-01.