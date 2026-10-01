No Canvas panel in this session, so the Deliverable Block is rendered below as one fenced block.

````markdown
# FE - iOS - CART - Cart badge keeps the old count after an item is removed

## About

---

In the Fernhouse iOS app on version 4.8.0, the cart badge in the tab bar keeps the previous unit count after a line is removed from the cart, and it stays stale until the app is restarted.

| Field           | Value                                                       |
| --------------- | ----------------------------------------------------------- |
| Frequency       | Always (reproduced both iOS test phones, per reporter)      |
| Severity        | Medium                                                      |
| Platform        | iOS                                                         |
| Device          | Not provided (two iOS test phones reported, models unknown)  |
| OS Version      | Not provided                                                |
| Browser         | Not applicable (native app)                                 |
| Browser Version | Not applicable (native app)                                 |

**References:** Not provided

---

### Bug

---

**1. Observed Behavior**

---

Removing a line from the cart leaves the tab bar badge on the unit count it held before the removal
- With 2 units of one product and 1 unit of another in the cart, the badge reads "3" as expected
- Tapping "Remove" on the single-unit line leaves 2 units in the cart while the badge still reads "3"
- The badge catches up only after the app is restarted
- The reporter sees this every time on both iOS test phones running iOS 4.8.0
- On Android 4.8.2 and on web, the same cart change updates the badge straight away

Steps to Reproduce:
1. Open the Fernhouse iOS app on version 4.8.0 and add 2 units of one product to the cart
2. Add 1 unit of a second product and confirm the tab bar badge reads "3"
3. Open the cart
4. Tap "Remove" on the line holding the single unit
5. Observe the cart now holds 2 units while the badge still reads "3"
6. Restart the app and observe the badge show the current unit count

Screen recording: Not provided

---

**2. Expected Behavior**

---

Removing a line from the cart updates the tab bar badge to the new unit count as soon as the cart changes
- Design specification: Not provided
- Previous working behavior: Not provided
- User expectation: the badge shows the units actually in the cart, so a customer reading it does not need to restart the app

Checklist
- [] Root cause identified
- [] Fix implemented
- [] Bug no longer reproducible
- [] No regressions introduced

---
````

Export-equivalent path: `export/001 - bug-ios-cart-badge-stale-count.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `**1. Observed Behavior**` and `**2. Expected Behavior**` (the two fixed corpus labels Bug Mode exempts), `**References:**`, `Design specification:`, `Previous working behavior:` and `User expectation:` (template field labels), and the quoted UI strings "3" and "Remove" (copy carried from the report).

Quality status: Structure pass (fixed About and Bug order, four-item QA checklist, no table of contents, `-` bullets and `- []` boxes). Evidence pass (deciding step pairs the tap with the cart state and the badge state). Scope pass (WHAT and WHY only, no fix direction, no invented cause, no invented device or OS values). Voice pass.

Summary: one report for a stale cart badge on iOS 4.8.0, with the unit-level reproduction and the Android 4.8.2 and web comparison kept as supplied. Title follows the Fernhouse `{Discipline} - {Surface} - {Feature code} - {Title}` convention as `FE - iOS - CART`.

Three points you may want to correct before this goes into ClickUp:
- `Device` and `OS Version` are `Not provided`. Phone models and iOS builds would let QA match your two test devices.
- `Frequency` is `Always`, read from "happens every time on both our iOS test phones". If it is narrower than every removal on every cart, tell me the real bound and I will restate it.
- Step 6 assumes the restart shows the correct count, read from "until the app is restarted". If a restart leaves the badge stale too, that step changes.

No ClickUp connector is present in this session, so there is nothing to push through. Tell me if you want the device and OS values filled, a BDD scenario added, or the report reissued under a different discipline code.