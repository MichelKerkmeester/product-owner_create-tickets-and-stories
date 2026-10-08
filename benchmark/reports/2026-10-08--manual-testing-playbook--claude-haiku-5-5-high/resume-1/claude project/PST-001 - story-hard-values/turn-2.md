```markdown
# Guest - Search - Free cancellation filter

* * *
## Problem
* * *
Guests asking "Can I cancel this for free?" make up about one in six pre-booking chats with Guest Support, the most common question there in August. Yet 44% of August bookings were on a free cancellation rate plan, and guests can only find those rates by opening each property page one at a time. Search gives no way to narrow results to them, so guests either open page after page or ask Guest Support. That puts the work on guests and on Guest Support, when the answer already sits in the rate plans.
* * *
##   

## Solution
* * *
Guests can narrow results to stays they can cancel for free, and each result card shows the date until which that rate can be cancelled for free. The price and the deadline on a card come from the same rate plan, the cheapest free cancellation one, so the price and the deadline describe the same rate. The map view, sorting by deadline, Partner Hub changes and a property page badge stay out of this release.

**Expected outcomes**
* * *
*   Guests find stays they can cancel for free from the results list, without opening each property page
*   Guests see the cancellation deadline on the result card, in the property's local date
*   On the Lisbon test search for 4 nights and 2 adults, results fall from 1,146 stays to 312 with the filter on
* * *
##   

## Requirements
* * *
**Filter sheet**
* * *
- [] The Free cancellation filter sits in the search filter sheet below Price and Star rating
- [] The filter is a single on and off switch

**Results**
* * *
- [] With the filter on, a stay shows only if at least one rate plan for the searched dates, guests and rooms has free cancellation and a deadline that has not passed
- [] With the filter on, the price on the result card is the cheapest free cancellation rate plan, even when a non-refundable rate is cheaper
- [] With the filter on, the results header shows the new count of stays
- [] The filter stays on while the guest changes dates or guests in the same search
- [] The filter stays on when the guest opens a property and goes back to the results
- [] The filter turns off when the guest starts a new search from the home screen

**Result card badge**
* * *
- [] With the filter on, each result card shows `Free cancellation until 14 Oct`, with the date in the `d MMM` pattern of the guest's locale and no year
- [] The deadline is the check-in date minus the partner's cancellation window, so a window of `14` days gives a deadline 14 days before check-in
- [] The deadline date is the property's local calendar date, not converted to the guest's time zone
- [] The badge shows the deadline of the rate plan whose price is on the card
- [] With the filter off, result cards stay as they are today

**Empty state**
* * *
- [] The empty message reads `No stays with free cancellation for these dates`
- [] The single button reads `Clear filter`
- [] `Clear filter` turns the filter off and reruns the same search

**Tracking**
* * *
- [] No new analytics event is added
- [] Turning the filter on fires `filter_applied` with `filter_name` set to `free_cancellation`

**Release**
* * *
- [] The filter ships in `8.13.0` on iOS and Android
- [] Web ships in the same week as the apps
- [] `search-service` ships before the apps, so no app shows a filter the service cannot apply
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Results
* * *
1\. **The list shows only stays the guest can cancel for free**
* * *
*   **Given** the guest runs a search with the filter off
*   **When** they turn on the Free cancellation filter
*   **Then** the list shows only stays with a free cancellation rate plan for the searched dates, guests and rooms whose deadline has not passed
*   **And** the results header shows the count of those stays
* * *
- [] _Mark as done, if the criteria are met_

2\. **A stay's price is its cheapest free cancellation rate plan**
* * *
*   **Given** a stay whose non-refundable rate is cheaper than its free cancellation rate
*   **When** the filter is on
*   **Then** the result card shows the price of the cheapest free cancellation rate plan
*   **And** the non-refundable price is not shown on the card
* * *
- [] _Mark as done, if the criteria are met_

3\. **The filter stays on through a search and a property visit**
* * *
*   **Given** the filter is on in a search
*   **When** the guest changes dates or guests, or opens a property and goes back to the results
*   **Then** the filter is still on
*   **And** the results still show only stays with free cancellation
* * *
- [] _Mark as done, if the criteria are met_

4\. **A new search from the home screen starts with the filter off**
* * *
*   **Given** the filter is on
*   **When** the guest starts a new search from the home screen
*   **Then** the filter is off
* * *
- [] _Mark as done, if the criteria are met_

#### Result card
* * *
5\. **Each card shows the deadline of the rate plan whose price it shows**
* * *
*   **Given** the filter is on
*   **When** a result card is shown
*   **Then** the card shows the deadline of the rate plan whose price is on the card
*   **And** the date is the property's local date, not the guest's
* * *
- [] _Mark as done, if the criteria are met_

6\. **Cards with the filter off show no deadline**
* * *
*   **Given** the filter is off
*   **When** results are shown
*   **Then** no card shows a free cancellation deadline, as today
* * *
- [] _Mark as done, if the criteria are met_

#### Empty state
* * *
7\. **A search with no matching stays offers one way out**
* * *
*   **Given** the filter is on and no stay matches the search
*   **When** the results list loads
*   **Then** the list explains that no stays have free cancellation for these dates
*   **And** a single button, Clear filter, is offered
*   **And** choosing Clear filter turns the filter off and reruns the same search
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/002 - Story-free-cancellation-filter.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Artifact kind: Story. It covers one feature with hard requirements, so it has no Epic shape.

Quality status: the Story template checks pass for the Problem length, the Solution and Expected outcomes order, the Requirements groups and the criteria grammar. Nothing in the draft is still open, as you said.

Three points to check before this goes anywhere:

- **Property local date:** Tomas's notes compute the deadline as a calendar date from check-in, so it is already a property-local date. The notes name the guest's locale only for the format, so the two do not conflict. The Story now states the date basis as the property's local date.
- **Filter state:** Tomas's notes cover date and guest changes and a new search from home, but not opening a property and going back. The Story adds that as a Results requirement and criterion 3, with no conflict with his notes.
- **Android version:** the Story follows Tomas's notes and writes `8.13.0` for Android. The company context records Android at `8.12.1` on the current train, because the store turned back `8.12.0`. If Android uses a different string for this train, tell me and I will change the one line.

I left out a Delivery section, because you did not ask for one, no requirement carries an open question and nothing in the notes is an undated outside constraint. References is also left out, because no link was supplied.