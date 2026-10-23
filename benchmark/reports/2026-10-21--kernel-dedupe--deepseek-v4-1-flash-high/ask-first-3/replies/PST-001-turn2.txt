```markdown
# Guest - Search - Free cancellation filter

* * *
## Problem
* * *
`Can I cancel this for free?` is the most common question in Guest Support chats before a booking, at about one in six pre-booking chats in August. 44% of August bookings were on a free cancellation rate plan, yet the only way to find one is to open property pages one at a time. A guest searching Lisbon for 4 nights with 2 adults gets 1,146 stays with no way to ask for the ones they can still cancel free. Search carries no filter for the term guests already use in chat, so the question reaches Guest Support instead.
* * *
##   

## Solution
* * *
The filter turns free cancellation into a search term, so a guest narrows a search to stays they can still cancel free instead of reading rate plans property by property. The price on a filtered card and the deadline in its badge follow the switch, and the filter holds through a property page and a date change.

**Expected outcomes**
* * *
*   Guests narrow a search to stays they can cancel free without opening a property page
*   Every price in a filtered list is one the guest can book and still cancel free
*   The badge names the date the property stops refunding, in the property's own date
*   The narrowed list survives a property page and a date change, and clears on a new search
* * *
##   

## Requirements
* * *
**Filter sheet**
* * *
- [] The filter sits in the search filter sheet, below `Price` and `Star rating`
- [] The filter is one on and off switch, with no settings inside it

**Results list**
* * *
- [] A stay shows only when at least one rate plan for the searched dates, guests and rooms has free cancellation, with its deadline not passed
- [] The result card carries the price of the cheapest free cancellation rate plan, even when a non-refundable rate is cheaper
- [] The results header shows the count of the filtered list, and Lisbon for 4 nights with 2 adults returns `312` stays against `1,146` unfiltered

**Filter state**
* * *
- [] The filter stays on while the guest changes dates or guests in the same search
- [] The filter stays on when the guest opens a property page and returns to the results
- [] The filter turns off when the guest starts a new search from the home screen

**Result card badge**
* * *
- [] With the filter on, every result card shows the deadline of the rate plan whose price is on the card, as `Free cancellation until 14 Oct`
- [] The deadline is the check-in date minus the partner's window, so a `14` day window puts it `14` days before check-in
- [] The badge carries the property's local date rather than the guest's, so a guest abroad reads the date on their confirmation email
- [] The date uses the `d MMM` pattern in the guest's locale, a day and a short month name with no year
- [] With the filter off, result cards carry no badge and stay as they are today

**Empty state**
* * *
- [] With no matching stay, the results list shows `No stays with free cancellation for these dates`
- [] The empty state carries one button, `Clear filter`
- [] `Clear filter` switches the filter off and reruns the same search

**Tracking**
* * *
- [] Turning the filter on fires the existing `filter_applied` event with `filter_name` set to `free_cancellation`
- [] No new event is added and the tracking plan is unchanged

**Release**
* * *
- [] iOS and Android ship the filter in `8.13.0`
- [] Web ships in the same week as the apps
- [] `search-service` ships first, so no app shows a filter the service cannot apply

**Not in this release**
* * *
- [] Map view pins keep showing every stay
- [] The result list offers no sort by cancellation deadline
- [] `Partner Hub` keeps its rate plan settings, since partners already set free cancellation per rate plan
- [] The property page carries no free cancellation badge, since it already lists the policy for each rate plan
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Filter and results
* * *
1 ) **A guest narrows a search to stays they can cancel free**
* * *
*   **Given** a guest has searched Lisbon for 4 nights with 2 adults
*   **When** they switch Free cancellation on in the filter sheet
*   **Then** the results list reloads to the stays with a rate plan they can still cancel free for those dates
*   **And** the results header shows the count for the narrowed list
* * *
- [] _Mark as done, if the criteria are met_

2 ) **A filtered price is one the guest can cancel free**
* * *
*   **Given** a stay offers a cheaper non-refundable rate plan and a dearer free cancellation one
*   **When** the guest reads its card with the filter on
*   **Then** the card carries the free cancellation price
*   **And** no card in the list carries a non-refundable price
* * *
- [] _Mark as done, if the criteria are met_

#### Filter state
* * *
3 ) **The narrowed list holds while the guest reads a property**
* * *
*   **Given** the filter is on and the guest is reading the results
*   **When** they open a property and come back to the results
*   **Then** the results return with the filter still on
*   **And** the header still shows the filtered count
* * *
- [] _Mark as done, if the criteria are met_

4 ) **A date or guest change keeps the filter on**
* * *
*   **Given** the filter is on
*   **When** the guest changes the dates or the guests and reruns the search
*   **Then** the filter stays on
*   **And** the results and the header count reflect the new dates
* * *
- [] _Mark as done, if the criteria are met_

5 ) **A new search starts with the filter off**
* * *
*   **Given** the filter is on
*   **When** the guest starts a new search from the home screen
*   **Then** the filter is off
*   **And** the results list shows every stay again
* * *
- [] _Mark as done, if the criteria are met_

#### Result card badge
* * *
6 ) **The badge names the date the guest can act on**
* * *
*   **Given** the filter is on
*   **When** the guest reads a result card from a timezone other than the property's
*   **Then** the badge shows the deadline of the rate plan whose price is on the card
*   **And** the date reads as the property's local date, whatever timezone the guest is in
* * *
- [] _Mark as done, if the criteria are met_

7 ) **A card with the filter off looks as it does today**
* * *
*   **Given** the filter is off
*   **When** the guest reads the results
*   **Then** no result card carries a badge
*   **And** the list, the prices and the cards look as they do today
* * *
- [] _Mark as done, if the criteria are met_

#### Empty state
* * *
8 ) **A guest with no free cancellation stays gets a way back**
* * *
*   **Given** no stay has a free cancellation rate plan for the searched dates
*   **When** the guest switches the filter on
*   **Then** the empty state replaces the results list
*   **And** it reads `No stays with free cancellation for these dates` with one `Clear filter` button
*   **And** `Clear filter` switches the filter off and reruns the same search
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/002 - Story-free-cancellation-filter.md`
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the badge string `Free cancellation until 14 Oct` and the empty state string, both exact product copy carried in backticks.
Quality: every floor met | Kind: Story | Energy: Standard

The Story carries the filter sheet switch, the eligibility and price rules, the badge, the empty state, the event and the release order, with every number from Tomas's notes verbatim. Both Guest Support asks landed as requirements and criteria, so the badge holds the property's local date and the filter survives a property page visit.

### Open items
1. **Badge date and locale**
   - **Situation:** The notes format the date with `d MMM` in the guest's locale, and Guest Support asks for the property's local date. I treated the property's timezone as the date itself and the guest's locale as the format only
   - **Open:** Confirm that reading, or say which one wins where a guest's timezone puts the deadline on a different day
2. **Out-of-release items**
   - **Situation:** Tomas's four out-of-release lines sit as a `Not in this release` group in Requirements, because no Delivery section holds No-gos
   - **Open:** Say if you would rather they move under a No-gos section
3. **Delivery section**
   - **Situation:** The Story ends on Acceptance criteria, as I recommended and you left standing
   - **Open:** Ask for a Delivery section if the squad wants estimation, rabbit holes and No-gos in the artifact

Want me to change anything?