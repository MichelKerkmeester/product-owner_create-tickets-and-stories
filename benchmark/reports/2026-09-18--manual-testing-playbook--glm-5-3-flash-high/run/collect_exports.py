#!/usr/bin/env python3
"""Rebuild export/benchmark from a playbook run, holding real artifact exports only.

The run folder keeps everything a run produces: plans, grading, transcripts,
event streams and a copy of every file each scenario wrote. export/benchmark is
the place a reader opens to see the deliverables themselves, so it gets those
and nothing else:

- skill/ holds every file a skill scenario created, as written, named
  "<scenario id> - <file name>".
- claude project/ holds every deliverable a Project scenario returned. A Project
  cannot write files, so its deliverable is the block in the reply that precedes
  or directly follows the export path the reply reports, saved under that
  reported name.
- Re-measure rounds land in <side>/<round>/<run>/ with the same naming.

Usage: collect_exports.py <run folder> <export/benchmark folder> [--dry-run]
Prints one review line per Project extraction, since a reply is prose and the
block boundaries are inferred.
"""
import os
import re
import shutil
import sys
from typing import List, Optional, Tuple

# The export lane, plus the curated folder a brand voice snippet is saved to,
# which is the one file a Deal Templates run writes outside export/.
PATH_RE = re.compile(r"(?:export|assets/tone-of-voice)/[^\n`|)*\"']*?\.md")
# A bracketed slot is a template placeholder, except the sequence number a Project
# cannot know, which a batch writes as [NNN], [NNN+1] and so on.
NUMBER_SLOT_RE = re.compile(r"\[(NNN(?:\+\d+)?|###)\]")
PLACEHOLDER_RE = re.compile(r"\[(?!NNN(?:\+\d+)?\]|###\])[^\]]+\]")
FENCE_RE = re.compile(r"^(`{3,}|~{3,})([^\n]*)$")
BLOCK_HEADING_RE = re.compile(r"^(#{1,4}\s*|\*\*)Deliverable Block\b", re.I)
PROSE_FENCE_LANGS = {"", "markdown", "md", "text"}
MIN_BODY_CHARS = 200
# Chat lines a model sometimes writes between an unfenced block and the path it
# reports. Everything from the first one on is the reply, not the deliverable.
TRAILER_RE = re.compile(r"^(HVR self-scan|HVR:|MEQT \d|DEAL \d+/25|\*\*Instruction set|"
                        r"\*\*How finished|Summary:|Single-paragraph summary)")


def scenario_id(folder: str) -> str:
    return os.path.basename(folder.rstrip("/")).split(" ")[0]


def turn_files(folder: str) -> List[Tuple[int, str]]:
    found = []
    for name in os.listdir(folder):
        match = re.fullmatch(r"turn-(\d+)\.md", name)
        if match:
            found.append((int(match.group(1)), os.path.join(folder, name)))
    return sorted(found)


def fences(lines: List[str]) -> List[Tuple[int, int, str]]:
    """(opening line, closing line, language) for every closed fence."""
    spans, open_at, marker, lang = [], None, "", ""
    for index, line in enumerate(lines):
        match = FENCE_RE.match(line.strip())
        if not match:
            continue
        if open_at is None:
            open_at, marker, lang = index, match.group(1), match.group(2).strip().lower()
        elif line.strip().startswith(marker) and not match.group(2).strip():
            spans.append((open_at, index, lang))
            open_at = None
    return spans


def inside(index: int, spans: List[Tuple[int, int, str]]) -> Optional[Tuple[int, int, str]]:
    for span in spans:
        if span[0] <= index <= span[1]:
            return span
    return None


def trim(block: List[str], leading_rule: bool = False) -> List[str]:
    """Drop blank edges and a closing rule. A leading rule goes only when asked,
    because a snippet's frontmatter opens with one."""
    while block and (not block[-1].strip() or block[-1].strip() in ("---", "***")):
        block.pop()
    while block and (not block[0].strip() or (leading_rule and block[0].strip() in ("---", "***"))):
        block.pop(0)
    return block


def extract(text: str) -> List[Tuple[str, str, str]]:
    """(reported name, body, how the start was found) for each reported export."""
    lines = text.split("\n")
    spans = fences(lines)
    found, floor, seen = [], 0, set()
    for index, line in enumerate(lines):
        for path in PATH_RE.findall(line):
            if PLACEHOLDER_RE.search(path) or path in seen:
                continue
            span = inside(index, spans)
            if span and span[2] not in PROSE_FENCE_LANGS:
                continue
            name = NUMBER_SLOT_RE.sub(lambda m: m.group(1).replace("###", "NNN"), os.path.basename(path))
            body, how, end = None, "", index
            prose = [s for s in spans if floor <= s[0] and s[1] < index and s[2] in PROSE_FENCE_LANGS]
            header = [i for i in range(floor, index)
                      if lines[i].startswith("<!--") and not inside(i, spans)]
            labelled = [i for i in range(floor, index) if BLOCK_HEADING_RE.match(lines[i].strip())]
            titled = [i for i in range(floor, index)
                      if re.match(r"#{1,2} ", lines[i]) and not inside(i, spans)]
            if prose and len("\n".join(lines[prose[-1][0] + 1:prose[-1][1]])) >= MIN_BODY_CHARS:
                body, how = lines[prose[-1][0] + 1:prose[-1][1]], "fence"
            elif header:
                body, how = lines[header[0]:index], "mode header"
            elif labelled:
                body, how = lines[labelled[-1] + 1:index], "deliverable heading"
            elif titled:
                body, how = lines[titled[0]:index], "title"
            else:
                # A reply that announces the path first puts the block right after it.
                after = [s for s in spans if index < s[0] <= index + 3 and s[2] in PROSE_FENCE_LANGS]
                if after:
                    body, how, end = lines[after[0][0] + 1:after[0][1]], "fence after path", after[0][1]
            if body is not None and how in ("mode header", "deliverable heading", "title"):
                cut = next((i for i, text in enumerate(body) if TRAILER_RE.match(text.strip())), None)
                body = body[:cut] if cut is not None else body
            if body is not None:
                body = trim(list(body), leading_rule=how == "deliverable heading")
                # A header comment already marks the block as a deliverable, so a
                # one-line tagline under it counts. Anything else needs some size.
                content = [text for text in body if text.strip() and not text.startswith("<!--")]
                if content and (how == "mode header" or len("\n".join(body)) >= MIN_BODY_CHARS):
                    found.append((name, "\n".join(body) + "\n", how))
                    seen.add(path)
                    floor = end + 1
    return found


def collect(run: str, out: str, dry: bool) -> None:
    rounds = [("", run)]
    for name in sorted(os.listdir(run)):
        if name.startswith("remeasure") and os.path.isdir(os.path.join(run, name)):
            for sub in sorted(os.listdir(os.path.join(run, name))):
                if sub.startswith("run-"):
                    rounds.append((os.path.join(name, sub), os.path.join(run, name, sub)))
    for label, base in rounds:
        skill = os.path.join(base, "skill")
        if os.path.isdir(skill):
            for folder in sorted(os.listdir(skill)):
                exports = os.path.join(skill, folder, "exports")
                for root, _, files in os.walk(exports):
                    for file in sorted(files):
                        target = os.path.join(out, "skill", label, f"{scenario_id(folder)} - {file}")
                        print(f"skill   {os.path.join(label, os.path.basename(target))}")
                        if not dry:
                            os.makedirs(os.path.dirname(target), exist_ok=True)
                            shutil.copy2(os.path.join(root, file), target)
        project = os.path.join(base, "claude project")
        if os.path.isdir(project):
            for folder in sorted(os.listdir(project)):
                path = os.path.join(project, folder)
                if not os.path.isdir(path):
                    continue
                written = set()
                for turn, file in turn_files(path):
                    for name, body, how in extract(open(file, encoding="utf-8").read()):
                        stem = f"{scenario_id(folder)} - {name}"
                        if stem in written:
                            stem = stem[:-3] + f" (turn {turn}).md"
                        written.add(stem)
                        target = os.path.join(out, "claude project", label, stem)
                        first = body.split("\n", 1)[0][:60]
                        print(f"project {os.path.join(label, stem)} | turn {turn} | {how} | "
                              f"{len(body)} chars | {first}")
                        if not dry:
                            os.makedirs(os.path.dirname(target), exist_ok=True)
                            with open(target, "w", encoding="utf-8") as handle:
                                handle.write(body)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    collect(sys.argv[1], sys.argv[2], "--dry-run" in sys.argv[3:])
