Round one of the intake for a process board on how a damaged-item refund moves between the customer, CS and the warehouse. Nothing is written yet.

**What I have so far**
* Type: process with three lanes (Customer, CS agent, Warehouse operator), because the question is who does what and where the work changes hands. Captured
* Entry: the customer reports damage with a photo through the help form. Captured
* Exit: the refund is released to the original payment method. Captured
* Decisions: CS checks the photo, approves clear damage and asks for a second photo when it is unclear. Captured
* First glance: the handoff to the warehouse, drawn as the approval that sends a claim to the warehouse queue. Captured from your request
* Source: the support runbook, as current behavior. The under 20 euro pickup skip is a proposal because the pilot is not live
* Target: the existing file `<test-file-key>`, as a new section beside what it holds. A named file needs no `create_new_file`, so the Fernhouse Product plan is not a write input. I'll read the file once and name it at the gate
* Not asked yet: the runbook is silent on a photo that shows no damage, a second photo that is still unclear and an inspection that does not match the customer's photo. Those come in round three

**Reader and outcome**
Reading: no source names a reader. The board goes into the Product plan, so it is most likely for the product team.
Question: who reads this board and what should they be able to decide afterwards?
Recommended: the product team, who can then see where a claim leaves CS for the warehouse and what each team does at that point.
Why: the handoff is the highlight you asked for, so the reader is someone deciding about that crossing.

**What the board must not do**
Reading: the runbook mixes today's process with a pilot that is not live.
Question: should the board show the under 20 euro pilot?
Recommended: leave the pilot off the board and name it on the `Left out:` line as a proposal. The claims table gets a single store with one edge from the CS decision, and the source line says every decision writes to it.
Why: a pilot that is not live drawn as a step would read as current behavior, and four logging edges would crowd a 12 node lane budget.

**Dials**
Reading: nothing says how the board is read.
Question: which detail level, audience and reading distance?
Recommended: Balanced, Mixed and Laptop. Steps carry short bodies for the form fields (order number, photo, short description) and the timings (CS answers within 1 working day, pickup booked for the next working day, refund within 5 working days of the inspection).
Why: the timings and form fields are what a reader would otherwise need the runbook for.

Take the recommended answers, or correct any of them?