---
title: "FigJam Type - ER"
description: "Entities, their key fields and how they relate, drawn as a FigJam ER diagram with documented cardinalities, labelled relationships, aliases on declarations only and a nine-entity budget."
contextType: implementation
importance_tier: important
trigger_phrases:
  - "figjam er diagram"
  - "entity relationship figjam"
  - "data model figjam"
  - "schema diagram"
version: 1.0.0.0
---

# FigJam Type - ER

An ER diagram shows which entities exist, the fields that matter on each and how they relate. The generator draws an entity with fields as a table with key badges and one without as a plain box.

**Loading Condition:** CONDITIONAL, when the Flow route draws an ER diagram
**Purpose:** The grammar, rules, budget and read-back for an ER diagram
**Pairs With:** `assets/templates/er.md`

---

## 1. WHEN TO USE

**The reader's question:** which entities exist, what fields do they carry and how do they relate?

- A data model a story or a doc depends on, such as bookings and rooms
- The tables behind a feature, read from a schema or a migration
- A domain model agreed before the build, drawn from a product doc

Use an architecture for services and stores, and a state diagram for one entity's lifecycle.

---

## 2. WHAT THE BOARD DRAWS

```text
erDiagram
    Guest ||--o{ Booking : makes
    Guest {
        string id PK
        string email UK
    }
```

- A relationship is `A <cardinality> B : label`, read from A's side
- `--` draws a solid line, for a child that cannot exist without its parent, and `..` a dotted one, for a looser link
- An attribute is `type name`, then any of `PK`, `FK` and `UK` joined by commas, then an optional quoted comment
- An alias names an entity for the board: `Property["Listed Property"] { ... }`

| Cardinality | Means |
|---|---|
| `\|\|--\|\|` | Exactly one to exactly one |
| `\|\|--o\|` | Exactly one to zero or one |
| `\|\|--o{` | Exactly one to zero or more |
| `\|\|--\|{` | Exactly one to one or more |
| `}o--o{` | Zero or more to zero or more |
| `}\|--\|{` | One or more to one or more |

The same ends work with `..` in place of `--`.

---

## 3. RULES

The check enforces:

- **Documented cardinalities only,** each end one of `||`, `|o`, `}o` or `}|` on the left and `||`, `o|`, `o{` or `|{` on the right
- **No alias inside a relationship line,** which fails to parse. Declare the alias on the entity and use the plain id in relationships
- **Every relationship labelled,** a label of two or more words in double quotes, at most 40 characters
- **Attributes in the documented form,** at most 10 per entity, and an entity with attributes marks its `PK`
- **One spelling per type,** never `string` beside `String`
- **No styling,** which the generator drops. Colour domains through the hybrid pass
- **Every entity in a relationship** once there is more than one, and entity ids camelCase or PascalCase. Figma's own examples write `LINE_ITEM`, but its universal rules say an underscore can break routing, so write `LineItem` with an alias when the board should read `Line Item`
- **At most 9 entities and 12 relationships,** sk-design-diagram's general budget
- The shared rules: no emoji, markup or literal `\n`

Judged by hand:

- **Relationships first, attributes second.** The right cardinality matters more than a full column list
- **Keep the 5 to 10 columns a reader needs.** The full schema belongs in the migration
- **Solid for a required parent, dotted for a loose link,** chosen on purpose
- **Labels are verbs from the left entity's side,** such as `makes` or `"is booked in"`
- **Mark `FK` on every foreign key,** because "which field joins these?" is the question readers ask most

---

## 4. BUDGET AND SPLITTING

Split by bounded context, such as guests and bookings in one diagram and properties and rates in another, each in the same file. When two diagrams share an entity, draw it in both and say so in the reply. At `Meeting screen` distance labels drop to 32 characters. At `Wall` distance the budget drops to 6 entities and 8 relationships, with labels at 25 characters, as the reading distance dial in `references/flow-mode.md` Section 4 sets out.

---

## 5. COLOUR AND THE HYBRID PASS

Colour by domain is the extension Figma ranks highest for ER, because Mermaid cannot do it: the status tint recipe in `references/hybrid-workflow.md` tints each entity's table. Annotations on a column, such as a soft-delete field, go on through the label and legend recipe.

---

## 6. CALLING THE TOOL

`generate_diagram` with `name`, `mermaidSyntax` and `userIntent`. No `useArchitectureLayoutCode`. The `fj` route cannot draw an ER diagram.

---

## 7. READ-BACK

Count entities, relationships and attributes, and check each relationship's two ends, the cardinality on each end and its label.

Read the cardinality from the end caps. Figma's connector cap carries a marker for each of the four cardinalities, named `ERD_EXACTLY_ONE`, `ERD_ZERO_OR_ONE`, `ERD_ZERO_OR_MORE` and `ERD_ONE_OR_MORE`, and the read compares each end's marker with the end the model drew. The right cardinality matters more than a full column list, because it is the part a reader decides on.

A connector with one marker and one plain end is never called reversed, and one with a marker at both ends is never called two-way, so the arrow rule in `references/flow-mode.md` Section 7 does not apply here. This check rests on the generator drawing ERD caps, which no live read has shown yet. Where the caps read plain, the read counts the two ends and the label and says the cardinality went unread.

```text
Read-back: 4 of 4 entities, 3 of 3 relationships, 11 of 11 attributes
```

---

## 8. PATTERNS AND EXAMPLE

- `assets/templates/er.md` holds a one-to-many core, a junction and an aliased entity
- `assets/examples/er-roamstay-stays.md` draws the booking model from a schema note
