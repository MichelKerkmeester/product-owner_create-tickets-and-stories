#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: CLAUDE CODE PLUGIN BUILD
# ───────────────────────────────────────────────────────────────

"""Build the Claude Code plugin's skills folder from the tracked sources.

The plugin under `claude-plugin/` tracks only its manifests. Its
`skills/` folder is rebuilt on every run, so exactly one tracked copy of each
skill file exists in this repository, and a hand edit inside `skills/` is
thrown away by the next build rather than drifting from its source.

The build follows the Media Editor plugin's refusals. The hub is this
repository's root, so the build copies only the skill out of it: the hub files,
`AGENTS.md` and the packets `mode-registry.json` registers, `sk-product-owner/`,
`sk-create-figjam/` and the vendored `mcp-figma/` and `mcp-click-up/`. They land
in `skills/product-owner/` with their relative layout kept, so every path
`AGENTS.md` and the hub write still resolves there. The repository's own
entries, such as the specs, the exports and the Claude Project package, never
ship. It then hashes every shipped file against its source and refuses:

- a source or copy that holds a symlink, which a clone or an install would
  carry as a pointer to nothing, `AGENTS.md` and the hub files included
- a plugin folder, `.claude-plugin/` or `skills/` that is a symlink or whose
  `skills/` resolves outside this repository, because the build deletes
  `skills/` before it copies
- a `vendor.json` path that escapes its root
- a vendored package whose files differ from the hashes `vendor.json` records,
  so a fork of the shared skill never ships as if it were the shared skill
- a copy whose bytes differ from the source
- a `plugin.json` that registers an MCP server, and a `bin/` folder, because
  the plugin ships skills only

Two runs over the same sources produce the same hash tree.

Usage:
  python3 scripts/build-plugin.py
  python3 scripts/build-plugin.py --check
  python3 scripts/build-plugin.py --self-test

Output:
  The default run prints BUILT with the copied file count and tree digest.
  --check prints FRESH or STALE with the current tree state.
  --self-test prints PASS or FAIL for each scratch-tree scenario.

Options:
  --check      Check generated plugin files without rewriting them.
  --self-test  Verify refusal cases against a temporary repository copy.
"""

# ───────────────────────────────────────────────────────────────
# 1. IMPORTS
# ───────────────────────────────────────────────────────────────

import hashlib
import importlib.util
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path
from types import ModuleType

# ───────────────────────────────────────────────────────────────
# 2. CONFIGURATION
# ───────────────────────────────────────────────────────────────

ROOT = Path(os.environ.get("PO_ROOT") or Path(__file__).resolve().parent.parent)
PLUGIN = Path("claude-plugin")
SKILL_NAME = "product-owner"
HUB_FILES = (
    "SKILL.md",
    "ROUTER.md",
    "mode-registry.json",
    "hub-router.json",
    "description.json",
    "graph-metadata.json",
    "leaf-manifest.json",
    "AGENTS.md",
)
# The playbooks, the changelogs and the hub benchmark cite repository paths and
# release history a plugin install does not carry, so they stay out of the
# shipped skill. A vendored packet ships whole, because its files are hashed.
UNSHIPPED = {
    Path("sk-product-owner/manual-testing-playbook"),
    Path("sk-product-owner/changelog"),
    Path("sk-create-figjam/manual-testing-playbook"),
    Path("sk-create-figjam/changelog"),
}
IGNORED_NAMES = {".DS_Store", "__pycache__"}


class BuildRefused(Exception):
    """A condition the plugin must never ship with."""


# ───────────────────────────────────────────────────────────────
# 3. SOURCE AND VALIDATION HELPERS
# ───────────────────────────────────────────────────────────────

def load_vendor_sync() -> ModuleType:
    """Load vendor-sync helpers used to validate vendored package contents.

    Returns:
        The loaded vendor-sync module.
    """
    spec = importlib.util.spec_from_file_location(
        "vendor_sync",
        Path(__file__).resolve().parent / "vendor-sync.py",
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha(path: Path) -> str:
    """Return the SHA-256 digest of a file's bytes.

    Args:
        path: File to hash.

    Returns:
        Lowercase hexadecimal SHA-256 digest.
    """
    return hashlib.sha256(path.read_bytes()).hexdigest()


def registered_packets(root: Path) -> list[str]:
    """Read the packet paths registered by the root mode registry.

    Args:
        root: Repository root containing ``mode-registry.json``.

    Returns:
        Sorted packet paths.
    """
    registry = json.loads((root / "mode-registry.json").read_text())
    return sorted(str(mode["packet"]) for mode in registry["modes"])


def shipped_sources(root: Path) -> dict[str, Path]:
    """Map plugin skill paths to the source files that populate them.

    Args:
        root: Repository root containing the hub and registered packets.

    Returns:
        Mapping from destination paths to source files.
    """
    sources = {}
    for name in HUB_FILES:
        if (root / name).is_symlink():
            raise BuildRefused(f"symlink in the source: {name}")
        sources[f"{SKILL_NAME}/{name}"] = root / name
    for packet in registered_packets(root):
        if (root / packet).is_symlink():
            raise BuildRefused(f"symlink in the source: {packet}")
        for dirpath, dirnames, filenames in os.walk(root / packet, followlinks=False):
            rel_dir = Path(dirpath).relative_to(root)
            for name in dirnames + filenames:
                if (Path(dirpath) / name).is_symlink():
                    raise BuildRefused(f"symlink in the source: {rel_dir / name}")
            dirnames[:] = sorted(d for d in dirnames if d not in IGNORED_NAMES and rel_dir / d not in UNSHIPPED)
            for name in sorted(filenames):
                if name not in IGNORED_NAMES:
                    sources[f"{SKILL_NAME}/{(rel_dir / name).as_posix()}"] = Path(dirpath) / name
    return sources


def check_vendored(root: Path) -> None:
    """Refuse a build when a vendored package differs from its manifest.

    Args:
        root: Repository root containing ``vendor.json``.

    Raises:
        BuildRefused: If a package path or file tree is invalid or has drifted.
    """
    vendor_sync = load_vendor_sync()
    manifest = json.loads((root / "vendor.json").read_text())
    for package in manifest["packages"]:
        try:
            local = vendor_sync.contained_path("local_path", package.get("local_path"))
            for rel in package.get("include") or []:
                vendor_sync.contained_path("include entry", rel)
            for rel in package.get("exclude") or []:
                vendor_sync.contained_path("exclude entry", rel)
            # hash_tree refuses a symlink with SetupError, which must refuse the build too.
            # The exclude rule keeps local build output, such as node_modules, from reading as drift.
            actual = vendor_sync.hash_tree(root / local, package.get("include"), vendor_sync.skip_rule(package))
        except vendor_sync.SetupError as error:
            raise BuildRefused(str(error)) from None
        drift = vendor_sync.diff_trees(package.get("files") or {}, actual)
        if drift:
            raise BuildRefused(f"vendored {package['name']} differs from vendor.json: {', '.join(drift)}")


def tree_hashes(folder: Path) -> dict[str, str]:
    """Hash every regular file beneath a generated tree.

    Args:
        folder: Root of the generated tree.

    Returns:
        Mapping from relative file paths to SHA-256 digests.

    Raises:
        BuildRefused: If the tree contains a symlink.
    """
    hashes = {}
    for dirpath, _, filenames in os.walk(folder, followlinks=False):
        for name in filenames:
            path = Path(dirpath) / name
            if path.is_symlink():
                raise BuildRefused(f"symlink in the copy: {path.relative_to(folder)}")
            hashes[path.relative_to(folder).as_posix()] = sha(path)
    return dict(sorted(hashes.items()))


def check_output_path(root: Path) -> None:
    """Ensure the generated skills folder cannot resolve outside the repository.

    Args:
        root: Repository root containing ``claude-plugin/``.

    Raises:
        BuildRefused: If the output path contains a symlink or escapes the root.
    """
    # The build deletes `skills/` before it copies, so neither the plugin folder
    # nor anything inside it on the way may be a link, and the folder it deletes
    # must resolve inside this repository.
    plugin = root / PLUGIN
    for path in (plugin, plugin / ".claude-plugin", plugin / "skills"):
        if path.is_symlink():
            raise BuildRefused(
                f"symlink in the plugin output path: {path.relative_to(root)}"
            )
    try:
        (plugin / "skills").resolve().relative_to(root.resolve())
    except ValueError:
        raise BuildRefused(f"{PLUGIN}/skills resolves outside the repository") from None


# ───────────────────────────────────────────────────────────────
# 4. BUILD
# ───────────────────────────────────────────────────────────────

def build(root: Path) -> dict[str, str]:
    """Rebuild and verify the generated plugin skills tree.

    Args:
        root: Repository root containing plugin inputs and output.

    Returns:
        Mapping from generated file paths to SHA-256 digests.

    Raises:
        BuildRefused: If source validation fails or the copy differs.
    """
    check_output_path(root)
    plugin = root / PLUGIN
    manifest = json.loads((plugin / ".claude-plugin" / "plugin.json").read_text())
    if "mcpServers" in manifest:
        raise BuildRefused("plugin.json registers an MCP server")
    if (plugin / "bin").exists():
        raise BuildRefused("claude-plugin/bin/ exists, and the plugin ships skills only")
    check_vendored(root)
    sources = shipped_sources(root)
    skills = plugin / "skills"
    if skills.exists():
        shutil.rmtree(skills)
    for rel, source in sources.items():
        destination = skills / rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    expected = {rel: sha(source) for rel, source in sorted(sources.items())}
    actual = tree_hashes(skills)
    differing = sorted(rel for rel in set(expected) | set(actual) if expected.get(rel) != actual.get(rel))
    if differing:
        raise BuildRefused(f"the copy differs from its source: {', '.join(differing)}")
    return actual


# ───────────────────────────────────────────────────────────────
# 5. STATUS AND OUTPUT
# ───────────────────────────────────────────────────────────────

def check_freshness(root: Path) -> int:
    """Compare generated plugin files with their sources without rewriting them.

    Args:
        root: Repository root containing the plugin sources and output.

    Returns:
        Zero when the generated tree is fresh, otherwise one.
    """
    try:
        check_output_path(root)
        manifest = json.loads((root / PLUGIN / ".claude-plugin" / "plugin.json").read_text())
        if "mcpServers" in manifest:
            raise BuildRefused("plugin.json registers an MCP server")
        if (root / PLUGIN / "bin").exists():
            raise BuildRefused("claude-plugin/bin/ exists, and the plugin ships skills only")
        check_vendored(root)
        sources = shipped_sources(root)
        expected = {rel: sha(source) for rel, source in sorted(sources.items())}
        skills = root / PLUGIN / "skills"
        if not skills.is_dir():
            raise BuildRefused("claude-plugin/skills/ is missing")
        actual = tree_hashes(skills)
        differing = sorted(rel for rel in set(expected) | set(actual) if expected.get(rel) != actual.get(rel))
        if differing:
            raise BuildRefused(f"the generated copy differs from its sources: {', '.join(differing)}")
    except BuildRefused as error:
        print(f"STALE {error}")
        return 1
    except (OSError, json.JSONDecodeError) as error:
        print(f"STALE {error}")
        return 1
    digest = hashlib.sha256(json.dumps(actual, sort_keys=True).encode()).hexdigest()
    print(f"FRESH {PLUGIN}/skills/{SKILL_NAME}: {len(actual)} files, tree {digest[:16]}")
    return 0


def run(root: Path) -> int:
    """Build the plugin tree and report the result.

    Args:
        root: Repository root containing the plugin sources and output.

    Returns:
        Zero when the build succeeds, otherwise one.
    """
    try:
        hashes = build(root)
    except BuildRefused as error:
        print(f"REFUSED {error}")
        return 1
    digest = hashlib.sha256(json.dumps(hashes, sort_keys=True).encode()).hexdigest()
    print(f"BUILT {PLUGIN}/skills/{SKILL_NAME}: {len(hashes)} files, AGENTS.md included, tree {digest[:16]}")
    return 0


# ───────────────────────────────────────────────────────────────
# 6. SELF TEST
# ───────────────────────────────────────────────────────────────

def self_test() -> int:
    """Exercise build refusal cases in a temporary repository copy.

    Returns:
        Zero when every scratch-tree scenario passes, otherwise one.
    """
    results = []
    with tempfile.TemporaryDirectory(prefix="po-plugin-selftest-") as scratch:
        tree = Path(scratch) / "po"
        tree.mkdir()
        for name in (*HUB_FILES, "vendor.json"):
            shutil.copy2(ROOT / name, tree / name)
        for folder in (*registered_packets(ROOT), str(PLUGIN / ".claude-plugin")):
            shutil.copytree(ROOT / folder, tree / folder, ignore=shutil.ignore_patterns("skills", *IGNORED_NAMES))
        # A vendored package outside the registered packets is still checked,
        # so the scratch tree carries its recorded files too.
        for package in json.loads((ROOT / "vendor.json").read_text())["packages"]:
            for rel in package.get("files") or {}:
                target = tree / package["local_path"] / rel
                if not target.exists():
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(ROOT / package["local_path"] / rel, target)
        (tree / "specs").mkdir()
        (tree / "specs" / "repo-only.md").write_text("never shipped\n")
        first, second = build(tree), build(tree)
        results.append(("two builds produce identical hash trees", first == second and len(first) > 0))
        results.append(("a repository folder beside the hub never ships",
                        not any(rel.startswith(f"{SKILL_NAME}/specs/") for rel in first)))

        planted = tree / "mcp-figma" / "SKILL.md"
        clean = planted.read_bytes()
        planted.write_bytes(clean + b"x")
        results.append(("a planted divergence in the vendored packet refuses", run(tree) == 1))
        planted.write_bytes(clean)

        link = tree / "sk-product-owner" / "references" / "planted-link.md"
        link.symlink_to("hvr-core.md")
        results.append(("a planted symlink refuses", run(tree) == 1))
        link.unlink()

        vendored_link = tree / "mcp-figma" / "planted-link.md"
        vendored_link.symlink_to("SKILL.md")
        results.append(("a planted symlink in a vendored packet refuses", run(tree) == 1))
        vendored_link.unlink()

        hub = tree / "SKILL.md"
        hub_bytes = hub.read_bytes()
        hub.unlink()
        (Path(scratch) / "outside-skill.md").write_bytes(hub_bytes)
        hub.symlink_to(Path(scratch) / "outside-skill.md")
        results.append(("a planted symlink on a hub file refuses", run(tree) == 1))
        hub.unlink()
        hub.write_bytes(hub_bytes)

        # A plugin folder linked out of the repository would have the build
        # delete the `skills/` folder of whatever it points at.
        outside = Path(scratch) / "outside-plugin"
        shutil.copytree(tree / PLUGIN, outside)
        (outside / "skills" / "keep.md").parent.mkdir(parents=True, exist_ok=True)
        (outside / "skills" / "keep.md").write_text("must survive\n")
        moved = Path(scratch) / "plugin-aside"
        (tree / PLUGIN).rename(moved)
        (tree / PLUGIN).symlink_to(outside)
        results.append(("a symlinked plugin folder refuses and leaves its target alone",
                        run(tree) == 1 and (outside / "skills" / "keep.md").is_file()))
        (tree / PLUGIN).unlink()
        moved.rename(tree / PLUGIN)

        build_output = tree / "mcp-code-mode" / "mcp-server" / "node_modules" / "dep" / "index.js"
        build_output.parent.mkdir(parents=True)
        build_output.write_text("installed by npm ci\n")
        results.append(
            ("excluded build output in a vendored packet does not refuse", run(tree) == 0)
        )
        shutil.rmtree(tree / "mcp-code-mode" / "mcp-server" / "node_modules")

        (tree / PLUGIN / "bin").mkdir()
        results.append(("a bin/ folder refuses", run(tree) == 1))
        (tree / PLUGIN / "bin").rmdir()
        results.append(("the restored tree builds", run(tree) == 0))
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
    return 0 if all(ok for _, ok in results) else 1


# ───────────────────────────────────────────────────────────────
# 7. CLI ENTRYPOINT
# ───────────────────────────────────────────────────────────────

def main() -> int:
    """Dispatch the selected build-plugin operation.

    Returns:
        Process exit status.
    """
    if sys.argv[1:] == ["--self-test"]:
        return self_test()
    if sys.argv[1:] == ["--check"]:
        return check_freshness(ROOT)
    return run(ROOT)


if __name__ == "__main__":
    sys.exit(main())
