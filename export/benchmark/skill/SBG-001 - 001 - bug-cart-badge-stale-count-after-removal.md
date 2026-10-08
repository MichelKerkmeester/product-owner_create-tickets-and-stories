# FE - iOS - CART - Cart badge keeps old count after item removal

## About

---

On iOS app 4.8.0, the tab bar cart badge keeps the old unit count after an item is removed from the cart, until the app is restarted. The cart itself holds 2 units after the removal.

| Field           | Value                                                    |
| --------------- | -------------------------------------------------------- |
| Frequency       | Always (reproduced on both iOS test phones, per reporter) |
| Severity        | Medium                                                   |
| Platform        | iOS                                                      |
| Device          | Not provided (two iOS test phones, models not supplied)  |
| OS Version      | Not provided                                             |
| Browser         | Not applicable                                           |
| Browser Version | Not applicable                                           |

**References:** Not provided

---

### Bug

---

**1. Observed Behavior**

---

After one line is removed from the cart, the tab bar cart badge keeps the count from before the removal. The count stays until the app is restarted.
- The cart holds 2 units after the removal
- The tab bar badge still reads 3
- Error message: Not provided

Steps to Reproduce:
1. Add two units of one product to the cart on iOS app 4.8.0
2. Add one unit of a second product. The tab bar cart badge reads 3
3. Open the cart
4. Tap "Remove" on the single-unit item, the second product
5. Observe the cart holds 2 units while the tab bar badge still reads 3. Expected: the badge reads 2

Screen recording: Not provided

---

**2. Expected Behavior**

---

The tab bar cart badge updates to 2 straight away after the removal, matching the 2 units in the cart.
- The badge counts units in the cart, not lines
- Android 4.8.2 and web update the badge straight away on the same removal, per reporter
- Design spec: Not provided

Checklist
- [] Root cause identified
- [] Fix implemented
- [] Bug no longer reproducible
- [] No regressions introduced

---
