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
- [] The filter stays on when the guest opens a property and goes back to the results
- [] The filter turns off when the guest starts a new search from the home screen

**Result card badge**
* * *
- [] With the filter on, every card shows the deadline of the rate plan it prices, as `Free cancellation until 14 Oct`
- [] The deadline is the check-in date minus the partner's cancellation window, so a `14`-day window puts it `14` days before check-in
- [] The deadline date is the property's local date
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
*   **And** that date is the property's local date, which the guest can check against the confirmation email
* * *
- [] _Mark as done, if the criteria are met_

3\. **The filter holds through a change of the same search and resets on a new one**
* * *
*   **Given** a guest with the filter on
*   **When** they change the dates or the number of guests in the same search
*   **Then** the filter is still on and the results answer the new dates and guests
*   **And** the filter is still on after the guest opens a property and comes back to the results
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

Artifact kind: **Story**, refined in place. The delivered Story is the structural baseline, so this keeps the same export-equivalent name rather than taking a new number.

What the two asks changed, and nothing beyond them:

* Result card badge gains `The deadline date is the property's local date`, sitting directly above Tomas's `d MMM` line so a developer reads the date basis and the date format as two separate rules.
* Search filter sheet gains `The filter stays on when the guest opens a property and goes back to the results`, inside the existing persistence rules, which already scope the filter's life to one search. It extends that rule rather than contradicting it.
* Acceptance criteria 2 and 3 each gained one `**And**` line to prove the new behavior. No criterion was rewritten, no requirement removed and no order changed.

One interpretation to confirm: I read "the property's local date" as the date basis, and left the format on Tomas's `d MMM` in the guest's locale, which is also what the company context says the apps do for dates. Read that way the two fit together. If Guest Support means the property's locale should drive the format as well, that collides with Tomas's line and someone has to pick which wins before a build.

Quality: six floors pass. Accuracy 9, since the two new items carry Guest Support's words and the property-local date is their ask rather than my inference. Clarity holds because criterion 2 and 3 still resolve to one reading each after the added `**And**` lines. Relevance holds because the round-trip item sits in the same-search rules and no new section was invented. No `## Delivery` section, since you have confirmed nothing in the notes is open and no external constraint carries an undated gate.

HVR self-scan: 0 hard blockers. Fixed: nothing new needed a repair. Kept with reason: `Given`, `When`, `Then` and `And` repeat as fixed house labels, the story preamble and the `All acceptance criteria below must be met...` line are the house's own wording, and `1,146` keeps the comma and `d MMM` keeps the source's notation.

Next step: this is ready for the Search squad as it stands. Tell me if you want it broken into tasks (name the split, or I will propose one), and send the design frame link whenever you have it so the `#### **References**` block can go in.