```markdown
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
6. Check the cart and the tab bar badge. Expected: the cart holds 2 units and the badge reads "2". Actual: the cart holds 2 units and the badge still reads "3"

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

---
```

Export-equivalent path: `export/NNN - bug-ios-cart-badge-stale-after-remove.md`

HVR self-scan: 0 hard blockers. Fixed: "Steps to Reproduce", "OS Version" and "Browser Version" changed to sentence case. Kept with reason: `**1. Observed Behavior**` and `**2. Expected Behavior**`, because the Bug Mode corpus uses these labels word for word.

**Quality:** Passes. The report follows the fixed Bug template: an About table, observed behavior before expected behavior, and the four checklist items unchanged. I added no root cause and no environment details you didn't give me.

**Summary:** This is a quick bug report for the stale tab bar badge on iOS 4.8.0. I built the title from your context file's `{Discipline} - {Surface} - {Feature code}` convention, and `CART` covers the cart badge.

- **Frequency:** Set to "Always" because you said it happens every time on two phones.
- **Missing details:** Device models, the iOS version on the phones and a screen recording are marked "Not provided". The "4.8.0" you gave is the app version, so it doesn't fill the iOS version field.
- **Final step:** Step 6 lists the expected and actual result side by side, so QA can check it on its own.

**Additions to check:**

- **Customer type and market line:** You didn't mention this. I added it as "Not provided" because the context file says signed-in carts follow the customer across web and the apps. Delete it if it isn't useful.
- **"Previous working behavior":** Marked "Not provided". Nothing you sent says whether the badge ever updated correctly on iOS, so I didn't call this a regression.
- **Other ways of removing items:** The report only covers tapping "Remove". Lowering the quantity or other ways of removing an item weren't tested, so I left them out.

Next step: tell me the device models and iOS versions, or attach a recording, and I'll add them to the report.