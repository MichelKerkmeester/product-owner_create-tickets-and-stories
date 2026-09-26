# FE - Guest app - BOOK - Android confirmation total leaves out city tax on stays of 2 nights or more

### About

---

On Android 8.12.1, the confirmation screen after a Pay now stay of 2 nights or more leaves city tax out of the total, and guests write in to Guest Support about what looks like an overcharge.

| Field           | Value                                                                 |
| --------------- | --------------------------------------------------------------------- |
| Frequency       | Always (Pay now stays of 2 nights or more, per Guest Support. Seen on the guest's phone and reproduced on the test phone) |
| Severity        | High                                                                  |
| Platform        | Android, Guest app 8.12.1, app language en-GB                         |
| Device          | Guest's phone: Not provided. Test phone: model not provided |
| OS Version      | Guest's phone: Not provided. Test phone: Android 14 |
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

The confirmation screen total is the room price only, without the city tax that was shown and charged
- On `RS-7Q4K2M` the guest saw `Total €387.00` and was charged €405.00, a gap of €18.00
- No error message is shown
- The confirmation email says `Total €405.00`, and back office shows one €405.00 Pay now charge, captured on 2026-09-20, the only one on the card
- On the Guest Support test phone, a 2-night stay showed `City tax` and €270.00 at payment, then `Total €258.00`, and charged €270.00
- A 1-night stay there showed `Total €135.00`, the charge of €129.00 plus €6.00 city tax
- The same 3-night booking on iOS 8.12.0 shows `Total €405.00`
- Web showed the right total for a 3-night Pay now booking on 2026-09-25
- Guest Support found 14 chats tagged `price-mismatch` from the 2026-09-16 release to 2026-09-21, none from iOS or web
- All 14 were Android 8.12.1 Pay now stays of 2 nights or more
- The staged rollout reached every Android user on 2026-09-21, so the number of affected guests can grow from here

Back office breakdown for `RS-7Q4K2M`:

| Line | Amount |
| ---- | ------ |
| Room, 3 nights at €129.00 | €387.00 |
| City tax, €3.00 per adult per night, 2 adults, 3 nights | €18.00 |
| Total | €405.00 |

Not known yet:
- Whether Pay at property bookings show the gap, since those guests pay on arrival and none has written in
- The cause, since the Booking squad has not looked at the code
- Whether Android 8.11.2 was correct, since the chat search started at the 8.12.1 release

Steps to Reproduce:
1. On Android 8.12.1, search property 40217 for 2 adults, 1 room, 2 nights
2. Pick a Pay now rate plan and continue to payment
3. The breakdown shows the `City tax` line and €270.00, as expected
4. Tap Pay now with a test card
5. Confirmation shows `Total €258.00` (without the €12.00 city tax), expected `Total €270.00` (the charge)
6. Cancel the test booking under Trips before the free cancellation deadline

Screenshot: the guest's confirmation screen showing `Total €387.00`, on ticket 58213 in the support desk tool

Screen recording: Not provided

---

**2. Expected Behavior**

---

For every stay length, the confirmation total equals the charge, city tax included
- Design spec: Not provided
- Previous working behavior: Not provided for Android, while iOS 8.12.0, web and the confirmation email show the full total
- Product rule: city tax is part of the total, and Pay now charges the full total
- User expectation: the confirmation total is the amount that leaves the guest's card

Checklist
- [ ] Root cause identified
- [ ] Fix implemented
- [ ] Bug no longer reproducible
- [ ] No regressions introduced

---

### BDD Scenarios

---

**Scenario:** Confirmation total includes city tax on a multi-night Pay now stay
- **Given** a guest on Android books 2 nights for 2 adults at a property charging €3.00 city tax per adult per night
- **When** they pay with Pay now
- **Then** the confirmation total matches the payment step and the card charge

**Scenario:** 1-night stays keep showing the right total
- **Given** a guest on Android books 1 night for 2 adults at the same property
- **When** they pay with Pay now
- **Then** the confirmation shows `Total €135.00`, the room price plus €6.00 city tax
