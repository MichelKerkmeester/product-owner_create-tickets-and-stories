```markdown
# FE - Guest app - BOOK - Android confirmation total leaves out city tax

### About

---

On Android 8.12.1, the Total on the booking confirmation screen leaves out city tax for Pay now stays of 2 nights or more. Guests then see a lower amount than the one charged to their card. The charge itself is correct. Only the confirmation screen shows less.

| Field           | Value                                                                 |
| --------------- | --------------------------------------------------------------------- |
| Frequency       | Always (Pay now stays of 2 nights or more, per Guest Support, reproduced on the guest's phone and the Guest Support test phone) |
| Severity        | High                                                                  |
| Platform        | Android, Guest app 8.12.1                                             |
| Device          | Guest's phone: Not provided. Guest Support test phone: model Not provided |
| OS Version      | Android 14 (Guest Support test phone). Guest's phone: Not provided    |
| Browser         | Not applicable (native app)                                           |
| Browser Version | Not applicable (native app)                                           |

**References:**

**Support ticket**
- Guest Support ticket 58213, escalated by Maren (Tier 2) on 2026-09-21, booking reference RS-7Q4K2M

---

### Bug

---

**1. Observed Behavior**

---

After Pay now on a stay of 2 nights or more, the confirmation screen shows the room price as the Total and leaves out city tax
- Booking RS-7Q4K2M, property 40217, 3 nights, 2 adults: the confirmation screen showed Total €387.00. The card was charged €405.00, which is €387.00 for the room plus €18.00 city tax (€3.00 per adult per night)
- Back office shows one Pay now charge of €405.00 for RS-7Q4K2M, and the confirmation email for the same booking shows Total €405.00
- Guest Support test, 2 nights: the payment step showed the City tax line and €270.00. After Pay now, the confirmation screen showed Total €258.00. Back office has the charge at €270.00
- Guest Support test, 1 night: the confirmation screen showed Total €135.00, which matches the charge of €129.00 plus €6.00 city tax
- The same 3-night booking on iOS 8.12.0 shows Total €405.00 on the confirmation screen. A 3-night Pay now booking on web, checked on 2026-09-26, showed the correct total
- 14 chats tagged price-mismatch since the 2026-09-16 release, all from Android 8.12.1 and all Pay now stays of 2 nights or more, with none from iOS or web. Guests read the difference as an overcharge
- Android 8.12.1 reached all users on 2026-09-21. Until a fix ships, Guest Support answers these chats with the Back office breakdown and points guests to the confirmation email

Steps to Reproduce:
1. Open the Guest app 8.12.1 on an Android 14 phone with app language en-GB
2. Search property 40217 for a 2-night stay, 2 adults, 1 room
3. Pick a rate plan with Pay now and continue to the payment step
4. Check that the price breakdown shows the City tax line and a total of €270.00
5. Tap Pay now and complete payment with a test card
6. On the confirmation screen, read Total. Expected: €270.00. Actual: €258.00

Screen recording: Not provided. The guest's screenshot of the confirmation screen is attached to ticket 58213 in the support desk tool (link not provided).

Not tested: Pay at property bookings, city tax set per stay, currencies other than EUR, locales other than en-GB and Android 8.11.2.

---

**2. Expected Behavior**

---

On Android, the confirmation screen Total matches the amount charged, city tax included, for every stay length. For RS-7Q4K2M the Total is €405.00
- Design spec: Not provided
- Previous working behavior: Not provided
- Matching surfaces: the iOS 8.12.0 and web confirmation screens and the confirmation email already show the total with city tax
- User expectation: the Total on the confirmation screen is the amount taken from the guest's card

Checklist
- [ ] Root cause identified
- [ ] Fix implemented
- [ ] Bug no longer reproducible
- [ ] No regressions introduced

---

### BDD Scenarios

---

**Scenario:** Confirmation total includes city tax on a multi-night Pay now stay
- **Given** a guest on Android books 2 nights for 2 adults at a property that charges €3.00 city tax per adult per night
- **And** the payment step shows the City tax line and a total of €270.00
- **When** the guest completes Pay now and the confirmation screen opens
- **Then** the confirmation screen shows Total €270.00, the same amount charged to the card
```

Export-equivalent path: `export/002 - bug-android-confirmation-total-city-tax.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `**1. Observed Behavior**` and `**2. Expected Behavior**` (fixed Bug corpus labels), `OS Version` and `Browser Version` (template field labels).

**Quality:** The report passes the Bug gate. It covers one defect in the fixed template order, uses numbered steps where the key step shows expected against actual, and keeps the four checklist items exactly as written. Every value comes from ticket 58213, the Roamstay context or your reply.

**Decisions to check.** You didn't answer these from my earlier question, so I made a call on each. Strike any you disagree with:
- **Frequency is Always.** Maren's escalation says every Pay now Android guest with 2+ nights sees it, and it happened on two devices. I wrote the scope into the cell next to the label.
- **The title uses `FE`.** iOS, web and the confirmation email all show the right total, which points at the Android screen. That is only an inference because nobody has read the code yet. If the root cause turns out to be in `booking-service`, change the title to `BE`.
- **Expected behavior only asks for the correct Total.** It doesn't require a City tax line on the confirmation screen.
- **Previous working behavior reads Not provided.** Nobody has checked Android 8.11.2, so I didn't call this a regression.
- **I added two things you didn't mention:**
  - The "Not tested" line, which covers Pay at property, per-stay city tax, other currencies, other locales and 8.11.2.
  - The BDD scenario.

**Next step:** Once you confirm or change the decisions above, the report is ready to go to the Booking squad as a ClickUp task.