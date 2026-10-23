````markdown
# Guest - Search - Free cancellation filter

* * *
## Problem
* * *
Guests who want to cancel for free can only check a rate plan by opening each property page one at a time. "Can I cancel this for free?" is the most common question in Guest Support chats before a booking, at about one in six pre-booking chats in August, and 44% of August bookings landed on a free cancellation rate plan. The cost lands twice: the guest does the work of opening page after page, and Guest Support answers what the search could have shown.
* * *
##   

## Solution
* * *
A free cancellation switch joins the filters the search sheet already holds. With it on, the results list answers one question: which stays can be cancelled at no cost, at what price, and until when. That answer sits on the card, so the guest never opens a property to find it.

The badge names the date the refund stops, taken from the rate plan the card prices and read as a date at the property, because guests abroad check it against their confirmation email.

The filter stays with the guest for the length of a search, so comparing stays never means setting it again.
* * *

**Expected outcomes**
* * *
*   A guest sees which stays can be cancelled for free without opening a property page
*   The price on a filtered result is the rate the guest can actually cancel for free
*   The date on a result card matches what the guest will read in their confirmation email
*   The filter holds while the guest compares stays, through a date change, a guest change and a look at a property
* * *
##   

## Requirements
* * *
**Filter sheet**
* * *
- [] The filter sits in the search filter sheet, below `Price` and `Star rating`
- [] The filter is a single on and off switch
- [] The filter stays on while the guest changes dates or guests in the same search
- [] The filter stays on when the guest opens a property page and returns to the results
- [] The filter turns off when the guest starts a new search from the home screen

**Results list**
* * *
- [] With the filter on, a stay shows only if a rate plan for the searched dates, guests and rooms has free cancellation
- [] A rate plan whose free cancellation deadline has passed does not qualify a stay
- [] The results header shows the count for the filtered search
- [] The Lisbon test search, 4 nights with 2 adults, goes from `1,146` stays to `312` stays with the filter on

**Result card**
* * *
- [] The card price is the cheapest free cancellation rate plan, even when a non-refundable rate is cheaper
- [] With the filter on, every result card shows the deadline of the rate plan whose price is on the card
- [] The badge reads `Free cancellation until` followed by the deadline date, as in `Free cancellation until 14 Oct`
- [] The deadline is the check-in date minus the partner's cancellation window
- [] A partner who allows free cancellation up to 14 days before check-in gets a deadline 14 days before check-in
- [] The badge date is the property's local date, so a guest abroad reads the same date as their confirmation email
- [] The date uses the `d MMM` pattern in the guest's locale, so a day and a short month name with no year
- [] With the filter off, result cards stay as they are today

**Empty state**
* * *
- [] When no stay matches, the results list shows `No stays with free cancellation for these dates`
- [] The empty state carries one button, `Clear filter`
- [] `Clear filter` switches the filter off and reruns the same search

**Tracking**
* * *
- [] Turning the filter on fires no new event
- [] Turning the filter on fires the existing `filter_applied` event with `filter_name` set to `free_cancellation`
- [] The change needs no tracking plan change

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

1 ) **Turning the filter on narrows the results to stays the guest can cancel for free**
* * *
*   **Given** a guest searching Lisbon for 4 nights with 2 adults
*   **When** the guest turns the free cancellation filter on
*   **Then** the results list holds only stays with a free cancellation rate the guest can cancel before its deadline
*   **And** the results header count matches the stays on screen
* * *
- [] _Mark as done, if the criteria are met_

2 ) **A filtered card prices a rate the guest can cancel for free**
* * *
*   **Given** a stay whose cheapest rate is non-refundable
*   **When** it appears in filtered results
*   **Then** the card prices the cheapest free cancellation rate for that stay
* * *
- [] _Mark as done, if the criteria are met_

3 ) **The card names when free cancellation stops**
* * *
*   **Given** a stay in filtered results
*   **When** the card renders
*   **Then** the card names the date free cancellation ends for the rate plan it prices
*   **And** the guest reads that date at the property, matching the date in their confirmation email
* * *
- [] _Mark as done, if the criteria are met_

4 ) **The filter holds through the search**
* * *
*   **Given** the guest has the free cancellation filter on
*   **When** they change the dates or guests, or open a property and return to the results
*   **Then** the filter is still on
*   **And** the results still hold the filtered set
* * *
- [] _Mark as done, if the criteria are met_

5 ) **A new search starts from a clean sheet**
* * *
*   **Given** the guest has the free cancellation filter on
*   **When** they start a new search from the home screen
*   **Then** the filter is off
* * *
- [] _Mark as done, if the criteria are met_

6 ) **The empty state gets the guest back to results**
* * *
*   **Given** no stay matches the free cancellation filter
*   **When** the results list renders
*   **Then** the guest sees a message explaining that no stay matches
*   **And** the guest sees one action to clear the filter
*   **And** that action reruns the same search with the filter off
* * *
- [] _Mark as done, if the criteria are met_

7 ) **The filter reports through the existing event**
* * *
*   **Given** the free cancellation filter is off
*   **When** the guest turns it on
*   **Then** the existing `filter_applied` event fires with `filter_name` set to `free_cancellation`
*   **And** no new event fires
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
````

Export-equivalent path: `export/002 - Story-free-cancellation-filter.md`
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality: every floor met | Kind: Story | Energy: Standard

The Story gives the Search squad one switch in the filter sheet that narrows results to stays with a free cancellation rate, prices the refundable rate and names its deadline on every card. Requirements carry Tomas's values as written: the `1,146` to `312` test count, the `d MMM` pattern, the empty state copy, the `filter_applied` mapping and the `8.13.0` release. Guest Support's two asks land as the property-local badge date and the filter surviving a property visit.

### Open items
1. **Both asks in scope for `8.13.0`**
   - **Situation:** Both Guest Support asks are written as requirements in this release, since nothing in your message marked either as a follow-up
   - **Open:** Strike either one if it belongs after `8.13.0`
2. **Badge date and locale format**
   - **Situation:** The ask sets the badge to the property's local date, while Tomas sets the `d MMM` pattern in the guest's locale, so I read the property as governing the date and the locale as governing the format
   - **Open:** Confirm the locale still governs the format, or say if the ask replaces it
3. **Delivery section left out**
   - **Situation:** Tomas rules out the map view, sorting by deadline, any Partner Hub change and a property page badge, and you did not ask for a delivery view, so no `## Delivery` is written
   - **Open:** Say the word and I'll add one with those four as No-gos

Want me to change anything?