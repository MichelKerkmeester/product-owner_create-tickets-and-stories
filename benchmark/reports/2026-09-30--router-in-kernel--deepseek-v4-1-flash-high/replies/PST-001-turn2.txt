```markdown
# Guest - Search - Free cancellation filter

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
This story adds a Free cancellation filter to the search filter sheet, so a guest who may need to cancel can find the stays that allow it without opening property pages one at a time. It covers the filter control, the deadline on each result card and the empty state when no stay matches.

#### Problem
* * *
One in six pre-booking Guest Support chats in August asked whether a stay could be cancelled free, and 44% of August bookings were on a free cancellation rate plan. A cancellation policy shows only on the property page, so a guest who needs to cancel later has to open properties one at a time to find one that allows it.

#### Solution
* * *
Bring cancellation terms into search, where the guest already compares price and rating. A guest who cannot risk a non-refundable booking narrows the results to stays that still allow a free cancellation, and each card carries what that flexibility costs and how long it lasts, so the choice happens in the results.

**Expected outcomes**
* * *
*   Guests find stays they can still cancel free without opening each property page
*   The price of a free cancellation rate plan is visible in the results, so the guest sees what the flexibility costs
* * *
##   

## Requirements
* * *
**Search filter sheet**
* * *
- [] The filter is in the search filter sheet, below the existing Price and Star rating filters
- [] The filter is a single switch that turns on and off
- [] The filter stays on when the guest changes dates or guests inside the same search
- [] The filter stays on when the guest opens a property page and returns to the results
- [] The filter turns off when the guest starts a new search from the home screen

**Search results**
* * *
- [] A stay appears in the results only if one rate plan for the searched dates, guests and rooms allows free cancellation
- [] A rate plan whose free cancellation deadline has passed does not qualify
- [] The result card price is the cheapest free cancellation rate plan, even where a non-refundable rate is cheaper
- [] The results header shows the count of stays that match the filter
- [] The test search of Lisbon for 4 nights with 2 adults goes from `1,146` stays to `312` with the filter on

**Result card badge**
* * *
- [] With the filter on, every result card shows the deadline of the rate plan priced on it
- [] The badge reads `Free cancellation until 14 Oct`
- [] The deadline is the check-in date minus the partner's cancellation window
- [] A partner window of `14 days` puts the deadline `14` days before check-in
- [] The date uses the `d MMM` pattern in the guest's locale, a day and a short month name with no year
- [] The badge date is the property's local date, so a guest abroad can check it against the confirmation email
- [] With the filter off, result cards are unchanged

**Empty state**
* * *
- [] When no stay matches, the results read `No stays with free cancellation for these dates`
- [] One button reads `Clear filter`
- [] `Clear filter` switches the filter off and reruns the same search

**Tracking**
* * *
- [] Turning the filter on fires the existing `filter_applied` event with `filter_name` set to `free_cancellation`
- [] No new event and no tracking plan change

**Release**
* * *
- [] iOS and Android ship the filter in `8.13.0`
- [] Web ships the filter in the same week as the apps
- [] `search-service` ships the filter first, so no app shows a filter the service cannot apply

**Not in this release**
* * *
- [] The map view keeps showing every stay while the filter is on, and the pins change only in a follow-up
- [] Sorting by cancellation deadline stays out of this release
- [] Partner Hub does not change, because partners already set free cancellation per rate plan
- [] No badge on the property page, which already lists each rate plan's policy
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Search results
* * *
1\. **Results hold only stays the guest can still cancel free**
* * *
*   **Given** a guest searching a destination for particular dates, guests and rooms
*   **When** they turn the Free cancellation filter on
*   **Then** the results hold only stays with a rate plan they can still cancel free for that search, and the header count matches what is on screen
*   **And** the filter stays on while they change dates or guests in the same search, and clears when they start a new search from the home screen
* * *
- [] _Mark as done, if the criteria are met_

2\. **The card price is the cheapest free cancellation rate plan**
* * *
*   **Given** a stay in the filtered results whose non-refundable rate is cheaper
*   **When** the guest reads the result card
*   **Then** the price on the card is the cheapest free cancellation rate plan, so the guest sees what the cancellation right costs
* * *
- [] _Mark as done, if the criteria are met_

3\. **The filter holds through a property page and back**
* * *
*   **Given** the guest has narrowed the results with the filter on
*   **When** they open a property page and return to the results
*   **Then** the filter is still on and the guest is back on the results they left
* * *
- [] _Mark as done, if the criteria are met_

#### Result card
* * *
4\. **The card says how long the guest has to cancel free**
* * *
*   **Given** the guest is reading filtered results
*   **When** they look at a result card
*   **Then** the card shows when free cancellation ends for the rate plan it prices, in the guest's own date format
*   **And** with the filter off the cards read as they do today
* * *
- [] _Mark as done, if the criteria are met_

5\. **A guest abroad reads the deadline date the property runs on**
* * *
*   **Given** a guest in a different time zone from the property they are looking at
*   **When** they read the deadline on a result card
*   **Then** the date is the property's local date, so it lines up with the confirmation email they hold
* * *
- [] _Mark as done, if the criteria are met_

#### Empty state
* * *
6\. **A search with no matching stay leaves the guest a way forward**
* * *
*   **Given** no stay matches the filter for the searched dates
*   **When** the results load
*   **Then** the guest sees the empty state for the filter and one action, and taking it clears the filter and reruns the same search with the results back
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/NNN - Story-free-cancellation-filter.md`

Artifact kind: Story, refined in place. The whole story keeps its structure, and only the two asks landed in it. Nothing else from Tomas's notes changed.

What changed: one new constraint item in **Search filter sheet** for the filter staying on through a property page visit, one new item in **Result card badge** for the property's local date, and one acceptance criterion for each, in the group whose surface it verifies. The criteria are renumbered so each surface's group still runs in order, and the numbers shifted are noted here rather than in the artifact.

One reading to confirm: I took Guest Support's local-date ask as stacking with Tomas's date rule rather than replacing it, so the badge carries the property's local date while the `d MMM` pattern still follows the guest's locale, which is what the two sources say between them. If Guest Support meant the month name or pattern should change too, say so and I will change that line.

Quality: both asks carried as the constraints they are, with Guest Support's own reason kept beside each, and no value from either source added or generalised. Requirements still holds only hard constraints with no outcomes or build steps, the four original criteria are untouched apart from their numbers, and the house grammar is as delivered.

HVR self-scan: 0 hard blockers. Fixed: no banned terms, and the two asks carried in the words given with no additions. Kept with reason: the property-local-date item and the property-page item keep Guest Support's reason clauses as the requirement's reason, `Free cancellation until 14 Oct`, `No stays with free cancellation for these dates`, `Clear filter`, `d MMM`, `filter_applied`, `free_cancellation`, `8.13.0`, `search-service`, `1,146`, `312` and `14 days` stay quoted verbatim as supplied values, and `_Mark as done, if the criteria are met_` stays as the house checklist wording.