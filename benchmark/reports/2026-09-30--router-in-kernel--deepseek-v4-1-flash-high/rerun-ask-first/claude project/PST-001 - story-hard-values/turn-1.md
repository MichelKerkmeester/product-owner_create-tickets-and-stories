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
The filter sheet gains a single switch, which is the step a guest already takes when price matters. With it on, the results list carries the cancellation answer: each card prices a rate plan the guest can cancel for free and shows that rate plan's deadline.

**Expected outcomes**
* * *
*   Guests find stays they can cancel for free from the results list
*   A guest comparing prices sees which stays can be cancelled, and until when
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
- [] The filter turns off when the guest starts a new search from the home screen

**Result card badge**
* * *
- [] With the filter on, every result card shows the deadline of the rate plan whose price it shows, as `Free cancellation until 14 Oct`
- [] The deadline is the check-in date minus the partner's cancellation window, so a `14 days` window puts the deadline `14 days` before check-in
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
3\. **A price under the filter always belongs to a rate plan the guest can cancel for free**
* * *
*   **Given** the filter is on and the cheapest rate plan for a stay is non-refundable
*   **When** the guest reads that stay's result card
*   **Then** the card price is the cheapest free cancellation rate plan for the search
*   **And** the card shows that rate plan's deadline in the guest's own date format
* * *
- [] _Mark as done, if the criteria are met_

#### Empty state
* * *
4\. **A search with no free cancellation stays says so and offers a way back**
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

Export-equivalent path: `export/001 - Story-free-cancellation-filter.md`

Artifact kind: Story, titled `Guest - Search - Free cancellation filter`, drafted from Tomas's PM notes for the Search squad plus the Roamstay company context.

Quality: house grammar passes (Story preamble, dividers after each content heading, `*   ` prose bullets, `- []` requirement items, numbered criteria each closed by a Mark-as-done line with no divider before the next, a section close above every spacer). Every hard value in the notes is in Requirements with its value intact: the filter position below `Price` and `Star rating`, the `312` against `1,146` test count for Lisbon, `4 nights`, `2 adults`, `Free cancellation until 14 Oct`, the `14 days` window, the `d MMM` pattern, both empty-state strings, `Clear filter`, `filter_applied` with `free_cancellation`, `8.13.0` and the `search-service` first order. No criterion carries a value, and nothing was added beyond your notes and the company context.

HVR self-scan: 0 hard blockers. Fixed: no banned terms to remove. Kept with reason: the fixed `Given`/`When`/`Then`/`And` labels repeat deliberately as house labels rather than voice cycling, the exact supplied strings stay verbatim inside backticks (source copy, never my wording), and `- [] _Mark as done, if the criteria are met_` is fixed house text.

Two things to flag before this goes further:

- The two Guest Support asks have not arrived, so nothing from them is in this draft. Send them and I will fold them in, either as requirements or as criteria, whichever they turn out to be.
- Tomas's `Not in this release` list (the map view pins, sorting by cancellation deadline, any Partner Hub change, a property page badge) is deliberately out of scope here rather than written as requirements, because those lines are exclusions and a new Story carries `## Delivery` with a No-gos block only when you ask for it. Say the word and I will add that section with those four as No-gos, and the story ends on Acceptance criteria until then.

Next step: send the Guest Support asks, or tell me to add the Delivery section, and I will revise the same file.