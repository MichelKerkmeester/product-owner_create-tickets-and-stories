# Label webhook thread from #fulfilment-eng

Exported from the #fulfilment-eng channel on 2026-09-16 by Noor, Engineering lead, Fulfilment, to attach to the label webhook ticket. Times are Amsterdam time. Reactions and two off-topic messages are removed, nothing else is edited.

---

**Wouter, Warehouse operations lead** 08:47

Morning all. Yesterday, 2026-09-15, the pack stations printed `37 duplicate labels` between 14:10 and 15:50. Same order, same parcel, two labels and sometimes three. The team caught most of them at packing, but the carrier bills every one.

**Wouter, Warehouse operations lead** 08:49

Second thing, and the worse one. `12 orders` paid before the `15:00` cut-off had no label when the 18:00 collection came, so they went out a day late. CS has sent those customers an apology.

**Femke, Finance, carrier invoices** 09:05

For the record, a label costs us `€0.42`, so the duplicates come to €15.54. Small money, but the carrier invoice gets checked line by line and I would rather not explain it every month.

**Joris, Backend engineer, Fulfilment** 09:31

Had a look at the logs. From 14:05 to 15:50 the label webhook handler took 6 to 9 seconds per event. For both event types it calls the warehouse system before answering, and the warehouse system was slow all afternoon. The carrier stops waiting after 5 seconds and retries, so most events in that window came in more than once, and we did the work every time.

For `label.failed` with `SERVICE_UNAVAILABLE` the handler creates the shipment again. Every retry of the same failed event created one more shipment, and that is where the 37 duplicates come from. Nothing in the handler looks at `event_id`.

**Joris, Backend engineer, Fulfilment** 09:34

The 12 late orders are the calls that hit our own 8-second timeout on the warehouse system. The handler answered 500 and saved nothing. Their `label.created` events failed on the first try and on the first four retries, all inside the slow window. The fifth retry comes 6 h after the fourth, so those labels only landed after 21:00.

**Noor, Engineering lead, Fulfilment** 09:52

Thanks. Proposal for the ticket, shout if you disagree:

1. Answer fast. Check the signature, store the raw event, return 200 and do the work from a queue. Nothing slow inside the request
2. Dedupe on `event_id`. Keep processed ids for `7 days`, well past the carrier's last retry
3. Before creating a shipment again after a failure, check that the parcel has no other open shipment. The carrier has no idempotency key, so this guard has to be ours
4. A shipment with no label `10 minutes` after the POST gets a GET, and we take the label from there when it is ready
5. A shipment with no label after `30 minutes` posts to `#fulfilment-alerts`, and on-call gets paged when `more than 5` are in that state at once

**Yusuf, Backend engineer, Fulfilment** 10:08

Playing devil's advocate: why keep the webhook at all? We could go polling only and GET every pending shipment every few seconds. No signatures, no retries to reason about.

**Joris, Backend engineer, Fulfilment** 10:15

The rate limit kills it. We get 20 requests per second for the whole account and the POSTs share it. Around the cut-off we POST up to 14 a second, which leaves 6 a second for polling while several hundred labels are pending. Labels would arrive later than they do now, in the busiest hour of the day.

**Wouter, Warehouse operations lead** 10:17

Please not later. The pack stations already wait on labels at 15:00.

**Noor, Engineering lead, Fulfilment** 10:24

Agreed. `polling only` is `rejected` because of the rate limit. The 10-minute GET in point 4 stays, since it only touches stragglers.

**Noor, Engineering lead, Fulfilment** 10:31

Summary for the ticket:

- Keep the webhook, answer inside the carrier's 5 seconds and process from a queue
- Dedupe on `event_id`, processed ids kept for 7 days
- Guard against a second open shipment for the same parcel
- GET after 10 minutes without a label, alert in `#fulfilment-alerts` after 30 minutes, page on-call when more than 5 are stuck
- Polling only: rejected, rate limit

Joris takes the BE task. Wouter, can the pack stations post here whenever a duplicate slips through until this ships?

**Wouter, Warehouse operations lead** 10:33

Yes, I will ask the shift leads to post it here.
