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
this repository, or `VENDOR_UPSTREAM_ROOT` when set. A standalone clone has no
such folder, and every command then says so and exits 2 rather than passing.

A package may name an `include` list of file paths. Only those files are then
hashed, pulled and pushed, so one script can be vendored out of a folder that
holds others, and a push never replaces the files beside it upstream.

A package may also name an `exclude` list. A plain name such as `node_modules`
or `dist` matches an entry of that name at any depth, and a relative path such
as `mcp-server/README.md` matches that one entry. An excluded entry is never
hashed or copied, and one that exists in the copy a pull or push replaces is
carried into the new copy, so a local build survives a pull.

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

Usage:
  python3 scripts/vendor-sync.py status [--package NAME]
  python3 scripts/vendor-sync.py pull [--package NAME]
  python3 scripts/vendor-sync.py push [--package NAME]

Output:
  Each command prints package status or change details. Exit codes are 0 for
  success, 1 for drift or a refused sync, and 2 for setup errors.

Options:
  --package NAME  Run the command for one package from vendor.json.
  --root PATH     Use another repository root. This internal option is hidden
                  from argparse help.
"""

# ───────────────────────────────────────────────────────────────
# 1. IMPORTS
# ───────────────────────────────────────────────────────────────

import argparse
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
    """
    override = os.environ.get("VENDOR_UPSTREAM_ROOT")
    if override:
        return Path(override)
    # Walk the unresolved path: the repository may itself be reached through a
    # link, and the shared skill folder sits beside the link, not its target.
    current = Path(os.path.abspath(start))
    for candidate in [current, *current.parents]:
        if (candidate / ".skilled").is_dir():
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
        Parsed manifest with at least one package.

    Raises:
        SetupError: If the manifest is missing or has no package list.
        json.JSONDecodeError: If the manifest is not valid JSON.
    """
    path = repo_root / MANIFEST_NAME
    if not path.is_file():
        raise SetupError(f"no {MANIFEST_NAME} at {repo_root}")
    manifest = json.loads(path.read_text())
    if not isinstance(manifest.get("packages"), list) or not manifest["packages"]:
        raise SetupError(f"{MANIFEST_NAME} declares no packages")
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
    local_rel = contained_path("local_path", package.get("local_path"))
    upstream_rel = contained_path("upstream_path", package.get("upstream_path"))
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


def status_package(repo_root: Path, package: Dict[str, Any]) -> int:
    """Report whether the local and upstream package match the manifest.

    Args:
        repo_root: Repository root containing ``vendor.json``.
        package: Manifest entry to compare.

    Returns:
        Zero when the package is in step, one when it has drifted.
    """
    local_dir, upstream_dir = resolve_dirs(repo_root, package)
    recorded = package.get("files") or {}
    include, skip = package.get("include"), skip_rule(package)
    local_changes = diff_trees(recorded, hash_tree(local_dir, include, skip))
    upstream_changes = diff_trees(recorded, hash_tree(upstream_dir, include, skip))
    name = package["name"]
    if not recorded:
        print(f"{name}: never pulled; run pull to vendor it")
        return EXIT_DRIFT
    if not local_changes and not upstream_changes:
        current = upstream_commit(upstream_dir, include)
        if package.get("base_commit") != current:
            print(
                f"{name}: files in step, but the manifest pins {package.get('base_commit')} and "
                f"upstream's last commit is {current}"
            )
            return EXIT_DRIFT
        print(f"{name}: in step at {package.get('base_commit')}, {len(recorded)} files")
        return EXIT_OK
    if local_changes:
        print(f"{name}: local-ahead, {len(local_changes)} change(s)")
        for change in local_changes:
            print(f"  local {change}")
    if upstream_changes:
        print(f"{name}: upstream-ahead, {len(upstream_changes)} change(s)")
        for change in upstream_changes:
            print(f"  upstream {change}")
    return EXIT_DRIFT


def pull_package(repo_root: Path, package: Dict[str, Any]) -> int:
    """Copy upstream package files to the local tree and update the baseline.

    Args:
        repo_root: Repository root containing the local package copy.
        package: Manifest entry to pull.

    Returns:
        Zero when the pull completes, one when drift blocks it.

    Raises:
        SetupError: If paths or the upstream commit cannot be resolved.
    """
    local_dir, upstream_dir = resolve_dirs(repo_root, package)
    recorded = package.get("files") or {}
    include, skip = package.get("include"), skip_rule(package)
    local = hash_tree(local_dir, include, skip)
    upstream = hash_tree(upstream_dir, include, skip)
    # Local edits that upstream already carries are a finished push, not a
    # conflict, so they may be overwritten; anything else would be lost.
    if recorded and diff_trees(recorded, local) and diff_trees(upstream, local):
        print(f"{package['name']}: pull refused, the local copy has edits upstream does not carry; push them first")
        return EXIT_DRIFT
    if upstream_dirty(upstream_dir, include):
        print(f"{package['name']}: pull refused, upstream has uncommitted changes; commit them first")
        return EXIT_DRIFT
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
    print(f"{package['name']}: pulled {len(package['files'])} files at {package['base_commit']}")
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


COMMANDS = {"status": status_package, "pull": pull_package, "push": push_package}


# ───────────────────────────────────────────────────────────────
# 6. MAIN
# ───────────────────────────────────────────────────────────────

def main(argv: Optional[List[str]] = None) -> int:
    """Run one vendor-sync command for all or one selected package.

    Args:
        argv: Optional command-line arguments, excluding the executable name.

    Returns:
        The highest exit status returned by the selected package commands.
    """
    parser = argparse.ArgumentParser(description="Sync vendored skills with their upstream.")
    parser.add_argument("command", choices=sorted(COMMANDS))
    parser.add_argument("--package", default=None)
    parser.add_argument("--root", default=str(REPO_ROOT), help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    repo_root = Path(args.root)
    try:
        manifest = load_manifest(repo_root)
        worst = EXIT_OK
        for package in select_packages(manifest, args.package):
            worst = max(worst, COMMANDS[args.command](repo_root, package))
        return worst
    except SetupError as error:
        print(f"vendor-sync: {error}", file=sys.stderr)
        return EXIT_SETUP


if __name__ == "__main__":
    sys.exit(main())
