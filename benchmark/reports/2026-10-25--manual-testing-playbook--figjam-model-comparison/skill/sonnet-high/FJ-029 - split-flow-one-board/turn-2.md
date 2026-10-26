The model passes the pre-write check and both boards compose, so this is the write gate. Nothing has been written yet.

**Assumptions I'm taking.** I took the playback's yes as confirming the reading. The three questions got no answer, so I'm proceeding on my recommendations. The boards leave out expired codes, network failures, Google-specific steps, Team billing and what invited teammates see. The flow is split into two boards. The reader and question are the product and design teams asking where a new person can choose or get stuck. Say so if you want any of these changed.

**What the boards say**

1. **Sign up** has 6 nodes and 6 connectors.
   * Landing page → Sign up with email or Google → Verify the email code → "Code correct?"
   * Yes leads to "Email verified", which is the hand-off.
   * No leads to "Wrong code error with resend", which returns to the code screen.
2. **Workspace setup** has 6 nodes and 6 connectors.
   * "Email verified" → "Free or team plan?"
   * Free goes to "Name the workspace". Team goes to "Invite teammates by email, or skip" and then to "Name the workspace".
   * Then "Pick a template or start blank" → "Editor opens with welcome tip".

**Glance lines**

* **First glance:** the "Code correct?" decision on board 1 and the "Free or team plan?" decision on board 2. Each takes the pink outline.
* **Second glance:** the two branches off each decision, which are the wrong-code loop and the Free and Team paths.
* **Last glance:** the key and the source line under each board.

**The write**

* **Target:** the existing file `<draft-file-key>`. I add two new sections beside what is already there and change nothing existing. No new file is created, so the Loomlist Product plan and the Barter drafts fallback don't come into play. If the file turns out to be unwritable, I stop and ask first.
* **Extensions:** none.
* **Calls, about six:**
  1. `create_session`
  2. One read of the file before the write, so the read-back can confirm the existing content is untouched.
  3. Two `use_figma` calls, one per board, written in order so "1. Sign up" lands on the left.
  4. One or two `get_figjam` read-backs.
  * A Starter plan or a View or Collab seat allows only six tool calls a month, so this could use the whole allowance.
* **Rollback:** delete the two board sections this write returns, and only after a separate yes that names them. Nothing already on the file is deleted.

Do you want me to write both boards into `<draft-file-key>` as described?