# FE - iOS - TRACK - Order page tracking timeline

## About

---

The iOS order page swaps its fixed `Order placed` and `Shipped` states for a per-parcel timeline and the carrier's delivery estimate when sent.

**References**

---

Page

- `Order page / Tracking timeline`

**Story**

---

- [Customer - Order tracking - Order page timeline](<NNN - Story-order-tracking-timeline.md>)

**Related tasks**

---

- [FE - Android - TRACK - Order page tracking timeline](<NNN.2 - task-android-tracking-timeline.md>)
- [FE - Web - TRACK - Order page tracking timeline](<NNN.3 - task-web-tracking-timeline.md>)
- [BE - TRACK - Tracking webhook](<NNN.4 - task-tracking-webhook.md>)

### Requirements

---

1.  **Tracking timeline**

---

**Checklist**

- [] Statuses show in order as reached: `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered` and `Delivery failed`
- [] Every past step shows its date and time
- [] `Delivery failed` shows no reason
- [] A new `Out for delivery` after `Delivery failed` keeps the failed attempt visible
- [] A multi-parcel order shows one timeline per parcel, with its items
- [] More than `90 days` after delivery, only the last status shows
- [] Status text is translated into `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR` and `en-GB`

---

2.  **Delivery estimate**

---

**Checklist**

- [] A delivery window shows under the current status as `Arriving Thursday 1 October` and `Between 10:00 and 14:00`
- [] With no window, no estimate shows or is derived from the dispatch date

---

3.  **Pallet items**

---

**Checklist**

- [] A pallet carrier shipment keeps today's page plus `The delivery company will call you to book a delivery slot`
