# FE - Web - TRACK - Order page tracking timeline

### About

---

The web order page shows `Order placed` until dispatch and `Shipped` after it, then never changes. Customers who want more go to the carrier's site or contact CS. This task replaces that with a status timeline for each parcel that updates as the parcel moves, plus the delivery day when the carrier sends one. The web layout is in the same frame as the apps.

**Story**

---

- [Customer - Order tracking - Order page timeline](<002 - Story-order-tracking.md>)

**Related tasks**

---

- [BE - TRACK - Carrier tracking webhook and status mapping](<002.4 - task-carrier-tracking-webhook.md>)
- [FE - iOS - TRACK - Order page tracking timeline](<002.1 - task-ios-order-tracking-timeline.md>)
- [FE - Android - TRACK - Order page tracking timeline](<002.2 - task-android-order-tracking-timeline.md>)

### Requirements

---

1.  **Status timeline**

---

Each parcel gets a timeline that tells the customer where it is, using the statuses the tracking webhook provides.

**Checklist**

- [ ] The layout follows the web layout in the `Order page / Tracking timeline` frame, on desktop and mobile browsers
- [ ] An order with several parcels shows one timeline per parcel, with that parcel's items under it
- [ ] The timeline uses the statuses `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered` and `Delivery failed`
- [ ] Every step that happened shows with its date and time
- [ ] `Delivery failed` shows no reason
- [ ] After a failed delivery and a new attempt, the parcel shows `Out for delivery` again and keeps `Delivery failed` in its history
- [ ] Status text is translated for all six locales

2.  **Delivery estimate**

---

The customer sees the delivery day only when the carrier sends one.

**Checklist**

- [ ] With an `eta_window`, the current status shows `Arriving Thursday 1 October` and `Between 10:00 and 14:00`, following the mock
- [ ] The estimate follows the newest `eta_window` the back end provides
- [ ] With no `eta_window`, no estimate shows, and none is worked out from the dispatch date
- [ ] The time zone of the window follows the decision on the Story's open question

3.  **Pallet items and older orders**

---

Orders that have no tracking events still show a clear status.

**Checklist**

- [ ] Pallet items keep today's order page plus the line `The delivery company will call you to book a delivery slot`
- [ ] A parcel delivered more than `90 days` ago shows its last status only
