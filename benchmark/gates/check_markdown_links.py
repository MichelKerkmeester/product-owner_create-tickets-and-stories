#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: MARKDOWN LINK INTEGRITY GATE
# ───────────────────────────────────────────────────────────────

"""Check source Markdown links whose destinations stay inside this repository.

Usage:
  check_markdown_links.py -> exit 0 when every relative link resolves, exit 1 otherwise
"""

from __future__ import annotations

from collections.abc import Iterator
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

# ───────────────────────────────────────────────────────────────
# 1. CONFIGURATION
# ───────────────────────────────────────────────────────────────

ROOT = Path(__file__).resolve().parents[2]
EXCLUDED_DIRS = {".git", "node_modules", "specs", "export", "mcp-click-up", "mcp-figma", "mcp-code-mode"}
REFERENCE_LINK = re.compile(r"(?m)^\s{0,3}\[[^\]]+\]:\s*(?:<([^>]+)>|(\S+))")
INLINE_CODE = re.compile(r"(`+)[^`\n]*?\1")
# Worked examples write link targets as placeholders such as figma-url, which the reader
# replaces with a real address, so they are not repository paths.
PLACEHOLDER = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*-url")


# ───────────────────────────────────────────────────────────────
# 2. HELPERS
# ───────────────────────────────────────────────────────────────

def markdown_files(root: Path) -> list[Path]:
    """Return Markdown files outside the excluded source trees."""
    files = []
    for current, directories, names in os.walk(root, followlinks=False):
        folder = Path(current)
        relative = folder.relative_to(root)
        directories[:] = [
            name for name in directories
            if name not in EXCLUDED_DIRS and not (folder / name).is_symlink()
            and not (relative == Path("benchmark") and name == "reports")
        ]
        files.extend(
            folder / name for name in names
            if name.lower().endswith(".md") and not (folder / name).is_symlink()
        )
    return sorted(files)


def without_code(text: str) -> str:
    """Remove fenced and inline code so examples are not treated as live links."""
    output = []
    fence_char = None
    fence_size = 0
    for line in text.splitlines(keepends=True):
        match = re.match(r"^[ \t]{0,3}(`{3,}|~{3,})", line)
        if fence_char is None and match:
            fence_char = match.group(1)[0]
            fence_size = len(match.group(1))
            output.append("\n" if line.endswith("\n") else "")
        elif fence_char is not None:
            if match and match.group(1)[0] == fence_char and len(match.group(1)) >= fence_size:
                fence_char = None
                fence_size = 0
            output.append("\n" if line.endswith("\n") else "")
        else:
            output.append(line)
    return INLINE_CODE.sub("", "".join(output))


def inline_destinations(text: str) -> Iterator[tuple[str, int]]:
    """Yield inline link destinations and their character offsets."""
    cursor = 0
    while True:
        close = text.find("](", cursor)
        if close < 0:
            return
        opener = text.rfind("[", 0, close)
        if opener < 0 or "\n" in text[opener:close] or (close and text[close - 1] == "\\"):
            cursor = close + 2
            continue
        position = close + 2
        while position < len(text) and text[position].isspace():
            position += 1
        if position < len(text) and text[position] == "<":
            end = text.find(">", position + 1)
            if end < 0:
                cursor = close + 2
                continue
            yield text[position + 1:end], position
            cursor = end + 1
            continue
        destination = []
        depth = 0
        start = position
        while position < len(text):
            char = text[position]
            if char == "\\" and position + 1 < len(text):
                destination.append(text[position + 1])
                position += 2
                continue
            if char == "(":
                depth += 1
            elif char == ")":
                if depth == 0:
                    break
                depth -= 1
            elif char.isspace() and depth == 0:
                break
            destination.append(char)
            position += 1
        if position > start:
            yield "".join(destination), start
        cursor = max(position + 1, close + 2)


def destinations(text: str) -> Iterator[tuple[str, int]]:
    """Yield Markdown destinations and offsets from inline and reference links."""
    source = without_code(text)
    for match in REFERENCE_LINK.finditer(source):
        yield match.group(1) or match.group(2), match.start()
    yield from inline_destinations(source)


def repository_target(destination: str, source: Path, root: Path) -> Path | None:
    """Resolve relative in-repository destinations without opening their targets."""
    parsed = urlsplit(destination)
    if parsed.scheme or parsed.netloc or destination.startswith("/") or not parsed.path:
        return None
    if PLACEHOLDER.fullmatch(destination):
        return None
    target = (source.parent / unquote(parsed.path)).resolve()
    try:
        target.relative_to(root.resolve())
    except ValueError:
        return None
    return target


# ───────────────────────────────────────────────────────────────
# 3. CORE LOGIC
# ───────────────────────────────────────────────────────────────

def check_links(root: Path) -> int:
    """Resolve every in-repository link under root, print the findings and return the exit code."""
    files = markdown_files(root)
    failures = []
    checked = 0
    for source in files:
        text = source.read_text(encoding="utf-8")
        for destination, offset in destinations(text):
            target = repository_target(destination, source, root)
            if target is None:
                continue
            checked += 1
            if not target.exists():
                line = text.count("\n", 0, offset) + 1
                failures.append(f"{source.relative_to(root)}:{line}: unresolved link {destination!r}")
    if failures:
        for failure in failures:
            print(failure)
        print(f"FAILED {len(failures)} unresolved relative Markdown link(s)")
        return 1
    print(f"PASSED {checked} relative Markdown links across {len(files)} in-scope Markdown files")
    return 0


# ───────────────────────────────────────────────────────────────
# 4. ENTRY POINT
# ───────────────────────────────────────────────────────────────

def main() -> int:
    """Check the links of this repository."""
    return check_links(ROOT)


if __name__ == "__main__":
    sys.exit(main())
