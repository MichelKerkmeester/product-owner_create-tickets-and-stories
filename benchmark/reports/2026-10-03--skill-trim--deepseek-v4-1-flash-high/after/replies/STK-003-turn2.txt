Path: `export/002 - task-label-webhook-fix.md`
Verified: read-back succeeded; 126 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the backticked carrier and thread values (`event_id`, `X-Carrier-Signature`, `HMAC-SHA256`, `5 seconds`, `7 days`, `10 minutes`, `30 minutes`, `#fulfilment-alerts`, `more than 5`) and the `{shipment_id}` path placeholder quoted from the carrier notes, which are literal identifiers, a channel and supplied numbers.

**Quality:** Task Mode, title `BE - SHIP - Label webhook duplicates and missing labels` with no surface segment because no single surface owns the back-end work. `## About`, `**References**` and `### Requirements` are present, with a checklisted group for each of the five points, a Done group and an Out of scope group. The format gate passes and the Human Voice linter reports zero hard violations. `context/` is unchanged and the turn-1 clarification file was left untouched.

The task is saved for Joris on the Fulfilment board with no parent. It keeps every carrier value (`event_id`, `X-Carrier-Signature`, `HMAC-SHA256`, `5 seconds`, `5 attempts` at `1 min, 5 min, 15 min, 1 h, 6 h`) and every thread value (`7 days`, `10 minutes`, `30 minutes`, `#fulfilment-alerts`, `more than 5`) unchanged, keeps polling only out as `rejected`, states that the carrier has no idempotency key so the open-shipment guard is ours, and carries the three carrier questions as still open.

**Additions I made that neither the thread nor the notes state, so you can strike them:**
- A duplicate `event_id` still gets `2xx`, and an event whose work fails is not marked processed
- An event that cannot be stored gets a non-`2xx` so the carrier sends it again
- Open means `label_pending` or `label_ready`, and the guard covers every shipment creation for a parcel, the wider reading your "one shipment per parcel" done condition needs
- Two failure events for one parcel that arrive together create at most one shipment
- A label from the `10 minutes` GET is copied into our own storage like a webhook label, and the GET shares `20 requests per second` and waits out a `429`
- Whichever of the webhook and the GET delivers the label second changes nothing
- Each alert posts once per shipment with its `reference` and `shipment_id`

**Left open or out on purpose:** what an alert post contains and which on-call rotation is paged, because neither the thread nor your reply settles them. Handling for `ADDRESS_INVALID` and `OTHER` is unchanged, the task says "before the November peak" with no date, and two thread gaps stay as notes for Joris to confirm with Noor: whether a still-pending shipment is read again before the `30 minutes` alert, and whether an `ADDRESS_INVALID` shipment counts toward the alert and page.