---
title: "Product Owner - Router Contract - v0.100"
description: "The Smart Router as running Python: primary detection, phase order, the semantic topic tables, confidence thresholds, resource loading and Story/Epic shape resolution, expressed as the exact algorithm benchmark/router/route_contract.py is checked against. SKILL.md carries the prose summary this file backs. ON_DEMAND for a reader who needs the precise regex or scoring behavior rather than the rule."
version: "0.100"
contextType: reference
importance_tier: medium
trigger_phrases:
  - "router contract"
  - "smart router pseudocode"
  - "exact routing algorithm"
  - "how does the router work"
  - "route_contract.py"
---

# Product Owner - Router Contract - v0.100

The Smart Router expressed as running Python, one level below the prose routing rules in `SKILL.md` Section 2. This is the algorithm those rules summarize, and the exact source `benchmark/router/differential.py` executes to prove `benchmark/router/route_contract.py` never drifts from it.

**Loading Condition:** ON-DEMAND
**Purpose:** Provides the exact router algorithm, primary detection, phase order, semantic scoring, confidence thresholds, resource loading and Story/Epic shape resolution, for a reader who needs the precise regex or scoring behavior rather than the summarized rule
**Scope:** Primary detection, phase order, semantic topic scoring, confidence thresholds, resource loading, Story/Epic shape resolution and the Doc context gate
**Output Path:** None. This file decides which resources a request loads, and writes no artifact
**Loads With:** nothing. It is read alone, one level below the prose routing rules in `SKILL.md` Section 2, when a request needs the exact algorithm rather than the rule
**Routed By:** nothing automatic. A reader opens it deliberately, and `benchmark/router/differential.py` extracts its Python fence on every gate run to prove `benchmark/router/route_contract.py` never drifts from it
**Hands Off To:** nothing. It is the leaf authority that `SKILL.md` Section 2 summarizes, and the resource map inside it names the mode reference each route loads

---

## 1. OVERVIEW

### Purpose

The Smart Router expressed as running Python, one level below the prose routing rules in `SKILL.md` Section 2. This is the algorithm those rules summarize, and the exact source `benchmark/router/differential.py` executes to prove `benchmark/router/route_contract.py` never drifts from it.

---

## 2. ROUTER ALGORITHM

### Smart Router Pseudocode

```python
import re
from pathlib import Path
from types import SimpleNamespace
from typing import Optional

SKILL_ROOT = Path(__file__).resolve().parent
RESOURCE_BASES = (SKILL_ROOT / "references", SKILL_ROOT / "assets")
DEFAULT_RESOURCE = "references/interactive-mode.md"
CONFIDENCE_THRESHOLDS = {"HIGH": 0.85, "MEDIUM": 0.60, "LOW": 0.40}
TOKEN_START = r"(?<![\w$])"
TOKEN_END = r"(?![\w$/-]|\.[\w])"
# Real requests qualify the artifact noun: "write a full story", "a proper
# PRD", "turn this into a quick story". Matching a multi-word phrase as an
# exact adjacent run let one inserted adjective drop a confident route past
# the HIGH, MEDIUM and LOW bands straight into the fallback, so every gap
# inside a phrase absorbs a bounded run of intervening words. The bound is
# what keeps it honest. One word per gap is an adjective or an article, and
# the gap is whitespace-separated word characters only, so it can never reach
# across a comma or a full stop to pull an artifact noun out of another
# clause.
PHRASE_GAP_WORDS = 1
PHRASE_GAP = rf"\s+(?:\w+\s+){{0,{PHRASE_GAP_WORDS}}}"
FRAME_MODIFIER = rf"(?:\w+\s+){{0,{PHRASE_GAP_WORDS}}}"
DOC_SOURCE_CLASSES = {
    "current behavior",
    "approved direction",
    "proposal",
    "retired material",
    "unknown",
}

# Two synonym families below close a gap the phrase-gap fix could not
# reach: it helps a request that contains the artifact word, and these are
# requests that never name one. Polish and consistency wording ("capitalised
# inconsistently ... make it consistent", "tidy up the button labels") is
# ordinary backlog intake and scores through ui_refinement instead of reaching
# Task only by the quick-energy fallback. Behaviour-change wording ("we are
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
# redesign, rework, revamp and overhaul, because one of them inside a defect
# report ("redesign the export button, it is broken and crashing") would
# outscore three bug terms.
SEMANTIC_TOPICS = {
    "bug": {
        "synonyms": ["bug", "fix", "issue", "defect", "error", "broken", "crash", "failing", "repro"],
        "template": "Bug Mode",
    },
    "feature": {
        "synonyms": ["capability", "enhancement", "functionality", "new", "add"],
        "template": "Task Mode",
    },
    "acceptance": {
        "synonyms": ["criteria", "definition of done", "validation", "success condition"],
        "template": "Task Mode",
    },
    "user_need": {
        "synonyms": ["user need", "persona", "journey", "workflow", "as a user"],
        "template": "Task Mode",
    },
    "technical_task": {
        "synonyms": ["refactor", "optimize", "debt", "cleanup", "update dependency"],
        "template": "Task Mode",
    },
    "integration": {
        "synonyms": ["api", "connect", "sync", "webhook", "third-party"],
        "template": "Task Mode",
    },
    "ui_refinement": {
        "synonyms": ["feedback", "polish", "tidy up", "clean up", "tighten up", "design parity", "Figma alignment", "visual QA", "UI tweak", "spacing", "alignment", "wording", "label", "capitalisation", "capitalization", "capitalised", "capitalized", "casing", "sentence case", "title case", "consistent", "consistency", "inconsistent", "inconsistently", "figma"],
        "template": "Task Mode",
        "confidence": 0.80,
    },
    "documentation": {
        "synonyms": ["document how", "write a guide", "create a catalog", "behavior reference", "product documentation", "engineering documentation", "engineering docs", "technical documentation", "technical docs", "api documentation", "api docs", "api reference", "schema documentation", "schema docs", "schema reference", "system behavior reference", "architecture document", "architecture documentation", "architecture docs", "architecture recommendation", "implementation guide", "configuration guide", "runbook", "troubleshooting guide", "technical proposal", "technical recommendation", "decision record", "future-state proposal", "refine this document"],
        "template": "Doc Mode",
        "confidence": 0.85,
    },
    "prd": {
        "synonyms": ["prd", "product requirements document", "user story", "write a story", "story for", "epic story", "epic", "write an epic", "create an epic", "epic for", "refine this epic", "acceptance scenarios", "given when then", "connextra", "definition of ready", "refine this story", "turn this into a story", "write a prd", "refine this prd", "draft for pm", "write a draft", "make a draft", "story", "changing how", "change how", "changing the way", "change the way"],
        "template": "Story Mode",
        "confidence": 0.85,
    },
}

RESOURCE_MAP = {
    "ALWAYS": [
        "sk-product-owner/SKILL.md",
        "references/hvr-core.md",
        "references/conciseness.md",
    ],
    "TASK": ["references/task-mode.md", "assets/task-templates.md"],
    "BUG": ["references/bug-mode.md", "assets/bug-report-template.md"],
    "DOC": ["references/doc-mode.md", "assets/doc-templates.md"],
    "STORY": ["references/story-mode.md"],
    "INTERACTIVE": ["references/interactive-mode.md", "assets/interactive-response-templates.md"],
    "ON_DEMAND": ["references/human-voice-rules.md"],
}

# Which shape each Story command selects, and the one scaffold that shape
# loads beside the mode reference. The intent picks the mode reference and the
# shape picks the scaffold, so a Story request never carries the Epic scaffold
# it will not read.
SHAPE_COMMANDS = {
    "$story": "STORY", "$s": "STORY",
    "$prd": "STORY", "$p": "STORY",
    "$epic": "EPIC", "$e": "EPIC",
}
SHAPE_TEMPLATES = {
    "STORY": "assets/story-template.md",
    "EPIC": "assets/epic-template.md",
}
# Most specific shape first. An epic noun names the initiative, and every
# other requirements framing is a Story.
SHAPE_PRECEDENCE = ("EPIC", "STORY")

# Story-lane framing, grouped by the shape each group names. The groups are
# the one copy: detect_artifact_frame flattens them for intent detection and
# resolve_shape reads them in precedence order for shape detection, so a
# pattern can never say one thing to the intent and another to the shape.
SHAPE_FRAMES = {
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

# Commissioning a document is not always phrased as writing one. "Put together
# a reference for the webhook payloads" and "prepare the on-call runbook" are
# the same request as "write" one, so the verb list is the family rather than
# the three verbs the earlier probe set happened to use.
DOC_AUTHOR_VERBS = r"(write|create|draft|put together|pull together|prepare|assemble)"

UNKNOWN_FALLBACK_CHECKLIST = [
    "Confirm whether the user needs a task, subtask, parent task, bug report, user story or product/engineering document",
    "Confirm scope, platform, user value and desired outcome",
    "Ask for evidence or reproduction steps when bug indicators appear",
    "For documentation, confirm purpose, audience, source authority and source classification",
    "Ask one consolidated question, then wait",
]

def discover_markdown_resources() -> set[str]:
    docs = []
    for base in RESOURCE_BASES:
        if base.exists():
            docs.extend(path for path in base.rglob("*.md") if path.is_file())
    return {doc.relative_to(SKILL_ROOT).as_posix() for doc in docs}

def load_if_available(relative_path: str, inventory: set[str], loaded: list[str], seen: set[str]) -> None:
    candidate = (SKILL_ROOT / relative_path).absolute()
    candidate.relative_to(SKILL_ROOT.absolute())
    if relative_path in inventory and relative_path not in seen:
        load(relative_path)
        loaded.append(relative_path)
        seen.add(relative_path)

def has_exact_token(text: str, token: str) -> bool:
    pattern = rf"{TOKEN_START}{re.escape(token)}{TOKEN_END}"
    return bool(re.search(pattern, text, flags=re.IGNORECASE))

def phrase_pattern(phrase: str) -> str:
    # A single-word synonym is unchanged, so "bug" still matches "file a bug"
    # and never "debugging". A multi-word synonym keeps its word order and its
    # outer boundaries and only tolerates the qualifier a person writes
    # between the words.
    words = [re.escape(word) for word in phrase.split()]
    return r"\b" + PHRASE_GAP.join(words) + r"(?:s|es|ed|ing)?\b"

def detect_controls(text: str) -> dict:
    normalized = " ".join((text or "").split())
    subtask = bool(re.search(
        rf"{TOKEN_START}\$task\s+--subtask{TOKEN_END}",
        normalized,
        flags=re.IGNORECASE,
    ))

    artifact_commands = set()
    if subtask or has_exact_token(normalized, "$task") or has_exact_token(normalized, "$t"):
        artifact_commands.add("TASK")
    if has_exact_token(normalized, "$bug") or has_exact_token(normalized, "$b"):
        artifact_commands.add("BUG")
    if has_exact_token(normalized, "$doc") or has_exact_token(normalized, "$d"):
        artifact_commands.add("DOC")
    if (has_exact_token(normalized, "$story") or has_exact_token(normalized, "$s")
            or has_exact_token(normalized, "$prd") or has_exact_token(normalized, "$p")):
        artifact_commands.add("STORY")
    # $epic/$e is the same Story intent under a different shape rather than a
    # separate intent, so it never conflicts with $story.
    if has_exact_token(normalized, "$epic") or has_exact_token(normalized, "$e"):
        artifact_commands.add("STORY")

    # "quick"/"fast" set energy only when they frame the request itself; as subject
    # matter ("crashes when scrolling fast") they must not skip intake gates.
    natural_quick = bool(re.search(
        r"^(?:please\s+)?(?:quick|fast)\b"
        r"|\b(?:quick|fast)\s+(?:task|subtask|bug|doc|document|draft|version|pass|one|check|write-?up)\b"
        r"|\b(?:make|keep)\s+(?:it|this|that)\s+(?:quick|fast)\b"
        r"|\bno[ -]?questions\b",
        normalized,
        flags=re.IGNORECASE,
    ))
    if natural_quick and re.search(
        r"\b(?:not|isn'?t|no|never)\s+(?:a\s+|an\s+|the\s+)?(?:quick|fast)\b",
        normalized,
        flags=re.IGNORECASE,
    ):
        natural_quick = False
    quick = has_exact_token(normalized, "$quick") or has_exact_token(normalized, "$q") or natural_quick
    return {
        "artifact_commands": artifact_commands,
        "subtask": subtask,
        "energy": "QUICK" if quick else "STANDARD",
    }

def detect_artifact_frame(text: str) -> Optional[str]:
    text_lower = " ".join(text.lower().split())
    frames = {
        "TASK": [
            r"\b(create|write|open|refine) (a )?(dev |development )?(task|subtask|parent task)\b",
            r"\btask to document\b",
            r"\bacceptance criteria\b",
            # Backlog intake for a concrete addition rarely says "task": "add
            # a deadline badge to the collab card" and "build a toggle row
            # component for notification prefs" name the thing to build
            # directly. Both carry a trailing anchor (the definite article
            # after the preposition, or the literal word "component") so a
            # bare "add this capability" or "add better logging around the
            # retry loop" still falls through to the weaker unweighted
            # feature score instead of a guaranteed direct route.
            r"\badd (?:a |an |another )?[\w'-]+(?:\s+[\w'-]+){0,3} (?:to|on|for|in) the\b",
            r"\bbuild (?:a |an )?[\w'-]+(?:\s+[\w'-]+){0,4} component\b",
            # Its own narrow entry because the surrounding sentence can carry
            # a competing bug word ("search results are slow, need
            # pagination"), and the build ask is what the person is actually
            # asking for.
            r"\bneed(?:s)? (?:\w+\s+){0,1}pagination\b",
        ],
        "BUG": [
            r"\b(create|write|file) (a )?(bug report|defect report)\b",
            r"\bbug report about\b",
            # A symptom report often carries no defect noun at all: "the app
            # crashes on rotate during upload", "the checkout screen freezes
            # when you tap pay twice" and "notifications stop arriving after
            # you background the app" never say bug, issue or error. The verb
            # family below is the vocabulary a person reaches for instead of
            # the noun, a surface that stops responding or a value that comes
            # out wrong, and it requires the verb form rather than the noun so
            # "the checkout crash" stays a subject. It carries a negative
            # lookahead across the whole line for the rest of the bug topic's
            # vocabulary: a report that already names a second symptom
            # (issue, error, defect, repro, or another verb form) already
            # clears the semantic score on its own, so framing stays out of
            # its way rather than overriding a confidence value fixtures
            # already pin. "it is broken, we already filed the defect" and
            # "we should redesign the export button, it is broken and
            # crashing constantly with an error" are exactly that case, and
            # both stay on the semantic path. The second lookahead holds
            # "stop" in its imperative sense, so "we should stop showing the
            # banner" stays a request to change behavior rather than a report
            # that behavior broke.
            r"^(?!.*\b(?:bug|fix(?:es|ed|ing)?|issue|defect|error|broken|failing|repro)\b)"
            r"(?!.*\b(?:should|to|want to|please|can|could|let'?s)\s+stop\b)"
            r".*\b(?:crash(?:es|ed|ing)|freez(?:es|ing)|froze|frozen|hangs|hanging"
            r"|stalls|stalling|glitch(?:es|ing)|locks up|locked up|times out|timed out"
            r"|stops? \w+ing|stopped \w+ing"
            r"|(?:is|are|was|were|looks?|comes? out) (?:completely |totally |just )?"
            r"(?:wrong|incorrect|duplicated|garbled))\b",
            r"^(?!.*\b(?:bug|fix(?:es|ed|ing)?|issue|defect|error|crash(?:es|ed|ing)?|repro)\b).*\b(?:this|it|that)\s+is\s+broken\b",
            # A report can also name the broken value instead of the
            # failure: "the follower count shows -- for tiktok" and "the
            # avatar shows a broken image after upload" have no word from the
            # bug topic's vocabulary in them at all, and the verb is whichever
            # one the surface suggests rather than "shows" alone.
            r"\b(?:shows?|showing|displays?|displaying|renders?|rendering)\s+(?:-{1,2}|nothing|blank|null|undefined)(?!\w)",
            r"\b(?:shows?|showing|displays?|displaying|renders?|rendering)\s+(?:a |an |the )?(?:broken|blank|empty|garbled|corrupted|placeholder)\b",
            # A failing call is named by its status code rather than by a
            # symptom word, and a 4xx or 5xx in a request is always a defect
            # report.
            r"\b(?:returns?|returning|throws?|throwing|gives?|giving)\s+(?:a |an )?[45]\d\d\b",
        ],
        "STORY": [pattern for shape in SHAPE_PRECEDENCE for pattern in SHAPE_FRAMES[shape]],
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
            # Explanation framing can ask for the artifact by function
            # instead of by name: "write up the notification provider
            # comparison" and "something for the team explaining the reel
            # rules" are both documentation requests that never say document,
            # guide or catalog.
            r"\bwrite up (?:the |a |an )?[\w'-]+(?:\s+[\w'-]+){0,4} comparison\b",
            r"\bsomething for (?:the )?(?:team|devs?|developers?|engineers?) explaining\b",
            # The artifact can also be named by what it produces rather than
            # by what it is called: "we need something written down
            # explaining how the payout schedule works" and "the ranking
            # algorithm written up properly" are documentation requests with
            # no documentation noun in them. The whole-line lookahead keeps a
            # defect out of the Doc lane, since "the crash needs writing up"
            # is a bug being filed rather than a guide being commissioned.
            r"^(?!.*\b(?:bug|defect|repro|crash(?:es|ed|ing)?|incident)\b)"
            r".*\b(?:written|writing) (?:up|down)\b",
        ],
    }
    matches = {intent for intent, patterns in frames.items() if any(re.search(pattern, text_lower) for pattern in patterns)}
    generic_doc_frame = bool(re.search(
        rf"\b{DOC_AUTHOR_VERBS} (an? )?(?:[a-z0-9][\w+./-]* ){{0,5}}(documentation|docs|document|guide|reference|catalog|runbook|proposal|recommendation|decision record)\b",
        text_lower,
    ))
    bug_about_documentation = bool(re.search(
        r"\b(create|write|file) (a )?(bug report|defect report) (about|for|covering|on)\b[^.!?]{0,80}\b(documentation|docs|document|guide|reference)\b",
        text_lower,
    ))
    if generic_doc_frame and not (matches == {"BUG"} and bug_about_documentation):
        matches.add("DOC")
    # A user story named as another artifact's subject, or inside a negated
    # action, is not PRD framing; the surviving artifact keeps the route.
    if "STORY" in matches and len(matches) > 1 and re.search(
        r"\b(?:bug report|defect report|document|documentation)\b[^.!?]{0,80}\b(?:user )?stor(?:y|ies)\b",
        text_lower,
    ):
        matches.discard("STORY")
    if "STORY" in matches and re.search(
        r"\b(?:do not|don'?t|never|not)\s+(?:write|create|draft)\b[^.!?]{0,40}\b(?:prd|stor(?:y|ies))\b",
        text_lower,
    ):
        matches.discard("STORY")
    # "task for/about the docs" and "task to write a PRD" name the other
    # artifact as the task's subject, not a second artifact to produce, so the
    # task keeps the route. "task and ... guide" stays a genuine multi-artifact
    # conflict.
    task_over_other = bool(re.search(
        r"\b(task|subtask|parent task)\s+(?:to\s+(?:document|write|create|draft|refine)|(?:for|about|covering|on))\b",
        text_lower,
    ))
    if task_over_other and "TASK" in matches:
        return "TASK"
    if len(matches) > 1:
        return "CONFLICT"
    return next(iter(matches)) if matches else None

def resolve_shape(primary: str, text: str) -> Optional[str]:
    # Command first, because an explicit command wins over every
    # natural-language signal. Then framing, read in precedence order. Then
    # the Story default, which is the majority case and the only shape a
    # semantic route can honestly claim, since a topic score names the lane
    # rather than the shape.
    if primary != "STORY":
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

def score_semantic_topics(text: str) -> list:
    text_lower = text.lower()
    semantic_text = re.sub(r"(?<!\S)\$[a-z][\w.-]*", " ", text_lower)
    scored = []
    for topic, config in SEMANTIC_TOPICS.items():
        # Word-boundary matching with plain inflections: "crashes" and "fixes"
        # still count, but "fix" must not score inside "prefix" or "fixture".
        # Multi-word synonyms go through phrase_pattern, so an adjective
        # between their words no longer costs the hit.
        hits = sum(
            1 for synonym in config["synonyms"]
            if re.search(phrase_pattern(synonym.lower()), semantic_text)
        )
        score = min(0.95, hits * 0.25)
        if hits and config.get("confidence"):
            score = max(score, config["confidence"])
        if topic == "ui_refinement" and hits:
            bug_terms = ["fix", "broken", "issue", "defect"]
            if any(re.search(phrase_pattern(term), semantic_text) for term in bug_terms):
                score = max(score, config.get("confidence", 0.80))
        scored.append(SimpleNamespace(topic=topic, score=score))
    return sorted(scored, key=lambda item: item.score, reverse=True)

def evaluate_doc_context(doc_context: Optional[dict]) -> dict:
    clarification_fields = [
        "create or refine operation",
        "purpose and audience",
        "source set, scoped authority and completed conflict review",
        "current behavior, approved direction, proposal, retired material or unknown status",
        "unresolved contradictions",
        "scope, exclusions and refinement-preservation constraints",
        "the subject of every claim the request asks for, and which supplied source covers it",
    ]
    if doc_context is None:
        return {
            "status": "PENDING",
            "draft_allowed": False,
            "next": "Read the request and sources, then evaluate all Doc contract fields",
            "clarification_fields": clarification_fields,
        }

    required = {
        "purpose_established": "purpose",
        "audience_established": "audience",
        "source_set_established": "source set",
        "source_authority_established": "source authority",
        "conflicts_evaluated": "completed conflict evaluation",
        "scope_established": "scope and exclusions",
    }
    missing = [label for key, label in required.items() if not doc_context.get(key)]
    operation = doc_context.get("operation")
    if operation not in {"create", "refine"}:
        missing.append("create-or-refine operation")

    classifications = set(doc_context.get("source_classifications") or [])
    invalid_classifications = sorted(classifications - DOC_SOURCE_CLASSES)
    if not classifications:
        missing.append("source classification")
    elif invalid_classifications:
        missing.append("valid source classification")

    conflicts = list(doc_context.get("unresolved_conflicts") or [])
    structure_blocked = bool(
        doc_context.get("refinement_requests_structural_change")
        and not doc_context.get("structural_change_authorized")
    )

    # The six booleans above are all procedural: they ask whether a purpose, an
    # audience, a source set, an authority, a conflict review and a scope
    # exist. Every one can be true while the sources say nothing about the
    # thing the document is being asked to claim. A request to compare two
    # services passes all six with a source set that never names either
    # service, and the gate would clear a draft whose entire substance has to
    # be invented. So the subjects the request asks the document to make claims
    # about are matched against the subjects the supplied sources actually
    # cover, and an uncovered subject blocks drafting exactly as an unresolved
    # conflict does. Comparison, migration and before-and-after requests are
    # where this fires most, because each names two subjects and a source set
    # commonly covers one.
    requested_subjects = [
        str(subject).strip().lower()
        for subject in (doc_context.get("requested_claim_subjects") or [])
        if str(subject).strip()
    ]
    covered_subjects = {
        str(subject).strip().lower()
        for subject in (doc_context.get("sourced_subjects") or [])
        if str(subject).strip()
    }
    if not requested_subjects:
        missing.append("subjects the requested claims cover")
    unsourced_subjects = [
        subject for subject in requested_subjects if subject not in covered_subjects
    ]

    if missing or conflicts or structure_blocked or unsourced_subjects:
        return {
            "status": "BLOCKED",
            "draft_allowed": False,
            "missing": missing,
            "conflicts": conflicts,
            "invalid_classifications": invalid_classifications,
            "structure_authority_missing": structure_blocked,
            "unsourced_subjects": unsourced_subjects,
            "clarification": "Ask one consolidated Doc clarification containing every listed field, then wait",
            "clarification_fields": clarification_fields,
        }

    return {"status": "READY", "draft_allowed": True, "clarification_fields": []}

def finalize_artifact_route(
    primary: str,
    energy: str,
    source: str,
    inventory: set[str],
    loaded: list[str],
    seen: set[str],
    doc_context: Optional[dict] = None,
    text: str = "",
    **metadata,
) -> dict:
    for reference in RESOURCE_MAP[primary]:
        load_if_available(reference, inventory, loaded, seen)
    # The Story lane is a mode reference plus exactly one scaffold, resolved
    # before any file is read, so the shapes the request did not ask for never
    # enter context.
    shape = resolve_shape(primary, text)
    if shape:
        load_if_available(SHAPE_TEMPLATES[shape], inventory, loaded, seen)

    result = {
        "intent": primary,
        "energy": energy,
        "source": source,
        "shape": shape,
        "resources": loaded,
        **metadata,
    }
    if primary != "DOC":
        return result

    gate = evaluate_doc_context(doc_context)
    result.update({"doc_gate": gate["status"], "draft_allowed": gate["draft_allowed"]})
    if gate["status"] == "PENDING":
        result["next"] = gate["next"]
        return result
    if gate["status"] == "BLOCKED":
        for reference in RESOURCE_MAP["INTERACTIVE"]:
            load_if_available(reference, inventory, loaded, seen)
        result.update({
            "intent": "INTERACTIVE",
            "requested_intent": "DOC",
            "source": "Doc context gate",
            "clarification": gate["clarification"],
            "clarification_fields": gate["clarification_fields"],
            "doc_gate_details": {
                "missing": gate["missing"],
                "conflicts": gate["conflicts"],
                "invalid_classifications": gate["invalid_classifications"],
                "structure_authority_missing": gate["structure_authority_missing"],
                "unsourced_subjects": gate["unsourced_subjects"],
            },
        })
    return result

def route_product_owner_resources(user_input: str, doc_context: Optional[dict] = None):
    text = user_input or ""
    inventory = discover_markdown_resources()
    loaded = []
    seen = set()
    for reference in RESOURCE_MAP["ALWAYS"]:
        if reference != "sk-product-owner/SKILL.md":
            load_if_available(reference, inventory, loaded, seen)

    controls = detect_controls(text)
    commands = controls["artifact_commands"]
    energy = controls["energy"]

    if len(commands) > 1:
        for reference in RESOURCE_MAP["INTERACTIVE"]:
            load_if_available(reference, inventory, loaded, seen)
        return {
            "intent": "INTERACTIVE",
            "energy": energy,
            "source": "conflicting artifact commands",
            "clarification": "Ask one comprehensive question to select Task, Bug, Doc or Story and, if Doc or Story is selected, gather its contract fields in the same answer; then wait",
            "clarification_fields": [
                "artifact choice",
                "if Doc: purpose, audience, sources, authority and lifecycle status",
                "if Story: role, value, requirements and shared machinery",
                "scope, evidence or preservation constraints for the selected artifact",
            ],
            "resources": loaded,
        }

    if len(commands) == 1:
        primary = next(iter(commands))
        return finalize_artifact_route(
            primary,
            energy,
            "explicit artifact command",
            inventory,
            loaded,
            seen,
            doc_context,
            text,
            subtask=controls["subtask"],
        )

    artifact_frame = detect_artifact_frame(text)
    if artifact_frame == "CONFLICT":
        for reference in RESOURCE_MAP["INTERACTIVE"]:
            load_if_available(reference, inventory, loaded, seen)
        return {
            "intent": "INTERACTIVE",
            "energy": energy,
            "source": "conflicting artifact framing",
            "clarification": "Ask one comprehensive question to select the requested artifact and gather its conditional fields; then wait",
            "resources": loaded,
        }
    if artifact_frame:
        return finalize_artifact_route(
            artifact_frame,
            energy,
            "explicit artifact framing",
            inventory,
            loaded,
            seen,
            doc_context,
            text,
        )

    best = score_semantic_topics(text)[0]
    template = SEMANTIC_TOPICS[best.topic]["template"]
    primary = {"Task Mode": "TASK", "Bug Mode": "BUG", "Doc Mode": "DOC", "Story Mode": "STORY"}.get(template, "TASK")

    if energy == "QUICK":
        quick_primary = primary if best.score >= CONFIDENCE_THRESHOLDS["LOW"] else "TASK"
        quick_source = "quick semantic routing" if best.score >= CONFIDENCE_THRESHOLDS["LOW"] else "quick task fallback"
        return finalize_artifact_route(
            quick_primary,
            energy,
            quick_source,
            inventory,
            loaded,
            seen,
            doc_context,
            text,
            confidence=best.score,
        )

    if best.score >= CONFIDENCE_THRESHOLDS["HIGH"]:
        return finalize_artifact_route(
            primary,
            energy,
            "high-confidence semantic routing",
            inventory,
            loaded,
            seen,
            doc_context,
            text,
            confidence=best.score,
        )

    if best.score >= CONFIDENCE_THRESHOLDS["MEDIUM"]:
        show_user(f"Detected: {template} ({best.score:.0%})")
        return finalize_artifact_route(
            primary,
            energy,
            "medium-confidence semantic routing",
            inventory,
            loaded,
            seen,
            doc_context,
            text,
            confidence=best.score,
        )

    if best.score >= CONFIDENCE_THRESHOLDS["LOW"]:
        for reference in RESOURCE_MAP["INTERACTIVE"]:
            load_if_available(reference, inventory, loaded, seen)
        return {"intent": "INTERACTIVE", "energy": energy, "confidence": best.score, "clarify": template, "resources": loaded}

    for reference in RESOURCE_MAP["INTERACTIVE"]:
        load_if_available(reference, inventory, loaded, seen)
    return {"intent": "INTERACTIVE", "energy": energy, "source": "fallback", "needs_disambiguation": True, "disambiguation_checklist": UNKNOWN_FALLBACK_CHECKLIST, "resources": loaded}
```

---

The kernel points here for the primary detection signal:

Detect the artifact command or framing and select the right mode before consulting deeper Knowledge.

```text
$task | $t                    -> Task Mode
$task --subtask               -> Task Mode (child-task scope)
$bug | $b                     -> Bug Mode
$doc | $d                     -> Doc Mode -> source-authority and conflict gate before draft
$story | $s | $prd | $p       -> Story Mode (Story shape)
$epic | $e                    -> Story Mode (Epic shape)
$quick | $q                   -> energy override only, never an intent. Bare, with no other artifact detected, it retains the narrow Task fallback
2+ artifact commands          -> Interactive Mode (one consolidated question)
no command, framing hit       -> route by artifact framing ("write a task/bug/prd/story/doc ...")
no command, no framing        -> score semantic topics, route by confidence threshold
confidence < LOW (0.40)       -> Interactive Mode (one comprehensive question), except under Quick energy, which keeps the narrow Task fallback
```

The kernel points here for the phase detection order:

1. Normalize case. Extract `$quick` / `$q` or natural quick/fast framing as energy only, never as intent.
2. Detect `$task --subtask` before the bare `$task` command. Both dedupe to Task intent with child-task scope.
3. Collect every exact artifact command (`$task`/`$t`, `$bug`/`$b`, `$doc`/`$d`, `$story`/`$s`/`$prd`/`$p`, `$epic`/`$e`) instead of stopping at the first match. More than one collected command is a conflict routed to one consolidated question. `$epic`/`$e` select the Epic shape and never conflict with the `$story`/`$s`/`$prd`/`$p` Story commands, since both select Story Mode and differ only in the one scaffold they consult. `$document`, `$docs`, `$debug`, `$prds`, `$stories`, `$epics`, embedded aliases and filename-like tokens such as `$d.md` are ordinary text, never commands. Punctuation-delimited commands such as `$d,` remain valid.
4. With exactly one command, it wins over any natural-language wording. `$quick $doc` and `$doc $quick` both mean Doc intent with Quick energy. The same order rule applies to `$quick $prd`, `$quick $story` and `$quick $epic`.
5. With no command, detect artifact framing ("write a task/bug/PRD/doc ..."). Framing beats subject nouns and semantic scores, and more than one framing match is also a conflict. "Create a task to document X" is Task, "bug report about documentation" is Bug, and "document bug behavior" is Doc. A clear write/create/draft request whose object is documentation, docs, a document, guide, reference, catalog, runbook, proposal, recommendation or decision record routes to Doc regardless of subject modifiers (developer, API, endpoint, deployment, debugging, SDK, CLI, integration, infrastructure or service). Explicit Task or Bug framing still wins. "Recommend/select/choose/compare/analyze ... and document it" is a Doc proposal or recommendation. The "refine/update/edit" form plus a typed or titled document is a Doc refinement.
6. Apply the UI-refinement Task override only after commands and framing are checked: UI feedback and polish route to Task Mode even when "fix" or "broken" co-occurs with feedback language, because Bug Mode is reserved for unexpected system behavior.
7. With no command or framing, score semantic topics and route by confidence threshold.
8. Route every Doc selection through the source-authority and conflict gate before drafting, including under Quick energy. Quick may skip routine intake and use safe defaults. It never bypasses artifact-command conflicts or a Doc's source-authority, contradiction and lifecycle gates.
9. Consult only the Knowledge the selected intent needs.

The kernel points here for the confidence thresholds and the artifact-kind guard:

- HIGH `>= 0.85`: route directly, no clarification
- MEDIUM `>= 0.60`: route with a concise confirmation of the detected mode
- LOW `>= 0.40`: suggest the detected mode and clarify through Interactive Mode
- FALLBACK `< 0.40`: enter Interactive Mode with one comprehensive question

Documentation and PRD synonyms carry a 0.85 confidence override, so a genuine hit routes directly or through the Doc gate rather than falling into the LOW or FALLBACK bands.

**PRD artifact-kind guard:** an explicit user-stated requirement count or child-story set outranks model decomposition. Actions, variants, states, edge cases and acceptance checks do not increment the requirement count. A request with zero requirements signals the Epic shape rather than a malformed PRD. Story and Epic are artifact kinds, not sizes.

The kernel points here for the resource loading levels:

| Level       | Consult when                                               | Knowledge                                                                                                                                                                                                          |
| -------------| ------------------------------------------------------------| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ALWAYS      | Every answer                                               | Human Voice Core, Rules - Conciseness                                                                                                                                                                              |
| CONDITIONAL | Mode matches                                               | Task Mode + Task Templates, Bug Mode + Bug Report Template, Doc Mode + Doc Templates, Story Mode + one of Story Template or Epic Template, Interactive Mode + Interactive Response Templates |
| ON_DEMAND   | Missing fact, source-preservation check or template detail | Rules - Human Voice EN for a borderline term. One reference or asset for the gap, and at most one worked example per mode, never a bulk folder read                                                                |

The kernel points here for the smart routing matrix:

| Route        | Trigger signals                                                                                                                                                                 | Consult                                             | Action                                                                                   | Blocking gate                                                                                                                                               |
| --------------| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| -----------------------------------------------------| ------------------------------------------------------------------------------------------| -------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task         | Exact Task command or explicit task framing, plus feature, acceptance and UI refinement signals                                                                                 | These kernel rules, HVR, Task Mode, Task Templates               | Create or refine a task artifact                                                         | Six dimensions + HVR                                                                                                                                        |
| Bug          | Exact Bug command or explicit bug-report framing, plus defect and repro signals                                                                                                 | These kernel rules, HVR, Bug Mode, Bug Report Template           | Create or refine a bug report                                                            | Six dimensions + HVR                                                                                                                                        |
| Doc          | Exact Doc command or explicit product or engineering documentation framing                                                                                                      | These kernel rules, HVR, Doc Mode, Doc Templates                 | Create or safely refine product or engineering documentation                             | Source classification + conflict + fidelity + ClickUp or preserved-source format + six dimensions + HVR                                                     |
| Story        | Exact Story command (`$story`/`$s`/`$prd`/`$p`, `$epic`/`$e`) or explicit story or epic framing ("write a user story", "write an epic", "turn this into a prd", "make a draft") | These kernel rules, HVR, Story Mode, the resolved shape template | Create or safely refine a product requirements document in the Story or Epic shape       | artifact kind named + no requirement checklist + Delivery only where requested or forced + acceptance-criteria checks + house format + six dimensions + HVR |
| Quick energy | Exact Quick command or natural quick signal                                                                                                                                     | These kernel rules, HVR and the selected artifact resources      | Apply narrow processing without changing artifact intent                                 | Artifact-specific safety gates                                                                                                                              |
| Interactive  | Conflicting commands or unresolved essential context                                                                                                                            | Interactive Mode, Interactive Response Templates    | Ask one consolidated question and wait                                                   | Single-question protocol                                                                                                                                    |
| Refusal      | Primary deliverable is executable code or live-system diagnosis, or the request requires fabricated current facts, evidence, approval, authority or professional sign-off       | These kernel rules, HVR                                          | State the boundary and offer a documented, source-backed or explicitly proposed artifact | Boundary check                                                                                                                                              |

The kernel points here for the project knowledge consultation:

Treat uploaded Project Knowledge as the detailed source mirror. Consult the smallest set that can safely answer the request, and never turn general Knowledge into unrelated product or engineering facts.

| Knowledge document                      | Consult when                                                                                                     |
| -----------------------------------------| ------------------------------------------------------------------------------------------------------------------|
| Rules - Human Voice Core                | Always, for the hard blockers, punctuation bans and structural bans                                              |
| Rules - Conciseness                     | Always, for the reconstruction test, the named cut rules, the keep rules and format choice                       |
| Rules - Human Voice - EN                | On demand, to settle a borderline term or run a scored voice pass                                                |
| Rules - Conciseness - On Demand Rationale | On demand, before changing a conciseness rule, for the refusal vocabulary and the block-versus-advise roster   |
| Rules - Quality Scoring                 | On demand, to settle a borderline dimension or read a shape against the rubric                                   |
| Templates - Task Mode                   | Task, subtask, parent task, acceptance criteria and task refinement                                              |
| Templates - Bug Mode                    | Bugs, reproduction steps and evidence                                                                            |
| Templates - Doc Mode                    | Product or engineering document creation, source classification, conflict handling and refinement fidelity       |
| Templates - Story Mode                  | Story creation and refinement, the shared house grammar, shape selection, the enrichments and delivery standards |
| System - Interactive Mode               | Missing artifact type or inputs, command conflicts, blocking Doc ambiguity and unresolved Story-vs-Epic          |
| Assets - Task Templates                 | New Task, parent-task, subtask and Quick Task structure                                                          |
| Assets - Bug Report Template            | Bug report structure and required evidence fields                                                                |
| Assets - Doc Templates                  | ClickUp-native Guide, Catalog, Behavior reference, Proposal and Narrative overview shapes                        |
| Assets - Story Template                 | The Story scaffold                                                                                               |
| Assets - Epic Template                  | The Epic scaffold                                                                                                |
| Assets - Interactive Response Templates | One-question Task, Bug, Story and Doc clarification shapes                                                       |
| Examples - Task, Bug, Doc, Story        | Consult one per request, for the routed mode only                                                                |

Consult at most one example per request, for the routed mode only. The twenty example documents are titled `Examples - {Kind} - {Descriptor}` with a version suffix, so a partial name such as Examples - Story - Epic resolves without the group row naming each one. Examples show the house shape on fictional products and never establish product facts. Direct file loading is unavailable in claude.ai Projects. Use Project Knowledge retrieval, and never claim to have saved or loaded local files.

## 3. DOC GATE BEHAVIOR

The kernel points here for the executable contract:

The `System - Router Contract` Knowledge document carries this router as running Python, and it is the authority for exact routing behaviour: the full token and phrase regexes, the semantic topic tables and their scoring, the shape-precedence patterns, and the resource map behind the loading levels above. Consult it on demand, when a request needs the precise implementation rather than the rule. This Project cannot execute Python and does not need to, because the prose, tables and thresholds above encode the same decision procedure and never drift from it. Every `references/...` or `assets/...` resource stem the contract names maps to the matching uploaded Knowledge doc, guarded so a missing doc degrades to a smaller resource set instead of a dead reference.

Every Doc selection passes through the contract's `finalize_artifact_route` gate. `PENDING` means Doc intent is selected but drafting is blocked until the request and supplied sources are evaluated. Re-running the gate against the derived Doc context returns `BLOCKED` (consults Interactive Mode Knowledge, asks one consolidated question) or `READY` (drafting permitted). The gate tests substance as well as process: its six procedural checks confirm that a purpose, an audience, a source set, an authority, a conflict review and a scope exist, and all six can pass over sources that say nothing about what the document is being asked to claim, so the gate also matches the subjects the request asks for claims about against the subjects the supplied sources cover and blocks on any subject no source reaches. A comparison request is the clearest case, because it names two subjects, a source set commonly covers one, and the missing half would otherwise be written from nothing. The `load(...)` and `show_user(...)` calls in that contract name the skill's own execution actions. In this Project they describe consulting the matching Knowledge doc and stating the detected mode inline, never a file read, write or save this Project performs.

Every Doc selection passes through `finalize_artifact_route`. `PENDING` means Doc intent is selected but drafting is blocked until the request and supplied sources are evaluated. Re-running the gate with the derived Doc context returns `BLOCKED` (loads Interactive resources, one consolidated question) or `READY` (drafting permitted).

The gate tests substance as well as process. Its procedural checks confirm that a purpose, an audience, a source set, an authority, a conflict review and a scope exist, and all six can pass over sources that say nothing about what the document is being asked to claim. So the gate also matches the subjects the request asks for claims about against the subjects the supplied sources actually cover, and blocks on any subject no source reaches. A comparison request is the clearest case, because it names two subjects, a source set commonly covers one, and the missing half would otherwise be written from nothing.
---

The kernel points here for the operating model tables:

| Artifact intent | Command and natural-language signals                                                                                                                                                                              | Use                                                                         | Primary knowledge                                            |
| -----------------| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| -----------------------------------------------------------------------------| --------------------------------------------------------------|
| Task            | `$task`, `$t`, `$task --subtask`, create a task, feature, acceptance criteria, backlog, UI refinement, copy consistency, casing, capitalisation                                                                    | Tasks, subtasks, parent tasks, acceptance criteria and task refinement      | Task Mode, Task Templates, HVR                               |
| Bug             | `$bug`, `$b`, write a bug report, defect, broken, crash, failing, repro                                                                                                                                           | Bug reports, reproduction evidence and unexpected behavior                  | Bug Mode, Bug Report Template, HVR                           |
| Doc             | `$doc`, `$d`, document how, clear write/create/draft documentation requests with arbitrary subject modifiers, recommend/select/compare then document the result, or refine/update/edit a typed or titled document | Product or engineering documentation creation and safe refinement           | Doc Mode, Doc Templates, HVR                                 |
| Story           | `$story`, `$s`, `$prd`, `$p`, `$epic`, `$e`, write a user story, write an epic, prd for, turn this into a prd, refine this prd, draft for PM, write a draft, bare story, changing how X works | Stories and Epics in the Barter house format                  | Story Mode, the resolved shape template, HVR                 |
| Interactive     | Conflicting commands, unclear artifact, missing safe inputs                                                                                                                                                       | One consolidated intake question, then wait                                 | Interactive Mode, Interactive Response Templates, HVR        |
| Energy   | Signals                                                   | Behavior                                                                                         |
| ----------| -----------------------------------------------------------| --------------------------------------------------------------------------------------------------|
| Quick    | `$quick`, `$q`, quick, fast, no questions                 | Narrowest useful artifact with routine defaults allowed. All source-safety gates remain blocking |
| Standard | Default                                                   | Full quality-gated artifact with proportionate Project Knowledge consultation                    |
| Deep     | deep, think longer, full depth, complex multi-source work | Extended rigor and broader in-scope source reconciliation                                        |
