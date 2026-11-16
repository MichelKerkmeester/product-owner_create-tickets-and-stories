# Customer - Ordering - Pickup slot picker

* * *
## Problem
* * *
Customers who order ahead cannot choose when to collect, so the counter fills at eight and empties by ten. Staff bake for a rush that never spreads out. Waste rises on slow mornings and queues lengthen on busy ones.
* * *
##   

## Solution
* * *
Let a customer pick a pickup slot before paying.

**Expected outcomes**
* * *
*   Pickups spread across the morning
* * *
##   

## Requirements
* * *
**Slot sheet**
* * *
- [] The sheet title reads `Choose your pickup time`
- [] The subtitle reads `Slots fill up fast on weekends`
- [] The primary action reads `Confirm pickup slot`
- [] The secondary action reads `Back to basket`
- [] A full slot shows `This slot is full`
- [] The empty state reads `No slots left today.`
- [] The toast reads `Pickup time saved`
- [] The error reads `Something went wrong, try again`
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
*   **And** the footer reads `Collect at the side door`
* * *
- [] _Mark as done, if the criteria are met_
