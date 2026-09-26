```markdown
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
```

Export-equivalent path: `export/001 - task-carrier-label-webhook-fix-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

I haven't drafted the task yet. `$t` asks its intake question first and waits for your answer. I read all three context files. Noor's five points, the rejection of polling only and the carrier's numbers are all clear:

- the 5-second timeout
- retries over 7 hours 21 minutes
- `event_id` is stable across retries
- 20 requests per second shared across the account

The questions cover what the sources leave open. The biggest one is the guard: as written, it could block the re-create the carrier asks for after `SERVICE_UNAVAILABLE`, and the carrier hasn't said whether a label can still arrive after that failure.

Once you answer, the task will be `export/002 - task-...` with the title following your ticket convention (`BE - SHIP - ...`, no surface). It will describe the outcome and the reason for each point, not the implementation.