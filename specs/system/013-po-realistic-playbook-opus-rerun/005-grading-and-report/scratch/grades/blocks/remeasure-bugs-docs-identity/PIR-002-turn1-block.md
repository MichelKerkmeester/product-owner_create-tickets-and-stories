Welcome! Let's create exactly what you need.

Please answer everything below in one reply. I'll draft once I have your answers.

I detected two deliverables in the request: `$bug` and `$story`. Choose one primary deliverable and complete its fields below.

**What the two context files say:**

- CS (Maud, 2026-09-21) counts 412 wishlist contacts from 2026-07-01 to 2026-09-20 and asks Storefront to fix it as a bug
- Storefront (Teun, 2026-09-22) says the app wishlist has always been saved on the device and the web wishlist on the account, and that nothing changed in 4.8.0 or 4.8.2
- Whether the apps should change is a product call. It sits with Lotte, who has not answered yet

**0. How should I work this?**

- Quick - lean pass with smart defaults, minimal back-and-forth
- Deeper - take more time, read more context and apply the full phase flow

**1. Deliverable type:**

- Bug - a defect report. It needs observed behavior that departs from what the wishlist was built to do. Teun says the current behavior is as built, so name the part you see as a defect and share any reproduction steps, devices or app versions beyond the CS summary
- Story - a PRD for a wishlist that follows the customer across web, iOS and Android
- Epic - the same change split into child stories, for example accounts-service, iOS, Android and web

**2. Decision status (Story or Epic):**

- Has Lotte approved moving the app wishlist to the account, or should the PRD be written as a proposal for her to decide on?

**3. Scope and requirements (Story or Epic):**

- Signed-out app customers can use the wishlist today without an account. Should they keep a device-only list or be asked to sign in, or do you want something else?
- When a customer signs in, should their existing device list merge into the account list, replace it or stay separate?
- Both lists hold up to 50 items. What happens when a merge would take the list past 50?
- Are lists already lost after a phone change or reinstall in scope, or out of scope?

**4. Success and references:**

- What does success look like: fewer wishlist contacts in the helpdesk (with a target number if you have one), or only the behavior change?
- Any Figma files, links or task IDs to carry into References?

**5. Assumptions to challenge:**

- I will not assume that lost lists can be recovered, that Lotte has decided or that signed-out app customers lose the wishlist. Tell me if any of these should change
