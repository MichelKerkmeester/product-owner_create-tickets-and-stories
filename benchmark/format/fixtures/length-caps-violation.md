# Free cancellation filter

## About

Guests can now filter search results to stays they can cancel for free. The filter sits beside the price filter on web and in both apps.

Search keeps today's results for a guest who leaves the filter off.

Support asked for the filter after refund contacts rose over the summer.

## Requirements

- The filter shows only stays whose cancellation deadline has not passed on the day of the search, counted in the property's own time zone rather than the guest's
- The filter label reads `Free cancellation`. It sits beside the price filter

## Ownership

The search squad owns the filter and the ranking team owns the order of filtered results, because ranking already reads the cancellation deadline for its own scoring and a second reader of the same field would drift from it over time, which is what happened with the price filter last year when two teams read the nightly rate in different ways.

The filter ships on web first. The apps follow a week later. The label is the same on every surface. The count of matching stays shows on the button.

## Edge cases

- When a guest turns the filter on after picking dates, the results reload at once and keep the sort order, the map position and every other filter the guest had set
