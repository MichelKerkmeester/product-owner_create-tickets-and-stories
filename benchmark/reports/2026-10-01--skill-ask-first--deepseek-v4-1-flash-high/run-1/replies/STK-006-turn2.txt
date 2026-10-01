`Path: export/002 - task-booking-funnel-events.md`

`Verified: read-back succeeded; 75 lines`

`HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.`

**Quality summary:** Task shape, all required sections present. H1, `## About` at H2, `### Requirements` at H3, three numbered groups each with a `**Checklist**` of `- []` items, `---` dividers throughout. Every event, status and property from the plan carries its supplied name and value in backticks, `checkout_complete` stays `deprecated` with its `2026-11-01` removal, `booking_confirmed` stays the `booking-service` server event that every booking count reads, and `date_changed` stays out as `proposed`. Body is 672 words, inside the 900-word task budget. Sources untouched, both checksums matching the staged fixtures.

This is the Data team's `TRK` task: Nadia checks each event in `events-collector` as the squads ship it, the funnel dashboard moves to `booking_confirmed`, and the collector drops `checkout_complete` on `2026-11-01`. The FE client-events build and the BE `booking_confirmed` build are named as work happening elsewhere, so neither is scoped into these requirements. Two boundaries worth confirming: I read your answer as keeping the event table as written, so no status changed, and I left `date_changed` out rather than inventing its trigger or properties.

Want me to tweak the split, or move this into ClickUp once the FE and BE tasks exist so the dependency links can be real?