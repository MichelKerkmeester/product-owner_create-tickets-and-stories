```markdown
# Customer - Order tracking - Order page timeline

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
This story adds a status timeline to the order page on web, iOS and Android. The timeline updates as the parcel moves and shows the expected delivery day when the parcel carrier sends one. Four tasks deliver it: one for each client and one for the tracking webhook.

### Problem
* * *
Where is my order is the biggest reason customers contact Fernhouse. In August, CS tagged 5,870 of 18,940 contacts as WISMO, which is 31%. Most of those customers already had a tracking number. What they wanted to know was when the parcel would arrive. Today the order page shows `Order placed` until dispatch and `Shipped` after it, with the tracking number, and it never changes after that. Customers copy the number into the carrier's own site, and the ones who get lost there contact CS.

### Solution
* * *
The order page follows each parcel through the carrier's scans, so customers can see where the parcel is and when it will arrive without leaving Fernhouse. The delivery day appears only when the carrier sends one. Fernhouse never estimates it from the dispatch date.

#### **Expected outcomes**
* * *
*   The WISMO share of contacts drops from 31% to under 20% within two months of release
*   Contacts from customers confused by the timeline do not rise

#### **Tasks**
* * *
*   [FE - iOS - TRACK - Order page tracking timeline](<002.1 - task-ios-order-tracking-timeline.md>)
*   [FE - Android - TRACK - Order page tracking timeline](<002.2 - task-android-order-tracking-timeline.md>)
*   [FE - Web - TRACK - Order page tracking timeline](<002.3 - task-web-order-tracking-timeline.md>)
*   [BE - TRACK - Carrier tracking webhook and status mapping](<002.4 - task-carrier-tracking-webhook.md>)
* * *
##   

## Requirements
* * *
**Order page timeline**
* * *
*   The layout on web, iOS and Android follows the `Order page / Tracking timeline` frame
*   `Order placed` comes from orders-service when the payment is authorised
*   `Packed` comes from the warehouse system when the order is packed, and orders-service already receives it
*   `Shipped` comes from parcel carrier codes `PU` and `IT`
*   `Out for delivery` comes from carrier code `OD`
*   `Delivered` comes from carrier code `DL`
*   `Delivery failed` comes from carrier code `EX` and shows no reason
*   A new `OD` after `Delivery failed` moves the parcel back to `Out for delivery`
*   The timeline shows every step that happened, each with its date and time
*   Status text is translated for all six locales: `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR` and `en-GB`

**Delivery estimate**
* * *
**Open:** does `Between 10:00 and 14:00` show the customer's local time, or the time exactly as the carrier sends it? The `eta_window` carries its own UTC offset, and UK customers are one hour behind the Netherlands. Product settles this before the FE tasks close.

*   The estimate shows under the current status only when the carrier has sent an `eta_window`
*   The copy follows the design mock: `Arriving Thursday 1 October` and `Between 10:00 and 14:00`
*   With no `eta_window`, no estimate shows, and none is worked out from the dispatch date
*   The newest `eta_window` by `occurred_at` wins

**Parcels and pallet items**
* * *
*   An order with several parcels shows one timeline per parcel, with that parcel's items under it
*   Items over `30 kg` or `120 cm` ship by the pallet carrier, which sends no tracking events
*   Pallet items keep today's order page plus the line `The delivery company will call you to book a delivery slot`

**Retention**
* * *
*   Tracking events are kept for `90 days` after delivery
*   After `90 days` the order page shows the last status only

**Shipping email**
* * *
*   The shipping email keeps the tracking number

**Tracking webhook**
* * *
*   The carrier posts `tracking.updated` to `/webhooks/carrier/tracking` on shipping-service, which stays separate from the label webhook path
*   Every event is checked against `X-Carrier-Signature`, the hex HMAC-SHA256 of the raw body, keyed with the tracking subscription's own secret
*   The webhook answers with a 2xx within `5 seconds`, because any other answer counts as a failed delivery
*   After a failed delivery the carrier makes up to `5 attempts` more, waiting `1 min, 5 min, 15 min, 1 h, 6 h` before each one, then drops the event
*   Events are deduplicated on `event_id`, because delivery is at least once
*   Events are ordered by `occurred_at`, never by arrival
*   An event with an `occurred_at` older than the newest event held for that parcel is stored for the history and does not change the status shown
*   The webhook handles peak days of up to 5,400 parcels at 5 to 8 events each, about 43,000 events
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Order page
* * *
1\. **The order page follows the parcel until it arrives**
* * *
*   **Given** a customer has an order whose parcel the carrier has picked up
*   **When** the carrier scans the parcel on its way to them
*   **Then** the order page on web, iOS and Android shows the parcel's current status and every earlier step with its date and time, in the customer's language
*   **And** the customer can tell where the parcel is without visiting the carrier's site
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **A failed delivery stays visible after the next attempt**
* * *
*   **Given** the carrier could not deliver a parcel
*   **When** the carrier takes it out for delivery again
*   **Then** the order page shows the parcel as out for delivery again
*   **And** the failed attempt stays in the parcel's history with no reason given
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **The delivery estimate comes only from the carrier**
* * *
*   **Given** a parcel is on its way
*   **When** the carrier has sent a delivery window
*   **Then** the day and window show under the current status and follow the newest window the carrier sent
*   **And** when the carrier has sent no window, the page shows no estimate at all
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **Every parcel and pallet item on an order is accounted for**
* * *
*   **Given** an order ships in several parcels or includes pallet items
*   **When** the customer opens the order page
*   **Then** each parcel has its own timeline with its items under it
*   **And** pallet items keep today's order page with the line saying the delivery company will call to book a slot
* * *
- [ ] _Mark as done, if the criteria are met_

5\. **Old orders keep their last status**
* * *
*   **Given** a parcel was delivered so long ago that its tracking events have been removed
*   **When** the customer opens the order
*   **Then** the page shows the parcel's last status
* * *
- [ ] _Mark as done, if the criteria are met_

#### Tracking events
* * *
6\. **Late or repeated scans never move a parcel backwards**
* * *
*   **Given** the order page shows a parcel as out for delivery
*   **When** an earlier scan arrives late, or the carrier sends the same event again
*   **Then** the current status stays the same and no step appears twice
*   **And** the late scan takes its place in the parcel's history
* * *
- [ ] _Mark as done, if the criteria are met_

7\. **Only events signed by the carrier change a parcel**
* * *
*   **Given** an event reaches the tracking webhook
*   **When** its signature does not match the tracking subscription's secret
*   **Then** no parcel's status or history changes
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
The delivery budget or expected size for the approved scope.

*   TBD...

#### Rabbit holes
* * *
Areas that could waste effort, create ambiguity or distract from the intended outcome.

*   Whether `Between 10:00 and 14:00` shows the customer's local time or the time exactly as the carrier sends it, given that the `eta_window` carries its own UTC offset and UK customers are one hour behind the Netherlands
*   Recovering missed events: `GET /v1/shipments/{shipment_id}` returns label fields only and tracking history is not part of the carrier plan, so a dropped event is gone for good and a missed `DL` leaves the parcel on its last status

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   A push notification for each status
*   Changing the delivery address or day after dispatch
*   Tracking for return parcels
*   A reason on `Delivery failed`
*   Analytics events for the timeline and the carrier link, which come in a later story
* * *
```

Export-equivalent path: `export/002 - Story-order-tracking/002 - Story-order-tracking.md`

```markdown
# FE - iOS - TRACK - Order page tracking timeline

### About

---

The iOS order page shows `Order placed` until dispatch and `Shipped` after it, then never changes. Customers who want more go to the carrier's site or contact CS. This task replaces that with a status timeline for each parcel that updates as the parcel moves, plus the delivery day when the carrier sends one.

**Story**

---

- [Customer - Order tracking - Order page timeline](<002 - Story-order-tracking.md>)

**Related tasks**

---

- [BE - TRACK - Carrier tracking webhook and status mapping](<002.4 - task-carrier-tracking-webhook.md>)
- [FE - Android - TRACK - Order page tracking timeline](<002.2 - task-android-order-tracking-timeline.md>)
- [FE - Web - TRACK - Order page tracking timeline](<002.3 - task-web-order-tracking-timeline.md>)

### Requirements

---

1.  **Status timeline**

---

Each parcel gets a timeline that tells the customer where it is, using the statuses the tracking webhook provides.

**Checklist**

- [ ] The layout follows the `Order page / Tracking timeline` frame
- [ ] An order with several parcels shows one timeline per parcel, with that parcel's items under it
- [ ] The timeline uses the statuses `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered` and `Delivery failed`
- [ ] Every step that happened shows with its date and time
- [ ] `Delivery failed` shows no reason
- [ ] After a failed delivery and a new attempt, the parcel shows `Out for delivery` again and keeps `Delivery failed` in its history
- [ ] Status text is translated for all six locales

2.  **Delivery estimate**

---

The customer sees the delivery day only when the carrier sends one.

**Checklist**

- [ ] With an `eta_window`, the current status shows `Arriving Thursday 1 October` and `Between 10:00 and 14:00`, following the mock
- [ ] The estimate follows the newest `eta_window` the back end provides
- [ ] With no `eta_window`, no estimate shows, and none is worked out from the dispatch date
- [ ] The time zone of the window follows the decision on the Story's open question

3.  **Pallet items and older orders**

---

Orders that have no tracking events still show a clear status.

**Checklist**

- [ ] Pallet items keep today's order page plus the line `The delivery company will call you to book a delivery slot`
- [ ] A parcel delivered more than `90 days` ago shows its last status only
```

Export-equivalent path: `export/002 - Story-order-tracking/002.1 - task-ios-order-tracking-timeline.md`

```markdown
# FE - Android - TRACK - Order page tracking timeline

### About

---

The Android order page shows `Order placed` until dispatch and `Shipped` after it, then never changes. Customers who want more go to the carrier's site or contact CS. This task replaces that with a status timeline for each parcel that updates as the parcel moves, plus the delivery day when the carrier sends one.

**Story**

---

- [Customer - Order tracking - Order page timeline](<002 - Story-order-tracking.md>)

**Related tasks**

---

- [BE - TRACK - Carrier tracking webhook and status mapping](<002.4 - task-carrier-tracking-webhook.md>)
- [FE - iOS - TRACK - Order page tracking timeline](<002.1 - task-ios-order-tracking-timeline.md>)
- [FE - Web - TRACK - Order page tracking timeline](<002.3 - task-web-order-tracking-timeline.md>)

### Requirements

---

1.  **Status timeline**

---

Each parcel gets a timeline that tells the customer where it is, using the statuses the tracking webhook provides.

**Checklist**

- [ ] The layout follows the `Order page / Tracking timeline` frame
- [ ] An order with several parcels shows one timeline per parcel, with that parcel's items under it
- [ ] The timeline uses the statuses `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered` and `Delivery failed`
- [ ] Every step that happened shows with its date and time
- [ ] `Delivery failed` shows no reason
- [ ] After a failed delivery and a new attempt, the parcel shows `Out for delivery` again and keeps `Delivery failed` in its history
- [ ] Status text is translated for all six locales

2.  **Delivery estimate**

---

The customer sees the delivery day only when the carrier sends one.

**Checklist**

- [ ] With an `eta_window`, the current status shows `Arriving Thursday 1 October` and `Between 10:00 and 14:00`, following the mock
- [ ] The estimate follows the newest `eta_window` the back end provides
- [ ] With no `eta_window`, no estimate shows, and none is worked out from the dispatch date
- [ ] The time zone of the window follows the decision on the Story's open question

3.  **Pallet items and older orders**

---

Orders that have no tracking events still show a clear status.

**Checklist**

- [ ] Pallet items keep today's order page plus the line `The delivery company will call you to book a delivery slot`
- [ ] A parcel delivered more than `90 days` ago shows its last status only
```

Export-equivalent path: `export/002 - Story-order-tracking/002.2 - task-android-order-tracking-timeline.md`

```markdown
# FE - Web - TRACK - Order page tracking timeline

### About

---

The web order page shows `Order placed` until dispatch and `Shipped` after it, then never changes. Customers who want more go to the carrier's site or contact CS. This task replaces that with a status timeline for each parcel that updates as the parcel moves, plus the delivery day when the carrier sends one. The web layout is in the same frame as the apps.

**Story**

---

- [Customer - Order tracking - Order page timeline](<002 - Story-order-tracking.md>)

**Related tasks**

---

- [BE - TRACK - Carrier tracking webhook and status mapping](<002.4 - task-carrier-tracking-webhook.md>)
- [FE - iOS - TRACK - Order page tracking timeline](<002.1 - task-ios-order-tracking-timeline.md>)
- [FE - Android - TRACK - Order page tracking timeline](<002.2 - task-android-order-tracking-timeline.md>)

### Requirements

---

1.  **Status timeline**

---

Each parcel gets a timeline that tells the customer where it is, using the statuses the tracking webhook provides.

**Checklist**

- [ ] The layout follows the web layout in the `Order page / Tracking timeline` frame, on desktop and mobile browsers
- [ ] An order with several parcels shows one timeline per parcel, with that parcel's items under it
- [ ] The timeline uses the statuses `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered` and `Delivery failed`
- [ ] Every step that happened shows with its date and time
- [ ] `Delivery failed` shows no reason
- [ ] After a failed delivery and a new attempt, the parcel shows `Out for delivery` again and keeps `Delivery failed` in its history
- [ ] Status text is translated for all six locales

2.  **Delivery estimate**

---

The customer sees the delivery day only when the carrier sends one.

**Checklist**

- [ ] With an `eta_window`, the current status shows `Arriving Thursday 1 October` and `Between 10:00 and 14:00`, following the mock
- [ ] The estimate follows the newest `eta_window` the back end provides
- [ ] With no `eta_window`, no estimate shows, and none is worked out from the dispatch date
- [ ] The time zone of the window follows the decision on the Story's open question

3.  **Pallet items and older orders**

---

Orders that have no tracking events still show a clear status.

**Checklist**

- [ ] Pallet items keep today's order page plus the line `The delivery company will call you to book a delivery slot`
- [ ] A parcel delivered more than `90 days` ago shows its last status only
```

Export-equivalent path: `export/002 - Story-order-tracking/002.3 - task-web-order-tracking-timeline.md`

```markdown
# BE - TRACK - Carrier tracking webhook and status mapping

### About

---

The parcel carrier sends a `tracking.updated` event for every scan of a parcel. This task receives and stores those events and maps carrier codes to the statuses customers see, so the order page on web, iOS and Android can show a timeline for each parcel. orders-service already receives `Packed` from the warehouse system, so no work is needed there. Yusuf's notes on the carrier's tracking events guide (version 2.4) and the 2026-09-19 call with the carrier are the source for the rules below.

**Story**

---

- [Customer - Order tracking - Order page timeline](<002 - Story-order-tracking.md>)

**Related tasks**

---

- [FE - iOS - TRACK - Order page tracking timeline](<002.1 - task-ios-order-tracking-timeline.md>)
- [FE - Android - TRACK - Order page tracking timeline](<002.2 - task-android-order-tracking-timeline.md>)
- [FE - Web - TRACK - Order page tracking timeline](<002.3 - task-web-order-tracking-timeline.md>)

### Requirements

---

1.  **Receive tracking events**

---

A dropped event is gone for good, because `GET /v1/shipments/{shipment_id}` returns label fields only. The webhook has to accept every real event the first time it can.

**Checklist**

- [ ] The carrier posts `tracking.updated` to `/webhooks/carrier/tracking` on shipping-service, separate from the label webhook path
- [ ] Every event is checked against `X-Carrier-Signature`, the hex HMAC-SHA256 of the raw body, keyed with the tracking subscription's own secret
- [ ] An event whose signature does not match changes no parcel
- [ ] The webhook answers with a 2xx within `5 seconds`
- [ ] Events are deduplicated on `event_id`, which stays the same on every retry
- [ ] The webhook handles peak days of up to 5,400 parcels at 5 to 8 events each, about 43,000 events

2.  **Map carrier codes to statuses**

---

The carrier's codes become the statuses customers see on the order page.

**Checklist**

- [ ] `PU` and `IT` map to `Shipped`
- [ ] `OD` maps to `Out for delivery`
- [ ] `DL` maps to `Delivered`
- [ ] `EX` maps to `Delivery failed`
- [ ] A new `OD` after `EX` moves the parcel back to `Out for delivery`
- [ ] The order page can read each parcel's steps with their date and time, its current status and its newest `eta_window`, alongside `Order placed` and `Packed` from orders-service

3.  **Event order**

---

Hub scans upload in batches and retries arrive late by design, so events arrive out of order. On busy days an `IT` can arrive more than an hour after the `OD` for the same parcel.

**Checklist**

- [ ] Events are ordered by `occurred_at`, never by arrival
- [ ] An event with an `occurred_at` older than the newest event held for that parcel is stored for the history and does not change the current status
- [ ] The newest `eta_window` by `occurred_at` wins

4.  **Retention**

---

Tracking history is only needed for as long as customers are likely to look at it.

**Checklist**

- [ ] Tracking events are kept for `90 days` after delivery
- [ ] After `90 days` the parcel keeps its last status only
```

Export-equivalent path: `export/002 - Story-order-tracking/002.4 - task-carrier-tracking-webhook.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `TBD...` in Estimation, which is the fixed Delivery placeholder.

I've written the Story and your four tasks in the order you gave: iOS, Android, web, then the webhook. There's no task for `Packed`, `Delivery failed` shows no reason, and the analytics events are listed as out of scope for a later story. It passes the quality check.

**Still open:** you didn't say whether the delivery window shows the customer's local time or the carrier's time, and it matters for UK customers. I've left that as an open point on the delivery estimate. Because of that open point, the Story ends with a Delivery section. It also lists the brief's out-of-scope items and the fact that a missed carrier event can't be recovered.

**Things I added that weren't in your answer. Remove any you don't want:**
- **Signature check:** acceptance criterion 7 and the matching webhook check say an event with a bad signature changes no parcel. Yusuf's notes say events are signed but don't say what happens when a signature doesn't match.
- **Parcel data for the order page:** the webhook task says the order page can read each parcel's steps, current status and delivery window. The brief implies this but doesn't say it.
- **Locale list:** I named the six locales from the company context file.

**Choices I made from the source notes, since you didn't answer these:**
- **Parcel point drop-off:** this shows `Delivered`, as the brief's status table says. So a parcel left at a parcel point shows `Delivered` before the customer has collected it.
- **Other failed deliveries:** after an address problem, damage or refusal, the parcel stays on `Delivery failed` until the carrier sends another scan.
- **Orders with parcel and pallet items:** these follow both of the brief's rules: one timeline per parcel, and the pallet items keep today's page.
- **Guest orders:** these aren't covered, because guests have no order history to open.
- **Frame link:** the `Order page / Tracking timeline` frame is named but not linked, because no link was supplied.

The next step is to settle the time zone question. Then I can remove the open point, and the Delivery section too if you don't want to keep it.