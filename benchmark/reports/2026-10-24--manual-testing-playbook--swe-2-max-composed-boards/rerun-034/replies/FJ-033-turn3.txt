Both diagrams passed the pre-write check and composed. Nothing is on the board yet.

**What changed from the plan:**
- **Two boards:** a sequence diagram holds at most 5 participants, and your request names 6 parties (three apps, the sync platform, the store and Apple's push service). So it splits into two boards in the same file instead of shrinking one.
- **Assumed:**
  - **Type:** sequence, since no gateway was named.
  - **Order:** the change is stored first, then the iPhone is woken. Your description doesn't give the order.
  - **Push sender:** the sync platform sends the wake itself.
  - **Labels:** "Change Store" and "Wakes the app" are my wording.
- **Left out:** Android and the other Loomlist services.

**Gate**

- **Question:** which parts carry a block change from every app, and how does a sleeping iPhone get woken?
- **Outcome:** leadership can see that every change is stored and that iPhones are reached through Apple's push service.
- **First glance:** Sync Platform, which receives every change and sends the wake.
- **Second glance:** Change Store, where each change is kept.
- **Last glance:** Apple Push, the outside hop to the iPhone.
- **File:** the existing FigJam file `<test-file-key>`, in the plan you named. I haven't verified the plan, and an existing file keeps the plan it was made in.
- **Writes:**
  - Board 1, "1. Block change saved": 5 participants and 4 messages.
  - Board 2, "2. Sleeping iPhone woken": 3 participants and 2 messages.
  - Each has a title, subtitle, key and source line, at Laptop reading distance.
- **Extensions:** none.
- **Calls:** `create_session`, two `use_figma` and one or two `get_figjam` read-backs. That is 4 to 5 calls, which matters if the file sits on a Starter plan, where Figma allows six a month.
- **Rollback:** delete the two board sections the write returns, which I'd do only after you say yes to the deletion.

Write both boards?