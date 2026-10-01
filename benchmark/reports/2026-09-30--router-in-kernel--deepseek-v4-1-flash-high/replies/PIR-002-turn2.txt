## Customer - Wishlist - One list across web and the apps

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
A signed-in customer's wishlist lives in the account, so web, iOS and Android show one list and saved items survive a new phone or a reinstall. Customers who never sign in keep the device wishlist the apps have today, with no account needed.

#### Problem
* * *
The apps save the wishlist on the device, and web saves it to the account, so a customer who moves to a new phone or reinstalls the app loses the app list, and a customer who uses both surfaces holds two lists without knowing.

CS logged `412` wishlist contacts between `2026-07-01` and `2026-09-20`, `171` about a list lost after a new phone or a reinstall and `138` about items saved in the app that web does not show. Storefront reports that no release changed this behavior, because the app list has always been device-only.

#### Solution
* * *
Signed-in customers get one wishlist on every surface, held in the account, so the app shows the list web shows and saved items survive a new phone or a reinstall. A device that already holds items keeps them, because the list on it joins the account list the first time the customer signs in. Customers who never sign in keep today's device wishlist.

**Expected outcomes**
* * *
*   A signed-in customer sees one wishlist on web, iOS and Android
*   Items saved in the app survive a new phone and a reinstall
*   Customers who never sign in keep the device wishlist they have today

#### **References**
* * *
Sources
*   [Wishlist contacts, 1 July to 20 September](context/fernhouse-wishlist-feedback.md)
*   [Fernhouse company context](context/fernhouse-context.md)
* * *
##   

## Requirements
* * *
**Account wishlist**
* * *
- [] On iOS and Android, a signed-in customer's wishlist is saved to the account rather than to the device
- [] The app shows the account wishlist, which is the same list web shows for that account

**First sign-in on a device**
* * *
- [] The items saved on the device join the account wishlist the first time the customer signs in on it

**Customers without an account**
* * *
- [] A customer who never signs in keeps the device wishlist as it works today

**Item limit**
* * *
**Open:** Whether an item saved on both the device wishlist and the account wishlist counts once or twice in the merge. Storefront settles it.

- [] The account wishlist holds up to `50` items
- [] The device wishlist keeps the `50`-item limit it has today for a customer who never signs in
- [] Where the device wishlist and the account wishlist together hold more than `50` items at the first sign-in, the account wishlist keeps the `50` most recently added
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **A signed-in customer keeps one wishlist in the app**
* * *
*   **Given** a customer with items saved in the app on iOS or Android
*   **When** they sign in
*   **Then** the app shows the account wishlist, with the items saved on that device joined into it
*   **And** the list the app shows is the list web shows for that account
* * *
- [] _Mark as done, if the criteria are met_

2\. **Saved items survive a new phone or a reinstall**
* * *
*   **Given** a customer whose items sit in their account
*   **When** they sign in on a new device or after reinstalling the app
*   **Then** the wishlist shows those items, with none of them lost
* * *
- [] _Mark as done, if the criteria are met_

3\. **A customer without an account keeps the device wishlist**
* * *
*   **Given** a customer who never signs in
*   **When** they use the wishlist in the app
*   **Then** it works without an account, saved on the device, as it does today
* * *
- [] _Mark as done, if the criteria are met_

4\. **The item limit holds when a device list joins an account list**
* * *
*   **Given** a customer whose device wishlist and account wishlist together hold more items than the account wishlist can keep
*   **When** they sign in on that device
*   **Then** the account wishlist stays within its item limit, keeping the most recently added items across both
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

*   **The iOS and Android app stores** - approve the release carrying the app change, which reaches app customers about a week later. Date: TBD...

#### Rabbit holes
* * *
Areas that could waste effort, create ambiguity or distract from the intended outcome.

*   Whether an item saved on both the device wishlist and the account wishlist counts once or twice in the merge, which Storefront settles

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   TBD...
* * *

Export-equivalent path: `export/001 - Story-wishlist-one-list-across-web-and-apps.md`

Artifact kind: Story. Quality: gate checked, with the six dimensions at or above floor. Requirements carry only the supplied hard values, `50` items and the `50` most recently added, in the source's own notation, and no criterion holds a value. Every supplied constraint landed either in Requirements or in the scope note below.

HVR self-scan: 0 hard blockers. Fixed: always-cut modifiers, and the draft carries no em dash, semicolon, Oxford comma or curly quote. Kept with reason: the fixed house labels `Given`, `When`, `Then` and `And` repeated verbatim in all four criteria, the house `TBD...` token in three Delivery slots, and the template's three lead lines in Delivery, all fixed by the Story scaffold.

Additions to strike if you disagree, none of them from your answer:

*   The `**Open:**` line on the item limit, asking whether an item saved on both lists counts once or twice in the merge, repeated in Rabbit holes. Your overflow rule fixes which items stay and not how duplicates count, so two developers could build two different lists from it
*   The `## Delivery` section, written because the app change is gated by store approval, which the team does not control and cannot date. Estimation and No-gos stay `TBD...` rather than guessed
*   The References block, carrying the two documents you pointed me at, since you supplied no other links

Next step: confirm the duplicate rule, then this is ready to hand to Storefront, with the account list owned by `accounts-service` and the change landing once on the app surface. Say the word if you want the task breakdown under this Story.