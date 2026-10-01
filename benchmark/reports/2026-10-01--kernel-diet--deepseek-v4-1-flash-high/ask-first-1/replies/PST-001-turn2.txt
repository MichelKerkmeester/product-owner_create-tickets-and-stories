```markdown
# Guest - Search - Free cancellation filter

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
The Guest app search filter sheet holds two filters today, Price and Star rating, and neither answers the question guests ask before they book. This story adds a Free cancellation filter to the search filter sheet on iOS, Android and web, so a guest sees only the stays they can still cancel for free.

#### Problem
* * *
Guest Support answers `Can I cancel this for free?` in about one in six pre-booking chats, and 44% of August bookings were on a free cancellation rate plan. Guests can only find those rates by opening property pages one at a time, so the refundable rate stays hidden in the results list they already have.
* * *

#### Solution
* * *
A single Free cancellation switch joins Price and Star rating in the filter sheet, and turning it on narrows the results to stays with a rate plan the guest can still cancel for free. The price on each result card becomes the cheapest free cancellation rate, so the number the guest compares belongs to the policy they are reading, and the same card shows that rate's deadline.
* * *

**Expected outcomes**
* * *
*   Guests find a stay they can cancel for free without opening property pages one at a time
*   The price and the deadline on a result card belong to the same rate plan
*   Guest Support answers the pre-booking cancellation question by pointing at the filter
* * *

## Requirements
* * *
**Filter sheet**
* * *
- [] The filter sits in the search filter sheet below Price and Star rating
- [] The filter is a Free cancellation switch with one on position and one off position

**Matching stays**
* * *
- [] A stay shows only if at least one rate plan for the searched dates, guests and rooms has free cancellation
- [] A rate plan whose deadline has passed does not keep the stay in the results
- [] The price on a result card is the cheapest free cancellation rate plan, even when a non-refundable rate plan is cheaper
- [] With the filter on, the header count on the Lisbon test search, 4 nights with 2 adults, goes from 1,146 stays to 312 stays

**Filter retention**
* * *
- [] The filter stays on while the guest changes dates or guests in the same search
- [] The filter stays on when the guest opens a property page and comes back to the results
- [] The filter turns off when the guest starts a new search from the home screen

**Result card badge**
* * *
- [] With the filter on, every result card shows the deadline of the rate plan priced on it, as `Free cancellation until 14 Oct`
- [] The deadline is the check-in date minus the partner's cancellation window
- [] A partner who allows free cancellation up to 14 days before check-in gets a deadline 14 days before check-in
- [] The badge shows the deadline as the property's local date, so a guest abroad can check it against their confirmation email
- [] The date uses the `d MMM` pattern in the guest's locale, a day and a short month name with no year
- [] With the filter off, result cards stay as they are today

**Empty state**
* * *
- [] When no stay matches, the results list shows `No stays with free cancellation for these dates`
- [] The empty state carries one button, `Clear filter`
- [] `Clear filter` switches the filter off and reruns the same search

**Tracking**
* * *
- [] No new event is added for the filter
- [] Turning the filter on fires the existing `filter_applied` event with `filter_name` set to `free_cancellation`

**Release**
* * *
- [] iOS and Android ship the filter in `8.13.0`
- [] Web ships the filter in the same week as the apps
- [] `search-service` ships first, so no app ever shows a filter the service cannot apply

**Out of this release**
* * *
- [] The map view pins keep showing every stay, with the filter not applied to them
- [] No sort by cancellation deadline is added to the results
- [] Partner Hub is unchanged, because partners already set free cancellation per rate plan
- [] The property page gains no badge, because it already lists the cancellation policy for each rate plan
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **Guests narrow the results to stays they can cancel for free**
* * *
*   **Given** the guest has searched for their dates, guests and rooms
*   **When** they turn the Free cancellation filter on in the filter sheet
*   **Then** the results hold only stays with a rate plan they can still cancel for free
*   **And** the count in the header and the list behind it agree
* * *
- [] _Mark as done, if the criteria are met_

2\. **The price on a result card belongs to the rate the guest is comparing**
* * *
*   **Given** the filter is on and a stay also has a cheaper non-refundable rate plan
*   **When** the guest reads the result card
*   **Then** the price shown is the cheapest free cancellation rate plan
*   **And** the deadline on the card is that rate plan's deadline
* * *
- [] _Mark as done, if the criteria are met_

3\. **The deadline reads as the property's date**
* * *
*   **Given** the filter is on and the guest is in a different time zone from the property
*   **When** they read the deadline on a result card
*   **Then** the date is the property's local date, so it matches the confirmation email
*   **And** it shows in the guest's own locale
* * *
- [] _Mark as done, if the criteria are met_

4\. **The filter holds through the search**
* * *
*   **Given** the guest has the filter on with results in front of them
*   **When** they change dates or guests, or open a property page and come back
*   **Then** the filter is still on and the results still answer it
*   **And** a new search started from the home screen turns it off
* * *
- [] _Mark as done, if the criteria are met_

5\. **An empty result set gives the guest a way back**
* * *
*   **Given** the filter is on and no stay matches
*   **When** the guest reads the empty state and takes its one action
*   **Then** the filter is off and the same search runs again with the stays back in the list
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: export/002 - Story-free-cancellation-filter.md

Detected: Story Mode, Story shape. The clarification took 001 in this lane, so the Story takes 002.

Quality status. House format passes: preamble, About umbrella, H2 sections, `* * *` closes above every `##   ` spacer, `- []` checkboxes, `1\.` criteria with a Mark-as-done line and no divider before the next. Source coverage passes: every line of Tomas's notes and both Guest Support asks lands in Requirements or a criterion, with the supplied values intact (`1,146` to `312`, `Free cancellation until 14 Oct`, `d MMM`, `filter_applied`, `free_cancellation`, `No stays with free cancellation for these dates`, `Clear filter`, `8.13.0`). `#### **References**` is omitted because no links were supplied, and `## Delivery` is omitted because you did not ask for it and nothing in the artifact forces one.

Three readings of mine, so you can strike any of them. The first ask sits beside the locale pattern rather than against it, so the badge takes its calendar date from the property's timezone and its format from the guest's locale. The property's local date applies to the badge as you asked, and I left the matching rule as Tomas wrote it, so a stay still turns on whether the rate plan's deadline has not passed. I housed his `Not in this release` list as a Requirements group rather than lose it, since the story has no Delivery section to hold No-gos.

HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: source-fixed list counts in Requirements, where each group's item count comes from the notes rather than from me, and `TBD...` does not appear because no Delivery section was written.

Next step: say whether those three readings hold, and if you want the task breakdown, name the split and it follows as the same Story bundle.