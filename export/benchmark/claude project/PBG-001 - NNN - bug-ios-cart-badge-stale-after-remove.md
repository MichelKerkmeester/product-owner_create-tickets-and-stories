# FE - iOS - CART - Cart badge keeps old count after an item is removed

## About

---

In the Fernhouse iOS app 4.8.0, the tab bar cart badge keeps the old unit count after a removal until the app restarts. Android 4.8.2 and web update it at once.

| Field           | Value                                                        |
| --------------- | ------------------------------------------------------------ |
| Frequency       | Always (two iOS test phones, per reporter) |
| Severity        | Medium                                                       |
| Platform        | iOS (app 4.8.0)                                              |
| Device          | Not provided (models not given) |
| OS version      | Not provided                                                 |
| Browser         | Not applicable (native app)                                  |
| Browser version | Not applicable (native app)                                  |

**References:** Not provided

---

### Bug

---

**1. Observed Behavior**

---

After a removal, the tab bar badge keeps the old unit count
- The cart holds 2 units but the badge reads "3" until the app restarts
- Error messages: Not provided

Steps to reproduce:
1. Open the Fernhouse iOS app 4.8.0
2. Add 2 units of one product
3. Add 1 unit of a second product, so the badge reads "3"
4. Open the cart
5. Tap "Remove" on the single-unit item
6. Expected 2 units and a badge reading "2", actual 2 units and a badge reading "3"

Screen recording: Not provided

Customer type (guest or signed in) and market used in testing: Not provided

---

**2. Expected Behavior**

---

After a removal, the badge shows the new count at once, as on Android 4.8.2 and web
- Design spec: Not provided
- Previous working behavior: Not provided
- User expectation: the badge reads "2" after this removal, without an app restart

Checklist
- [] Root cause identified
- [] Fix implemented
- [] Bug no longer reproducible
- [] No regressions introduced
