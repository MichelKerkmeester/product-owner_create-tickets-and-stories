```markdown
# Customer - Wishlist - One list across app and web

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
Signed-in customers keep two wishlists, one in the app on the device and one on the account for web. Customers read that as items going missing.

`412` wishlist contacts arrived between `2026-07-01` and `2026-09-20`, `171` of them after a new phone or a reinstall and `138` after a customer looked for app items on web. This story moves the app wishlist for signed-in customers onto the account, so one list follows the customer.

#### Problem
* * *
The app and the website are one shop from the customer's side, so a list that exists in only one of them reads as lost. The app wishlist has been saved on the device since it shipped, which works for customers who never sign in, while the web wishlist has always been saved to the account.

#### Solution
* * *
Signed-in customers get one wishlist on the account, so it follows them between the app and web and outlives any single phone. The list a customer builds in the app stops being a property of the device, and the account list becomes the list the app shows.

**Expected outcomes**
* * *
*   A signed-in customer's saved items are there after a new phone or a reinstall, and when they switch between web and the app
*   Wishlist contacts stop arriving because a list was lost or split across the app and web
* * *
##   

## Requirements
* * *
**Wishlist storage**
* * *
- [] A signed-in customer's wishlist is saved to the account on `iOS` and `Android`, not to the device
- [] The account wishlist is the same list web shows for that sign-in
- [] A customer's wishlist holds up to `50` items
- [] Web keeps asking a customer to sign in to show or change the wishlist

**First sign-in on a device**
* * *
- [] On the first sign-in on a device, the items saved on that device move into the account wishlist
- [] When the device list and the account list together pass `50` items, the account keeps the `50` most recently added

**Customers without an account**
* * *
- [] A customer who is not signed in keeps the device wishlist, saved without an account
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **A signed-in customer's list is the same everywhere**
* * *
*   **Given** a signed-in customer with items in their wishlist
*   **When** they open the wishlist on web, in the app and after signing in on another phone
*   **Then** every surface shows the same saved items, with none lost as they move between them
* * *
- [] _Mark as done, if the criteria are met_

2\. **Items saved before signing in arrive in the account list**
* * *
*   **Given** a customer who saved items in the app before signing in
*   **When** they sign in on that device for the first time
*   **Then** those items appear in the account wishlist
* * *
- [] _Mark as done, if the criteria are met_

3\. **A customer without an account keeps the device wishlist**
* * *
*   **Given** a customer who is not signed in
*   **When** they save or open the wishlist in the app
*   **Then** it works on the device as it does today, and no sign-in is asked for
* * *
- [] _Mark as done, if the criteria are met_

4\. **The two lists meet inside the cap**
* * *
*   **Given** a device list and an account list that together hold more than the cap allows
*   **When** the customer signs in on that device
*   **Then** the account wishlist holds its full cap and keeps the items added most recently
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
The delivery budget or expected size for the approved scope.

*   TBD...

#### External dependencies
* * *
Constraints outside the team's control that gate delivery, with no date the team can set.

*   **App stores** - review and approve the next iOS and Android builds, so most customers get the change about a week after release. Date: TBD...

#### Rabbit holes
* * *
Areas that could waste effort, create ambiguity or distract from the intended outcome.

*   TBD...

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   TBD...
* * *
```

Export-equivalent path: `export/001 - Story-wishlist-one-list-app-and-web.md`

Artifact kind: Story. One feature area, four supplied requirements that become implementation work, so this is not an Epic.

HVR self-scan: 0 hard blockers. Fixed: no banned wording needed changing. Kept with reason: `TBD...` is the fixed house token in the three Delivery slots rather than a prose ellipsis, the `- []`, `1\.` and `_Mark as done, if the criteria are met_` literals are house grammar, and the hyphen separator in the External dependencies bullet follows the Delivery template.

Quality status: all four requirements you gave landed as `- []` constraints with their values intact, including `50` and the most-recently-added rule, and each acceptance criterion traces to one of them without restating a value. Solution is written as the decision and does not preview Requirements or the criteria. House grammar passes: preamble, dividers after content headings, `* * *` above each `##   ` spacer, `1\.` numbering, no divider between a Mark-as-done line and the next criterion.

Three notes you can strike:

- I added `- [] Web keeps asking a customer to sign in to show or change the wishlist` as a scope constraint, because your change is app-side and web's sign-in is how it works today. Remove it if web's sign-in should change as well.
- I added the `## Delivery` section, because the change needs the next store releases and the team cannot date store approval. The three `TBD...` slots sit there because you supplied no estimate, risks or exclusions.
- Not covered: what the app shows for a customer who signs out. Say the word and it becomes a fifth requirement and criterion.

Lotte's sign-off reads as approval for the direction, so the story is written as a decision rather than a proposal. No ClickUp connector is attached in this session, so filing is yours to do. Answer any of the three notes above and I will fold it in as a refinement.