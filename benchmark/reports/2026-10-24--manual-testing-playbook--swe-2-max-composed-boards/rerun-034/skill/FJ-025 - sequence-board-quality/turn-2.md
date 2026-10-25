The model passes the pre-write check and both boards compose. This is the write gate. Nothing has been written to Figma.

* **Check:** diagram 1 has 4 participants and 7 messages. Diagram 2 has 3 participants and 6 messages, because the partner hub never appears on the decline path.
* **Composed:** the code for each board is under the 50,000-character limit for one call.
* **Colour:** a sequence takes no accent colour, so nothing is marked.

**Question:** in what order do the guest app, the booking API, the payment provider and the partner hub exchange messages at checkout payment?

**Outcome:** an engineer can read the checkout calls in order, with paths and status codes, for an authorised card and for a declined one.

**First glance:** "Authorise card", the call that decides which path checkout takes.

**Second glance:** "Authorised" on board 1 and "Declined" on board 2. These are the answers that lead to "Confirm the hold" or "Release the hold".

**Last glance:** "Notify partner hub", the message that sends no reply and doesn't hold up the 201.

**Plan and file:** Roamstay Product, as you supplied it. The file is the existing FigJam file `<test-file-key>`, so no new file is created.

**Writes:** two composed boards, each with a title, subtitle, key and source line, at Laptop reading distance.
* Board 1, "1. Checkout payment, authorised card", has 4 participants and 7 numbered messages
* Board 2, "2. Checkout payment, declined card", has 3 participants and 6 numbered messages

Each board lands 400 pixels to the right of what is already on the page, so no existing content is covered.

**Extensions:** none.

**Calls:** `create_session` on the file, two `use_figma` calls (one per board) and one or two `get_figjam` read-backs. That is about five calls. A Starter plan or a View or Collab seat is limited to six tool calls a month, and read tools count against that.

**Rollback:** I delete the one board section each write returns, through `use_figma`, and only after you say yes to that deletion. Nothing else on the page is touched.

**Left out:** the webhook confirmation and the `payment_pending` state from the Roamstay context file, because your description governs. The source line on both boards says so.

Do you want me to write these two boards to that file?