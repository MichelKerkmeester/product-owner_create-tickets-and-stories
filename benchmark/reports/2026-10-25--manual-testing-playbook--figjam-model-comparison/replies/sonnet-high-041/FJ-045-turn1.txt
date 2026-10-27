The target file is empty (one page, no sections), so a same-titled board isn't a risk. Before I model anything I need one answer on a source conflict. Nothing has been written to the board.

**Replay of what's settled**
- Question: how a Fernhouse customer starts a return in the app (captured)
- Entry and exit: the order list, then either the confirmation with a QR code or Contact support after 30 days (captured)
- Window: 30 days from delivery, which matches the Return window in `context/fernhouse-context.md` (captured)
- Step order: order list, order detail, reasons, drop-off or courier choice, confirmation. I'm using the order you listed them in (assumed, rung 3 of the ladder)
- Contact support: shown on the order detail in place of Start a return once the window has passed (assumed, because your note doesn't say which screen shows it)
- Target: the existing file `<draft-file-key>` in the Fernhouse Product plan, which you named. The board lands as a new section and nothing else on the file changes

**Question 1: which source governs?**
Reading: `context/fernhouse-context.md` (updated 2026-09-18, after app 4.8) says "There is no self-serve return today". The customer contacts CS, and a CS agent creates the return in Admin. Your description has a Start a return button in the app. The doc predates the next app release (4.9.0), so either the flow shipped since or it is not live yet.
Question: is this in-app flow current behavior, or an approved or proposed direction?
Recommended: current behavior shipped after the context doc, with your app and returns doc governing the screens.
Why: you are reading the app and the returns doc directly, and the context doc cannot see a release made after it was written. If it is not live, the board is labelled as a proposal instead.

**Question 2: reader, outcome and what the board must not do**
Reading: the board is for the people who own or review the return experience, to check the app against the returns doc.
Question: who reads it, and what should they be able to decide? What should it leave out?
Recommended: the Post-purchase and CS teams, to confirm every step and the 30-day cut-off. It leaves out everything after the confirmation (the parcel handover, the warehouse check and the refund).
Why: your question stops at "starts a return", and the context doc puts the rest in other teams' hands.

**Question 3: does the QR code appear on both methods?**
Reading: a QR code fits a drop-off point, where the carrier scans it. Your note doesn't say what a courier pickup confirmation shows.
Question: do both methods end on the QR confirmation?
Recommended: yes, one confirmation screen for both, drawn after a merge dot.
Why: you described a single confirmation. If the courier confirmation differs, it needs its own node.

If you'd rather skip these, say "use the recommended answers". I'll mark each one assumed and replay it before the write gate.