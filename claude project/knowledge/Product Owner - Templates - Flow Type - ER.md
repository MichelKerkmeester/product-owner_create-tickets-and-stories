# Product Owner - Templates - Flow Type - ER

An ER diagram shows which entities exist, the fields that matter on each and how they relate. The composer draws each entity as a card in the `neutral` role, its name in bold above one line per field with its keys first, and each relationship as a line with no arrow, its cardinality marked at both ends and repeated in words in the label.

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

On the board each end of a relationship carries Figma's crow's-foot mark for its cardinality, so a reader sees which side is the many, and the label reads the verb and then the two ends in words, such as `makes (1 to 0..n)`. An identifying relationship is a solid line and a non-identifying one dashed, and the key names both. A `%% zone: <label>: <entity>, <entity>` line draws a tinted section around the entities of one domain.

---

## 3. RULES

Check these rule by rule before the gate:

- **Documented cardinalities only,** each end one of `||`, `|o`, `}o` or `}|` on the left and `||`, `o|`, `o{` or `|{` on the right
- **No alias inside a relationship line,** which fails to parse. Declare the alias on the entity and use the plain id in relationships
- **Every relationship labelled,** a label of two or more words in double quotes, at most 40 characters
- **Attributes in the documented form,** at most 10 per entity, and an entity with attributes marks its `PK`
- **One spelling per type,** never `string` beside `String`
- **No styling,** which neither route draws. Group a domain with a `%% zone:` line instead
- **Every entity in a relationship** once there is more than one, and entity ids camelCase or PascalCase. Figma's own examples write `LINE_ITEM`, but its universal rules say an underscore can break routing, so write `LineItem` with an alias when the board should read `Line Item`
- **At most 9 entities and 12 relationships,** the house diagram guide's general budget
- The shared rules: no emoji, markup or literal `\n`

Judged by hand:

- **Relationships first, attributes second.** The right cardinality matters more than a full column list
- **Keep the 5 to 10 columns a reader needs.** The full schema belongs in the migration
- **Solid for a required parent, dotted for a loose link,** chosen on purpose
- **Labels are verbs from the left entity's side,** such as `makes` or `"is booked in"`
- **Mark `FK` on every foreign key,** because "which field joins these?" is the question readers ask most

---

## 4. BUDGET AND SPLITTING

Split by bounded context, such as guests and bookings in one diagram and properties and rates in another, each in the same file. When the user asked for one board, cut the lowest-priority part instead, name it under `Left out:` and offer the split as the alternative in the playback. When two diagrams share an entity, draw it in both and say so in the reply. At `Meeting screen` distance labels drop to 32 characters. At `Wall` distance the budget drops to 6 entities and 8 relationships, with labels at 25 characters, as the reading distance dial in Templates - Flow Mode Section 4 sets out.

---

## 5. COLOUR, ZONES AND NOTES

Colour by domain is what Figma ranks highest for ER, and the model carries it: a `%% zone:` line names a domain and lists its entities, and the composer tints a section around them. An entity sits in one zone at most, and an entity in no zone sits outside every section. Sections never overlap: when the entities of two zones would interleave, the composer stacks the sections one above the other, and a board that still has zones on top of each other is refused before anything is drawn. Annotations on a column, such as a soft-delete field, go on through the pins and legend recipe in Templates - Flow Hybrid Workflow. A `%% focus: <id>` line may name the one node the first glance lands on. It is a comment, so the model stays styleless.

---

## 6. WRITING THE BOARD

The model is placed into Assets - Flow Board Composer and one `use_figma` call draws the board, as Templates - Flow Mode Section 6 sets out. On the generated fallback, `generate_diagram` takes `name`, `mermaidSyntax` and `userIntent` with no `useArchitectureLayoutCode`. The generator strips the zone lines.

---

## 7. READ-BACK

Count entities, relationships and attributes, and check each relationship's two ends, the cardinality on each end and its label.

On a composed board read each end's mark against the label, which carries both ends in words, and check the line is solid or dashed as the model draws it. The attributes are the lines of each entity card. The right cardinality matters more than a full column list, because it is the part a reader decides on.

A relationship has no arrow, so the arrow rule in Templates - Flow Mode Section 7 does not apply here. Figma's connector cap carries a mark for each of the four cardinalities, named `ERD_EXACTLY_ONE`, `ERD_ZERO_OR_ONE`, `ERD_ZERO_OR_MORE` and `ERD_ONE_OR_MORE`. The composer sets them on every relationship, while no live read has shown the generated route drawing them yet. Where those caps read plain, the read counts the two ends and the label and says the cardinality went unread.

```text
Read-back: 4 of 4 entities, 3 of 3 relationships, 11 of 11 attributes
```

---

## 8. PATTERNS AND EXAMPLE

- Assets - Flow Templates - ER holds a one-to-many core, a junction and an aliased entity
- Examples - Flow - ER draws the booking model from a schema note
