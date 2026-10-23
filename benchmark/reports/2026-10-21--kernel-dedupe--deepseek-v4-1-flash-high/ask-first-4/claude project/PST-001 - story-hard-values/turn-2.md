```markdown
# Guest - Search - Free cancellation filter

* * *
## Problem
* * *
Guests ask whether they can cancel a stay for free more than any other question before booking, at about one in six pre-booking Guest Support chats in August. 44% of August bookings were on a free cancellation rate plan, yet the only way to find those rates is to open each property page and read its rate plans one at a time. A guest who needs that flexibility compares properties one at a time, so finding a free cancellation rate comes down to luck.
* * *
##   

## Solution
* * *
Put the cancellation policy in the filter sheet, where a guest already narrows the results, and price each filtered stay on the rate that carries the flexibility. A guest then compares the stays they can still cancel without opening a property page.

The result card carries the deadline, because the deadline is what a guest weighs against their own plans. It reads as the date on the property's calendar, which is the date the confirmation email carries.

When nothing matches, the sheet says so and offers one action back to the full list. The filter belongs to the search rather than to one screen, so it survives a changed date, a changed guest count and a look at a property.

**Expected outcomes**
* * *
*   A guest sees only the stays they can still cancel for free, without opening a property
*   The price on those stays reflects the rate that carries the free cancellation
*   The deadline reads as the date on the guest's confirmation email, wherever the guest is
*   The filter stays with the search until the guest starts a new one
*   A search that matches nothing reaches the full list in one action
* * *
##   

## Requirements
* * *
**Filter sheet**
* * *
- [] The filter sits in the search filter sheet below `Price` and `Star rating`, which stay the only two filters the sheet carries
- [] The filter is a single on and off switch
- [] The switch label string comes from the frames Ines owns

**Results list**
* * *
- [] A stay appears only when at least one rate plan for the searched dates, guests and rooms allows free cancellation
- [] That rate plan's deadline has not passed, judged on the property's local date so a stay matches the same way for every guest
- [] A filtered result card prices the stay at its cheapest free cancellation rate plan, even where a non-refundable rate plan is cheaper
- [] The results header shows the filtered count, so a Lisbon search for 4 nights with 2 adults drops from `1,146` stays to `312` stays
- [] The filter stays on while the guest changes dates or guests inside the same search
- [] The filter stays on when the guest opens a property and returns to the results
- [] The filter turns off when the guest starts a new search from the home screen

**Result card badge**
* * *
- [] With the filter on, every card shows the deadline of the rate plan priced on it, as `Free cancellation until 14 Oct`
- [] The deadline is the check-in date minus the partner's cancellation window
- [] A partner allowing free cancellation up to `14` days before check-in gets a deadline `14` days before check-in
- [] The deadline reads as the date on the property's calendar, so a guest abroad sees the date their confirmation email carries
- [] The date uses the `d MMM` pattern in the guest's locale, a day and a short month name with no year
- [] With the filter off, result cards carry no badge and read as they do today

**Empty state**
* * *
- [] A search with no matching stay reads `No stays with free cancellation for these dates`
- [] The empty state carries one action, `Clear filter`, which switches the filter off and reruns the same search

**Tracking**
* * *
- [] Turning the filter on fires the existing `filter_applied` event with `filter_name` set to `free_cancellation`
- [] No new event is added and no tracking plan change is opened, as Nadia confirmed on `2026-09-17`

**Release**
* * *
- [] iOS and Android carry the filter in `8.13.0`
- [] Web carries the filter in the same week as the apps
- [] `search-service` ships before the apps, so no app shows a filter the service cannot apply

**Out of this release**
* * *
- [] The map view keeps every stay on its pins
- [] Sorting by cancellation deadline is not built
- [] Partner Hub keeps its rate plan controls, since partners already set free cancellation per rate plan
- [] The property page carries no badge, since it already lists the policy of each rate plan
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1 ) **A guest narrows the results to stays they can still cancel for free**
* * *
*   **Given** a guest has searched with the filter off
*   **When** they turn the free cancellation filter on
*   **Then** the results hold only stays with a rate plan that allows free cancellation and has not passed its deadline
*   **And** the results header shows the count of the filtered set
* * *
- [] _Mark as done, if the criteria are met_

2 ) **A filtered result is priced on the rate that carries the flexibility**
* * *
*   **Given** the filter is on
*   **When** a card shows a stay with a free cancellation rate plan and a cheaper non-refundable one
*   **Then** the price on the card is the cheapest free cancellation rate plan
* * *
- [] _Mark as done, if the criteria are met_

3 ) **The card carries the deadline on the property's calendar**
* * *
*   **Given** the filter is on
*   **When** the guest reads a result card
*   **Then** the card shows the deadline of the rate plan priced on it, as the date that plan falls on at the property
*   **And** the date reads in the guest's own locale
* * *
- [] _Mark as done, if the criteria are met_

4 ) **A search with no match leads back to the full list**
* * *
*   **Given** the filter is on and no stay matches the search
*   **When** the results load
*   **Then** the list says that no stay with free cancellation matches those dates
*   **And** the one action shown clears the filter and reruns the same search
* * *
- [] _Mark as done, if the criteria are met_

5 ) **The filter stays with the search**
* * *
*   **Given** the filter is on
*   **When** the guest changes dates or guests, or opens a property and comes back
*   **Then** the results return with the filter still on
*   **And** the results header keeps the filtered count
* * *
- [] _Mark as done, if the criteria are met_

6 ) **A new search starts unfiltered**
* * *
*   **Given** the filter is on
*   **When** the guest starts a new search from the home screen
*   **Then** the results carry no free cancellation filter
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/NNN - Story-free-cancellation-filter.md`
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality: every floor met | Kind: Story | Energy: Standard

The Story scopes the free cancellation filter to the Guest app on iOS, Android and web for `8.13.0`, with `search-service` shipping first. Requirements carry every value Tomas wrote down, including the count drop, the badge string, the empty state copy and the `filter_name`, and add Guest Support's two asks as the property's local date on the badge and filter persistence through a property view. Acceptance criteria cover the filtered results, the priced card, the badge, the empty state and the search lifecycle.

### Open items
1. **Switch label**
   - **Situation:** Tomas names the filter but supplies no string for the sheet row, so Requirements points at Ines's frames rather than inventing one
   - **Open:** Send the settled label and I will quote it in backticks
2. **Filter stacking**
   - **Situation:** The notes put the filter below Price and Star rating and never say how the three combine, so I assumed a stay must match every filter that is on
   - **Open:** Confirm that reading, or say if the filters should widen the set instead
3. **Deadline clock**
   - **Situation:** I applied the property's local date to the match check as well as the badge, so a stay cannot show a deadline the filter has already treated as passed
   - **Open:** Confirm that reading, or name the clock the match check uses
4. **Deadline day**
   - **Situation:** The notes exclude a rate plan whose deadline has passed and do not say whether the deadline day itself still qualifies
   - **Open:** Confirm the day itself still qualifies, or strike this if today's rate plan rule already decides
5. **Story title**
   - **Situation:** I used `Guest - Search - Free cancellation filter`, from the house title pattern and the Search area
   - **Open:** Send the squad's own title if it differs
6. **No task breakdown**
   - **Situation:** You asked for a Story, so there is no `#### **Tasks**` bundle for Ines and Dario to pick up
   - **Open:** Ask for the tasks and I will add the bundle as sibling files

Want me to change anything?