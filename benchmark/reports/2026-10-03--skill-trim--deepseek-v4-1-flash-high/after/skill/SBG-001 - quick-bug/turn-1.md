Path: `export/001 - bug-ios-cart-badge-stale-count.md`

Verified: read-back succeeded; 67 lines

HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: `**1. Observed Behavior**` and `**2. Expected Behavior**` (Bug Mode grants these two corpus labels verbatim), `**References:**` (template field label), `---` dividers and `- []` checkboxes (required Bug Mode formatting).

**Quality summary** — Completeness 9, Clarity 9, Actionability 9, Accuracy 9, Relevance 9, Mechanism Depth 8. The two granted corpus labels and the Bug template structure are the only non-sentence-case items, and the title follows the Fernhouse `{Discipline} - {Surface} - {Feature code}` convention. Internal scores, not in the file.

**Summary**
A Quick-energy bug report for the iOS 4.8.0 stale cart badge, built on the template's fixed About and Bug structure with a unit-count repro that pairs the decisive step against the badge the reporter actually sees. It keeps the cross-platform contrast (Android 4.8.2 and web update immediately) as evidence that narrows the report to iOS 4.8.0, and the Fernhouse context line grounds the expected `2` in the badge-shows-units rule. Frequency reads `Always` on the reporter's every-time claim across two test phones, and unprovided fields stay `Not provided` rather than guessed.

Three additions you did not supply, so strike any you disagree with: the discipline code and title (`FE` / `iOS` / `CART`, inferred from the surface where the customer sees it), the `Not applicable` browser fields since an iOS bug has no browser, and repro step 7, which reads your "until the app is restarted" as meaning the badge corrects on restart. I did not add a root cause, and the checklist keeps root-cause tracking open for engineering.

ClickUp tooling is not available in this session, so there is nothing to push. Want a `DS` or `CART` design-link reference added once the badge spec is to hand, or the BDD scenario added to pin the expected badge state?