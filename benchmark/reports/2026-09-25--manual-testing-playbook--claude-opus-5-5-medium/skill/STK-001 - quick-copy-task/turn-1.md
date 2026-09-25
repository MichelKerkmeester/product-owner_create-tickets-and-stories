I've written the task and saved it.

Path: `export/001 - task-free-shipping-banner-copy.md`
Verified: read-back succeeded; 40 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality:** It clears every quality floor. The part that relies most on judgement is the title's discipline code, explained below.

The task changes the English banner copy to `Free shipping over €50` for NL, BE, DE and FR and `Free shipping over £45` for the UK, on Web, iOS and Android. The thresholds stay the same. The context file says the English lines are the source for every locale, so the task also asks for the same shorter wording in `nl-NL`, `nl-BE`, `fr-BE`, `de-DE` and `fr-FR`.

**Choices I made without asking, so you can change them:**
- **Title:** I used `FS - PROMO - …` with no surface in the title. The change covers Web, iOS and Android. The naming rule only lets back-end and data tasks drop the surface, so this is an exception. If the team wants separate FE tasks per platform, this should become a parent task with subtasks.
- **What I added:** the translation update, checking that each translated banner fits on one line, and flagging any language that still wraps before release. You didn't ask for any of these. Delete them if the translations are tracked somewhere else.
- **"Small phones":** the context doesn't give a screen width, so the checks refer to the phone widths where the current copy wraps. They don't name a pixel value.
- **Where the copy is stored:** the context doesn't say whether it's in the app builds or on the server. If it's in the apps, most app customers will see the new copy about a week after the release that includes it.

Want me to push this to ClickUp? I'll only do it once you say yes.