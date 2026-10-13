# FE - iOS - CART - Cart badge keeps old count after an item is removed

### About

---

In the Fernhouse iOS app 4.8.0, the cart badge in the tab bar does not update when an item is removed from the cart. It keeps showing the old unit count until the app is restarted. Android 4.8.2 and web update the badge straight away.

| Field           | Value                                                        |
| --------------- | ------------------------------------------------------------ |
| Frequency       | Always (every time on two iOS test phones, per reporter)     |
| Severity        | Medium                                                       |
| Platform        | iOS (app 4.8.0)                                              |
| Device          | Not provided (two iOS test phones, models not given)         |
| OS version      | Not provided                                                 |
| Browser         | Not applicable (native app)                                  |
| Browser version | Not applicable (native app)                                  |

**References:** Not provided

---

### Bug

---

**1. Observed Behavior**

---

After an item is removed in the cart, the tab bar badge keeps showing the unit count from before the removal
- The cart holds 2 units but the badge still reads "3"
- The badge stays on "3" until the app is restarted
- Error messages: Not provided
- On Android 4.8.2 and web, the badge updates straight away after the same removal

Steps to reproduce:
1. Open the Fernhouse iOS app on version 4.8.0
2. Add 2 units of one product to the cart
3. Add 1 unit of a second product, so the tab bar badge reads "3"
4. Open the cart
5. Tap "Remove" on the single-unit item
6. Check the cart and the tab bar badge: expected 2 units and a badge reading "2", actual 2 units and a badge still reading "3"

Screen recording: Not provided

Customer type (guest or signed in) and market used in testing: Not provided

---

**2. Expected Behavior**

---

When an item is removed from the cart, the tab bar badge should show the new unit count straight away, as it does on Android 4.8.2 and web
- Design spec: Not provided
- Previous working behavior: Not provided
- User expectation: the badge shows the number of units in the cart, so after this removal it reads "2" without restarting the app

Checklist
- [ ] Root cause identified
- [ ] Fix implemented
- [ ] Bug no longer reproducible
- [ ] No regressions introduced
