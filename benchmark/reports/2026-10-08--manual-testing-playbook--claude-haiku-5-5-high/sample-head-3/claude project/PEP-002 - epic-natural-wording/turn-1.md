The brief groups its dependency by area, not by platform, which bears directly on your split question. Conflict handling is still open, so the first reply is one consolidated question, with no draft.

```markdown
# Epic - Platform - Offline mode: clarification needed

I can draft the Epic once you answer the points below. Please reply to all of them together.

**1. Child story split:** Should the child stories follow Oskar's four areas (offline reading, offline editing and creation, sync on reconnect, offline indicator and storage settings), or split per platform (iOS, Android, Desktop)?

- My lean is the four areas. The brief's dependency splits by area: reading and the indicator can start now, while editing and sync wait for Joana's decision.
- A per-platform split would repeat the blocked sync work in three stories.
- Platform differences would sit inside each area story as criteria. Is that enough, or should one platform get its own story?
- Desktop wraps the web client in a native window, so its offline storage may differ from iOS and Android. Should Desktop storage get its own story?
- iOS and Android ship every two weeks with a 7-day rollout, while Desktop picks up web client changes with no release. If the sync decision changes protocol v3, that gap may favour a platform split for the sync stories.

**2. Conflict decision:** Joana decides conflict handling on 2026-10-09, tomorrow. The options sit in the #sync-eng thread, which I have not received.

- Should I draft now, with the editing and sync stories marked as waiting on that decision, or wait until it lands?
- Please paste the options from the #sync-eng thread. Without them, the sync stories can name the decision but not its options.

**3. Target:** The brief sets Q1 2027 for all four areas. If the conflict decision slips, should only the sync stories move, with reading and the indicator keeping Q1 2027?

**4. References:** Which links should the References block carry: the brief, the #sync-eng thread, Marta's `lost-edit` tickets or others? Send the links, or say none can be shared.

**5. Assumptions to check:** I assume Web and the Support console stay out of scope, as the brief states. Tell me if either has moved.
```

Export-equivalent path: `export/NNN - Epic-offline-mode-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

I have not drafted the Epic yet. The split and the open conflict decision both change its child stories, so this reply holds to one question. Once you answer, I will render the Epic as a new Deliverable Block. Quality status does not apply to a clarification.