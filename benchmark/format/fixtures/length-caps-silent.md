# Free cancellation filter

## About

Guests can now filter search results to stays they can cancel for free. The filter sits beside the price filter on web and in both apps.

Search keeps today's results for a guest who leaves the filter off.

**References**

Brief

- `Free cancellation filter, PM brief`

The design frames are ready for review.

## Requirements

- The filter shows only stays whose cancellation deadline has not passed on the day of the search, counted in the property's own local time zone
- The label reads `Free cancellation, no charge before the deadline the property sets for each stay and room type`

## Acceptance criteria

- **Given** a guest turns the filter on and searches for a city with more than two hundred stays, **when** results load, **then** every stay shown can be cancelled for free

## Source copy

> Guests keep asking us for a way to see only the stays they can cancel for free, and today they have to open every listing and read the policy line by line to find out, which takes most of them several minutes per search.

| Surface | Where the filter sits and what it shows when no stay in the results can be cancelled for free |
|---|---|
| Web | Beside the price filter, with an empty state that suggests widening the dates or the price range |

```text
filter=free_cancellation&deadline_after=2026-10-01&tz=property&sort=ranking_default&page_size=40&include_count=true
```

## Ownership

The search squad owns the filter, and the ranking team owns the order of filtered results. Ranking already reads the cancellation deadline for its own scoring, so a second reader of the same field would drift from it. The price filter drifted the same way last year when two teams read the nightly rate differently.
