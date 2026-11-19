# FE - Android - TRACK - Tracking timeline on the order page

### About

---

The order page in the Android app shows `Order placed` until dispatch and `Shipped` after it, and never changes after that. This task replaces that with a status timeline that moves as the parcel moves. It adds the expected delivery day when the carrier sends one, so customers no longer need the carrier's own site or a CS contact to know when their parcel arrives.

The tracking data comes from the BE tracking webhook task. The layout is in the `Order page / Tracking timeline` frame.

**Story**

---

- [Customer - Order page - Order tracking](<002 - Story-order-tracking.md>)

**Related tasks**

---

- [FE - iOS - TRACK - Tracking timeline on the order page](<002.1 - task-ios-tracking-timeline.md>)
- [FE - Web - TRACK - Tracking timeline on the order page](<002.3 - task-web-tracking-timeline.md>)
- [BE - TRACK - Tracking webhook](<002.4 - task-tracking-webhook.md>)

### Requirements

---

1.  **Status timeline**

---

The timeline shows each status the parcel has reached, so the customer can see where it is and what happened before.

**Checklist**

- [ ] Statuses show in this order: `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered`, `Delivery failed`
- [ ] Every step that happened shows with its date and time
- [ ] `Delivery failed` shows no reason
- [ ] After `Delivery failed`, a new delivery attempt shows as `Out for delivery` again, and the failed step stays in the timeline
- [ ] Layout matches the app design in the `Order page / Tracking timeline` frame
- [ ] Status text is translated for `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR` and `en-GB`

2.  **Delivery estimate**

---

The estimate shows only when the carrier has sent a delivery window, so the page never shows a day the carrier did not give.

**Checklist**

- [ ] The day and window show under the current status, as in the frame: `Arriving Thursday 1 October` and `Between 10:00 and 14:00`
- [ ] With no window from the carrier, no estimate shows
- [ ] A newer window replaces the one shown before

3.  **Parcels, pallet items and older orders**

---

Orders that do not fit a single tracked parcel still show something true.

**Checklist**

- [ ] An order with several parcels shows one timeline per parcel, with that parcel's items under it
- [ ] Items over `30 kg` or `120 cm` keep today's page plus the line `The delivery company will call you to book a delivery slot`
- [ ] More than `90 days` after delivery, the page shows the last status only
