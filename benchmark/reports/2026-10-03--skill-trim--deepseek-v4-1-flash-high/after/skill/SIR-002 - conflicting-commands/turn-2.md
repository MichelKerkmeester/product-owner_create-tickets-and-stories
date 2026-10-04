Path: `export/002 - Story-wishlist-saved-to-account-in-apps.md`
Verified: read-back succeeded; 87 lines

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the template-fixed acceptance intro line, the ClickUp house-grammar dividers and checklist markers, and supplied literals in backticks (`Web`, `iOS`, `Android`, `50`, `412`, `2026-07-01`, `2026-09-20`, `4.8.0`, `4.8.2`).

Quality summary: Story kind, Quick energy, logged as an approved direction with Lotte named as the decision owner. House grammar passes, including the story preamble, `* * *` section closes above every `##   ` spacer, `- []` requirement items with no build steps, four outcome-led criteria with no divider between a Mark-as-done line and the next criterion, and no `## Delivery` since none was requested and no `Open:` line or undated external gate forced one. The output-format gate ran clean on the file after one fix: the Problem paragraph was split from 100 words and four sentences into three paragraphs inside the 60-word and three-sentence caps. 737 words, inside the 1,400 Story budget. Quick perspectives: User, Delivery.

Summary: the Story makes the wishlist one account-backed list for signed-in customers on `Web`, `iOS` and `Android`, moves a device's saved items into the account list on first sign-in, keeps the `50` item limit with the `50` most recently added kept when two lists merge, and leaves device storage in place for customers with no account. The Problem carries the CS evidence (`412` contacts, `171` and `138` leading cases) and the fact that the split is the shipped design, so the artifact reads as a change rather than a defect. No links were supplied, so `#### **References**` is omitted rather than invented.

Additions and open points, named so you can strike them:

*   The `Web` sign-in requirement and its current behavior are stated as a constraint, taken from the company context, so the change stays in the apps
*   Deliberately left out, not populated: what a signed-in customer sees after signing out, de-duplication when the same product sits on both lists, and the tie-break when items share the same added time at the limit
*   The `64` web-items-missing-in-the-app and `39` limit-reached contact groups are accounted for by the unified-list and limit requirements rather than repeated as Problem numbers, and the month split, the `23` complaint-tagged contacts and the customer quotes stay in the source
*   The feature code `WISH`, `accounts-service` and the two-week store cycle plus the roughly one-week propagation are left out of the Story, since Story titles carry no discipline code and the release mechanics belong to the tasks

The next step is either your amendments to those four points, or a `$task` breakdown in the Story lane. No ClickUp tooling is available in this runtime, so there is nothing to push.