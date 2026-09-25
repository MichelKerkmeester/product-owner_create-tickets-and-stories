# Free cancellation filter, PM notes

Source: PM notes from the Search squad kickoff, shared in the Search squad space
Written by Tomas, Product Manager, Search, on 2026-09-18, after Thursday's kickoff with Ines and the Search engineers

I've written down every number we agreed, so nobody has to dig through the design file or the kickoff recording for it.

## Why

"Can I cancel this for free?" is the most common question in Guest Support chats before a booking, about one in six pre-booking chats in August. 44% of August bookings were on a free cancellation rate plan, yet guests can only find those rates by opening each property page one at a time.

## What we're building

A Free cancellation filter in the search filter sheet, below Price and Star rating, which are the only two filters there today. It's a single on and off switch.

With the filter on:

- A stay shows in results only if at least one rate plan for the searched dates, guests and rooms has free cancellation and its deadline hasn't passed
- The price on the result card is the cheapest free cancellation rate plan, even when a non-refundable rate is cheaper
- The results header shows the new count. Our test search, Lisbon for 4 nights with 2 adults, goes from 1,146 stays to 312 stays with the filter on
- The filter stays on while the guest changes dates or guests in the same search, and turns off when they start a new search from the home screen

## Result card badge

With the filter on, every result card shows the deadline of the rate plan whose price is on the card, as `Free cancellation until 14 Oct`.

- The deadline is the check-in date minus the partner's cancellation window. A partner who allows free cancellation up to 14 days before check-in gets a deadline 14 days before check-in
- The date uses the `d MMM` pattern in the guest's locale, so a day and a short month name with no year
- With the filter off, result cards stay as they are today

## Empty state

When no stay matches, the results list shows `No stays with free cancellation for these dates` and one button, `Clear filter`. Clear filter switches the filter off and reruns the same search.

## Tracking

No new event. Turning the filter on fires the existing `filter_applied` event with `filter_name` set to `free_cancellation`. Nadia confirmed on 2026-09-17 that this fits the analytics conventions and needs no tracking plan change.

## Release

- iOS and Android in `8.13.0`
- Web in the same week as the apps
- search-service ships first, so no app ever shows a filter the service can't apply

## Not in this release

- The map view. Pins keep showing every stay until we follow up
- Sorting by cancellation deadline
- Any Partner Hub change. Partners already set free cancellation per rate plan
- A badge on the property page, which already lists the policy for each rate plan

Questions to me in the Search squad channel. Ines owns the frames and Dario leads the search-service change.
