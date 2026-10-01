```markdown
# FE - iOS - CART - Cart badge keeps stale count after item removal

## About

---

On the Fernhouse iOS app `4.8.0`, removing the final unit of a cart line leaves the tab bar badge on the pre-removal unit count until the app is restarted.

| Field           | Value                                                                 |
| --------------- | --------------------------------------------------------------------- |
| Frequency       | Always (reproduced on both iOS test phones, per reporter)              |
| Severity        | Medium                                                                |
| Platform        | iOS                                                                    |
| Device          | Not provided (two iOS test devices reported, models unknown)           |
| OS Version      | Not provided                                                           |
| Browser         | Not applicable (native app)                                            |
| Browser Version | Not applicable (native app)                                            |

**References:** Not provided

---

### Bug

---

**1. Observed Behavior**

---

Removing an item from the cart clears the item from the cart screen while the tab bar badge keeps the count it held before the removal
- The cart screen shows the remaining 2 units while the tab bar badge still reads `3`
- Error message: Not provided
- The badge holds the stale count until the app is restarted, after which it matches the cart
- Android `4.8.2` and web updated the badge straight away in the same scenario, per the reporter

Steps to Reproduce:
1. Add 2 units of one product to the cart
2. Add 1 unit of a different product
3. Open the cart and check that the tab bar badge reads `3`
4. Tap `Remove` on the line holding the single unit
5. Observe the cart holding 2 units while the tab bar badge still reads `3`, where `2` is expected

Screen recording: Not provided.

---

**2. Expected Behavior**

---

Tapping `Remove` on the single-unit line should drop the tab bar badge to `2` at the same moment the cart drops to 2 units, with no restart needed
- Design spec: Not provided
- Previous working behavior: Not provided
- User expectation: the badge matches the units in the cart whenever the cart changes

Checklist
- [] Root cause identified
- [] Fix implemented
- [] Bug no longer reproducible
- [] No regressions introduced
```

Export-equivalent path: `export/001 - bug-ios-cart-badge-stale-count.md`

Quality status: PASS. Six floors cleared. Accuracy decides a bug, so the report states only what the reporter observed, and no root-cause hypothesis was added because none was supplied. Environment cells the reporter did not give carry `Not provided` rather than a guess. Scope is the badge count on iOS only.

HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: `**1. Observed Behavior**` and `**2. Expected Behavior**` (the fixed Barter corpus labels, granted exemption), `Not provided` (the template's placeholder for unsupplied fields).

Summary: one bug report for the iOS badge, titled in the house format from `context/fernhouse-context.md` as `FE - iOS - CART`, since `cart-service` owns the badge count and CART is the area where the customer sees the count. Frequency is `Always` on the reporter's every-time claim across two devices, with the device detail kept beside the label. The Android and web comparison sits in Observed Behavior as the reporter's control, not as evidence of a cause. The `$quick` route narrowed the artifact, so `### BDD Scenarios` is left out and the reproduction steps carry the expected-versus-actual pair instead. Two additions you may want to strike: step 3 asks the reader to confirm the badge reads `3` before removing, and the expected behavior names `2` as the badge value. Both restate the numbers in your repro.

Next step: say the word and I can raise it in ClickUp, or add a BDD scenario if QA wants the state sequence in Given/When/Then form.