# Wishlist across devices and web: which artifact?

I detected two deliverables, a Bug (`$bug`) and a Story (`$story`). Please choose one and answer its fields below in one reply.

The sources lean one way. The company context says the app wishlist is saved on the device and the web wishlist is saved to the account. Teun confirmed on 2026-09-22 that this is how it was built and that nothing changed in 4.8.0 or 4.8.2. That makes the 412 contacts a gap in the design rather than a defect, so a bug report would have no expected behavior to cite. Maud's note calls it a bug, and Lotte has not decided whether the apps should change.

**0. How should I work this?**
- Quick: lean pass with smart defaults
- Deeper: full read of both context files and the complete phase flow

**1. Deliverable:** Story, Epic or Bug?

**2. If Story or Epic**
- Decision status: has Lotte approved changing the apps, or should I write it as a proposal awaiting her decision?
- Kind: one Story covering web, iOS and Android, or an Epic with child stories (for example sync for signed-in customers, bringing a device list into the account at sign-in and one shared 50-item limit)?
- Guests: the app wishlist works without an account today. Must it keep working for guests, and should their list survive a new phone or a reinstall?
- Merge at sign-in: when a device list and an account list together pass `50 items`, which items are kept, and is the customer told?
- Value and success: is the target measure fewer wishlist contacts, fewer complaint tags or something else?

**3. If Bug**
- Which source defines the expected behavior that the current build breaks? Without one, the report would contradict Teun's reply and the company context

**4. Anything I should not assume**
- For example, a change to the 50-item limit, analytics for `wishlist_item_added` or a release target such as 4.9.0
