<figma-url>
<figma-url>
Read-back: board 1, 4 of 4 participants and 7 of 7 messages. Board 2, 3 of 3 participants and 6 of 6 messages, labels read visually, first glance: Authorise card, start here: 1. Checkout payment, authorised card
Left out: the webhook confirmation and the `payment_pending` state, `context/roamstay-context.md` describes them and your message doesn't, so your description governs. Both boards' source lines say so.
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Both boards sit in the existing file, 400 pixels to the right of what was already there. Each write returned no warnings, and its counts matched the model.

* **What `get_figjam` confirmed:** every participant, every message, each message's two ends, its order and its arrow head. The two self-messages and the async message to the partner hub read as drawn.
* **What I only saw on screenshots:** the message labels, because `get_figjam` returns no connector text. The screenshots show every label matching the model.
* **Figma skills:** I couldn't load Figma's `figma-use` and `figma-use-figjam` skills before the writes, because this session has no skill or resource reader. The composer code ran unchanged, and nothing in the file was touched beyond the two new sections.
* **One cosmetic finding:** the subtitle on board 2 wraps "engineers" onto a second line. It overlaps nothing, and I left it because fixing it means a recompose and a delete of the old board, each on its own yes.
* **Repo and plan:** no model, Mermaid or image file is left in the repository, and nothing was saved to `export/`. The plan is Roamstay Product as you gave it, and I couldn't verify it from the file.

To undo, I delete the two board sections, `73:562` and `74:954`, once you say yes to the deletion.