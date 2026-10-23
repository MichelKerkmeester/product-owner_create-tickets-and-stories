```markdown
# Guest - Search - Free cancellation filter

* * *
## Problem
* * *
`Can I cancel this for free?` is the most common question in Guest Support chats before a booking, about one in six pre-booking chats in August. 44% of August bookings were on a free cancellation rate plan, yet guests can only find those rates by opening each property page one at a time. Guests who will not open every page cannot use those rates at all. Search shows no cancellation policy, so the results list cannot answer the question and the ask lands on Guest Support instead.
* * *
##   

## Solution
* * *
The filter decides which stays appear rather than how they are sorted, so it answers the pre-booking cancellation question inside the search the guest is already running. With it on, the result card carries the answer the guest would otherwise open a property page to find, and the deadline it names is the one the guest will be held to. The filter holds for one search and resets at the next, which keeps it a view of the current search rather than a saved setting.

**Expected outcomes**
* * *
*   A guest reaches a stay they can cancel for free without opening property pages one at a time
*   Guest Support sees fewer pre-booking chats asking whether a stay can be cancelled for free
*   The deadline on the card matches the one in the guest's confirmation email
* * *
##   

## Requirements
* * *
**Filter sheet**
* * *
- [] One on and off switch in the search filter sheet
- [] The filter sits below `Price` and `Star rating`, the only two filters in the sheet today

**Results with the filter on**
* * *
- [] A stay appears only when one of its rate plans for the searched dates, guests and rooms has free cancellation and a deadline still ahead
- [] The price on the result card is the cheapest free cancellation rate plan, even when a non-refundable rate plan costs less
- [] The results header shows the count of stays that remain
- [] The test search, Lisbon for `4` nights with `2` adults, returns `1,146` stays with the filter off and `312` with it on

**Filter persistence**
* * *
- [] The filter stays on while the guest changes dates or guests in the same search
- [] The filter stays on when the guest opens a property page and comes back to the results
- [] The filter turns off when the guest starts a new search from the home screen

**Result card badge**
* * *
- [] With the filter on, every result card shows the deadline of the rate plan whose price is on the card, as `Free cancellation until 14 Oct`
- [] The deadline is the check-in date minus the partner's cancellation window
- [] A partner who allows free cancellation up to `14` days before check-in gets a deadline `14` days before check-in
- [] The date uses the `d MMM` pattern in the guest's locale, so a day and a short month name with no year
- [] The date is the property's local date, so a guest abroad sees the day their confirmation email states
- [] With the filter off, result cards stay as they are today

**Empty state**
* * *
- [] When no stay matches, the results list shows `No stays with free cancellation for these dates`
- [] The empty state has one button, `Clear filter`
- [] `Clear filter` switches the filter off and reruns the same search

**Tracking**
* * *
- [] Turning the filter on fires the existing `filter_applied` event with `filter_name` set to `free_cancellation`
- [] No new event is added, and the tracking plan stays as it is

**Release**
* * *
- [] iOS and Android ship in `8.13.0`, and web ships in the same week as the apps
- [] `search-service` ships first, so no app ever shows a filter the service cannot apply

**Not in this release**
* * *
- [] The map view is out of scope, so map pins keep showing every stay
- [] Sorting by cancellation deadline is out of scope
- [] Partner Hub is unchanged, because partners already set free cancellation per rate plan
- [] The property page carries no badge, because it already lists the policy for each rate plan
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Search results
* * *
1 ) **Only stays the guest can cancel for free remain**
* * *
*   **Given** a search with the filter off
*   **When** the guest turns Free cancellation on
*   **Then** the results keep only stays with at least one rate plan for those dates, guests and rooms whose free cancellation deadline has not passed
*   **And** the header states how many stays remain
*   **And** each card prices the cheapest free cancellation rate plan, even where a non-refundable plan costs less
* * *
- [] _Mark as done, if the criteria are met_

2 ) **The filter follows a change of dates or guests**
* * *
*   **Given** the filter is on and results are showing
*   **When** the guest changes the dates or the number of guests in the same search
*   **Then** the filter stays on
*   **And** the results keep only the stays the guest can cancel for free on the new dates or guest count
* * *
- [] _Mark as done, if the criteria are met_

3 ) **A look at a property does not lose the filter**
* * *
*   **Given** the filter is on and results are showing
*   **When** the guest opens a property page and comes back to the results
*   **Then** the filter is still on
*   **And** the results still hold only the stays the guest can cancel for free
* * *
- [] _Mark as done, if the criteria are met_

4 ) **A new search starts with the filter off**
* * *
*   **Given** the filter is on from an earlier search
*   **When** the guest starts a new search from the home screen
*   **Then** the filter is off
* * *
- [] _Mark as done, if the criteria are met_

#### Result card
* * *
5 ) **The card names the deadline the guest will be held to**
* * *
*   **Given** the filter is on
*   **When** a result card shows a free cancellation price
*   **Then** the badge names that rate plan's cancellation deadline
*   **And** the date shown is the property's local date, matching the deadline on the guest's confirmation email
*   **And** with the filter off, the card stays as it is today
* * *
- [] _Mark as done, if the criteria are met_

#### Empty state
* * *
6 ) **No match leaves a way back to other stays**
* * *
*   **Given** a search where no stay has free cancellation for the dates
*   **When** the guest turns the filter on
*   **Then** the results list states that no stays match for these dates
*   **And** one action sits on the empty state, switching the filter off and rerunning the same search
* * *
- [] _Mark as done, if the criteria are met_

#### Tracking
* * *
7 ) **The switch reports through the existing filter event**
* * *
*   **Given** a guest turns Free cancellation on
*   **When** the event reaches `events-collector`
*   **Then** it is `filter_applied` with `filter_name` set to `free_cancellation`
*   **And** no new event is introduced for this filter
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/002 - Story-free-cancellation-filter.md`
HVR self-scan: 1 hard blocker. Fixed: "offers" rewritten as "has" (copula avoidance). Kept with reason: none.
Quality: every floor met | Kind: Story | Energy: Standard

The Story gives the Search squad the switch, the filtering and pricing rule for the results, the deadline badge, the empty state and the tracking, with the two Guest Support asks carried as their own constraints and criteria. Requirements hold every value from Tomas's notes in his own units and groupings, including the Lisbon test search and the `8.13.0` release.

### Open items
1. **Deadline date basis**
   - **Situation:** Tomas's notes format the badge date with `d MMM` in the guest's locale, and Guest Support asks for the property's local date, so I carried both rather than treating them as a conflict
   - **Open:** Confirm that the locale only formats the date while the property's time zone decides which day it is
2. **Exclusions inside Requirements**
   - **Situation:** I carried "Not in this release" into Requirements as its own group, so a developer reads that the map view, deadline sorting, Partner Hub and the property page stay out
   - **Open:** Strike the group if those four belong only in a delivery view
3. **References**
   - **Situation:** No design link arrived, so the Story carries no References section
   - **Open:** Send the Figma link from Ines and I'll add it under References

Want me to change anything?