# Guest - Search - Free cancellation filter

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
A Free cancellation filter for search in the Guest app on iOS, Android and web shows only stays the guest can still cancel for free, with that rate's price and deadline.

#### Problem
* * *
"Can I cancel this for free?" is the top pre-booking Guest Support question, about one in six chats in August. 44% of August bookings used a free cancellation rate plan, yet guests find these rates only on each property page.

#### Solution
* * *
Guests get the answer on the results list, because that is where they compare stays.

**Expected outcomes**
* * *
*   Guests find free cancellation stays from results
*   Fewer pre-booking Guest Support chats ask about it
*   The card deadline matches the confirmation email
* * *
##   

## Requirements
* * *
**Free cancellation filter**
* * *
- [] `Free cancellation` is one on and off switch in the filter sheet, below `Price` and `Star rating`
- [] With it on, only stays with an unexpired free cancellation rate plan for the searched dates, guests and rooms show
- [] Cards then price the cheapest free cancellation rate plan, even if a non-refundable rate is cheaper
- [] The header shows the filtered count
- [] Test search: Lisbon, `4 nights`, `2 adults` goes from `1,146` stays to `312`
- [] It stays on through date or guest changes, or a property visit and back
- [] A new home screen search turns it off

**Result card badge**
* * *
- [] With the filter on, cards show their rate plan's deadline, as `Free cancellation until 14 Oct`
- [] The deadline is check-in minus the partner's cancellation window, so `14 days` means 14 days before
- [] The deadline uses the property's local date, not the device's
- [] The date uses `d MMM` in the guest's locale, no year
- [] With the filter off, cards stay as today

**Empty state**
* * *
- [] With no match, the list shows `No stays with free cancellation for these dates` and one button, `Clear filter`
- [] `Clear filter` switches the filter off and reruns the search

**Tracking**
* * *
- [] No new event is added
- [] Turning the filter on fires the existing `filter_applied` with `filter_name` set to `free_cancellation`
- [] The tracking plan does not change, as Nadia confirmed on `2026-09-17`

**Release**
* * *
- [] iOS and Android ship in `8.13.0`, and web the same week
- [] `search-service` ships first, so no app shows an unsupported filter

**Not in this release**
* * *
- [] The map view is unchanged, its pins showing every stay
- [] No sorting by cancellation deadline
- [] Partner Hub is unchanged, because partners already set free cancellation per rate plan
- [] No badge on the property page, because it already lists each rate plan's policy
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **With the filter on, results show only stays the guest can still cancel for free**
* * *
*   **Given** a guest has searched
*   **When** they turn the filter on
*   **Then** list and count show only stays with an unexpired free cancellation rate for the searched dates, guests and rooms
*   **And** each card shows the free cancellation price, even when a non-refundable rate is cheaper
* * *
- [] _Mark as done, if the criteria are met_

2\. **The card shows a deadline the guest can trust**
* * *
*   **Given** the filter is on
*   **When** the guest reads a card
*   **Then** it shows its rate plan's deadline in property-local date and the guest's language
*   **And** after booking that rate plan, the confirmation email shows the same date
* * *
- [] _Mark as done, if the criteria are met_

3\. **With the filter off, results stay as they are today**
* * *
*   **Given** the filter is off
*   **When** the guest views results
*   **Then** stays, prices and cards are unchanged
* * *
- [] _Mark as done, if the criteria are met_

4\. **The filter stays on for the rest of the same search**
* * *
*   **Given** the filter is on
*   **When** the guest changes dates or guests, or opens a property and returns
*   **Then** the filter stays on and applied
*   **And** a new search from the home screen starts with it off
* * *
- [] _Mark as done, if the criteria are met_

5\. **A search with no matching stays still gives the guest a way forward**
* * *
*   **Given** the filter is on and no stay matches
*   **When** results load
*   **Then** the empty state offers one action to clear the filter
*   **And** it switches the filter off and shows the full results
* * *
- [] _Mark as done, if the criteria are met_

6\. **Turning the filter on is recorded in analytics**
* * *
*   **Given** a guest on any platform
*   **When** they turn the filter on
*   **Then** the existing filter event records it for this filter, with no new event
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
