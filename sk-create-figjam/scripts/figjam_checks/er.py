# ───────────────────────────────────────────────────────────────
# COMPONENT: ER PROFILE
# ───────────────────────────────────────────────────────────────

"""An entity-relationship diagram, parsed here because the shared extractor
drops the fields of an entity that carries a display alias.

The generator draws an entity with attributes as a table and one without as a
plain rectangle, puts each key as a badge and draws `--` solid and `..` dotted.
Styling is silently dropped, and an alias inside a relationship line fails to
parse, so both are refused here.
"""
from __future__ import annotations

import re

from .common import content_lines, id_problems, length_problems, raw_problems

MAX_ENTITIES = 9
MAX_RELATIONSHIPS = 12
MAX_ATTRIBUTES = 10
DIRECTIONS = {"LR", "TB", "TD"}
LEFT_ENDS = {"||", "|o", "}o", "}|"}
RIGHT_ENDS = {"||", "o|", "o{", "|{"}
CARDINALITY = re.compile(r"^(\S{2})(--|\.\.)(\S{2})$")
CARDINALITY_TOKEN = re.compile(r"\s\S{2}(?:--|\.\.)\S{2}\s")
ENTITY_OPEN = re.compile(r'^([^\s\[{]+)(\["([^"]*)"\])?\s*\{$')
ENTITY_ALONE = re.compile(r'^([^\s\[{]+)(\["([^"]*)"\])?$')
RELATIONSHIP = re.compile(r'^(\S+)\s+(\S+)\s+(\S+)\s*(?::\s*(.*))?$')
ATTRIBUTE = re.compile(r'^(\S+)\s+([A-Za-z][\w]*)((?:\s+(?:PK|FK|UK)(?:\s*,\s*(?:PK|FK|UK))*)?)(\s+"[^"]*")?$')
STYLING = re.compile(r"^(classDef|class|style)\s", re.I)


def check_er(block_text: str) -> tuple[list[str], int, int]:
    problems = raw_problems(block_text)
    lines = content_lines(block_text)
    if not lines or lines[0][1] != "erDiagram":
        return problems + ["an ER diagram starts with the line erDiagram"], 0, 0
    entities, attributes, relationships, current = {}, {}, [], None
    for number, text in lines[1:]:
        if current is not None:
            if text == "}":
                current = None
                continue
            attribute = ATTRIBUTE.match(text)
            if not attribute:
                problems.append(f"line {number}: an attribute is written type name, then PK, FK or UK, "
                                f"then a quoted comment: {text!r}")
                continue
            attributes[current].append((attribute.group(1), attribute.group(2), attribute.group(3)))
            continue
        if STYLING.match(text) or ":::" in text:
            problems.append(
                f"line {number}: styling, which the generator drops: "
                "colour entities through the hybrid workflow"
            )
            continue
        if text.lower().startswith("direction "):
            direction = text.split()[1].upper()
            if direction not in DIRECTIONS:
                problems.append(f"line {number}: direction {direction}, an ER diagram runs LR or TB")
            continue
        opened = ENTITY_OPEN.match(text)
        if opened:
            current = opened.group(1)
            entities[current] = opened.group(3) or current
            attributes[current] = []
            continue
        if "[" in text and CARDINALITY_TOKEN.search(text):
            problems.append(f"line {number}: an alias inside a relationship line fails to parse: "
                            "declare the alias on the entity and use the id here")
            continue
        relationship = RELATIONSHIP.match(text)
        if relationship and CARDINALITY.match(relationship.group(2)):
            relationships.append((number, *relationship.groups()))
            continue
        alone = ENTITY_ALONE.match(text)
        if alone:
            entities.setdefault(alone.group(1), alone.group(3) or alone.group(1))
            attributes.setdefault(alone.group(1), [])
            continue
        problems.append(f"line {number} is outside the ER grammar the generator draws: {text!r}")
    joined = set()
    for number, left, cardinality, right, label in relationships:
        for end in (left, right):
            if "[" in end:
                problems.append(f"line {number}: an alias inside a relationship line fails to parse: "
                                "declare the alias on the entity and use the id here")
                continue
            entities.setdefault(end, end)
            attributes.setdefault(end, [])
            joined.add(end)
        left_end, middle, right_end = CARDINALITY.match(cardinality).groups()
        if left_end not in LEFT_ENDS or right_end not in RIGHT_ENDS:
            problems.append(f"line {number}: the cardinality {cardinality} is not one Figma documents, "
                            "such as ||--o{ or }o..o{")
        label = (label or "").strip()
        bare = label.strip('"')
        if not bare:
            problems.append(
                f"line {number}: the relationship {left} to {right} has no label: "
                f"name it from {left}'s side"
            )
        elif " " in bare and not (label.startswith('"') and label.endswith('"')):
            problems.append(f"line {number}: the label {label!r} has more than one word: put it in double quotes")
        problems += length_problems(f"line {number}: the relationship", bare)
    for entity, alias in entities.items():
        problems += id_problems(entity, "entity id") + length_problems(f"entity {entity}", alias)
        fields = attributes[entity]
        if len(fields) > MAX_ATTRIBUTES:
            problems.append(f"entity {entity} lists {len(fields)} attributes, at most {MAX_ATTRIBUTES}: "
                            "keep the columns a reader needs")
        if fields and not any("PK" in keys for _, _, keys in fields):
            problems.append(f"entity {entity} lists attributes but no PK")
        if len(entities) > 1 and entity not in joined:
            problems.append(f"entity {entity} takes part in no relationship")
    spellings = {}
    for fields in attributes.values():
        for kind, _, _ in fields:
            spellings.setdefault(kind.lower(), set()).add(kind)
    for kind, variants in sorted(spellings.items()):
        if len(variants) > 1:
            problems.append(f"the type {kind} is spelled {' and '.join(sorted(variants))}: use one spelling")
    if not entities:
        problems.append("the diagram has no entity")
    if len(entities) > MAX_ENTITIES:
        problems.append(f"{len(entities)} entities, at most {MAX_ENTITIES}: split by domain")
    if len(relationships) > MAX_RELATIONSHIPS:
        problems.append(f"{len(relationships)} relationships, at most {MAX_RELATIONSHIPS}: split by domain")
    return problems, len(entities), len(relationships)
