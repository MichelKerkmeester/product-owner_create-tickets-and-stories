```markdown
# Guest - Search - Free cancellation filter

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
The search filter sheet holds `Price` and `Star rating` today, so a guest who wants a stay they can cancel for free opens property pages one at a time. This story adds a Free cancellation filter, a deadline badge on every result card and a way back from an empty list, on the Guest app across iOS, Android and web.

#### Problem
* * *
"Can I cancel this for free?" is the most common question in Guest Support chats before a booking, about one in six pre-booking chats in August. 44% of August bookings were on a free cancellation rate plan, and a guest can only find those rates by opening each property page in turn.

#### Solution
* * *
Put cancellation into the search itself, so a guest can see which stays are refundable before opening one. Surviving cards are priced and badged by the free cancellation rate that put them in the list, an empty list gives one step back, and the filter holds until a new search starts from the home screen.

**Expected outcomes**
* * *
*   Guests find the stays they can cancel for free without opening pages one at a time
*   The price on a filtered card is one the guest can still cancel for free
*   Guests see the deadline their refund depends on before they book
*   A guest who finds nothing returns to the full result list in one step

* * *
##   

## Requirements
* * *
**Search filter sheet**
* * *
- [] The filter sits in the search filter sheet below `Price` and `Star rating`
- [] The filter is one control with two states, on and off
- [] A stay matches only when one of its rate plans has free cancellation open for the searched dates, guests and rooms
- [] With the filter on, the result card price is the cheapest free cancellation rate plan, even when a non-refundable rate is cheaper
- [] The results header shows the count for the filtered set
- [] The test search, Lisbon for 4 nights with 2 adults, goes from `1,146` stays with the filter off to `312` with it on
- [] The filter stays on while the guest changes dates or guests in the same search
- [] The filter stays on when the guest opens a property page and returns to the results
- [] The filter switches off when the guest starts a new search from the home screen
- [] `search-service` ships before the apps, so no app shows a filter the service cannot apply

**Result card badge**
* * *
- [] With the filter on, every result card shows the deadline of the rate plan whose price is on the card
- [] The badge reads `Free cancellation until 14 Oct`
- [] The deadline is the check-in date minus the partner's cancellation window, so a 14-day window gives a deadline 14 days before check-in
- [] The deadline is dated at the property, so a guest abroad can check it against the confirmation email
- [] The date uses the `d MMM` pattern in the guest's locale, a day and a short month name with no year
- [] With the filter off, result cards stay as they are today

**Empty state**
* * *
- [] When no stay matches, the results list shows `No stays with free cancellation for these dates`
- [] The empty state carries one button, `Clear filter`
- [] `Clear filter` switches the filter off and reruns the same search

**Tracking**
* * *
- [] Turning the filter on fires the existing `filter_applied` event with `filter_name` set to `free_cancellation`
- [] No new event is added, and the tracking plan needs no change

**Release**
* * *
- [] iOS and Android ship the filter in `8.13.0`
- [] Web ships it in the same week as the apps

* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Filter and results
* * *
1\. **A guest can narrow the results to stays they can cancel for free**
* * *
*   **Given** a guest searching a destination for dates, guests and rooms
*   **When** they turn Free cancellation on
*   **Then** the results hold only stays with a free cancellation rate plan still open for those dates, and the header count matches the list
* * *
- [] _Mark as done, if the criteria are met_

2\. **The price on a filtered card is one the guest can still cancel for free**
* * *
*   **Given** the filter is on and a stay's non-refundable rate is cheaper than its free cancellation rate
*   **When** the stay appears in the results
*   **Then** the card shows the cheapest free cancellation price, and a booking made from it keeps its free cancellation terms
* * *
- [] _Mark as done, if the criteria are met_

#### Result card
* * *
3\. **Every filtered card shows how long the guest can cancel for free**
* * *
*   **Given** the filter is on
*   **When** a result card appears
*   **Then** the card shows the deadline of the rate plan whose price it carries, dated at the property and formatted for the guest's locale
* * *
- [] _Mark as done, if the criteria are met_

4\. **The filter keeps the guest's place while they look around**
* * *
*   **Given** the filter is on
*   **When** the guest changes dates or guests, or opens a property page and returns to the results
*   **Then** the filter is still on and still applied to those results
*   **And** only a new search started from the home screen clears it
* * *
- [] _Mark as done, if the criteria are met_

#### Empty state
* * *
5\. **A guest who finds nothing can return to the full list**
* * *
*   **Given** the filter is on
*   **When** no stay matches the search
*   **Then** the list says nothing matched for those dates and offers one action, which turns the filter off and reruns the same search
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/[###] - Story-free-cancellation-filter.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Quality status: Story Mode, Story kind, sourced from Tomas's notes, the Roamstay company context and your two Guest Support asks. Every supplied value travelled verbatim, criteria stay outcome-led and the Story ends on Acceptance criteria.

Three decisions I made, each easy to change:
- No `## Delivery` section, because you did not ask for a delivery view and nothing forced one. The notes' out-of-scope list is the natural No-gos entry if you want it added: the map view, sorting by cancellation deadline, any Partner Hub change and the property page badge. None of the four are in the Story.
- No `#### **References**` section, since no links came with the request.
- The two Guest Support asks landed as requirements and one acceptance criterion: the badge is dated at the property, and the filter survives a trip into a property page and back. Your date ask does not collide with Tomas's `d MMM` guest-locale pattern, because the pattern settles how the date is written while the property settles which date it is, so both are carried.

Next step: send a task split if you want the Story bundled with its task files, or tell me which requirement to adjust.