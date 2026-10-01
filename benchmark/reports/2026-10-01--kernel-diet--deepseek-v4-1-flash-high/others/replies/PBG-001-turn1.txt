Deliverable Block:

```markdown
<!-- Mode: Bug | Energy: Quick | Template: Assets - Bug Report Template - v0.102 -->

# FE - iOS - CART - Cart badge keeps stale count after an item is removed

## About

---

On the Fernhouse iOS app, the cart tab bar badge keeps its previous unit count after an item is removed. The badge shows the stale count until the app restarts, so the number no longer matches the cart the customer is looking at.

| Field           | Value                                          |
| --------------- | ---------------------------------------------- |
| Frequency       | Always (reproduced on both iOS test phones)      |
| Severity        | Medium                                          |
| Platform        | iOS                                             |
| Device          | Not provided (two iOS test phones, models not supplied) |
| OS Version      | Not provided                                    |
| App Version     | `4.8.0`                                         |

**References:**
- Product context: `context/fernhouse-context.md`

---

### Bug

---

**1. Observed Behavior**

---

Removing the single-unit line from the cart leaves the tab bar badge on its pre-removal count
- The badge reads `3` while the cart holds 2 units in one line, so it overstates the cart by one unit
- The badge keeps `3` for the rest of the session and corrects itself only after the app restarts
- Reproduced on every attempt on both iOS test phones, on iOS `4.8.0`
- The same removal on Android `4.8.2` and on web updates the badge straight away, so the stale count is seen on iOS only

Steps to Reproduce:
1. Add 2 units of one product to the cart
2. Add 1 unit of a second product, so the tab bar badge reads `3`
3. Open the cart
4. Tap `Remove` on the single-unit line, which should take the badge to `2`, and it stays on `3`
5. Restart the app, and the badge then reads `2`

Screen recording: Not provided.

Hypothesis, unverified, needs engineering confirmation: the stale count follows the iOS client, because cart-service holds the badge count for all three surfaces and the other two surfaces update it correctly.

---

**2. Expected Behavior**

---

The tab bar badge should show the current unit count as soon as the removal completes
- Product reference: the badge shows the number of units in the cart, not the number of lines, and reads `99+` above 99 units, per the product context
- Design specification: Not provided
- Previous working behavior: Not provided
- User expectation: a customer who removes an item can trust the badge to match the cart without restarting the app

Checklist
- [] Root cause identified
- [] Fix implemented
- [] Bug no longer reproducible
- [] No regressions introduced

---
```

Export-equivalent path: `export/NNN - bug-ios-cart-badge-stale-count.md`

`HVR self-scan: 0 hard blockers. Fixed: nothing beyond always-cut modifiers, which are structural edits and are not counted. Kept with reason: the fixed Bug labels **1. Observed Behavior** and **2. Expected Behavior**, written verbatim under the Bug Mode exemption.`

Quality status: all six dimensions clear their floors. Accuracy 9 carries the reliance, since every specific claim traces to your report or to `fernhouse-context.md`, and the client-vs-service point sits under an explicit unverified label rather than reading as a root cause. Completeness 8 is measured against what you supplied, so the empty `Not provided` cells are honest rather than thin.

What I did with your material, so you can correct any of it:

- **Addition you may strike:** I put iOS `4.8.0` in an `App Version` row, which is not one of the template's fields, because the version is load-bearing for a mobile defect. The template's `Browser` and `Browser Version` rows are omitted because this is not a web bug.
- **Title** follows the Fernhouse convention `{Discipline} - {Surface} - {Feature code} - {Title}`, giving `FE - iOS - CART`, with the cart area taking the `CART` code.
- **Frequency** reads `Always (reproduced on both iOS test phones)`, which your "happens every time on both phones" supports, and the count stays in the cell beside the label.
- **No BDD scenarios section**, matching the compact Quick form.
- **Hypothesis line:** your Android and web comparison is the evidence, and the point about cart-service comes from the product context. It is labelled unverified rather than asserted as the cause. Strike it if you would rather the report carry the reproduction alone.

Next step is your call on those two points: the added `App Version` row and the unverified hypothesis line. There is no ClickUp connector in this session, so I cannot offer a push from here. If tooling is connected in a later message and you approve it explicitly, the body above is already in the push shape, with the H1 becoming the task name.