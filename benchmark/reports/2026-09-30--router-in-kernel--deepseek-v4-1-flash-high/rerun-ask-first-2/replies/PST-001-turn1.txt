```markdown
# Guest - Search - Free cancellation filter

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
The search filter sheet holds two filters today, Price and Star rating. This story adds a Free cancellation switch so a guest can see only the stays they can cancel for free on their dates, each priced at its free cancellation rate.

#### Problem
* * *
The most common question in Guest Support chats before a booking is whether the guest can cancel for free, at about one in six pre-booking chats in August. 44% of August bookings were on a free cancellation rate plan, and the only way to find one today is to open property pages one at a time.

#### Solution
* * *
Turn the cancellation question into a filter instead of a per-property hunt. One switch in the search filter sheet narrows the results to stays with a free cancellation rate plan for the guest's dates and prices them at that plan, so a guest can compare the stays that keep their options open.

**Expected outcomes**
* * *
*   Guests find free cancellation stays in the results list rather than one property page at a time
*   Every stay shown under the filter can be cancelled free before its deadline, at the price the card shows
*   Each card tells the guest when free cancellation ends for the rate plan it prices
* * *
##   

## Requirements
* * *
**Search filter sheet**
* * *
- [] The filter sits in the search filter sheet below `Price` and `Star rating`
- [] The filter is a single on and off switch
- [] With the filter on, a stay shows only when a rate plan for the searched dates, guests and rooms is still free to cancel
- [] With the filter on, the card price is the cheapest free cancellation rate plan, even when a non-refundable rate plan is cheaper
- [] With the filter on, the results header shows the new stay count
- [] On the Lisbon test search of 4 nights with 2 adults, the header count moves from `1,146` stays to `312` stays
- [] The filter stays on while the guest changes dates or guests in the same search
- [] The filter turns off when the guest starts a new search from the home screen

**Result card badge**
* * *
- [] With the filter on, every card shows the deadline of the rate plan it prices, as `Free cancellation until 14 Oct`
- [] The deadline is the check-in date minus the partner's cancellation window, so a `14`-day window puts it `14` days before check-in
- [] The date uses the `d MMM` pattern in the guest's locale, a day and a short month name with no year
- [] With the filter off, result cards stay as they are today

**Empty state**
* * *
- [] When no stay matches, the results list shows `No stays with free cancellation for these dates`
- [] The empty state carries one button, `Clear filter`
- [] `Clear filter` switches the filter off and reruns the same search

**Tracking**
* * *
- [] No new event is added
- [] Turning the filter on fires the existing `filter_applied` event with `filter_name` set to `free_cancellation`
- [] No tracking plan change is needed, confirmed on `2026-09-17`

**Release**
* * *
- [] iOS and Android ship the filter in `8.13.0`
- [] Web ships in the same week as the apps
- [] `search-service` ships first, so no app shows a filter the service cannot apply

**Not in this release**
* * *
- [] No filter on map view pins, which keep showing every stay
- [] No sorting by cancellation deadline
- [] No Partner Hub change, because partners already set free cancellation per rate plan
- [] No badge on the property page, which already lists the policy for each rate plan
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **A guest sees only stays they can cancel for free**
* * *
*   **Given** a guest searching a destination with dates, guests and rooms
*   **When** they turn on Free cancellation
*   **Then** every stay in the results has at least one rate plan for those dates, guests and rooms that is free to cancel before its deadline
*   **And** the price on each card is a free cancellation rate, not a cheaper non-refundable one
*   **And** the results header count matches the stays the list shows
* * *
- [] _Mark as done, if the criteria are met_

2\. **The card says when free cancellation ends**
* * *
*   **Given** a guest with the filter on
*   **When** the results list loads
*   **Then** each card states the last date free cancellation can be used for the rate plan whose price it shows
* * *
- [] _Mark as done, if the criteria are met_

3\. **The filter holds through a change of the same search and resets on a new one**
* * *
*   **Given** a guest with the filter on
*   **When** they change the dates or the number of guests in the same search
*   **Then** the filter is still on and the results answer the new dates and guests
*   **And** a new search started from the home screen opens with the filter off
* * *
- [] _Mark as done, if the criteria are met_

4\. **A search with no match says so and offers one way out**
* * *
*   **Given** a guest with the filter on and no matching stay for their dates
*   **When** the results list renders
*   **Then** the empty state replaces the results, with its message and one action
*   **And** that action clears the filter and runs the same search again
* * *
- [] _Mark as done, if the criteria are met_

5\. **A guest who has not turned the filter on sees the results they see today**
* * *
*   **Given** a guest searching with the filter off
*   **When** the results list renders
*   **Then** the cards are unchanged, with no cancellation deadline on them
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/001 - Story-guest-search-free-cancellation-filter.md`

Artifact kind: **Story** (requirements present, so not the Epic shape), Standard energy, house format, no `## Delivery` section. Delivery is opt-in, nobody asked for it here, and no requirement carries an `**Open:**` line or an undated external constraint, so Acceptance criteria closes the artifact.

Quality: six floors pass. Accuracy 9, since every claim traces to Tomas's notes or the company context and no figure, name or platform detail was invented. Clarity and Mechanism Depth decide a Story, and both clear: each criterion resolves to one reading, and the Problem carries the why (a one-in-six question that costs a property page per stay). Requirements holds only hard constraints, so no build steps and no outcomes leaked in.

HVR self-scan: 0 hard blockers. Fixed: no banned terms, em dashes, semicolons or Oxford commas were needed, and no source hedge survived ("I've written down", "Questions to me", the "simply" framing). Kept with reason: `Given`, `When`, `Then` and `And` repeat as fixed house labels, and the story preamble and the `All acceptance criteria below must be met...` line are the house's own wording.

Two things to check before this goes to the squad:

* The two Guest Support asks are not in Tomas's notes, so nothing about them is in this Story. I did not guess at them. Send them over and they land as requirement items, and I will flag any that collide with the **Not in this release** group.
* I carried the four **Not in this release** items into Requirements as constraints, so a build cannot filter map pins, add a deadline sort, change Partner Hub or add a property page badge by accident. The words are Tomas's, the placement in Requirements is mine, so strike that group if you would rather keep the exclusions out of the spec.

One more gap worth knowing: no design or Figma link came with the notes, so the Story carries no `#### **References**` block. Send the frame link and I will add it.

Next step: pass on the Guest Support asks, and tell me if you want this broken into tasks for the Search squad (name the split, or I will propose one) and I will render the Story with its task files.