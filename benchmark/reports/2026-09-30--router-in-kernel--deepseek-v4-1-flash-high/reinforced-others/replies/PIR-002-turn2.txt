```markdown
<!-- Mode: Story | Shape: Story | Template: Story Template v0.101 -->

# Customer - Wishlist - Account sync

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
The app has always saved the wishlist on the device and `Web` has always saved it in the account, so a signed-in customer keeps two lists and loses the app one after a new phone or a reinstall.

This story makes the account list the wishlist in `iOS` and `Android` as well, and moves the items already saved on a device into the account the first time the customer signs in there.

#### Problem
* * *
Nothing about the wishlist changed in `4.8.0` or `4.8.2`, so the loss comes from where the list is stored rather than from a regression. A signed-in customer keeps one list on the laptop and a different one on the phone, and a new phone or a reinstall wipes the phone's list without the customer deleting anything.

CS tagged `412` wishlist contacts between `2026-07-01` and `2026-09-20`. `171` of them were about a wishlist gone after a new phone or a reinstall, and `39` about reaching the `50` item limit while holding a full list on one surface and a shorter one on the other.

#### Solution
* * *
Make the account the single home of the wishlist for every customer who signs in. The app in `iOS` and `Android` reads and writes the account list `Web` already shows, the items on a device move into it at the first sign-in there, and a customer who never signs in keeps the device list.

**Expected outcomes**
* * *
*   One wishlist per signed-in customer, in the app and on `Web`
*   Items collected on a device survive a sign-in, a new phone and a reinstall
*   Fewer wishlist contacts about items that moved or went missing

* * *
##   

## Requirements
* * *
**Account wishlist**
* * *
- [] A signed-in customer's wishlist in `iOS` and `Android` is saved to the account rather than the device
- [] The account wishlist is the list `Web` shows
- [] The first time a signed-in customer signs in on a device, the items saved on that device move into the account wishlist
- [] A merge adds the device items to the account wishlist and keeps the items already in it
- [] A customer who is not signed in keeps the device wishlist unchanged

**Item limit**
* * *
- [] The account wishlist keeps the `50` item limit
- [] When the device items and the account items together pass `50`, the account wishlist keeps the `50` most recently added items
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **A signed-in customer keeps one wishlist across the app and web**
* * *
*   **Given** I am signed in and using the app on `iOS` or `Android`
*   **When** I save an item
*   **Then** that item is on my wishlist on `Web`
*   **And** an item I save on `Web` is on my wishlist in the app
* * *
- [] _Mark as done, if the criteria are met_

2\. **Items saved on a device move into the account at the first sign-in**
* * *
*   **Given** I saved items in the app on `iOS` or `Android` before signing in
*   **When** I sign in there for the first time
*   **Then** those items are in my account wishlist, beside the items already saved to the account
* * *
- [] _Mark as done, if the criteria are met_

3\. **The account wishlist stays within its item limit when the lists merge**
* * *
*   **Given** the items on my device and the items in my account together are more than my account wishlist can carry
*   **When** I sign in and the lists merge
*   **Then** my account wishlist is within its item limit and holds the items I added most recently
* * *
- [] _Mark as done, if the criteria are met_

4\. **A customer without an account keeps the wishlist on the device**
* * *
*   **Given** I use the app on `iOS` or `Android` without signing in
*   **When** I save items
*   **Then** my wishlist stays on the device and works as it does today
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/001 - Story-customer-wishlist-account-sync.md`

Artifact kind: Story, at Quick energy. Not an Epic, because the four rules cover one feature area and one list, not an initiative split across child stories.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the Given, When, Then and And labels and the `Mark as done, if the criteria are met` line, which the house format fixes verbatim, and the repeated term wishlist, since the house wants one fixed term rather than a synonym.

Quality status: house grammar passes, carrying the story preamble, a divider after every content heading, `- []` requirement items with no Checklist label, and a `* * *` above each `##   ` spacer. All seven requirement items trace to a rule or value you supplied, and `50` is stated once in Requirements rather than inside a criterion. Each acceptance criterion traces to a requirement and names the surface it verifies. No Delivery section, so Acceptance criteria closes the file.

Additions you can strike:
- The merge is additive, so items already in the account list survive it
- I read "the same list web shows" as both directions, so an item saved on web is on the list in the app

Left out on purpose:
- Lotte's sign-off, because the house Story has no field for it. Say the word and I will carry it in the About prose
- The app-to-web (138) and web-to-app (64) counts and the monthly split. The 412 total, the 171 device-loss contacts and the 39 limit contacts sit in Problem as evidence
- The app-store release lag, which is a planning fact rather than an undated external dependency

Your four rules do not settle the device list after a merge, what a sign-out does, or a second device signing in. None of those is in the artifact.

Next step: correct anything above and I will revise, or say the word and I will break the requirements into tasks.