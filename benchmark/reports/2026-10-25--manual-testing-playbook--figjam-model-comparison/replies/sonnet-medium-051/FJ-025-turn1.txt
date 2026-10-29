Here is how I read the request so far:

* Type: sequence, because the question is the order of messages between parties
* Parties: GuestApp, BookingApi, PaymentProvider and PartnerHub
* Target: file `<test-file-key>` in Roamstay Product, added as a new section beside what the file already holds, with no new file and nothing already on it changed
* Source: your summary of the payments brief, with its status (current behavior, approved direction or proposal) not yet stated
* Assumed: the message to the partner hub is fire-and-forget, because the brief lists no answer from it

**Question 1: reader and outcome**
Reading: the brief names no reader. The board answers "in what order do the app, the booking API, the payment provider and the partner hub exchange messages when a guest pays at checkout?"
Question: who reads the board, and what should they decide or do after reading it?
Recommended: the payments team, who check the call order and the status codes
Why: the source is a payments brief, so the order of calls and the codes carry the board

**Question 2: detail, audience and reading distance**
Reading: the brief states 201 and 402 but gives no endpoint paths or provider call names
Question: which detail level, audience and reading distance?
Recommended: Balanced, Engineer, Laptop, with plain verbs in the labels unless you send the paths
Why: an engineer audience keeps status codes in the labels, and I will not invent a path the brief does not state

**Question 3: scope and what the board must not do**
Reading: the brief covers two paths, a confirmed booking and a declined card. A sequence draws one path per diagram, because a branch would render flat. You asked for one new board as a destination, not for a single diagram.
Question: what must the board not do, and are two diagrams right?
Recommended: two diagrams in the same file, "1. Checkout payment, happy path" and "2. Checkout payment, declined card", with retries, timeouts and partner hub failures left out
Why: both paths are in the brief and none of those three is

Take the recommended answers, or correct any of them?