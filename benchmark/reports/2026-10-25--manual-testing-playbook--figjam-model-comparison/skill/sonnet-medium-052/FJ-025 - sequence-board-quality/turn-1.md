Settled so far from your message and the brief:

- Type: sequence, since you want the order of the calls
- Parties: guest app, booking API, payment provider and partner hub
- Authorised path: the app posts the booking (room, dates, card token), the API holds the room for 15 minutes, asks the provider to authorise the card, confirms the hold, tells the hub (booking id, dates) and answers the app with 201
- Declined path: the card is declined, the API releases the hold and returns 402
- Target: file <test-file-key> in the Roamstay Product plan. The board lands as a new section beside what the file holds, with no new file and nothing already there changed
- Labels: the brief gives no URL for the booking post, so its label states what it carries instead of a path

Three questions are still open. Nothing is drawn or written yet.

Question 1: reader, outcome and dials

Reading: the request names no reader. The brief is a payments brief, and its details (card token, 201, 402) are the kind an engineer checks.
Question: who reads this board, and what should they be able to do afterwards?
Recommended: engineers on checkout and payments, who can check the call order and the 15 minute hold against the code. Balanced detail, engineer audience, laptop reading distance.
Why: the labels carry message contents and status codes, which only that reader needs.

Question 2: what the board must not do

Reading: the request sets no limits. The brief lists the calls and says nothing about timeouts, retries or what happens when the hold runs out.
Question: what should the board refuse to show?
Recommended: nothing beyond the calls the brief lists. That means no hold expiry at 15 minutes, no retries and no hub message on a decline.
Why: a call the brief never states reads as fact once it is on the board. I will name these under Left out.

Question 3: one path per diagram

Reading: a sequence draws one path per diagram because an alt box renders flat. Your brief has two paths, and you did not ask for a single diagram.
Question: should both paths go on the board?
Recommended: two boards in the same file, "1. Checkout payment, card authorised" (4 parties, 7 messages) and "2. Checkout payment, card declined" (3 parties, 6 messages). The authorised board is the one to read first. The alternative is the authorised path alone, with the decline listed under Left out.
Why: both boards sit well inside the budget of 5 parties and 12 messages, and the decline stays visible.

Take the recommended answers, or correct any of them?