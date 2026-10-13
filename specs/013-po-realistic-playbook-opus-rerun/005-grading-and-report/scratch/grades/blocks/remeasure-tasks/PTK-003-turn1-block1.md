# BE task: carrier label webhook fix (clarification)

I'll create the BE task for Joris. The three sources cover the five points well. These are the gaps I would otherwise have to guess at:

**Title and links:**
- Is `BE - SHIP - Label webhook answers inside the carrier timeout` right, or do you want different wording?
- Noor exported the thread "to attach to the label webhook ticket". Is there an existing ticket, parent task or epic I should link? Do you have links for the thread and Joris's API notes?

**Open shipment guard:**
- Does a shipment that received `label.failed` count as closed? If it doesn't, the guard would block the `SERVICE_UNAVAILABLE` re-create that the carrier asks for
- The carrier hasn't yet said whether `SERVICE_UNAVAILABLE` can be followed by `label.created` for the same shipment. Should the task list that as an open dependency, or hold the re-create until they answer?
- Should the handling for `ADDRESS_INVALID` and `OTHER` stay as it is today?

**10-minute GET:**
- The GETs share the 20 requests per second with the POSTs, which run at up to 14 a second around the cut-off. Should the task require the GET to back off on `429` and respect `Retry-After`, or leave that to Joris?
- When the GET returns `label_failed`, should it follow the same path as a `label.failed` event, guard included?

**Alerting:**
- Should `#fulfilment-alerts` get one post per stuck shipment, or one post listing them all?
- Which on-call rotation or paging tool takes the page? Should it page outside working days too?
- Should an event that sits unprocessed in the queue count toward the same alert?

**Acceptance:**
- Now that the work runs from a queue, is there a target for how soon a label reaches the pack station after the event? The company context only says the label arrives "usually within a minute"
- Should QA replay the 2026-09-15 case as an acceptance check? That means the warehouse system taking 6 to 9 seconds while the carrier retries

**Validation:**
- Is anything in Noor's summary still not agreed, or has anything changed since 2026-09-16?
