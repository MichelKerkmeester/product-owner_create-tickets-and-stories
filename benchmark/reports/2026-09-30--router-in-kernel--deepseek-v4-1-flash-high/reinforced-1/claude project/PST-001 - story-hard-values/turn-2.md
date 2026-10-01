```markdown
# Guest - Search - Free cancellation filter

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
Guests who want to cancel for free cannot find those stays without opening property pages one at a time, and the question is Guest Support's most common one before a booking. This story adds a Free cancellation switch to the filter sheet, so a filtered search returns only stays with that rate plan, priced at that plan and showing its deadline.

#### Problem
* * *
"Can I cancel this for free?" is the most common question in Guest Support chats before a booking, about one in six pre-booking chats in August. 44% of August bookings were on a free cancellation rate plan, yet the only way to find those rates is to open each property page one at a time.

#### Solution
* * *
Let the results list answer the cancellation question, rather than sending the guest into property pages. One switch joins the filter sheet, and with it on a search returns only stays with a free cancellation rate plan for those dates, priced at that plan and carrying its deadline, so the guest reads the terms of the rate they are offered.

**Expected outcomes**
* * *
*   Guests find the stays they can cancel for free without opening property pages one at a time
*   Every stay and every price in a filtered result set is one the guest can cancel for free
*   Guests read the deadline of the rate they are being quoted before they open the stay
* * *
##   

## Requirements
* * *
**Free cancellation filter**
* * *
- [] A `Free cancellation` filter sits in the search filter sheet, below `Price` and `Star rating`, which are the only two filters there today
- [] The filter is a single on and off switch
- [] The filter stays on while the guest changes dates or guests in the same search
- [] The filter stays on when the guest opens a property and returns to the results
- [] The filter turns off when the guest starts a new search from the home screen

**Results list**
* * *
- [] With the filter on, a stay appears only if at least one rate plan for the searched dates, guests and rooms has free cancellation
- [] That rate plan's free cancellation deadline has not passed
- [] The price on a result card is the cheapest free cancellation rate plan, even when a non-refundable rate is cheaper
- [] The results header shows the filtered count, and the Lisbon test search, 4 nights with 2 adults, moves from `1,146` stays to `312`

**Result card badge**
* * *
- [] Every result card with the filter on shows the deadline of the rate plan whose price is on the card
- [] The badge reads `Free cancellation until 14 Oct`
- [] The deadline is the check-in date minus the partner's cancellation window
- [] A partner who allows free cancellation up to 14 days before check-in gets a deadline 14 days before check-in
- [] The badge date is the property's local date, so a guest abroad reads the same date the confirmation email carries
- [] The date uses the `d MMM` pattern in the guest's locale, a day and a short month name with no year
- [] With the filter off, result cards stay as they are today

**Empty state**
* * *
- [] With no stay matching, the results list reads `No stays with free cancellation for these dates`
- [] The empty state holds one button, `Clear filter`
- [] `Clear filter` switches the filter off and reruns the same search

**Tracking**
* * *
- [] Turning the filter on fires the existing `filter_applied` event with `filter_name` set to `free_cancellation`
- [] No new event is added and the tracking plan needs no change

**Release**
* * *
- [] iOS and Android ship the filter in `8.13.0`, and web ships in the same week as the apps
- [] `search-service` ships first, so no app shows a filter the service cannot apply

**Not in this release**
* * *
- [] The map view keeps showing every stay, with its pins unchanged until we follow up
- [] No sorting by cancellation deadline
- [] No Partner Hub change, since partners already set free cancellation per rate plan
- [] No badge on the property page, which already lists the policy for each rate plan
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Results
* * *
1\. **A filtered search returns only stays a guest can cancel for free**
* * *
*   **Given** a guest searching Lisbon for 4 nights with 2 adults
*   **When** they turn on `Free cancellation` in the filter sheet
*   **Then** every stay in the results has at least one rate plan they can cancel for free for those dates
*   **And** the count in the results header matches the stays listed
* * *
- [] _Mark as done, if the criteria are met_

2\. **Every price in a filtered result set is one the guest can cancel for free**
* * *
*   **Given** a stay whose non-refundable rate is cheaper than its free cancellation rate
*   **When** it appears in a filtered result set
*   **Then** the price on the card is the cheapest free cancellation rate, not the lower non-refundable one
* * *
- [] _Mark as done, if the criteria are met_

#### Result card badge
* * *
3\. **The guest reads the cancellation deadline before opening a stay**
* * *
*   **Given** a guest with `Free cancellation` on
*   **When** a result card appears
*   **Then** the card carries the deadline of the rate plan whose price it shows
*   **And** a guest in another time zone reads the same date as their confirmation email carries
* * *
- [] _Mark as done, if the criteria are met_

#### Filter state
* * *
4\. **The filter survives a look at a property and the way back**
* * *
*   **Given** a guest with `Free cancellation` on and a result set in front of them
*   **When** they open a property and return to the results
*   **Then** the filter is still on and the same stays are in place
*   **And** the filter clears only when they start a new search from the home screen
* * *
- [] _Mark as done, if the criteria are met_

#### Empty state
* * *
5\. **A guest with no matching stays can clear the filter in one move**
* * *
*   **Given** a guest with `Free cancellation` on for dates no stay matches
*   **When** the results list comes back empty
*   **Then** they are told no stays have free cancellation for those dates and offered one action to clear the filter
*   **And** that action switches the filter off and reruns the same search
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/001 - Story-free-cancellation-filter.md`

HVR self-scan: 0 hard blockers. Fixed: none required. Kept with reason: none.

Quality status: PASS. Routed as a **Story**, not an Epic, because both sources supply hard values. House grammar, heading depth and all six floors clear, with Clarity and Mechanism Depth carrying the delivery and Accuracy resting on Tomas's notes plus the two Guest Support asks.

Both asks landed inside this Story. The badge date is now the property's local date, and the filter is required to survive a trip into a property page and back. Requirements is grouped by the surface each value lands in, and five criteria cover the surfaces the story touches.

Two things to check before it goes to the squad.

- I read the local-date ask as compatible with Tomas's locale line rather than a replacement for it. The property's local date sets which calendar date the badge shows, and `d MMM` in the guest's locale sets how that date is written. If Guest Support meant the guest's locale to stop governing the badge, say so and I will swap that item out.
- No frame link came through, so the Story omits References rather than carrying an empty one. Send Ines's link and I will add it.

Tomas's four "Not in this release" lines are carried as a Requirements group under his own heading, because you did not ask for a delivery view and neither an open question nor an undated external constraint forced one. That keeps the map view, deadline sorting, Partner Hub and the property-page badge in the spec rather than only in this conversation.

No ClickUp connector is present in this session, so there is nothing to push and nothing has been written elsewhere.