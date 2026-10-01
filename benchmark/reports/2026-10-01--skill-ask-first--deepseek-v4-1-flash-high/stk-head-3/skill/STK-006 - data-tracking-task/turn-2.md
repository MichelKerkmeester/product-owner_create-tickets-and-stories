**Path:** `export/002 - task-booking-funnel-events.md` (supersedes `001`)

Verified: read-back succeeded; 74 lines

HVR self-scan: 0 hard blockers. Fixed: scoping the rewrite surfaced no blocked term; the About opening was cut from 83 words to two 58-word paragraphs to meet the paragraph cap, a conciseness edit and so not counted. Kept with reason: backticked supplied identifiers and status words (`checkout_complete`, `booking_confirmed`, `events-collector`, `total_amount_minor`, `_minor`, `pay_now`, `pay_at_property`, `proposed`) stay verbatim because the plan supplies them.

**Quality summary**

| Dimension | Reading |
| --- | --- |
| Completeness | Covers the user's three Data workstreams as three numbered groups, with a check per event in `events-collector` |
| Accuracy | Every event, property, format, date and status traces to the plan, with the closed refinement and the trimmed scope reflected |
| Actionability | Each item is observable in `events-collector` or on the dashboard |
| Clarity | One reading per item, no build steps, no FE or BE work absorbed |
| Relevance | Data-team scope only: checks, dashboard move, collector drop |
| Mechanism depth | The About states why the funnel is broken today, so the checks and the ordering follow from it |

**Summary.** The task is now the Data team's `TRK` slice: verify each funnel event as it lands in `events-collector`, move the funnel dashboard to `booking_confirmed` before `2026-11-01`, and drop `checkout_complete` from the collector on that date. The client events and `booking_confirmed` are named as separate FE and BE tasks this one checks rather than builds, and the refinement closure is recorded in the References line.

**Judgment calls**

- Title `DATA - Guest app - TRK - Booking funnel events`, surface read as Guest app. Say so if it should read as a Data-only internal title
- `room_selected` from Android is accepted a few hundred milliseconds late, from Oskar's thread rather than the event table
- The two dashboard checks on revenue per step and Trips double-counting are the acceptance side of the plan's first two problems, not new requirements

No ClickUp tooling is in this runtime, so nothing was pushed. Want the FE and BE sibling tasks drafted next, or the collector drop split into its own task with the removal date as the only anchor?