I've treated this as an ER diagram for Flow Mode. Two gaps need answers before I build the model. One is in what you sent me and one is in where you asked me to write.

**What your note already settles**
- Six tables: guests, bookings, payments, properties, rooms and rate plans
- Relationships:
  - a guest makes many bookings
  - a booking reserves exactly one room and exactly one rate plan
  - a booking holds many payments
  - a property offers many rooms and publishes many rate plans
- Two groups. Partner: properties, rooms and rate plans. Guest: guests, bookings and payments.

**1. The schema itself**
- Reading: I only have your summary of the schema note. It gives no key names and no columns. I won't make up a field, and "the few columns support asks about" doesn't name any.
- Question: Can you paste the schema note (or migration or model file), and list the columns support asks about for each table?
- Recommended: Paste the note, and I'll keep each table's primary key, its foreign keys and only the columns you name.
- Why: Without them each card would show only the table name. That doesn't answer a support agent's question.

**2. Where the board goes**
- Reading: You asked for "a new board in our Roamstay Product plan" and also to write into the existing file `<test-file-key>`. Those are two different targets. Flow Mode only composes into a new file or a board this work already wrote, and I didn't write that file.
- Question: Should I create a new FigJam file in the Roamstay Product plan, or add a new section next to the existing content in `<test-file-key>`?
- Recommended: Add a section to `<test-file-key>`. I'd read it first, place the diagram 400 px to the right of what's there and leave everything else alone. If you'd rather keep to the rule, I'll create a new file in the plan instead.
- Why: You named that file explicitly, and putting the diagram beside the existing content means nothing already there gets touched.

**3. Who reads it**
- Reading: The mention of support suggests the readers are support agents tracing a guest's booking and payments back to a property.
- Question: Is that the reader, and will they read the board on a laptop?
- Recommended: Yes, support agents, read on a laptop, with simple labels in plain verbs.
- Why: That's the audience your column choice implies.

Once you answer, I'll play back the full reading. Nothing gets written to Figma until you say yes at a separate write step.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.