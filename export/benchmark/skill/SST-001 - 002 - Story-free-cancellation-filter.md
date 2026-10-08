# Guest - Search - Free cancellation filter

* * *
## Problem
* * *
Guests can find free cancellation rates only by opening each property page one at a time. Whether a stay can be cancelled for free is the most common question in Guest Support chats before a booking, and about one in six of those chats in August asked it. Free cancellation is already common, since 44% of August bookings were on a free cancellation rate plan, yet search gives guests no way to find those rates.
* * *
##   

## Solution
* * *
Search gets a Free cancellation filter that narrows results to stays the guest can cancel for free. With the filter on, each card shows the cheapest free cancellation price and that rate's deadline, and the filter holds through changes to dates or guests and through visits to a property until a new search starts. Sorting by cancellation deadline and a property page badge stay out of this release, and no Partner Hub change ships with it.

**Expected outcomes**
* * *
*   Guests find stays with free cancellation in search without opening each property page
*   Guests compare the cheapest free cancellation price and its deadline on each result card
*   Guests keep their filtered results while they change dates or guests, or open a property
*   Filter use is measured through the existing `filter_applied` event
* * *
##   

## Requirements
* * *
**Filter sheet**
* * *
- [] The Free cancellation filter sits below Price and Star rating in the search filter sheet
- [] The filter is a single on and off switch

**Results**
* * *
- [] With the filter on, a stay appears only if at least one rate plan for the searched dates, guests and rooms has free cancellation and a deadline that has not passed
- [] With the filter on, the price on each result card is the cheapest free cancellation rate plan, even when a non-refundable rate is cheaper
- [] With the filter on, the results header shows the count of matching stays
- [] The test search for Lisbon, `4` nights and `2` adults, shows `1,146` stays with the filter off and `312` stays with the filter on
- [] The filter stays on while the guest changes dates or guests in the same search
- [] The filter stays on when the guest opens a property and goes back to the results
- [] The filter turns off when the guest starts a new search from the home screen

**Result card badge**
* * *
- [] With the filter on, each result card shows the deadline of the rate plan whose price is on the card, in the form `Free cancellation until 14 Oct`
- [] The deadline is the check-in date minus the partner's cancellation window, so a window of `14` days gives a deadline `14` days before check-in
- [] The date is the property's local date, whatever time zone the guest is in
- [] The date uses the `d MMM` pattern in the guest's locale, with no year
- [] With the filter off, result cards stay as they are today

**Empty state**
* * *
- [] When no stay matches, the results list shows `No stays with free cancellation for these dates` and one button, `Clear filter`
- [] `Clear filter` switches the filter off and reruns the same search

**Tracking**
* * *
- [] Turning the filter on fires `filter_applied` with `filter_name` set to `free_cancellation`
- [] The change adds no new event and needs no tracking plan change

**Map view**
* * *
- [] With the filter on, map pins keep showing every stay in this release

**Release**
* * *
- [] iOS and Android ship in `8.13.0`
- [] Web ships in the same week as the apps
- [] `search-service` ships first, so no app shows a filter the service cannot apply
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1 ) **Filtered results show only stays the guest can cancel for free**
* * *
*   **Given** a guest has a search with results
*   **When** the guest turns the Free cancellation filter on
*   **Then** every stay shown has free cancellation for the searched dates, guests and rooms, with a deadline that has not passed
*   **And** the results header shows how many stays match
- [] _Mark as done, if the criteria are met_

2 ) **Result cards show the cheapest free cancellation price and its deadline**
* * *
*   **Given** the filter is on
*   **When** a result card shows its price
*   **Then** the price is the cheapest free cancellation rate plan, even when a non-refundable rate is cheaper
*   **And** the card shows the deadline of that same rate plan
- [] _Mark as done, if the criteria are met_

3 ) **The filter holds while the guest moves around the search**
* * *
*   **Given** the filter is on
*   **When** the guest changes dates or guests, or opens a property and goes back to the results
*   **Then** the filter stays on
*   **And** the results stay filtered
- [] _Mark as done, if the criteria are met_

4 ) **A new search from the home screen starts unfiltered**
* * *
*   **Given** the filter is on
*   **When** the guest starts a new search from the home screen
*   **Then** the filter is off
- [] _Mark as done, if the criteria are met_

5 ) **A search with no matching stays explains why and lets the guest clear the filter**
* * *
*   **Given** no stay matches the filter for the searched dates
*   **When** the results load
*   **Then** the results list explains that no stays have free cancellation for these dates
*   **And** the guest can clear the filter with one button
*   **And** clearing the filter reruns the same search with the filter off
- [] _Mark as done, if the criteria are met_

6 ) **Turning the filter on is recorded in the existing filter analytics**
* * *
*   **Given** the filter is off
*   **When** the guest turns the filter on
*   **Then** the existing filter event records that the filter was turned on
- [] _Mark as done, if the criteria are met_
* * *
##   
