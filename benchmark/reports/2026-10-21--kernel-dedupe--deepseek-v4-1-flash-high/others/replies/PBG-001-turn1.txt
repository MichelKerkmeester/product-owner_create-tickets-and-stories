```markdown
# FE - iOS - CART - Cart badge keeps the old count after an item is removed

## About

---

On the iOS app running 4.8.0, the tab bar cart badge keeps the count it held before an item was removed, and only corrects itself when the app restarts. The cart holds the right number of units throughout.

| Field     | Value                                                     |
| --------- | --------------------------------------------------------- |
| Frequency | Always (every attempt on both iOS test phones, per reporter) |
| Severity  | Medium                                                    |
| Platform  | iOS 4.8.0                                                 |
| Device    | Not provided (two internal iOS test phones)               |
| OS Version | Not provided                                             |

**References:** Not provided

---

### Bug

---

**1. Observed Behavior**

---

Tapping "Remove" on a cart item on iOS 4.8.0 leaves the tab bar badge on the earlier unit count
- Adding 2 units of one product and 1 unit of another sets the badge to "3"
- Tapping "Remove" on the single item leaves the cart holding 2 units while the badge still reads "3"
- The stale count survives closing and reopening the cart, and clears only when the app restarts
- The reporter reproduced it every time on both iOS test phones, while Android 4.8.2 and web update the badge straight away

Steps to Reproduce:
1. Open the iOS app on version 4.8.0
2. Add 2 units of one product to the cart
3. Add 1 unit of a second product, and confirm the tab bar badge reads "3"
4. Open the cart and tap "Remove" on the single item (expected badge "2", actual badge stays "3")
5. Close and reopen the cart, and confirm the cart holds 2 units while the badge still reads "3"
6. Restart the app, and confirm the badge then reads "2"

Screen recording: Not provided

---

**2. Expected Behavior**

---

Removing an item should move the badge to the remaining unit count as soon as the cart changes, with no restart needed
- Design specification: Not provided
- Previous working behavior: Android 4.8.2 and web update the badge immediately after the same removal, per reporter
- User expectation: the badge shows the units actually in the cart, so it never sends a customer to a count the cart does not hold

Checklist
- [] Root cause identified
- [] Fix implemented
- [] Bug no longer reproducible
- [] No regressions introduced

---
```

Export-equivalent path: `export/NNN - bug-ios-cart-badge-stale-count.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `"Remove"`, `"3"` and `"2"` are supplied UI labels and observed screen values, and `Not provided` is the Bug template's own token for unsupplied fields.

Quality: every floor met | Kind: Bug | Energy: Quick

The report holds your steps, the Android 4.8.2 and web comparison and the Medium severity as given, and it stops at WHAT is wrong rather than guessing at a cause. The title follows the house `{Discipline} - {Surface} - {Feature code} - {Title}` form, taking `CART` because the badge belongs to that area. Step 4 pairs the expected badge with the actual one so QA can verify the reproduction without reading the rest.

### Open items

1. **Device and OS version**
   - **Situation:** The two test phones were named only as internal iOS test phones, with no model or OS build stated.
   - **Open:** Send the device models and OS versions, or leave both as `Not provided`.
2. **App version placement**
   - **Situation:** The house field table has no app version row, so 4.8.0 sits in Platform and in the first reproduction step.
   - **Open:** Say if your tracker needs an App Version row added to the table.

Want me to change anything?