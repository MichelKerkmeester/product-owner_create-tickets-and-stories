# Guest - Search - Free cancellation filter

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
This story adds a Free cancellation filter to search in the Guest app on iOS, Android and web. With it on, a guest sees only stays they can still cancel for free, priced at the free cancellation rate and marked with the date the free cancellation ends.

The Search squad owns it. Tomas is the product manager, Ines owns the frames and Dario leads the `search-service` change.

### Problem
* * *
"Can I cancel this for free?" is the most common question in pre-booking Guest Support chats, at about one in six in August. In the same month, 44% of bookings were on a free cancellation rate plan. Guests can only find those rates today by opening each property page, so the question lands on Guest Support instead of being answered in search.

### Solution
* * *
A single switch in the search filter sheet narrows results to stays with a free cancellation rate the guest can still book, and each result card shows that rate's price and deadline. Guests get the answer before opening a property, so the card must show the rate they would book and a date to check against their confirmation email.

The filter stays on for as long as the guest works through one search, because a guest who compares properties expects the filtered list to still be there when they return.

#### **Expected outcomes**
* * *
*   Guests find free cancellation stays from the results list without opening each property page
*   Fewer pre-booking Guest Support chats ask whether a stay can be cancelled for free
##   

## Requirements
* * *
**Search filter sheet**
* * *
*   The Free cancellation filter sits below Price and Star rating, which are the only two filters in the sheet today
*   The filter is a single on and off switch

**Results with the filter on**
* * *
*   A stay shows only if a rate plan for the searched dates, guests and rooms has free cancellation and its deadline has not passed
*   The price on the result card is the cheapest free cancellation rate plan, even when a non-refundable rate plan is cheaper
*   The results header shows the filtered count
*   Reference search at the kickoff: Lisbon, 4 nights, 2 adults, `1,146` stays with the filter off and `312` with it on

**Filter state**
* * *
*   The filter stays on when the guest changes dates or guests in the same search
*   The filter stays on when the guest opens a property and goes back to the results
*   The filter turns off when the guest starts a new search from the home screen

**Result card badge**
* * *
*   With the filter on, every result card shows the deadline of the rate plan whose price is on the card, as `Free cancellation until 14 Oct`
*   The deadline is the check-in date minus the partner's cancellation window, so a 14-day window gives a deadline 14 days before check-in
*   The deadline is the property's local date, because guests abroad check it against their confirmation email
*   The date uses the `d MMM` pattern in the guest's locale: a day and a short month name, with no year
*   With the filter off, result cards stay as they are today

**Empty state**
* * *
*   When no stay matches, the results list shows `No stays with free cancellation for these dates` and one button, `Clear filter`
*   `Clear filter` switches the filter off and reruns the same search

**Tracking**
* * *
*   No new event: turning the filter on fires the existing `filter_applied` event with `filter_name` set to `free_cancellation`
*   No tracking plan change, as Nadia confirmed on 2026-09-17

**Release**
* * *
*   The filter ships on iOS, Android and web
*   iOS and Android ship in `8.13.0`
*   Web ships in the same week as the apps
*   `search-service` ships first, so no app shows a filter the service cannot apply

**Unchanged in this release**
* * *
*   Map view pins keep showing every stay, whether the filter is on or off
*   No sort by cancellation deadline
*   No Partner Hub change, because partners already set free cancellation per rate plan
*   No badge on the property page, which already lists the policy for each rate plan
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **Guests see only stays they can still cancel for free**
* * *
*   **Given** a guest has run a search
*   **When** they turn on the Free cancellation filter
*   **Then** the results hold only stays with a free cancellation rate plan for their dates, guests and rooms whose deadline has not passed
*   **And** the results header shows the filtered count
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **The result card shows the free cancellation rate the guest would book**
* * *
*   **Given** a stay has both a free cancellation rate plan and a cheaper non-refundable one
*   **When** it appears in results with the filter on
*   **Then** the card shows the price of the cheapest free cancellation rate plan
*   **And** the badge shows the deadline of that same rate plan
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **A guest abroad sees the deadline on the property's calendar**
* * *
*   **Given** a guest searches from a time zone other than the property's
*   **When** they read the badge on a result card
*   **Then** the date is the property's local date, formatted for the guest's locale
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **The filter holds for the whole search**
* * *
*   **Given** a guest has the filter on
*   **When** they change dates or guests, or open a property and go back to the results
*   **Then** the filter is still on and the results reflect it
*   **And** starting a new search from the home screen turns the filter off
* * *
- [ ] _Mark as done, if the criteria are met_

5\. **A guest with no matches can get back to results in one step**
* * *
*   **Given** no stay matches a search with the filter on
*   **When** the guest taps `Clear filter`
*   **Then** the filter is off and the same search shows its unfiltered results
* * *
- [ ] _Mark as done, if the criteria are met_

6\. **Search is unchanged for guests who leave the filter off**
* * *
*   **Given** a guest has not turned on the filter
*   **When** they search and browse results
*   **Then** results, prices and result cards are the same as before this release
* * *
- [ ] _Mark as done, if the criteria are met_

7\. **The Search squad can count filter use from existing analytics**
* * *
*   **Given** a guest on iOS, Android or web
*   **When** they turn the filter on
*   **Then** the event reaches `events-collector` with the filter identified, and the Data team's tracking plan needs no new row
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   
