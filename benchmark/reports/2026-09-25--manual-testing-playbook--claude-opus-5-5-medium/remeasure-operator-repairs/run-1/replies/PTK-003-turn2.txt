```markdown
# BE - SHIP - Label webhook answers inside the carrier timeout

### About

---

On 2026-09-15 the label webhook handler on shipping-service called the warehouse system before answering the carrier, and the warehouse system was slow all afternoon. Each event took 6 to 9 seconds, which is longer than the carrier's 5-second wait. The carrier retried, and the handler repeated the work on every retry. Each retry of a `label.failed` event with `SERVICE_UNAVAILABLE` created one more shipment, so the pack stations printed 37 duplicate labels, billed at €0.42 each. Events that hit our own 8-second timeout on the warehouse system got a `500` and were never saved. As a result, 12 orders paid before the 15:00 cut-off had no label when the 18:00 collection came, and they shipped a day late.

This task makes the handler answer the carrier inside its wait and moves the work to a queue, so a slow warehouse system can no longer cause retries or lose events. It also adds three safeguards: a dedupe on `event_id`, a check against a second open shipment for the same parcel and a GET for shipments still without a label after 10 minutes, with alerting after 30 minutes. It has to be live before the November peak.

Polling every pending shipment instead of using the webhook is out of scope. The team rejected it because the POSTs share the carrier's 20 requests per second and run at up to 14 a second around the cut-off.

**References**

---

- `Label webhook thread from #fulfilment-eng` (exported by Noor, 2026-09-16)
- `Parcel carrier label API, working notes` (Joris, 2026-09-11)

### Requirements

---

1.  **Answer the carrier inside 5 seconds and process from a queue**

---

The carrier treats a timeout, a `4xx` or a `5xx` as a failed delivery and sends the event again, so nothing slow may run inside the request.

**Checklist**

- [ ] The handler checks `X-Carrier-Signature` against the raw request body and answers `401` when it does not match
- [ ] A valid event is stored as received and answered with `200` within the carrier's `5 seconds`, however slow the warehouse system is
- [ ] The warehouse system call and all other processing run from the queue, for both `label.created` and `label.failed`
- [ ] The warehouse system call keeps its `8-second` timeout
- [ ] When a queued event's warehouse system call times out, the event is retried from the queue and never dropped

---

2.  **Process each event once**

---

The carrier delivers each event at least once and keeps the same `event_id` on every retry of that event. A repeat has to be recognised before it does any work.

**Checklist**

- [ ] An event whose `event_id` was already processed creates no shipment and repeats no work
- [ ] Processed `event_id` values are kept for `7 days`, well past the carrier's last retry at 7 hours 21 minutes after the first try

---

3.  **Never open a second shipment for a parcel**

---

The carrier has no idempotency key and does not dedupe on `reference`, so two POSTs for the same parcel create two labels, and both are billed. The check has to be on our side.

**Checklist**

- [ ] Before creating a shipment again after a failure, shipping-service checks that the parcel (its `reference`, such as `FH-2291834-1`) has no other open shipment, and skips the create when it does
- [ ] A shipment in `label_failed` does not count as open, so the re-create the carrier asks for after `SERVICE_UNAVAILABLE` still goes ahead

> The carrier has not yet confirmed whether a `label.failed` with `SERVICE_UNAVAILABLE` can be followed by a `label.created` for the same shipment. If it can, the re-create would produce a second billed label. The question is open with the carrier's integration engineer.

---

4.  **Fetch the label for stragglers after 10 minutes**

---

The carrier drops an event after its fifth failed retry, but a GET on the shipment still returns the label. The GET only covers shipments that are still waiting after 10 minutes, so it stays well within the rate limit that ruled out polling.

**Checklist**

- [ ] A shipment with no label `10 minutes` after its POST gets a `GET /v1/shipments/{shipment_id}`
- [ ] When the GET returns `label_ready`, shipping-service takes the `tracking_number` and `label_url` from the response and stores the label as it would for a `label.created` event
- [ ] The GETs stay within the shared `20 requests per second` and wait for the `Retry-After` time on a `429`, so they never hold up the POSTs around the cut-off

---

5.  **Alert on shipments still without a label**

---

A shipment that neither the webhook nor the GET has resolved after 30 minutes needs someone to look at it before the 18:00 collection.

**Checklist**

- [ ] A shipment with no label `30 minutes` after its POST gets a post in `#fulfilment-alerts`
- [ ] On-call is paged when `more than 5` shipments are in that state at once

---

6.  **Replay a slow afternoon in staging**

---

The task is done when a replay in staging holds up under the conditions of 2026-09-15.

**Checklist**

- [ ] With the warehouse system taking 6 to 9 seconds per call and carrier events redelivered on each retry, the replay ends with one shipment and one label per parcel
- [ ] A `label.created` that arrives after the 10-minute GET has already taken the label changes nothing
```

Export-equivalent path: `export/002 - task-carrier-label-webhook-fix.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality:** passes the gate. The About section explains why, with the numbers from 2026-09-15. Each of the five points from the thread has testable checks, and the done condition is your staging replay, written as the final group.

**Things I added that you didn't give me.** Strike any you don't want:
- **Queue retry (group 1):** if a queued event's warehouse call times out, it gets retried instead of dropped. Without this, the 12 lost events could happen again, just in the worker instead of the request.
- **`label_failed` doesn't count as open (group 3):** without this rule, the check would block the re-create the carrier asks for after `SERVICE_UNAVAILABLE`.
- **Rate limit on the GETs (group 4):** they stay within the 20 requests per second and wait on a `429`. This comes from Joris's API notes, not from Noor's five points.

**Still not covered.** These were in my first message and weren't answered, so the task doesn't include them:
- What should happen when the 10-minute GET returns `label_failed`?
- Should `#fulfilment-alerts` get one post per stuck shipment, or one post listing them all?
- Which on-call rotation takes the page?
- Does `ADDRESS_INVALID` and `OTHER` handling stay as it is? The task doesn't mention them, so as written it leaves them unchanged.

The blockquote in group 3 keeps the carrier's open question visible so it doesn't get lost.

**Next step:** save the task to the Fulfilment board with Joris as the assignee. ClickUp isn't connected in this session, so I can't push it for you.