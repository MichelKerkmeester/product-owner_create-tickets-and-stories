# FE - Guest app - BOOK - Android confirmation screen total leaves out city tax on stays of 2 nights or more

### About

---

On Android 8.12.1, the confirmation screen after a Pay now booking of 2 nights or more shows a total without the city tax. The total the guest sees is lower than the charge on their card, so guests read the difference as an overcharge and contact Guest Support. The Android rollout reached all users on 2026-09-21.

| Field           | Value                                                                 |
| --------------- | --------------------------------------------------------------------- |
| Frequency       | Always, on Pay now stays of 2 nights or more (guest's phone and the Guest Support test phone, per Guest Support) |
| Severity        | High                                                                  |
| Platform        | Android                                                               |
| Device          | Guest's phone: not known. Guest Support Android test phone: model not provided |
| OS Version      | Guest's phone: not known. Guest Support test phone: Android 14. Guest app Android 8.12.1 on both |
| Browser         | Not applicable, native app                                            |
| Browser Version | Not applicable, native app                                            |

**References:**

**Support ticket**
- Guest Support ticket 58213, escalated to the Booking squad by Maren (Guest Support, Tier 2) on 2026-09-21
- Booking RS-7Q4K2M at property 40217, booked on 2026-09-20 with Pay now

**Related bugs**
- None open

---

### Bug

---

**1. Observed Behavior**

---

After a Pay now booking on Android 8.12.1 with a stay of 2 nights or more, the confirmation screen total is the room price only and leaves out the city tax
- Booking RS-7Q4K2M (3 nights, 2 adults, 1 room): the confirmation screen showed Total €387.00 and the card was charged €405.00
- The €18.00 difference is the property's city tax of €3.00 per adult per night, for 2 adults over 3 nights
- The charge is correct. Back office shows one Pay now charge of €405.00, captured on 2026-09-20, and the confirmation email for the same booking says Total €405.00
- The payment step before the confirmation screen shows the correct total. In Guest Support's 2-night test it showed the City tax line and €270.00
- 1-night stays show the correct total. Guest Support's 1-night test showed Total €135.00, which is €129.00 plus €6.00 city tax
- The same 3-night booking on iOS 8.12.0 shows Total €405.00 on the confirmation screen
- Web shows the correct total. A 3-night Pay now booking on web on 2026-09-25 showed the right total on the confirmation screen
- Error message: none reported in the ticket
- Guest Support found 14 chats tagged price-mismatch since the 2026-09-16 release, all from Android 8.12.1 and all Pay now bookings of 2 nights or more. None came from iOS or web
- Pay at property bookings: not known whether the confirmation screen shows the same gap. Those guests are charged at the property, and no guest has written in about one yet

Steps to Reproduce:
1. On an Android phone with Guest app 8.12.1, open property 40217
2. Choose a 2-night stay for 2 adults with Pay now
3. At the payment step, check the price breakdown. It shows the City tax line and a total of €270.00
4. Pay now with a test card
5. On the confirmation screen, check the total. Expected: Total €270.00. Actual: Total €258.00, the room price without the €12.00 city tax

Screen recording: Not provided. The guest's screenshot of the Android confirmation screen showing Total €387.00 is kept on ticket 58213 in the support desk tool.

Back office breakdown for RS-7Q4K2M:

| Line | Amount |
|------|--------|
| Room, 3 nights at €129.00 | €387.00 |
| City tax, €3.00 per adult per night, 2 adults, 3 nights | €18.00 |
| Total | €405.00 |

---

**2. Expected Behavior**

---

For every stay length, the confirmation screen total equals the amount the guest is charged, with city tax included
- Product rule: city tax is part of the total, and Pay now charges the full total with city tax included
- The confirmation screen total matches the payment step total and the confirmation email total for the same booking
- Previous working behavior: iOS 8.12.0, web and 1-night stays on Android 8.12.1 already show the full total. Android behavior before 8.12.1 is not provided
- User expectation: the confirmation screen shows the same amount the guest later sees on their card

Checklist
- [ ] Root cause identified
- [ ] Fix implemented
- [ ] Bug no longer reproducible
- [ ] No regressions introduced

---

### BDD Scenarios

---

**Scenario:** Confirmation total includes city tax on a multi-night Pay now stay
- **Given** a guest on Android books property 40217 for 2 nights and 2 adults with Pay now, and the payment step shows a total of €270.00 with the City tax line
- **When** the booking confirms and the confirmation screen opens
- **Then** the confirmation screen shows Total €270.00, the same amount as the card charge and the confirmation email
