I'll create a new reference page for the six Loomlist activity emails, EM-01 to EM-06. Before drafting, I need the unresolved decisions below in one response:

**Authority & conflicts:** The two notification sources disagree on when the daily digest goes out, and neither page says it governs the other, nor does the newer edit date settle it on its own. Which should the page state?

*   `loomlist-notification-spec.md` (Lena, edited 2026-07-14) says EM-01 goes out "every day at 08:00 in the recipient's local time", with local time taken from the profile time zone
*   `loomlist-email-template-inventory.md` (Mateo, edited 2026-09-11) says "Daily at 07:00 UTC", and the `digest-sender` job hands the batch to the email delivery provider at 07:00 UTC
*   Options: the spec is the rule and the inventory describes a bug, or the inventory is what ships and the spec is out of date
*   A third option: the page shows both as an open discrepancy, with Lena as the decision owner

**Document status:** Should the page describe current behavior (what notifications-service sends today) or intended product behavior from the spec? That choice also decides whether the digest time above reads as fact or as a gap.

**Purpose & audience:** Who reads this page and what do they use it for? Engineers changing a template need template IDs, variables, jobs and the pre-change checks. PMs, Support or writers need triggers, timing, who receives each email and the opt-out rules.

**Domain & detail:** Should the engineering-only detail from the inventory go in? That covers template names such as `tpl_digest_v4`, variables, the 20-item digest cap, the 140-character mention excerpt, the 14-day invite token, the `digest-sender` and `summary-sender` jobs, last test-send dates and the "Checks before changing a template" list.

**Source set:** You said "so far". Are more sources coming, such as a Settings > Notifications design or real email copy, or should I work from these three files only? `loomlist-context.md` stays background, as you asked.

**Scope & shape:** Two things to confirm:

*   Scope: should the page, like both sources, leave out push notifications, reminders, digest-time choice and sign-in, receipt and plan emails, or list them under "Not covered"?
*   Shape: I'd suggest a Catalog, with one entry per email ID and a shared-rules section for guests, locale fallback, the footer and the mention-over-reply rule

If the page should explain how the emails interact instead, it would be a Behavior reference. Which do you want?
