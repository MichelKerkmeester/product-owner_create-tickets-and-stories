# Order tracking on the order page, questions before drafting

I'll write this as a new Story with its tasks in one folder. Hamid's brief settles the role and value, and the carrier notes hold the technical facts. The points below are still open or contradict each other, so please answer them in one reply.

**1. Task split:** The brief lists six tasks. Should the Story use exactly these, in this order, under these titles?

1. `BE - TRACK - Tracking webhook` receives and stores `tracking.updated` events and maps carrier codes to statuses
2. `BE - TRACK - Packed status from the warehouse system` sets `Packed` in orders-service
3. `DATA - TRACK - Tracking timeline events` adds the tracking plan rows. It comes before the FE tasks because the company context requires a DATA task before any FE task sends an event
4. `FE - Web - TRACK - Tracking timeline and delivery estimate`
5. `FE - iOS - TRACK - Tracking timeline and delivery estimate`
6. `FE - Android - TRACK - Tracking timeline and delivery estimate`

**2. Carrier link:** The DATA task tracks taps on "the carrier link", but the brief never puts a carrier link on the order page. Is there one? If so, where does it sit and what does it say? If not, should the DATA task track timeline views only?

**3. Delivered to a parcel point:** After a second `NOT_HOME`, the carrier sends `DL` with `delivered_to` set to `parcel_point` when it drops the parcel at the parcel point. The customer has not collected it yet. Should the page still show `Delivered`, or something else? If something else, what exact copy? Does the `90 days` retention period start at that `DL`?

**4. Delivery failed:** The carrier only retries the next working day after `NOT_HOME`. What should the customer see after `ADDRESS_PROBLEM`, `DAMAGED` or `REFUSED`? On the open question about showing a reason: has Hamid decided, going by Maud's split (yes for not home, no for anything that sounds like our fault)? Or should the Story mark this as an open question on the requirement? An open question adds a Delivery section that repeats it under Rabbit holes.

**5. Missed events:** A dropped event is lost for good, and our carrier plan includes no tracking history. A missed `DL` would leave the parcel on its last status, and the `90 days` period would never start. Should the Story accept this as a known limitation, or require a fallback? If a fallback, who decides what it is?

**6. Web design:** The timeline is mocked for the apps only. Should the Web task follow the app mock and point to the web layout as still to come, or wait until Design delivers the web layout?

**7. Parcel and pallet items in one order:** How should the order page look when an order has both? Parcel timelines for the parcel items, plus today's page and the delivery-slot line for the pallet items?

**8. Guest orders:** Guests have no order history. Should tracking reach guest orders too, for example through a link in the shipping email? Or is it only for signed-in customers?
