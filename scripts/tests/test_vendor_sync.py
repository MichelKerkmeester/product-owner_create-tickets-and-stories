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
from typing import Any, Dict, Optional

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
        *flags: str,
        upstream: bool = True,
        override: Optional[Path] = None,
    ) -> subprocess.CompletedProcess[str]:
        """Run vendor-sync against this scratch repository.

        Args:
            command: Vendor-sync command to run.
            *flags: Extra command-line flags for the command.
            upstream: Whether to expose the scratch upstream root.
            override: Another path to expose as the upstream root.

        Returns:
            Completed subprocess result.
        """
        env = dict(os.environ)
        env.pop("VENDOR_UPSTREAM_ROOT", None)
        if override is not None:
            env["VENDOR_UPSTREAM_ROOT"] = str(override)
        elif upstream:
            env["VENDOR_UPSTREAM_ROOT"] = str(self.upstream_root)
        return subprocess.run([sys.executable, str(SCRIPT), command, *flags, "--root", str(self.repo_root)],
                              capture_output=True, text=True, env=env, cwd=str(self.repo_root))

    def add_package(self, name: str) -> Path:
        """Add a second skill to the scratch upstream and to the manifest.

        Args:
            name: Folder and manifest name of the new skill.

        Returns:
            The new skill folder inside the scratch upstream.
        """
        upstream_path = f".skilled/skills/mcp-tooling/{name}"
        skill_dir = self.upstream_root / upstream_path
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(f"# {name}\n")
        git(self.upstream_root, "-c", "user.name=t", "-c", "user.email=t@t", "add", "-A")
        self.commit_upstream(f"add {name}")
        path = self.repo_root / "vendor.json"
        manifest = json.loads(path.read_text())
        manifest["packages"].append({"name": name, "local_path": name, "upstream_path": upstream_path,
                                     "base_commit": None, "files": {}})
        path.write_text(json.dumps(manifest))
        return skill_dir

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

    def entry(self, name: str) -> Dict[str, Any]:
        """Return one package entry of the scratch manifest by name.

        Args:
            name: Package name to look up.

        Returns:
            The manifest entry as it is on disk now.
        """
        packages = json.loads((self.world.repo_root / "vendor.json").read_text())["packages"]
        return next(p for p in packages if p["name"] == name)

    def test_sync_pulls_the_entry_that_is_behind_and_leaves_the_one_in_step(self) -> None:
        """Sync pulls only the entry upstream moved and lists the commits that moved it."""
        self.world.add_package("other-skill")
        self.world.run("pull")
        other_before = self.entry("other-skill")
        other_file = self.world.repo_root / "other-skill" / "SKILL.md"
        other_inode = other_file.stat().st_ino
        (self.world.skill_dir / "references" / "guide.md").write_text("guide line\nupstream fix\n")
        self.world.commit_upstream("fix the guide")
        result = self.world.run("sync")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("other-skill: in step", result.stdout)
        self.assertIn("sample-skill: pulled, 1 file(s) changed", result.stdout)
        self.assertIn("fix the guide", result.stdout, "a pulled entry must list the commits that moved it")
        head = git(self.world.upstream_root, "rev-parse", "HEAD").strip()
        self.assertEqual(self.entry("sample-skill")["base_commit"], head)
        self.assertEqual(
            (self.world.repo_root / "sample-skill" / "references" / "guide.md").read_text(),
            "guide line\nupstream fix\n",
        )
        self.assertEqual(self.entry("other-skill"), other_before, "an entry in step keeps its record")
        self.assertEqual(other_file.stat().st_ino, other_inode, "an entry in step must not be copied again")

    def test_sync_rebaselines_a_fix_pushed_and_committed_upstream(self) -> None:
        """Sync takes the commit of a pushed fix as the new base instead of refusing the local edit."""
        self.world.run("pull")
        (self.world.repo_root / "sample-skill" / "SKILL.md").write_text("# Sample skill\nfixed here\n")
        self.assertEqual(self.world.run("push").returncode, 0)
        self.world.commit_upstream("take the fix made here")
        result = self.world.run("sync")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("sample-skill: pulled, 1 file(s) changed", result.stdout)
        self.assertEqual(self.world.run("status").returncode, 0)

    def test_sync_with_every_entry_in_step_writes_nothing(self) -> None:
        """Sync leaves vendor.json and the local copy untouched when nothing moved."""
        self.world.run("pull")
        manifest_path = self.world.repo_root / "vendor.json"
        # Compact JSON differs from the indented form a save writes, so any rewrite shows.
        manifest_path.write_text(json.dumps(json.loads(manifest_path.read_text())))
        before = manifest_path.read_bytes()
        skill = self.world.repo_root / "sample-skill" / "SKILL.md"
        inode = skill.stat().st_ino
        result = self.world.run("sync")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("in step", result.stdout)
        self.assertNotIn("out of step", result.stdout)
        self.assertEqual(manifest_path.read_bytes(), before, "an in-step sync must not rewrite vendor.json")
        self.assertEqual(skill.stat().st_ino, inode, "an in-step sync must not copy the package again")

    def test_sync_refuses_local_edits_even_when_upstream_moved(self) -> None:
        """Sync keeps a local edit upstream does not carry and exits 1 with the reason."""
        self.world.run("pull")
        recorded = self.entry("sample-skill")
        edited = self.world.repo_root / "sample-skill" / "SKILL.md"
        edited.write_text(edited.read_text() + "local edit\n")
        (self.world.skill_dir / "references" / "guide.md").write_text("guide line\nupstream fix\n")
        self.world.commit_upstream("fix the guide")
        result = self.world.run("sync")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("sample-skill: refused, the local copy has edits upstream does not carry", result.stdout)
        self.assertIn("1 of 1 entries out of step: sample-skill", result.stdout)
        self.assertTrue(edited.read_text().endswith("local edit\n"), "a refused sync must keep the local edit")
        self.assertEqual(self.entry("sample-skill"), recorded, "a refused sync must not move the record")

    def test_sync_refuses_a_never_pulled_entry_whose_folder_already_holds_other_files(self) -> None:
        """Sync keeps files in the folder of an entry with no recorded hashes to compare them with."""
        local = self.world.repo_root / "sample-skill" / "SKILL.md"
        local.parent.mkdir()
        local.write_text("# written here before any pull\n")
        recorded = self.entry("sample-skill")
        result = self.world.run("sync")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("sample-skill: refused, never pulled and its folder holds files", result.stdout)
        self.assertEqual(local.read_text(), "# written here before any pull\n", "a refused sync must keep the file")
        self.assertEqual(self.entry("sample-skill"), recorded, "a refused sync must not move the record")

    def test_sync_vendors_a_never_pulled_entry_with_no_local_folder(self) -> None:
        """Sync pulls an entry that was never pulled when nothing local could be lost."""
        result = self.world.run("sync")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("sample-skill: pulled, 2 file(s) changed", result.stdout)
        self.assertTrue((self.world.repo_root / "sample-skill" / "references" / "guide.md").is_file())

    def test_sync_prints_the_rebuild_commands_only_when_a_dependency_file_changed(self) -> None:
        """A pulled entry that keeps build output out names the rebuild for a changed dependency file."""
        (self.world.skill_dir / "mcp-server").mkdir()
        (self.world.skill_dir / "mcp-server" / "package.json").write_text('{"v": 1}\n')
        git(self.world.upstream_root, "-c", "user.name=t", "-c", "user.email=t@t", "add", "-A")
        self.world.commit_upstream("add a server")
        self.set_package(exclude=["node_modules", "dist"])
        self.world.run("pull")
        (self.world.skill_dir / "mcp-server" / "package.json").write_text('{"v": 2}\n')
        self.world.commit_upstream("raise the dependency")
        hinted = self.world.run("sync")
        self.assertIn(
            "rebuild: cd sample-skill/mcp-server && nvm exec 24 npm ci && nvm exec 24 npm run build", hinted.stdout
        )
        (self.world.skill_dir / "references" / "guide.md").write_text("guide line\nonly prose\n")
        self.world.commit_upstream("fix the guide")
        quiet = self.world.run("sync")
        self.assertEqual(quiet.returncode, 0, quiet.stdout + quiet.stderr)
        self.assertNotIn("rebuild", quiet.stdout, "a pull with no dependency change needs no rebuild")

    def test_status_local_passes_with_no_upstream_and_fails_on_a_local_edit(self) -> None:
        """Local status checks the copy against vendor.json alone and still catches an edit."""
        self.world.run("pull")
        clean = self.world.run("status", "--local", upstream=False)
        self.assertEqual(clean.returncode, 0, clean.stdout + clean.stderr)
        self.assertIn("local copy matches vendor.json", clean.stdout)
        guide = self.world.repo_root / "sample-skill" / "references" / "guide.md"
        guide.write_text("guide line\nedited\n")
        edited = self.world.run("status", "--local", upstream=False)
        self.assertEqual(edited.returncode, 1, edited.stdout + edited.stderr)
        self.assertIn("changed references/guide.md", edited.stdout)
        self.assertIn("1 of 1 entries out of step: sample-skill", edited.stdout)

    def test_local_flag_is_refused_outside_status(self) -> None:
        """The local flag cannot ride along with a command that writes."""
        result = self.world.run("pull", "--local")
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertIn("--local is valid only with status", result.stderr)
        self.assertFalse((self.world.repo_root / "sample-skill").exists(), "a refused flag must pull nothing")

    def test_diff_shows_the_changed_line_and_exits_one(self) -> None:
        """Diff prints upstream's added line under the local and upstream file headers."""
        self.world.run("pull")
        (self.world.skill_dir / "references" / "guide.md").write_text("guide line\nimproved line\n")
        result = self.world.run("diff")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("--- local/references/guide.md", result.stdout)
        self.assertIn("+++ upstream/references/guide.md", result.stdout)
        self.assertIn("+improved line", result.stdout)
        self.assertEqual(
            (self.world.repo_root / "sample-skill" / "references" / "guide.md").read_text(),
            "guide line\n",
            "diff is read-only",
        )

    def test_diff_exits_zero_when_in_step(self) -> None:
        """Diff reports nothing to show for a copy that equals upstream."""
        self.world.run("pull")
        result = self.world.run("diff")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("sample-skill: no differences", result.stdout)
        self.assertNotIn("---", result.stdout)

    def test_diff_notes_a_binary_file_and_a_file_on_one_side(self) -> None:
        """Diff names a binary, a local-only and an upstream-only file in one line each."""
        (self.world.skill_dir / "data.bin").write_bytes(b"\x00\x01\x02")
        git(self.world.upstream_root, "-c", "user.name=t", "-c", "user.email=t@t", "add", "-A")
        self.world.commit_upstream("add a binary")
        self.world.run("pull")
        local = self.world.repo_root / "sample-skill"
        (local / "data.bin").write_bytes(b"\x00\x01\x03")
        (local / "mine.md").write_text("local only\n")
        (self.world.skill_dir / "theirs.md").write_text("upstream only\n")
        result = self.world.run("diff")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("binary file differs data.bin", result.stdout)
        self.assertIn("only in local mine.md", result.stdout)
        self.assertIn("only in upstream theirs.md", result.stdout)

    def test_status_ends_with_one_line_naming_the_entries_out_of_step(self) -> None:
        """Status closes with a count and the names, and stays silent when every entry is in step."""
        self.world.add_package("other-skill")
        self.world.run("pull")
        green = self.world.run("status")
        self.assertEqual(green.returncode, 0, green.stdout)
        self.assertNotIn("out of step", green.stdout)
        guide = self.world.repo_root / "sample-skill" / "references" / "guide.md"
        guide.write_text("guide line\nedited\n")
        red = self.world.run("status")
        self.assertEqual(red.returncode, 1, red.stdout)
        self.assertEqual(red.stdout.splitlines()[-1], "1 of 2 entries out of step: sample-skill")
        self.assertIn("other-skill: in step", red.stdout, "the existing per-entry lines must stay")

    def test_override_root_without_a_skilled_folder_is_refused(self) -> None:
        """An override that is not a root, or sits one level off, is a setup error."""
        not_a_root = self.world.repo_root.parent / "not-a-root"
        not_a_root.mkdir()
        for bad in (not_a_root, self.world.upstream_root / ".skilled"):
            result = self.world.run("status", override=bad)
            self.assertEqual(result.returncode, 2, f"{bad}: {result.stdout}{result.stderr}")
            self.assertIn("VENDOR_UPSTREAM_ROOT holds no .skilled folder", result.stderr)
        pulled = self.world.run("pull", override=not_a_root)
        self.assertEqual(pulled.returncode, 2)
        self.assertFalse((self.world.repo_root / "sample-skill").exists(), "a refused root must vendor nothing")


if __name__ == "__main__":
    unittest.main(verbosity=2)
