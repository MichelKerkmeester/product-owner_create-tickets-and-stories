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
