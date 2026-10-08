```markdown
I'll create your bug report. Before drafting, I need the unresolved details below in one response.

**Scope:** The ticket covers Pay now on Android 8.12.1. Should the report also cover Pay at property bookings? Maren could not tell whether those show the same total, so I can add it as a check or leave it out.

**Expected behavior:** I plan to write the expected total as the amount charged, €405.00 in the 3-night case, city tax included. Should the confirmation screen also show a City tax line, as the payment step does, or only the total?

**Current status:** The ticket is dated 2026-09-21, and the product context names 8.12.1 as the current Android build as of 2026-09-18. Does the defect still reproduce on the current build, and has a fix or hotfix shipped?

**Reproduction and frequency:** Confirm the steps Maren ran: property 40217, 2 adults, 2 nights, the Pay now rate plan, the test card, then the confirmation screen. Has the 2-night case failed on every attempt across more than one account, device or session? If not, Frequency stays Not provided.

**Environment:** Which model and Android version does the Guest Support test phone run? The guest's device and OS are not in the ticket.

**Severity and discipline:** Should Severity be High, as the ticket priority is, or Critical? For the title, is FE right for a Guest app screen, or does the defect sit in a service, which would make it BE?

**Evidence:** The guest's screenshot is referenced in the ticket but is not in the context folder. Can you add it, along with any screenshots from Maren's tests?

**Validation:** The 2-night threshold rests on Maren's single 2-night and 1-night tests on one Android phone, plus the 14 chats. What other evidence supports it, and what should the report avoid calling a root cause?
```

Export-equivalent path: `export/NNN - bug-android-confirmation-city-tax-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

The bug report comes next, once you answer. The ticket already gives the observed behavior: the €387.00 total on the confirmation screen against the €405.00 charge, the €18.00 city tax (2 adults, 3 nights, €3.00 each per night), the Android 8.12.1 platform and the iOS comparison. Your answers fill the remaining gaps.

Quality status: not scored, since no artifact is drafted yet.