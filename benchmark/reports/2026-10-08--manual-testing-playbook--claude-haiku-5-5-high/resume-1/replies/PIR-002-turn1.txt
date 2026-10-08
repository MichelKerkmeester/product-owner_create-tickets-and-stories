```markdown
# Wishlist sync clarification

Before I draft, I need the decisions below in one response.

**0. How should I work this?**
- Quick - lean pass with smart defaults, minimal back-and-forth
- Deeper - take more time, read more context and apply the full phase flow

**1. Deliverable type:** You asked for both, so choose one.
- Bug - defect report with evidence and reproduction steps
- Story - product requirements document in the Barter house format, for changing how the wishlist is stored

**2. Decision that gates both:** Storefront says the app wishlist is saved on the device by design, and web saves it to the account. Their reply says whether the apps should change is a product call, and it has not been answered. Which should apply?
- Apps move to the account, so one wishlist works everywhere
- Apps keep the device save, and the gap is documented for CS and customers
- Not decided yet, so this comes before any artifact

**3. Bug details (if Bug):** Which steps reproduce the loss on iOS 4.8.0 or Android 4.8.2 after a new phone and after a reinstall? What is the expected behavior? Which account state applies, guest or signed in?

**4. Story details (if Story):** Who is the customer, and what do they gain? Which requirements must hold? Do the requirements share one save mechanism, and which limits carry over, such as the 50 item cap?

**5. Scope:** Are the 39 contacts at the 50 item limit in scope, including the second list in the app? Are the 23 contacts with a complaint tag in scope?

**6. Assumptions to challenge:**
- Assumed: the 412 count and its four categories are accurate tag counts, not checked against the helpdesk
- Assumed: Storefront's account of how storage works is correct, not checked against the code
- Maud calls this a bug. Her ask is customer feedback, not a verified defect
```

Export-equivalent path: `export/NNN - intake-wishlist-cross-device-clarification.md`

Your `$bug` and `$story` commands conflict, so I asked one question instead of drafting. The question also asks for the decision Storefront marked as open, because whether this is a bug or a story depends on whether the apps should change. Once you answer, the artifact comes next as a new delivery.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.