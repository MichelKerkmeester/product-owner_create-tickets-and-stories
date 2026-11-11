#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: HUMAN VOICE HARD-BLOCKER LINTER
# ───────────────────────────────────────────────────────────────

"""Deterministic Human Voice hard-blocker linter for Product Owner replies.

Usage:
  hvr_lint.py <file>      ->  prints JSON {file, clean, violations:[{type,count,samples}]}
  hvr_lint.py --self-test ->  proves the lists follow the card and the named exceptions hold

Exit codes:
  0   the report was printed, whether or not the reply is clean
  1   the reply file could not be read, reported by Python's own traceback
  2   the card could not be read or one of its lists came out empty
  64  no reply file was given

This is a code gate, never a model judging its own prose: every check below is
a fixed string or a narrow regex, so the result cannot be talked past. The
word list, the phrase list, the metaphor list and the copula list are read from
`references/hvr-core.md` at run time, the file this system loads on every turn
specifically so those terms stay in view while writing. A term added there is
linted here with no second edit, which a retyped copy could not promise: it had
already lost "a world where" from Section 5. The format validator reads the same
sections out of the same file for the same reason. The punctuation bans of
Section 2 are patterns written below, because they are shapes and not terms.

Five departures from the card are named in the configuration section, each with
its reason: a US spelling of a listed word, the fixed prefix of a phrase that
carries a placeholder, a metaphor that Section 3 already counts as a word, two
copula verbs that are ordinary in backlog prose and the list of words the card
allows when literal, which the word list never held.

Sections 6 (setup language) and 7 (generalisation fixes) are not read. They
hold thirty terms the format validator does block, and this linter never has, so
a reply with "In summary" or "Studies show" in it grades clean here. Reading
them would change the counts of every report already graded, so that choice is
left to the owner of the playbook and is not made by this change.

`references/hvr-core.md` also names narrow, system-granted exemptions to
the em-dash ban (Section 2, "System-granted exemptions"). Three of them are
punctuation shapes that show up in real deliverables: the ClickUp definition
delimiter (`*   **Term** — definition`), the status-label delimiter
(`Status: {class} — {qualifier}`) and the Catalog entry delimiter
(`### {Stable ID} — {Entry name}` and its index link). A line matching one shape is exempted
from the em-dash count on that line, because the card grants the exemption
there and nowhere else.

Section 10, "Always cut," is deliberately absent from this linter. HVR core
states outright that those terms "are edits, so they never count toward the
hard blocker total," so filler words like "very" or "basically" are a
different system's job, not this one's.

Also absent, and left to a human reader rather than approximated badly: the
Oxford comma (no reliable list-boundary signal without a parser), asterisk
emphasis used mid-sentence versus the same asterisks used as a sanctioned
structural label (the two are visually identical and only context tells them
apart), title-case headings (needs a per-word part-of-speech judgement this
tool does not make), and the fuzzier Section 9 bans that require counting
across a whole document rather than matching a span (triad density, synonym
cycling, false ranges, notability by association). A green result here is a
statement about the checks it actually runs, not about every rule the card
states.

Extraction confidence is carried through rather than hidden. A Product Owner
delivery response carries its `HVR self-scan:` line and its process metadata
(Mode, export path, quality summary) beside the artifact, never inside it
(`references/hvr-core.md` Section 11), and the manual playbook lists process
material inside a delivered body as a blocking defect in its own right. The
self-scan line in particular exists to *name* the blocked terms it fixed, so
scanning it as prose would fail a clean delivery on its own compliance report.
When that line is found, it and known metadata lines are stripped before
scanning and confidence is `high`. A reply with no such line is prose
throughout (a plain chat answer, or a capture that dropped the metadata), so
this falls back to scanning the whole text at confidence `low`, and phrase-type
findings are downgraded to `soft` there because a phrase like "the truth is"
is far more likely to be the model narrating its own reasoning than a line a
Product Owner artifact would actually ship. Punctuation and the fixed word
list stay `hard` at any confidence, because an em dash or a semicolon is not
a matter of narration versus deliverable.
"""
import functools
import json
import re
import sys
import tempfile
from pathlib import Path
from typing import NamedTuple, Optional

# ───────────────────────────────────────────────────────────────
# 1. CONFIGURATION
# ───────────────────────────────────────────────────────────────

CARD = Path(__file__).resolve().parents[2] / "sk-product-owner" / "references" / "hvr-core.md"

# The card names these departures itself or the grader needs them, so each is a
# constant here rather than a quiet difference between two copies.
#
# A US spelling of a card word. The card lists "revolutionise" alone, and a reply
# written in the spelling of "utilize" and "utilizing", which the card lists in
# US form, would otherwise slip past.
US_SPELLING = {"revolutionise": "revolutionize"}
# Section 9 lists "features" and "offers" beside the other copula verbs. As bare
# words they are ordinary nouns and verbs in backlog prose ("the task features
# three checklist items," "the plan offers two options"), so they would fire on
# ordinary sentences far more often than on the copula the card means to catch.
ORDINARY_COPULA = {"features", "offers"}

CARD_LITERAL_NOTE = "Blocked as metaphor, allowed when literal:"
CARD_HEADING = re.compile(r"^##\s+\d+\.")
QUOTED_SPAN = re.compile(r'"([^"]+)"')
COPULA_BULLET = "- **Copula avoidance.**"


class CardError(RuntimeError):
    """The card is missing, or a list this linter needs came out of it empty."""


class CardLists(NamedTuple):
    """The four term lists read from the card, each lower-cased and in card order."""

    words: tuple[str, ...]
    phrases: tuple[str, ...]
    metaphors: tuple[str, ...]
    copula: tuple[str, ...]


SELF_SCAN = re.compile(r"^HVR self-scan:.*$", re.M)
# Delivery-proof lines the manual playbook names as fixed fixtures beside the
# artifact rather than inside it: the skill's path-first line, its read-back
# confirmation (`Verified: read-back succeeded; N lines`, the exact fixture
# the SID-001 scenario contract names, semicolon included), the Project
# runtime's export-equivalent line, and the process headers HVR core Section
# 11 and the playbook's own defect table both say never belong in a
# delivered body (Mode, Energy, Template, Quality Score, Perspectives).
META_LINE = re.compile(
    r"^\s*(Mode|Energy|Template|Framework|Quality Score|Export path|"
    r"Export-equivalent path|Perspectives|Kernel-Version|Path|Verified)\s*:", re.I
)
# The shapes `references/hvr-core.md` Section 2 grants as exceptions to the
# em-dash ban: the ClickUp definition delimiter, the status-label delimiter and
# the Catalog entry delimiter on an entry heading or its index link. A line
# matching one keeps every em dash on that line out of the count, because the
# card's exemption is granted to the shape, not to a document.
DEFINITION_DELIMITER_LINE = re.compile(r"^\s*[*\-]\s+\*\*[^*]+\*\*\s+—")
STATUS_LABEL_LINE = re.compile(r"\bStatus:\s*.+—")
CATALOG_STABLE_ID = r"(?:`[^`\s]+`|[A-Z][A-Z0-9]*[-_][A-Za-z0-9_-]+)"
CATALOG_ENTRY_LINE = re.compile(
    rf"^### {CATALOG_STABLE_ID} — [^—\s][^—]*$|^\* {{3}}\[{CATALOG_STABLE_ID} — [^\]—]+\]\(#[^)\s]+\)\s*$"
)
CURLY_QUOTES = re.compile("[‘’“”]")
# `TBD...` is the fixed Delivery placeholder `references/hvr-core.md` Section 2
# grants as a token rather than prose punctuation, so it never counts toward
# the one-ellipsis cap.
ELLIPSIS = re.compile(r"(?<!TBD)\.\.\.|…")
# A bullet line (ClickUp `*   ` or a plain `-   `) whose content ends in a
# single period. Excludes `...` and a line ending in two or more periods, and
# never matches a numbered acceptance-criteria title, which HVR core does not
# ban from ending in punctuation the way it bans bullets from it.
BULLET_FULL_STOP = re.compile(r"^[ \t]*[*\-]\s+.*[^.\n]\.[ \t]*$", re.M)
NOT_JUST_X_BUT = re.compile(r"not (?:just|only) .{1,40}? but", re.I)
# Phrase terms match whole words only, the same boundary the output format
# gate uses, so "acts as" never fires inside "contacts as".
TERM_EDGE_BEFORE = r"(?<![A-Za-z0-9])"
TERM_EDGE_AFTER = r"(?![A-Za-z0-9])"


# ───────────────────────────────────────────────────────────────
# 2. HELPERS
# ───────────────────────────────────────────────────────────────


def card_section(lines: list[str], number: int) -> list[str]:
    """The lines under one numbered `##` heading of the card, up to the next numbered heading."""
    start = next((i for i, line in enumerate(lines) if re.match(rf"^##\s+{number}\.\s", line)), None)
    if start is None:
        return []
    end = next((i for i in range(start + 1, len(lines)) if CARD_HEADING.match(lines[i])), len(lines))
    return lines[start + 1:end]


@functools.lru_cache(maxsize=None)
def card_lists(card: Path = CARD) -> CardLists:
    """Read the word, phrase, metaphor and copula lists out of the Human Voice card.

    Section 3 is one bare comma list followed by the allowed-when-literal note,
    Sections 4 and 5 are quoted phrase lists and the copula verbs are the quoted
    terms in the first sentence of one Section 9 bullet. A phrase that carries a bracketed placeholder
    keeps the text before it, since the bracket names a slot and not literal text.
    A metaphor already in the word list is dropped so it counts once.

    Args:
        card: Path of the card file.

    Returns:
        The four lists, each lower-cased and in the card's own order.

    Raises:
        CardError: If the card cannot be read or any list comes out empty, because
            a linter holding an empty list passes every reply it is given.
    """
    try:
        lines = card.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        raise CardError(f"the Human Voice card cannot be read: {error}") from None
    listing = next(
        (line for line in card_section(lines, 3)
         if line.strip() and not line.startswith(CARD_LITERAL_NOTE) and not re.fullmatch(r"-{3,}", line.strip())),
        "",
    )
    words: list[str] = []
    for word in (part.strip().lower() for part in listing.split(",")):
        if word:
            words.append(word)
            if word in US_SPELLING:
                words.append(US_SPELLING[word])

    def quoted(number: int) -> list[str]:
        """Every quoted term of one section, lower-cased, with a placeholder cut to its fixed prefix."""
        terms = (span.lower().split("[")[0].strip() for line in card_section(lines, number) for span in QUOTED_SPAN.findall(line))
        return [term for term in terms if term]

    # The bullet ends on the fix, `Write "is" or "has"`, so only the first sentence names verbs to avoid.
    bullet = next((line for line in lines if line.startswith(COPULA_BULLET)), "")
    avoided = bullet[len(COPULA_BULLET):].split(". ", 1)[0]
    copula = [span.lower() for span in QUOTED_SPAN.findall(avoided) if span.lower() not in ORDINARY_COPULA]
    lists = CardLists(
        tuple(words),
        tuple(quoted(4)),
        tuple(term for term in quoted(5) if term not in words),
        tuple(copula),
    )
    for name, terms in lists._asdict().items():
        if not terms:
            raise CardError(f"the Human Voice card yielded no {name}, so the linter would guard nothing")
    return lists


def extract_deliverable(raw: str) -> tuple[str, str]:
    """Return (text, confidence): the reply body with delivery metadata cut.

    Prefer the structured shape a Product Owner reply is supposed to carry:
    an `HVR self-scan:` line plus a handful of labelled metadata lines,
    neither of which is part of the artifact and both of which can
    legitimately name a blocked term while reporting on it. Finding and
    removing that shape is `high` confidence. Finding none of it means the
    text is prose throughout, either a plain chat reply or a capture that
    lost its structure, so the whole text is scanned at `low` confidence.
    """
    found_scan = SELF_SCAN.search(raw) is not None
    kept = [line for line in raw.splitlines() if not META_LINE.match(line)]
    text = SELF_SCAN.sub("", "\n".join(kept))
    return text, ("high" if found_scan else "low")


def term_pattern(term: str) -> re.Pattern:
    """A case-blind pattern for one listed phrase, bounded at both ends."""
    return re.compile(TERM_EDGE_BEFORE + re.escape(term) + TERM_EDGE_AFTER, re.I)


def samples(pattern: re.Pattern, text: str, n: int = 2) -> list[str]:
    """Up to `n` context windows around each match, for the samples list."""
    out = []
    for m in pattern.finditer(text):
        s = text[max(0, m.start() - 25): m.end() + 25].replace("\n", " ")
        out.append(s.strip())
        if len(out) >= n:
            break
    return out


def _exempt_em_dash_lines(text: str) -> set[int]:
    """Line numbers (0-based) where a granted delimiter shape sits.

    Returned as a set of line indices so the em-dash scan below can drop a
    match that falls on one of them without needing a second pass over the
    granted shape's own em dash.
    """
    exempt = set()
    for i, line in enumerate(text.splitlines()):
        if (DEFINITION_DELIMITER_LINE.search(line) or STATUS_LABEL_LINE.search(line)
                or CATALOG_ENTRY_LINE.search(line)):
            exempt.add(i)
    return exempt


# ───────────────────────────────────────────────────────────────
# 3. CORE LOGIC
# ───────────────────────────────────────────────────────────────


def lint(text: str, confidence: str = "high", card: Path = CARD) -> list[dict[str, object]]:
    """Every hard-blocker finding in `text`, each typed, counted and sampled.

    Raises:
        CardError: If the card the term lists come from cannot be read.
    """
    v = []
    terms = card_lists(card)

    def add(kind: str, pat: Optional[re.Pattern], severity: str = "hard",
            count: Optional[int] = None, sample_list: Optional[list[str]] = None) -> None:
        """Record a finding, either from a pattern scanned fresh over `text`
        or from a pre-filtered hit list the caller already built (`count`
        and `sample_list` both given, `pat` used only to type the entry)."""
        if count is None:
            hits = list(pat.finditer(text))
            count = len(hits)
            sample_list = samples(pat, text)
        if count:
            v.append({"type": kind, "severity": severity, "count": count,
                       "samples": sample_list or []})

    # --- Section 2: punctuation, never (minus Oxford comma, asterisk
    # emphasis and title-case headings, all left to a reader, see module
    # docstring) ---
    lines = text.splitlines()
    exempt_lines = _exempt_em_dash_lines(text)
    em_dash_hits = [
        (line, m) for i, line in enumerate(lines) for m in re.finditer("—", line)
        if i not in exempt_lines
    ]
    em_dash_samples = [
        line[max(0, m.start() - 25): m.end() + 25].strip() for line, m in em_dash_hits[:2]
    ]
    add("em_dash", None, count=len(em_dash_hits), sample_list=em_dash_samples)
    add("semicolon", re.compile(";"))
    add("curly_quote", CURLY_QUOTES)
    add("bullet_ends_with_full_stop", BULLET_FULL_STOP)
    ellipsis_hits = list(ELLIPSIS.finditer(text))
    if len(ellipsis_hits) > 1:
        add("more_than_one_ellipsis", None, count=len(ellipsis_hits),
            sample_list=samples(ELLIPSIS, text))

    # --- Section 3: hard blocker words ---
    # A bare trailing "s" is allowed after the listed form, so "leverages"
    # and "fosters" are caught alongside "leverage" and "foster". Other
    # inflections are not attempted: several of these verbs drop or double a
    # letter before "-ing" or "-ed" (elevate -> elevating, not elevateing),
    # and a guessed suffix that gets that wrong is a false negative dressed
    # up as coverage.
    for w in terms.words:
        add(f"hard_blocker_word:{w}", re.compile(r"\b" + re.escape(w) + r"s?\b", re.I))

    # --- Section 9: structural ban that is a fixed pattern rather than a
    # document-wide count ---
    add("not_just_x_but", NOT_JUST_X_BUT)

    # Phrase-shaped rules (Sections 4, 5 and the Section 9 copula list) are
    # hard at high confidence, where the text is known to be the delivered
    # artifact, and soft at low confidence, where the text could equally be
    # the model narrating its own reasoning rather than shipping copy.
    phrase_severity = "hard" if confidence == "high" else "soft"
    for p in terms.phrases:
        add(f"hard_blocker_phrase:{p}", term_pattern(p), severity=phrase_severity)
    for m in terms.metaphors:
        add(f"metaphor:{m}", term_pattern(m), severity=phrase_severity)
    for c in terms.copula:
        add(f"copula:{c}", term_pattern(c), severity=phrase_severity)

    return v


# ───────────────────────────────────────────────────────────────
# 4. SELF-TEST
# ───────────────────────────────────────────────────────────────


SYNTHETIC_CARD = """## 3. HARD BLOCKER WORDS

alpha, revolutionise, game-changer, beta

Blocked as metaphor, allowed when literal: journey

---

## 4. HARD BLOCKER PHRASES

"Zz phrase", "Navigating the [X]"

---

## 5. BANNED METAPHORS AND CLICHES

"zz figure", "game-changer"

---

## 9. STRUCTURAL BANS

- **Copula avoidance.** "serves as", "features", "offers". Write "is" or "has"
"""


def self_test() -> int:
    """Prove the lists follow the card and each named departure from it holds.

    The cases read a small made-up card, so none depends on which terms the real
    card carries today. One case reads the real card, to prove its sections still
    parse into every list.
    """
    results: list[tuple[str, bool]] = []
    with tempfile.TemporaryDirectory(prefix="po-hvr-lint-") as scratch:

        def card(name: str, text: str = SYNTHETIC_CARD) -> Path:
            """Write a card file into the scratch folder and return its path."""
            path = Path(scratch) / name
            path.write_text(text, encoding="utf-8")
            return path

        def found(text: str, path: Path) -> set[str]:
            """The finding types lint reports for a sentence under one card."""
            return {v["type"] for v in lint(text, "high", path)}

        base = card("base.md")
        results.append(("a word in the card's Section 3 is flagged", "hard_blocker_word:alpha" in found("an alpha plan", base)))
        results.append(("a word the card does not list is not", found("a gamma plan", base) == set()))
        results.append(("a word added to the card is flagged", "hard_blocker_word:gamma" in found("a gamma plan", card("added.md", SYNTHETIC_CARD.replace("beta", "beta, gamma")))))
        results.append(("a word removed from the card stops being flagged", "hard_blocker_word:beta" not in found("a beta plan", card("removed.md", SYNTHETIC_CARD.replace(", beta", "")))))
        results.append(("a phrase and a metaphor of the card are flagged", {"hard_blocker_phrase:zz phrase", "metaphor:zz figure"} <= found("Zz phrase, then a zz figure", base)))
        results.append(("a US spelling of a card word is flagged", "hard_blocker_word:revolutionize" in found("we revolutionize it", base)))
        results.append(("a phrase with a placeholder keeps its fixed prefix", "hard_blocker_phrase:navigating the" in found("Navigating the rollout", base)))
        twice = found("a game-changer", base)
        results.append(("a metaphor the word list already holds counts once", "hard_blocker_word:game-changer" in twice and "metaphor:game-changer" not in twice))
        verbs = found("this is a guide that serves as a map, has two options, features a map and offers a choice", base)
        results.append(("the copula verbs are the card's minus the two ordinary ones", verbs == {"copula:serves as"}))

        for label, text in (
            ("a card with no word list", SYNTHETIC_CARD.replace("alpha, revolutionise, game-changer, beta", "")),
            ("a card with no quoted phrases", SYNTHETIC_CARD.replace('"', "")),
            ("a card with no copula bullet", SYNTHETIC_CARD.replace("Copula avoidance", "Something else")),
        ):
            try:
                lint("anything", "high", card("broken.md", text))
                refused = False
            except CardError:
                refused = True
            results.append((f"{label} is refused, not passed", refused))
        try:
            lint("anything", "high", Path(scratch) / "gone.md")
            refused = False
        except CardError:
            refused = True
        results.append(("a missing card is refused, not passed", refused))

    try:
        real = card_lists()
        results.append(("the real card parses into all four lists", all(real)))
    except CardError:
        results.append(("the real card parses into all four lists", False))

    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
    return 0 if all(ok for _, ok in results) else 1


# ───────────────────────────────────────────────────────────────
# 5. ENTRY POINT
# ───────────────────────────────────────────────────────────────


def main() -> None:
    """Lint one reply file and print the finding report as JSON, or run the self-test."""
    if len(sys.argv) < 2:
        print("usage: hvr_lint.py <reply file> | --self-test", file=sys.stderr)
        sys.exit(64)
    if sys.argv[1] == "--self-test":
        sys.exit(self_test())
    path = sys.argv[1]
    with open(path, encoding="utf-8", errors="replace") as handle:
        raw = handle.read()
    text, confidence = extract_deliverable(raw)
    try:
        viols = lint(text, confidence)
    except CardError as error:
        print(f"hvr_lint: {error}", file=sys.stderr)
        sys.exit(2)
    hard = [x for x in viols if x["severity"] == "hard"]
    print(json.dumps({
        "file": path,
        "extraction_confidence": confidence,
        "clean": len(hard) == 0,
        "hard_violations": len(hard),
        "violations": viols,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
