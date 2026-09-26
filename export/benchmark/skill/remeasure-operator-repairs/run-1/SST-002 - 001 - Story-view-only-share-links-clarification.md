I'll create a new PRD for view-only share links from Kofi's design notes of 2026-09-15. Before drafting, I need the decisions below in one reply.

**Artifact kind:** The notes cover four surfaces: the Share panel switch and link settings, the plan limits with the Team Admin workspace-wide off control, the viewer page and opening the link in the iOS and Android apps. Should this be one Story for the Sharing team, or an Epic with those parts as child stories?

**Role and value:** Whose story is it? My reading is a member with edit access who wants to share a page with people outside the workspace without inviting each one, so that readers get to the page without signing in. Is that right, or should the viewer or the Team Admin (Mireille) lead?

**Approval status:** Kofi's notes come from a design review with Lena and Caio. Apart from the sub-page question, is everything in them agreed scope, or is any part still a design proposal?

**Sub-page inheritance:** Lena has not decided whether sub-pages inherit the link, and no date is set. My plan is to scope the Story to a single page, as the frames do, and add an Open line on the Duplicate requirement, because Duplicate is the one part of the viewer that depends on the answer. The Delivery section would then list the question under Rabbit holes and the security review as an undated external dependency. Does that match what you want, or should sub-pages stay out of the Story entirely?

**Gaps in the notes:** The notes do not cover these cases. For each one, should I leave it as an open question or mark it out of scope?

1. A Plus or Team workspace that moves to Free while it has more than 3 active links, or links set to expire after 7 or 30 days
2. What a signed-out viewer sees in the iOS or Android app when the link opens there. The notes say the app opens but not what it shows
3. What a viewer gets when they open a link that has expired or been turned off, before the page loads. The notes give copy only for someone who already has the page open

**Evidence and links:** Can you send the ClickUp or design-file URLs for `Share / View-only link`, `Share / Link settings` and `Shared page / Viewer`? Should analytics events be in scope? If so, the Data team has to review the tracking plan before client work starts.
