```markdown
# DATA - Guest app - TRK - Booking funnel events and dashboard cut-over

## About

---

Roamstay cannot draw one clean funnel from search to booking today. `checkout_complete` fires on the client at the confirmation screen, so a closed app loses the booking and a reopened confirmation counts it twice. Web sends amounts as decimals where the apps send minor units, and dates arrive in three formats.

It covers the Data team's side of tracking plan draft v0.3, whose refinement closed with no change to the event table. It checks each event in `events-collector` as squads ship it, moves the funnel dashboard to `booking_confirmed` and drops `checkout_complete` on `2026-11-01`. Separate FE and BE tasks build the client events and `booking_confirmed`.

**References**

---

- `Booking funnel tracking plan, draft v0.3`, Data team space, comments closed `2026-09-24`

### Requirements

---

1.  **Check each event against the plan as its squad ships it**

---

Nadia checks each event in `events-collector` when it starts arriving, and confirms its trigger, properties and formats against the plan. Every check below reads from the plan's event table and property table.

**Checklist**

- [] Every event carries `app_version`, `session_id`, `platform`, `locale` and `source`
- [] Every event carries `check_in`, `check_out`, `nights`, `guests` and `rooms`
- [] `search_submitted` carries `destination_id`
- [] `property_viewed` and every later event carry `property_id`
- [] `search_submitted` and `property_viewed` move their dates to `check_in` and `check_out`, and add `nights` and `guests`
- [] `room_selected` and every later event carry `room_type_id`, `rate_plan_id`, `total_amount_minor` and `currency`
- [] `room_selected` arrives once per pick, and again when a guest goes back and picks another room
- [] `checkout_started` arrives when the checkout screen opens
- [] `payment_submitted` arrives on the Pay now tap or the Pay at property confirm, before the provider answers
- [] `payment_submitted` and `booking_confirmed` carry `payment_option`
- [] `booking_confirmed` carries `booking_id` and `source` set to `server`
- [] `booking_confirmed` copies `session_id` and `app_version` from the checkout request, and joins to its client events on `session_id`

2.  **Confirm the three causes of the rework are closed**

---

The plan exists because one funnel could not be drawn from today's data. These checks are the evidence behind each cause.

**Checklist**

- [] `check_in` and `check_out` arrive as `YYYY-MM-DD` on every event, with no second date format in the funnel
- [] `total_amount_minor` arrives as an integer in minor units, with `currency` beside it
- [] Web, iOS and Android send the same minor-unit amount for the same stay, so revenue per step reconciles across platforms
- [] A booking counts once, whether or not the guest reopens the confirmation from Trips
- [] A booking counts when the app closed before the confirmation screen drew
- [] Booking counts read `booking_confirmed` alone, never `checkout_complete`

3.  **Move the funnel dashboard to `booking_confirmed`**

---

The dashboard moves while both events still fire, so booking counts can be compared before the old event goes.

**Checklist**

- [] The funnel shows `search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted` and `booking_confirmed` in one view
- [] Every booking count on the dashboard reads `booking_confirmed`
- [] Counts are compared against `checkout_complete` while both fire, before `2026-11-01`
- [] The dashboard reads no `checkout_complete` data from `2026-11-01`

4.  **Drop `checkout_complete` in `events-collector`**

---

`checkout_complete` keeps firing next to `booking_confirmed` until its removal date. From `2026-11-01` the collector stops taking it, whatever app version sends it.

**Checklist**

- [] `checkout_complete` keeps arriving, unchanged, until `2026-11-01`
- [] `events-collector` drops `checkout_complete` from `2026-11-01`, on every app version
- [] No dashboard, alert or export reads `checkout_complete` after the drop

```

Export-equivalent path: `export/002 - task-booking-funnel-tracking.md`
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality: every floor met | Kind: Task | Energy: Standard

The task holds the Data team's three outcomes: verify each event in `events-collector` as squads ship it, move the funnel dashboard to `booking_confirmed` before `2026-11-01`, and drop `checkout_complete` on its removal date. Requirements carry the plan's property names, formats and the removal date verbatim, and the client and server builds stay out as separate FE and BE tasks.

### Open items
1. **`date_changed`**
   - **Situation:** The plan marks it `proposed`, with the trigger still open between one event per picker tap and one per applied range, and no properties agreed beyond the common ones and the dates
   - **Open:** Confirm it stays out of this task until Search settles the trigger
2. **App version floor**
   - **Situation:** The funnel needs one answer on which app versions still send old date formats, and the client work sits in the later FE task
   - **Open:** Confirm the floor belongs there rather than in this task
3. **Stay properties on the live events**
   - **Situation:** The notes name only `nights` and `guests` as additions, while the property table puts all five stay properties on every event, so I applied the table
   - **Open:** Nothing to confirm
4. **Title surface**
   - **Situation:** The conventions offer Guest app, Partner Hub or Back office as the surface, and this task covers Data checks and a dashboard, so I named Guest app after the events it tracks
   - **Open:** Rename it if Data uses a different surface for tracking work

Want me to change anything?