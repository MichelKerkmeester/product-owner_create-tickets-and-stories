# Product Owner - Templates - Flow Type - Sequence

A sequence shows who sends what to whom, in order. The generator parses most of Mermaid's sequence grammar and then silently drops much of it, so a sequence model here is written in the subset the board actually shows.

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
| `->>` | Solid with a head | A request or a call |
| `-->>` | Dotted with a head | A return or a reply |
| `-)` | Solid with an open head | A fire-and-forget message |
| `--)` | Dotted with an open head | An asynchronous return or callback |

Every participant draws as the same rectangle, and the participant id is the text the board shows.

### What the generator drops

Notes, activations and the `+` and `-` shorthand, every fragment (`loop`, `alt`, `opt`, `par`, `critical`, `break`), coloured `rect` regions, `box` groups, `autonumber`, links, aliases written `as "Name"` and type annotations such as `@{"type": "database"}`. Each is refused, because the board would show the messages without the thing that gave them meaning. When it matters, generate the plain sequence and add it through Templates - Flow Hybrid Workflow: a labelled rectangle behind a group of messages stands in for a loop or a branch, and a numbered pin stands in for `autonumber`.

---

## 3. RULES

Check these rule by rule before the gate:

- **The four arrows only.** `-x` and `--x` draw the same as `->>` and `-->>` without the cross, `->` and `-->` draw no head, and a two-way arrow hides which side starts
- **Every message labelled,** at most 40 characters, with no semicolon, which the generator turns into a full stop
- **Readable participant ids** of 3 to 20 letters and digits, camelCase or PascalCase, such as `AuthServer`, never a cryptic `a` or `p1`
- **Every participant declared** once there are three or more, so the board keeps their order, and every declared participant sends or receives something
- **No dropped feature,** as listed above, and `participant` rather than `actor`
- **At most 5 participants and 12 messages,** the house diagram guide's sequence budget
- The shared rules: no emoji, markup or literal `\n`

Judged by hand:

- **`->>` for a request and `-->>` for its return** covers most diagrams. Add an async arrow only when the message really is fire-and-forget
- **Labels carry the specifics that make a sequence useful,** such as the path, the status code or the key field: `POST /bookings`, `402 Declined`
- **One path per diagram.** A failure path is its own diagram, because `alt` would render flat

---

## 4. BUDGET AND SPLITTING

Over 5 participants or 12 messages, split into the happy path and a detail, such as the failure or the retry. Put both in one file, named after the path each shows. At `Meeting screen` distance message labels drop to 32 characters. At `Wall` distance the budget drops to 3 participants and 8 messages, with labels at 25 characters, as the reading distance dial in Templates - Flow Mode Section 4 sets out.

---

## 5. COLOUR AND THE HYBRID PASS

Mermaid cannot colour a sequence. Annotations, phase regions, step numbers and distinct participant shapes are hybrid extensions. Figma ranks sequence low for extensions, so add them only when the request asks for them.

---

## 6. CALLING THE TOOL

`generate_diagram` with `name`, `mermaidSyntax` and `userIntent`. No `useArchitectureLayoutCode`.

---

## 7. READ-BACK

Count participants and messages, and check each message's label, direction and arrow style against the model.

```text
Read-back: 4 of 4 participants, 9 of 9 messages
```

---

## 8. PATTERNS AND EXAMPLE

- Assets - Flow Templates - Sequence holds a request and response chain and an event handoff
- Examples - Flow - Sequence draws a checkout payment from an API brief
