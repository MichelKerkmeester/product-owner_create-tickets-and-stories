`export/002 - task-carrier-label-webhook-fix.md`

Verified: read-back succeeded; 117 lines

HVR self-scan: 0 hard blockers. Fixed: one comma spliced before "and" in the signature check. Kept with reason: none.

Quality summary
- Structure: canonical single task, no parent. `## About` at H2, `### Requirements` at H3, six numbered groups under four categories, `---` dividers throughout, `- []` checklists only
- Title: `BE - SHIP - Label webhook acknowledgement, dedupe and shipment guard`, per the Fernhouse `{Discipline} - {Feature code} - {Title}` convention with the surface dropped for back-end work
- Scope: the five thread points, your staging done conditions, the warehouse call moved to the queue with its `8-second` timeout kept, polling only excluded
- Values: `5 seconds`, `event_id`, `7 days`, `10 minutes`, `30 minutes`, `5`, `#fulfilment-alerts`, `SERVICE_UNAVAILABLE`, `ADDRESS_INVALID`, `OTHER`, `X-Carrier-Signature`, `401`, `POST /v1/shipments`, `GET /v1/shipments/{shipment_id}`, `label_url`, `tracking_number`, `label_pending`, `24 hours` all carried as the sources write them
- Size: ~600 words, inside the 900 budget. All six quality floors clear

One standpoint task for Joris on the Fulfilment board, live before the November peak: the handler answers the carrier inside `5 seconds` from a queue, one shipment and one label per parcel, the 10-minute GET catches stragglers and the 30-minute alert catches the rest.

Additions worth striking if you disagree: the alert names each stuck shipment's `reference` and `shipment_id`; a failed shipment left `label_pending` waits for the next check; and the guard permits a re-create only for `SERVICE_UNAVAILABLE`, never for `ADDRESS_INVALID` or `OTHER`. The staging replay checks are drawn straight from your done conditions plus the timeout point.