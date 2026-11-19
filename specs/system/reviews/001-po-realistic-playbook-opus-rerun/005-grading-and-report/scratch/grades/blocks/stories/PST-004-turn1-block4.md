# FE - Web - TRACK - Order page tracking timeline

### About

---

The web order page replaces its fixed `Order placed` and `Shipped` states with a timeline that follows each parcel, plus the delivery estimate when the carrier sends one. Design has mocked the timeline for the apps only, and this task needs the web layout from design before the build starts.

**References**

---

Page

- `Order page / Tracking timeline`

**Story**

---

- [Customer - Order tracking - Order page timeline](<NNN - Story-order-tracking-timeline.md>)

**Related tasks**

---

- [BE - TRACK - Tracking webhook](<NNN.1 - task-tracking-webhook.md>)
- [DATA - TRACK - Tracking timeline events](<NNN.6 - task-tracking-timeline-events.md>)

### Requirements

---

1.  **Tracking timeline**

---

**Checklist**

- [ ] The order page shows `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered` and `Delivery failed` in that order, as each is reached
- [ ] Every step that happened shows with its date and time
- [ ] A new `Out for delivery` after `Delivery failed` keeps the failed attempt visible
- [ ] An order with several parcels shows one timeline per parcel, with that parcel's items under it
- [ ] More than `90 days` after delivery the page shows the last status only
- [ ] Status text is translated for `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR` and `en-GB`

---

2.  **Delivery estimate**

---

**Checklist**

- [ ] With a delivery window, the day and window show under the current status, as in the frame: `Arriving Thursday 1 October` and `Between 10:00 and 14:00`
- [ ] With no delivery window, no estimate shows, and none is derived from the dispatch date

---

3.  **Pallet items**

---

**Checklist**

- [ ] A shipment by the pallet carrier keeps today's page plus the line `The delivery company will call you to book a delivery slot`

---

4.  **Analytics**

---

**Checklist**

- [ ] The page sends the timeline viewed and carrier link tapped events once their tracking plan rows exist
