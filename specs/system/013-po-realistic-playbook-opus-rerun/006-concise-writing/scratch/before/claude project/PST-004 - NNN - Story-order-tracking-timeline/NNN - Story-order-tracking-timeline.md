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
