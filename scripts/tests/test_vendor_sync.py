#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: VENDOR SYNC TESTS
# ───────────────────────────────────────────────────────────────

"""Prove vendor-sync.py against a scratch upstream, never the real one.

Each test builds a throwaway git repository holding a `.skilled` skill folder
and a throwaway Product Owner root with its own `vendor.json`, then drives the
script as a subprocess, the way a gate or an operator runs it. Nothing here
reads or writes the shared skill repo.

Usage:
  python3 -m pytest -q scripts/tests
  python3 scripts/tests/test_vendor_sync.py

Output:
  Pytest prints a test summary. Direct execution prints each unittest result
  and a final summary. A failed test run exits nonzero.

Options:
  No project-specific options. Direct execution accepts standard unittest
  runner options.
"""

# ───────────────────────────────────────────────────────────────
# 1. IMPORTS
# ───────────────────────────────────────────────────────────────

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Dict

# ───────────────────────────────────────────────────────────────
# 2. FIXTURES
# ───────────────────────────────────────────────────────────────

SCRIPT = Path(__file__).resolve().parent.parent / "vendor-sync.py"
UPSTREAM_PATH = ".skilled/skills/mcp-tooling/sample-skill"


def git(cwd: Path, *args: str) -> str:
    """Run a Git command in a scratch repository.

    Args:
        cwd: Repository directory.
        *args: Arguments passed to Git after ``-C`` and the directory.

    Returns:
        Standard output from Git.
    """
    result = subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True, check=True)
    return result.stdout


class ScratchWorld:
    """A scratch upstream repository and a scratch vendoring repository side by side."""

    def __init__(self, base: Path) -> None:
        """Create isolated upstream and local repositories for one test.

        Args:
            base: Temporary parent directory for both repositories.
        """
        self.upstream_root = base / "upstream"
        self.skill_dir = self.upstream_root / UPSTREAM_PATH
        self.repo_root = base / "product-owner"
        self.skill_dir.mkdir(parents=True)
        (self.skill_dir / "SKILL.md").write_text("# Sample skill\n")
        (self.skill_dir / "references").mkdir()
        (self.skill_dir / "references" / "guide.md").write_text("guide line\n")
        git(self.upstream_root, "init", "-q")
        git(self.upstream_root, "-c", "user.name=t", "-c", "user.email=t@t", "add", "-A")
        git(self.upstream_root, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", "seed")
        self.repo_root.mkdir()
        manifest = {"packages": [{"name": "sample-skill", "local_path": "sample-skill",
                                  "upstream_path": UPSTREAM_PATH, "base_commit": None, "files": {}}]}
        (self.repo_root / "vendor.json").write_text(json.dumps(manifest))

    def run(
        self,
        command: str,
        upstream: bool = True,
    ) -> subprocess.CompletedProcess[str]:
        """Run vendor-sync against this scratch repository.

        Args:
            command: Vendor-sync command to run.
            upstream: Whether to expose the scratch upstream root.

        Returns:
            Completed subprocess result.
        """
        env = dict(os.environ)
        env.pop("VENDOR_UPSTREAM_ROOT", None)
        if upstream:
            env["VENDOR_UPSTREAM_ROOT"] = str(self.upstream_root)
        return subprocess.run([sys.executable, str(SCRIPT), command, "--root", str(self.repo_root)],
                              capture_output=True, text=True, env=env, cwd=str(self.repo_root))

    def commit_upstream(self, message: str) -> None:
        """Commit current changes in the scratch upstream repository.

        Args:
            message: Commit message for the scratch change.
        """
        git(self.upstream_root, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-am", message)

    def manifest(self) -> Dict[str, Any]:
        """Return the first package entry from the local vendor manifest.

        Returns:
            The scratch package manifest entry.
        """
        return json.loads((self.repo_root / "vendor.json").read_text())["packages"][0]


# ───────────────────────────────────────────────────────────────
# 3. TESTS
# ───────────────────────────────────────────────────────────────

class VendorSyncTests(unittest.TestCase):
    """Verify vendor-sync behavior against isolated repositories."""

    def setUp(self) -> None:
        """Create a temporary scratch world for one test."""
        self._tmp = tempfile.TemporaryDirectory()
        self.world = ScratchWorld(Path(self._tmp.name))

    def tearDown(self) -> None:
        """Remove the temporary scratch world after one test."""
        self._tmp.cleanup()

    def test_pull_then_status_is_in_step(self) -> None:
        """A pull records a baseline that status accepts."""
        self.assertEqual(self.world.run("pull").returncode, 0)
        status = self.world.run("status")
        self.assertEqual(status.returncode, 0, status.stdout)
        self.assertIn("in step", status.stdout)
        self.assertEqual(
            self.world.manifest()["base_commit"], git(self.world.upstream_root, "rev-parse", "HEAD").strip()
        )

    def test_one_byte_local_edit_is_local_ahead_and_blocks_pull(self) -> None:
        """A local edit is reported and preserved when pull is refused."""
        self.world.run("pull")
        edited = self.world.repo_root / "sample-skill" / "SKILL.md"
        edited.write_text(edited.read_text() + "x")
        status = self.world.run("status")
        self.assertEqual(status.returncode, 1)
        self.assertIn("local-ahead", status.stdout)
        pull = self.world.run("pull")
        self.assertEqual(pull.returncode, 1)
        self.assertIn("refused", pull.stdout)
        self.assertTrue(edited.read_text().endswith("x"), "a refused pull must leave the local edit in place")

    def test_planted_symlink_is_refused(self) -> None:
        """A symlink in the local tree is reported as a setup error."""
        self.world.run("pull")
        (self.world.repo_root / "sample-skill" / "link.md").symlink_to("SKILL.md")
        status = self.world.run("status")
        self.assertEqual(status.returncode, 2)
        self.assertIn("symlink refused", status.stderr)

    def test_push_writes_a_diff_upstream(self) -> None:
        """Push copies a local content change into the upstream tree."""
        self.world.run("pull")
        guide = self.world.repo_root / "sample-skill" / "references" / "guide.md"
        guide.write_text("guide line\nimproved line\n")
        push = self.world.run("push")
        self.assertEqual(push.returncode, 0, push.stdout)
        stat = git(self.world.upstream_root, "diff", "--stat")
        self.assertIn("guide.md", stat)

    def test_push_refused_when_upstream_moved(self) -> None:
        """Push refuses to overwrite a changed upstream tree."""
        self.world.run("pull")
        (self.world.skill_dir / "SKILL.md").write_text("# Sample skill\nupstream edit\n")
        (self.world.repo_root / "sample-skill" / "SKILL.md").write_text("# Sample skill\nlocal edit\n")
        push = self.world.run("push")
        self.assertEqual(push.returncode, 1)
        self.assertIn("upstream moved", push.stdout)

    def test_pull_refused_while_upstream_is_uncommitted(self) -> None:
        """Pull refuses upstream bytes that do not belong to a commit."""
        (self.world.skill_dir / "SKILL.md").write_text("# Sample skill\nnot committed\n")
        pull = self.world.run("pull")
        self.assertEqual(pull.returncode, 1)
        self.assertIn("uncommitted", pull.stdout)
        self.assertFalse((self.world.repo_root / "sample-skill").exists(), "a refused pull must vendor nothing")

    def test_status_reports_a_mispinned_base_commit(self) -> None:
        """Status reports when the manifest baseline commit is incorrect."""
        self.world.run("pull")
        manifest_path = self.world.repo_root / "vendor.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["packages"][0]["base_commit"] = "0" * 40
        manifest_path.write_text(json.dumps(manifest))
        status = self.world.run("status")
        self.assertEqual(status.returncode, 1)
        self.assertIn("pins " + "0" * 40, status.stdout)

    def test_pull_after_committed_push_rebaselines(self) -> None:
        """Pull records the commit that includes a previously pushed change."""
        self.world.run("pull")
        (self.world.repo_root / "sample-skill" / "SKILL.md").write_text("# Sample skill\nv2\n")
        self.world.run("push")
        self.world.commit_upstream("take the vendored change")
        self.assertEqual(self.world.run("pull").returncode, 0)
        status = self.world.run("status")
        self.assertEqual(status.returncode, 0, status.stdout)
        self.assertEqual(
            self.world.manifest()["base_commit"], git(self.world.upstream_root, "rev-parse", "HEAD").strip()
        )

    def test_include_vendors_one_file_and_push_spares_its_siblings(self) -> None:
        """An include list limits copied files and preserves upstream siblings."""
        manifest = json.loads((self.world.repo_root / "vendor.json").read_text())
        manifest["packages"][0]["include"] = ["references/guide.md"]
        (self.world.repo_root / "vendor.json").write_text(json.dumps(manifest))
        self.assertEqual(self.world.run("pull").returncode, 0)
        local = self.world.repo_root / "sample-skill"
        self.assertEqual(sorted(p.relative_to(local).as_posix() for p in local.rglob("*") if p.is_file()),
                         ["references/guide.md"])
        self.assertEqual(self.world.run("status").returncode, 0)
        (local / "references" / "guide.md").write_text("guide line\nimproved\n")
        self.assertEqual(self.world.run("push").returncode, 0)
        self.assertTrue(
            (self.world.skill_dir / "SKILL.md").is_file(), "a push must not remove an unlisted upstream file"
        )
        self.assertIn("guide.md", git(self.world.upstream_root, "diff", "--stat"))

    def test_exclude_keeps_build_output_out_and_carries_a_local_build_across_a_pull(self) -> None:
        """Excluded build output stays local and survives an upstream pull."""
        (self.world.skill_dir / ".gitignore").write_text("node_modules/\n")
        git(self.world.upstream_root, "-c", "user.name=t", "-c", "user.email=t@t", "add", "-A")
        self.world.commit_upstream("ignore build output")
        (self.world.skill_dir / "node_modules").mkdir()
        (self.world.skill_dir / "node_modules" / "dep.js").write_text("upstream dependency\n")
        self.set_package(exclude=["node_modules", "dist"])
        self.assertEqual(self.world.run("pull").returncode, 0)
        local = self.world.repo_root / "sample-skill"
        self.assertFalse((local / "node_modules").exists(), "an excluded folder must not be copied")
        self.assertNotIn("node_modules/dep.js", self.world.manifest()["files"])
        (local / "dist").mkdir()
        (local / "dist" / "index.js").write_text("local build\n")
        self.assertEqual(self.world.run("status").returncode, 0, "build output must not read as a local edit")
        (self.world.skill_dir / "references" / "guide.md").write_text("guide line\nupstream fix\n")
        self.world.commit_upstream("upstream fix")
        result = self.world.run("pull")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual((local / "references" / "guide.md").read_text(), "guide line\nupstream fix\n")
        self.assertEqual(
            (local / "dist" / "index.js").read_text(), "local build\n", "a local build must survive a pull"
        )

    def test_exclude_path_skips_one_link_and_keeps_its_namesake(self) -> None:
        """An exact excluded path skips one symlink without skipping its name elsewhere."""
        (self.world.skill_dir / "server").mkdir()
        (self.world.skill_dir / "server" / "README.md").symlink_to("../SKILL.md")
        git(self.world.upstream_root, "-c", "user.name=t", "-c", "user.email=t@t", "add", "-A")
        self.world.commit_upstream("link a readme")
        self.assertEqual(self.world.run("pull").returncode, 2, "an unexcluded link must still be refused")
        self.set_package(exclude=["server/README.md"])
        result = self.world.run("pull")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        local = self.world.repo_root / "sample-skill"
        self.assertTrue((local / "SKILL.md").is_file())
        self.assertFalse((local / "server" / "README.md").exists())
        self.assertEqual(self.world.run("status").returncode, 0)

    def test_escaping_exclude_entry_is_refused(self) -> None:
        """An exclude path that escapes its root is a setup error."""
        self.set_package(exclude=["../elsewhere"])
        result = self.world.run("status")
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertIn("exclude entry", result.stderr)

    def set_package(self, **fields: object) -> None:
        """Apply package fields to the scratch vendor manifest.

        Args:
            **fields: Manifest fields to update on the package entry.
        """
        manifest = json.loads((self.world.repo_root / "vendor.json").read_text())
        manifest["packages"][0].update(fields)
        (self.world.repo_root / "vendor.json").write_text(json.dumps(manifest))

    def plant_outside(self) -> Path:
        """Create a sibling directory used to test path escape guards.

        Returns:
            The outside directory containing a sentinel file.
        """
        outside = self.world.repo_root.parent / "outside"
        outside.mkdir()
        (outside / "keep.md").write_text("must survive\n")
        return outside

    def assert_escape_refused(self, outside: Path) -> None:
        """Verify commands reject a path escape and preserve outside content.

        Args:
            outside: Directory that must remain untouched by rejected commands.
        """
        for command in ("pull", "push", "status"):
            result = self.world.run(command)
            self.assertEqual(result.returncode, 2, f"{command}: {result.stdout}{result.stderr}")
            self.assertIn("vendor.json", result.stderr)
        self.assertEqual(sorted(p.name for p in outside.iterdir()), ["keep.md"])
        self.assertEqual((outside / "keep.md").read_text(), "must survive\n")

    def test_parent_traversal_local_path_is_refused(self) -> None:
        """A local path with parent traversal is rejected."""
        outside = self.plant_outside()
        self.set_package(local_path="../outside")
        self.assert_escape_refused(outside)

    def test_absolute_local_path_is_refused(self) -> None:
        """An absolute local path is rejected."""
        outside = self.plant_outside()
        self.set_package(local_path=str(outside))
        self.assert_escape_refused(outside)

    def test_local_path_through_an_outward_link_is_refused(self) -> None:
        """A local path that resolves through an outward link is rejected."""
        outside = self.plant_outside()
        (self.world.repo_root / "linked").symlink_to(outside)
        self.set_package(local_path="linked")
        self.assert_escape_refused(outside)

    def test_escaping_include_entry_is_refused(self) -> None:
        """An include path that escapes its root is rejected."""
        outside = self.plant_outside()
        self.set_package(include=["../../outside/keep.md"])
        self.assert_escape_refused(outside)

    def test_escaping_upstream_path_is_refused(self) -> None:
        """An upstream path with parent traversal is rejected."""
        outside = self.plant_outside()
        self.set_package(upstream_path="../outside")
        self.assert_escape_refused(outside)

    def test_missing_upstream_is_a_setup_error_not_a_pass(self) -> None:
        """Missing shared upstream configuration returns a setup error."""
        result = self.world.run("status", upstream=False)
        self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
