```markdown
# Guest - Search - Free cancellation filter

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
A guest who wants free cancellation has no way to search for it, so this story moves the choice into search. It adds one switch to the search filter sheet, narrows the results to stays a guest can still cancel for free, and puts each stay's deadline on its result card.

#### Problem
* * *
"Can I cancel this for free?" is the most common question in Guest Support chats before a booking, about one in six pre-booking chats in August. 44% of August bookings were on a free cancellation rate plan, and a guest can only find those rates by opening property pages one at a time.

#### Solution
* * *
Cancellation terms belong in search, where the guest is already comparing stays. One filter narrows the results to stays with a rate the guest could still cancel for free, prices each stay at a rate they can book, and puts the deadline in front of them while they decide.

**Expected outcomes**
* * *
*   Guests find stays they can cancel for free without opening property pages one at a time
*   The deadline on a result card is a date a guest abroad can check against their confirmation email
*   A guest who opens a property and goes back keeps browsing the filtered results
* * *
##   

## Requirements
* * *
**Search filter sheet**
* * *
- [] The filter sits in the search filter sheet below the two filters there today, `Price` and `Star rating`
- [] The filter is a single on and off switch
- [] The filter stays on while the guest changes dates or guests in the same search, and turns off when the guest starts a new search from the home screen
- [] The filter stays on when the guest opens a property from the results and goes back to the results

**Results list**
* * *
- [] A stay shows in the results only if at least one rate plan for the searched dates, guests and rooms has free cancellation and its deadline has not passed
- [] The price on a result card is the cheapest free cancellation rate plan, even when a non-refundable rate is cheaper
- [] The results header count covers the filtered list, which on the test search of Lisbon for `4` nights with `2` adults falls from `1,146` stays to `312` stays

**Result card badge**
* * *
- [] Every result card shows the deadline of the rate plan whose price is on the card, as `Free cancellation until 14 Oct`
- [] The deadline is the check-in date minus the partner's cancellation window, so a partner who allows free cancellation up to `14 days` before check-in gets a deadline `14 days` before check-in
- [] The deadline date is the property's local date
- [] The date uses the `d MMM` pattern in the guest's locale, a day and a short month name with no year
- [] With the filter off, result cards stay as they are today

**Empty state**
* * *
- [] When no stay matches, the results list shows `No stays with free cancellation for these dates`
- [] The empty state has one action, `Clear filter`, which switches the filter off and runs the same search again

**Tracking**
* * *
- [] Turning the filter on fires the existing `filter_applied` event with `filter_name` set to `free_cancellation`
- [] No new event is added and the tracking plan is unchanged

**Release**
* * *
- [] iOS and Android ship the filter in `8.13.0`
- [] Web ships in the same week as the apps
- [] `search-service` ships before the apps, so no app shows a filter the service cannot apply
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Search filter sheet
* * *
1\. **The filter shows only stays a guest can still cancel for free**
* * *
*   **Given** a guest searching the Guest app for dates, guests and rooms
*   **When** they turn on the Free cancellation filter
*   **Then** every stay in the results has a rate the guest could still cancel for free on those dates
*   **And** the count in the results header matches the filtered list
* * *
- [] _Mark as done, if the criteria are met_

2\. **The filtered results survive a look at a property**
* * *
*   **Given** a guest with the filter on and results showing
*   **When** they open a property and go back to the results
*   **Then** the filter is still on and the results still match it
* * *
- [] _Mark as done, if the criteria are met_

#### Result card badge
* * *
3\. **A guest can read the deadline without opening the property**
* * *
*   **Given** the filter is on and results are showing
*   **When** the guest reads a result card
*   **Then** the card names the deadline of the rate plan it prices, on the date the guest will find on their confirmation email
*   **And** with the filter off, result cards read as they do today
* * *
- [] _Mark as done, if the criteria are met_

#### Empty state
* * *
4\. **A search with no free cancellation stays offers the guest a way out**
* * *
*   **Given** a guest with the filter on for dates no stay matches
*   **When** the results come back empty
*   **Then** the results list says that no stay matches and offers one action to clear the filter
*   **And** clearing the filter switches it off and runs the same search again
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/002 - Story-free-cancellation-filter.md`

Artifact kind: Story, one feature area with hard values to hold.

Quality status: house grammar passes, with the preamble, divider per content heading, `- []` requirement items, four numbered criteria closed by their Mark-as-done lines, and a `* * *` above each spacer. Every hard value in the notes appears in Requirements under the source's own surfaces, and Guest Support's two asks landed in the filter sheet group and the result card badge group. No References section, because no links were supplied, and no Delivery section, because nobody asked for one and nothing forced it.

HVR self-scan: 0 hard blockers. Fixed: "carries one action" rewritten as "has one action", and no serial comma in any list. Kept with reason: `Free cancellation until 14 Oct`, `No stays with free cancellation for these dates`, `Clear filter`, `Price`, `Star rating`, `filter_applied`, `free_cancellation`, `d MMM`, `8.13.0`, `14 days` and the search figures, all supplied values carried verbatim.

Assumptions you can strike:
*   Guest Support's ask fixes which calendar date the badge shows, so the badge reads the property's local date while Tomas's `d MMM` in the guest's locale still fixes the format. Say so if the whole format should change instead.
*   Both asks are requirements of this Story, so neither becomes its own ticket.
*   The four "Not in this release" items stay out of the artifact as deliberate exclusions, and I left the ownership lines (Ines on the frames, Dario on the service change) and Nadia's 2026-09-17 confirmation date out of the Story. The fact they confirm is recorded as "no new event, tracking plan unchanged".
*   The property visit ask names the filter only, so result-list position and loaded pages are not covered by criterion 2.

Next step: tell me what to change, or ask for the four exclusions as a No-gos block in a Delivery section, or ask me to break the Story into tasks.