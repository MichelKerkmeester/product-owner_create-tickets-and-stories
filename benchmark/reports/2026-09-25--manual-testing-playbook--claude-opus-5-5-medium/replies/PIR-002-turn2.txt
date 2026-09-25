```markdown
# Customer - Wishlist - Account wishlist in the apps

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
This story saves the app wishlist to the customer's account on iOS and Android, so a signed-in customer has one wishlist in the apps and on web. Lotte, Head of Product, signed off the change on 2026-09-24.

The apps have saved the wishlist on the device since it first shipped, and web has always saved it to the account. Nothing broke in 4.8.0 or 4.8.2. This is a change to how the product works, not a fix.

### Problem
* * *
From the customer's side, the app and the website are one shop, but they have two wishlists. The app wishlist lives on the phone and is lost with a new phone or a reinstall. The web wishlist lives in the account and never shows up in the app.

CS tagged `412` wishlist contacts between `2026-07-01` and `2026-09-20`. That makes wishlist the third biggest tag after WISMO and returns, and the count grew every month: 118 in July, 139 in August and 155 in September up to the 20th. Of those contacts, 171 lost their wishlist after a new phone or a reinstall, 138 could not find their app items on web and 64 could not find their web items in the app. Another 39 hit the limit, and several of them did not know they had two separate lists. 23 of the contacts also carry a complaint tag.

### Solution
* * *
A signed-in customer gets one wishlist that belongs to their account, whichever surface they save from. Items a customer saved on a device before signing in are moved into that account list, so moving to the account never costs them what they already saved. Customers who use the app without an account keep the device wishlist, because it is how the wishlist works for anyone who never signs in.

#### **Expected outcomes**
* * *
*   Signed-in customers keep their wishlist when they change phones or reinstall the app
*   Customers find the same wishlist on web and in the apps
*   Fewer wishlist contacts reach CS
* * *
##   

## Requirements
* * *
**Platforms**
* * *
*   The change lands in the `iOS` and `Android` apps

**Account wishlist**
* * *
*   Applies to customers signed in to an account in the app
*   The app shows and edits the same account wishlist that web shows
*   The limit stays at `50 items`

**First sign-in on a device**
* * *
*   The first time a customer signs in on a device, the items saved on that device move into the account wishlist
*   When the device items and the account items together pass `50`, the account wishlist keeps the `50` most recently added
*   A product saved in both lists is kept once and counts once toward the limit

**Customers without an account**
* * *
*   The app keeps saving the wishlist on the device, as it works today
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **The same wishlist in the app and on web**
* * *
*   **Given** a customer is signed in to the app and on web
*   **When** they add or remove an item on either surface
*   **Then** the other surface shows the same wishlist the next time they open it
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **A new phone or a reinstall keeps the wishlist**
* * *
*   **Given** a signed-in customer has items in their wishlist
*   **When** they sign in on a new phone or after reinstalling the app
*   **Then** every item is there, with nothing to restore by hand
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **Items saved before signing in are kept**
* * *
*   **Given** a customer saved items in the app on a device without signing in
*   **When** they sign in on that device for the first time
*   **Then** those items are in their account wishlist, in the app and on web
*   **And** the app shows one wishlist, not two
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **A move that passes the limit keeps the newest items**
* * *
*   **Given** the device items and the account items together pass the limit
*   **When** the customer signs in on that device for the first time
*   **Then** the wishlist keeps the most recently added items up to the limit, whichever list they came from
* * *
- [ ] _Mark as done, if the criteria are met_

5\. **Customers without an account keep today's wishlist**
* * *
*   **Given** a customer uses the app without an account
*   **When** they save and remove items
*   **Then** the wishlist works on that device as it does today
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/002 - Story-customer-wishlist-account-wishlist-in-apps.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

I wrote this as a **Story**, using the requirements you gave: one account wishlist, items moving over on the first sign-in, the 50-item limit and today's behaviour for customers without an account.

**Quality:** the key rules pass. All your values are in Requirements, including `50 items` and keeping the 50 most recently added items. Every acceptance criterion traces back to a requirement, and none of them repeats a number. There's no Delivery section because you didn't ask for one and nothing in the Story is left open. There are no References because no links were supplied.

**Additions to check.** You didn't state these, so strike them if they're wrong:
- A product saved in both lists is kept once and counts once toward the limit
- The Problem section uses CS's contact numbers and the note that nothing changed in 4.8.0 or 4.8.2 from Teun's reply. The date of Lotte's sign-off (2026-09-24) is worked out from "yesterday"

**Gaps before this is split into tasks.** I left these out rather than guess:
- What happens when an account holder signs out in the app? Do they see an empty device wishlist, keep a copy of the account wishlist or something else?
- The 171 customers who already lost a wishlist aren't covered. The app never saved those items anywhere else, so this Story can't bring them back.
- No target release is set. App changes take about a week to reach most customers.

If you answer the sign-out question, I'll add it as a requirement and an acceptance criterion.