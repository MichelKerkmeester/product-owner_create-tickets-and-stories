```markdown
# Guest - Search - Free cancellation filter

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
Guests cannot compare cancellation terms while they search, so the answer is a message to Guest Support rather than a choice in the results. This story adds a `Free cancellation` filter to the search filter sheet, and while that filter is on, every result card carries the deadline the guest is working to.

#### Problem
* * *
Guests ask "Can I cancel this for free?" before they can see what cancelling a stay would cost:
*   About one in six pre-booking Guest Support chats in August were that question
*   44% of August bookings were on a free cancellation rate plan, yet those rates surface one property page at a time

#### Solution
* * *
Move the cancellation terms into the results list, where a guest is already comparing stays. A guest who needs the option filters the search itself, and each card then carries the deadline they are working to, so the price on a card is one they can still back out of.

**Expected outcomes**
* * *
*   Guests find stays they can still cancel for free without opening a property page
*   The price a guest compares belongs to a rate plan they can still cancel, so a cheaper non-refundable rate never reads as the better option
*   Fewer guests ask Guest Support whether a stay can be cancelled for free

* * *
##   

## Requirements
* * *
**Search filter sheet**
* * *
- [] A `Free cancellation` filter sits in the search filter sheet below `Price` and `Star rating`, as a single on and off switch
- [] The filter stays on while the guest changes the dates or guests inside the same search
- [] A new search started from the home screen turns the filter off

**Results list**
* * *
- [] With the filter on, a stay appears only when at least one rate plan for the search has free cancellation
- [] That rate plan's free cancellation deadline must not have passed for the searched dates, guests and rooms
- [] With the filter on, the price on a result card is the cheapest free cancellation rate plan, even when a non-refundable rate is cheaper
- [] With the filter on, the results header shows the count of matching stays
- [] The Lisbon test search, 4 nights for 2 adults, returns `312` stays from `1,146` with the filter on

**Result card badge**
* * *
- [] With the filter on, every result card shows the deadline of the rate plan behind its price, as `Free cancellation until 14 Oct`
- [] The deadline is the check-in date minus the partner's cancellation window
- [] A partner who allows free cancellation up to 14 days before check-in gets a deadline 14 days before check-in
- [] The deadline uses the `d MMM` date pattern in the guest's locale, a day and a short month with no year
- [] With the filter off, result cards are unchanged

**Empty state**
* * *
- [] When no stay matches, the results list shows `No stays with free cancellation for these dates` and one button, `Clear filter`
- [] `Clear filter` switches the filter off and reruns the same search

**Tracking**
* * *
- [] Turning the filter on fires the existing `filter_applied` event with `filter_name` set to `free_cancellation`, and adds no new event or tracking plan change

**Release**
* * *
- [] iOS and Android ship the filter in `8.13.0`, with web shipping in the same week
- [] `search-service` ships before the apps, so no app shows a filter the service cannot apply
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Search results
* * *
1\. **A guest can narrow the results to stays they can still cancel for free**
* * *
*   **Given** a guest has searched a destination for their dates, guests and rooms
*   **When** they turn on `Free cancellation` in the filter sheet
*   **Then** the results hold only stays with a free cancellation rate plan for that search and the header shows how many match
*   **And** a stay whose free cancellation deadline has already passed stays out of the list
* * *
- [] _Mark as done, if the criteria are met_

2\. **The price on a result is one the guest can still cancel for free**
* * *
*   **Given** the filter is on and a stay also has a cheaper non-refundable rate
*   **When** the guest reads the price on its card
*   **Then** that price belongs to a free cancellation rate plan for their search, not to the cheaper non-refundable rate
* * *
- [] _Mark as done, if the criteria are met_

3\. **The filter follows the guest through one search and clears when they start again**
* * *
*   **Given** the filter is on in a search with results
*   **When** the guest changes the dates or guests within that search
*   **Then** the filter is still on and the results reflect the change
*   **And** a search started from the home screen comes back unfiltered
* * *
- [] _Mark as done, if the criteria are met_

#### Result card
* * *
4\. **Every card carries the deadline the guest is working to**
* * *
*   **Given** the filter is on and a card carries a price the guest can cancel for free
*   **When** the guest reads that card
*   **Then** it shows the last date they can cancel for free, written for their locale
* * *
- [] _Mark as done, if the criteria are met_

#### Empty state
* * *
5\. **An empty result still gives the guest a way forward**
* * *
*   **Given** the filter is on and no stay matches the search
*   **When** the results come back empty
*   **Then** the guest is told no stay matches and given one action that clears the filter
*   **And** that action runs the same search again without the filter
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/001 - Story-free-cancellation-filter.md`

HVR self-scan: 0 hard blockers. Fixed: the notes' first-person build framing ("we're building", "our test search") rewritten as facts, and the current-state aside that Price and Star rating are the only filters there today dropped. Kept with reason: supplied strings and values carried verbatim in backticks (`Free cancellation until 14 Oct`, `d MMM`, `8.13.0`, `312` from `1,146`), plus the house `Given`/`When`/`Then`/`And` labels and the `- []` and Mark-as-done tokens.

Detected route: Story Mode, Story shape (not Epic, since the source supplies concrete requirements). Artifact kind: **Story**, titled `Guest - Search - Free cancellation filter` for the Search squad.

**What is in it.** Every value in Tomas's notes lands in Requirements with its units and notation intact: the filter's position and switch type, the two results rules, the header count with the Lisbon test figures, the state-persistence rule, the badge string, the deadline arithmetic, the `d MMM` pattern, the two empty-state strings, the reuse of `filter_applied` with `filter_name` `free_cancellation`, and the release order. The five acceptance criteria verify the results list, the price guarantee, the filter's lifetime, the badge and the empty state. No design or tracking link was supplied, so `#### **References**` is omitted rather than invented.

**Two things to know.**

1. The two Guest Support asks are not in this draft, because they have not arrived. Send them and I will add them in place as requirement items and criteria, in the source's own grammar, and flag anything that lands on something Tomas has already excluded.
2. Tomas's "Not in this release" list is reported here rather than in the artifact, because `## Delivery` is opt-in and nobody asked for a delivery view: the map view pins, sorting by cancellation deadline, any Partner Hub change, and a badge on the property page. Say the word and I will add `## Delivery` with these as No-gos, leaving Estimation and Rabbit holes as `TBD...`.

One addition to strike if you disagree: the third expected outcome, that fewer guests ask Guest Support about cancellation terms, is drawn from the support-chat evidence in the notes rather than stated by Tomas.

Next step: pass on the two Guest Support asks and I will fold them into this story.