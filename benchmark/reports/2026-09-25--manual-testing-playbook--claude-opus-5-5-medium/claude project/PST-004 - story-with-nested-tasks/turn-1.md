```markdown
# Customer - Order tracking - Order page timeline

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
The order page on web, iOS and Android gets a status timeline that follows each parcel from payment to delivery. It also shows the expected delivery day whenever the parcel carrier sends one. The timeline covers parcel shipments only, because the pallet carrier sends no tracking events.

### Problem
* * *
"Where is my order" is the biggest reason customers contact Fernhouse. In August CS tagged `5,870` of `18,940` contacts as WISMO, which is `31%`. Most of those customers already had a tracking number. What they wanted to know was when the parcel would arrive, and the order page could not tell them. The page shows `Order placed` until dispatch and `Shipped` after it, and then never changes. Customers copy the number into the parcel carrier's own site, and the ones who get lost there contact CS.

### Solution
* * *
The order page becomes the place where a customer checks on a parcel, so they no longer need the carrier's site. The page moves through each status as the parcel moves, and it shows an arrival day and time window only when the carrier has sent one. The tracking number stays in the shipping email for customers who still prefer the carrier's page.

#### **Expected outcomes**
* * *
*   The WISMO share of contacts drops from `31%` to under `20%` within two months of release
*   Contacts from customers confused by the timeline do not rise

#### **Tasks**
* * *
*   [BE - TRACK - Tracking webhook](<NNN.1 - task-tracking-webhook.md>)
*   [BE - TRACK - Packed status from the warehouse system](<NNN.2 - task-packed-status.md>)
*   [FE - Web - TRACK - Order page tracking timeline](<NNN.3 - task-web-tracking-timeline.md>)
*   [FE - iOS - TRACK - Order page tracking timeline](<NNN.4 - task-ios-tracking-timeline.md>)
*   [FE - Android - TRACK - Order page tracking timeline](<NNN.5 - task-android-tracking-timeline.md>)
*   [DATA - TRACK - Tracking timeline events](<NNN.6 - task-tracking-timeline-events.md>)
* * *
##   

## Requirements
* * *
**Status timeline**
* * *
**Open:** the web layout. Design has mocked the timeline for the apps only, and the web layout is still to come from design.

*   The timeline is on the order page on `Web`, `iOS` and `Android`
*   Statuses in order: `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered`, `Delivery failed`
*   `Order placed` comes from orders-service when the payment is authorised
*   `Packed` comes from the warehouse system when the order is packed
*   `Shipped` comes from parcel carrier codes `PU` and `IT`
*   `Out for delivery` comes from code `OD`, `Delivered` from `DL` and `Delivery failed` from `EX`
*   A new `OD` after `Delivery failed` moves the order back to `Out for delivery`
*   Every step that happened shows with its date and time

**Delivery failed**
* * *
**Open:** whether `Delivery failed` shows the carrier's reason. Maud from CS says yes for not home, and no for any reason that sounds like Fernhouse's fault. Hamid settles it with CS.

*   The carrier's `exception_code` values are `NOT_HOME`, `ADDRESS_PROBLEM`, `DAMAGED` and `REFUSED`

**Delivery estimate**
* * *
*   The estimate shows under the current status only when the carrier sends an `eta_window`
*   The day line follows the `Order page / Tracking timeline` design frame, shown there as `Arriving Thursday 1 October`
*   The window line follows the same frame, shown there as `Between 10:00 and 14:00`
*   With no `eta_window`, no estimate shows, and none is derived from the dispatch date
*   The newest `eta_window` by `occurred_at` wins
*   An `OD` always carries a window, and an `IT` carries one only when the carrier can predict the day, mostly inside the Netherlands and Belgium

**Order page rules**
* * *
*   An order with several parcels shows one timeline per parcel, with that parcel's items under it
*   Tracking events are kept for `90 days` after delivery, after which the order page shows the last status only
*   Items over `30 kg` or `120 cm` go by the pallet carrier and keep today's page plus the line `The delivery company will call you to book a delivery slot`
*   The shipping email keeps the tracking number
*   Status text is translated for all six locales: `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR` and `en-GB`

**Carrier tracking events**
* * *
*   The carrier posts one `tracking.updated` event per scan to `/webhooks/carrier/tracking` on shipping-service
*   The tracking path stays separate from the label events path, because the carrier signs each subscription with its own secret
*   Each event is signed with `X-Carrier-Signature`, the hex HMAC-SHA256 of the raw body, keyed with the tracking subscription's secret
*   The carrier waits `5 seconds` for a 2xx and counts anything else as a failed delivery
*   After a failed delivery the carrier makes up to `5 attempts` more, waiting `1 min, 5 min, 15 min, 1 h, 6 h` before each, then drops the event
*   Delivery is at least once, so events are deduplicated on `event_id`
*   A dropped event cannot be recovered, because `GET /v1/shipments/{shipment_id}` returns label fields only and tracking history is not part of the carrier plan
*   About `3,100` parcels leave on a normal working day and up to `5,400` on the busiest, at `5` to `8` events each, so a peak day brings up to about `43,000` events

**Event order**
* * *
*   Events can arrive `out of order`, and an `IT` can reach shipping-service more than an hour after the `OD` for the same parcel
*   The timeline orders events by `occurred_at`, never by arrival
*   An event older than the newest one held for that parcel is stored for the history and does not change the status shown
*   After an `EX` with `NOT_HOME` the carrier tries again the next working day, which sends a new `OD`
*   After a second `NOT_HOME` the parcel goes to a parcel point, and its `DL` carries `delivered_to` set to `parcel_point` when the parcel is dropped there, not when the customer collects it

**Analytics**
* * *
*   Events cover the timeline being viewed and the carrier link being tapped
*   Each event needs a row in the Data team's tracking plan and a DATA task before any FE task sends it
*   Event names follow `object_action` in snake_case with a past-tense verb
*   Every event carries `platform`, `app_version`, `market`, `locale` and `customer_type`
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **The order page shows where the parcel is now**
* * *
*   **Given** a customer opens a shipped order on web, iOS or Android
*   **When** the parcel carrier has scanned the parcel since their last visit
*   **Then** the timeline shows the status that scan reached, with every earlier step and its date and time
*   **And** the status text appears in the customer's locale
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **A late or repeated scan never moves the status backwards**
* * *
*   **Given** an order showing `Out for delivery`
*   **When** an older in-transit scan or a retried event arrives afterwards
*   **Then** the status stays `Out for delivery`
*   **And** the older scan appears once in the history, at the time it happened
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **The delivery estimate appears only when the carrier gives one**
* * *
*   **Given** a parcel on its way to the customer
*   **When** the carrier has sent a delivery window
*   **Then** the day and window appear under the current status and follow the carrier's newest window
*   **And** when the carrier has sent no window, no estimate appears at all
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **A failed delivery and the next attempt both stay visible**
* * *
*   **Given** the carrier could not deliver the parcel
*   **When** the customer opens the order
*   **Then** the order shows `Delivery failed`
*   **And** once the carrier sets out again, the order returns to `Out for delivery` and the failed attempt stays in the timeline
* * *
- [ ] _Mark as done, if the criteria are met_

5\. **Each parcel in a split order has its own timeline**
* * *
*   **Given** an order that ships in several parcels
*   **When** the customer opens it
*   **Then** each parcel has its own timeline with the items it carries
* * *
- [ ] _Mark as done, if the criteria are met_

6\. **Pallet deliveries keep today's page with a booking note**
* * *
*   **Given** an order with an item that goes by the pallet carrier
*   **When** the customer opens it
*   **Then** that shipment keeps today's page, with the note that the delivery company will call to book a slot
* * *
- [ ] _Mark as done, if the criteria are met_

7\. **Old deliveries show their last status**
* * *
*   **Given** an order delivered longer ago than the tracking retention period
*   **When** the customer opens it
*   **Then** the order page shows the last status only
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

*   Whether `Delivery failed` shows the carrier's reason, open until Hamid settles it with CS
*   The web layout, open until design delivers it
*   A dropped `DL` leaves the order on its last status for good, because the carrier offers no tracking history to recover it
*   A parcel-point `DL` shows `Delivered` while the parcel still waits for the customer to collect it

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   A push notification for each status, which follows once the events are trusted
*   Changing the delivery address or day after dispatch
*   Tracking for return parcels
* * *
```
Export-equivalent path: `export/NNN - Story-order-tracking-timeline/NNN - Story-order-tracking-timeline.md`

```markdown
# BE - TRACK - Tracking webhook

### About

---

shipping-service receives the parcel carrier's `tracking.updated` events, stores them and maps each carrier code to the status the customer sees. Every timeline on the order page depends on this task. A tracking event the carrier drops after its last retry cannot be recovered, so the endpoint has to answer reliably at peak volume.

**Story**

---

- [Customer - Order tracking - Order page timeline](<NNN - Story-order-tracking-timeline.md>)

**Related tasks**

---

- [BE - TRACK - Packed status from the warehouse system](<NNN.2 - task-packed-status.md>)
- [FE - Web - TRACK - Order page tracking timeline](<NNN.3 - task-web-tracking-timeline.md>)
- [FE - iOS - TRACK - Order page tracking timeline](<NNN.4 - task-ios-tracking-timeline.md>)
- [FE - Android - TRACK - Order page tracking timeline](<NNN.5 - task-android-tracking-timeline.md>)

### Requirements

---

1.  **Receive and verify events**

---

The carrier signs the tracking subscription with its own secret and treats a slow answer as a failure. Five failed attempts mean the event is gone for good.

**Checklist**

- [ ] Events arrive at `/webhooks/carrier/tracking` on shipping-service, separate from the label events path
- [ ] Each event is verified against `X-Carrier-Signature`, the hex HMAC-SHA256 of the raw body keyed with the tracking subscription's secret
- [ ] A valid event gets a 2xx within `5 seconds`
- [ ] The endpoint keeps within that time at up to about `43,000` events on a peak day

---

2.  **Deduplicate and order events**

---

Delivery is at least once and events can arrive out of order. An `IT` can arrive more than an hour after the `OD`, and a retried event always arrives late.

**Checklist**

- [ ] Events are deduplicated on `event_id`
- [ ] Events are ordered by `occurred_at`, never by arrival
- [ ] An event older than the newest one held for that parcel is stored for the history and does not change the status shown
- [ ] The newest `eta_window` by `occurred_at` wins
- [ ] Each event is stored with its `eta_window`, `exception_code`, `delivered_to` and `location` when present

---

3.  **Map carrier codes to customer statuses**

---

**Checklist**

- [ ] `PU` and `IT` map to `Shipped`
- [ ] `OD` maps to `Out for delivery`
- [ ] `DL` maps to `Delivered`
- [ ] `EX` maps to `Delivery failed`
- [ ] A new `OD` after an `EX` moves the parcel back to `Out for delivery`

---

4.  **Retention**

---

**Checklist**

- [ ] Tracking events are kept for `90 days` after delivery, after which only the last status remains available to the order page
```
Export-equivalent path: `export/NNN - Story-order-tracking-timeline/NNN.1 - task-tracking-webhook.md`

```markdown
# BE - TRACK - Packed status from the warehouse system

### About

---

The warehouse system already reports back to orders-service when an order is packed, but the customer never sees it. This task records that report as the `Packed` status, so the timeline has a step between `Order placed` and `Shipped`.

**Story**

---

- [Customer - Order tracking - Order page timeline](<NNN - Story-order-tracking-timeline.md>)

**Related tasks**

---

- [BE - TRACK - Tracking webhook](<NNN.1 - task-tracking-webhook.md>)

### Requirements

---

**Packed status**

---

**Checklist**

- [ ] orders-service records `Packed` when the warehouse system reports the order packed
- [ ] `Packed` carries a date and time for the timeline
- [ ] `Order placed` stays tied to payment authorisation
```
Export-equivalent path: `export/NNN - Story-order-tracking-timeline/NNN.2 - task-packed-status.md`

```markdown
# FE - Web - TRACK - Order page tracking timeline

### About

---

The web order page replaces its fixed `Order placed` and `Shipped` states with a timeline that follows each parcel, plus the delivery estimate when the carrier sends one. Design has mocked the timeline for the apps only, and this task needs the web layout from design before the build starts.

**References**

---

Page

- `Order page / Tracking timeline`

**Story**

---

- [Customer - Order tracking - Order page timeline](<NNN - Story-order-tracking-timeline.md>)

**Related tasks**

---

- [BE - TRACK - Tracking webhook](<NNN.1 - task-tracking-webhook.md>)
- [DATA - TRACK - Tracking timeline events](<NNN.6 - task-tracking-timeline-events.md>)

### Requirements

---

1.  **Tracking timeline**

---

**Checklist**

- [ ] The order page shows `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered` and `Delivery failed` in that order, as each is reached
- [ ] Every step that happened shows with its date and time
- [ ] A new `Out for delivery` after `Delivery failed` keeps the failed attempt visible
- [ ] An order with several parcels shows one timeline per parcel, with that parcel's items under it
- [ ] More than `90 days` after delivery the page shows the last status only
- [ ] Status text is translated for `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR` and `en-GB`

---

2.  **Delivery estimate**

---

**Checklist**

- [ ] With a delivery window, the day and window show under the current status, as in the frame: `Arriving Thursday 1 October` and `Between 10:00 and 14:00`
- [ ] With no delivery window, no estimate shows, and none is derived from the dispatch date

---

3.  **Pallet items**

---

**Checklist**

- [ ] A shipment by the pallet carrier keeps today's page plus the line `The delivery company will call you to book a delivery slot`

---

4.  **Analytics**

---

**Checklist**

- [ ] The page sends the timeline viewed and carrier link tapped events once their tracking plan rows exist
```
Export-equivalent path: `export/NNN - Story-order-tracking-timeline/NNN.3 - task-web-tracking-timeline.md`

```markdown
# FE - iOS - TRACK - Order page tracking timeline

### About

---

The iOS order page replaces its fixed `Order placed` and `Shipped` states with a timeline that follows each parcel, plus the delivery estimate when the carrier sends one, following the app mock.

**References**

---

Page

- `Order page / Tracking timeline`

**Story**

---

- [Customer - Order tracking - Order page timeline](<NNN - Story-order-tracking-timeline.md>)

**Related tasks**

---

- [BE - TRACK - Tracking webhook](<NNN.1 - task-tracking-webhook.md>)
- [FE - Android - TRACK - Order page tracking timeline](<NNN.5 - task-android-tracking-timeline.md>)
- [DATA - TRACK - Tracking timeline events](<NNN.6 - task-tracking-timeline-events.md>)

### Requirements

---

1.  **Tracking timeline**

---

**Checklist**

- [ ] The order page shows `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered` and `Delivery failed` in that order, as each is reached
- [ ] Every step that happened shows with its date and time
- [ ] A new `Out for delivery` after `Delivery failed` keeps the failed attempt visible
- [ ] An order with several parcels shows one timeline per parcel, with that parcel's items under it
- [ ] More than `90 days` after delivery the page shows the last status only
- [ ] Status text is translated for `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR` and `en-GB`

---

2.  **Delivery estimate**

---

**Checklist**

- [ ] With a delivery window, the day and window show under the current status, as in the frame: `Arriving Thursday 1 October` and `Between 10:00 and 14:00`
- [ ] With no delivery window, no estimate shows, and none is derived from the dispatch date

---

3.  **Pallet items**

---

**Checklist**

- [ ] A shipment by the pallet carrier keeps today's page plus the line `The delivery company will call you to book a delivery slot`

---

4.  **Analytics**

---

**Checklist**

- [ ] The page sends the timeline viewed and carrier link tapped events once their tracking plan rows exist
```
Export-equivalent path: `export/NNN - Story-order-tracking-timeline/NNN.4 - task-ios-tracking-timeline.md`

```markdown
# FE - Android - TRACK - Order page tracking timeline

### About

---

The Android order page replaces its fixed `Order placed` and `Shipped` states with a timeline that follows each parcel, plus the delivery estimate when the carrier sends one, following the app mock.

**References**

---

Page

- `Order page / Tracking timeline`

**Story**

---

- [Customer - Order tracking - Order page timeline](<NNN - Story-order-tracking-timeline.md>)

**Related tasks**

---

- [BE - TRACK - Tracking webhook](<NNN.1 - task-tracking-webhook.md>)
- [FE - iOS - TRACK - Order page tracking timeline](<NNN.4 - task-ios-tracking-timeline.md>)
- [DATA - TRACK - Tracking timeline events](<NNN.6 - task-tracking-timeline-events.md>)

### Requirements

---

1.  **Tracking timeline**

---

**Checklist**

- [ ] The order page shows `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered` and `Delivery failed` in that order, as each is reached
- [ ] Every step that happened shows with its date and time
- [ ] A new `Out for delivery` after `Delivery failed` keeps the failed attempt visible
- [ ] An order with several parcels shows one timeline per parcel, with that parcel's items under it
- [ ] More than `90 days` after delivery the page shows the last status only
- [ ] Status text is translated for `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR` and `en-GB`

---

2.  **Delivery estimate**

---

**Checklist**

- [ ] With a delivery window, the day and window show under the current status, as in the frame: `Arriving Thursday 1 October` and `Between 10:00 and 14:00`
- [ ] With no delivery window, no estimate shows, and none is derived from the dispatch date

---

3.  **Pallet items**

---

**Checklist**

- [ ] A shipment by the pallet carrier keeps today's page plus the line `The delivery company will call you to book a delivery slot`

---

4.  **Analytics**

---

**Checklist**

- [ ] The page sends the timeline viewed and carrier link tapped events once their tracking plan rows exist
```
Export-equivalent path: `export/NNN - Story-order-tracking-timeline/NNN.5 - task-android-tracking-timeline.md`

```markdown
# DATA - TRACK - Tracking timeline events

### About

---

The release goal is a drop in WISMO contacts. These two events show whether customers use the timeline and how often they still leave for the carrier's page. No FE task can send a new event until the event has a row in the tracking plan, so this task comes before the FE analytics work.

**Story**

---

- [Customer - Order tracking - Order page timeline](<NNN - Story-order-tracking-timeline.md>)

**Related tasks**

---

- [FE - Web - TRACK - Order page tracking timeline](<NNN.3 - task-web-tracking-timeline.md>)
- [FE - iOS - TRACK - Order page tracking timeline](<NNN.4 - task-ios-tracking-timeline.md>)
- [FE - Android - TRACK - Order page tracking timeline](<NNN.5 - task-android-tracking-timeline.md>)

### Requirements

---

**Tracking plan rows**

---

**Checklist**

- [ ] One row for the tracking timeline being viewed on the order page
- [ ] One row for the carrier link being tapped
- [ ] Event names follow `object_action` in snake_case with a past-tense verb
- [ ] Each event carries `platform`, `app_version`, `market`, `locale` and `customer_type`
```
Export-equivalent path: `export/NNN - Story-order-tracking-timeline/NNN.6 - task-tracking-timeline-events.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `TBD...` in Estimation (a fixed Delivery placeholder).

I wrote a **Story** from Hamid's brief and Yusuf's carrier notes, plus six tasks following the split in Hamid's brief. They're one folder with seven files: the Story first, then the tasks in the brief's order. The DATA task lists the tracking plan rule from the company context, so its rows have to exist before the FE tasks send the events.

**Quality:** all six quality scores meet their minimum. Every hard value from both sources is in Requirements, and no acceptance criterion repeats a value. The brief has two open questions, whether a failed delivery shows the carrier's reason and the missing web layout. Each is marked **Open:** on its requirement. They also add the Delivery section: the estimate is left as `TBD...` and the out-of-scope list is Hamid's.

**Things I added that you can remove:**
- A Rabbit hole for parcel-point deliveries. Yusuf's notes say the carrier's "delivered" event for a parcel point arrives when the parcel is dropped there, so the order would show `Delivered` before the customer has it. That could create the kind of contact this story is meant to cut.
- The dropped-`DL` risk as a Rabbit hole.
- In the webhook task, storing `exception_code`, `delivered_to` and `location` with each event, which I took from "store tracking events".

**Questions the sources don't answer.** I left all of these out of the artifacts:
1. Which time zone should dates and times show in, especially for the UK?
2. Does each `IT` hub scan show as its own `Shipped` step, or as one?
3. After a failed delivery or a delivery, does the last estimate stay or disappear?
4. What happens after an `EX` with `ADDRESS_PROBLEM`, `DAMAGED` or `REFUSED`?
5. Is `Packed` recorded per order or per parcel on split orders?
6. Does the order page have a carrier link? The DATA task counts taps on one, but the brief never places it.
7. Do the estimate lines and the pallet line need translating, as the status text does?
8. Can guests see the order page at all?

**Next step:** send answers to any of these and I'll update the Story and tasks.