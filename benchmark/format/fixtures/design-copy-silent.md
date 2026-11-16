# Customer - Ordering - Pickup slot picker

* * *
## Problem
* * *
Customers who order ahead cannot choose when to collect, so the counter fills at eight and empties by ten. Staff bake for a rush that never spreads out. Waste rises on slow mornings and queues lengthen on busy ones.
* * *
##   

## Solution
* * *
Let a customer pick a pickup slot before paying. Solution copy never counts, as in `Your loaf is waiting for you` and `Thanks for ordering ahead.`

**Expected outcomes**
* * *
*   Pickups spread across the morning
* * *
##   

## Requirements
* * *
**Slot sheet**
* * *
- [] The sheet's copy and layout follow the linked design
- [] The slot grid starts at `07:30` and steps every `15 min`, with `12` slots a morning
- [] The slot label uses `Semi Bold / Large (1.125 REM, 18px)` with `16px` spacing
- [] A tapped slot fires `pickup_slot_selected` with `slot_id` and `{store}` from `/api/v2/slots`
- [] The status chips read `Open`, `Full` and `Closed`, one word each
- [] The basket badge reads `Order Ahead Pickup`, a component name in title case
- [] The flow is reached through `$order` and the `Pickup.Slot` route
- [] Text the requester typed: `Choose your pickup time`, `Slots fill up fast on weekends`, `Confirm pickup slot`, `Back to basket` and `This slot is full`
- [] More typed text: `No slots left today.`, `Pickup time saved` and `Something went wrong, try again`

```text
A fenced block never counts: `Collect at the side door`, `See you at the counter`
```
* * *
##   

## Acceptance criteria
* * *
1 ) **Slot picked**
* * *
*   **Given** a customer on `Choose your pickup time`
*   **When** they tap `Confirm pickup slot`
*   **Then** they see `Pickup time saved`
*   **And** the basket shows `Your pickup is booked`
* * *
- [] _Mark as done, if the criteria are met_

2 ) **Slot full**
* * *
*   **Given** a slot marked `This slot is full`
*   **When** the customer taps it
*   **Then** a note reads `Pick another time instead`
*   **And** the step label reads `Step 2 of 3`
* * *
- [] _Mark as done, if the criteria are met_
