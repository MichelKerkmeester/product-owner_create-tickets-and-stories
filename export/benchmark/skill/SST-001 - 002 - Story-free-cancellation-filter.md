# Guest - Search - Free cancellation filter

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
A Free cancellation filter in Guest app search on iOS, Android and web shows only stays a guest can still cancel for free, with that rate's price and deadline.

Search squad owns it, with Tomas as product manager, Ines on frames and Dario leading the `search-service` change.

#### Problem
* * *
"Can I cancel this for free?" was the top pre-booking Guest Support question in August, about one in six chats, while 44% of bookings used a free cancellation rate plan. Guests find those rates only on property pages.

#### Solution
* * *
A filter sheet switch answers the question in search, before a guest opens a property.

It holds through one search, because a guest comparing properties expects the list to stay filtered.

**Expected outcomes**
* * *
*   Guests find free cancellation stays without opening each property page
*   Fewer pre-booking Guest Support chats ask about free cancellation
##   

## Requirements
* * *
**Search filter sheet**
* * *
- [] The filter sits below Price and Star rating, today the sheet's only two filters
- [] It is a single on and off switch

**Results with the filter on**
* * *
- [] A stay shows only if a rate plan for the searched dates, guests and rooms has free cancellation with its deadline still ahead
- [] The card shows the cheapest free cancellation price, even when a non-refundable one is cheaper
- [] The results header shows the filtered count
- [] Kickoff reference: Lisbon, 4 nights, 2 adults, `1,146` stays unfiltered and `312` filtered

**Filter state**
* * *
- [] It stays on when the guest changes dates or guests in the same search
- [] It stays on when the guest opens a property and returns
- [] It turns off on a new search from the home screen

**Result card badge**
* * *
- [] With the filter on, each card shows its priced rate plan's deadline, as `Free cancellation until 14 Oct`
- [] The deadline is check-in minus the partner's cancellation window, so 14 days before check-in for a 14-day window
- [] It uses the property's local date, because guests abroad check it against their confirmation email
- [] It uses the `d MMM` pattern in the guest's locale, with no year
- [] With the filter off, cards stay as today

**Empty state**
* * *
- [] With no match, the list shows `No stays with free cancellation for these dates` and one button, `Clear filter`
- [] `Clear filter` switches the filter off and reruns the search

**Tracking**
* * *
- [] Turning the filter on fires the existing `filter_applied` event with `filter_name` set to `free_cancellation`
- [] No tracking plan change, as Nadia confirmed on 2026-09-17

**Release**
* * *
- [] The filter ships on iOS, Android and web
- [] iOS and Android ship in `8.13.0`
- [] Web ships the same week
- [] `search-service` ships first, so no app shows a filter it cannot apply

**Unchanged in this release**
* * *
- [] Map view pins keep showing every stay, filter on or off
- [] No sort by cancellation deadline
- [] No Partner Hub change, because partners already set free cancellation per rate plan
- [] No property page badge, since it already lists each rate plan's policy
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **Guests see only stays they can still cancel for free**
* * *
*   **Given** a guest has run a search
*   **When** they turn on the filter
*   **Then** results hold only stays with a free cancellation rate plan whose deadline has not passed
*   **And** the header shows the filtered count
* * *
- [] _Mark as done, if the criteria are met_

2\. **The result card shows the free cancellation rate the guest would book**
* * *
*   **Given** a stay with a free cancellation rate plan and a cheaper non-refundable one
*   **When** it appears with the filter on
*   **Then** the card shows the cheapest free cancellation price
*   **And** the badge shows that rate plan's deadline
* * *
- [] _Mark as done, if the criteria are met_

3\. **A guest abroad sees the deadline on the property's calendar**
* * *
*   **Given** a guest in another time zone than the property
*   **When** they read a card's badge
*   **Then** the date is the property's local date in the guest's locale format
* * *
- [] _Mark as done, if the criteria are met_

4\. **The filter holds for the whole search**
* * *
*   **Given** a guest has the filter on
*   **When** they change dates or guests, or open a property and go back
*   **Then** the filter stays on and results reflect it
*   **And** a new search from the home screen turns it off
* * *
- [] _Mark as done, if the criteria are met_

5\. **A guest with no matches can get back to results in one step**
* * *
*   **Given** no stay matches with the filter on
*   **When** the guest taps `Clear filter`
*   **Then** the filter is off and the same search shows unfiltered results
* * *
- [] _Mark as done, if the criteria are met_

6\. **Search is unchanged for guests who leave the filter off**
* * *
*   **Given** the filter is off
*   **When** a guest searches and browses
*   **Then** results, prices and cards match the previous release
* * *
- [] _Mark as done, if the criteria are met_

7\. **The Search squad can count filter use from existing analytics**
* * *
*   **Given** a guest on iOS, Android or web
*   **When** they turn the filter on
*   **Then** `events-collector` receives the event with the filter identified, and the Data team's tracking plan needs no new row
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
