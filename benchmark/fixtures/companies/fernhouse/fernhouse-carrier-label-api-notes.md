# Parcel carrier label API, working notes

Written by Joris, Backend engineer, Fulfilment, on 2026-09-11. Source: the parcel carrier's integration guide for labels (version 3.2, sent over as a PDF by their integration team) and a call with their integration engineer the same afternoon. These are my notes for the team. Where they and the guide disagree, the guide wins.

## What shipping-service does with it

When the warehouse system starts picking an order, shipping-service creates one shipment per parcel. The carrier builds the label on its side and tells us by webhook when it is ready or when it failed. The pack station prints the label from our own copy. Every label the carrier creates is billed, including the ones we never print.

## Endpoints

| Call | Use |
|------|-----|
| `POST /v1/shipments` | Create a shipment for one parcel. Answers `201` with a `shipment_id` and `status` set to `label_pending`. The label is not in the response |
| `GET /v1/shipments/{shipment_id}` | Read one shipment: `status` (`label_pending`, `label_ready` or `label_failed`), plus `tracking_number` and `label_url` once the label is ready |

The POST body carries our `reference` (order number and parcel index, such as `FH-2291834-1`), the `service` (`standard`, or `cross_border` for the UK), the recipient address, `weight_grams` and `dimensions_cm`. The carrier refuses a parcel over 30 kg or over 120 cm on the longest side with `422` before any label work starts.

There is no idempotency key on the POST. Sending the same parcel twice creates two shipments and two labels, and both are billed. The carrier does not dedupe on `reference` either. Their engineer said an idempotency header is planned and could not give a date.

## Label webhooks

Both events arrive at `/webhooks/carrier/labels` on shipping-service.

| Event | When | Extra fields |
|-------|------|--------------|
| `label.created` | The label is ready | `tracking_number`, `label_url` |
| `label.failed` | The carrier could not make a label | `error_code`, `error_message` |

Every event has `event_id`, `type`, `shipment_id`, `reference` and `created_at`. The `event_id` is unique per event and stays the same on every retry of that event, so it is the key to dedupe on. Delivery is at least once. The carrier promises no order between events for different shipments.

`error_code` on `label.failed` is one of:

- `ADDRESS_INVALID`: the address failed the carrier's check. A CS agent has to fix it with the customer
- `SERVICE_UNAVAILABLE`: a problem on their side. They ask us to create the shipment again
- `OTHER`: anything else, with the detail in `error_message`

Example `label.created` body, from their test environment:

```json
{
  "event_id": "evt_01J8Q3M7ZK4T",
  "type": "label.created",
  "shipment_id": "shp_7731902",
  "reference": "FH-2291834-1",
  "created_at": "2026-09-11T14:32:08Z",
  "tracking_number": "TRK4471-1182-06",
  "label_url": "signed link, valid for 24 hours"
}
```

## Signature

Each request carries `X-Carrier-Signature`: the hex `HMAC-SHA256` of the raw request body, keyed with our webhook secret. Check it against the raw bytes before parsing the JSON, and answer `401` when it does not match. The secret sits in the secrets store under the shipping-service entry, never in code and never in this page. Their test environment signs with a separate test secret.

## Timeouts and retries

- The carrier waits `5 seconds` for a `2xx`. A timeout, a `4xx` and a `5xx` all count as a failed delivery
- After a failed delivery it makes up to `5 attempts` more, waiting `1 min, 5 min, 15 min, 1 h, 6 h` before each one
- That is 7 hours 21 minutes from the first try to the last. After the fifth failed retry the event is dropped and never sent again
- A dropped label event does not lose the label: `GET /v1/shipments/{shipment_id}` still returns it

## Label links

`label_url` is a signed link that expires `24 hours` after the event. After that, GET the shipment for a fresh one. We copy the label file into our own storage as soon as the event arrives, so the pack stations never depend on the carrier's link.

## Rate limit

`20 requests per second` for our whole account, across POST and GET together. Above that the API answers `429` with a `Retry-After` header in seconds. Webhook deliveries to us do not count against it. Their engineer said a higher limit needs a contract change and is not on offer to us this year.

## Still open with the carrier

- Can a `label.failed` with `SERVICE_UNAVAILABLE` be followed by a `label.created` for the same shipment? Their engineer thought not and promised to check
- Will they resend a dropped event if we ask? The answer so far is no
- Is there a sandbox rate limit lower than production? Not answered yet
