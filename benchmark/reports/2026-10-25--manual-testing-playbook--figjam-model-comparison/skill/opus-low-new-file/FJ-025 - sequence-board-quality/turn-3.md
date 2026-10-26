I didn't recommend a plan last time, so here is one, sent as the write confirmation. Nothing is written until you say yes.

**Question:** What order do the calls run in when a guest pays at Roamstay checkout, and where does a declined card leave the flow?
**Outcome:** One sequence diagram with the success path ending in 201 and the decline path ending in 402.

**What the reader sees first, next and last**
- First: the split where the card is authorised or declined
- Next: the success path (confirm the hold, tell the partner hub, return 201)
- Last: the decline path (release the hold, return 402)

**Where it goes**
- **Plan:** <figma-plan-1> (Pro, Full seat, admin). I'm recommending it because your email is on getbarter.com and this is the work plan where you're an admin. Its members will see the board as soon as it's created
- **File:** a new FigJam file called "Roamstay checkout payment". The existing file `<test-file-key>` stays untouched

**What gets drawn:** One framed sequence diagram. Participants: Guest app, Booking API, Payment provider, Partner hub. There are 6 messages, 3 Booking API self-calls and an authorised-or-declined split. It carries a title, a source line ("Payments brief") and a key. There are no extra notes or pins.

**Calls it will use:** `create_new_file`, then one `use_figma` to draw the diagram, then `get_figjam` to check the result. The plan lookup is already done. Pro plans with Full seats aren't held to the six-calls-a-month limit.

**Undoing it:** the board lives in its own new file, so deleting that file removes everything. I'll only delete it if you say yes to a question that names it.

**Shall I create "Roamstay checkout payment" as a new FigJam file in the <figma-plan-1> plan and draw the diagram?**