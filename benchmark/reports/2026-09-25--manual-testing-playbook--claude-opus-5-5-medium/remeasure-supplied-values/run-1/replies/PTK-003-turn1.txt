```markdown
I'll create the BE task for the label webhook fix. Before drafting, I need the decisions below in one response:

**Title & links:**
- Does `BE - SHIP - Label webhook retries and duplicate labels` work, or do you already have a working title?
- Should I name a parent task, an epic or related tickets, even without links?
- Should the thread and the API notes go in as references?

**Failure codes outside the thread:**
- The guard and the re-create only cover `SERVICE_UNAVAILABLE`. Should `ADDRESS_INVALID` and `OTHER` keep today's behaviour and be named out of scope?
- A shipment waiting on a CS address fix will still have no label after `30 minutes`. Should it count towards the `#fulfilment-alerts` post and the `more than 5` page, or should it be left out?

**Open shipment and the 10-minute GET:**
- Which carrier statuses count as open for the guard: only `label_pending`, or `label_ready` as well?
- If the GET returns `label_failed`, should it follow the same path as a `label.failed` event?
- The carrier hasn't confirmed whether a `label.created` can follow a `SERVICE_UNAVAILABLE` failure for the same shipment. Should the task require the guard to hold either way, or record this as an open question?
- Should the task require the GET to stay inside the shared `20 requests per second` limit and to honour `429` with `Retry-After`?

**Queue processing:**
- If a queued event fails, for example because the warehouse system is slow again, should it be retried from the stored raw event? Do you want a retry limit or an alert for this? The thread doesn't set either

**Validation:**
- Should About include the 2026-09-15 figures (`37 duplicate labels`, €15.54 and `12 orders` sent a day late), or stick to the fix?
- Am I likely to misread anything in the five points?
```

Export-equivalent path: `export/001 - task-label-webhook-fix-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Quality: this is a clarification, not the task. It asks one set of questions and doesn't draft anything or answer its own questions.

I'm asking before drafting because `$t` always needs these answers first. I already have the five scope points, the values from the thread and the API notes, the rejected polling-only option, Joris as owner and the `BE - SHIP` title format from the context file. The questions only cover what those sources leave open or leave for you to decide:

- **Other error codes:** the thread only covers `SERVICE_UNAVAILABLE`.
- **30-minute alert:** it would also catch shipments waiting on an address fix.
- **Open shipment:** the thread doesn't define it.
- **Unconfirmed carrier behaviour:** the carrier still has to confirm a point that affects the guard.
- **Queue failures:** nothing says how they're retried.

I'll draft the task as soon as you answer.