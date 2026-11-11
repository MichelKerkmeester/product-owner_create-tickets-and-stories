#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: IDENTIFIER SCAN GATE
# ───────────────────────────────────────────────────────────────

"""Fail when a tracked file holds an identifier this public repository must not carry.

The skill states that a link's value never enters a tracked file, but no check
read the tracked files for one, so a ClickUp workspace id, a work email address,
a Figma team id and an absolute home path all reached the history through
specs, reports and a vendored reference. Redacting them once holds only until
the next report is committed, so this gate reads every tracked file on each run.

Four rules apply, each a pattern and never a stored value:

  clickup-workspace-id  an 11-digit number that begins 9015
  company-email         an email address at the company domain
  figma-team-id         `team::` followed by six or more digits
  home-path             an absolute home path under /Users/ for any name that is
                        not a placeholder such as name, user, username, you or example

A finding prints the file, the line and the rule name and never the matched
value, so a failing run cannot copy the identifier into a log. The files are the
ones `git ls-files` lists, so ignored and untracked files stay out of scope. A
tracked symlink is read as its target path, because an absolute link is how a
home path lands in the history without any file text. A file that holds a NUL
byte is binary and a file over 5 MB is too large to read in full, so both are
skipped and the verdict line counts them.

There is no allowlist. Every placeholder form a document needs already passes
the home-path rule, and a path or file that is exempt by name would become the
place an identifier hides.

Usage:
  check_identifiers.py             -> exit 0 when no tracked file holds one, exit 1 otherwise
  check_identifiers.py --all       -> list every finding, where the default lists the first 20 per rule
  check_identifiers.py --self-test -> prove each rule fires, placeholders pass and a finding never prints its value

Exit codes: 0 clean, 1 at least one finding, 2 setup error such as a folder that is not a git repository.
"""

from __future__ import annotations

import bisect
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import NamedTuple

# ───────────────────────────────────────────────────────────────
# 1. CONFIGURATION
# ───────────────────────────────────────────────────────────────

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("PO_ROOT") or HERE.parent.parent)

USAGE = "usage: check_identifiers.py [--all | --self-test]"
MAX_BYTES = 5 * 1024 * 1024
BINARY_SNIFF = 8192
FINDING_LIMIT = 20


class Rule(NamedTuple):
    """One private-identifier pattern and the lower-case captures that are placeholders."""

    name: str
    pattern: re.Pattern[str]
    placeholders: frozenset[str] = frozenset()


RULES = (
    Rule("clickup-workspace-id", re.compile(r"(?<!\d)9015\d{7}(?!\d)")),
    # The pattern opens on the at sign with a one-character lookbehind for the local part.
    # A leading run such as [A-Za-z0-9._%+-]+ re-scans every long token in a report, which
    # took 76 of the 79 seconds this gate first needed over the tracked tree.
    Rule("company-email", re.compile(r"(?<=[A-Za-z0-9._%+-])@(?:[A-Za-z0-9-]+\.)*getbarter\.com\b", re.IGNORECASE)),
    Rule("figma-team-id", re.compile(r"team::\d{6,}")),
    Rule(
        "home-path",
        re.compile(r"/Users/([A-Za-z0-9][A-Za-z0-9._-]*)"),
        frozenset({"name", "user", "username", "you", "example"}),
    ),
)
RULE_NAMES = tuple(rule.name for rule in RULES)


class SetupError(Exception):
    """A condition no scan can proceed past, such as a folder that is not a git repository."""


class Scan(NamedTuple):
    """The findings of one scan and how many files it read or skipped."""

    findings: list[tuple[str, int, str]]
    scanned: int
    binary: int
    oversize: int


# ───────────────────────────────────────────────────────────────
# 2. HELPERS
# ───────────────────────────────────────────────────────────────

def git_env(root: Path) -> dict[str, str]:
    """Return an environment that makes git read `root` and nothing a caller exported.

    A git hook exports GIT_DIR and GIT_INDEX_FILE for its own repository. Left in
    place they would aim a scan of another folder at the hook's repository. The
    ceiling stops git walking above `root`, so a folder that is not a repository
    fails here instead of borrowing the repository that happens to contain it.
    """
    env = {key: value for key, value in os.environ.items() if key not in {"GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE"}}
    env["GIT_CEILING_DIRECTORIES"] = str(root.parent)
    return env


def tracked_files(root: Path) -> list[str]:
    """Return the repository-relative paths git tracks under `root`.

    Args:
        root: Repository root to list.

    Returns:
        Tracked paths, read NUL-separated so a name with a space or a dash survives unquoted.

    Raises:
        SetupError: If git is missing or `root` is not a git repository.
    """
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-z"],
            capture_output=True,
            env=git_env(root),
        )
    except OSError as error:
        raise SetupError(f"git could not run: {error}") from None
    if result.returncode != 0:
        raise SetupError(f"{root} is not a git repository, so there are no tracked files to read")
    return [name for name in result.stdout.decode("utf-8", errors="replace").split("\0") if name]


def scan_text(text: str) -> list[tuple[int, str]]:
    """Return one (line, rule) pair for each rule that matches on a line of `text`.

    Lines count the way `grep -n` counts them, by newline only, so a finding
    points at the line an editor shows.
    """
    found: set[tuple[int, str]] = set()
    newlines: list[int] | None = None
    for rule in RULES:
        for match in rule.pattern.finditer(text):
            if rule.placeholders and match.group(1).rstrip("._-").lower() in rule.placeholders:
                continue
            if newlines is None:
                newlines = [hit.start() for hit in re.finditer("\n", text)]
            found.add((bisect.bisect_left(newlines, match.start()) + 1, rule.name))
    return sorted(found)


def scan_file(path: Path) -> tuple[str, list[tuple[int, str]]]:
    """Read one tracked path and return how it was handled and what it holds.

    Returns:
        ("scanned", findings), ("binary", []), ("oversize", []) or ("missing", []).
        A path git still tracks but the working tree no longer holds is missing,
        which a pending deletion leaves behind.
    """
    try:
        if path.is_symlink():
            return "scanned", scan_text(os.readlink(path))
        if not path.is_file():
            return "missing", []
        if path.stat().st_size > MAX_BYTES:
            return "oversize", []
        data = path.read_bytes()
    except OSError:
        return "missing", []
    if b"\0" in data[:BINARY_SNIFF]:
        return "binary", []
    return "scanned", scan_text(data.decode("utf-8", errors="replace"))


# ───────────────────────────────────────────────────────────────
# 3. CORE LOGIC
# ───────────────────────────────────────────────────────────────

def scan_repo(root: Path) -> Scan:
    """Scan every tracked file under `root` and return the findings with the file counts."""
    findings: list[tuple[str, int, str]] = []
    scanned = binary = oversize = 0
    for name in tracked_files(root):
        status, hits = scan_file(root / name)
        if status == "scanned":
            scanned += 1
        elif status == "binary":
            binary += 1
        elif status == "oversize":
            oversize += 1
        findings.extend((name, line, rule) for line, rule in hits)
    return Scan(findings, scanned, binary, oversize)


def report_lines(scan: Scan, show_all: bool) -> list[str]:
    """Render a scan as finding lines, per-rule counts and a verdict, with no matched value in any of them."""
    lines: list[str] = []
    shown: dict[str, int] = {}
    hidden: dict[str, int] = {}
    for path, number, rule in sorted(scan.findings):
        if show_all or shown.get(rule, 0) < FINDING_LIMIT:
            lines.append(f"  {path}:{number}: {rule}")
            shown[rule] = shown.get(rule, 0) + 1
        else:
            hidden[rule] = hidden.get(rule, 0) + 1
    for rule in RULE_NAMES:
        if hidden.get(rule):
            lines.append(f"  ... {hidden[rule]} more {rule} finding(s), run with --all to list them")
    skipped = f"{scan.binary} binary and {scan.oversize} over {MAX_BYTES // (1024 * 1024)} MB skipped"
    if not scan.findings:
        lines.append(f"PASSED {scan.scanned} tracked files hold no private identifier ({skipped})")
        return lines
    for rule in RULE_NAMES:
        hits = [finding for finding in scan.findings if finding[2] == rule]
        if hits:
            lines.append(f"  {rule}: {len({finding[0] for finding in hits})} file(s), {len(hits)} line(s)")
    files = len({finding[0] for finding in scan.findings})
    lines.append(f"FAILED {len(scan.findings)} finding(s) in {files} file(s) of {scan.scanned} scanned ({skipped})")
    return lines


def lint(show_all: bool) -> int:
    """Scan the repository, print the report and return the exit code."""
    try:
        scan = scan_repo(ROOT)
    except SetupError as error:
        print(f"FAILED setup: {error}")
        return 2
    if scan.scanned == 0:
        print("FAILED no tracked file was read, so nothing was scanned")
        return 1
    for line in report_lines(scan, show_all):
        print(line)
    return 1 if scan.findings else 0


# ───────────────────────────────────────────────────────────────
# 4. SELF-TEST
# ───────────────────────────────────────────────────────────────

def synthetic_values() -> dict[str, str]:
    """Return one made-up value per rule, assembled from parts.

    The parts keep this file clear of its own rules, so the gate passes on the
    script that defines it and no real identifier is stored anywhere in a test.
    """
    return {
        "clickup-workspace-id": "9015" + "0000001",
        "company-email": "jane.doe@" + "getbarter" + ".com",
        "figma-team-id": "team::" + "123456",
        "home-path": "/Users/" + "alice" + "/work/notes.md",
    }


def near_misses() -> list[str]:
    """Return values that look close to a rule but are not private identifiers."""
    return [
        "9015" + "000001",
        "9015" + "000000001",
        "team::" + "12345",
        "team::" + "<redacted>",
        "jane.doe@" + "example" + ".com",
        "https://" + "getbarter" + ".com/pricing",
        "/Users/" + "<user>" + "/work",
        "/Users/" + "you" + "/work",
        "/Users/" + "Username" + "/work",
        "/Users/" + "example" + ".",
        "/Users/" + "name" + "/work",
    ]


def make_repo(base: Path, files: dict[str, bytes], untracked: dict[str, bytes]) -> Path:
    """Build a throwaway git repository holding `files` as tracked and `untracked` as plain files."""
    repo = base / "repo"
    repo.mkdir()
    env = git_env(repo)
    subprocess.run(["git", "-C", str(repo), "init", "-q"], check=True, env=env)
    for name, data in {**files, **untracked}.items():
        target = repo / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    subprocess.run(["git", "-C", str(repo), "add", "--", *files], check=True, env=env)
    return repo


def self_test() -> int:
    """Prove each rule fires, a placeholder passes and the scan reads only what it should."""
    results: list[tuple[str, bool]] = []
    values = synthetic_values()
    for rule in RULE_NAMES:
        results.append((f"{rule} flags its value", scan_text(f"see {values[rule]} here") == [(1, rule)]))
    results.append(("a near miss or placeholder passes", all(scan_text(value) == [] for value in near_misses())))
    results.append(("a second line is reported on its own line", scan_text("clean\n" + values["figma-team-id"]) == [(2, "figma-team-id")]))

    many = Scan([(f"f{index}.md", 1, "home-path") for index in range(FINDING_LIMIT + 5)], 30, 0, 0)
    capped = report_lines(many, show_all=False)
    results.append(("the default lists a capped number per rule and says how many it left out", sum(line.startswith("  f") for line in capped) == FINDING_LIMIT and any("5 more home-path" in line for line in capped)))
    results.append(("--all lists every finding", sum(line.startswith("  f") for line in report_lines(many, show_all=True)) == FINDING_LIMIT + 5))

    with tempfile.TemporaryDirectory(prefix="po-identifier-scan-") as scratch:
        base = Path(scratch)
        text = "line one\n" + values["home-path"] + "\n"
        sniff = Path(base / "sniff.bin")
        sniff.write_bytes(b"\0" + text.encode())
        big = Path(base / "big.txt")
        big.write_bytes(text.encode() + b"x" * MAX_BYTES)
        plain = Path(base / "plain.txt")
        plain.write_text(text)
        results.append(("a text file is read", scan_file(plain) == ("scanned", [(2, "home-path")])))
        results.append(("a binary file is skipped", scan_file(sniff) == ("binary", [])))
        results.append(("a file over the size limit is skipped", scan_file(big) == ("oversize", [])))
        results.append(("a path that no longer exists is skipped", scan_file(base / "gone.txt") == ("missing", [])))

        # A folder in this repository is named with spaces and a non-ASCII dash, so the
        # fixture name carries both to prove they survive the listing unquoted.
        spaced = "notes/a b " + chr(0x2014) + " c.md"
        repo_base = base / "world"
        repo_base.mkdir()
        repo = make_repo(
            repo_base,
            {spaced: text.encode(), "clean.md": b"nothing here\n", "removed.md": text.encode()},
            {"untracked.md": text.encode()},
        )
        (repo / "removed.md").unlink()
        os.symlink(values["home-path"], repo / "link.md")
        subprocess.run(["git", "-C", str(repo), "add", "link.md"], check=True, env=git_env(repo))
        scan = scan_repo(repo)
        results.append(
            (
                "only tracked files are read, a spaced name survives and a pending deletion is skipped",
                sorted(scan.findings) == [("link.md", 1, "home-path"), (spaced, 2, "home-path")] and scan.scanned == 3,
            )
        )
        rendered = "\n".join(report_lines(scan, show_all=False))
        results.append(
            (
                "a finding names file, line and rule and never the value",
                "link.md:1: home-path" in rendered and "alice" not in rendered and values["home-path"] not in rendered,
            )
        )
        stranger = base / "stranger"
        stranger.mkdir()
        try:
            tracked_files(stranger)
            refused = False
        except SetupError:
            refused = True
        results.append(("a folder that is not a repository is a setup error", refused))

    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
    return 0 if all(ok for _, ok in results) else 1


# ───────────────────────────────────────────────────────────────
# 5. ENTRY POINT
# ───────────────────────────────────────────────────────────────

def main() -> int:
    """Run the self-test when asked, the scan otherwise."""
    args = set(sys.argv[1:])
    if args - {"--self-test", "--all"}:
        print(USAGE, file=sys.stderr)
        return 2
    if "--self-test" in args:
        return self_test()
    return lint("--all" in args)


if __name__ == "__main__":
    sys.exit(main())
