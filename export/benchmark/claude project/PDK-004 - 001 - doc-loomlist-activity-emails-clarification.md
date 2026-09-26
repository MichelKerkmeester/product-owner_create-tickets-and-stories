I'll build the Loomlist activity emails reference page. Before drafting, I need the unresolved decisions below in one response:

**Source set:** You said "so far": are more sources coming, such as the Settings > Notifications screen spec, the push notifications page or a newer digest decision? If so, please share them now, and otherwise I'll work from the notification spec and the template inventory, using loomlist-context.md only for background terms (roles, locales, services).

**Authority & conflicts:** One conflict needs a decision:
- EM-01 daily digest send time: Lena's spec (Product, 2026-07-14) says "every day at 08:00 in the recipient's local time"
- Mateo's inventory (notifications-service, 2026-09-11) says the `digest-sender` job hands the batch to the email delivery provider "daily at 07:00 UTC"
- These match only for recipients in a UTC+1 time zone, neither page says it overrides the other, and the newer date does not settle it
- Which one should the page state?
- Or should it show both: the spec as intended behavior, the inventory as what the service sends today, and a flag on the gap?

**Document status:** Should the page describe what Loomlist sends today (current behavior), what the Notifications team intends (approved direction) or both, labelled where they differ?

**Purpose & audience:** Who reads this page, and what do they use it for? For example: support agents answering "why did I get this email", PMs and designers writing tickets, or engineers changing a template.

**Domain & detail:** Only the inventory has the engineering detail: template names and versions, variables, the 20-item digest cap, the 140-character mention excerpt, the 14-day invite token, the `digest-sender` and `summary-sender` jobs, last test-send dates and the checks to run before changing a template. Should all of it go in, only some or none?

**Scope & shape:** Both sources leave out sign-in, receipt and plan emails, push notifications, reminders and a choice of digest time. Should the page leave those out too?

For shape, "reference page" suggests a Catalog: one entry per email, EM-01 to EM-06, with shared fields and the rules that apply to all six. Or do you want a Behavior reference built around who gets which email and when?

**Validation:** Is there any claim in either source you already know is out of date or not yet shipped?
