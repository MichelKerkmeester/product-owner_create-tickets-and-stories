```markdown
# Guest - Search - Free cancellation filter

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
The search filter sheet holds two filters today, Price and Star rating. This story adds a Free cancellation filter to that sheet, so a guest sees only the stays they can cancel for free, with the deadline of the rate plan behind the price on the result card. It covers the filter sheet, the results list and its empty state on iOS, Android and web.

#### Problem
* * *
*   "Can I cancel this for free?" is the question Guest Support answers most before a booking, about one in six pre-booking chats in August
*   `44%` of August bookings were on a free cancellation rate plan
*   Those rate plans are findable only by opening property pages one at a time

#### Solution
* * *
Add one switch to the filter sheet the guest already uses, so a refundable stay is findable from the results list instead of one property page at a time. Everything else about the search stays as it is, and the result card carries the one fact a guest needs to decide, which is how long they have to cancel.

**Expected outcomes**
* * *
*   A guest finds a stay they can cancel for free without opening property pages one at a time
*   The deadline that governs the free cancellation sits on the result card, so the guest can judge it before choosing
*   Guest Support answers fewer pre-booking questions asking whether a stay can be cancelled for free
* * *
##   

## Requirements
* * *

**Filter sheet**
* * *
- [] The filter sits in the search filter sheet below `Price` and `Star rating`, is named `Free cancellation` and is a single on and off switch
- [] A stay appears in the results only when at least one rate plan for the searched dates, guests and rooms has free cancellation and its deadline has not passed
- [] The price on a result card is the cheapest free cancellation rate plan, even where a non-refundable rate is cheaper
- [] On the Lisbon 4-night, 2-adult test search the filtered count reads `312` where the unfiltered count reads `1,146`
- [] The filter stays on while the guest changes dates or guests inside the same search, and when they open a property page and return to the results
- [] The filter is off at the start of a new search from the home screen
- [] The map view keeps showing every stay while the filter is on

**Result card badge**
* * *
- [] With the filter on, every result card shows the deadline of the rate plan whose price is on the card, reading `Free cancellation until 14 Oct`
- [] The deadline is the check-in date minus the partner's cancellation window, so a partner who allows free cancellation up to `14 days` before check-in shows a deadline `14 days` before check-in
- [] The deadline reads as the property's local date, so a guest abroad sees the same date the confirmation email carries
- [] The date follows the `d MMM` pattern in the guest's locale, a day and a short month name with no year
- [] With the filter off, result cards are unchanged

**Empty state**
* * *
- [] When no stay matches, the results list reads `No stays with free cancellation for these dates` with one action, `Clear filter`
- [] `Clear filter` switches the filter off and reruns the same search

**Tracking**
* * *
- [] Turning the filter on fires the existing `filter_applied` event with `filter_name` set to `free_cancellation`, and adds no new event or tracking plan row

**Release**
* * *
- [] iOS and Android ship the filter in `8.13.0`, with web in the same week
- [] `search-service` ships the filter first, so no app shows a filter the service cannot apply
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Filter sheet
* * *
1\. **A guest sees only the stays they can cancel for free**
* * *
*   **Given** a guest searching Lisbon for 4 nights with 2 adults
*   **When** they turn the Free cancellation filter on
*   **Then** every stay in the results has at least one rate plan for those dates, guests and rooms with free cancellation and a deadline that has not passed
*   **And** the results header counts only the stays shown
* * *
- [] _Mark as done, if the criteria are met_

2\. **A filtered search stays filtered while the guest explores**
* * *
*   **Given** the guest has the Free cancellation filter on
*   **When** they open a property page and return to the results
*   **Then** the results are still filtered and the filter switch is still on
*   **And** the filter also holds while they change dates or guests inside that search
* * *
- [] _Mark as done, if the criteria are met_

3\. **A new search starts unfiltered**
* * *
*   **Given** the guest had the Free cancellation filter on
*   **When** they start a new search from the home screen
*   **Then** the results are unfiltered and the filter switch is off
* * *
- [] _Mark as done, if the criteria are met_

#### Result card badge
* * *
4\. **The result card says how long the guest has to cancel**
* * *
*   **Given** the guest has the Free cancellation filter on
*   **When** the results load
*   **Then** every result card states the last day the guest can cancel for free, as the property's local date, which is the date on the confirmation email
*   **And** the price on the card is the price of the rate plan that deadline belongs to
* * *
- [] _Mark as done, if the criteria are met_

#### Empty state
* * *
5\. **A search with no refundable stay offers a way back**
* * *
*   **Given** the guest has the Free cancellation filter on
*   **When** no stay matches those dates
*   **Then** the results list states that no stay with free cancellation matches these dates, with one action, `Clear filter`
*   **And** that action turns the filter off and reruns the same search
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/002 - Story-free-cancellation-filter.md`

Artifact kind: Story. Tomas's notes govern the spec, with the Roamstay context supplying the surfaces, locales, event conventions and release facts, and the two Guest Support asks folded in.

Quality status: PASS. Accuracy, Completeness, Relevance, Actionability, Clarity and Mechanism Depth all clear their floors. House grammar validated, with `## Delivery` omitted because nobody asked for a delivery view and nothing forced one, so Acceptance criteria closes the artifact.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the house-format tokens (`* * *`, `- []`, `1\.`, `##   `, `_Mark as done, if the criteria are met_`) and the repeated `Given`, `When`, `Then` and `And` labels, all of which the Barter grammar fixes verbatim.

Where the two Guest Support asks landed: the property's local date is a constraint in Result card badge, sitting beside the `d MMM` locale pattern from Tomas's notes, and returning from a property page with the filter still on joins the same persistence rule as changing dates or guests.

Three things worth your eye before this goes out. I read the local date and the `d MMM` pattern as one badge doing two jobs, where the property decides which day and the guest's locale decides how it is written, so strike that if Guest Support meant the format follows the property. Tomas's `Not in this release` list is split deliberately: the map behaviour is carried as a constraint in Filter sheet, while sorting by cancellation deadline, the Partner Hub change and the property page badge are out of this story by decision. No links came through, so `#### **References**` is omitted rather than written empty, and the closing lines naming Ines for the frames and Dario for the search-service change stay out of the artifact.

Next step: tell me what to strike or add, or ask for the task breakdown and I will cut the Search squad tasks from these requirements.