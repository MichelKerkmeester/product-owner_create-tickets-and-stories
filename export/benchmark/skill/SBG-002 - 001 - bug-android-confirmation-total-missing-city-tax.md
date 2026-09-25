# FE - Guest app - BOOK - Android confirmation total leaves out city tax on stays of 2 nights or more

### About

---

On Android 8.12.1, the Guest app confirmation screen shows a total without city tax after a Pay now booking of 2 nights or more, so the total is lower than the amount charged to the guest's card. Guests read the difference as an overcharge and write in to Guest Support.

| Field           | Value                                                                 |
| --------------- | --------------------------------------------------------------------- |
| Frequency       | Always (Pay now stays of 2 nights or more, per Guest Support escalation. Seen on the guest's phone and reproduced on the Guest Support test phone) |
| Severity        | High                                                                  |
| Platform        | Android, Guest app 8.12.1, app language en-GB                         |
| Device          | Guest's phone: Not provided. Guest Support test phone: model not provided |
| OS Version      | Guest's phone: Not provided. Guest Support test phone: Android 14     |
| Browser         | Not applicable (native app)                                           |
| Browser Version | Not applicable (native app)                                           |

**References:**

**Support ticket**
- Guest Support ticket 58213, escalated to the Booking squad by Maren (Tier 2) on 2026-09-21
- Booking reference `RS-7Q4K2M`, property 40217, booked on 2026-09-20 with Pay now

**Related bugs**
- None open

**Flows**
- Not provided

**Components**
- Not provided

---

### Bug

---

**1. Observed Behavior**

---

After Pay now on a stay of 2 nights or more, the confirmation screen shows the room price as the total and leaves out the city tax that the payment step showed and the card was charged for
- The guest on booking `RS-7Q4K2M` saw `Total €387.00` on the confirmation screen and was charged €405.00, a gap of €18.00
- No error message is shown. The screen looks like a normal confirmation with a lower total
- The confirmation email for the same booking says `Total €405.00`, which matches the charge
- Back office shows one Pay now charge of €405.00, captured on 2026-09-20, and it is the only charge on the card
- On the Guest Support test phone, a 2-night stay showed the `City tax` line and €270.00 at the payment step, then `Total €258.00` on the confirmation screen. Back office has the charge at €270.00
- A 1-night stay on the same test phone showed `Total €135.00`, which matches the charge of €129.00 plus €6.00 city tax
- The same 3-night booking on the iOS test phone, app 8.12.0, shows `Total €405.00`
- A 3-night Pay now booking on the web Guest app, checked on 2026-09-25, showed the right total on the confirmation screen
- Guest Support found 14 chats tagged `price-mismatch` between the release on 2026-09-16 and 2026-09-21. All 14 came from Android 8.12.1 and all were Pay now bookings of 2 nights or more. None came from iOS or web
- The Android staged rollout reached every user on 2026-09-21, so the number of affected guests can grow from here

Back office breakdown for `RS-7Q4K2M`:

| Line | Amount |
| ---- | ------ |
| Room, 3 nights at €129.00 | €387.00 |
| City tax, €3.00 per adult per night, 2 adults, 3 nights | €18.00 |
| Total | €405.00 |

Not known yet:
- Whether Pay at property bookings show the same lower total. Those guests are not charged until arrival, and no guest has written in about one
- The cause. Nobody on the Booking squad has looked at the code yet
- Whether Android 8.11.2 showed the right total. The chat search started at the 8.12.1 release

Steps to Reproduce:
1. On an Android phone with Guest app 8.12.1, search for property 40217 for 2 adults, 1 room, 2 nights
2. Pick a rate plan with Pay now and continue to the payment step
3. Check the price breakdown. Expected and actual: the `City tax` line is shown and the total is €270.00
4. Tap Pay now with a test card
5. Check the total on the confirmation screen. Expected: `Total €270.00`, the amount charged. Actual: `Total €258.00`, the room price without the €12.00 city tax
6. Cancel the test booking under Trips before the free cancellation deadline

Screenshot: the guest's Android confirmation screen showing `Total €387.00`, kept on ticket 58213 in the support desk tool

Screen recording: Not provided

---

**2. Expected Behavior**

---

The confirmation screen total equals the amount charged for the booking, city tax included, on every stay length
- Design spec: Not provided
- Previous working behavior: Not provided for Android. The iOS 8.12.0 app, the web Guest app and the confirmation email all show the full total with city tax
- Product rule: city tax is part of the total, and Pay now charges the full total with city tax included
- User expectation: the total on the confirmation screen is the amount that leaves the guest's card, so a guest never sees a lower number than their bank shows

Checklist
- [ ] Root cause identified
- [ ] Fix implemented
- [ ] Bug no longer reproducible
- [ ] No regressions introduced

---

### BDD Scenarios

---

**Scenario:** Confirmation total includes city tax on a multi-night Pay now stay
- **Given** a guest on Android books a 2-night stay for 2 adults at a property that charges €3.00 city tax per adult per night
- **When** the guest pays with Pay now and the confirmation screen opens
- **Then** the confirmation screen shows the same total as the payment step and the card charge, city tax included

**Scenario:** 1-night stays keep showing the right total
- **Given** a guest on Android books a 1-night stay for 2 adults at the same property
- **When** the guest pays with Pay now and the confirmation screen opens
- **Then** the confirmation screen shows `Total €135.00`, the room price plus €6.00 city tax
