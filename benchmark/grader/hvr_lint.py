#!/usr/bin/env python3
"""Deterministic Human Voice hard-blocker linter for Product Owner replies.

Usage: hvr_lint.py <file>   ->  prints JSON {file, clean, violations:[{type,count,samples}]}

This is a code gate, never a model judging its own prose: every check below is
a fixed string or a narrow regex, so the result cannot be talked past. The
word list, the phrase list, the metaphor list and the punctuation bans are
`references/hvr-core.md`'s own Sections 2 through 5 and 9, the file this
system loads on every turn specifically so those terms stay in view while
writing. A term added there is added here in the same change.

`references/hvr-core.md` also names four narrow, system-granted exemptions to
the em-dash ban (Section 2, "System-granted exemptions"). Two of them are
punctuation shapes that show up in real deliverables: the ClickUp definition
delimiter (`*   **Term** — definition`) and the status-label delimiter
(`Status: {class} — {qualifier}`). A line matching either shape is exempted
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
import sys, json, re

# Section 3, HARD BLOCKER WORDS, verbatim, minus the six terms the same
# section calls out as "blocked as metaphor, allowed when literal"
# (navigating, landscape, unlock, ecosystem, journey, deep dive). Detecting
# literal versus figurative use needs a reader, not a word-boundary regex, so
# those six are left out rather than flagged wrong half the time.
HARD_BLOCKER_WORDS = [
    "delve", "embark", "realm", "tapestry", "illuminate", "unveil", "elucidate",
    "abyss", "revolutionise", "revolutionize", "game-changer", "groundbreaking",
    "cutting-edge", "ever-evolving", "shed light", "dive deep",
    "leverage", "foster", "nurture", "resonate", "empower", "disrupt", "curate",
    "harness", "elevate", "robust", "seamless", "holistic", "synergy", "unpack",
    "paradigm", "enlightening", "esteemed", "remarkable", "skyrocket",
    "skyrocketing", "utilize", "utilizing",
]

# Section 4, HARD BLOCKER PHRASES, verbatim. "Navigating the [X]" is
# represented as the fixed prefix before the placeholder, since the bracket
# names a slot rather than literal text.
HARD_BLOCKER_PHRASES = [
    "it's important to", "it's worth noting", "it goes without saying",
    "at the end of the day", "moving forward", "in today's world",
    "in today's digital landscape", "when it comes to", "dive into",
    "i'd love to", "navigating the", "that being said", "having said that",
    "let me be clear", "the reality is", "here's the thing",
    "in a world where", "you're not alone", "the real question is",
    "here's what you need to know", "what most people don't realise is",
    "the truth is",
]

# Section 5, BANNED METAPHORS AND CLICHES, verbatim, minus "game-changer,"
# which Section 3 already lists and this linter already counts once there.
BANNED_METAPHORS = [
    "bridge the gap", "tip of the iceberg", "pave the way",
    "the landscape of", "at the heart of", "double-edged sword",
    "move the needle", "low-hanging fruit", "think outside the box",
    "raise the bar", "level the playing field", "a perfect storm",
    "the elephant in the room", "a deep dive", "the bottom line",
    "food for thought", "a breath of fresh air",
    "light at the end of the tunnel",
]

# Section 9's copula-avoidance list, minus "features" and "offers": both are
# ordinary nouns and verbs in backlog prose ("the task features three
# checklist items," "the plan offers two options"), so as bare words they
# would fire on ordinary sentences far more often than on the copula HVR
# means to catch.
COPULA_AVOIDANCE = ["serves as", "stands as", "functions as", "acts as", "boasts"]

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
# The two shapes `references/hvr-core.md` Section 2 grants as exceptions to
# the em-dash ban: the ClickUp definition delimiter and the status-label
# delimiter. A line matching either keeps every em dash on that line out of
# the count, because the card's exemption is granted to the shape, not to a
# document.
DEFINITION_DELIMITER_LINE = re.compile(r"^\s*[*\-]\s+\*\*[^*]+\*\*\s+—")
STATUS_LABEL_LINE = re.compile(r"\bStatus:\s*.+—")
CURLY_QUOTES = re.compile("[‘’“”]")
ELLIPSIS = re.compile(r"\.\.\.|…")
# A bullet line (ClickUp `*   ` or a plain `-   `) whose content ends in a
# single period. Excludes `...` and a line ending in two or more periods, and
# never matches a numbered acceptance-criteria title, which HVR core does not
# ban from ending in punctuation the way it bans bullets from it.
BULLET_FULL_STOP = re.compile(r"^[ \t]*[*\-]\s+.*[^.\n]\.[ \t]*$", re.M)
NOT_JUST_X_BUT = re.compile(r"not (?:just|only) .{1,40}? but", re.I)


def extract_deliverable(raw: str):
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


def samples(pattern, text, n=2):
    out = []
    for m in pattern.finditer(text):
        s = text[max(0, m.start() - 25): m.end() + 25].replace("\n", " ")
        out.append(s.strip())
        if len(out) >= n:
            break
    return out


def _exempt_em_dash_lines(text):
    """Line numbers (0-based) where a granted delimiter shape sits.

    Returned as a set of line indices so the em-dash scan below can drop a
    match that falls on one of them without needing a second pass over the
    granted shape's own em dash.
    """
    exempt = set()
    for i, line in enumerate(text.splitlines()):
        if DEFINITION_DELIMITER_LINE.search(line) or STATUS_LABEL_LINE.search(line):
            exempt.add(i)
    return exempt


def lint(text: str, confidence: str = "high"):
    v = []

    def add(kind, pat, severity="hard", count=None, sample_list=None):
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
    for w in HARD_BLOCKER_WORDS:
        add(f"hard_blocker_word:{w}", re.compile(r"\b" + re.escape(w) + r"s?\b", re.I))

    # --- Section 9: structural ban that is a fixed pattern rather than a
    # document-wide count ---
    add("not_just_x_but", NOT_JUST_X_BUT)

    # Phrase-shaped rules (Sections 4, 5 and the Section 9 copula list) are
    # hard at high confidence, where the text is known to be the delivered
    # artifact, and soft at low confidence, where the text could equally be
    # the model narrating its own reasoning rather than shipping copy.
    phrase_severity = "hard" if confidence == "high" else "soft"
    for p in HARD_BLOCKER_PHRASES:
        add(f"hard_blocker_phrase:{p}", re.compile(re.escape(p), re.I), severity=phrase_severity)
    for m in BANNED_METAPHORS:
        add(f"metaphor:{m}", re.compile(re.escape(m), re.I), severity=phrase_severity)
    for c in COPULA_AVOIDANCE:
        add(f"copula:{c}", re.compile(re.escape(c), re.I), severity=phrase_severity)

    return v


def main():
    if len(sys.argv) < 2:
        print("usage: hvr_lint.py <reply file>", file=sys.stderr)
        sys.exit(64)
    path = sys.argv[1]
    raw = open(path, encoding="utf-8", errors="replace").read()
    text, confidence = extract_deliverable(raw)
    viols = lint(text, confidence)
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
