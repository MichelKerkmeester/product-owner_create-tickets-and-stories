I've read your brief and checked your Figma account. Before I draw anything I need answers to three questions, and the first is about where the board goes. Nothing has been written yet.

**What the brief gives me**
- **Diagram type:** a sequence diagram fits the brief. It shows the order in which four parties send messages: the guest app, the booking API, the payment provider and the partner hub.
- **Message order:** the app posts the booking. The API holds the room, asks the payment provider to authorise the card, confirms the hold, tells the partner hub and answers the app with 201.
- **Gaps:** the brief doesn't say what the provider sends back, what happens when a card is declined, or whether "holds the room" is a call to another system or work inside the API. I'll ask about these after the questions below.

**1. Where the board goes**
- Reading: your account has three Figma plans: <figma-plan-3> (Starter, View seat), <figma-plan-1> (Pro, Full seat) and <figma-plan-2> None is called "Roamstay Product". I can only write into a new file I create or a board this work already drew, and nothing shows that this work drew <test-file-key>.
- Question: which should I do?
  - **New file:** create it in <figma-plan-1> and leave it in drafts with no project.
  - **Existing file:** first read <test-file-key> to see whether this work drew it. If it didn't, I stop there and won't write into it.
- Recommended: a new file in <figma-plan-1> drafts.
- Why: it's the fallback you named, your Full seat on that plan isn't capped at six tool calls a month like the Starter View seat, and you can move it into the Roamstay project later.

**2. Who reads it and what they do next**
- Reading: the brief describes the order of the calls but doesn't say who the board is for.
- Question: who reads this board, and what do they decide after reading it?
- Recommended: engineers and product people working on Roamstay checkout, checking which party makes each call and in what order before they change the flow.
- Why: a sequence diagram answers "in what order", and that question belongs to whoever builds or changes these calls.

**3. What the board must not do**
- Reading: the brief covers only the path where everything succeeds.
- Question: should the board stay on that path, or also show failures such as a declined card or a hub that can't be reached?
- Recommended: the success path only, with the declined card listed as not drawn.
- Why: a failure path drawn from guesses would show behaviour the payments brief doesn't state.

If you skip a question, I'll go with its recommendation and mark it as assumed. You can still correct it when I play the brief back before anything is written.