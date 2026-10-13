# FE - iOS - CART - Cart badge keeps the old count after an item is removed

### About

---

In iOS app 4.8.0, the tab bar cart badge keeps the old unit count after a cart item is removed, until the app restarts. Android 4.8.2 and web update at once.

| Field           | Value                                                                 |
| --------------- | --------------------------------------------------------------------- |
| Frequency       | Always (every attempt, both iOS test phones, per reporter) |
| Severity        | Medium                                                                |
| Platform        | iOS (app 4.8.0)                                                       |
| Device          | Not provided (two iOS test phones, no models) |
| OS Version      | Not provided                                                          |
| Browser         | Not applicable (native app)                                           |
| Browser Version | Not applicable (native app)                                           |

**References:** Not provided

---

### Bug

---

**1. Observed Behavior**

---

After "Remove" on a cart line, the cart is right but the badge keeps the old count
- Removing the single-unit line from 3 units leaves 2, but the badge reads "3"
- No error message is shown
- It stays wrong for the session until an app restart

Steps to Reproduce:
1. Open Fernhouse iOS app 4.8.0 with an empty cart
2. Add 2 units of one product
3. Add 1 unit of a second product
4. Check the badge reads "3"
5. In the cart, tap "Remove" on the second product's line
6. Expected: the badge reads "2", actual: the cart holds 2 units and the badge reads "3"
7. Restart the app, and the badge now reads "2"

Screen recording: Not provided

---

**2. Expected Behavior**

---

The badge shows the new unit count on removal, without a restart
- Design spec: the badge counts units, not lines, so removing the 1-unit line from a 3-unit cart leaves "2"
- Previous working behavior: Not provided
- User expectation: the badge matches the cart, as on Android 4.8.2, web and iOS when adding

Checklist
- [ ] Root cause identified
- [ ] Fix implemented
- [ ] Bug no longer reproducible
- [ ] No regressions introduced

---

### BDD Scenarios

---

**Scenario:** Removing a line updates the badge on iOS
- **Given** the cart holds 2 units of one product and 1 of another, and the badge reads "3"
- **When** the customer taps "Remove" on the 1-unit line
- **Then** the badge reads "2" straight away, without a restart
