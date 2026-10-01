## Wishlist intake question

<!-- Mode: Interactive intake | Template: Comprehensive question | Energy: Standard -->

Your message named two deliverables, `$bug` and `$story`, and the two sources you gave me point at different lanes. `context/fernhouse-wishlist-feedback.md` asks Storefront to fix the wishlist, while `context/fernhouse-context.md` records the app list as device storage and the web list as account storage. Storefront's reply says nothing about those lists changed in 4.8.0 or 4.8.2.

Answer the items below in one response and I will draft the artifact you pick.

**0. How should I work this?**
- Quick - lean pass with smart defaults and minimal back-and-forth
- Deeper - more context read, full phase flow at Standard or Deep energy

**1. Which artifact, and what decides it:**
- Bug - the wishlist was promised as one list, or as one that survives a reinstall, and current behavior departs from that promise
- Story - the device list and the account list are the intended build, and joining them is a product change with requirements of its own
- Epic - joining them is one initiative split across child stories
- Name the lane you want, and name the source that settles the promise

**2. Bug lane, if you choose it:**
- Unexpected behavior in one sentence, and the surface where it shows
- Expected behavior, plus where that expectation is written or was told to customers
- Steps to reproduce, on web, iOS and Android
- App versions and platforms where it shows, and the date it was first noticed
- Evidence: helpdesk contact IDs, screenshots or logs, and the wishlist figure you want cited
- Any 4.x release you believe changed wishlist behavior, since Storefront reports none did

**3. Story or Epic lane, if you choose it:**
- Create a new spec, or refine an existing one? Name the file if it exists
- Role and value, which becomes the Connextra line
- Which of the four contact reasons are in scope: 171 lost after a new phone or a reinstall, 138 saved in the app and invisible on web, 64 saved on web and invisible in the app, 39 blocked by the 50-item limit
- Requirements as hard values, and the surfaces, markets and app versions they cover
- The shared mechanism, if there is one, such as signing a device list into an account or merging two lists on first sign-in
- Merge rules: what happens to an existing device list on first sign-in, and what happens when two lists hold more than 50 items together
- Whether the app list must keep working without an account, and whether that sits in or out of scope

**4. Scope, value and success, for either lane:**
- Which of the four contact reasons are in scope, and which are out
- The outcome you want, and how CS would know it landed, for example the wishlist tag count per month
- Anything that must not change

**5. Sources, authority and the decision:**
- The governing source for current wishlist behavior, if it is newer than the company context
- Who signs off. Lotte was added to the thread and has not answered, and Storefront called the app behavior a product call
- Any upstream decision already taken that I should carry into the artifact

**6. Assumptions to challenge, confirm or correct each:**
- The app list is device-only, so a reinstall cannot bring it back and no server copy of a lost list exists
- The web list is account-only, so one customer can hold two lists and see only one at a time
- The 39 contacts reached the 50-item limit on one list, not a sync fault
- The 412-contacts figure is CS tagging, and the per-reason split is the only evidence of scale
- Storefront's reply reports that no release changed this behavior, rather than a decision to leave it alone
- Lotte's answer is still open, so no product direction exists yet

Export-equivalent path: `export/001 - intake-wishlist-bug-or-story-clarification.md`

Quality: gate checked. Completeness, Clarity, Actionability, Accuracy, Relevance and Mechanism Depth hold at or above floor for an intake question, with the six lanes of unresolved context named and no artifact drafted ahead of your answer.

HVR self-scan: 0 hard blockers. Fixed: always-cut modifiers on the second pass, and the draft carries no em dash, semicolon, Oxford comma or curly quote. Kept with reason: the bold intake labels and the `Quick - lean pass` hyphen-minus lead, both fixed by the Interactive Response Templates asset.

Summary: the clarification asks for one response covering the lane choice, the conditional Bug evidence, the conditional Story or Epic requirements, the scope split across the four contact reasons in the 412 contacts, the deciding authority, and six assumptions to confirm. The assumption carrying the most weight is the first one, because if the app list has no server copy then a Bug lane has no list to restore and the promise question decides everything. Answer the items and the chosen artifact follows as a new deliverable.