# FE - iOS - CART - Cart badge keeps the old count after an item is removed

### About

---

In the iOS app 4.8.0, the cart badge in the tab bar keeps showing the previous unit count after the customer removes an item in the cart. The badge only corrects itself after the app is restarted, while Android 4.8.2 and web update it straight away.

| Field           | Value                                                                 |
| --------------- | --------------------------------------------------------------------- |
| Frequency       | Always (every attempt on both iOS test phones, per reporter)          |
| Severity        | Medium                                                                |
| Platform        | iOS (app 4.8.0)                                                       |
| Device          | Not provided (two iOS test phones, models not given)                  |
| OS Version      | Not provided                                                          |
| Browser         | Not applicable (native app)                                           |
| Browser Version | Not applicable (native app)                                           |

**References:** Not provided

---

### Bug

---

**1. Observed Behavior**

---

After "Remove" is tapped on a cart line, the cart holds the right number of units but the tab bar badge still shows the count from before the removal
- With 3 units in the cart, removing the single-unit line leaves 2 units in the cart and the badge still reads "3"
- No error message is shown
- The badge stays wrong for the rest of the session and shows the correct count only after the app is restarted
- Android 4.8.2 and web show the new count on the badge as soon as the item is removed

Steps to Reproduce:
1. Open the Fernhouse iOS app 4.8.0 with an empty cart
2. Add 2 units of one product to the cart
3. Add 1 unit of a second product to the cart
4. Check that the tab bar badge reads "3"
5. Open the cart and tap "Remove" on the line for the second product
6. Expected: the badge reads "2", actual: the cart holds 2 units and the badge still reads "3"
7. Restart the app and observe that the badge now reads "2"

Screen recording: Not provided

---

**2. Expected Behavior**

---

The tab bar badge shows the new unit count as soon as an item is removed from the cart, without a restart
- Design spec: the badge counts units in the cart, not lines, so removing the 1-unit line from a 3-unit cart leaves the badge on "2"
- Previous working behavior: Not provided
- User expectation: the badge matches the cart on screen, as it does on Android 4.8.2, on web and on iOS when an item is added

Checklist
- [ ] Root cause identified
- [ ] Fix implemented
- [ ] Bug no longer reproducible
- [ ] No regressions introduced

---

### BDD Scenarios

---

**Scenario:** Removing a line updates the badge on iOS
- **Given** the cart holds 2 units of one product and 1 unit of another, and the tab bar badge reads "3"
- **When** the customer taps "Remove" on the 1-unit line in the cart
- **Then** the tab bar badge reads "2" straight away, without restarting the app
