#!/usr/bin/env python3
"""Second pass after convert.py: repoint the remaining routing references, the
conditional read order, the gate counts, both validators and the Sync Loop docs.
Usage: fixes.py <scratch systems root>, holding "Product Owner" and the Sync Loop folder."""
import re
import sys
from pathlib import Path

SYS = Path(sys.argv[1])
PO = SYS / "Product Owner"
SL = SYS / "z — Claude Project Sync Loop"


def sub(path: Path, old: str, new: str, count: int = 1) -> None:
    text = path.read_text()
    assert text.count(old) == count, (path, text.count(old), old[:80])
    path.write_text(text.replace(old, new))


# ── AGENTS.md: the read order follows the packet the hub picks ────────
AG = PO / "AGENTS.md"
sub(AG, "Read the hub `SKILL.md`, `sk-product-owner/ROUTER.md` and `sk-product-owner/SKILL.md`, in that order, before processing any request. A request naming only a `figma-ds-cli` operation goes to `mcp-figma/` instead. On load",
    "Read the hub `SKILL.md` first, then `sk-product-owner/ROUTER.md` and `sk-product-owner/SKILL.md`. A request naming only a `figma-ds-cli` operation reads `mcp-figma/SKILL.md` instead. On load")
sub(AG, "read the three files named below directly and apply their routing,",
    "read the hub `SKILL.md` and the files it routes to directly and apply their routing,")
sub(AG, "| 2 | Skill Logic | Read `sk-product-owner/SKILL.md` or use the loaded `sk-product-owner` skill. |",
    "| 2 | Skill Logic | Read the hub `SKILL.md`, then the packet's `ROUTER.md` and `SKILL.md`. |")

# ── The packet SKILL.md ───────────────────────────────────────────────
SK = PO / "sk-product-owner" / "SKILL.md"
sub(SK, "The routing, energy-scaled thinking process, template gates, Human Voice Rules, quality floors and export protocol below replace generic assistant behavior.",
    "The energy-scaled thinking process, template gates, Human Voice Rules, quality floors and export protocol below replace generic assistant behavior.")
sub(SK, "- `sk-product-owner/SKILL.md` is the executable Product Owner identity and router",
    "- `sk-product-owner/SKILL.md` is the executable Product Owner identity")

# ── router-contract.md keeps its line count, the playbook cites its lines ─
RC = PO / "sk-product-owner" / "references" / "router-contract.md"
before = RC.read_text().count("\n")
sub(RC, "the prose routing rules in `SKILL.md` Section 2", "the prose routing rules in `ROUTER.md`", 3)
sub(RC, "the leaf authority that `SKILL.md` Section 2 summarizes", "the leaf authority that `ROUTER.md` summarizes")
assert RC.read_text().count("\n") == before

# ── READMEs ───────────────────────────────────────────────────────────
SR = PO / "sk-product-owner" / "README.md"
sub(SR, "`SKILL.md` carries the router, the identity and every rule.",
    "`ROUTER.md` carries the router, and `SKILL.md` the identity and every rule.")
sub(SR, "| [`SKILL.md`](./SKILL.md) | Executable router, energy-scaled thinking process, rules, and export protocol |",
    "| [`ROUTER.md`](./ROUTER.md) | Prose router: commands, framing, topics, thresholds and resource loading |\n"
    "| [`SKILL.md`](./SKILL.md) | Energy-scaled thinking process, rules, and export protocol |")

RM = PO / "README.md"
sub(RM, "It reads `sk-product-owner/SKILL.md` and works as the Product Owner from then on.",
    "It reads the hub `SKILL.md`, then `sk-product-owner/ROUTER.md` and `sk-product-owner/SKILL.md`, and works as the Product Owner from then on.")
sub(RM, "- **[→ Product Owner Skill](sk-product-owner/SKILL.md)** - router, rules and delivery protocol",
    "- **[→ Hub](SKILL.md)** - picks the packet for a request\n"
    "- **[→ Product Owner Router](sk-product-owner/ROUTER.md)** - commands, framing, topics and resource loading\n"
    "- **[→ Product Owner Skill](sk-product-owner/SKILL.md)** - rules and delivery protocol")
sub(RM, "| `bash benchmark/gates/run_gates.sh` | Router fixtures, format fixtures, rule parity, the example lint and its self-test in one run | `all 5 gates pass`, or `4 of 5 gates pass, 1 skipped` from a clone, where rule parity has no shared declaration to read |",
    "| `python3 benchmark/gates/check_hub.py` | The hub files, the registry packets, their routers and the stage one gold rows | `PASSED the hub, 2 registry packets and 11 gold rows` |\n"
    "| `bash benchmark/gates/run_gates.sh` | Router fixtures, format fixtures, rule parity, the example lint, the vendor sync, the hub check and their self-tests in one run | `all 9 gates pass`, or `7 of 9 gates pass, 2 skipped` from a clone, where rule parity and vendor sync have no shared folder to read |")
sub(RM, "holds `rule_parity.py` beside the example lint and the gate runner.",
    "holds `rule_parity.py` beside the example lint, the hub check and the gate runner.")
sub(RM, "│   ├── gates/                       rule_parity.py, example_lint.py and run_gates.sh",
    "│   ├── gates/                       rule_parity.py, example_lint.py, check_hub.py and run_gates.sh")

BR = PO / "benchmark" / "router" / "README.md"
sub(BR, "pseudocode, and `SKILL.md`'s prose routing section states the two must never",
    "pseudocode, and `ROUTER.md`'s prose routing section states the two must never")
sub(BR, "  line for line and as a parsed tree, while `SKILL.md` grows no python fence",
    "  line for line and as a parsed tree, while `SKILL.md` and `ROUTER.md` grow no python fence")

# ── Playbook rows that cite SKILL.md for routing ──────────────────────
PB = PO / "sk-product-owner" / "manual-testing-playbook"
ROW = re.compile(r"^\| \[`SKILL\.md`\]\(\.\./\.\./SKILL\.md\) \| (.*[Rr]out.*|Command collection and the conflict route) \|$", re.M)
rows = 0
for doc in sorted(PB.rglob("*.md")):
    text = doc.read_text()
    new, count = ROW.subn(lambda m: f"| [`ROUTER.md`](../../ROUTER.md) and [`SKILL.md`](../../SKILL.md) | {m.group(1)} |", text)
    if count:
        doc.write_text(new)
        rows += count
assert rows == 7, rows

# ── Gates README ──────────────────────────────────────────────────────
GR = PO / "benchmark" / "gates" / "README.md"
sub(GR, "The runner prints one line per gate and `all 5 gates pass` with exit 0 on a healthy tree.",
    "The runner prints one line per gate and `all 9 gates pass` with exit 0 on a healthy tree.")
sub(GR, 'title: "Gates: rule parity, example lint and the gate runner"', 'title: "Gates: rule parity, example lint, hub check and the gate runner"')
sub(GR, "lints the worked examples and replies, and runs", "lints the worked examples and replies, checks the hub, and runs")
sub(GR, "# Gates: rule parity, example lint and the gate runner", "# Gates: rule parity, example lint, hub check and the gate runner")
sub(GR, "*   Three files: `rule_parity.py`, `example_lint.py` and `run_gates.sh`",
    "*   Four files: `rule_parity.py`, `example_lint.py`, `check_hub.py` and `run_gates.sh`")
sub(GR, "the vendor sync status and its tests, keeps going", "the vendor sync status and its tests, the hub check and its self-test, keeps going")
sub(GR, "*   The vendor sync gate runs",
    "*   `check_hub.py` checks that the hub `SKILL.md`, `mode-registry.json` and `hub-router.json` agree with each packet and its router, exempts a registry packet marked vendored only when it is a non-default tool packet that `vendor.json` lists, and replays 11 stage one gold rows. `--self-test` plants five defects, among them an unregistered packet folder, a wrong `defaultMode` and a missing router pointer, and requires each to fail\n"
    "*   The vendor sync gate runs")
sub(GR, "| `run_gates.sh` | Runs every gate above plus",
    "| `check_hub.py` | Checks the hub files, the registry packets, each packet router and its pointer, the vendored exemption against `vendor.json` and the stage one gold rows. `--self-test` plants five defects in a scratch copy and requires each to fail |\n"
    "| `run_gates.sh` | Runs every gate above plus")
sub(GR, "python3 benchmark/gates/example_lint.py --self-test\n",
    "python3 benchmark/gates/example_lint.py --self-test\npython3 benchmark/gates/check_hub.py\npython3 benchmark/gates/check_hub.py --self-test\n")

# ── Leaf manifest note ────────────────────────────────────────────────
LM = PO / "sk-product-owner" / "leaf-manifest.config.json"
sub(LM, "sk-product-owner is a normal skill (no mode-registry.json).",
    "sk-product-owner is the default packet of the repository hub, whose mode-registry.json sits one level up, outside this skill root.")

# ── SYNC.md maintenance record ────────────────────────────────────────
SY = PO / "SYNC.md"
text = SY.read_text().rstrip("\n")
SY.write_text(text + "\n- 2026-10-20 Claude Code, on the operator's decision, made the repository root a parent hub: a root `SKILL.md`, `mode-registry.json` and `hub-router.json` pick the Product Owner packet or the vendored `mcp-figma/` packet, and the prose router moved from `SKILL.md` Section 2 into `sk-product-owner/ROUTER.md`, with a pointer left behind. No Project file needs an edit, because the kernel carries its own router section and the Project has no hub to pick. Skill and kernel versions are unchanged until the release step. This is a maintenance record, not a review.\n")

# ── The two validators lint the hub file and the router ───────────────
TW = PO / "benchmark" / "format" / "validate-output-format.cjs"
sub(TW, """const sourceFiles = [
  path.join(systemRoot, 'AGENTS.md'),
  path.join(skillRoot, 'SKILL.md'),
  path.join(skillRoot, 'README.md'),""", """const sourceFiles = [
  path.join(systemRoot, 'AGENTS.md'),
  path.join(skillRoot, 'SKILL.md'),
  // The system is a parent hub, so the stage one hub file at the root and the
  // packet router beside the skill are instruction surface the walk of
  // references and assets never reaches.
  path.join(systemRoot, 'SKILL.md'),
  path.join(skillRoot, 'ROUTER.md'),
  path.join(skillRoot, 'README.md'),""")
sub(TW, """const hvrEnforced = new Set([
  path.join(systemRoot, 'AGENTS.md'),
  path.join(skillRoot, 'SKILL.md'),""", """const hvrEnforced = new Set([
  path.join(systemRoot, 'AGENTS.md'),
  path.join(systemRoot, 'SKILL.md'),
  path.join(skillRoot, 'SKILL.md'),
  path.join(skillRoot, 'ROUTER.md'),""")

sub(SL / "systems.cjs", """    checkboxForm: { artifacts: 'blocking', sources: 'off' },
    hvrEnforced: [
      'AGENTS.md',
      'skill:SKILL.md',
""", """    checkboxForm: { artifacts: 'blocking', sources: 'off' },
    // The system is a parent hub, so the stage one hub file at the root and the
    // packet router beside the skill are instruction surface the walk of
    // references and assets never reaches.
    extraSources: ['SKILL.md', 'skill:ROUTER.md'],
    hvrEnforced: [
      'AGENTS.md',
      'SKILL.md',
      'skill:SKILL.md',
      'skill:ROUTER.md',
""")
sub(SL / "systems.cjs", """    hvrEnforced: system.hvrEnforced.map((entry) => resolveIn(system, entry)),
""", """    // A system with no hub has no instruction surface outside its skill folder.
    extraSources: (system.extraSources || []).map((entry) => resolveIn(system, entry)),
    hvrEnforced: system.hvrEnforced.map((entry) => resolveIn(system, entry)),
""")
sub(SL / "validate-output-format.cjs", """    path.join(system.skillRoot, 'SKILL.md'),
    path.join(system.skillRoot, 'README.md'),
    ...sharedCards,""", """    path.join(system.skillRoot, 'SKILL.md'),
    ...system.extraSources,
    path.join(system.skillRoot, 'README.md'),
    ...sharedCards,""")
sub(SL / "README.md", "| `sourcePerimeter(system)` | Function | Builds the source file list for a resolved system, leaving out the copies its entry declares as `vendoredShared` |",
    "| `sourcePerimeter(system)` | Function | Builds the source file list for a resolved system, adding the files its entry declares as `extraSources` and leaving out the copies it declares as `vendoredShared` |")
sub(SL / "feature-catalog" / "output-format-gate" / "output-format-validator.md",
    "`sourcePerimeter` builds the source file list for a resolved system, leaving out the regular-file copies the entry declares as `vendoredShared`",
    "`sourcePerimeter` builds the source file list for a resolved system, adding the hub files the entry declares as `extraSources` and leaving out the regular-file copies it declares as `vendoredShared`")
print("fixes applied")
