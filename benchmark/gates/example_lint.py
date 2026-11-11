#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: EXAMPLE LINT GATE
# ───────────────────────────────────────────────────────────────

"""Hold the worked examples and the worked replies to the rules they model.

Models copy a worked example more closely than they follow a rule, so an
example that breaks a rule teaches the break. Six of the seven Doc examples
once carried em dashes and semicolons the output-format gate blocks, and no
check read them, because the format gate's own perimeter is the skill
instruction surface plus whatever deliverable it is handed.

This gate hands it the examples. Every worked example under
`sk-product-owner/assets/examples/` runs through the system's own validator in
artifact mode, exactly as a delivered artifact would. Every Project mirror of
an example runs the same way once its mirror preamble is set aside: the title,
the one-paragraph description and the `---` under it belong to the mirror, not
to the artifact it shows, and a `---` divider is itself a finding in a
house-grammar deliverable.

The fenced scaffold blocks in the template assets are linted too. A model
copies the scaffold it is handed, and three Doc scaffolds once taught a prose
em dash the gate blocks, because the source lint skips fenced blocks and the
examples are a different set of files. Each block that carries markdown runs
through the same validator in artifact mode, and only the two punctuation
findings the voice card bans in a deliverable are kept: a prose em dash outside
the card's sanctioned shapes and a semicolon. Placeholder text such as `{Title}`
trips other artifact checks that mean nothing in a scaffold, so those findings
are dropped. The validator keeps the judgement of what a sanctioned dash is,
which this gate then never restates. A block fenced as `text` or as code holds a
path or a literal, and the worked replies below are read by their own check.

The worked replies in the Delivery Reply Shape section of the response
templates asset, and in its Project mirror, are read line by line against that
shape: the path line first, the read-back line on the skill only, the
self-scan line, the quality line, the Open items block with its numbered topic
and its two bold bullets and no blank line inside it, and one closing line
last. Only the reply lines are read, so a change to the wording of a summary
never trips it.

No file found is a failure, because a lint that read nothing would print a
pass it did not earn.

Usage:
  example_lint.py             -> exit 0 when every example, scaffold block and worked reply passes
  example_lint.py --self-test -> prove the gate fails on a broken example, scaffold block and reply
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# ───────────────────────────────────────────────────────────────
# 1. CONFIGURATION
# ───────────────────────────────────────────────────────────────

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("PO_ROOT") or HERE.parent.parent)

VALIDATOR = Path("benchmark/format/validate-output-format.cjs")
EXAMPLES = Path("sk-product-owner/assets/examples")
# The FigJam worked examples are mirrored into the Project as well, so both sides are read.
FIGJAM_EXAMPLES = Path("sk-create-figjam/assets/examples")
KNOWLEDGE = Path("claude project/knowledge")
MIRROR_GLOB = "Product Owner - Examples - *.md"
REPLY_SOURCE = Path("sk-product-owner/assets/interactive-response-templates.md")
REPLY_MIRROR = KNOWLEDGE / "Product Owner - Assets - Interactive Response Templates.md"

# The scaffolds an agent copies from. Each has a Project mirror named
# `Product Owner - Assets - <Title Case Name>.md`, and the mirror carries the same blocks.
ASSETS = Path("sk-product-owner/assets")
SCAFFOLD_GLOBS = ("*-template.md", "*-templates.md")
# Only a block fenced as markdown, or with no language, holds prose to read.
SCAFFOLD_LANGUAGES = {"", "markdown", "md"}
# The validator messages kept from a scaffold block. Every other finding belongs to a
# finished artifact and fires on placeholder text.
SCAFFOLD_RULES = ("prose em dash", "prose semicolon")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")

REPLY_SECTION = "## 3. DELIVERY REPLY SHAPE"
WORKED_HEADING = "### Worked Replies"
MIN_REPLIES = 3

PATH_LINE = re.compile(r"^Path: `export/[^`/][^`]*\.md`$")
PROJECT_PATH_LINE = re.compile(r"^Export-equivalent path: `export/[^`]+\.md`$")
VERIFIED_LINE = re.compile(r"^Verified: read-back succeeded; \d+ lines$")
SELF_SCAN_LINE = re.compile(r"^HVR self-scan: \d+ hard blockers\. Fixed: .+\. Kept with reason: .+\.$")
QUALITY_LINE = re.compile(r"^Quality: [^|]+ \| Kind: [^|]+ \| Energy: (?:Quick|Standard|Deep)$")
OPEN_HEADING = "### Open items"
ITEM_TOPIC = re.compile(r"^\d+\. \*\*[^*]+\*\*$")
ITEM_SITUATION = re.compile(r"^ {3}- \*\*Situation:\*\* [A-Z0-9`]")
ITEM_OPEN = re.compile(r"^ {3}- \*\*Open:\*\* [A-Z0-9`]")
CLOSING_LINES = (
    re.compile(r"^Want me to change anything\?$"),
    re.compile(r"^Want me to push this to .+, or upload it as a private ClickUp doc instead\?$"),
    re.compile(
        r"^Where in ClickUp should this go\? Send a list link, or I'll upload it as a private doc, "
        r"which I recommend for now\.$"
    ),
    re.compile(r"^Answer in one message and I'll draft the [A-Za-z ]+\.$"),
)
FINDING_LINE = re.compile(r"^(?P<path>.+?):(?P<line>\d+): (?P<message>.+)$")


# ───────────────────────────────────────────────────────────────
# 2. HELPERS
# ───────────────────────────────────────────────────────────────

def run_validator(paths: list[Path]) -> tuple[int, list[str]]:
    """Run the system validator on files in artifact mode, return exit status and blocking lines."""
    result = subprocess.run(
        ["node", str(ROOT / VALIDATOR), *(str(path) for path in paths)],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    output = (result.stdout + result.stderr).splitlines()
    blocking = [line for line in output if line and not line.startswith(" ") and FINDING_LINE.match(line)]
    return result.returncode, blocking


def validate(path: Path) -> tuple[int, list[str]]:
    """Run the system validator on one file in artifact mode, return exit status and blocking lines."""
    return run_validator([path])


def strip_mirror_preamble(text: str) -> tuple[str, int]:
    """Drop the mirror's title, description and the `---` under them, return the body and its line offset."""
    lines = text.split("\n")
    for index, line in enumerate(lines):
        if index > 0 and line.strip() == "---":
            return "\n".join(lines[index + 1:]), index + 1
    return text, 0


# ───────────────────────────────────────────────────────────────
# 3. CORE LOGIC
# ───────────────────────────────────────────────────────────────

def example_findings() -> tuple[list[str], int]:
    """Lint every source example and every mirrored example, return findings and the file count."""
    findings: list[str] = []
    sources = sorted((ROOT / EXAMPLES).rglob("*.md")) + sorted((ROOT / FIGJAM_EXAMPLES).rglob("*.md"))
    mirrors = sorted((ROOT / KNOWLEDGE).glob(MIRROR_GLOB))
    for path in sources:
        status, blocking = validate(path)
        if status != 0:
            relative = path.relative_to(ROOT)
            for line in blocking or [f"{path}:0: validator exit {status}"]:
                findings.append(_relabel(line, relative, 0))
    with tempfile.TemporaryDirectory(prefix="po-example-lint-") as scratch:
        for path in mirrors:
            body, offset = strip_mirror_preamble(path.read_text(encoding="utf-8"))
            staged = Path(scratch) / path.name
            staged.write_text(body, encoding="utf-8")
            status, blocking = validate(staged)
            if status != 0:
                relative = path.relative_to(ROOT)
                for line in blocking or [f"{staged}:0: validator exit {status}"]:
                    findings.append(_relabel(line, relative, offset))
    return findings, len(sources) + len(mirrors)


def _relabel(line: str, relative: Path, offset: int) -> str:
    """Rewrite a validator finding to name the real file and the real line."""
    match = FINDING_LINE.match(line)
    if not match:
        return f"{relative}: {line}"
    return f"{relative}:{int(match.group('line')) + offset}: {match.group('message')}"


def scaffold_files() -> list[Path]:
    """Return every template asset and the Project mirror of each, the files whose fenced blocks are scaffolds.

    A mirror that does not exist is left out here, because the parity gates own
    the question of whether every declared mirror is present.
    """
    sources = sorted({path for pattern in SCAFFOLD_GLOBS for path in (ROOT / ASSETS).glob(pattern)})
    files = list(sources)
    for source in sources:
        title = source.stem.replace("-", " ").title()
        mirror = ROOT / KNOWLEDGE / f"Product Owner - Assets - {title}.md"
        if mirror.is_file():
            files.append(mirror)
    return files


def scaffold_blocks(text: str) -> list[tuple[int, str]]:
    """Return each fenced block that holds markdown as its opening fence line number and its body.

    A fence closes on a line of the same character, at least as long as the
    opener, with nothing after it. A scaffold fenced with four backticks
    therefore keeps the three-backtick code block inside it as body text.
    """
    lines = text.split("\n")
    blocks: list[tuple[int, str]] = []
    index = 0
    while index < len(lines):
        opener = FENCE.match(lines[index])
        if not opener:
            index += 1
            continue
        mark, info = opener.group(1), opener.group(2).strip()
        end = index + 1
        while end < len(lines):
            closer = FENCE.match(lines[end])
            if closer and closer.group(1)[0] == mark[0] and len(closer.group(1)) >= len(mark) and not closer.group(2).strip():
                break
            end += 1
        language = info.split()[0].lower() if info else ""
        if language in SCAFFOLD_LANGUAGES:
            blocks.append((index + 1, "\n".join(lines[index + 1:end])))
        index = end + 1
    return blocks


def scaffold_findings() -> tuple[list[str], int]:
    """Lint the prose punctuation of every scaffold block, return findings and the block count.

    Every block is staged as its own file and the validator runs once over all
    of them, so a finding maps back to the block it came from by file name.
    """
    findings: list[str] = []
    staged: dict[str, tuple[Path, int]] = {}
    with tempfile.TemporaryDirectory(prefix="po-scaffold-lint-") as scratch:
        for path in scaffold_files():
            for opened_at, body in scaffold_blocks(path.read_text(encoding="utf-8")):
                name = f"block-{len(staged):04d}.md"
                (Path(scratch) / name).write_text(body, encoding="utf-8")
                staged[name] = (path.relative_to(ROOT), opened_at)
        if not staged:
            return findings, 0
        status, blocking = run_validator([Path(scratch) / name for name in staged])
        # Anything but a pass or a finding means the validator broke, and a broken
        # validator reports nothing, which would read as a clean scaffold.
        if status not in (0, 1):
            findings.append(f"{ASSETS}: the validator exited {status} on the scaffold blocks")
        for line in blocking:
            match = FINDING_LINE.match(line)
            if not match or not any(rule in match.group("message") for rule in SCAFFOLD_RULES):
                continue
            relative, opened_at = staged[Path(match.group("path")).name]
            findings.append(f"{relative}:{int(match.group('line')) + opened_at}: scaffold block, {match.group('message')}")
    return findings, len(staged)


def worked_replies(text: str) -> list[tuple[int, list[str]]]:
    """Return each fenced worked reply in the reply-shape section with its first line number."""
    lines = text.split("\n")
    try:
        start = lines.index(REPLY_SECTION)
    except ValueError:
        return []
    try:
        worked = lines.index(WORKED_HEADING, start)
    except ValueError:
        return []
    replies, current, opened_at = [], None, 0
    for index in range(worked + 1, len(lines)):
        line = lines[index]
        if line.startswith("## ") and current is None:
            break
        if line.startswith("```"):
            if current is None:
                current, opened_at = [], index + 2
            else:
                replies.append((opened_at, current))
                current = None
            continue
        if current is not None:
            current.append(line)
    return replies


def reply_findings(label: Path, first: int, reply: list[str], project_only: bool) -> list[str]:
    """Check one worked reply against the Delivery Reply Shape."""
    found: list[str] = []

    def fail(offset: int, message: str) -> None:
        """Record one finding at a line offset inside the reply."""
        found.append(f"{label}:{first + offset}: {message}")

    if not reply:
        fail(0, "worked reply is empty")
        return found
    cursor = 0
    if PATH_LINE.match(reply[0]):
        if project_only:
            fail(0, "a Project worked reply prints a `Path:` line, which only the skill writes")
        if len(reply) < 2 or not VERIFIED_LINE.match(reply[1]):
            fail(1, "the skill path line is not followed by the `Verified: read-back succeeded; N lines` line")
        cursor = 2
    elif PROJECT_PATH_LINE.match(reply[0]):
        cursor = 1
    else:
        fail(0, "the reply does not open on the path line")
        cursor = 1
    if cursor >= len(reply) or not SELF_SCAN_LINE.match(reply[cursor]):
        fail(cursor, "the `HVR self-scan:` line does not follow the path line")
    if cursor + 1 >= len(reply) or not QUALITY_LINE.match(reply[cursor + 1]):
        fail(cursor + 1, "the quality line does not follow the self-scan line in its fixed shape")

    if OPEN_HEADING not in reply:
        fail(0, "the reply carries no `### Open items` heading")
    else:
        head = reply.index(OPEN_HEADING)
        body = []
        index = head + 1
        while index < len(reply) and reply[index].strip():
            body.append((index, reply[index]))
            index += 1
        following = next((line for line in reply[index:] if line.strip()), "")
        if ITEM_TOPIC.match(following) or ITEM_SITUATION.match(following) or ITEM_OPEN.match(following):
            fail(index, "a blank line sits inside or between open items")
        if not body:
            fail(head, "Open items is empty, where `None identified` stands alone")
        elif body[0][1] == "None identified":
            if len(body) > 1:
                fail(body[1][0], "`None identified` does not stand alone")
        else:
            expected = "topic"
            for line_index, line in body:
                if expected == "topic" and ITEM_TOPIC.match(line):
                    expected = "situation"
                elif expected == "situation" and ITEM_SITUATION.match(line):
                    expected = "open"
                elif expected == "open" and ITEM_OPEN.match(line):
                    expected = "topic"
                else:
                    fail(line_index, f"open item line out of shape, expected the {expected} line")
                    break
            else:
                if expected != "topic":
                    fail(body[-1][0], f"open item ends without its {expected} line")

    tail = [line for line in reply if line.strip()]
    if not tail or not any(pattern.match(tail[-1]) for pattern in CLOSING_LINES):
        fail(len(reply) - 1, "the reply does not end on one of the closing lines")
    for offset, line in enumerate(reply):
        if re.match(r"^\s*[-*]\s+.*\.$", line):
            fail(offset, "a bullet ends with a full stop")
        prose = line if not VERIFIED_LINE.match(line) else ""
        if "—" in prose:
            fail(offset, "an em dash in the reply")
        if ";" in prose:
            fail(offset, "a semicolon in the reply")
    return found


def reply_shape_findings() -> list[str]:
    """Read the worked replies on both packagings."""
    findings: list[str] = []
    for relative, project_only in ((REPLY_SOURCE, False), (REPLY_MIRROR, True)):
        path = ROOT / relative
        if not path.is_file():
            findings.append(f"{relative}: missing")
            continue
        replies = worked_replies(path.read_text(encoding="utf-8"))
        if len(replies) < MIN_REPLIES:
            findings.append(f"{relative}: {len(replies)} worked replies found, at least {MIN_REPLIES} expected")
        for first, reply in replies:
            findings.extend(reply_findings(relative, first, reply, project_only))
    return findings


def lint() -> int:
    """Run both halves and print one verdict."""
    findings, count = example_findings()
    if count == 0:
        print("FAILED no example file found, so nothing was linted")
        return 1
    scaffold, blocks = scaffold_findings()
    if blocks == 0:
        print("FAILED no scaffold block found, so nothing was linted")
        return 1
    findings.extend(scaffold)
    findings.extend(reply_shape_findings())
    if findings:
        for finding in findings:
            print(f"  {finding}")
        print(f"FAILED {len(findings)} finding(s) across {count} example files, {blocks} scaffold blocks and the worked replies")
        return 1
    print(f"PASSED {count} example files, {blocks} scaffold blocks and the worked replies on both packagings")
    return 0


# ───────────────────────────────────────────────────────────────
# 4. SELF-TEST
# ───────────────────────────────────────────────────────────────

def plant_in_first_block(path: Path, line: str) -> int:
    """Insert a line as the first body line of the first markdown block of a file, return its line number."""
    text = path.read_text(encoding="utf-8")
    opened_at = scaffold_blocks(text)[0][0]
    lines = text.split("\n")
    lines.insert(opened_at, line)
    path.write_text("\n".join(lines), encoding="utf-8")
    return opened_at + 1


def scaffold_cases(tree: Path) -> list[tuple[str, bool]]:
    """Plant punctuation in scaffold blocks of the scratch tree and check what the gate reports.

    The dash is built from its code point so this file never carries one. The
    cases compare against the findings the scratch copy already has, so they
    stay true while a scaffold in the real tree is still being fixed.
    """
    dash = chr(0x2014)
    source = tree / ASSETS / "story-template.md"
    mirror = tree / KNOWLEDGE / "Product Owner - Assets - Story Template.md"
    untouched = {path: path.read_text(encoding="utf-8") for path in (source, mirror)}

    def reported(path: Path, line: str, rule: str) -> bool:
        """Plant one line in a file, report whether the gate names that file, line and rule, then restore it."""
        at = plant_in_first_block(path, line)
        found, _ = scaffold_findings()
        for name, text in untouched.items():
            name.write_text(text, encoding="utf-8")
        return any(item.startswith(f"{path.relative_to(tree)}:{at}: ") and rule in item for item in found)

    def adds_nothing(path: Path, line: str) -> bool:
        """Plant one line in a file, report whether the finding count stays put, then restore it."""
        plant_in_first_block(path, line)
        found, _ = scaffold_findings()
        for name, text in untouched.items():
            name.write_text(text, encoding="utf-8")
        return len(found) == len(baseline)

    baseline, blocks = scaffold_findings()
    results = [
        ("the scaffold gate reads blocks in the skill and the mirror", blocks > 0),
        ("a prose em dash in a scaffold fails", reported(source, f"A scaffold line {dash} with a dash", "prose em dash")),
        ("a semicolon in a scaffold fails", reported(source, "A scaffold line; with a semicolon", "prose semicolon")),
        ("a dash in the Project mirror of a scaffold fails", reported(mirror, f"A scaffold line {dash} with a dash", "prose em dash")),
        ("the sanctioned bold-term definition adds no finding", adds_nothing(source, f"*   **Term** {dash} what it means")),
    ]
    # A block fenced as text holds a literal such as a path, which no voice rule reads.
    source.write_text(untouched[source] + "\n```text\nexport/a; b\n```\n", encoding="utf-8")
    found, _ = scaffold_findings()
    results.append(("a block fenced as text is not read", found == baseline))
    source.write_text(untouched[source], encoding="utf-8")
    return results


def self_test() -> int:
    """Copy the checked files to a scratch tree, break one example and one reply, require two failures."""
    global ROOT
    original = ROOT
    results = []
    with tempfile.TemporaryDirectory(prefix="po-example-lint-selftest-") as scratch:
        tree = Path(scratch)
        # The validator walks the FigJam packet beside the skill when it loads,
        # so the scratch tree carries it too.
        for relative in (VALIDATOR, Path("sk-product-owner"), Path("sk-create-figjam"), REPLY_MIRROR):
            source = original / relative
            target = tree / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            if source.is_dir():
                shutil.copytree(source, target)
            else:
                shutil.copy2(source, target)
        for mirror in (original / KNOWLEDGE).glob(MIRROR_GLOB):
            shutil.copy2(mirror, tree / KNOWLEDGE / mirror.name)
        for path in scaffold_files():
            target = tree / path.relative_to(original)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)
        ROOT = tree
        try:
            results.append(("the clean copy passes", lint() == 0))
            example = tree / EXAMPLES / "doc" / "doc-example-quick.md"
            text = example.read_text(encoding="utf-8").split("\n")
            heading = next(index for index, line in enumerate(text) if line.startswith("# "))
            text[heading] = text[heading] + " — broken"
            example.write_text("\n".join(text), encoding="utf-8")
            results.append(("a broken example fails", lint() == 1))
            example.write_text(example.read_text(encoding="utf-8").replace(" — broken", ""), encoding="utf-8")
            reply = tree / REPLY_SOURCE
            reply.write_text(
                reply.read_text(encoding="utf-8").replace(
                    "```text\nPath: `export/009", "```text\nExport complete.\nPath: `export/009", 1
                ),
                encoding="utf-8",
            )
            results.append(("a reply with a sentence before the path fails", lint() == 1))
            results.extend(scaffold_cases(tree))
        finally:
            ROOT = original
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
    return 0 if all(ok for _, ok in results) else 1


# ───────────────────────────────────────────────────────────────
# 5. ENTRY POINT
# ───────────────────────────────────────────────────────────────

def main() -> int:
    """Run the self-test when asked, the lint otherwise."""
    if "--self-test" in sys.argv[1:]:
        return self_test()
    return lint()


if __name__ == "__main__":
    sys.exit(main())
