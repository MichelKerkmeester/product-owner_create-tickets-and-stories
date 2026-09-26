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
- A deliverable saved inside a folder under export/, such as a Story with its
  tasks, keeps that folder on both sides: "<scenario id> - <folder>/<file name>".
  On the skill side the folder is the one the runtime wrote, and on the Project
  side it is the folder part of the path the reply reports. Flattening it would
  lose which tasks belong to which Story.
- context/ holds the attachments the runner staged. They are inputs, never
  deliverables, so they are not collected, and one the runtime changed prints a
  warning line, since an attachment is never meant to be modified.
- Re-measure rounds are collected only with --rounds, into
  <side>/<round>/<run>/ with the same naming, since a round's evidence already
  lives in its own replies/ and results.csv.
- A target that already exists and differs from what the run holds was edited
  after collection, so it is skipped with a warning rather than overwritten.
  --force overwrites it.

Usage: collect_exports.py <run folder> <export/benchmark folder> [--dry-run] [--rounds] [--force]
Prints one review line per Project extraction, since a reply is prose and the
block boundaries are inferred.
"""
import os
import re
import shutil
import sys
from typing import List, Optional, Tuple

# The export lane, plus the curated folder a brand voice snippet is saved to,
# which is the one file a Deal Templates run writes outside export/. Prompt
# Improver also exports JSON and YAML when the user locks the format.
PATH_RE = re.compile(r"(?:export|assets/tone-of-voice)/[^\n`|)*\"']*?\.(?:md|json|ya?ml)\b")
# A bracketed slot is a template placeholder, except the sequence number a Project
# cannot know, which a batch writes as [NNN], [NNN+1] and so on.
NUMBER_SLOT_RE = re.compile(r"\[(NNN(?:\+\d+)?|###)\]")
PLACEHOLDER_RE = re.compile(r"\[(?!NNN(?:\+\d+)?\]|###\])[^\]]+\]")
FENCE_RE = re.compile(r"^(`{3,}|~{3,})([^\n]*)$")
BLOCK_HEADING_RE = re.compile(r"^(#{1,4}\s*|\*\*)Deliverable Block\b", re.I)
PROSE_FENCE_LANGS = {"", "markdown", "md", "text", "json", "yaml", "yml"}
# Prompt Improver opens its block with a template line rather than a comment.
MODE_LINE_RE = re.compile(r"^\**Mode: \$\w+ \| Complexity:")
MIN_BODY_CHARS = 200
# Chat lines a model sometimes writes between an unfenced block and the path it
# reports. Everything from the first one on is the reply, not the deliverable.
TRAILER_RE = re.compile(r"^(HVR self-scan|HVR:|MEQT \d|DEAL \d+/25|\*\*Instruction set|"
                        r"\*\*How finished|Summary:|Single-paragraph summary|\*\*Chat report)")
# The folder the runner stages a scenario's attachments into.
CONTEXT_DIR = "context"
EXPORT_DIR = "export"


def scenario_id(folder: str) -> str:
    return os.path.basename(folder.rstrip("/")).split(" ")[0]


def number_slot(text: str) -> str:
    return NUMBER_SLOT_RE.sub(lambda m: m.group(1).replace("###", "NNN"), text)


def export_parts(path: str, slots: bool = True) -> Tuple[str, str]:
    """(folder, file name) for a path relative to the sandbox or reported in a reply.

    The folder is whatever sits between export/ and the file, empty for a single
    file and for anything saved outside export/. With slots, every part takes the
    number slot rule, so a Project bundle named with the number it cannot know lands
    under the same folder name as the files the reply puts inside it. A skill
    runtime writes real files, so its names are kept exactly as written, and a
    literal slot in one stays visible as the defect it is."""
    parts = path.replace(os.sep, "/").split("/")
    folder = parts[1:-1] if parts[0] == EXPORT_DIR else []
    keep = number_slot if slots else (lambda text: text)
    return "/".join(keep(p) for p in folder), keep(parts[-1])


def target_name(sid: str, folder: str, name: str) -> str:
    return f"{sid} - {folder}/{name}" if folder else f"{sid} - {name}"


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


def extract(text: str) -> List[Tuple[str, str, str, str]]:
    """(reported folder, reported name, body, how the start was found) for each
    reported export. The folder is empty unless the path names one under export/."""
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
            folder, name = export_parts(path)
            body, how, end = None, "", index
            prose = [s for s in spans if floor <= s[0] and s[1] < index and s[2] in PROSE_FENCE_LANGS]
            header = [i for i in range(floor, index)
                      if (lines[i].startswith("<!--") or MODE_LINE_RE.match(lines[i]))
                      and not inside(i, spans)]
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
                    found.append((folder, name, "\n".join(body) + "\n", how))
                    seen.add(path)
                    floor = end + 1
    return found


def edited(target: str, data: bytes) -> bool:
    """True when the target exists and holds something other than data."""
    if not os.path.isfile(target):
        return False
    with open(target, "rb") as handle:
        return handle.read() != data


def collect(run: str, out: str, dry: bool, with_rounds: bool = False, force: bool = False) -> None:
    rounds = [("", run)]
    for name in sorted(os.listdir(run)) if with_rounds else []:
        if name.startswith("remeasure") and os.path.isdir(os.path.join(run, name)):
            for sub in sorted(os.listdir(os.path.join(run, name))):
                if sub.startswith("run-"):
                    rounds.append((os.path.join(name, sub), os.path.join(run, name, sub)))
    for label, base in rounds:
        skill = os.path.join(base, "skill")
        if os.path.isdir(skill):
            for folder in sorted(os.listdir(skill)):
                exports = os.path.join(skill, folder, "exports")
                for root, dirs, files in os.walk(exports):
                    dirs.sort()
                    for file in sorted(files):
                        rel = os.path.relpath(os.path.join(root, file), exports)
                        if rel.split(os.sep)[0] == CONTEXT_DIR:
                            print(f"warning skill {scenario_id(folder)} changed {rel} during the run. "
                                  f"An attachment is never modified, so it is not collected")
                            continue
                        stem = target_name(scenario_id(folder), *export_parts(rel, slots=False))
                        target = os.path.join(out, "skill", label, stem)
                        with open(os.path.join(root, file), "rb") as handle:
                            data = handle.read()
                        if not force and edited(target, data):
                            print(f"warning skill {os.path.join(label, stem)} differs from the run's copy, "
                                  f"so it was edited after collection and is kept. --force overwrites it")
                            continue
                        print(f"skill   {os.path.join(label, stem)}")
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
                    for bundle, name, body, how in extract(open(file, encoding="utf-8").read()):
                        stem = target_name(scenario_id(folder), bundle, name)
                        if stem in written:
                            root, ext = os.path.splitext(stem)
                            stem = f"{root} (turn {turn}){ext}"
                        written.add(stem)
                        target = os.path.join(out, "claude project", label, stem)
                        if not force and edited(target, body.encode("utf-8")):
                            print(f"warning project {os.path.join(label, stem)} differs from the run's copy, "
                                  f"so it was edited after collection and is kept. --force overwrites it")
                            continue
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
    flags = sys.argv[3:]
    collect(sys.argv[1], sys.argv[2], "--dry-run" in flags, "--rounds" in flags, "--force" in flags)
