Deliverable Block (no Canvas panel in this session, so the block is rendered here)

```markdown
# Guest - Search - Free cancellation filter

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
This story adds a free cancellation filter to the search filter sheet, so a guest can search only the stays they can still cancel for free and see the date by which they have to decide. The filter stays on while the guest explores one search, and an empty result offers a way back.

#### Problem
* * *
Free cancellation is the question guests ask most before booking, at about one in six pre-booking Guest Support chats in August, and 44% of August bookings were on a free cancellation rate plan. Those guests cannot find the rates without opening one property page at a time.

#### Solution
* * *
Put the choice where guests already narrow a search, and let the results carry the answer. With the filter on, the results hold only stays with a free cancellation rate plan still open, each card prices that plan and names the date the guest has to decide by, so a guest gets the answer in the list rather than on a property page.

**Expected outcomes**
* * *
*   A guest finds stays with free cancellation in one search instead of opening property pages
*   Guests see how long they have to cancel while they compare prices
*   Fewer pre-booking chats ask Guest Support whether a stay can be cancelled for free

## Requirements
* * *
**Filter sheet**
* * *
- [] The free cancellation filter sits in the search filter sheet below Price and Star rating, the only two filters there today
- [] The filter is one on and off switch

**Search results**
* * *
- [] A stay appears in the results list only when at least one rate plan for the searched dates, guests and rooms has free cancellation and its deadline has not passed
- [] The price on the result card is the cheapest free cancellation rate plan, even when a non-refundable rate is cheaper
- [] The results header shows the count for the filtered set
- [] The Lisbon test search, `4` nights with `2` adults, drops from `1,146` stays to `312` stays with the filter on

**Filter persistence**
* * *
- [] The filter stays on while the guest changes dates or guests in the same search
- [] The filter stays on when the guest opens a property page and returns to the results
- [] The filter turns off when the guest starts a new search from the home screen

**Result card badge**
* * *
- [] With the filter on, every result card shows the deadline of the rate plan whose price is on the card, as `Free cancellation until 14 Oct`
- [] The deadline is the check-in date minus the partner's cancellation window, so a partner who allows free cancellation up to `14` days before check-in gets a deadline `14` days before check-in
- [] The deadline shows in the `d MMM` pattern in the guest's locale, a day and a short month name with no year
- [] The deadline is the property's local date, so a guest abroad reads the same day the confirmation email names
- [] With the filter off, result cards stay as they are today

**Empty state**
* * *
- [] Where no stay matches, the results list reads `No stays with free cancellation for these dates`
- [] The empty state carries one button, `Clear filter`
- [] `Clear filter` switches the filter off and reruns the same search

**Tracking**
* * *
- [] Turning the filter on fires the existing `filter_applied` event with `filter_name` set to `free_cancellation`
- [] No new event ships and the tracking plan needs no change

**Release**
* * *
- [] iOS and Android ship the filter in `8.13.0`
- [] Web ships it in the same week as the apps
- [] `search-service` ships first, so no app shows a filter the service cannot apply

**Not in this release**
* * *
- [] The map view keeps showing every stay, with its pins unfiltered
- [] Sorting by cancellation deadline stays out
- [] No Partner Hub change, because partners already set free cancellation per rate plan
- [] No badge on the property page, which already lists the policy for each rate plan
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Filter and results
* * *
1\. **Guests see only stays they can still cancel for free**
* * *
*   **Given** a guest searching a destination for a set of dates, guests and rooms
*   **When** they turn the free cancellation filter on
*   **Then** every stay in the results list has at least one free cancellation rate plan whose deadline has not passed, and the header count matches what the guest can see
*   **And** each card prices the cheapest free cancellation rate plan, even where a non-refundable rate is cheaper
* * *
- [] _Mark as done, if the criteria are met_

2\. **The card tells the guest how long they have left to decide**
* * *
*   **Given** the filter is on
*   **When** the results appear
*   **Then** every card names the deadline of the rate plan whose price it shows, as the property's local date, so a guest abroad can check it against the confirmation email
* * *
- [] _Mark as done, if the criteria are met_

#### Persistence
* * *
3\. **The filter holds while the guest works inside one search**
* * *
*   **Given** the guest turned the filter on
*   **When** they change dates or guests in the same search, or open a property page and come back to the results
*   **Then** the filter is still on and the results list still holds only stays they can cancel for free
* * *
- [] _Mark as done, if the criteria are met_

4\. **A new search starts unfiltered**
* * *
*   **Given** the guest has been searching with the filter on
*   **When** they start a search from the home screen
*   **Then** the filter is off and the results list is unfiltered
* * *
- [] _Mark as done, if the criteria are met_

#### Empty state
* * *
5\. **Finding nothing leaves the guest a way back**
* * *
*   **Given** no stay for the searched dates has free cancellation
*   **When** the results load
*   **Then** the results list says nothing matches these dates and offers a single action
*   **And** that action turns the filter off and reruns the same search
* * *
- [] _Mark as done, if the criteria are met_

#### Tracking
* * *
6\. **Filter use shows up in the existing analytics**
* * *
*   **Given** the guest turns the free cancellation filter on
*   **When** the search is applied
*   **Then** the existing `filter_applied` event carries `free_cancellation` as its filter name, and no new event ships
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/002 - Story-free-cancellation-filter.md`
HVR self-scan: 0 hard blockers. Fixed: an About enumeration that would have put two three-item lists inside 150 words, and "the list" where the house term is the results list. Kept with reason: `Free cancellation until 14 Oct`, `No stays with free cancellation for these dates`, `Clear filter`, `d MMM`, `8.13.0`, `filter_applied` and `free_cancellation` carried verbatim as supplied strings and identifiers, and the Given/When/Then labels repeating per the house grammar.

Quality status: Story kind, house grammar checked against the Story scaffold. Preamble and dividers in place, `*   ` bullets, `- []` requirement items, numbered criteria with a Mark-as-done line and no divider between criteria, and the `* * *` above every `##   ` spacer, so Acceptance criteria is the last section. Eight requirement groups cover every line of Tomas's notes, including the release and exclusion lines, and the two Guest Support asks.

Two calls worth your eye. The asks land as a persistence requirement and a badge requirement, and they sit together cleanly: the locale still drives the `d MMM` format while the property's timezone fixes which calendar day the guest reads. The notes' "Not in this release" list went into Requirements as a group rather than into No-gos, because no Delivery section was requested and nothing carries an Open line.

Next step: say the word if you want a Delivery close with estimation, rabbit holes and no-gos, or the task breakdown under this story, and I will add it.