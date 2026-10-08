# FE - Guest app - BOOK - Android confirmation total omits city tax on stays of 2 or more nights

## About

---

On Android 8.12.1, the confirmation screen for a Pay now stay of 2 or more nights shows a Total without the City tax, so the Total is lower than the amount charged. The payment step shows the City tax line, and the confirmation email for the same booking shows the charged Total.

| Field           | Value                                                          |
| --------------- | -------------------------------------------------------------- |
| Frequency       | Not provided                                                   |
| Severity        | High                                                           |
| Platform        | Android                                                        |
| Device          | Not provided (guest). Guest Support test phone model not provided |
| OS Version      | Not provided (guest). Guest Support test phone runs Android 14 |
| Browser         | Not applicable                                                 |
| Browser Version | Not applicable                                                 |

**References:**

**Flows**
- Not provided

**Components**
- Not provided

---

### Bug

---

**1. Observed Behavior**

---

The Total on the confirmation screen is the room price only, with no City tax line. The amount charged is higher than that Total by the City tax.

- Source: Guest Support ticket 58213, booking RS-7Q4K2M, Pay now, booked 2026-09-20
- The guest saw Total €387.00 for a 3-night stay for 2 adults and was charged €405.00
- Back office shows the charge as room €387.00 plus City tax €18.00, totalling €405.00
- The confirmation email for the same booking shows Total €405.00
- Guest Support test on 2026-09-21, Guest app 8.12.1 on Android 14, 2 nights and 2 adults, Pay now: the payment step shows the City tax line and €270.00
- The same test's confirmation screen shows Total €258.00, and Back office records the charge as €270.00
- A 1-night test on the same setup shows Total €135.00, which is room €129.00 plus City tax €6.00. The Back office charge for this test is not recorded
- The same 3-night booking on iOS 8.12.0 shows Total €405.00
- A 3-night Pay now booking on web, checked on 2026-10-08, shows the correct Total
- Pay at property: not tested
- 14 chats tagged price-mismatch between 2026-09-16 and 2026-09-21 are all Android 8.12.1 Pay now bookings of 2 or more nights. Whether each was checked for this cause is not recorded
- Error message: Not provided

Steps to Reproduce:
1. Open the Guest app 8.12.1 on an Android 14 device
2. Book property 40217 for 2 nights, 2 adults and 1 room
3. Choose a rate plan with Pay now and continue to payment
4. Observe the payment step shows a City tax line and a total of €270.00
5. Pay with the test card
6. Observe the confirmation Total is €258.00. Expected: €270.00, matching the payment step and the charge

Screen recording: Not provided. The guest's screenshot is held in the support desk tool for ticket 58213 and is not attached.

---

**2. Expected Behavior**

---

The confirmation Total equals the amount charged, with the City tax included. For the ticket stay, that is €405.00. For the 2-night test, it is €270.00.

- Design specifications: Not provided
- Previous working behavior: The iOS 8.12.0 confirmation showed Total €405.00 for the same 3-night booking
- User expectations: The guest expects the confirmation Total to match the amount charged and says the app should show the right number

Checklist
- [] Root cause identified
- [] Fix implemented
- [] Bug no longer reproducible
- [] No regressions introduced

---

### BDD Scenarios

---

**Scenario:** Confirmation total on Android for a Pay now stay with city tax
- **Given** a Pay now booking of 2 or more nights in Guest app 8.12.1 on Android
- **When** the guest completes payment and the confirmation screen loads
- **Then** the Total equals the amount charged, with the City tax included
