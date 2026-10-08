Path: `export/001 - bug-cart-badge-stale-count-after-removal.md`

Verified: read-back succeeded; 63 lines

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Quality summary: Quick energy. The report covers frequency, severity, platform, steps, observed and expected behavior, and the four fixed QA checklist items. Device models, iOS OS version and account type are not provided, so those fields read "Not provided" rather than guessed values.

Please confirm two additions I made:
- **Title discipline code:** `FE` is my proposal, since the defect sits in the iOS client. The `CART` feature code comes from the Fernhouse context. Change `FE` if triage assigns another discipline.
- **Frequency:** `Always` rests on your "every time on both iOS test phones" line.

The context says iOS 4.8.0 is still the current iOS release with no hotfix, so the defect is live in production. If you can send the phone models, iOS version and whether the tester was signed in, I can fill those fields.