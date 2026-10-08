# FE - iOS - CART - Cart badge keeps old count after item removed

## About

---

The cart badge in the iOS tab bar keeps the unit count from before an item is removed from the cart. It stays stale until the app is restarted.

| Field           | Value                                                  |
| --------------- | ------------------------------------------------------ |
| Frequency       | Always (reproduced on both iOS test phones, per reporter) |
| Severity        | Medium                                                 |
| Platform        | iOS 4.8.0                                              |
| Device          | Two iOS test phones, models not provided               |
| OS Version      | Not provided                                           |
| Browser         | Not applicable                                         |
| Browser Version | Not applicable                                         |

**References:** Not provided

---

### Bug

---

**1. Observed Behavior**

---

After one unit is removed from the cart, the tab bar badge still shows the old unit count.
- The cart holds 2 units after the removal, but the badge reads "3"
- The badge stays on "3" until the app is restarted
- The result happens every time on both iOS test phones
- Android 4.8.2 and web update the badge straight away for the same removal
- Error message: Not provided

Steps to Reproduce:

1. Add 2 units of one product to the cart on iOS 4.8.0
2. Add 1 unit of a different product to the cart
3. Observe the tab bar cart badge reads "3"
4. Open the cart
5. Tap "Remove" on the single-unit item
6. Observe the cart holds 2 units while the badge still reads "3". The badge should read "2"

Screen recording: Not provided

---

**2. Expected Behavior**

---

The tab bar badge updates at once after the removal and reads "2", matching the units in the cart.
- The badge counts units, not lines
- Design specification: Not provided
- Previous working behavior: Not provided
- Android 4.8.2 and web show the updated count straight away for the same removal
- User expectation: the badge matches the cart without an app restart

Checklist

- [] Root cause identified
- [] Fix implemented
- [] Bug no longer reproducible
- [] No regressions introduced
