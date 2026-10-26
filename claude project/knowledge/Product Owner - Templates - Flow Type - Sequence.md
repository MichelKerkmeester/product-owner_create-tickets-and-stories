# Product Owner - Templates - Flow Type - Sequence

A sequence shows who sends what to whom, in order. Neither the composer nor Figma's generated fallback draws much of Mermaid's sequence grammar, and the generator drops what it cannot draw in silence, so a sequence model here is written in the subset the board actually shows.

---

## 1. WHEN TO USE

**The reader's question:** in what order do these parties exchange messages?

- An API call flow, from an app through services to a store and back
- A sign-in or payment handshake
- Events passed between producers and consumers, where the order is the point

Use an architecture for which parts exist without time order, a process for decisions and people, and a state diagram for one thing changing state.

---

## 2. WHAT THE BOARD DRAWS

```text
sequenceDiagram
    title Checkout payment
    participant GuestApp
    participant BookingApi
    GuestApp->>BookingApi: POST /bookings
    BookingApi-->>GuestApp: 201 Created
```

| Arrow | Draws | Use for |
|---|---|---|
| `->>` | Solid with a closed head | A request or a call |
| `-->>` | Dotted with a closed head | A return or a reply |
| `-)` | Solid with an open head | A fire-and-forget message |
| `--)` | Dotted with an open head | An asynchronous return or callback |

Every participant draws as the same rectangle in the `neutral` role, at the top of its lifeline and again, smaller, at the foot, and the participant id is the text the board shows. Each message is a straight line in its own row with its label beside the sender and a pin in the `marker` role beside the sender's lifeline carrying its number. A request is a solid line and a reply a dashed one, both in the connector colour with a closed head, and an async message or reply takes the async colour with an open head, so an async message reads apart from a reply by its head as well as its colour. Assets - Flow Board Design names the swatch each role draws and the colour of each line. A message to itself loops out and back, and a message that skips a participant runs across the lifeline between.

### What the board does not draw

Notes, activations and the `+` and `-` shorthand, every fragment (`loop`, `alt`, `opt`, `par`, `critical`, `break`), coloured `rect` regions, `box` groups, `autonumber`, links, aliases written `as "Name"` and type annotations such as `@{"type": "database"}`. Each is refused, because the board would show the messages without the thing that gave them meaning. The composer numbers every message already, so `autonumber` is never needed. When a loop or a branch matters, compose the plain sequence and add a note through Templates - Flow Hybrid Workflow naming the message numbers it covers.

---

## 3. RULES

Check these rule by rule before the gate:

- **The four arrows only.** `-x` and `--x` lose their cross, `->` and `-->` draw no head, and a two-way arrow hides which side starts
- **Every message labelled,** at most 40 characters, with no semicolon, which the generated fallback turns into a full stop
- **Readable participant ids** of 3 to 20 letters and digits, camelCase or PascalCase, such as `AuthServer`, never a cryptic `a` or `p1`
- **Every participant declared** once there are three or more, so the board keeps their order, and every declared participant sends or receives something
- **No dropped feature,** as listed above, and `participant` rather than `actor`
- **At most 5 participants and 12 messages,** the house diagram guide's sequence budget
- The shared rules: no emoji, markup or literal `\n`

Judged by hand:

- **`->>` for a request and `-->>` for its return** covers most diagrams. Add an async arrow only when the message really is fire-and-forget. A message the caller sends without waiting for an answer, such as telling another system an event happened, is async even when the brief does not say fire-and-forget
- **Labels carry the specifics that make a sequence useful,** such as the path, the status code or the key field: `POST /bookings`, `402 Declined`
- **One path per diagram.** A failure path is its own diagram, because `alt` would render flat. When the user asked for one diagram, the failure path is named under `Left out:` and offered as a second diagram in the playback

---

## 4. BUDGET AND SPLITTING

Over 5 participants or 12 messages, split into the happy path and a detail, such as the failure or the retry. Put both in one file, named after the path each shows. When the user asked for one diagram or one board, cut the detail instead, name it under `Left out:` and offer the split as the alternative in the playback. At `Meeting screen` distance message labels drop to 32 characters. At `Wall` distance the budget drops to 3 participants and 8 messages, with labels at 25 characters, as the reading distance dial in Templates - Flow Mode Section 4 sets out.

---

## 5. COLOUR, ZONES AND NOTES

None in the model. The arrow sets each message's colour and line, and the composer numbers the messages. A sequence takes no zone line. A `%% focus: <number>` line may name the one message the first glance lands on. It is a comment, so the model stays styleless. Architecture and sequence take no style line. A `%% focus:` line marks their first glance, and it is refused where it names nothing. Notes are the one extension left, and Figma ranks sequence low for extensions, so add them only when the request asks for them.

---

## 6. WRITING THE BOARD

The model is placed into Assets - Flow Board Composer and one `use_figma` call draws the board, as Templates - Flow Mode Section 6 sets out. On the generated fallback, `generate_diagram` takes `name`, `mermaidSyntax` and `userIntent` with no `useArchitectureLayoutCode`.

---

## 7. READ-BACK

Count participants and messages, and check each message's label, direction and arrow style against the model. On a composed board each message is the connector named `edge:<from>-><to>:<n>`, so its name gives both parties and its order, and the participant drawn again at the foot of a lifeline is not counted twice.

```text
Read-back: 4 of 4 participants, 9 of 9 messages
```

---

## 8. PATTERNS AND EXAMPLE

- Assets - Flow Templates - Sequence holds a request and response chain and an event handoff
- Examples - Flow - Sequence draws a checkout payment from an API brief
