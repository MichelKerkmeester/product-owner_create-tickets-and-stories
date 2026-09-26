# FE - Guest app - BOOK - Android confirmation total leaves out city tax

### About

---

On Android 8.12.1, the confirmation screen for Pay now bookings of 2 nights or more shows a total without city tax, so the total is lower than the amount charged to the guest's card. Guests read the difference as an overcharge, and Guest Support escalated it to the Booking squad as ticket 58213.

| Field           | Value                                                                              |
| --------------- | ---------------------------------------------------------------------------------- |
| Frequency       | Always, for Pay now stays of 2 nights or more (per the Guest Support escalation)   |
| Severity        | High                                                                               |
| Platform        | Android                                                                            |
| Device          | Guest's phone not provided, Guest Support Android test phone (model not provided)  |
| OS Version      | Android 14 on the test phone, guest's version not provided                         |
| Browser         | Not applicable                                                                     |
| Browser Version | Not applicable                                                                     |

**References:**

**Support ticket**
- Guest Support ticket 58213, booking RS-7Q4K2M, escalated to the Booking squad by Maren (Tier 2) on 2026-09-21 (link not provided)

---

### Bug

---

**1. Observed Behavior**

---

After a guest completes Pay now on a stay of 2 nights or more, the Android confirmation screen shows only the room price as the total. The card is charged the full total with city tax, and the payment step and the confirmation email both show that full total.

- Booking RS-7Q4K2M (3 nights, 2 adults, 1 room, property 40217, city tax €3.00 per adult per night): the confirmation screen showed Total €387.00. The one Pay now charge was €405.00, which is €387.00 for the room plus €18.00 city tax
- The confirmation email for RS-7Q4K2M shows Total €405.00, and Back office shows the same breakdown. The charge is correct, and only the confirmation screen is wrong
- Guest Support test, 2 nights, 2 adults: the payment step showed the City tax line and €270.00, the confirmation screen showed Total €258.00 and the charge was €270.00
- Guest Support test, 1 night, 2 adults: the confirmation screen showed Total €135.00, which matches the €129.00 room plus €6.00 city tax charged
- The same 3-night Pay now booking shows Total €405.00 on the iOS 8.12.0 confirmation screen. A 3-night Pay now booking on web, checked on 2026-09-26, also showed the correct confirmation total
- Guest Support has 14 price-mismatch chats since the 2026-09-16 release. All came from Android 8.12.1 and all were Pay now bookings of 2 nights or more. None came from iOS or web. The staged Android rollout reached all users on 2026-09-21
- Tested only with EUR, the en-GB app language and a per adult per night city tax rule. Pay at property bookings were not tested, and no guest has reported the problem on one yet

Until the fix ships, Guest Support answers these chats with the Back office breakdown and points guests to the confirmation email, because the email shows the correct total.

Steps to Reproduce:
1. On an Android phone with app 8.12.1, open property 40217, which charges city tax of €3.00 per adult per night
2. Select a 2-night stay for 2 adults and choose a Pay now rate plan
3. Go to the payment step. The price breakdown shows the City tax line and a total of €270.00
4. Complete Pay now with a test card
5. Look at the confirmation screen total. Expected: Total €270.00. Actual: Total €258.00, which leaves out the €12.00 city tax
6. Look up the booking in Back office. It shows a charge of €270.00

Guest Support cancelled its test bookings within the free cancellation period immediately after testing.

Screen recording: Not provided. The guest's screenshot of the Android confirmation screen showing Total €387.00 is on ticket 58213 in the support desk tool.

---

**2. Expected Behavior**

---

The Android confirmation screen should show the same total the guest is charged, including city tax. That total also matches the payment step, the confirmation email and Back office. For RS-7Q4K2M, that is Total €405.00.

- Design specifications: Not provided
- Previous working behavior: Not provided for Android 8.11.2. In the current release, the iOS 8.12.0 and web confirmation screens show the full total for a 3-night Pay now booking, and Android shows the correct total for a 1-night Pay now booking
- User expectation: the guest in ticket 58213 wrote "The app should show the right number". Guest Support needs the Android confirmation screen to show the same total that is charged, so guests stop reporting an overcharge

Checklist
- [ ] Root cause identified
- [ ] Fix implemented
- [ ] Bug no longer reproducible
- [ ] No regressions introduced

---

### BDD Scenarios

---

**Scenario:** Confirmation total includes city tax on a stay of 2 nights or more
- **Given** a guest on Android books a 3-night Pay now stay for 2 adults at a property with a city tax of €3.00 per adult per night and a room total of €387.00
- **When** the payment is charged and the confirmation screen opens
- **Then** the confirmation screen shows Total €405.00, the same amount charged to the card and shown in the confirmation email

**Scenario:** 1-night confirmation total stays correct
- **Given** a guest on Android books a 1-night Pay now stay for 2 adults at the same property
- **When** the payment is charged and the confirmation screen opens
- **Then** the confirmation screen shows Total €135.00, the same amount charged to the card
