# Customer - Post-purchase - Order tracking

* * *
## Problem
* * *
Where is my order (WISMO) is the biggest reason customers contact us. In August, CS tagged 5,870 of 18,940 contacts as WISMO, which is 31%. Most of those customers already had a tracking number, but the order page could not tell them when the parcel would arrive. Today the page shows `Order placed` until dispatch and `Shipped` after it, with the tracking number, and it never changes after that. Customers copy the number into the carrier's own site, and the ones who get lost there contact us.
* * *
##   

## Solution
* * *
Customers see where their parcel is on the order page, on web, iOS and Android. The page moves through the statuses as the parcel moves, with one timeline per parcel and the expected delivery day and window under the current status when the carrier gives one. That answers the problem where the customer already looks, so the carrier's site becomes an option instead of the next step.

**Expected outcomes**
* * *
*   Customers learn where their parcel is from the order page, without copying the tracking number into the carrier's site
*   The WISMO share of contacts falls from 31% to under 20% within two months of release
*   Contacts from customers confused by the timeline do not rise

#### **Tasks**
* * *
*   [FE - iOS - TRACK - Order page tracking timeline](<002.1 - task-order-tracking-ios.md>)
*   [FE - Android - TRACK - Order page tracking timeline](<002.2 - task-order-tracking-android.md>)
*   [FE - Web - TRACK - Order page tracking timeline](<002.3 - task-order-tracking-web.md>)
*   [BE - TRACK - Carrier tracking webhook](<002.4 - task-carrier-tracking-webhook.md>)
* * *
##   

## Requirements
* * *
**Status steps**
* * *
- [] `Order placed` comes from orders-service when the payment is authorised
- [] `Packed` comes from the warehouse system into orders-service, which already receives it
- [] `Shipped` comes from carrier codes `PU` and `IT`
- [] `Out for delivery` comes from carrier code `OD`
- [] `Delivery failed` comes from carrier code `EX` and shows no reason in this story
- [] After `Delivery failed`, a new `OD` moves the order back to `Out for delivery`
- [] The timeline keeps every step that happened, each with its date and time

**Delivered**
* * *
**Open:** Whether a `DL` with `delivered_to` set to `parcel_point` shows `Delivered`. That event arrives when the parcel is dropped at a parcel point, not when the customer collects it. Hamid settles it.

- [] `Delivered` comes from carrier code `DL` when `delivered_to` is `recipient` or `neighbour`

**Event order and status source**
* * *
**Open:** Which service holds the status the order page reads, and how a tracking event reaches it. The Post-purchase and Fulfilment teams settle it.

- [] Events are ordered by `occurred_at`, never by arrival
- [] An event with an `occurred_at` older than the newest event held for its parcel is stored in the history and does not change the status shown

**Delivery window**
* * *
**Open:** The time zone the day and window show in. The design shows no time zone, and each time the carrier sends carries its own offset. Hamid settles it.

- [] When the carrier sends a window, the estimate shows the day and the window under the current status, as `Arriving Thursday 1 October` and `Between 10:00 and 14:00`
- [] When the carrier sends no window, the page shows no estimate, and no estimate is derived from the dispatch date
- [] The newest window by `occurred_at` is the one shown when the carrier changes it
- [] `OD` always carries a window, and `IT` carries one only when the carrier can predict the day

**Parcels and pallet items**
* * *
- [] An order with several parcels shows one timeline per parcel, with that parcel's items under it
- [] An item over `30 kg` or `120 cm` on its longest side goes by the pallet carrier, which sends no tracking events
- [] An order with a parcel item and a pallet item shows a timeline for the parcel and keeps today's page for the pallet item
- [] The page for a pallet item keeps today's content and adds the line `The delivery company will call you to book a delivery slot`

**Tracking history**
* * *
- [] Tracking events are kept for `90 days` after delivery
- [] Once the `90 days` after delivery have passed, the order page shows the last status only

**Shipping email**
* * *
- [] The shipping email keeps the tracking number

**Status text**
* * *
- [] Status text is translated for six locales: `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR` and `en-GB`
- [] Status copy is written in English first and then translated

**Platforms**
* * *
- [] The apps support iOS 16 and later and Android 9 and later
- [] Web is one responsive build for desktop and mobile browsers, supported on the two latest versions of each major browser

**Analytics**
* * *
- [] No task in this story sends a new analytics event
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1 ) **The customer sees each status as the parcel moves**
* * *
*   **Given** a customer on web, iOS or Android whose order has been dispatched
*   **When** the carrier reports a new status for the parcel
*   **Then** the order page shows that status on the timeline
*   **And** every earlier step stays on the timeline, with its date and time
* * *
- [] _Mark as done, if the criteria are met_

2 ) **The customer sees the delivery day and window**
* * *
*   **Given** the carrier has sent a window for the parcel
*   **When** the customer opens the order page
*   **Then** the page shows the delivery day and window under the current status
*   **And** when the carrier has sent no window, the page shows no estimate
* * *
- [] _Mark as done, if the criteria are met_

3 ) **A late event does not move the status back**
* * *
*   **Given** the parcel is out for delivery
*   **When** an older event for the parcel arrives after the newest one
*   **Then** the order page still shows out for delivery as the current status
*   **And** the older step appears on the timeline in its place, with its date and time
* * *
- [] _Mark as done, if the criteria are met_

4 ) **A failed delivery can be followed by a new attempt**
* * *
*   **Given** the carrier has marked a delivery as failed
*   **When** the carrier sends a new out-for-delivery event for the parcel
*   **Then** the order page shows out for delivery as the current status
*   **And** the failed attempt stays on the timeline, with its date and time
* * *
- [] _Mark as done, if the criteria are met_

5 ) **Each parcel in a multi-parcel order has its own timeline**
* * *
*   **Given** an order with several parcels
*   **When** the customer opens the order page
*   **Then** each parcel shows its own timeline, with that parcel's items under it
* * *
- [] _Mark as done, if the criteria are met_

6 ) **Pallet items keep today's page**
* * *
*   **Given** an order with an item that goes by the pallet carrier
*   **When** the customer opens the order page
*   **Then** the pallet item shows today's page with the pallet booking line
*   **And** a parcel item in the same order keeps its timeline
* * *
- [] _Mark as done, if the criteria are met_

7 ) **Old history gives way to the last status**
* * *
*   **Given** a parcel delivered longer ago than tracking history is kept
*   **When** the customer opens the order page
*   **Then** the page shows the last status only
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
*   TBD...

#### External dependencies
* * *
*   **App store approval** - approves the iOS and Android releases that carry the timeline, and the timeline reaches most app customers about a week after release. Date: TBD...

#### Rabbit holes
* * *
*   The time zone of the delivery window, which Requirements leaves open for Hamid to settle
*   Which service holds the status the order page reads and how a tracking event reaches it, which Requirements leaves open for the Post-purchase and Fulfilment teams to settle
*   Whether a `DL` with `delivered_to` set to `parcel_point` shows `Delivered`, which Requirements leaves open for Hamid to settle

#### No-gos
* * *
*   A push notification for each status, which comes once the events are trusted
*   Changing the delivery address or day after dispatch
*   Tracking for return parcels
*   Tracking for pallet items, since the pallet carrier sends no tracking events
*   A reason on `Delivery failed`
*   DATA events for the timeline being viewed and the carrier link being tapped, which wait for a later story
*   A task for `Packed`, since orders-service already receives it from the warehouse system
* * *
