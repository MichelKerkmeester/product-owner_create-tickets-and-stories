```markdown
# Guest - Search - Free cancellation filter

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
This story adds a Free cancellation filter to search in the Guest app on iOS, Android and web. When the filter is on, results show only stays the guest can still cancel for free. Each result card then shows the price of the free cancellation rate and its deadline.

### Problem
* * *
"Can I cancel this for free?" is the most common question guests ask in Guest Support chats before they book. It came up in about one in six pre-booking chats in August. 44% of August bookings were on a free cancellation rate plan. Even so, guests can only find these rates by opening each property page one at a time.

### Solution
* * *
Guests get the answer on the results list, because that is where they compare stays. A single switch in the filter sheet narrows the list to stays with free cancellation. The card then shows the free cancellation price and the deadline for that rate, so the guest can choose a stay without opening its property page. The filter stays on while the guest refines the same search and turns off when they start a new one.

#### **Expected outcomes**
* * *
*   Guests find stays with free cancellation from the results list without opening each property page
*   Fewer pre-booking Guest Support chats ask whether a stay can be cancelled for free
*   The deadline a guest sees on the result card matches the one in their confirmation email
* * *
##   

## Requirements
* * *
**Free cancellation filter**
* * *
*   The `Free cancellation` filter sits in the search filter sheet, below `Price` and `Star rating`
*   The filter is a single on and off switch
*   With the filter on, a stay shows in results only if at least one rate plan for the searched dates, guests and rooms has free cancellation and its deadline has not passed
*   With the filter on, the price on the result card is the cheapest free cancellation rate plan, even when a non-refundable rate is cheaper
*   The results header shows the filtered count
*   Test search: Lisbon for `4 nights` with `2 adults` goes from `1,146` stays to `312` stays with the filter on
*   The filter stays on when the guest changes dates or guests in the same search
*   The filter stays on when the guest opens a property and goes back to the results
*   The filter turns off when the guest starts a new search from the home screen

**Result card badge**
* * *
*   With the filter on, every result card shows the deadline of the rate plan whose price is on the card, as `Free cancellation until 14 Oct`
*   The deadline is the check-in date minus the partner's cancellation window, so a partner who allows free cancellation up to `14 days` before check-in gets a deadline 14 days before check-in
*   The deadline is the date at the property's location, not the date on the guest's device
*   The date uses the `d MMM` pattern in the guest's locale, which gives a day and a short month name with no year
*   With the filter off, result cards stay as they are today

**Empty state**
* * *
*   When the filter is on and no stay matches, the results list shows `No stays with free cancellation for these dates` and one button, `Clear filter`
*   `Clear filter` switches the filter off and reruns the same search

**Tracking**
* * *
*   No new event is added
*   Turning the filter on fires the existing `filter_applied` event with `filter_name` set to `free_cancellation`
*   The tracking plan does not change, as confirmed by Nadia on `2026-09-17`

**Release**
* * *
*   iOS and Android ship the filter in `8.13.0`
*   Web ships the filter in the same week as the apps
*   `search-service` ships first, so no app ever shows a filter the service cannot apply

**Not in this release**
* * *
*   The map view does not change, and its pins keep showing every stay while the filter is on
*   Results cannot be sorted by cancellation deadline
*   Partner Hub does not change, because partners already set free cancellation per rate plan
*   The property page gets no badge, because it already lists the policy for each rate plan
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **With the filter on, results show only stays the guest can still cancel for free**
* * *
*   **Given** a guest has run a search
*   **When** they turn on the Free cancellation filter
*   **Then** the results list and the header count include only stays with a free cancellation rate whose deadline has not passed, for the dates, guests and rooms they searched
*   **And** each card shows the free cancellation price, even when the stay has a cheaper non-refundable rate
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **The card shows a deadline the guest can trust**
* * *
*   **Given** the filter is on
*   **When** the guest reads a result card
*   **Then** the card shows the free cancellation deadline for the rate plan whose price it shows, as the date at the property's location, written in the guest's language
*   **And** after booking that rate plan, the deadline in the confirmation email is the same date
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **With the filter off, results stay as they are today**
* * *
*   **Given** the filter is off
*   **When** the guest views the results
*   **Then** the stays, prices and result cards are the same as before this change
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **The filter stays on for the rest of the same search**
* * *
*   **Given** the filter is on
*   **When** the guest changes dates or guests, or opens a property and goes back to the results
*   **Then** the filter is still on, and the results reflect it
*   **And** when the guest starts a new search from the home screen, the filter is off
* * *
- [ ] _Mark as done, if the criteria are met_

5\. **A search with no matching stays still gives the guest a way forward**
* * *
*   **Given** the filter is on and no stay matches the search
*   **When** the results load
*   **Then** the guest sees the empty state with a single action to clear the filter
*   **And** using that action switches the filter off and shows the full results for the same search
* * *
- [ ] _Mark as done, if the criteria are met_

6\. **Turning the filter on is recorded in analytics**
* * *
*   **Given** a guest is on any platform
*   **When** they turn the filter on
*   **Then** analytics records it through the existing filter event, named for the free cancellation filter, and no new event is sent
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/NNN - Story-free-cancellation-filter.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

I wrote this as a **Story** covering Tomas's notes plus both Guest Support asks. Every number and exact string from his notes is in Requirements unchanged. The six acceptance criteria describe what the guest can rely on and leave out the values.

**How I placed the Guest Support asks:**
- **Property's local date:** this fits with Tomas's rule rather than replacing it. The date is taken from the property's location, and it is still written in the `d MMM` pattern in the guest's locale. Tell me if Guest Support meant the language too.
- **Filter stays on after opening a property:** this is a new line in the filter group, next to Tomas's rule about changing dates or guests.

**Changes from what I said in the clarification:**
- **Exclusions:** Tomas's four exclusions are in a "Not in this release" group under Requirements, not in the Solution text. The map pins are a rule a developer could get wrong, and his notes list the exclusions as their own group.
- **No Delivery section:** you didn't ask for one, so the Story ends on Acceptance criteria.
- **No References section:** no links were supplied.

**Things I added that aren't in the sources:** strike any you don't want.
- The second and third expected outcomes (fewer pre-booking chats about free cancellation, and the card deadline matching the confirmation email).
- The "And" line in criterion 2 about the confirmation email.
- Criterion 3, which checks that nothing changes with the filter off.

All of these are based on Tomas's "Why" section or Guest Support's reasoning.

**Not covered:** the Story doesn't say how the filter works together with the Price filter. Tomas's notes don't cover it, and I haven't added a rule for it.

**Next step:** check that the local-date reading is right. Then the Story is ready to split into tasks.