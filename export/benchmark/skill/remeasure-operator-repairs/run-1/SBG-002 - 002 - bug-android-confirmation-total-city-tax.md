# FE - Guest app - BOOK - Android confirmation total leaves out city tax on stays of 2 nights or more

### About

---

On Android 8.12.1, the confirmation screen shows a total without city tax for Pay now stays of 2 nights or more. The card is charged the correct amount with city tax, so guests see a total lower than their charge and contact Guest Support to report an overcharge.

| Field           | Value                                     |
| --------------- | ----------------------------------------- |
| Frequency       | Always (every Pay now stay of 2 nights or more, per Guest Support escalation, reproduced on the guest's phone and the Guest Support test phone) |
| Severity        | High                                      |
| Platform        | Android, app 8.12.1                       |
| Device          | Not provided                              |
| OS Version      | Android 14 on the Guest Support test phone. Guest's phone not provided |
| Browser         | Not applicable                            |
| Browser Version | Not applicable                            |

**References:**

**Support ticket**
- Guest Support ticket 58213, escalated to the Booking squad by Maren (Tier 2) on 2026-09-21, booking RS-7Q4K2M, property 40217
- Guest's screenshot of the confirmation screen showing Total €387.00, attached to ticket 58213 in the support desk tool

**Flows**
- Not provided

**Components**
- Not provided

---

### Bug

---

**1. Observed Behavior**

---

After a Pay now booking of 2 nights or more on Android, the confirmation screen shows the room price as the total and leaves out the city tax. The payment step before it shows the `City tax` line and the correct total, and the card charge and confirmation email are correct.

- Guest booking RS-7Q4K2M, 3 nights, 2 adults, property 40217 with city tax €3.00 per adult per night: the confirmation screen showed Total €387.00 and the card was charged €405.00
- Back office shows one Pay now charge of €405.00 for RS-7Q4K2M: room €387.00 (3 nights at €129.00) plus city tax €18.00. The confirmation email for the same booking says Total €405.00
- 2-night test booking on the Guest Support test phone: the payment step showed the `City tax` line and €270.00, then the confirmation screen showed Total €258.00. Back office has the charge at €270.00
- 1-night test booking on Android shows the correct total: Total €135.00, matching the €129.00 room plus €6.00 city tax charge
- iOS 8.12.0 shows the correct total for the same 3-night booking: Total €405.00. Web showed the correct confirmation total for a 3-night Pay now booking checked on 2026-09-26
- Guest Support found 14 price-mismatch chats from 2026-09-16 (the 8.12 release) to 2026-09-21, all from Android 8.12.1 and all Pay now bookings of 2 nights or more. None came from iOS or web. The Android staged rollout reached every user on 2026-09-21, the day of the escalation
- Pay at property bookings have not been tested and no guest has reported one, because those guests are not charged until arrival
- Until the fix, Guest Support answers these chats with the Back office breakdown and points guests to the confirmation email, which shows the correct total

Steps to Reproduce:
1. On an Android phone with Guest app 8.12.1, search for property 40217 for 2 nights, 2 adults, 1 room
2. Pick a rate plan with Pay now and continue to the payment step
3. Check the price breakdown: expected and actual both show the `City tax` line and a total of €270.00
4. Tap Pay now and complete payment with a test card
5. On the confirmation screen, check the total: expected Total €270.00, actual Total €258.00
6. Open the booking in Back office: the charge is €270.00
7. Cancel the test booking inside free cancellation

Screen recording: Not provided

---

**2. Expected Behavior**

---

The Android confirmation screen shows the same total the guest is charged, with city tax included, for every stay length.

- The confirmation total matches the payment step total, the Back office charge and the confirmation email total
- City tax is part of the total wherever the price breakdown shows a `City tax` line
- Working behavior today: 1-night stays on Android 8.12.1 and 3-night stays on iOS 8.12.0 and web show the full total with city tax
- User expectations: the guest trusts the confirmation total as the amount charged. In the guest's words, "The app should show the right number though"

Checklist
- [ ] Root cause identified
- [ ] Fix implemented
- [ ] Bug no longer reproducible
- [ ] No regressions introduced

---

### BDD Scenarios

---

**Scenario:** Android confirmation total on a multi-night Pay now stay
- **Given** a guest on Android books 2 or more nights with Pay now at a property that charges city tax
- **When** the payment succeeds and the confirmation screen opens
- **Then** the confirmation total includes city tax and equals the amount charged to the card
