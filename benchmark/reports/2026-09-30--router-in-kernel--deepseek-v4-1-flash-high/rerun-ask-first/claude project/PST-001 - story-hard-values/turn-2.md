````markdown
# Guest - Search - Free cancellation filter

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
Guests get a `Free cancellation` switch in the search filter sheet and use it to see only stays they can cancel for free. The results list then answers the cancellation question on the card itself, so a guest compares stays without opening property pages one at a time.

#### Problem
* * *
*   About `1 in 6` pre-booking chats with Guest Support in August asked whether a stay could be cancelled for free
*   `44%` of August bookings were on a free cancellation rate plan
*   The filter sheet holds only `Price` and `Star rating`, so a guest who wants free cancellation opens property pages one at a time

#### Solution
* * *
The filter sheet gains a single switch, which is the step a guest already takes when price matters. With it on, the results list carries the cancellation answer: each card prices a rate plan the guest can cancel for free and states that rate plan's deadline.

**Expected outcomes**
* * *
*   Guests find stays they can cancel for free from the results list
*   A guest comparing prices sees which stays can be cancelled, and until when
*   A guest abroad reads the same deadline date on the card as on their booking confirmation
*   Fewer pre-booking chats reach Guest Support to ask whether a stay can be cancelled for free
* * *
##   

## Requirements
* * *
**Free cancellation filter**
* * *
- [] The filter is a single on and off switch in the search filter sheet, below `Price` and `Star rating`
- [] A stay appears in the results only when at least one rate plan for the searched dates, guests and rooms has free cancellation
- [] A stay drops out of the results once every free cancellation rate plan for the search has passed its deadline
- [] The price on a result card is the cheapest free cancellation rate plan for the search, even when a non-refundable rate is cheaper
- [] The results header shows the count of stays matching the filter
- [] The test search Lisbon, `4 nights`, `2 adults`, returns `312` stays against `1,146` unfiltered
- [] The filter stays on while the guest changes dates or guests in the same search
- [] The filter stays on when the guest opens a property page from the results and comes back
- [] The filter turns off when the guest starts a new search from the home screen

**Result card badge**
* * *
- [] With the filter on, every result card shows the deadline of the rate plan whose price it shows, as `Free cancellation until 14 Oct`
- [] The deadline is the check-in date minus the partner's cancellation window, so a `14 days` window puts the deadline `14 days` before check-in
- [] The deadline is stated in the property's local date, so it matches the cancellation date on the guest's confirmation email
- [] The date uses the `d MMM` pattern in the guest's locale, a day and a short month name with no year
- [] With the filter off, result cards stay as they are today

**Empty state**
* * *
- [] When no stay matches, the results list shows `No stays with free cancellation for these dates`
- [] The empty state carries one button, `Clear filter`
- [] `Clear filter` switches the filter off and reruns the same search

**Tracking**
* * *
- [] Turning the filter on fires the existing `filter_applied` event, with `filter_name` set to `free_cancellation`
- [] No new event is added and the tracking plan needs no change

**Release**
* * *
- [] iOS and Android ship the filter in `8.13.0`
- [] Web ships in the same week as the apps
- [] `search-service` ships before the apps, so no app version shows a filter the service cannot apply
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Filter sheet
* * *
1\. **Guests can narrow results to stays they can cancel for free**
* * *
*   **Given** a guest has searched with dates, guests and rooms
*   **When** they switch the filter on in the filter sheet
*   **Then** the results keep only stays with a free cancellation rate plan for those dates
*   **And** the header count matches the stays listed
* * *
- [] _Mark as done, if the criteria are met_

2\. **The filter follows the search and clears for a new one**
* * *
*   **Given** a guest has the filter on
*   **When** they change the dates or the guests and run the search again
*   **Then** the filter is still on and the results answer the new dates
*   **And** starting a new search from the home screen turns the filter off
* * *
- [] _Mark as done, if the criteria are met_

#### Results
* * *
3\. **A property page visit does not cost the guest the filter**
* * *
*   **Given** a guest has the filter on and opens a property from the results
*   **When** they come back to the results
*   **Then** the filter is still on and the results still answer the search they left
*   **And** no stay outside the filter reappears in the list
* * *
- [] _Mark as done, if the criteria are met_

4\. **A price under the filter always belongs to a rate plan the guest can cancel for free**
* * *
*   **Given** the filter is on and the cheapest rate plan for a stay is non-refundable
*   **When** the guest reads that stay's result card
*   **Then** the card price is the cheapest free cancellation rate plan for the search
*   **And** the card shows that rate plan's deadline in the guest's own date format
* * *
- [] _Mark as done, if the criteria are met_

5\. **The deadline reads the same abroad as it does on the guest's booking confirmation**
* * *
*   **Given** a guest searching from a different time zone than the property
*   **When** they read the deadline on a result card
*   **Then** the date shown is the property's local date for that deadline
*   **And** it matches the cancellation date on the guest's booking confirmation
* * *
- [] _Mark as done, if the criteria are met_

#### Empty state
* * *
6\. **A search with no free cancellation stays says so and offers a way back**
* * *
*   **Given** the filter is on and no stay matches
*   **When** the results load
*   **Then** the list tells the guest that no stays have free cancellation for these dates
*   **And** one action clears the filter and reruns the same search
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
````

Export-equivalent path: `export/001 - Story-free-cancellation-filter.md` (the same file as before, updated in place)

Artifact kind: Story. Both Guest Support asks are folded in, as two new requirement items and two new acceptance criteria, with one new expected outcome:

- The property's local date is a new item in `**Result card badge**`, sitting between the deadline calculation and the `d MMM` format rule, because it decides which date the badge shows.
- The property page round trip is a new item in `**Free cancellation filter**`, next to the other two persistence rules, and its own criterion sits first in `#### Results`.
- Acceptance criteria are now six, numbered 1 to 6, with `#### Filter sheet` holding 1 and 2, `#### Results` holding 3 to 5, and `#### Empty state` holding 6.

Quality: nothing in Tomas's notes was dropped or altered, and both asks read as constraints their group already supports rather than as new sections. The house grammar still passes, no criterion carries a value, and no `**Open:**` line or undated external constraint exists in the notes or the asks, so `## Delivery` stays out and Acceptance criteria closes the story.

HVR self-scan: 0 hard blockers. Fixed: no banned terms to remove. Kept with reason: the fixed `Given`/`When`/`Then`/`And` labels repeat as house labels rather than voice cycling, the supplied strings stay verbatim inside backticks (`Free cancellation until 14 Oct`, `No stays with free cancellation for these dates`, `Clear filter`, `filter_applied`, `free_cancellation`, `8.13.0`), and `- [] _Mark as done, if the criteria are met_` is fixed house text.

One reading to confirm. The ask sets which date the badge shows (the property's local date) and Tomas's note still sets how that date is written (the `d MMM` pattern in the guest's locale). I kept both as separate constraints, so a guest abroad sees the property's date in their own language's format. If Guest Support meant the writing format should follow the property's locale too, tell me and I will change that one line.

The `Not in this release` list stays deliberately out of scope, as before, and I can still add a `## Delivery` section with those four as No-gos on request.