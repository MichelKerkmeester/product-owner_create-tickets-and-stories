#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: VENDOR SYNC
# ───────────────────────────────────────────────────────────────

"""Keep a vendored skill byte-identical to its upstream, and move changes both ways.

Product Owner carries a copy of a skill that lives in the shared skill repo,
which is a different git repository. A copy with no record of where it came
from drifts silently: an edit here never reaches upstream, and an upstream fix
never arrives here. `vendor.json` records, per package, the upstream path, the
upstream commit the copy was taken at and the sha256 of every file at that
point. Every command compares three trees against that record: the local copy,
the upstream working tree and the manifest itself.

The upstream root is the folder that holds `.skilled`, found by walking up from
this repository, or `VENDOR_UPSTREAM_ROOT` when set. The override must hold
`.skilled` too, so a path one level off is a setup error and never a wrong tree.
A standalone clone has no such folder, so every command except `status --local`
says so and exits 2 rather than passing.

A package may name an `include` list of file paths. Only those files are then
hashed, pulled and pushed, so one script can be vendored out of a folder that
holds others, and a push never replaces the files beside it upstream.

A package may also name an `exclude` list. A plain name such as `node_modules`
or `dist` matches an entry of that name at any depth, and a relative path such
as `mcp-server/README.md` matches that one entry. An excluded entry is never
hashed or copied, and one that exists in the copy a pull or push replaces is
carried into the new copy, so a local build survives a pull.

A manifest that is not valid JSON, or that holds a package entry with no name,
is a setup error too, so a truncated file never reads as drift.

Every manifest path, the local and upstream paths and each include entry, must
stay beneath its root: an absolute path or a `..` part is a setup error, and
the local copy must also resolve inside this repository. A pull deletes and
rewrites the local path, so a manifest edit must never be able to aim it
elsewhere.

Symlinks are refused on both sides. A link inside a vendored tree would copy
as a pointer to a path that does not exist in a clone, and a hash of the link
target would claim a byte equality the clone cannot reproduce.

Push writes into the upstream working tree and stops there. Committing
upstream is the operator's step, and `pull` afterwards re-baselines the
manifest at the new commit.

`sync` is the one command to run after upstream moved. It leaves an entry that
is in step alone and pulls an entry that is only behind upstream. It refuses an
entry a pull would not be safe for, and it prints one line per entry. That
includes a never-pulled entry whose folder already holds other files, which only
an explicit `pull` vendors over. Under a
pulled entry it lists up to five upstream commit subjects. When the entry keeps
build output out of the copy and a dependency file changed, it also prints the
rebuild commands.

`status --local` compares each local copy with the hashes in `vendor.json` and
reads no upstream, so it works in a standalone clone too. `diff` prints what
differs between each local copy and upstream and writes nothing.

Usage:
  python3 scripts/vendor-sync.py status [--package NAME] [--local]
  python3 scripts/vendor-sync.py sync [--package NAME]
  python3 scripts/vendor-sync.py diff [--package NAME]
  python3 scripts/vendor-sync.py pull [--package NAME]
  python3 scripts/vendor-sync.py push [--package NAME]

Output:
  Each command prints package status or change details. Status and sync end
  with one line naming the entries that are out of step. Exit codes are 0 for
  success, 1 for drift, a refused sync or a difference to show, and 2 for setup
  errors.

Options:
  --package NAME  Run the command for one package from vendor.json.
  --local         With status, check the local copies against vendor.json only.
  --root PATH     Use another repository root. This internal option is hidden
                  from argparse help.
"""

# ───────────────────────────────────────────────────────────────
# 1. IMPORTS
# ───────────────────────────────────────────────────────────────

import argparse
import difflib
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any, Callable, Dict, List, Optional, Tuple

# ───────────────────────────────────────────────────────────────
# 2. CONFIGURATION
# ───────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_NAME = "vendor.json"
IGNORED_NAMES = {".DS_Store", "__pycache__"}
UPSTREAM_MARKER = ".skilled"
SUBJECT_LIMIT = 5

# A pull never touches build output, so a changed dependency file leaves the old
# build stale. The commands are the ones the repository README gives for the Code
# Mode server, which needs Node 24 because its sandbox has no build for a later Node.
BUILD_OUTPUT = {"node_modules", "dist"}
DEPENDENCY_FILES = {"package.json", "package-lock.json", ".nvmrc"}
REBUILD_COMMANDS = "nvm exec 24 npm ci && nvm exec 24 npm run build"

EXIT_OK = 0
EXIT_DRIFT = 1
EXIT_SETUP = 2


class SetupError(Exception):
    """A condition no sync can proceed past: a missing tree, a link, a bad manifest."""


# ───────────────────────────────────────────────────────────────
# 3. TREE READING
# ───────────────────────────────────────────────────────────────

def find_upstream_root(start: Path) -> Optional[Path]:
    """Find the shared skill tree above a repository or in the override.

    Args:
        start: Repository path from which to search for a ``.skilled`` folder.

    Returns:
        The upstream root, or ``None`` when no shared skill tree is available.

    Raises:
        SetupError: If the override names a folder that holds no ``.skilled``.
    """
    override = os.environ.get("VENDOR_UPSTREAM_ROOT")
    if override:
        # The override meets the test a discovered root meets, so a path one level
        # off, such as the `.skilled` folder itself, stops here with a clear line.
        if not (Path(override) / UPSTREAM_MARKER).is_dir():
            raise SetupError(f"VENDOR_UPSTREAM_ROOT holds no {UPSTREAM_MARKER} folder: {override}")
        return Path(override)
    # Walk the unresolved path: the repository may itself be reached through a
    # link, and the shared skill folder sits beside the link, not its target.
    current = Path(os.path.abspath(start))
    for candidate in [current, *current.parents]:
        if (candidate / UPSTREAM_MARKER).is_dir():
            return candidate
    return None


Skip = Callable[[str], bool]


def skip_rule(package: Optional[Dict[str, Any]] = None) -> Skip:
    """Create the shared skip predicate for hashing and copying a package.

    Args:
        package: Optional manifest entry with excluded names or paths.

    Returns:
        Predicate that marks an entry to skip.
    """
    # One test for hashing, copying and carrying over: a plain name matches at
    # any depth, a relative path matches exactly that entry.
    entries = (package or {}).get("exclude") or []
    names = IGNORED_NAMES | {e for e in entries if "/" not in e}
    paths = {e for e in entries if "/" in e}
    return lambda rel: rel.rsplit("/", 1)[-1] in names or rel in paths


def hash_tree(
    root: Path,
    include: Optional[List[str]] = None,
    skip: Optional[Skip] = None,
) -> Dict[str, str]:
    """Hash regular files in a package tree or an explicit include list.

    Args:
        root: Package directory to inspect.
        include: Optional paths that limit hashing to selected files.
        skip: Optional predicate for excluded paths.

    Returns:
        Mapping from relative file paths to SHA-256 digests.

    Raises:
        SetupError: If an included or traversed entry is a symlink.
    """
    skip = skip or skip_rule()
    if not root.is_dir():
        return {}
    if include is not None:
        hashes = {}
        for rel in sorted(include):
            path = root / rel
            if path.is_symlink():
                raise SetupError(f"symlink refused: {path}")
            if path.is_file():
                hashes[rel] = hashlib.sha256(path.read_bytes()).hexdigest()
        return hashes
    hashes: Dict[str, str] = {}
    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        here = Path(dirpath)
        dirnames[:] = sorted(d for d in dirnames if not skip((here / d).relative_to(root).as_posix()))
        kept = [f for f in sorted(filenames) if not skip((here / f).relative_to(root).as_posix())]
        for name in list(dirnames) + kept:
            if (here / name).is_symlink():
                raise SetupError(f"symlink refused: {here / name}")
        for name in kept:
            path = here / name
            hashes[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return hashes


def diff_trees(expected: Dict[str, str], actual: Dict[str, str]) -> List[str]:
    """List sorted additions, removals and changes between two hash trees.

    Args:
        expected: Baseline file digests.
        actual: Current file digests.

    Returns:
        Descriptions of all differences.
    """
    changes = []
    for rel in sorted(set(expected) | set(actual)):
        if rel not in actual:
            changes.append(f"removed {rel}")
        elif rel not in expected:
            changes.append(f"added {rel}")
        elif expected[rel] != actual[rel]:
            changes.append(f"changed {rel}")
    return changes


def changed_paths(old: Dict[str, str], new: Dict[str, str]) -> List[str]:
    """List the sorted paths whose digest differs, or that exist on one side only.

    Args:
        old: File digests before a pull.
        new: File digests after it.

    Returns:
        Relative paths of every added, removed or changed file.
    """
    return sorted(rel for rel in old.keys() | new.keys() if old.get(rel) != new.get(rel))


def upstream_commit(upstream_dir: Path, include: Optional[List[str]] = None) -> Optional[str]:
    """Read the last upstream commit affecting a package or included files.

    Args:
        upstream_dir: Package path inside the shared skill repository.
        include: Optional paths that limit the commit lookup.

    Returns:
        Commit hash, or ``None`` when Git cannot find one.
    """
    # The upstream path may be a link into another repository, so git runs from
    # the resolved folder and reports the last commit that touched it, or the
    # last one that touched the included files alone.
    real = upstream_dir.resolve()
    result = subprocess.run(
        ["git", "-C", str(real), "log", "-1", "--format=%H", "--", *(include or ["."])],
        capture_output=True, text=True,
    )
    commit = result.stdout.strip()
    return commit if result.returncode == 0 and commit else None


def commit_subjects(
    upstream_dir: Path,
    old: Optional[str],
    new: str,
    include: Optional[List[str]] = None,
) -> List[str]:
    """List the upstream commits that moved a package from one base commit to another.

    Args:
        upstream_dir: Package path inside the shared skill repository.
        old: Base commit before the pull, or ``None`` when nothing was pulled yet.
        new: Base commit after the pull.
        include: Optional paths that limit the log to selected files.

    Returns:
        One ``git log --oneline`` line per commit, newest first, or an empty list.
    """
    # A missing or unknown old commit, such as a mispinned manifest, gives no range,
    # so the list is empty and the pull still reports its files.
    if not old:
        return []
    real = upstream_dir.resolve()
    result = subprocess.run(
        ["git", "-C", str(real), "log", "--oneline", f"{old}..{new}", "--", *(include or ["."])],
        capture_output=True, text=True,
    )
    return result.stdout.splitlines() if result.returncode == 0 else []


def upstream_dirty(upstream_dir: Path, include: Optional[List[str]] = None) -> bool:
    """Check whether upstream has uncommitted changes in the selected paths.

    Args:
        upstream_dir: Package path inside the shared skill repository.
        include: Optional paths that limit the working-tree check.

    Returns:
        Whether the selected upstream paths have uncommitted changes.
    """
    # A pull records the last commit, so bytes no commit holds would be pinned
    # to a commit that does not contain them.
    real = upstream_dir.resolve()
    result = subprocess.run(
        ["git", "-C", str(real), "status", "--porcelain", "--", *(include or ["."])],
        capture_output=True, text=True,
    )
    return result.returncode != 0 or bool(result.stdout.strip())


# ───────────────────────────────────────────────────────────────
# 4. MANIFEST
# ───────────────────────────────────────────────────────────────

def load_manifest(repo_root: Path) -> Dict[str, Any]:
    """Load and validate the vendoring manifest.

    Args:
        repo_root: Repository root containing ``vendor.json``.

    Returns:
        Parsed manifest with at least one package, each a named object.

    Raises:
        SetupError: If the manifest is missing, unreadable, not valid JSON, not
            an object, has no package list, or holds an entry that is not an
            object with a name.
    """
    path = repo_root / MANIFEST_NAME
    if not path.is_file():
        raise SetupError(f"no {MANIFEST_NAME} at {repo_root}")
    # A truncated or hand-edited manifest is the likeliest way this file breaks,
    # and a traceback would exit 1, which every caller reads as drift.
    try:
        manifest = json.loads(path.read_text())
    except json.JSONDecodeError as error:
        raise SetupError(f"{MANIFEST_NAME} is not valid JSON: {error}") from None
    except (OSError, UnicodeDecodeError) as error:
        raise SetupError(f"{MANIFEST_NAME} cannot be read: {error}") from None
    if not isinstance(manifest, dict):
        raise SetupError(f"{MANIFEST_NAME} is not a JSON object")
    packages = manifest.get("packages")
    if not isinstance(packages, list) or not packages:
        raise SetupError(f"{MANIFEST_NAME} declares no packages")
    # Every command reads a package's name, so checking the entries here covers
    # them all rather than leaving each handler to fail on its own.
    for position, package in enumerate(packages, start=1):
        if not isinstance(package, dict):
            raise SetupError(f"{MANIFEST_NAME} package {position} is not an object")
        name = package.get("name")
        if not isinstance(name, str) or not name:
            raise SetupError(f"{MANIFEST_NAME} package {position} has no name")
        if package.get("files") is not None and not isinstance(package["files"], dict):
            raise SetupError(f"{MANIFEST_NAME} files of {name} is not an object")
    return manifest


def save_manifest(repo_root: Path, manifest: Dict[str, Any]) -> None:
    """Write the updated manifest with stable indentation.

    Args:
        repo_root: Repository root containing ``vendor.json``.
        manifest: Updated manifest data.
    """
    (repo_root / MANIFEST_NAME).write_text(json.dumps(manifest, indent=2, sort_keys=False) + "\n")


def select_packages(
    manifest: Dict[str, Any],
    name: Optional[str],
) -> List[Dict[str, Any]]:
    """Select all packages or one named package from a manifest.

    Args:
        manifest: Parsed vendor manifest.
        name: Optional package name filter.

    Returns:
        Matching package entries.

    Raises:
        SetupError: If the requested package is not declared.
    """
    packages = manifest["packages"]
    if name is None:
        return packages
    chosen = [p for p in packages if p.get("name") == name]
    if not chosen:
        raise SetupError(f"no package named {name} in {MANIFEST_NAME}")
    return chosen


def contained_path(field: str, value: object) -> PurePosixPath:
    """Parse a manifest path and reject values that escape its root.

    Args:
        field: Manifest field name used in any error message.
        value: Candidate relative path.

    Returns:
        Valid relative POSIX path.

    Raises:
        SetupError: If the value is empty, absolute or contains traversal.
    """
    # Every manifest path stays beneath its root by spelling alone. The upstream
    # path is reached through the `.skilled` link, so a resolved-path check would
    # refuse it, while an absolute path or a `..` part is refused on any side.
    if not isinstance(value, str) or not value.strip():
        raise SetupError(f"{MANIFEST_NAME} {field} is empty or not a path")
    rel = PurePosixPath(value)
    if rel.is_absolute() or ".." in rel.parts or "\\" in value:
        raise SetupError(f"{MANIFEST_NAME} {field} escapes its root: {value}")
    return rel


def resolve_local_dir(
    repo_root: Path,
    package: Dict[str, Any],
) -> Path:
    """Resolve and validate a package's local directory and its include and exclude lists.

    Args:
        repo_root: Repository root containing the local package copy.
        package: Manifest entry with a local path.

    Returns:
        Local package directory.

    Raises:
        SetupError: If the local path or a list entry is invalid.
    """
    local_rel = contained_path("local_path", package.get("local_path"))
    include = package.get("include")
    if include is not None:
        if not isinstance(include, list):
            raise SetupError(f"{MANIFEST_NAME} include is not a list")
        for rel in include:
            contained_path("include entry", rel)
    exclude = package.get("exclude")
    if exclude is not None:
        if not isinstance(exclude, list):
            raise SetupError(f"{MANIFEST_NAME} exclude is not a list")
        for entry in exclude:
            contained_path("exclude entry", entry)
        if include is not None:
            raise SetupError(f"{MANIFEST_NAME} a package names include or exclude, not both")
    local_dir = repo_root / local_rel
    # The local copy is written and deleted, so its resolved location must also
    # sit inside the repository: a link on the way would carry it out.
    try:
        local_dir.resolve().relative_to(repo_root.resolve())
    except ValueError:
        raise SetupError(f"{MANIFEST_NAME} local_path resolves outside the repository: {local_rel}") from None
    if local_dir.resolve() == repo_root.resolve():
        raise SetupError(f"{MANIFEST_NAME} local_path names the repository root itself")
    return local_dir


def resolve_dirs(
    repo_root: Path,
    package: Dict[str, Any],
) -> Tuple[Path, Path]:
    """Resolve and validate a package's local and upstream directories.

    Args:
        repo_root: Repository root containing the local package copy.
        package: Manifest entry with local and upstream paths.

    Returns:
        Local package directory and upstream package directory.

    Raises:
        SetupError: If paths are invalid or the upstream tree is unavailable.
    """
    local_dir = resolve_local_dir(repo_root, package)
    upstream_rel = contained_path("upstream_path", package.get("upstream_path"))
    upstream_root = find_upstream_root(repo_root)
    if upstream_root is None:
        raise SetupError("no folder holding .skilled above this repository; set VENDOR_UPSTREAM_ROOT")
    upstream_dir = upstream_root / upstream_rel
    if not upstream_dir.is_dir():
        raise SetupError(f"upstream path missing: {upstream_dir}")
    return local_dir, upstream_dir


# ───────────────────────────────────────────────────────────────
# 5. COMMANDS
# ───────────────────────────────────────────────────────────────

def carry_excluded(old: Path, new: Path, skip: Skip) -> None:
    """Move excluded local entries into the replacement package tree.

    Args:
        old: Existing local package directory.
        new: Staged replacement directory.
        skip: Predicate identifying excluded paths.
    """
    # Moves each excluded entry of the replaced copy into the new one, at the
    # same place, so build output such as node_modules outlives the swap.
    for dirpath, dirnames, filenames in os.walk(old, followlinks=False):
        here = Path(dirpath)
        for name in dirnames + filenames:
            rel = (here / name).relative_to(old).as_posix()
            dest = new / rel
            if not skip(rel) or name in IGNORED_NAMES:
                continue
            if dest.parent.is_dir() and not dest.exists():
                (here / name).rename(dest)
        dirnames[:] = [d for d in dirnames if (here / d).exists()]


def copy_tree(
    source: Path,
    target: Path,
    include: Optional[List[str]] = None,
    skip: Optional[Skip] = None,
) -> None:
    """Copy a full package or only its included files to a target tree.

    Args:
        source: Source package directory.
        target: Destination package directory.
        include: Optional paths that limit the copy to selected files.
        skip: Optional predicate for entries excluded from a full copy.
    """
    skip = skip or skip_rule()
    if include is not None:
        # File by file, so the files beside an included one are never touched.
        for rel in include:
            src, dst = source / rel, target / rel
            if src.is_file():
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
            elif dst.is_file():
                dst.unlink()
        return
    # The new copy is built beside the old one and swapped in by rename, so an
    # interrupted pull leaves either the old packet or the new one, never a partial one.
    staging = target.with_name(target.name + ".pull-new")
    retired = target.with_name(target.name + ".pull-old")
    for leftover in (staging, retired):
        if leftover.exists():
            shutil.rmtree(leftover)

    def ignore(directory: str, names: List[str]) -> List[str]:
        """Return names excluded from one source directory copy."""
        base = Path(directory).relative_to(source)
        return [n for n in names if skip((base / n).as_posix())]

    shutil.copytree(source, staging, ignore=ignore)
    if target.exists():
        carry_excluded(target, staging, skip)
        target.rename(retired)
    staging.rename(target)
    if retired.exists():
        shutil.rmtree(retired)


def status_lines(repo_root: Path, package: Dict[str, Any]) -> Tuple[int, List[str]]:
    """Compare the local and upstream package with the manifest.

    Args:
        repo_root: Repository root containing ``vendor.json``.
        package: Manifest entry to compare.

    Returns:
        Zero and the report lines when the package is in step, one and the
        report lines when it has drifted.
    """
    local_dir, upstream_dir = resolve_dirs(repo_root, package)
    recorded = package.get("files") or {}
    include, skip = package.get("include"), skip_rule(package)
    local_changes = diff_trees(recorded, hash_tree(local_dir, include, skip))
    upstream_changes = diff_trees(recorded, hash_tree(upstream_dir, include, skip))
    name = package["name"]
    if not recorded:
        return EXIT_DRIFT, [f"{name}: never pulled; run pull to vendor it"]
    if not local_changes and not upstream_changes:
        current = upstream_commit(upstream_dir, include)
        if package.get("base_commit") != current:
            return EXIT_DRIFT, [
                f"{name}: files in step, but the manifest pins {package.get('base_commit')} and "
                f"upstream's last commit is {current}"
            ]
        return EXIT_OK, [f"{name}: in step at {package.get('base_commit')}, {len(recorded)} files"]
    lines = []
    if local_changes:
        lines.append(f"{name}: local-ahead, {len(local_changes)} change(s)")
        lines.extend(f"  local {change}" for change in local_changes)
    if upstream_changes:
        lines.append(f"{name}: upstream-ahead, {len(upstream_changes)} change(s)")
        lines.extend(f"  upstream {change}" for change in upstream_changes)
    return EXIT_DRIFT, lines


def status_package(repo_root: Path, package: Dict[str, Any]) -> int:
    """Report whether the local and upstream package match the manifest.

    Args:
        repo_root: Repository root containing ``vendor.json``.
        package: Manifest entry to compare.

    Returns:
        Zero when the package is in step, one when it has drifted.
    """
    code, lines = status_lines(repo_root, package)
    print("\n".join(lines))
    return code


def status_local_package(repo_root: Path, package: Dict[str, Any]) -> int:
    """Report whether the local package copy matches the hashes in the manifest.

    Args:
        repo_root: Repository root containing ``vendor.json``.
        package: Manifest entry to compare.

    Returns:
        Zero when the local copy matches its record, one when it differs.

    Raises:
        SetupError: If a manifest path is invalid or the copy holds a symlink.
    """
    # Reads the local copy and the manifest alone, so a standalone clone with no
    # upstream can still prove that no vendored file was edited by hand.
    local_dir = resolve_local_dir(repo_root, package)
    recorded = package.get("files") or {}
    name = package["name"]
    if not recorded:
        print(f"{name}: never pulled; nothing recorded to compare with")
        return EXIT_DRIFT
    changes = diff_trees(recorded, hash_tree(local_dir, package.get("include"), skip_rule(package)))
    if not changes:
        print(f"{name}: local copy matches vendor.json, {len(recorded)} files")
        return EXIT_OK
    print(f"{name}: local copy differs from vendor.json, {len(changes)} change(s)")
    for change in changes:
        print(f"  local {change}")
    return EXIT_DRIFT


def file_diff(rel: str, local_path: Path, upstream_path: Path) -> List[str]:
    """Build the report lines for one file that differs between the local copy and upstream.

    Args:
        rel: Package-relative path shown in the report.
        local_path: File in the local copy.
        upstream_path: File in the upstream tree.

    Returns:
        A unified diff for a text file, or one note for a binary file.
    """
    old, new = local_path.read_bytes(), upstream_path.read_bytes()
    binary = [f"  binary file differs {rel}"]
    if b"\0" in old or b"\0" in new:
        return binary
    try:
        old_lines, new_lines = old.decode("utf-8").splitlines(), new.decode("utf-8").splitlines()
    except UnicodeDecodeError:
        return binary
    lines = list(difflib.unified_diff(old_lines, new_lines, f"local/{rel}", f"upstream/{rel}", lineterm=""))
    # Equal lines with different bytes means only a line ending or the final newline moved.
    return lines or [f"  line endings or the final newline differ {rel}"]


def diff_package(repo_root: Path, package: Dict[str, Any]) -> int:
    """Print what differs between the local package copy and the upstream working tree.

    Args:
        repo_root: Repository root containing the local package copy.
        package: Manifest entry to compare.

    Returns:
        Zero when the two trees hold the same files, one when they differ.

    Raises:
        SetupError: If paths or the upstream tree cannot be resolved.
    """
    local_dir, upstream_dir = resolve_dirs(repo_root, package)
    include, skip = package.get("include"), skip_rule(package)
    local = hash_tree(local_dir, include, skip)
    upstream = hash_tree(upstream_dir, include, skip)
    differing = changed_paths(local, upstream)
    name = package["name"]
    if not differing:
        print(f"{name}: no differences")
        return EXIT_OK
    print(f"{name}: {len(differing)} file(s) differ")
    for rel in differing:
        if rel not in upstream:
            print(f"  only in local {rel}")
        elif rel not in local:
            print(f"  only in upstream {rel}")
        else:
            print("\n".join(file_diff(rel, local_dir / rel, upstream_dir / rel)))
    return EXIT_DRIFT


def pull_entry(repo_root: Path, package: Dict[str, Any]) -> Optional[str]:
    """Copy upstream package files to the local tree and update the baseline.

    Args:
        repo_root: Repository root containing the local package copy.
        package: Manifest entry to pull.

    Returns:
        The reason drift blocked the pull, or ``None`` when the pull completed.

    Raises:
        SetupError: If paths or the upstream commit cannot be resolved.
    """
    local_dir, upstream_dir = resolve_dirs(repo_root, package)
    recorded = package.get("files") or {}
    include, skip = package.get("include"), skip_rule(package)
    local = hash_tree(local_dir, include, skip)
    upstream = hash_tree(upstream_dir, include, skip)
    # Local edits that upstream already carries are a finished push, not a
    # conflict, so they may be overwritten. Anything else would be lost.
    if recorded and diff_trees(recorded, local) and diff_trees(upstream, local):
        return "the local copy has edits upstream does not carry; push them first"
    if upstream_dirty(upstream_dir, include):
        return "upstream has uncommitted changes; commit them first"
    commit = upstream_commit(upstream_dir, include)
    if commit is None:
        raise SetupError(
            f"cannot read the last upstream commit for {package['name']}; "
            f"is {upstream_dir} inside a git repository?"
        )
    copy_tree(upstream_dir, local_dir, include, skip)
    package["files"] = hash_tree(local_dir, include, skip)
    package["base_commit"] = commit
    save_manifest(repo_root, _manifest_with(repo_root, package))
    return None


def pull_package(repo_root: Path, package: Dict[str, Any]) -> int:
    """Pull one package and report the result.

    Args:
        repo_root: Repository root containing the local package copy.
        package: Manifest entry to pull.

    Returns:
        Zero when the pull completes, one when drift blocks it.

    Raises:
        SetupError: If paths or the upstream commit cannot be resolved.
    """
    refusal = pull_entry(repo_root, package)
    if refusal:
        print(f"{package['name']}: pull refused, {refusal}")
        return EXIT_DRIFT
    print(f"{package['name']}: pulled {len(package['files'])} files at {package['base_commit']}")
    return EXIT_OK


def sync_package(repo_root: Path, package: Dict[str, Any]) -> int:
    """Bring one package in step with upstream, touching nothing when it already is.

    Args:
        repo_root: Repository root containing the local package copy.
        package: Manifest entry to sync.

    Returns:
        Zero when the package ends in step, one when the pull was refused.

    Raises:
        SetupError: If paths or the upstream commit cannot be resolved.
    """
    name = package["name"]
    code, _ = status_lines(repo_root, package)
    if code == EXIT_OK:
        print(f"{name}: in step at {package.get('base_commit')}")
        return EXIT_OK
    old_files, old_commit = dict(package.get("files") or {}), package.get("base_commit")
    # A pull finds local edits by comparing with the recorded hashes, and a never-pulled
    # entry has none, so files already in its folder would be overwritten unseen.
    if not old_files:
        local_dir, upstream_dir = resolve_dirs(repo_root, package)
        include, skip = package.get("include"), skip_rule(package)
        local = hash_tree(local_dir, include, skip)
        if local and local != hash_tree(upstream_dir, include, skip):
            print(f"{name}: refused, never pulled and its folder holds files upstream does not match; run pull to vendor over them")
            return EXIT_DRIFT
    refusal = pull_entry(repo_root, package)
    if refusal:
        print(f"{name}: refused, {refusal}")
        return EXIT_DRIFT
    changed = changed_paths(old_files, package["files"])
    print(f"{name}: pulled, {len(changed)} file(s) changed, now at {package['base_commit']}")
    _, upstream_dir = resolve_dirs(repo_root, package)
    subjects = commit_subjects(upstream_dir, old_commit, package["base_commit"], package.get("include"))
    for subject in subjects[:SUBJECT_LIMIT]:
        print(f"  {subject}")
    if len(subjects) > SUBJECT_LIMIT:
        print(f"  and {len(subjects) - SUBJECT_LIMIT} more")
    if BUILD_OUTPUT & set(package.get("exclude") or []):
        folders = {
            (PurePosixPath(package["local_path"]) / PurePosixPath(rel).parent).as_posix()
            for rel in changed if PurePosixPath(rel).name in DEPENDENCY_FILES
        }
        for folder in sorted(folders):
            print(f"  rebuild: cd {folder} && {REBUILD_COMMANDS}")
    return EXIT_OK


def push_package(repo_root: Path, package: Dict[str, Any]) -> int:
    """Copy local package changes into an unchanged upstream working tree.

    Args:
        repo_root: Repository root containing the local package copy.
        package: Manifest entry to push.

    Returns:
        Zero when the push completes or has no changes, one when drift blocks it.

    Raises:
        SetupError: If package paths or the upstream tree cannot be resolved.
    """
    local_dir, upstream_dir = resolve_dirs(repo_root, package)
    recorded = package.get("files") or {}
    if not recorded:
        print(f"{package['name']}: push refused, nothing was ever pulled")
        return EXIT_DRIFT
    include, skip = package.get("include"), skip_rule(package)
    local_changes = diff_trees(recorded, hash_tree(local_dir, include, skip))
    if diff_trees(recorded, hash_tree(upstream_dir, include, skip)):
        print(f"{package['name']}: push refused, upstream moved since the base commit; pull first")
        return EXIT_DRIFT
    if not local_changes:
        print(f"{package['name']}: nothing to push")
        return EXIT_OK
    copy_tree(local_dir, upstream_dir, include, skip)
    print(f"{package['name']}: pushed {len(local_changes)} change(s) into {upstream_dir}")
    for change in local_changes:
        print(f"  {change}")
    print("commit them upstream, then run pull to re-baseline the manifest")
    return EXIT_OK


def _manifest_with(
    repo_root: Path,
    package: Dict[str, Any],
) -> Dict[str, Any]:
    """Return the manifest with one package entry replaced by its updated record."""
    manifest = load_manifest(repo_root)
    manifest["packages"] = [package if p.get("name") == package["name"] else p for p in manifest["packages"]]
    return manifest


COMMANDS = {
    "status": status_package,
    "sync": sync_package,
    "diff": diff_package,
    "pull": pull_package,
    "push": push_package,
}


# ───────────────────────────────────────────────────────────────
# 6. MAIN
# ───────────────────────────────────────────────────────────────

COMMAND_HELP = """commands:
  status  compare each local copy and upstream with vendor.json (--local: local copy only)
  sync    pull every entry that is behind upstream and leave the rest alone
  diff    print what differs between each local copy and upstream
  pull    copy upstream into the local copy and re-baseline vendor.json
  push    copy local edits into the upstream working tree
"""


def main(argv: Optional[List[str]] = None) -> int:
    """Run one vendor-sync command for all or one selected package.

    Args:
        argv: Optional command-line arguments, excluding the executable name.

    Returns:
        The highest exit status returned by the selected package commands.
    """
    parser = argparse.ArgumentParser(
        description="Sync vendored skills with their upstream.",
        epilog=COMMAND_HELP,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("command", choices=sorted(COMMANDS))
    parser.add_argument("--package", default=None, help="run the command for one entry of vendor.json")
    parser.add_argument("--local", action="store_true", help="with status, read no upstream (works in a clone)")
    parser.add_argument("--root", default=str(REPO_ROOT), help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    if args.local and args.command != "status":
        parser.error("--local is valid only with status")
    repo_root = Path(args.root)
    handler = status_local_package if args.local else COMMANDS[args.command]
    try:
        manifest = load_manifest(repo_root)
        selected = select_packages(manifest, args.package)
        worst = EXIT_OK
        out_of_step = []
        for package in selected:
            code = handler(repo_root, package)
            worst = max(worst, code)
            if code != EXIT_OK:
                out_of_step.append(package["name"])
        # A red entry hides among the green lines above it, so the output ends by naming it.
        if out_of_step and args.command in ("status", "sync"):
            print(f"{len(out_of_step)} of {len(selected)} entries out of step: {', '.join(out_of_step)}")
        return worst
    except SetupError as error:
        print(f"vendor-sync: {error}", file=sys.stderr)
        return EXIT_SETUP


if __name__ == "__main__":
    sys.exit(main())
