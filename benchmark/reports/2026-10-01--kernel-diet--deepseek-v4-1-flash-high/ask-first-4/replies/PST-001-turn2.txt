```markdown
# Guest - Search - Free cancellation filter

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
This story adds a Free cancellation filter to the search filter sheet and a deadline badge to each result card. A guest can then find refundable stays without opening property pages one at a time. The map view, deadline sorting, Partner Hub and the property page badge stay unchanged.

#### Problem
* * *
A guest asks "Can I cancel this for free?" in about one in six pre-booking Guest Support chats. 44% of August bookings were on a free cancellation rate plan, and the only way to find those rates is to open property pages one at a time.

#### Solution
* * *
The filter answers the cancellation question inside the search, so a stay is ruled in or out before a property page opens. With the filter on, the price on a result card is a price the guest can still cancel, and its deadline reads as the property's local date, so a guest abroad can check it against their confirmation email.

**Expected outcomes**
* * *
*   Guests find the stays they can cancel for free without opening property pages one at a time
*   Guests see the cheapest price they can still cancel, with its deadline on the result card
* * *
##   

## Requirements
* * *
**Free cancellation filter**
* * *
- [] The filter sits in the search filter sheet below `Price` and `Star rating`
- [] The control is a single on and off switch
- [] A stay is in the results only when at least one rate plan for the searched dates, guests and rooms has free cancellation
- [] A rate plan whose free cancellation deadline has passed does not qualify a stay
- [] The price on a result card is the cheapest free cancellation rate plan, even when a non-refundable rate plan is cheaper
- [] The results header count follows the filtered set
- [] On the test search, Lisbon for 4 nights with 2 adults, the header count moves from `1,146` stays to `312` stays
- [] The filter stays on while the guest changes dates or guests in the same search
- [] The filter stays on when the guest opens a property page and returns to the results
- [] The filter turns off when the guest starts a new search from the home screen

**Result card badge**
* * *
- [] With the filter on, every result card carries the deadline of the rate plan whose price is on the result card
- [] The badge copy is `Free cancellation until 14 Oct`
- [] The deadline is the check-in date minus the partner's cancellation window, so a 14-day window puts the deadline 14 days before check-in
- [] The badge date is the property's local date
- [] The date uses the `d MMM` pattern in the guest's locale, a day and a short month name with no year
- [] With the filter off, result cards stay as they are today

**Empty state**
* * *
- [] The empty state message is `No stays with free cancellation for these dates`
- [] The empty state carries one button, `Clear filter`
- [] `Clear filter` switches the filter off and reruns the same search

**Tracking**
* * *
- [] No new event is added
- [] Turning the filter on fires the existing `filter_applied` event with `filter_name` set to `free_cancellation`
- [] The tracking plan needs no change, confirmed by Nadia on 2026-09-17

**Release**
* * *
- [] iOS and Android carry the filter in `8.13.0`
- [] Web ships the same week as the apps
- [] `search-service` ships first, so no app version shows a filter the service cannot apply
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Results list
* * *
1\. **A guest can see only the stays they can cancel for free**
* * *
*   **Given** a guest searching dates, guests and rooms
*   **When** they turn the Free cancellation filter on
*   **Then** the results hold only stays with at least one free cancellation rate plan for those dates whose deadline has not passed
*   **And** the results header count follows the filtered set
* * *
- [] _Mark as done, if the criteria are met_

2\. **Every price shown while filtering is a price the guest can still cancel**
* * *
*   **Given** the filter is on and a stay is cheaper on a non-refundable rate plan
*   **When** the guest reads its result card
*   **Then** the price is the cheapest free cancellation rate plan for the searched dates, guests and rooms
* * *
- [] _Mark as done, if the criteria are met_

3\. **The filter holds while the guest is in the same search**
* * *
*   **Given** the filter is on
*   **When** the guest changes dates or guests, or opens a property page and returns to the results
*   **Then** the filter is still on and the results match the search they are in
*   **And** a search started from the home screen begins with the filter off
* * *
- [] _Mark as done, if the criteria are met_

#### Result cards
* * *
4\. **The result card tells the guest when free cancellation ends**
* * *
*   **Given** the filter is on and a result card shows a price
*   **When** the guest reads the result card
*   **Then** the result card carries the deadline of the rate plan that price came from, as a date in the property's local time they can check against their confirmation email
*   **And** the date reads in the guest's own date format
* * *
- [] _Mark as done, if the criteria are met_

5\. **Result cards look as they do today while the filter is off**
* * *
*   **Given** a guest searching with the filter off
*   **When** the results show
*   **Then** no cancellation deadline appears on any result card
* * *
- [] _Mark as done, if the criteria are met_

#### Empty state
* * *
6\. **A search with no free cancellation stays says so and offers one way out**
* * *
*   **Given** the filter is on
*   **When** no stay has a free cancellation rate plan for the search
*   **Then** the results show the empty state with `Clear filter` as the only action
*   **And** taking it turns the filter off and reruns the same search
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/002 - Story-free-cancellation-filter.md`

HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: the `_Mark as done, if the criteria are met_` line and the repeated `**Given/When/Then/And**` labels, both fixed house grammar rather than emphasis or synonym cycling, and the supplied values carried verbatim in backticks (`filter_applied`, `free_cancellation`, `Free cancellation until 14 Oct`, `1,146`, `312`, `8.13.0`, `d MMM`).

Quality: Story, not Epic, since the notes supply requirements for one feature area on one squad's surface. Source completeness passes: every value in Tomas's notes lands in Requirements, including the test-search counts and the release order, and both Guest Support asks are carried. House grammar passes, with no Delivery section, so Acceptance criteria closes the artifact. Readability: six criteria across three surfaces, each tracing to a requirement.

Three things I decided that you should look at, because they are mine rather than Tomas's:

*   Both Guest Support asks are drafted as in-scope requirements of this story, not as follow-ups
*   The property-local-date ask sits beside the note's `d MMM` in the guest's locale rather than replacing it, so the day comes from the property and the format from the guest's locale. Tell me if Guest Support meant the format too, and I will move it into the badge copy item
*   The four exclusions from his "Not in this release" list sit in the About scope line, because the Delivery section is opt-in and you did not ask for a delivery view. Say the word and they move into No-gos

Ines owning the frames and Dario leading the `search-service` change are left out as owners rather than requirements. The clarification in the Story lane is left as it stands, and the story file takes the next number.