I've written the view-only share links spec as a Story. The sub-page question stays open inside it, as you asked.

Path: `export/002 - Story-view-only-share-links.md`
Verified: read-back succeeded; 167 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `TBD...` twice in Delivery (a fixed house placeholder, allowed for these slots).

**What's in it:**
- **Requirements:** Every value in Kofi's notes is copied exactly, in his own groups: Share panel, Plans and What a viewer sees. That includes the 60-second cutoff, the Free limit of 3 active links, the expiry options and all the exact wording. A fourth group, Sub-pages, holds the open question.
- **Open question:** Lena decides `Do sub-pages inherit the link?` with the security reviewer. Until then the Story only promises that the link opens the page it was turned on for, and no acceptance criterion depends on the answer. The same question, with the design and engineering positions, is repeated under Rabbit holes, which is why the Story has a Delivery section. Estimation and No-gos say TBD.
- **Acceptance criteria:** Seven criteria in three groups (Share panel, Plans, Viewer). They describe what users get and leave the exact values in Requirements.

**Assumptions to check:**
- The notes aren't marked as approved. The Story treats them as the scope to build and doesn't say who signed off. If Lena hasn't approved them, tell me.
- I treated the security review as input to Lena's decision, not a release sign-off. If it has to happen before release, it belongs under External dependencies.
- The Team Admin switch for the whole workspace is in this Story. The notes don't say where that switch lives, so the Story doesn't say either.
- Nothing supplied a design file link, so the About section names the three frames without linking them.
- These are left out, since nothing supplied them: analytics events for the Data team's tracking plan, and translations of the new wording into the other five languages.

Only one addition is mine rather than from the notes: acceptance criterion 5 says a client can read the page "in a browser", which frames the test on the web. Remove it if you don't want that.

The earlier question file, `001`, is unchanged. Next, you could fill in Estimation and No-gos once the team has sized the work.