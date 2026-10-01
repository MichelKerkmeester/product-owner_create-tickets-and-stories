```markdown
# DATA - Guest app - TRK - Booking funnel verification and dashboard move

## About

---

The funnel from search to booking cannot be drawn cleanly today. `checkout_complete` fires when the confirmation screen renders, so a booking is lost when the app closes before the screen draws and counted twice when the guest reopens the confirmation from Trips. The web sends decimals while the apps send minor units, and the search and property page events carry dates in three formats.

This task carries the Data team's side of Nadia's tracking plan. It checks every event in `events-collector` as the squads ship their builds, moves the funnel dashboard onto `booking_confirmed`, and drops `checkout_complete` on its removal date. The client events and `booking_confirmed` itself arrive from separate FE and BE tasks, so neither build sits here.

**References**

---

Source

- `roamstay-booking-funnel-tracking-plan.md`, booking funnel tracking plan draft v0.3, Nadia, Data team

### Requirements

---

### **Event verification**

---

1.  **Check every plan event in `events-collector` as its squad ships it**

---

The plan's rows are the check, and an event is verified once it arrives with the trigger, the properties and the status its row gives it. The refinement closed with the event table unchanged, so the rows stand as written.

**Checklist**

- [] `search_submitted` and `property_viewed` arrive with `check_in` and `check_out` in `YYYY-MM-DD`, plus `nights` and `guests`
- [] `room_selected`, `checkout_started` and `payment_submitted` arrive once their FE task ships
- [] `booking_confirmed` arrives from `booking-service` with `source` set to `server` once its BE task ships
- [] Every event carries `app_version`, `session_id`, `platform`, `locale` and `source`
- [] Every event carries `check_in`, `check_out`, `nights`, `guests` and `rooms`
- [] Money arrives as an integer in minor units, in a property whose name ends in `_minor` with `currency` beside it, so `EUR 516.00` arrives as `51600`
- [] `total_amount_minor` includes city tax
- [] `booking_confirmed` arrives with `session_id` and `app_version` copied from the checkout request
- [] Client events and `booking_confirmed` join on `session_id` for one booking
- [] `date_changed` is checked once Search settles its granularity and an FE task ships it

---

### **Funnel dashboard**

---

2.  **Move the funnel dashboard onto `booking_confirmed`**

---

The dashboard reads `checkout_complete` today, which counts a rendered screen rather than a booking. Every booking count moves to `booking_confirmed` before the collector drops the old event.

**Checklist**

- [] Every booking count on the funnel dashboard reads `booking_confirmed`
- [] No step on the dashboard reads `checkout_complete` after the move
- [] The funnel shows each step from `search_submitted` to `booking_confirmed` for the same booking
- [] A booking whose app closes before the confirmation screen draws still counts once
- [] Reopening the confirmation from Trips adds no second booking
- [] Revenue per step adds up across iOS, Android and web, now that amounts are integers in minor units

---

### **Collector cutover**

---

3.  **Drop `checkout_complete` in the collector on its removal date**

---

The plan retires `checkout_complete` on 2026-11-01, and the collector stops accepting it from that date whatever app version sends it.

**Checklist**

- [] `events-collector` drops `checkout_complete` on `2026-11-01`
- [] The drop holds for older app versions that still send it
- [] Nothing in the collector, the dashboard or a scheduled job reads `checkout_complete` after that date
- [] Up to `2026-11-01` the event keeps arriving next to `booking_confirmed`, so dashboards can move over
```

Export-equivalent path: `export/001 - task-booking-funnel-events.md`, replacing the earlier scoped version under the same number.

Quality: PASS on all six floors. Completeness 8, Clarity 8, Actionability 9, Accuracy 9, Relevance 8, Mechanism Depth 8. Accuracy and Actionability carry it, since every item names something observable in `events-collector` or on the dashboard.

HVR self-scan: 0 hard blockers. Fixed: no banned terms or punctuation survived the pass. Kept with reason: backticked plan values such as `_minor`, `pay`-free identifiers, `session_id` and `2026-11-01`, plus the supplied lifecycle words `deprecated` and `proposed`.

Two judgment calls I made, both easy to strike. The title's surface is Guest app, since the convention allows Guest app, Partner Hub or Back office and the funnel is the Guest app's. The FE and BE builds are named inside the body as separate tasks rather than described, so the squad that picks this up can see the dependency without this task claiming their work.

Next step: the FE task for the client events and the BE task for `booking_confirmed` are ready to draft from the same plan whenever you want them.