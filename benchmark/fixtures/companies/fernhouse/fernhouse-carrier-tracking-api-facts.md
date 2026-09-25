# Parcel carrier tracking API, facts for order tracking

Written by Yusuf, Backend engineer, Fulfilment, on 2026-09-21. Source: the parcel carrier's tracking events guide (version 2.4) and a call with their integration engineer on 2026-09-19, where they confirmed the points marked as confirmed below. The label events are in Joris's label API notes and follow the same delivery rules.

## The event

There is one event type, `tracking.updated`, sent for every scan of a parcel. The carrier posts it to `/webhooks/carrier/tracking` on shipping-service. The label events have their own path, and the two stay separate because the carrier signs each subscription with its own secret.

| Field | Meaning |
|-------|---------|
| `event_id` | Unique per event, and the same on every retry of that event |
| `shipment_id` | The shipment created with `POST /v1/shipments` |
| `tracking_number` | As printed on the label |
| `status_code` | One of the five codes below |
| `occurred_at` | When the scan happened, with its UTC offset |
| `sent_at` | When the carrier sent this delivery |
| `eta_window` | The expected delivery window as `from` and `to`, each with its offset. Can be missing |
| `exception_code` | Only on `EX` |
| `location` | Depot or hub, with city and country |

## Status codes

| Code | Meaning | Notes |
|------|---------|-------|
| `PU` | Picked up at our warehouse | Once per parcel, at the 18:00 collection |
| `IT` | In transit | One per hub scan. Usually 2 to 4 per parcel, more for the UK |
| `OD` | Out for delivery | Always carries `eta_window`. Can come again after an `EX` |
| `DL` | Delivered | Carries `delivered_to`: `recipient`, `neighbour` or `parcel_point` |
| `EX` | Exception | Carries `exception_code`: `NOT_HOME`, `ADDRESS_PROBLEM`, `DAMAGED` or `REFUSED` |

After an `EX` with `NOT_HOME` the carrier tries again the next working day, which sends a new `OD`. After a second `NOT_HOME` the parcel goes to a parcel point, and a `DL` with `delivered_to` set to `parcel_point` comes when the parcel is dropped there, not when the customer collects it. Confirmed on the call.

## Order of events

Events can arrive `out of order`. Hub scans upload in batches, so an `IT` can reach us after the `OD` for the same parcel, on busy days by more than an hour. Retries make it worse, since a retried event arrives late by design. Order by `occurred_at`, never by arrival. An event whose `occurred_at` is older than the newest one we hold for that parcel is stored for the history and does not change the status shown. Confirmed on the call.

`eta_window` can change between events, and the newest window by `occurred_at` wins. An `OD` always has one. An `IT` has one only when the carrier can predict the day, which is mostly inside the Netherlands and Belgium.

## Delivery and signature

The same rules as the label webhooks:

- Signed with `X-Carrier-Signature`, the hex HMAC-SHA256 of the raw body, keyed with the tracking subscription's own secret
- The carrier waits 5 seconds for a 2xx, and anything else counts as a failed delivery
- After a failed delivery it makes up to `5 attempts` more, waiting `1 min, 5 min, 15 min, 1 h, 6 h` before each one, then drops the event
- Delivery is at least once, so dedupe on `event_id`

A dropped tracking event is gone for good. `GET /v1/shipments/{shipment_id}` returns label fields only, and tracking history is not part of our plan with the carrier. A missed `DL` would leave the order on its last status.

## Volume

About 3,100 parcels leave on a normal working day, and up to 5,400 on the busiest days so far this year. Each parcel produces 5 to 8 events, so a peak day means up to about 43,000 events.

## Example body

```json
{
  "event_id": "evt_01J8V6R2KX9D",
  "type": "tracking.updated",
  "shipment_id": "shp_7731902",
  "tracking_number": "TRK4471-1182-06",
  "status_code": "OD",
  "occurred_at": "2026-09-21T07:42:10+02:00",
  "sent_at": "2026-09-21T07:42:31+02:00",
  "eta_window": {
    "from": "2026-09-21T10:00:00+02:00",
    "to": "2026-09-21T14:00:00+02:00"
  },
  "location": "Depot 14, Utrecht, NL"
}
```

## Not covered here

- The pallet carrier has no tracking API at all
- Which status the customer sees for each code is in Hamid's brief
