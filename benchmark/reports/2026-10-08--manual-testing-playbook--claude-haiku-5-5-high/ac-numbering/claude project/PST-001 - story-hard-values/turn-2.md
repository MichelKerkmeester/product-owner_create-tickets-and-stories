```markdown
# Guest - Search - Free cancellation filter

* * *
## Problem
* * *
Guests ask "Can I cancel this for free?" more than any other question in Guest Support chats before a booking, about one in six of those chats in August. Free cancellation rate plans were 44% of August bookings, yet guests can only find them by opening each property page one at a time. Guest Support answers the question chat by chat, and search does not show the answer at all.
* * *
##   

## Solution
* * *
The search filter sheet gets one new switch, Free cancellation, below Price and Star rating. With it on, a guest sees only stays that have a rate plan still free to cancel for their dates, guests and rooms, and each result shows that plan's price and deadline. The switch holds while the guest adjusts the search or looks at a property, and it clears when they start a new search.

**Expected outcomes**
* * *
*   Guests find stays with free cancellation from the search results, without opening each property page
*   Guests see the free cancellation deadline on each result while the filter is on
* * *
##   

## Requirements
* * *
**Filter sheet**
* * *
- [] A `Free cancellation` on and off switch in the search filter sheet, below Price and Star rating

**Results**
* * *
- [] With the filter on, a stay shows only if at least one rate plan for the searched dates, guests and rooms has free cancellation and its deadline has not passed
- [] With the filter on, the price on each result card is the cheapest free cancellation rate plan, even when a non-refundable rate is cheaper
- [] With the filter on, the results header shows the matching count, so the Lisbon test search for 4 nights and 2 adults shows `312` stays against `1,146` with the filter off

**Result card badge**
* * *
- [] With the filter on, every result card shows `Free cancellation until {date}` for the rate plan whose price is on the card, for example `Free cancellation until 14 Oct`
- [] The deadline is the check-in date minus the partner's cancellation window, so a partner allowing free cancellation up to 14 days before check-in gives a deadline 14 days before check-in
- [] The date uses the `d MMM` pattern in the guest's locale, with no year
- [] The date is the property's local date and is not converted to the guest's time zone
- [] With the filter off, result cards stay as they are today

**Empty state**
* * *
- [] When no stay matches, the results list shows `No stays with free cancellation for these dates`
- [] The empty state has one button, `Clear filter`
- [] `Clear filter` switches the filter off and reruns the same search

**Filter state**
* * *
- [] The filter stays on while the guest changes dates or guests in the same search
- [] The filter stays on when the guest opens a property and goes back to the results
- [] The filter turns off when the guest starts a new search from the home screen

**Tracking**
* * *
- [] Turning the filter on fires the existing `filter_applied` event with `filter_name` set to `free_cancellation`
- [] No new analytics event is added

**Release**
* * *
- [] iOS and Android ship in `8.13.0`
- [] Web ships in the same week as the apps
- [] `search-service` ships first, so no app shows a filter the service cannot apply

**Out of this release**
* * *
- [] The map view keeps showing every stay as a pin
- [] Sorting by cancellation deadline is not added
- [] Partner Hub does not change, and partners keep setting free cancellation per rate plan
- [] The property page does not get a free cancellation badge
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1 ) **Filter narrows results to stays with free cancellation**
* * *
*   **Given** the guest has searched for a stay with the filter off
*   **When** they turn the free cancellation filter on
*   **Then** the results show only stays with a rate plan that is free to cancel for their dates, guests and rooms
*   **And** the results header shows the matching count
* * *
- [] _Mark as done, if the criteria are met_

2 ) **Price and deadline come from the cheapest free cancellation rate**
* * *
*   **Given** a stay has a non-refundable rate that is cheaper than its free cancellation rate
*   **When** the guest has the filter on
*   **Then** the result card shows the price of the cheapest free cancellation rate
*   **And** the card shows the deadline of that rate plan
* * *
- [] _Mark as done, if the criteria are met_

3 ) **Deadline date matches the property's local date**
* * *
*   **Given** the guest is in a different time zone from the property
*   **When** they view a result with the filter on
*   **Then** the deadline date is the property's local date
*   **And** the date reads in the guest's locale without a year
* * *
- [] _Mark as done, if the criteria are met_

4 ) **Filter holds through date changes and a property visit**
* * *
*   **Given** the filter is on in a search
*   **When** the guest changes dates or guests, or opens a property and goes back to the results
*   **Then** the filter stays on
* * *
- [] _Mark as done, if the criteria are met_

5 ) **Filter resets on a new search**
* * *
*   **Given** the filter is on
*   **When** the guest starts a new search from the home screen
*   **Then** the filter is off
* * *
- [] _Mark as done, if the criteria are met_

6 ) **Empty state offers a way out**
* * *
*   **Given** no stay matches the searched dates, guests and rooms with the filter on
*   **When** the results list loads
*   **Then** the results list explains that no stay has free cancellation for these dates
*   **And** the guest can clear the filter with one action
*   **And** clearing the filter reruns the same search
* * *
- [] _Mark as done, if the criteria are met_

7 ) **Turning the filter on is tracked**
* * *
*   **Given** the filter is off on the results list
*   **When** the guest turns the filter on
*   **Then** the existing filter event fires with free cancellation as the filter name
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/NNN - Story-free-cancellation-filter.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

This is a Story for one feature area. I wrote the Requirements from Tomas's notes and the two Guest Support asks, which are the local-date badge and the filter staying on through a property visit. Please check these points before it goes to the squad:

- **Android build:** I kept `8.13.0` as Tomas wrote it. Android carried a different number from iOS on the last train, so confirm it when the build is cut.
- **Deadline cut-off:** Neither the notes nor your answers set the time of day or the time zone the deadline closes at. I kept "its deadline has not passed" as written. If you want a time, it becomes a Requirement.
- **Wording I wrote:** The Problem and Expected outcomes are my wording drawn from the notes. The "Out of this release" group comes from the notes' "Not in this release" section. I placed it in Requirements because no Delivery section was requested.

I left out the Delivery section because nobody asked for it and no item is open.