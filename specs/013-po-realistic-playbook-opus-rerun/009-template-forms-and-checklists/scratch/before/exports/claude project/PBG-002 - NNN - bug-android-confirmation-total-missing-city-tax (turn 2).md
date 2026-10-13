# FE - Guest app - BOOK - Android confirmation screen total leaves out city tax on stays of 2 nights or more

### About

---

On Android 8.12.1, the confirmation screen after a Pay now stay of 2 nights or more leaves city tax out of the total, and guests contact Guest Support about what looks like an overcharge. The Android rollout reached all users on 2026-09-21.

| Field           | Value                                                                 |
| --------------- | --------------------------------------------------------------------- |
| Frequency       | Always, on Pay now stays of 2 nights or more (guest's phone and Guest Support test phone) |
| Severity        | High                                                                  |
| Platform        | Android                                                               |
| Device          | Guest's phone: not known. Guest Support test phone: model not provided |
| OS Version      | Guest's phone: not known. Test phone: Android 14. Guest app Android 8.12.1 on both |
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

The confirmation screen total is the room price only, without city tax
- Booking RS-7Q4K2M (3 nights, 2 adults, 1 room): the screen showed Total €387.00 and the card was charged €405.00, an €18.00 city tax gap
- Back office shows one €405.00 Pay now charge captured on 2026-09-20, and the confirmation email says Total €405.00
- Guest Support's 2-night test showed the City tax line and €270.00 at the payment step
- A 1-night test showed Total €135.00, €129.00 plus €6.00 city tax
- iOS 8.12.0 shows Total €405.00 for the same booking
- A 3-night Pay now web booking showed the full total on 2026-09-25
- Error message: none in the ticket
- 14 chats tagged price-mismatch since the 2026-09-16 release were all Android 8.12.1 Pay now stays of 2 nights or more
- None came from iOS or web
- Pay at property: not known whether the screen shows the same gap
- Those guests pay at the property, and none has written in

Steps to Reproduce:
1. On Android 8.12.1, open property 40217
2. Choose a 2-night stay for 2 adults with Pay now
3. At the payment step, the breakdown shows the City tax line and €270.00
4. Pay now with a test card
5. On the confirmation screen, expected Total €270.00, actual Total €258.00, without the €12.00 city tax

Screen recording: Not provided. The guest's screenshot showing Total €387.00 is on ticket 58213 in the support desk tool.

Back office breakdown for RS-7Q4K2M:

| Line | Amount |
|------|--------|
| Room, 3 nights at €129.00 | €387.00 |
| City tax, €3.00 per adult per night, 2 adults, 3 nights | €18.00 |
| Total | €405.00 |

---

**2. Expected Behavior**

---

For every stay length, the confirmation total equals the charge, city tax included
- Product rule: city tax is part of the total, and Pay now charges the full total
- It matches the payment step and confirmation email for the same booking
- Previous working behavior: iOS 8.12.0, web and Android 8.12.1 1-night stays show the full total, and Android before 8.12.1 is not provided
- User expectation: the screen shows the amount later on the guest's card

Checklist
- [ ] Root cause identified
- [ ] Fix implemented
- [ ] Bug no longer reproducible
- [ ] No regressions introduced

---

### BDD Scenarios

---

**Scenario:** Confirmation total includes city tax on a multi-night Pay now stay
- **Given** a guest on Android books property 40217 for 2 nights, 2 adults, Pay now, and the payment step shows €270.00 with City tax
- **When** the confirmation screen opens
- **Then** it shows Total €270.00, matching the card charge and confirmation email
