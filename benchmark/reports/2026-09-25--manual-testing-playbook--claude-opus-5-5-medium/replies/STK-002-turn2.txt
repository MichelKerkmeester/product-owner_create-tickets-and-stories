I've updated the task with your decisions in the same file.

Path: `export/001 - task-date-picker-stay-limits.md`
Verified: read-back succeeded; 183 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality:** It's still one FE task for iOS, Android and web, with no parent. Your answers are added and everything else is unchanged. After the read-back I removed a reason I had added for testing en-US, because you didn't give one.

**Summary:** The About section now says the Search squad takes this into the 8.13.0 train. It also lists search-service as not changing in this task, since its own 30-night check stays as the backstop. A new group 9 asks QA to sign off groups 1 to 8 on iOS, Android and web, each in en-GB and en-US. For web, I added sign-off on both desktop and mobile web, because they show the calendar differently.

Things you may want to check:
- **8.13.0 and web:** the app release trains cover iOS and Android. Web deploys on its own several times a day, so it may need its own release note or a feature flag if it has to go live alongside 8.13.0.
- **Where the limits come from:** leaving search-service as it is only works if the apps and web can already read the 30-night and 365-day limits from it. The task still says they come from search-service settings and aren't hard-coded, and I haven't checked whether the apps and web can read them today.
- **Disabled days:** it's still not defined what happens when a guest taps a disabled day, meaning a past day or one more than 365 days out.

If you want this in ClickUp, I can push it once you say so.