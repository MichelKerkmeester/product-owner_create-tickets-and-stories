```markdown
# Guest - Search - Free cancellation filter

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
The search filter sheet gets a Free cancellation filter that narrows the results to stays the guest can cancel for free, and every result card carries that rate plan's price and its cancellation deadline. This story covers the filter, the results list, the result card badge and the empty state.

#### Problem
* * *
Guests can only find free cancellation rates by opening property pages one at a time, even though 44% of August bookings were on a free cancellation rate plan. "Can I cancel this for free?" is the most common question in Guest Support chats before a booking, about one in six pre-booking chats in August.

#### Solution
* * *
Guests narrow the results to the stays they can cancel for free, and each card answers what that costs and how long it lasts. Putting the answer in the results list is the smallest change that serves guests where they compare stays, instead of leaving them to open property pages one at a time.

**Expected outcomes**
* * *
*   Guests see only the stays they can cancel for free, with the price and the deadline on each card
*   Guest Support fields fewer pre-booking questions about cancelling for free
##   

## Requirements
* * *
**Search filter sheet**
* * *
- [] The filter sits in the search filter sheet below `Price` and `Star rating`
- [] The filter is a single on and off switch

**Results list**
* * *
- [] A stay shows in the results only if at least one rate plan for the searched dates, guests and rooms has free cancellation and its deadline has not passed
- [] The price on a result card is the cheapest free cancellation rate plan, even where a non-refundable rate is cheaper
- [] The results header shows the count of matching stays. The team's test search, Lisbon for `4` nights with `2` adults, goes from `1,146` stays to `312` stays with the filter on
- [] The filter stays on while the guest changes dates or guests in the same search
- [] The filter stays on when the guest opens a property and returns to the results
- [] The filter turns off when the guest starts a new search from the home screen

**Result card badge**
* * *
- [] With the filter on, every result card shows the deadline of the rate plan whose price is on the card, as `Free cancellation until 14 Oct`
- [] The deadline is the check-in date minus the partner's cancellation window, so a partner who allows free cancellation up to `14` days before check-in gets a deadline `14` days before check-in
- [] The deadline shows as the property's local date, so a guest abroad can check it against their confirmation email
- [] The date uses the `d MMM` pattern in the guest's locale, a day and a short month name with no year
- [] With the filter off, result cards stay as they are today

**Empty state**
* * *
- [] When no stay matches, the results list shows `No stays with free cancellation for these dates` and one button, `Clear filter`
- [] `Clear filter` switches the filter off and reruns the same search

**Tracking**
* * *
- [] Turning the filter on fires the existing `filter_applied` event with `filter_name` set to `free_cancellation`
- [] No new event is added

**Release**
* * *
- [] iOS and Android ship the filter in `8.13.0`
- [] Web ships it in the same week as the apps
- [] `search-service` ships first, so no app shows a filter the service cannot apply
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **Guests see only the stays they can cancel for free**
* * *
*   **Given** a guest has searched dates, guests and rooms
*   **When** they turn the Free cancellation filter on
*   **Then** every stay in the results has at least one rate plan for those dates, guests and rooms with free cancellation and a deadline that has not passed
*   **And** the results header agrees with the number of stays shown
* * *
- [] _Mark as done, if the criteria are met_

2\. **The price on a card is a rate plan the guest can cancel for free**
* * *
*   **Given** a stay is in the filtered results
*   **When** the guest reads the price on its result card
*   **Then** that price is the stay's cheapest free cancellation rate plan
*   **And** it stays that price where a non-refundable rate plan is cheaper
* * *
- [] _Mark as done, if the criteria are met_

3\. **The card says when free cancellation ends**
* * *
*   **Given** the filter is on
*   **When** the guest looks at a result card
*   **Then** the card shows when free cancellation ends for the rate plan whose price is on it
*   **And** the date a guest abroad reads matches the one on their confirmation email
* * *
- [] _Mark as done, if the criteria are met_

4\. **The filter holds while the guest keeps browsing**
* * *
*   **Given** the guest turned the filter on for a search
*   **When** they change the dates or guests, or open a property and come back to the results
*   **Then** the filter is still on and the results still match it
*   **And** the filter turns off when they start a new search from the home screen
* * *
- [] _Mark as done, if the criteria are met_

5\. **An empty results list still gets the guest back to the full set**
* * *
*   **Given** no stay matches the search the guest is running
*   **When** the guest reaches the empty results list with the filter on
*   **Then** the guest can clear the filter from that screen and lands on the same search, unfiltered
*   **And** the filter is off once they do
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/002 - Story-free-cancellation-filter.md`

Artifact kind: Story, not Epic. One feature area with concrete requirements, so the Epic shape does not apply.

Quality status: house grammar, heading depth, the Mark-as-done separation and the spacer closes all pass. Requirements hold only supplied hard values, and every note line is accounted for. References is omitted because no link was supplied.

HVR self-scan: 0 hard blockers. Fixed: "actually" cut from an acceptance criterion title. Kept with reason: `Free cancellation until 14 Oct` and `No stays with free cancellation for these dates` as exact product strings carried verbatim in backticks, and `d MMM` as the source's own notation.

Three things to check before this hardens.

First, I read Guest Support's two asks as additions to Tomas's notes, not corrections. The property's local date settles which calendar date the badge shows, while Tomas's `d MMM` in the guest's locale still settles the format. If Guest Support meant the whole date should follow the property's locale, that is a one-line change to the badge group.

Second, two intake questions went unanswered, so I took the house defaults. No Delivery section, because it is opt-in and nobody asked for one. One Story file rather than a Story with a task breakdown, because no split was named.

Third, the notes' exclusions are named here as deliberately out of scope rather than in the artifact: the map view, with pins keeping every stay until the squad follows up, sorting by cancellation deadline, any Partner Hub change, and a badge on the property page.

Add any of those three back, a Delivery section or a task bundle, and I will fold them in. Otherwise the Story is ready to review with Ines and Dario, and I can turn it into tasks for the squad whenever you want them.