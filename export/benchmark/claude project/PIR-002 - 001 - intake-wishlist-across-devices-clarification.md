Before I draft, I need one answer covering everything below. You sent both `$bug` and `$story`. I can only produce one primary deliverable, so the first choice is which one.

**What the two sources say**

- Company context: the web wishlist is saved to the account and needs sign-in
- The app wishlist is saved on the device and works without an account, and both hold up to 50 items
- CS (Maud, 2026-09-21): 412 wishlist contacts from 1 July to 20 September
- The split: 171 lost after a new phone or reinstall, 138 app to web, 64 web to app, 39 hit the 50-item limit
- CS calls it a bug and asks for "the wishlist is the same everywhere"
- Storefront (Teun, 2026-09-22): the app has saved the wishlist on the device since it first shipped, and nothing changed in 4.8.0 or 4.8.2
- Teun calls it a product decision and added Lotte
- Open: Lotte has not answered, and nobody has picked it up

A bug report needs expected behavior the product was built to have. So far both sources describe the wishlist working as built.

**0. How should I work this?**

- Quick: lean pass with smart defaults
- Deeper: full pass over both sources

**1. Deliverable:**

- Bug: only if you have a case that breaks the current design
- For example, a signed-in web wishlist that lost items, or an app list lost without a reinstall or a new phone
- If so, give the steps to reproduce, the platform and app version, and the evidence
- Story: a change so the wishlist follows the customer across devices and between app and web
- Epic: the same change split into child stories, if you want sync, merging and the limit delivered separately

**2. Decision status (Story or Epic):**

- Has Lotte approved changing how the app saves the wishlist, or should I write it as a proposal for her to decide on?

**3. Requirements (Story or Epic):**

- Signed-in app customers: should their wishlist save to the account and match web?
- Guests in the app: keep a device-only wishlist, ask them to sign in to save, or something else?
- Existing device wishlists: merge into the account at first sign-in after the update, and what happens if the merged list would go over 50 items?
- The 50-item limit (39 contacts): keep it, raise it, or leave it out of scope?
- Customers who already lost a list: in scope, or accepted as unrecoverable?
- Any target release, such as app 4.9.0?

**4. Evidence and links:**

- Helpdesk tag or view, Figma, related tickets, or a written decision from Lotte

**5. Assumptions to challenge:**

- I am assuming web keeps requiring sign-in for the wishlist, and that the fix lives in accounts-service plus both apps
- Correct me if either is wrong
