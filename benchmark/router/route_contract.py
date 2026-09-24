#!/usr/bin/env python3
"""Deterministic route contract for the Barter Product Owner skill.

Characterizes a request into one stable route object so artifact routing,
energy detection and disambiguation behavior are testable without invoking a
model. This is the executable oracle the skill and project kernels are
written against, not a claim about what claude.ai executes internally.

The skill document carries the same router as pseudocode and states that the
two must never drift. Every table below is therefore a copy of that block's
table, value for value and in the same order, because table order is the score
tie-break. `differential.py` executes the skill's block and proves the copy,
so a table edited here alone fails the gate rather than passing quietly.

The contract fixes three observed failure classes. Substring alias matching (a
command like `$doc` matched inside `$document`, or a keyword like `bug`
matched inside `debugging`) must never select an intent, so only a complete
`$token` and a word-boundary keyword can. A multi-word phrase matched as an
exact adjacent run must not be defeated by the qualifier a person types inside
it, so "write a full story" routes exactly where "write a story" routes
instead of falling to the fallback band. And a `$token` is a routing control
rather than subject matter, so it is stripped before semantic scoring: without
that, a false prefix such as `$epics` leaks the keyword hit that the
exact-token rule just refused to honour as a command.

Explicit commands win over every natural-language signal, and artifact framing
("write a bug report about...") wins over plain topic scoring. Confidence
thresholds gate directness the same way the skill's own router does. Standard
energy routes directly at 0.60 and above and asks one question below it. Quick
energy routes directly at 0.40 and above and otherwise falls back to Task, its
narrow safe default. Every decision here is deterministic and fixture-checkable.

Python 3.9 compatible.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

# ---------------------------------------------------------------------------
# Token tables (exact, delimiter-aware matches only)
# ---------------------------------------------------------------------------

# `$task`/`$t` must not fire inside `$taskforce`, and `$doc` must not fire
# inside `$document` or `$doc.md`. TOKEN_START/TOKEN_END reject a `$`, word
# character, dot-extension, slash or hyphen immediately touching the token,
# so only a complete, delimiter-bounded token counts.
TOKEN_START = r"(?<![\w$])"
TOKEN_END = r"(?![\w$/-]|\.[\w])"

# Real requests qualify the artifact noun: "write a full story", "a proper
# PRD", "turn this into a quick story". Matching a multi-word phrase as an
# exact adjacent run let one inserted adjective drop a confident route past
# the HIGH, MEDIUM and LOW bands straight into the fallback, so every gap
# inside a phrase now absorbs a bounded run of intervening words. The bound is
# what keeps it honest. One word per gap is an adjective or an article, and
# the gap is whitespace-separated word characters only, so it can never reach
# across a comma or a full stop to pull an artifact noun out of another
# clause.
PHRASE_GAP_WORDS = 1
PHRASE_GAP = rf"\s+(?:\w+\s+){{0,{PHRASE_GAP_WORDS}}}"
FRAME_MODIFIER = rf"(?:\w+\s+){{0,{PHRASE_GAP_WORDS}}}"


def phrase_pattern(phrase: str) -> str:
    """Word-boundary pattern for one synonym, gap-tolerant between its words.

    A single-word synonym is unchanged, so `bug` still matches "file a bug"
    and never "debugging". A multi-word synonym keeps its word order and its
    outer boundaries and only tolerates the qualifier a person actually
    writes between the words.
    """
    words = [re.escape(word) for word in phrase.split()]
    return r"\b" + PHRASE_GAP.join(words) + r"(?:s|es|ed|ing)?\b"


# Explicit artifact commands. Exactly one wins outright over every
# natural-language signal; more than one collected command is a conflict.
ARTIFACT_COMMANDS: Dict[str, str] = {
    "$task": "TASK", "$t": "TASK",
    "$bug": "BUG", "$b": "BUG",
    "$doc": "DOC", "$d": "DOC",
    "$story": "STORY", "$s": "STORY",
    # $prd/$p stay valid back-compat aliases for the Story intent, because
    # existing prompts and habits reach for them.
    "$prd": "STORY", "$p": "STORY",
    # $epic/$e is the same Story intent under a different shape rather than a
    # separate intent, so it never conflicts with $story.
    "$epic": "STORY", "$e": "STORY",
}

# Which shape each Story command selects. The intent picks the mode reference,
# the shape picks the single scaffold that loads with it, so a Story request
# never carries the Epic scaffold it will not use.
SHAPE_COMMANDS: Dict[str, str] = {
    "$story": "STORY", "$s": "STORY",
    "$prd": "STORY", "$p": "STORY",
    "$epic": "EPIC", "$e": "EPIC",
}

# Most specific shape first. An epic noun names the initiative, and every
# other requirements framing is a Story.
SHAPE_PRECEDENCE = ("EPIC", "STORY")

# `$quick`/`$q` and natural quick/fast framing set energy only; they never
# select an artifact intent by themselves.
QUICK_TOKENS = {"$quick", "$q"}
# "quick" and "fast" set energy only when they frame the request itself. As
# subject matter ("crashes when scrolling fast") they must not skip an intake
# gate, and a denial ("this is not a quick fix") must not read as the override.
NATURAL_QUICK_RE = re.compile(
    r"^(?:please\s+)?(?:quick|fast)\b"
    r"|\b(?:quick|fast)\s+(?:task|subtask|bug|doc|document|draft|version|pass|one|check|write-?up)\b"
    r"|\b(?:make|keep)\s+(?:it|this|that)\s+(?:quick|fast)\b"
    r"|\bno[ -]?questions\b",
    re.IGNORECASE,
)
NEGATED_QUICK_RE = re.compile(
    r"\b(?:not|isn'?t|no|never)\s+(?:a\s+|an\s+|the\s+)?(?:quick|fast)\b",
    re.IGNORECASE,
)

# Story-lane framing, grouped by the shape each group names. The groups are
# the one copy: FRAME_PATTERNS flattens them for intent detection and
# resolve_shape reads them in precedence order for shape detection, so a
# pattern can never say one thing to the intent and another to the shape.
SHAPE_FRAMES: Dict[str, List[str]] = {
    "EPIC": [
        rf"\b(write|create|draft) (an? )?{FRAME_MODIFIER}epic\b",
        r"\bepic (for|about|covering)\b",
        rf"\bturn (this|these|it) into (an? )?{FRAME_MODIFIER}epic\b",
        r"\b(refine|update|edit) (this |the |an? )?epic\b",
        # An initiative can be named by its scale instead of the word "epic":
        # "whole dashboard thing", "the whole creator verification programme"
        # and "the full payments migration across web and mobile" all scope a
        # body of work the way an epic noun does, and this construction is the
        # only semantic path to the Epic shape, since a topic score names the
        # lane rather than the shape. A scale word alone cannot carry it,
        # because "we tested the whole login flow" scopes a test and "the
        # whole team" names a group, so the scale word has to land on a noun
        # that already means a body of work. The initiative verbs redesign,
        # rework, revamp and overhaul stay out of the noun list: each one
        # appears inside ordinary defect and polish reports, where it would
        # pull a request into the Epic shape on the strength of one word.
        r"\b(?:whole|entire|full|complete|end-to-end)\s+(?:[\w'-]+\s+){0,3}"
        r"(?:thing|initiative|programme|program|rollout|roll-out|migration"
        r"|workstream|project|effort|launch)\b",
    ],
    "STORY": [
        rf"\b(write|create|draft) (a |an )?{FRAME_MODIFIER}(prd|product requirements? doc(?:ument)?)\b",
        rf"\b(write|create|draft) (a |an )?{FRAME_MODIFIER}(user )?stor(y|ies)\b",
        r"\buser story\b",
        r"\bstory (for|about|covering)\b",
        rf"\bturn (this|these|it) into (a |an )?{FRAME_MODIFIER}(prd|stor(y|ies))\b",
        r"\b(refine|update|edit) (this |the |an? )?(prd|(user )?story)\b",
        # "Creators cannot X, we should let them" is a capability request with
        # no PRD noun anywhere in it: the denial names the gap and "let them"
        # names the fix, and together they are exactly a user-need frame. The
        # unmarked spelling "cant" is included because that is how the denial
        # is typed in practice. The 80-character window keeps "let them" from
        # reaching across an unrelated later clause to pair with a distant
        # negation, so "this isn't a quick fix, we can't let it slip" (a
        # different sense of "let") is not swept in: it also has no "let
        # them" at all.
        r"\b(?:can'?t|cant|cannot|can not)\b[^.!?]{0,80}\blet them\b",
        # More often the gap is stated with no fix clause at all: "brands cant
        # filter by engagement rate", "creators have no way to pause a
        # campaign". What makes that a requirements frame rather than a defect
        # report is the subject. A role is being denied a capability, where a
        # failure report has a system as its subject, so the denial only
        # counts behind a person noun. That also keeps an ordinary aside like
        # "we can't let it slip" out of the Story lane. Two whole-line
        # lookaheads carry the rest of the separation: a line already naming a
        # defect is a defect report about a capability that exists, and a line
        # saying the capability used to work is a regression rather than a
        # gap.
        r"^(?!.*\b(?:bug|defect|error|broken|crash(?:es|ed|ing)?|repro|failing)\b)"
        r"(?!.*\b(?:anymore|any more|no longer|used to|suddenly|regressed)\b)"
        r".*\b(?:users?|creators?|brands?|customers?|clients?|admins?|members?"
        r"|people|teams?|managers?|owners?|advertisers?|agencies|agency"
        r"|partners?|reviewers?|editors?|subscribers?|buyers?|sellers?)\s+"
        r"(?:can'?t|cant|cannot|can not|are unable to|is unable to"
        r"|are not able to|is not able to|aren'?t able to"
        r"|have no way to|has no way to|have no option to)\b",
        # The pre-PM draft was its own artifact kind once, and these are the
        # wordings people reached for to ask for one. The kind is gone and the
        # Story is what a request like this now wants, so the phrasings stay
        # here rather than being deleted: an old habit lands on a Story
        # instead of scoring nothing and falling to an intake question.
        # The negative lookahead holds "draft" in its noun sense, so "a draft
        # task" and "a draft guide" stay those artifacts in an early state.
        r"\b(write|create|make|draft) (a |an )?(story )?draft\b"
        r"(?!\s+(?:task|subtask|bug|doc|document|documentation|guide|reference"
        r"|catalog|runbook|prd|epic|stor(?:y|ies)|report|proposal))",
        # The object handed over is named as loosely as the request itself is:
        # notes, an outline or a brief for the PM is the same ask as a draft
        # for the PM, and the destination is what marks it as requirements
        # work rather than a document.
        r"\b(?:draft|notes?|write-?up|outline|brief) for (the |a )?(pm|product manager|product owner)\b",
        rf"\bturn (this|these|it) into (a |an )?{FRAME_MODIFIER}(story )?draft\b",
        # A handoff can name the ask from the receiving end instead of the
        # noun order above: "give the PM a draft" is the same request as
        # "write a draft for the PM", just phrased as delivery.
        r"\bgive (?:the |a )?(?:pm|product manager|product owner) (?:a |an )?draft\b",
        # A handoff can also skip the word "draft" entirely when the
        # destination names it instead. "turn my notes into something the
        # devs can pick up" is still requirements work even though no word in
        # it is "draft", and the phrase gap is capped at 80 characters so it
        # cannot reach across an unrelated clause to pair with "pick up".
        r"\bturn (?:my |these |this |the )?notes into\b[^.!?]{0,80}\b(?:pick up|run with)\b",
        # The handoff can name what the PM will do with it instead of naming
        # the object at all: "something the PM can turn into stories later"
        # is the same request described by its destination. The story noun has
        # to sit inside the same clause as the handing over, so an unrelated
        # later mention of a story cannot pair with a distant PM.
        r"\b(?:pm|product manager|product owner)\b[^.!?]{0,40}"
        r"\b(?:turn|cut|write|make|build)\b[^.!?]{0,20}\b(?:stor(?:y|ies)|prds?|tickets?)\b",
    ],
}
_STORY_FRAMES = [pattern for shape in SHAPE_PRECEDENCE for pattern in SHAPE_FRAMES[shape]]

# Commissioning a document is not always phrased as writing one. "Put together
# a reference for the webhook payloads" and "prepare the on-call runbook" are
# the same request as "write" one, so the verb list is the family rather than
# the three verbs the earlier probe set happened to use.
DOC_AUTHOR_VERBS = r"(write|create|draft|put together|pull together|prepare|assemble)"

# Artifact framing (word/phrase patterns, not exact tokens). Framing beats
# subject nouns and semantic scoring but loses to an explicit command.
FRAME_PATTERNS: Dict[str, List[str]] = {
    "TASK": [
        r"\b(create|write|open|refine) (a )?(dev |development )?(task|subtask|parent task)\b",
        r"\btask to document\b",
        r"\bacceptance criteria\b",
        # Backlog intake for a concrete addition rarely says "task": "add a
        # deadline badge to the collab card" and "build a toggle row
        # component for notification prefs" name the thing to build
        # directly. Both carry a trailing anchor (the definite article after
        # the preposition, or the literal word "component") so a bare "add
        # this capability" or "add better logging around the retry loop"
        # still falls through to the weaker unweighted feature score instead
        # of a guaranteed direct route.
        r"\badd (?:a |an |another )?[\w'-]+(?:\s+[\w'-]+){0,3} (?:to|on|for|in) the\b",
        r"\bbuild (?:a |an )?[\w'-]+(?:\s+[\w'-]+){0,4} component\b",
        # Its own narrow entry because the surrounding sentence can carry a
        # competing bug word ("search results are slow, need pagination"),
        # and the build ask is what the person is actually asking for.
        r"\bneed(?:s)? (?:\w+\s+){0,1}pagination\b",
    ],
    "BUG": [
        r"\b(create|write|file) (a )?(bug report|defect report)\b",
        r"\bbug report about\b",
        # A symptom report often carries no defect noun at all: "the app
        # crashes on rotate during upload", "the checkout screen freezes when
        # you tap pay twice" and "notifications stop arriving after you
        # background the app" never say bug, issue or error. The verb family
        # below is the vocabulary a person reaches for instead of the noun, a
        # surface that stops responding or a value that comes out wrong, and
        # it requires the verb form rather than the noun so "the checkout
        # crash" stays a subject. It carries a negative lookahead across the
        # whole line for the rest of the bug topic's vocabulary: a report that
        # already names a second symptom (issue, error, defect, repro, or
        # another verb form) already clears the semantic score on its own, so
        # framing stays out of its way rather than overriding a confidence
        # value fixtures already pin. "it is broken, we already filed the
        # defect" and "we should redesign the export button, it is broken and
        # crashing constantly with an error" are exactly that case, and both
        # stay on the semantic path. The second lookahead holds "stop" in its
        # imperative sense, so "we should stop showing the banner" stays a
        # request to change behavior rather than a report that behavior broke.
        r"^(?!.*\b(?:bug|fix(?:es|ed|ing)?|issue|defect|error|broken|failing|repro)\b)"
        r"(?!.*\b(?:should|to|want to|please|can|could|let'?s)\s+stop\b)"
        r".*\b(?:crash(?:es|ed|ing)|freez(?:es|ing)|froze|frozen|hangs|hanging"
        r"|stalls|stalling|glitch(?:es|ing)|locks up|locked up|times out|timed out"
        r"|stops? \w+ing|stopped \w+ing"
        r"|(?:is|are|was|were|looks?|comes? out) (?:completely |totally |just )?"
        r"(?:wrong|incorrect|duplicated|garbled))\b",
        r"^(?!.*\b(?:bug|fix(?:es|ed|ing)?|issue|defect|error|crash(?:es|ed|ing)?|repro)\b).*\b(?:this|it|that)\s+is\s+broken\b",
        # A report can also name the broken value instead of the failure:
        # "the follower count shows -- for tiktok" and "the avatar shows a
        # broken image after upload" have no word from the bug topic's
        # vocabulary in them at all, and the verb is whichever one the surface
        # suggests rather than "shows" alone.
        r"\b(?:shows?|showing|displays?|displaying|renders?|rendering)\s+(?:-{1,2}|nothing|blank|null|undefined)(?!\w)",
        r"\b(?:shows?|showing|displays?|displaying|renders?|rendering)\s+(?:a |an |the )?(?:broken|blank|empty|garbled|corrupted|placeholder)\b",
        # A failing call is named by its status code rather than by a symptom
        # word, and a 4xx or 5xx in a request is always a defect report.
        r"\b(?:returns?|returning|throws?|throwing|gives?|giving)\s+(?:a |an )?[45]\d\d\b",
    ],
    "STORY": _STORY_FRAMES,
    "DOC": [
        r"\bdocument how\b",
        r"^(please )?document\b",
        r"\b(can you|could you|please) document\b",
        rf"\b{DOC_AUTHOR_VERBS} (an? )?(product |engineering |technical |system )?(documentation|docs|document|guide|catalog|behavior reference|runbook|troubleshooting guide|implementation guide|future-state proposal|technical proposal|decision record)\b",
        rf"\b{DOC_AUTHOR_VERBS} (an? )?(api|schema|architecture|system|implementation|configuration|technical|engineering|operational|security|compliance) (documentation|docs|document|guide|reference|catalog|runbook|proposal|recommendation|analysis|decision record|plan)\b",
        rf"\b{DOC_AUTHOR_VERBS} (an? )?(rfc|adr)\b",
        r"\b(recommend|select|choose|compare|analyze|analyse)\b.{0,120}\band document (it|the (decision|recommendation|analysis|selection))\b",
        r"\b(refine|update|edit) (this |the |an? )?(product |engineering |technical |api |schema |architecture |system )?(documentation|docs|document|guide|reference|catalog|runbook|proposal|decision record)\b",
        r"\b(refine|update|edit) (this |the )?[a-z0-9][\w .&/()'-]{0,80} (documentation|docs|document|guide|reference|catalog|runbook|proposal|decision record)\b",
        # Explanation framing can ask for the artifact by function instead of
        # by name: "write up the notification provider comparison" and
        # "something for the team explaining the reel rules" are both
        # documentation requests that never say document, guide or catalog.
        r"\bwrite up (?:the |a |an )?[\w'-]+(?:\s+[\w'-]+){0,4} comparison\b",
        r"\bsomething for (?:the )?(?:team|devs?|developers?|engineers?) explaining\b",
        # The artifact can also be named by what it produces rather than by
        # what it is called: "we need something written down explaining how
        # the payout schedule works" and "the ranking algorithm written up
        # properly" are documentation requests with no documentation noun in
        # them. The whole-line lookahead keeps a defect out of the Doc lane,
        # since "the crash needs writing up" is a bug being filed rather than
        # a guide being commissioned.
        r"^(?!.*\b(?:bug|defect|repro|crash(?:es|ed|ing)?|incident)\b)"
        r".*\b(?:written|writing) (?:up|down)\b",
    ],
}

# A documentation noun still carries Doc framing when a compound name sits
# between the verb and the noun ("write an ingest pipeline runbook"), which the
# fixed adjective list above cannot reach.
GENERIC_DOC_FRAME_RE = re.compile(
    rf"\b{DOC_AUTHOR_VERBS} (an? )?(?:[a-z0-9][\w+./-]* ){{0,5}}(documentation|docs|document|guide|reference|catalog|runbook|proposal|recommendation|decision record)\b"
)
# A bug report whose subject is the documentation is still a bug report.
BUG_ABOUT_DOCUMENTATION_RE = re.compile(
    r"\b(create|write|file) (a )?(bug report|defect report) (about|for|covering|on)\b[^.!?]{0,80}\b(documentation|docs|document|guide|reference)\b"
)
# A user story named as another artifact's subject is not PRD framing.
STORY_AS_SUBJECT_RE = re.compile(
    r"\b(?:bug report|defect report|document|documentation)\b[^.!?]{0,80}\b(?:user )?stor(?:y|ies)\b"
)
# A negated action is not a request for the artifact it names.
NEGATED_PRD_RE = re.compile(
    r"\b(?:do not|don'?t|never|not)\s+(?:write|create|draft)\b[^.!?]{0,40}\b(?:prd|stor(?:y|ies))\b"
)
# "task for/about the docs" and "task to write a PRD" name the other artifact as
# the task's subject, not a second artifact to produce, so the task keeps the
# route. "task and ... guide" stays a genuine multi-artifact conflict.
TASK_OVER_OTHER_RE = re.compile(
    r"\b(task|subtask|parent task)\s+(?:to\s+(?:document|write|create|draft|refine)|(?:for|about|covering|on))\b"
)


# Semantic topics (word-boundary, inflection-aware). Nine topics, weighting and
# confidence overrides all mirror SKILL.md's SEMANTIC_TOPICS: documentation and
# PRD synonyms carry a 0.85 override so a genuine hit routes directly instead of
# needing four keyword hits like the unweighted topics. Insertion order is the
# tie-break, so it is part of the contract and must stay as written.
SEMANTIC_TOPICS: Dict[str, Dict[str, Any]] = {
    "bug": {
        "synonyms": ["bug", "fix", "issue", "defect", "error", "broken", "crash", "failing", "repro"],
        "intent": "BUG",
    },
    "feature": {
        "synonyms": ["capability", "enhancement", "functionality", "new", "add"],
        "intent": "TASK",
    },
    "acceptance": {
        "synonyms": ["criteria", "definition of done", "validation", "success condition"],
        "intent": "TASK",
    },
    "user_need": {
        "synonyms": ["user need", "persona", "journey", "workflow", "as a user"],
        "intent": "TASK",
    },
    "technical_task": {
        "synonyms": ["refactor", "optimize", "debt", "cleanup", "update dependency"],
        "intent": "TASK",
    },
    "integration": {
        "synonyms": ["api", "connect", "sync", "webhook", "third-party"],
        "intent": "TASK",
    },
    "ui_refinement": {
        "synonyms": ["feedback", "polish", "tidy up", "clean up", "tighten up", "design parity", "Figma alignment", "visual QA", "UI tweak", "spacing", "alignment", "wording", "label", "capitalisation", "capitalization", "capitalised", "capitalized", "casing", "sentence case", "title case", "consistent", "consistency", "inconsistent", "inconsistently", "figma"],
        "intent": "TASK",
        "confidence": 0.80,
    },
    "documentation": {
        "synonyms": ["document how", "write a guide", "create a catalog", "behavior reference", "product documentation", "engineering documentation", "engineering docs", "technical documentation", "technical docs", "api documentation", "api docs", "api reference", "schema documentation", "schema docs", "schema reference", "system behavior reference", "architecture document", "architecture documentation", "architecture docs", "architecture recommendation", "implementation guide", "configuration guide", "runbook", "troubleshooting guide", "technical proposal", "technical recommendation", "decision record", "future-state proposal", "refine this document"],
        "intent": "DOC",
        "confidence": 0.85,
    },
    "prd": {
        "synonyms": ["prd", "product requirements document", "user story", "write a story", "story for", "epic story", "epic", "write an epic", "create an epic", "epic for", "refine this epic", "acceptance scenarios", "given when then", "connextra", "definition of ready", "refine this story", "turn this into a story", "write a prd", "refine this prd", "draft for pm", "write a draft", "make a draft", "story", "changing how", "change how", "changing the way", "change the way"],
        "intent": "STORY",
        "confidence": 0.85,
    },
}

# UI feedback stays Task even when "fix" or "broken" co-occurs, because Bug Mode
# is reserved for unexpected system behavior, not visual polish.
#
# Two synonym families above close a gap the phrase-gap fix could not reach:
# it helps a request that contains the artifact word, and these are requests
# that never name one. Polish and consistency wording ("capitalised
# inconsistently ... make it consistent", "tidy up the button labels") is
# ordinary backlog intake and scores through ui_refinement instead of arriving
# at Task only by the quick-energy fallback. Behaviour-change wording ("we're
# changing how creator ratings work") is a PRD request with no artifact noun in
# it, and bare "story" joins the compound phrases so "one story or several"
# scores the way bare "epic" already does.
#
# Both families are written as the vocabulary rather than as the sentences a
# probe set happened to contain. An earlier pass listed "tidy up the copy",
# "make it consistent" and "inconsistent copy" as whole phrases, which routed
# those exact sentences and left "tidy up the labels" in the fallback. The
# stems "tidy up", "clean up", "consistent" and "inconsistent" carry the same
# intent across the wordings people actually type. Generic terms like
# "padding" and "copy" alone stay out, because they occur just as often in
# unrelated bug and documentation requests, and so do the initiative verbs
# redesign, rework, revamp and overhaul, because one of them in a defect
# report ("redesign the export button, it is broken and crashing") would
# outscore three bug terms.
UI_BUG_COOCURRENCE_TERMS = ["fix", "broken", "issue", "defect"]

# A `$token` is a routing control, not subject matter, so it is stripped before
# semantic scoring. Without this a false prefix like `$epics` or `$prds` leaks a
# keyword hit that no command was allowed to fire, and a statement about epics
# routes as a request to write one. The lookbehind keeps the strip to tokens
# that start a whitespace-delimited word, so a price like `us$500` survives.
SEMANTIC_TOKEN_STRIP_RE = re.compile(r"(?<!\S)\$[a-z][\w.-]*")

CONFIDENCE_THRESHOLDS = {"HIGH": 0.85, "MEDIUM": 0.60, "LOW": 0.40}

# ---------------------------------------------------------------------------
# Route object schema (fixed field set; unknown or duplicate fields reject)
# ---------------------------------------------------------------------------

ROUTE_FIELDS = ["intent", "energy", "source", "shape", "confidence", "needs_disambiguation", "resources", "on_demand"]

INTENT_VALUES = ["TASK", "BUG", "DOC", "STORY", "INTERACTIVE"]
# Only the Story intent carries a shape. Every other route leaves it None, so
# a shape appearing on a Task or Doc route is a bug the schema catches.
SHAPE_VALUES = ["STORY", "EPIC", None]
ENERGY_VALUES = ["QUICK", "STANDARD"]
SOURCE_VALUES = ["command", "framing", "semantic", "fallback", "quick-fallback", "conflict"]

# --- Runtime discovery + guarded loading (resilient router mechanics) ---
# Resource names below are resolved against the actual skill inventory at
# every call, so a renamed or deleted reference degrades to a smaller
# resource set instead of a dead path or a crash.
SKILL_ROOT = Path(__file__).resolve().parent.parent.parent / "sk-product-owner"
RESOURCE_BASES = ("references", "assets")

# The Human Voice card carries every hard blocker inline, so the terms are in
# view while writing. The conciseness layer sits above it, governing quantity
# and structure where the card governs word choice, and both are preloaded
# because a length problem cannot be caught by a term list. The full standard
# behind the card stays out of the always-on tier and loads only to
# adjudicate a borderline term or run a scored pass.
ALWAYS = ["references/hvr-core.md", "references/conciseness.md"]
ON_DEMAND = ["references/human-voice-rules.md"]
RESOURCE_MAP: Dict[str, List[str]] = {
    "TASK": ["references/task-mode.md", "assets/task-templates.md"],
    "BUG": ["references/bug-mode.md", "assets/bug-report-template.md"],
    "DOC": ["references/doc-mode.md", "assets/doc-templates.md"],
    "STORY": ["references/story-mode.md"],
    "INTERACTIVE": ["references/interactive-mode.md", "assets/interactive-response-templates.md"],
}

# The one scaffold each Story shape loads beside the mode reference. Splitting
# the shapes into their own files is what lets the CONDITIONAL tier stay a
# reference plus one template: a Story request no longer pays for the Epic
# scaffold it will never read.
SHAPE_TEMPLATES: Dict[str, str] = {
    "STORY": "assets/story-template.md",
    "EPIC": "assets/epic-template.md",
}

# One consolidated intake question governs every ambiguous or conflicting
# turn: the router asks once, then waits, and never guesses the artifact.
DISAMBIGUATION_CHECKLIST = [
    "Confirm whether the user needs a task, subtask, parent task, bug report, user story or product/engineering document",
    "Confirm scope, platform, user value and desired outcome",
    "Ask for evidence or reproduction steps when bug indicators appear",
    "For documentation, confirm purpose, audience, source authority and source classification",
    "Ask one consolidated question, then wait",
]


def _guard_in_skill(relative_path: str) -> str:
    # .absolute() (not .resolve()) so this stays lexical and never dereferences
    # references/human-voice-rules.md, which is a relative symlink to a shared
    # global three directories up in z - Knowledge/. Resolving it would land
    # outside SKILL_ROOT and fail the guard for a routable resource.
    resolved = (SKILL_ROOT / relative_path).absolute()
    resolved.relative_to(SKILL_ROOT.absolute())
    if resolved.suffix.lower() != ".md":
        raise ValueError(f"Only markdown resources are routable: {relative_path}")
    return resolved.relative_to(SKILL_ROOT.absolute()).as_posix()


def discover_resource_inventory() -> Set[str]:
    """Return routable markdown paths under references/ and assets/.

    A missing base contributes nothing instead of raising. Symlinked files
    (the shared Human Voice Rules global) resolve through `is_file()` for the
    existence check without dereferencing the path itself, so the guard fence
    in `_guard_in_skill` never has to walk outside `SKILL_ROOT`.
    """
    inventory: Set[str] = set()
    for base_name in RESOURCE_BASES:
        base = SKILL_ROOT / base_name
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            if path.is_file():
                inventory.add(path.relative_to(SKILL_ROOT).as_posix())
    return inventory


def guard_resources(names: List[str], inventory: Set[str]) -> List[str]:
    """Keep only resources that exist in the current inventory, dedupe, keep order."""
    seen: Set[str] = set()
    kept: List[str] = []
    for name in names:
        guarded = _guard_in_skill(name)
        if guarded in inventory and guarded not in seen:
            seen.add(guarded)
            kept.append(guarded)
    return kept


def conditional_for(intent: str, shape: Optional[str]) -> List[str]:
    """The routed lane: one mode reference, plus one scaffold on the Story lane."""
    lane = list(RESOURCE_MAP.get(intent, []))
    if intent == "STORY" and shape in SHAPE_TEMPLATES:
        lane.append(SHAPE_TEMPLATES[shape])
    return lane


def resources_for(intent: str, shape: Optional[str] = None) -> List[str]:
    inventory = discover_resource_inventory()
    return guard_resources(list(ALWAYS) + conditional_for(intent, shape), inventory)


def on_demand_for(intent: str, shape: Optional[str] = None) -> List[str]:
    """Resources the route names but does not preload.

    Carried on the route object so the demotion is asserted, not assumed: a
    fixture can prove the full standard stayed out of `resources` and stayed
    reachable in `on_demand`, and a later promotion back into the always-on
    tier fails the gate instead of passing silently.
    """
    inventory = discover_resource_inventory()
    preloaded = set(resources_for(intent, shape))
    return [name for name in guard_resources(list(ON_DEMAND), inventory) if name not in preloaded]


# ---------------------------------------------------------------------------
# Tokenization + detection
# ---------------------------------------------------------------------------

def has_exact_token(text: str, token: str) -> bool:
    """Whole-token match only. `$doc` never fires inside `$document`."""
    pattern = rf"{TOKEN_START}{re.escape(token)}{TOKEN_END}"
    return bool(re.search(pattern, text, flags=re.IGNORECASE))


def detect_commands(text: str) -> Set[str]:
    """Every exact artifact command present, never a substring `in` test."""
    found: Set[str] = set()
    if re.search(rf"{TOKEN_START}\$task\s+--subtask{TOKEN_END}", text, flags=re.IGNORECASE):
        found.add("TASK")
    for token, intent in ARTIFACT_COMMANDS.items():
        if has_exact_token(text, token):
            found.add(intent)
    return found


def detect_energy(text: str) -> str:
    if has_exact_token(text, "$quick") or has_exact_token(text, "$q"):
        return "QUICK"
    if NATURAL_QUICK_RE.search(text) and not NEGATED_QUICK_RE.search(text):
        return "QUICK"
    return "STANDARD"


def detect_framing(text: str) -> Optional[str]:
    """Artifact framing, word-boundary phrase match. Returns 'CONFLICT' for two+.

    Matching runs on lowercased text rather than a case-insensitive pass so a
    character class written for lowercase input keeps its intended span.
    """
    text_lower = " ".join(text.lower().split())
    matches = {
        intent for intent, patterns in FRAME_PATTERNS.items()
        if any(re.search(pattern, text_lower) for pattern in patterns)
    }
    if GENERIC_DOC_FRAME_RE.search(text_lower) and not (
        matches == {"BUG"} and BUG_ABOUT_DOCUMENTATION_RE.search(text_lower)
    ):
        matches.add("DOC")
    if "STORY" in matches and len(matches) > 1 and STORY_AS_SUBJECT_RE.search(text_lower):
        matches.discard("STORY")
    if "STORY" in matches and NEGATED_PRD_RE.search(text_lower):
        matches.discard("STORY")
    if TASK_OVER_OTHER_RE.search(text_lower) and "TASK" in matches:
        return "TASK"
    if len(matches) > 1:
        return "CONFLICT"
    return next(iter(matches)) if matches else None


def resolve_shape(intent: str, text: str) -> Optional[str]:
    """Which Story scaffold the request asked for, or None off the Story lane.

    Command first, because an explicit command wins over every
    natural-language signal. Then framing, read in precedence order. Then the
    Story default, which is the majority case and the only shape a semantic
    route can honestly claim, since a topic score names the lane rather than
    the shape.
    """
    if intent != "STORY":
        return None
    normalized = " ".join((text or "").split())
    for shape in SHAPE_PRECEDENCE:
        if any(has_exact_token(normalized, token)
               for token, mapped in SHAPE_COMMANDS.items() if mapped == shape):
            return shape
    lowered = normalized.lower()
    for shape in SHAPE_PRECEDENCE:
        if any(re.search(pattern, lowered) for pattern in SHAPE_FRAMES[shape]):
            return shape
    return "STORY"


def score_semantic_topics(text: str) -> Tuple[str, float, str]:
    """Word-boundary, inflection-aware keyword scores per topic.

    Never substring: `\\bbug\\b` matches "file a bug" but not "debugging",
    because the boundary before/after "bug" fails inside a longer word. A
    multi-word synonym goes through `phrase_pattern`, so an adjective between
    its words no longer costs the hit. `$token` text is removed first, so a
    routing control never contributes a topic hit as if it were prose.
    Returns (topic, score, intent) for the highest-scoring topic, ties going to
    the earliest topic in table order.
    """
    semantic_text = SEMANTIC_TOKEN_STRIP_RE.sub(" ", " ".join(text.lower().split()))
    best_topic, best_score = next(iter(SEMANTIC_TOPICS)), 0.0
    for topic, cfg in SEMANTIC_TOPICS.items():
        hits = sum(
            1 for synonym in cfg["synonyms"]
            if re.search(phrase_pattern(synonym.lower()), semantic_text)
        )
        score = min(0.95, hits * 0.25)
        if hits and cfg.get("confidence"):
            score = max(score, cfg["confidence"])
        if topic == "ui_refinement" and hits:
            if any(re.search(phrase_pattern(term), semantic_text) for term in UI_BUG_COOCURRENCE_TERMS):
                score = max(score, cfg.get("confidence", 0.80))
        if score > best_score:
            best_topic, best_score = topic, score
    return best_topic, best_score, SEMANTIC_TOPICS[best_topic]["intent"]


# ---------------------------------------------------------------------------
# Route resolution + schema validation
# ---------------------------------------------------------------------------

def _route(intent: str, energy: str, source: str, confidence: Optional[float],
           needs_disambiguation: bool, text: str = "") -> Dict[str, Any]:
    shape = resolve_shape(intent, text)
    return {
        "intent": intent,
        "energy": energy,
        "source": source,
        "shape": shape,
        "confidence": confidence,
        "needs_disambiguation": needs_disambiguation,
        "resources": resources_for(intent, shape),
        "on_demand": on_demand_for(intent, shape),
    }


def route_request(text: str) -> Dict[str, Any]:
    normalized = " ".join((text or "").split())
    energy = detect_energy(normalized)

    commands = detect_commands(normalized)
    if len(commands) > 1:
        return _route("INTERACTIVE", energy, "conflict", None, True, normalized)
    if len(commands) == 1:
        return _route(next(iter(commands)), energy, "command", None, False, normalized)

    frame = detect_framing(normalized)
    if frame == "CONFLICT":
        return _route("INTERACTIVE", energy, "conflict", None, True, normalized)
    if frame:
        return _route(frame, energy, "framing", None, False, normalized)

    _, score, intent = score_semantic_topics(normalized)

    # Standard energy routes directly at MEDIUM (0.60) and above, and asks one
    # question below it. Quick energy trusts the same score down to LOW
    # (0.40), and only below that falls back to Task, its narrow safe default
    # per SKILL.md's Detection Sequence rule 12 ("`$quick`/`$q` without
    # another detectable artifact retains the narrow Task fallback").
    if energy == "QUICK":
        if score >= CONFIDENCE_THRESHOLDS["LOW"]:
            return _route(intent, energy, "semantic", score, False, normalized)
        return _route("TASK", energy, "quick-fallback", score, False, normalized)

    if score >= CONFIDENCE_THRESHOLDS["MEDIUM"]:
        return _route(intent, energy, "semantic", score, False, normalized)
    return _route("INTERACTIVE", energy, "fallback", score, True, normalized)


def validate_route_object(obj: Dict[str, Any]) -> List[str]:
    """Reject unknown or duplicate fields and invalid enum values.

    Returns a list of violations (empty when the object is schema-valid).
    """
    errors: List[str] = []
    if not isinstance(obj, dict):
        return ["route object is not a dict"]
    if list(obj.keys()) != ROUTE_FIELDS:
        missing = [f for f in ROUTE_FIELDS if f not in obj]
        extra = [k for k in obj if k not in ROUTE_FIELDS]
        if missing:
            errors.append(f"missing fields: {missing}")
        if extra:
            errors.append(f"unknown fields: {extra}")
    if obj.get("intent") not in INTENT_VALUES:
        errors.append(f"bad intent: {obj.get('intent')}")
    if obj.get("energy") not in ENERGY_VALUES:
        errors.append(f"bad energy: {obj.get('energy')}")
    if obj.get("source") not in SOURCE_VALUES:
        errors.append(f"bad source: {obj.get('source')}")
    if obj.get("shape") not in SHAPE_VALUES:
        errors.append(f"bad shape: {obj.get('shape')}")
    if obj.get("shape") is not None and obj.get("intent") != "STORY":
        errors.append(f"shape on a non-Story route: {obj.get('intent')}")
    if obj.get("shape") is None and obj.get("intent") == "STORY":
        errors.append("Story route resolved no shape, so no scaffold would load")
    confidence = obj.get("confidence")
    if confidence is not None and not (isinstance(confidence, (int, float)) and 0.0 <= confidence <= 1.0):
        errors.append(f"bad confidence: {confidence!r}")
    if not isinstance(obj.get("needs_disambiguation"), bool):
        errors.append("needs_disambiguation must be a bool")
    if not isinstance(obj.get("resources"), list):
        errors.append("resources must be a list")
    on_demand = obj.get("on_demand")
    if not isinstance(on_demand, list):
        errors.append("on_demand must be a list")
    elif set(on_demand) & set(obj.get("resources") or []):
        errors.append("on_demand overlaps resources: a preloaded file is not on demand")
    return errors


# ---------------------------------------------------------------------------
# Fixture runner
# ---------------------------------------------------------------------------

def load_fixtures(path: str) -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def _check_duplicate_json_keys(path: str) -> List[str]:
    """Reject duplicate keys inside any single JSON object in the fixture file.

    json.load silently keeps the last duplicate, which would let a typo'd
    override pass; scan per object so the manifest cannot drift silently.
    """
    def _pairs(pairs):
        seen = {}
        for k, v in pairs:
            if k in seen:
                raise ValueError(f"duplicate key {k!r} in object")
            seen[k] = v
        return seen

    errors = []
    with open(path, "r", encoding="utf-8") as fh:
        raw = fh.read()
    try:
        json.loads(raw, object_pairs_hook=_pairs)
    except ValueError as exc:
        errors.append(str(exc))
    return errors


def run_fixtures(fixtures: List[Dict[str, Any]], source_path: Optional[str] = None) -> Tuple[int, List[str]]:
    failures: List[str] = []
    if source_path:
        failures.extend(_check_duplicate_json_keys(source_path))
    for idx, fx in enumerate(fixtures, start=1):
        inp = fx["input"]
        expect = fx["expect"]
        unknown = [k for k in expect if k not in ROUTE_FIELDS]
        if unknown:
            failures.append(f"fixture {idx} unknown expect fields: {unknown}")
        actual = route_request(inp)
        schema_errors = validate_route_object(actual)
        if schema_errors:
            failures.append(f"fixture {idx} schema: {schema_errors}")
            continue
        for field in ROUTE_FIELDS:
            if field not in expect:
                continue
            if actual.get(field) != expect[field]:
                failures.append(
                    f"fixture {idx} field {field}: expected {expect[field]!r}, got {actual.get(field)!r}"
                )
    return len(failures), failures


# The self-check is a smoke test of the router, not of the schema. One sample per
# detection layer, each with the outcome the contract owes it, because a
# schema-only self-check passed a router patched to send every request to
# INTERACTIVE with a fallback source. Every expectation below is stated by the
# skill's own routing table, so a sample that stops matching is either a router
# regression or a routing change that has to be made deliberately.
SELF_CHECK_SAMPLES = [
    # A concrete addition with no command word routes on the feature topic.
    ("add a new capability with more functionality for filters", {"intent": "TASK", "source": "semantic"}),
    # An explicit command beats every framing signal in the same string.
    ("$doc write a bug report about the outage", {"intent": "DOC", "source": "command"}),
    # A token that only looks like a command fires none, so the request falls
    # through to the semantic and framing layers instead.
    ("$document is the filename I meant", {"source": "fallback"}),
    # Quick energy is extracted before the artifact intent.
    ("$quick $bug the login screen hangs", {"intent": "BUG", "energy": "QUICK"}),
    # An unroutable request asks rather than guessing.
    ("thoughts?", {"intent": "INTERACTIVE", "needs_disambiguation": True}),
]


def run_self_check() -> Tuple[int, List[str]]:
    """Route each sample and compare it with the outcome the contract owes."""
    failures: List[str] = []
    for text, expect in SELF_CHECK_SAMPLES:
        actual = route_request(text)
        errs = validate_route_object(actual)
        if errs:
            failures.append(f"self-check {text!r} schema: {errs}")
            continue
        for field, value in expect.items():
            if actual.get(field) != value:
                failures.append(
                    f"self-check {text!r} field {field}: expected {value!r}, got {actual.get(field)!r}"
                )
    return len(failures), failures


def main(argv: List[str]) -> int:
    usage = 'usage: route_contract.py <fixtures.json | --self-check | --request "text">'
    if len(argv) == 3 and argv[1] == "--request":
        obj = route_request(argv[2])
        errs = validate_route_object(obj)
        print(json.dumps(obj, indent=2, ensure_ascii=False))
        if errs:
            print("SCHEMA ERRORS:", errs, file=sys.stderr)
            return 1
        return 0
    if len(argv) != 2:
        print(usage)
        return 2
    arg = argv[1]
    if arg == "--self-check":
        count, failures = run_self_check()
        if failures:
            print(f"SELF-CHECK FAILED {count} expectation(s)", file=sys.stderr)
            for failure in failures:
                print(" -", failure, file=sys.stderr)
            return 1
        print(f"self-check passed {len(SELF_CHECK_SAMPLES)} routing expectations")
        return 0
    # The positional argument is the fixture manifest and nothing else. It used
    # to fall through to routing the argument as a request string, which turned a
    # renamed, moved or deleted manifest into a green run that validated no
    # fixture at all, and `run_fixtures.sh` calls this with a bare filename. A
    # request to inspect goes through --request, where a typo cannot be mistaken
    # for a gate pass.
    if not Path(arg).is_file():
        print(f"not a fixtures file: {arg}", file=sys.stderr)
        print(usage, file=sys.stderr)
        return 2
    try:
        fixtures = load_fixtures(arg)
    except json.JSONDecodeError as exc:
        print(f"invalid fixtures JSON: {exc}", file=sys.stderr)
        return 2
    count, failures = run_fixtures(fixtures, arg)
    if failures:
        print(f"FAILED {count}/{len(fixtures)}")
        for f in failures:
            print(" -", f)
        return 1
    print(f"PASSED {len(fixtures)}/{len(fixtures)} fixtures")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
