```markdown
# Customer - Order page - Order tracking

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
The order page on web, iOS and Android gets a status timeline that follows each parcel from payment to delivery. It also shows the expected delivery day when the parcel carrier sends one. Pallet items keep today's page, because the pallet carrier sends no tracking events.

This story does not cover push notifications for each status, changes to the delivery address or day after dispatch, tracking for return parcels or analytics events for the timeline. The analytics events come in a later story.

### Problem
* * *
Where is my order is the biggest reason customers contact CS. In August CS tagged 5,870 of 18,940 contacts as WISMO, which is 31%. Most of those customers already had a tracking number. What they wanted to know was when the parcel would arrive, and the order page cannot tell them. It shows `Order placed` until dispatch and `Shipped` after it, and it never changes after that. Customers copy the tracking number into the parcel carrier's own site, and the ones who get lost there contact CS.

### Solution
* * *
The order page answers the question customers now take to CS: where the parcel is and when it will arrive. The timeline moves with each carrier scan. The arrival day shows only when the carrier supplies it, so the page never promises a day the carrier has not given.

#### **Expected outcomes**
* * *
*   The WISMO share of contacts drops from 31% to under 20% within two months of release
*   Contacts from customers confused by the timeline do not rise

#### **Tasks**
* * *
*   [FE - iOS - TRACK - Tracking timeline on the order page](<002.1 - task-ios-tracking-timeline.md>)
*   [FE - Android - TRACK - Tracking timeline on the order page](<002.2 - task-android-tracking-timeline.md>)
*   [FE - Web - TRACK - Tracking timeline on the order page](<002.3 - task-web-tracking-timeline.md>)
*   [BE - TRACK - Tracking webhook](<002.4 - task-tracking-webhook.md>)
* * *
##   

## Requirements
* * *
**Status timeline**
* * *
*   The timeline shows these statuses in this order: `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered`, `Delivery failed`
*   `Order placed` comes from orders-service when the payment is authorised
*   `Packed` comes from the warehouse system through orders-service, which already receives it
*   `Shipped` comes from parcel carrier codes `PU` and `IT`
*   `Out for delivery` comes from `OD`
*   `Delivered` comes from `DL`
*   `Delivery failed` comes from `EX` and shows no reason, whatever `exception_code` the carrier sends
*   A new `OD` after an `EX` moves the parcel back to `Out for delivery`
*   Every step that happened shows with its date and time
*   The web, iOS and Android layouts follow the `Order page / Tracking timeline` frame
*   Status text is translated for all six locales: `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR` and `en-GB`

**Delivery estimate**
* * *
*   The estimate shows under the current status only when the carrier sends an `eta_window`
*   The estimate uses the two lines in the frame: `Arriving Thursday 1 October` and `Between 10:00 and 14:00`
*   The newest `eta_window` by `occurred_at` replaces any earlier one
*   With no `eta_window`, no estimate shows, and none is derived from the dispatch date

**Carrier tracking events**
* * *
*   Events arrive as `tracking.updated` at `/webhooks/carrier/tracking` on shipping-service, on a path separate from the label events
*   Each request is verified against `X-Carrier-Signature`, the hex HMAC-SHA256 of the raw body keyed with the tracking subscription's own secret
*   The endpoint answers with a 2xx within `5 seconds`, since the carrier counts anything else as a failed delivery
*   After a failed delivery the carrier makes up to `5 attempts` more, waiting `1 min, 5 min, 15 min, 1 h, 6 h`, then drops the event for good
*   Delivery is at least once, so events are deduplicated on `event_id`
*   Events are ordered by `occurred_at`, never by arrival
*   An event older than the newest one held for that parcel is stored for the history and does not change the status shown
*   Tracking history cannot be fetched from the carrier, because `GET /v1/shipments/{shipment_id}` returns label fields only
*   The endpoint handles up to about `43,000` events on a peak day

**Parcels, pallet items and retention**
* * *
*   An order with several parcels shows one timeline per parcel, with that parcel's items under it
*   Items over `30 kg` or `120 cm` go by the pallet carrier, which sends no tracking events, and keep today's page plus the line `The delivery company will call you to book a delivery slot`
*   Tracking events are kept for `90 days` after delivery, and after that the order page shows the last status only

**Shipping email**
* * *
*   The shipping email keeps the tracking number
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **The order page shows where the parcel is now**
* * *
*   **Given** a customer opens the order page for a parcel the carrier has scanned
*   **When** the carrier reports a new scan
*   **Then** the timeline shows the matching status on web, iOS and Android
*   **And** every earlier step stays visible with its date and time
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **The arrival day shows only when the carrier gives one**
* * *
*   **Given** the carrier has sent a delivery window for the parcel
*   **When** the customer opens the order page
*   **Then** the day and window from the carrier's latest window show under the current status
*   **And** a parcel with no window shows no estimate at all
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **A failed delivery and the next attempt both show**
* * *
*   **Given** the carrier could not deliver the parcel
*   **When** the customer opens the order page
*   **Then** the timeline shows `Delivery failed` with no reason
*   **And** when the carrier sends the parcel out again, the timeline moves back to `Out for delivery` and keeps the failed attempt in its history
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **Late or repeated events never move the timeline backwards**
* * *
*   **Given** a parcel is `Out for delivery`
*   **When** an earlier in-transit scan or a retried event arrives after it
*   **Then** the status shown stays `Out for delivery`
*   **And** each scan appears once in the history, in the order it happened
* * *
- [ ] _Mark as done, if the criteria are met_

5\. **Each parcel in an order has its own timeline**
* * *
*   **Given** an order shipped in several parcels
*   **When** the customer opens the order page
*   **Then** each parcel shows its own timeline with its own items under it
* * *
- [ ] _Mark as done, if the criteria are met_

6\. **Pallet items keep today's page**
* * *
*   **Given** an order item that ships by the pallet carrier
*   **When** the customer opens the order page
*   **Then** the page shows today's status and tracking number, plus the line saying the delivery company will call to book a delivery slot
* * *
- [ ] _Mark as done, if the criteria are met_

7\. **Older orders show their last status**
* * *
*   **Given** a parcel was delivered longer ago than the tracking retention period
*   **When** the customer opens the order page
*   **Then** the page shows the parcel's last status only
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/002 - Story-order-tracking/002 - Story-order-tracking.md`

```markdown
# FE - iOS - TRACK - Tracking timeline on the order page

### About

---

The order page in the iOS app shows `Order placed` until dispatch and `Shipped` after it, and never changes after that. This task replaces that with a status timeline that moves as the parcel moves. It adds the expected delivery day when the carrier sends one, so customers no longer need the carrier's own site or a CS contact to know when their parcel arrives.

The tracking data comes from the BE tracking webhook task. The layout is in the `Order page / Tracking timeline` frame.

**Story**

---

- [Customer - Order page - Order tracking](<002 - Story-order-tracking.md>)

**Related tasks**

---

- [FE - Android - TRACK - Tracking timeline on the order page](<002.2 - task-android-tracking-timeline.md>)
- [FE - Web - TRACK - Tracking timeline on the order page](<002.3 - task-web-tracking-timeline.md>)
- [BE - TRACK - Tracking webhook](<002.4 - task-tracking-webhook.md>)

### Requirements

---

1.  **Status timeline**

---

The timeline shows each status the parcel has reached, so the customer can see where it is and what happened before.

**Checklist**

- [ ] Statuses show in this order: `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered`, `Delivery failed`
- [ ] Every step that happened shows with its date and time
- [ ] `Delivery failed` shows no reason
- [ ] After `Delivery failed`, a new delivery attempt shows as `Out for delivery` again, and the failed step stays in the timeline
- [ ] Layout matches the app design in the `Order page / Tracking timeline` frame
- [ ] Status text is translated for `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR` and `en-GB`

2.  **Delivery estimate**

---

The estimate shows only when the carrier has sent a delivery window, so the page never shows a day the carrier did not give.

**Checklist**

- [ ] The day and window show under the current status, as in the frame: `Arriving Thursday 1 October` and `Between 10:00 and 14:00`
- [ ] With no window from the carrier, no estimate shows
- [ ] A newer window replaces the one shown before

3.  **Parcels, pallet items and older orders**

---

Orders that do not fit a single tracked parcel still show something true.

**Checklist**

- [ ] An order with several parcels shows one timeline per parcel, with that parcel's items under it
- [ ] Items over `30 kg` or `120 cm` keep today's page plus the line `The delivery company will call you to book a delivery slot`
- [ ] More than `90 days` after delivery, the page shows the last status only
```

Export-equivalent path: `export/002 - Story-order-tracking/002.1 - task-ios-tracking-timeline.md`

```markdown
# FE - Android - TRACK - Tracking timeline on the order page

### About

---

The order page in the Android app shows `Order placed` until dispatch and `Shipped` after it, and never changes after that. This task replaces that with a status timeline that moves as the parcel moves. It adds the expected delivery day when the carrier sends one, so customers no longer need the carrier's own site or a CS contact to know when their parcel arrives.

The tracking data comes from the BE tracking webhook task. The layout is in the `Order page / Tracking timeline` frame.

**Story**

---

- [Customer - Order page - Order tracking](<002 - Story-order-tracking.md>)

**Related tasks**

---

- [FE - iOS - TRACK - Tracking timeline on the order page](<002.1 - task-ios-tracking-timeline.md>)
- [FE - Web - TRACK - Tracking timeline on the order page](<002.3 - task-web-tracking-timeline.md>)
- [BE - TRACK - Tracking webhook](<002.4 - task-tracking-webhook.md>)

### Requirements

---

1.  **Status timeline**

---

The timeline shows each status the parcel has reached, so the customer can see where it is and what happened before.

**Checklist**

- [ ] Statuses show in this order: `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered`, `Delivery failed`
- [ ] Every step that happened shows with its date and time
- [ ] `Delivery failed` shows no reason
- [ ] After `Delivery failed`, a new delivery attempt shows as `Out for delivery` again, and the failed step stays in the timeline
- [ ] Layout matches the app design in the `Order page / Tracking timeline` frame
- [ ] Status text is translated for `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR` and `en-GB`

2.  **Delivery estimate**

---

The estimate shows only when the carrier has sent a delivery window, so the page never shows a day the carrier did not give.

**Checklist**

- [ ] The day and window show under the current status, as in the frame: `Arriving Thursday 1 October` and `Between 10:00 and 14:00`
- [ ] With no window from the carrier, no estimate shows
- [ ] A newer window replaces the one shown before

3.  **Parcels, pallet items and older orders**

---

Orders that do not fit a single tracked parcel still show something true.

**Checklist**

- [ ] An order with several parcels shows one timeline per parcel, with that parcel's items under it
- [ ] Items over `30 kg` or `120 cm` keep today's page plus the line `The delivery company will call you to book a delivery slot`
- [ ] More than `90 days` after delivery, the page shows the last status only
```

Export-equivalent path: `export/002 - Story-order-tracking/002.2 - task-android-tracking-timeline.md`

```markdown
# FE - Web - TRACK - Tracking timeline on the order page

### About

---

The order page on web shows `Order placed` until dispatch and `Shipped` after it, and never changes after that. This task replaces that with a status timeline that moves as the parcel moves. It adds the expected delivery day when the carrier sends one, so customers no longer need the carrier's own site or a CS contact to know when their parcel arrives.

The tracking data comes from the BE tracking webhook task. The web layout is in the `Order page / Tracking timeline` frame.

**Story**

---

- [Customer - Order page - Order tracking](<002 - Story-order-tracking.md>)

**Related tasks**

---

- [FE - iOS - TRACK - Tracking timeline on the order page](<002.1 - task-ios-tracking-timeline.md>)
- [FE - Android - TRACK - Tracking timeline on the order page](<002.2 - task-android-tracking-timeline.md>)
- [BE - TRACK - Tracking webhook](<002.4 - task-tracking-webhook.md>)

### Requirements

---

1.  **Status timeline**

---

The timeline shows each status the parcel has reached, so the customer can see where it is and what happened before.

**Checklist**

- [ ] Statuses show in this order: `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered`, `Delivery failed`
- [ ] Every step that happened shows with its date and time
- [ ] `Delivery failed` shows no reason
- [ ] After `Delivery failed`, a new delivery attempt shows as `Out for delivery` again, and the failed step stays in the timeline
- [ ] Layout matches the web design in the `Order page / Tracking timeline` frame
- [ ] Status text is translated for `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR` and `en-GB`

2.  **Delivery estimate**

---

The estimate shows only when the carrier has sent a delivery window, so the page never shows a day the carrier did not give.

**Checklist**

- [ ] The day and window show under the current status, as in the frame: `Arriving Thursday 1 October` and `Between 10:00 and 14:00`
- [ ] With no window from the carrier, no estimate shows
- [ ] A newer window replaces the one shown before

3.  **Parcels, pallet items and older orders**

---

Orders that do not fit a single tracked parcel still show something true.

**Checklist**

- [ ] An order with several parcels shows one timeline per parcel, with that parcel's items under it
- [ ] Items over `30 kg` or `120 cm` keep today's page plus the line `The delivery company will call you to book a delivery slot`
- [ ] More than `90 days` after delivery, the page shows the last status only
```

Export-equivalent path: `export/002 - Story-order-tracking/002.3 - task-web-tracking-timeline.md`

```markdown
# BE - TRACK - Tracking webhook

### About

---

The order page timeline on web, iOS and Android depends on the parcel carrier's tracking events. This task receives and stores those events and maps each carrier code to the status the customer sees.

The carrier sends each event by webhook, can deliver events in any order and drops an event for good after its last retry. Tracking history cannot be fetched again later, so a missed `DL` leaves the order on its last status. The endpoint's reliability decides whether a customer ever sees `Delivered`.

**Story**

---

- [Customer - Order page - Order tracking](<002 - Story-order-tracking.md>)

**Related tasks**

---

- [FE - iOS - TRACK - Tracking timeline on the order page](<002.1 - task-ios-tracking-timeline.md>)
- [FE - Android - TRACK - Tracking timeline on the order page](<002.2 - task-android-tracking-timeline.md>)
- [FE - Web - TRACK - Tracking timeline on the order page](<002.3 - task-web-tracking-timeline.md>)

### Requirements

---

1.  **Receiving events**

---

Every `tracking.updated` event the carrier sends is accepted once and only once, even on the busiest days.

**Checklist**

- [ ] Events are received at `/webhooks/carrier/tracking` on shipping-service, on a path separate from the label events
- [ ] Each request is verified against `X-Carrier-Signature`, the hex HMAC-SHA256 of the raw body keyed with the tracking subscription's own secret
- [ ] The endpoint answers with a 2xx within `5 seconds`
- [ ] A retried event is recognised by its `event_id` and stored once
- [ ] The endpoint handles up to about `43,000` events on a peak day, from up to `5,400` parcels at 5 to 8 events each

> The carrier counts anything other than a 2xx within 5 seconds as a failed delivery. It makes up to `5 attempts` more, waiting `1 min, 5 min, 15 min, 1 h, 6 h`, then drops the event. `GET /v1/shipments/{shipment_id}` returns label fields only, so a dropped event cannot be recovered.

2.  **Status mapping**

---

Each carrier code becomes one status the order page shows.

**Checklist**

- [ ] `PU` and `IT` map to `Shipped`
- [ ] `OD` maps to `Out for delivery`
- [ ] `DL` maps to `Delivered`
- [ ] `EX` maps to `Delivery failed`, and no failure reason reaches the order page
- [ ] A new `OD` after an `EX` moves the parcel back to `Out for delivery`
- [ ] `Order placed` and `Packed` still come from orders-service, which already receives `Packed` from the warehouse system

3.  **Event order and delivery estimate**

---

Events can arrive out of order. On busy days an `IT` can reach us more than an hour after the `OD` for the same parcel, and retried events arrive late by design. The status shown has to follow the time of the scan.

**Checklist**

- [ ] Events are ordered by `occurred_at`, never by arrival
- [ ] An event older than the newest one held for that parcel is stored for the history and does not change the status shown
- [ ] The newest `eta_window` by `occurred_at` becomes the delivery estimate
- [ ] A parcel with no `eta_window` has no estimate

> An `OD` always carries an `eta_window`. An `IT` carries one only when the carrier can predict the day, which is mostly inside the Netherlands and Belgium.

4.  **Retention**

---

**Checklist**

- [ ] Tracking events are kept for `90 days` after delivery, and after that only the last status is kept for the order page
- [ ] Pallet shipments have no tracking events, because the pallet carrier sends none
```

Export-equivalent path: `export/002 - Story-order-tracking/002.4 - task-tracking-webhook.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

This is a **Story** with four tasks in the order you gave. The Story, its tasks and the task links all agree. Every value from Hamid's brief and Yusuf's notes that's still in scope appears in Requirements, with its original units and notation. I left out `## Delivery` because nothing needed it: the failure reason is decided, and the web design is ready.

**Changes from your answers**
- There's no task for `Packed`. The Story says orders-service already receives it.
- The DATA events are out, and About says they come in a later story.

**Things I added (strike any you don't want)**
- **Out of scope:** The Story's About lists what it doesn't cover, taken from the brief's out-of-scope section. I put it there instead of a No-gos section so the Story doesn't need a Delivery section.
- **Task links:** Each task links to the other three tasks.
- **Step times:** In the BE task, the time shown for each step comes from `occurred_at`, the time of the scan.

**Still open from my first question (I did not decide these for you)**
- **Parcel point drop-off:** When the carrier drops a parcel at a parcel point, it sends `DL`. That shows as `Delivered` even though the customer hasn't collected it yet. I followed the brief's mapping.
- **Guests:** Guests have no order history, and the Story doesn't say whether they can see tracking.
- **Time zone:** The Story doesn't say which time zone the delivery window uses. This matters for the UK.
- **Figma link:** There's no link to the design frame, so the Story has no References section.

**New gaps I found while writing**
- **Repeated scans:** A parcel gets 2 to 4 `IT` scans, and all of them map to `Shipped`. "Every step that happened" could mean one `Shipped` step or one step per scan. The design frame should decide this.
- **Mixed orders:** The brief doesn't say what happens when one order has both parcel items and pallet items.
- **Estimate translation:** The brief asks for translated status text only. The estimate lines probably need translating too, but I didn't add that.

Next step: tell me how to handle the open points, and I'll update the files. I can't write to ClickUp from this session, so the files are ready to save or paste.