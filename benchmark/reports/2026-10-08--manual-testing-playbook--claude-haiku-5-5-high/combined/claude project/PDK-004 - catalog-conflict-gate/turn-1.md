# Activity emails reference page: clarification

I'll create a new reference page for the six activity emails. Before I draft, I need the unresolved decisions below in one response.

- **Purpose and audience:** Who will read this page: engineers on notifications-service, Product, Support, or a mix? What should readers be able to look up, decide or do after reading it?
- **Domain and detail:** Should the page include template IDs, job names (`digest-sender`, `summary-sender`) and template variables, or only the product rules?
- **Source set:** I plan to use `context/loomlist-notification-spec.md` and `context/loomlist-email-template-inventory.md` for the six emails, and `context/loomlist-context.md` for background. Confirm that set, or name any other source I may use.
- **Authority and conflicts:** Which source controls each item below?
  - Daily digest send time: the spec says 08:00 in the recipient's local time. The inventory says 07:00 UTC for every recipient.
  - Digest item limit: the inventory caps the digest at 20 items grouped by page. The spec sets no cap. Should the page include the cap?
  - Digest in the background page: the "Receive email" flow in `loomlist-context.md` names mention, comment reply, share, invite and summary emails, but not the daily digest. Confirm that the spec governs the digest, and I will flag the gap to Elif.
- **Document status:** Should the page describe current behavior (what the inventory records as live), approved direction (what the spec states), or a mix with each claim labelled? The spec was last edited 2026-07-14 and the inventory 2026-09-11, so the newer date does not settle it.
- **Scope and shape:** Should the page cover only the six emails, leaving out push, reminders, sign-in, receipts, plan emails and the digest time choice that the spec marks as not planned? I suggest a Catalog with one entry per email (EM-01 to EM-06) and shared fields, because readers will look up and compare entries. Confirm that shape, or ask for a Behavior reference if the page should explain how the emails interact.
- **Layout:** Is the page bound for ClickUp, which keeps spacer headings, or for a file export?
- **Validation:** Which claims are you unsure of? I will label them unknown rather than present them as fact.

Export-equivalent path: export/NNN - doc-activity-emails-reference-clarification.md

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Quality status: Doc gate blocked, no draft yet. Source safety needs attention because the digest send time conflicts between the spec and the inventory. Document status and shape are still open.

All six emails appear in both specs, so the sources cover every subject the page would describe. The blocking conflict is the digest send time, where the two sources differ on both the hour and the time zone basis. Once you answer, the reference page comes next.