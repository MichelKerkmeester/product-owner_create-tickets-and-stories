#!/usr/bin/env python3
"""Prove this folder's run tooling against planted faults, before any scenario runs.

No model is called and nothing leaves the machine. The synthetic tests build a
small system tree, its fixtures and a run folder in a temporary directory, plant
the fault each change exists to catch, and pass only when the fault is caught and
the clean case is not flagged. A check that would pass without the change it
guards proves nothing, so the same input also runs through the unchanged Sonnet
scripts beside this folder as a negative control. Those run from a temporary copy,
so the Sonnet folder is never touched.

Tests:
  parse-synthetic  attachments parse into basename, repository-relative source and
                   sha256, a scenario without them parses exactly as the Sonnet
                   runner parses it, and a dead link, a basename collision and a
                   bullet with no link each exit 2 before any scenario starts
  isolation        staged attachments pass on both sides, and an undeclared file, a
                   missing one, a one-byte change and a subfolder in context/ fail
  staging-order    run_scenario with a stand-in turn sees every attachment in the
                   baseline, so an attachment edited in place is a modification
  collector        a Story bundle lands in its subfolder on both sides, flat files
                   stay flat, context/ is skipped with a warning, a dry run writes
                   nothing, and the Sonnet collector flattens the same input
  check-run        the default model is claude-opus-5-5, and an engine, model or
                   effort other than the run's own is a finding
  root-links       every relative link in the real playbook root resolves
  parse-real       the real playbook: 46 rows, their sides, slugs, turns, waves,
                   twins, attachments and export words, every attachment staged
                   and checked. It waits on the rewritten scenarios and the company
                   fixtures, and says so while either is missing

Usage: selftest.py [--keep]
  --keep  leave the temporary directory in place and print where it is

Exit codes:
  0  every test passed
  1  at least one test failed
"""
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
from urllib.parse import unquote

# Loading the run scripts as modules must leave no bytecode cache beside them,
# least of all in the Sonnet folder, which stays byte for byte as it was.
sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
REPORTS = os.path.dirname(os.path.dirname(HERE))
SYSTEM = os.path.dirname(os.path.dirname(REPORTS))
SONNET_RUN = os.path.join(REPORTS, "2026-09-25--manual-testing-playbook--claude-sonnet-5-medium", "run")
SCRIPTS = ("playbook_runner.py", "collect_exports.py", "check_run.py")
KEY = "product-owner"
MODEL = "claude-opus-5-5"
PLAYBOOK = os.path.join("sk-product-owner", "manual-testing-playbook")
FIXTURES = os.path.join("benchmark", "fixtures", "companies")

# The scenario manifest and each skill ID's attachments after its company context
# file. A Project twin carries the same row. Each export kind names the pattern the
# scenario file must hold for the export its row gives.
# id: (slug, group, company, turns, wave, export kind, attachments after the context file)
MANIFEST = {
    "SID-001": ("identity-handover", "identity", "loomlist", 2, 1, "task", []),
    "STK-001": ("quick-copy-task", "backlog-modes", "fernhouse", 1, 2, "task", []),
    "STK-002": ("design-notes-fe-task", "backlog-modes", "roamstay", 2, 2, "task",
                ["roamstay-date-picker-design-notes.md"]),
    "STK-003": ("long-be-integration-task", "backlog-modes", "fernhouse", 2, 2, "task",
                ["fernhouse-carrier-label-api-notes.md", "fernhouse-carrier-label-thread.md"]),
    "STK-004": ("parent-task-with-subtasks", "backlog-modes", "loomlist", 2, 2, "task",
                ["loomlist-recurring-todos-pm-brief.md"]),
    "STK-005": ("supplied-parent-subtask", "backlog-modes", "loomlist", 2, 2, "task",
                ["loomlist-recurring-todos-parent-task.md"]),
    "STK-006": ("data-tracking-task", "backlog-modes", "roamstay", 2, 2, "task",
                ["roamstay-booking-funnel-tracking-plan.md"]),
    "SBG-001": ("quick-bug", "backlog-modes", "fernhouse", 1, 3, "bug", []),
    "SBG-002": ("support-ticket-bug", "backlog-modes", "roamstay", 2, 3, "bug",
                ["roamstay-support-ticket-58213.md"]),
    "SBG-003": ("two-platform-log-bug", "backlog-modes", "loomlist", 2, 3, "bug",
                ["loomlist-reminders-dst-log-excerpt.md", "loomlist-reminders-dst-user-reports.md"]),
    "SDK-001": ("behavior-reference", "document-modes", "fernhouse", 2, 4, "doc",
                ["fernhouse-promotions-rules.md"]),
    "SDK-002": ("incident-runbook", "document-modes", "roamstay", 2, 4, "doc",
                ["roamstay-payment-webhook-incident-notes.md"]),
    "SDK-003": ("proposal-decision-owner", "document-modes", "loomlist", 2, 4, "doc",
                ["loomlist-sync-conflict-thread.md"]),
    "SDK-004": ("catalog-conflict-gate", "document-modes", "loomlist", 2, 4, "doc",
                ["loomlist-notification-spec.md", "loomlist-email-template-inventory.md"]),
    "SST-001": ("story-hard-values", "story-modes", "roamstay", 2, 5, "Story",
                ["roamstay-free-cancellation-pm-notes.md"]),
    "SST-002": ("story-forced-delivery", "story-modes", "loomlist", 2, 5, "Story",
                ["loomlist-view-only-links-design-notes.md"]),
    "SST-003": ("story-refinement", "story-modes", "fernhouse", 2, 5, "refinement",
                ["fernhouse-save-card-draft.md"]),
    "SST-004": ("story-with-nested-tasks", "story-modes", "fernhouse", 2, 5, "bundle",
                ["fernhouse-order-tracking-pm-brief.md", "fernhouse-carrier-tracking-api-facts.md"]),
    "SEP-001": ("epic-from-strategy-brief", "story-modes", "roamstay", 2, 5, "Epic",
                ["roamstay-partner-self-onboarding-brief.md"]),
    "SEP-002": ("epic-natural-wording", "story-modes", "loomlist", 2, 5, "Epic",
                ["loomlist-offline-mode-brief.md"]),
    "SEP-003": ("epic-quick-energy", "story-modes", "fernhouse", 1, 5, "Epic", []),
    "SIR-001": ("vague-intake-kind-and-energy", "interactive-routing", "roamstay", 2, 6, "intake", []),
    "SIR-002": ("conflicting-commands", "interactive-routing", "fernhouse", 2, 6, "intake",
                ["fernhouse-wishlist-feedback.md"]),
}
TOTAL_TURNS = 86
NUMBER = r"(?:\[###\]|\[NNN\]|NNN|###|\d{3})"
EXPORT_PATTERNS = {
    "refinement": r"export/fernhouse-save-card-draft\.md",
    "bundle": rf"export/{NUMBER} - Story-[^/`\n]+/",
}
LINK_TARGET_RE = re.compile(r"\]\(\s*(?:<([^>]+)>|([^)\s]+))(?:\s+\"[^\"]*\")?\s*\)")


# --- harness ------------------------------------------------------------------

class Test:
    def __init__(self, name):
        self.name, self.checks, self.failures, self.caught = name, 0, [], []
        self.waits_on = None

    def check(self, ok, message):
        self.checks += 1
        if not ok:
            self.failures.append(message)
        return ok

    def fault(self, label, caught, detail=""):
        """A planted fault must be caught. Each caught one is listed, so the output
        shows the fault was planted rather than only that nothing failed."""
        self.checks += 1
        if caught:
            self.caught.append(label)
        else:
            self.failures.append(f"planted fault not caught: {label}" + (f" ({detail})" if detail else ""))


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def py(script, *args):
    return subprocess.run([sys.executable, "-B", script, *args], capture_output=True, text=True,
                          stdin=subprocess.DEVNULL, timeout=120)


def files_under(root):
    if not os.path.isdir(root):
        return set()
    return {os.path.relpath(os.path.join(dp, f), root) for dp, _, fs in os.walk(root) for f in fs}


def strip_code(text):
    """Markdown with fenced blocks and inline code removed, so a link shown as an
    example is not read as a link."""
    text = re.sub(r"^(`{3,}|~{3,}).*?^\1[ \t]*$", "", text, flags=re.M | re.S)
    return re.sub(r"`[^`\n]*`", "", text)


# --- synthetic trees ------------------------------------------------------------

def scenario(sid, title, turns, attachments=None):
    """A scenario file in the playbook's contract shape. Section 1 carries a stray
    Attachments bullet with a dead link, so a parse that reads outside the contract
    fails loudly."""
    if attachments is None:
        bullet = ""
    elif isinstance(attachments, str):
        bullet = f"- Attachments: {attachments}\n"
    else:
        bullet = "- Attachments: " + ", ".join(
            f"[{os.path.basename(a)}](../../../benchmark/fixtures/companies/{a})" for a in attachments) + "\n"
    table = "".join(f"| {n} | `{t}` | Behave | State | Evidence |\n" for n, t in enumerate(turns, 1))
    return (f'---\ntitle: "{sid} -- {title}"\ndescription: "Synthetic scenario."\nversion: 1.0.0.0\n---\n\n'
            f"# {sid} -- {title}\n\n## 1. OVERVIEW\n\nAn example outside the contract:\n\n"
            "- Attachments: [not-staged.md](../../../benchmark/fixtures/companies/nowhere/not-staged.md)\n\n"
            f"## 2. SCENARIO CONTRACT\n\n- Objective: Exercise the run tooling\n- Prompt: `{turns[0]}`\n"
            f"{bullet}- Runtime profile: synthetic\n\n### Conversation chain\n\n"
            "| Turn | Exact user input | Expected assistant behavior | State check | Evidence |\n"
            "|---|---|---|---|---|\n"
            f"{table}\n## 3. TEST EXECUTION\n\n- Prompt: `{turns[0]}`\n")


LEGACY_TURNS = ["$story Write the checkout story."]
REFINE_TURNS = ["$story Refine context/fernhouse-save-card-draft.md and keep its file name."]
BUNDLE_TURNS = ["$story Write the order tracking story from context/fernhouse-order-tracking-pm-brief.md "
                "and break it into tasks.",
                "Split it into FE iOS, FE Android, FE web and BE tracking webhook."]
BUNDLE_ATTACHMENTS = ["fernhouse/fernhouse-context.md", "fernhouse/fernhouse-order-tracking-pm-brief.md"]
FIXTURE_TEXT = {
    "fernhouse/fernhouse-context.md": "# Fernhouse\n\nSurfaces: Web, iOS, Android.\n",
    "fernhouse/fernhouse-order-tracking-pm-brief.md": "# Order tracking brief\n\nOrder placed, Packed, Shipped.\n",
    "fernhouse/fernhouse-save-card-draft.md": "# PRD - Checkout - Save card for next time\n\nRough draft.\n",
    "other/fernhouse-order-tracking-pm-brief.md": "# Another file with the same basename\n",
}


def make_po_system(root, bundle_attachments=BUNDLE_ATTACHMENTS):
    """A Product Owner shaped tree: AGENTS.md, a skill holding its playbook, a
    Project kernel with knowledge, and company fixtures under benchmark/."""
    system = os.path.join(root, "repo", "AI Systems", "Product Owner")
    write(os.path.join(system, "AGENTS.md"), "# Product Owner\n")
    write(os.path.join(system, "sk-product-owner", "SKILL.md"), "# Skill\n")
    write(os.path.join(system, "export", ".gitkeep"), "")
    write(os.path.join(system, "claude project", "Custom Instructions.md"), "# Kernel\n")
    write(os.path.join(system, "claude project", "knowledge", "Story Mode.md"), "# Story Mode\n")
    for rel, text in FIXTURE_TEXT.items():
        write(os.path.join(system, FIXTURES, rel), text)
    pb = os.path.join(system, PLAYBOOK)
    write(os.path.join(pb, "manual-testing-playbook.md"),
          "# Playbook\n\n| Wave | IDs | Notes |\n|---|---|---|\n"
          "| 1 | `SST-001`, `PST-001` | No attachments |\n"
          "| 2 | `SST-003..SST-004`, `PST-003..PST-004` | Attachments |\n")
    refine = ["fernhouse/fernhouse-context.md", "fernhouse/fernhouse-save-card-draft.md"]
    for prefix, side in (("S", "skill"), ("P", "project")):
        folder = os.path.join(pb, f"{side}-story-modes")
        write(os.path.join(folder, "legacy-no-attachments.md"),
              scenario(f"{prefix}ST-001", "No attachments", LEGACY_TURNS))
        write(os.path.join(folder, "story-refinement.md"),
              scenario(f"{prefix}ST-003", "Refinement", REFINE_TURNS, refine))
        write(os.path.join(folder, "story-with-nested-tasks.md"),
              scenario(f"{prefix}ST-004", "Story with tasks", BUNDLE_TURNS,
                       bundle_attachments if prefix == "S" else BUNDLE_ATTACHMENTS))
    return system


def make_deal_system(root):
    """A Deal Templates shaped tree with the two scenarios the runner's profiles
    name, which must parse and build exactly as the Sonnet runner does."""
    system = os.path.join(root, "repo", "AI Systems", "Barter - Deal Templates")
    write(os.path.join(system, "AGENTS.md"), "# Deal Templates\n")
    write(os.path.join(system, "sk-deal-templates", "SKILL.md"), "# Skill\n")
    write(os.path.join(system, "claude project", "Custom Instructions.md"), "# Kernel\n")
    pb = os.path.join(system, "sk-deal-templates", "manual-testing-playbook")
    write(os.path.join(pb, "manual-testing-playbook.md"),
          "# Playbook\n\n| Wave | IDs | Notes |\n|---|---|---|\n| 1 | `SVC-003`, `SBD-002` | Profiles |\n")
    write(os.path.join(pb, "skill-voice", "web-access.md"), scenario("SVC-003", "No web", ["Write a deal."]))
    write(os.path.join(pb, "skill-batch", "high-filename.md"), scenario("SBD-002", "Numbering", ["Next deal."]))
    return system


# --- the stand-in turn ------------------------------------------------------------

BUNDLE_FILES = [  # (number suffix, file stem, H1), Story first, then its tasks in order
    ("", "Story-order-tracking", "Order tracking"),
    (".1", "task-ios-order-status", "FE - iOS - TRACK - Order status timeline"),
    (".2", "task-android-order-status", "FE - Android - TRACK - Order status timeline"),
    (".3", "task-web-order-status", "FE - Web - TRACK - Order status timeline"),
    (".4", "task-tracking-webhook", "BE - TRACK - Carrier tracking webhook"),
]


def body(h1):
    return (f"# {h1}\n\n## About\n* * *\n"
            "Customers follow an order from the moment it is placed until it arrives, on every surface "
            "they shop on, so nobody has to ask support where a parcel is.\n"
            "The carrier reports each status change, and the order page shows the latest one.\n")


def reply(blocks):
    lines = []
    for label, text, path in blocks:
        lines += [f"**Deliverable Block: {label}**", "", "```markdown", text.rstrip("\n"), "```", "",
                  f"Export-equivalent path: `{path}`", ""]
    return "\n".join(lines + ["HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none."])


def skill_write(scratch, rel, text):
    write(os.path.join(scratch, rel), text)
    return f"Path: {rel}\nVerified: read-back succeeded; {text.count(chr(10))} lines"


def turn_action(sid, turn, scratch):
    """What the stand-in runtime does and says for one turn."""
    clar = body("Order tracking question")
    if (sid, turn) == ("SST-001", 1):
        # A skill runtime that leaves the number slot unfilled has written a defect,
        # and the collected name must keep it visible.
        skill_write(scratch, "export/[###] - task-unnumbered.md", body("Unnumbered"))
        return skill_write(scratch, "export/001 - Story-checkout.md", body("Checkout"))
    if (sid, turn) == ("PST-001", 1):
        return reply([("Story", body("Checkout"), "export/[NNN] - Story-checkout.md")])
    if (sid, turn) == ("SST-003", 1):
        # The planted fault: the refinement is exported, and the attachment is also
        # edited in place, which the ledger must show as a modification.
        with open(os.path.join(scratch, "context", "fernhouse-save-card-draft.md"), "a", encoding="utf-8") as fh:
            fh.write("Edited in place.\n")
        return skill_write(scratch, "export/fernhouse-save-card-draft.md", body("Checkout - Save card"))
    if (sid, turn) == ("PST-003", 1):
        return reply([("Story", body("Checkout - Save card"), "export/fernhouse-save-card-draft.md")])
    if (sid, turn) == ("SST-004", 1):
        return skill_write(scratch, "export/001 - Story-order-tracking-clarification.md", clar)
    if (sid, turn) == ("PST-004", 1):
        return reply([("clarification", clar, "export/[NNN] - Story-order-tracking-clarification.md")])
    if (sid, turn) == ("SST-004", 2):
        return "\n".join(skill_write(scratch, f"export/002 - Story-order-tracking/002{n} - {stem}.md", body(h1))
                         for n, stem, h1 in BUNDLE_FILES)
    if (sid, turn) == ("PST-004", 2):
        return reply([(stem, body(h1), f"export/[NNN] - Story-order-tracking/[NNN]{n} - {stem}.md")
                      for n, stem, h1 in BUNDLE_FILES])
    raise AssertionError(f"no stand-in action for {sid} turn {turn}")


# --- tests ------------------------------------------------------------------------

def test_parse_synthetic(t, ctx):
    runner, sonnet, system = ctx["runner"], ctx["sonnet_runner"], ctx["po"]
    rows = {r["id"]: r for r in runner.load_playbook(system, KEY)}
    ctx["rows"] = rows
    t.check(sorted(rows) == ["PST-001", "PST-003", "PST-004", "SST-001", "SST-003", "SST-004"],
            f"rows parsed: {sorted(rows)}")
    want = [{"basename": os.path.basename(a),
             "source": "/".join(["AI Systems", "Product Owner", "benchmark", "fixtures", "companies", a]),
             "sha256": sha(os.path.join(system, FIXTURES, a))} for a in BUNDLE_ATTACHMENTS]
    t.check(rows["SST-004"]["attachments"] == want,
            f"SST-004 attachments {rows['SST-004']['attachments']} are not {want}")
    t.check(rows["PST-004"]["attachments"] == rows["SST-004"]["attachments"], "PST-004 differs from its twin")
    t.check(rows["SST-001"]["attachments"] == [] and rows["PST-001"]["attachments"] == [],
            "a scenario with no Attachments bullet gained attachments")
    t.fault("an Attachments bullet outside the scenario contract, with a dead link, is never staged",
            all("not-staged.md" not in json.dumps(r["attachments"]) for r in rows.values()))

    # Everything except the new field matches the Sonnet runner, on this system and
    # on a Deal Templates tree whose profiles drop a tool and seed export/.
    def strip(r):
        return {k: v for k, v in r.items() if k != "attachments"}

    old ={r["id"]: r for r in sonnet.load_playbook(system, KEY)}
    t.check(set(old) == set(rows) and all(strip(rows[i]) == old[i] for i in old),
            "a parsed row differs from the Sonnet runner's beyond the attachments field")
    t.check(runner.load_waves(system) == sonnet.load_waves(system), "load_waves differs from the Sonnet runner")
    t.check(runner.SYSTEM_KEYS == sonnet.SYSTEM_KEYS and runner.PROFILES == sonnet.PROFILES
            and runner.SKILL_TOOLS == sonnet.SKILL_TOOLS and runner.PROJECT_TOOLS == sonnet.PROJECT_TOOLS,
            "SYSTEM_KEYS, PROFILES or a tool list changed")
    deal = ctx["deal"]
    new_deal = runner.load_playbook(deal, "deal-templates")
    t.check([strip(r) for r in new_deal] == sonnet.load_playbook(deal, "deal-templates")
            and all(r["attachments"] == [] for r in new_deal),
            "the Deal Templates rows differ from the Sonnet runner's")
    t.check(any(r["id"] == "SVC-003" and "bash" not in r["tools"] for r in new_deal)
            and any(r["id"] == "SBD-002" and len(r["seed_export"]) == 8 for r in new_deal),
            "drop_tools or seed_export no longer reaches its row")

    # The dry run lists every attachment with its source and hash.
    dry = os.path.join(ctx["tmp"], "dry-run")
    proc = py(ctx["runner_path"], "--system", system, "--out", dry, "--engine", "claude",
              "--model", MODEL, "--effort", "medium", "--dry-run")
    listed = {r["id"]: r for r in json.loads(proc.stdout)} if proc.returncode == 0 else {}
    t.check(proc.returncode == 0 and all(listed[i]["attachments"] == rows[i]["attachments"] for i in rows),
            f"the dry run did not list each row's attachments (exit {proc.returncode}) {proc.stderr[-300:]}")
    shutil.rmtree(dry, ignore_errors=True)

    # Each planted fault stops the load, and the command exits 2 before it creates
    # the run folder, so no scenario can have started.
    faults = [
        ("an attachment link that does not resolve",
         ["fernhouse/fernhouse-context.md", "fernhouse/fernhouse-missing.md"], "does not resolve"),
        ("two attachments sharing one basename",
         ["fernhouse/fernhouse-order-tracking-pm-brief.md", "other/fernhouse-order-tracking-pm-brief.md"],
         "share the basename"),
        ("an Attachments bullet that names a file without linking it", "fernhouse-context.md", "names no link"),
    ]
    for n, (label, attachments, needle) in enumerate(faults, 1):
        faulty = make_po_system(os.path.join(ctx["tmp"], f"parse-fault-{n}"), attachments)
        try:
            runner.load_playbook(faulty, KEY)
            raised = ""
        except runner.PlaybookError as exc:
            raised = str(exc)
        out = os.path.join(ctx["tmp"], f"parse-fault-{n}-out")
        proc = py(ctx["runner_path"], "--system", faulty, "--out", out, "--engine", "claude",
                  "--model", MODEL, "--effort", "medium", "--dry-run")
        t.fault(f"{label} exits 2 before any scenario starts",
                needle in raised and proc.returncode == 2 and not proc.stdout.strip() and not os.path.exists(out),
                f"raised={raised[:120]!r} exit={proc.returncode}")
        if n == 1:
            control = py(ctx["sonnet_paths"]["playbook_runner.py"], "--system", faulty, "--out", out,
                         "--engine", "claude", "--model", MODEL, "--effort", "medium", "--dry-run")
            t.check(control.returncode == 0,
                    "negative control: the Sonnet runner should load the same dead link without noticing")
            shutil.rmtree(out, ignore_errors=True)


def test_isolation(t, ctx):
    runner, sonnet, system, rows, tmp = ctx["runner"], ctx["sonnet_runner"], ctx["po"], ctx["rows"], ctx["tmp"]
    for side, sid in (("skill", "SST-004"), ("project", "PST-004")):
        atts = rows[sid]["attachments"]
        scratch = os.path.join(tmp, "isolation", side)
        folder = os.path.join(scratch, "context")
        runner.build(system, side, scratch, [], atts)
        t.check(sorted(os.listdir(folder)) == sorted(a["basename"] for a in atts),
                f"{side}: context/ holds {sorted(os.listdir(folder))}")
        t.check(all(sha(os.path.join(folder, a["basename"])) == a["sha256"] for a in atts),
                f"{side}: a staged copy differs from its source")
        clean = runner.prove_isolation(side, scratch, atts)
        t.check(clean == [], f"{side}: the clean sandbox was flagged: {clean}")

        def extra():
            write(os.path.join(folder, "extra-notes.md"), "Not declared.\n")

        def missing():
            os.remove(os.path.join(folder, atts[-1]["basename"]))

        def altered():
            path = os.path.join(folder, atts[0]["basename"])
            data = bytearray(open(path, "rb").read())
            data[-2] ^= 1
            open(path, "wb").write(bytes(data))

        def subfolder():
            os.makedirs(os.path.join(folder, "nested"))

        planted = [("an undeclared file in context/", extra, "extra-notes.md"),
                   ("a declared attachment missing from context/", missing, atts[-1]["basename"]),
                   ("an attachment changed by one byte", altered, atts[0]["basename"]),
                   ("a subfolder inside context/", subfolder, "nested")]
        for label, plant, needle in planted:
            runner.build(system, side, scratch, [], atts)
            plant()
            problems = runner.prove_isolation(side, scratch, atts)
            t.fault(f"{side}: {label}", any(needle in p for p in problems), str(problems))
            if plant is extra:
                t.check(sonnet.prove_isolation(side, scratch) == [],
                        f"negative control: the Sonnet isolation proof should pass the {side} sandbox "
                        "holding an undeclared file")

    # A scenario without attachments builds the same bytes as the Sonnet runner and
    # is never judged on context/, including the seeded export/ a profile names.
    for side in ("skill", "project"):
        new, old = os.path.join(tmp, "legacy-new", side), os.path.join(tmp, "legacy-old", side)
        runner.build(system, side, new, [], [])
        sonnet.build(system, side, old, [])
        t.check(not os.path.exists(os.path.join(new, "context")), f"{side}: context/ created with no attachments")
        t.check(runner.snapshot(new) == sonnet.snapshot(old), f"{side}: the sandbox differs from the Sonnet build")
        t.check(runner.prove_isolation(side, new, []) == sonnet.prove_isolation(side, old),
                f"{side}: isolation verdict differs from the Sonnet runner")
    write(os.path.join(tmp, "legacy-new", "skill", "context", "own-file.md"), "System content.\n")
    t.check(runner.prove_isolation("skill", os.path.join(tmp, "legacy-new", "skill"), []) == [],
            "a scenario that declares no attachments was judged on context/")
    seed = runner.PROFILES[("deal-templates", "SBD-002")]["seed_export"]
    new, old = os.path.join(tmp, "deal-new"), os.path.join(tmp, "deal-old")
    runner.build(ctx["deal"], "skill", new, seed, [])
    sonnet.build(ctx["deal"], "skill", old, seed)
    t.check(runner.snapshot(new) == sonnet.snapshot(old) and len(os.listdir(os.path.join(new, "export"))) == 8,
            "a seeded export/ differs from the Sonnet build")


def test_staging_order(t, ctx):
    runner, system, rows, tmp = ctx["runner"], ctx["po"], ctx["rows"], ctx["tmp"]
    runner.ENGINE, runner.MODEL, runner.THINKING = "claude", MODEL, "medium"
    seen = {}

    def stand_in(scratch, session_dir, session_id, first, system_prompt, tools, prompt, events_path,
                 deny_roots, tail):
        sid = tail[-7:]
        turn = 1 if first else 2
        folder = os.path.join(scratch, "context")
        seen[(sid, turn)] = sorted(os.listdir(folder)) if os.path.isdir(folder) else None
        text = turn_action(sid, turn, scratch)
        open(events_path, "w").close()
        return {"rc": 0, "status": "ok", "wall_s": 0.0, "reply": text, "transcript": [], "tool_calls": 0,
                "tools_used": [], "input_tokens": 0, "output_tokens": 0, "reasoning_tokens": 0,
                "cost_usd": 0.0, "model_s": None, "startup_s": None, "stop_reason": None,
                "response_models": [MODEL]}

    runner.run_turn_claude = stand_in
    run, harness = os.path.join(tmp, "run"), os.path.join(tmp, "harness")
    os.makedirs(run)
    for sid in ("SST-001", "PST-001", "SST-003", "PST-003", "SST-004", "PST-004"):
        result = runner.run_scenario(system, KEY, rows[sid], run, harness)
        t.check(result["status"] == "ok", f"{sid}: run_scenario returned {result}")
    ctx["run"] = run

    for sid in ("SST-003", "PST-003", "SST-004", "PST-004"):
        want = sorted(a["basename"] for a in rows[sid]["attachments"])
        t.check(seen.get((sid, 1)) == want, f"{sid}: turn 1 saw context/ as {seen.get((sid, 1))}, not {want}")
    t.check(seen.get(("SST-001", 1)) is None and seen.get(("PST-001", 1)) is None,
            "a scenario with no attachments was given a context/ folder")

    def meta(side, sid, slug):
        return json.load(open(os.path.join(run, side, f"{sid} - {slug}", "meta.json"), encoding="utf-8"))

    for side, sid, slug in (("skill", "SST-004", "story-with-nested-tasks"),
                            ("claude project", "PST-004", "story-with-nested-tasks"),
                            ("skill", "SST-001", "legacy-no-attachments")):
        t.check(meta(side, sid, slug)["attachments"] == rows[sid]["attachments"],
                f"{sid}: meta.json does not record the row's attachments")
    changes = meta("skill", "SST-003", "story-refinement")["net_file_changes"]
    t.fault("an attachment edited in place is a modification of the baseline, never a created file",
            changes["modified"] == ["context/fernhouse-save-card-draft.md"]
            and changes["created"] == ["export/fernhouse-save-card-draft.md"], str(changes))
    created = meta("skill", "SST-004", "story-with-nested-tasks")["net_file_changes"]["created"]
    t.check(len(created) == 6 and all(p.startswith("export/") for p in created),
            f"SST-004 created {created}")
    ledgers = [json.loads(line)["ledger"] for line in open(os.path.join(run, "run-log.jsonl"), encoding="utf-8")]
    t.check(all(not p.startswith("context/") for led in ledgers for p in led["created"]),
            "a turn ledger lists a staged attachment as created")


def test_collector(t, ctx):
    run, tmp = ctx.get("run"), ctx["tmp"]
    if not run:
        t.check(False, "no synthetic run to collect, because staging-order did not produce one")
        return
    out = os.path.join(tmp, "collected")
    proc = py(os.path.join(HERE, "collect_exports.py"), run, out)
    t.check(proc.returncode == 0, f"the collector exited {proc.returncode}: {proc.stderr[-300:]}")
    skill_bundle = "skill/SST-004 - 002 - Story-order-tracking"
    project_bundle = "claude project/PST-004 - NNN - Story-order-tracking"
    want = {"skill/SST-001 - 001 - Story-checkout.md",
            "skill/SST-001 - [###] - task-unnumbered.md",
            "skill/SST-003 - fernhouse-save-card-draft.md",
            "skill/SST-004 - 001 - Story-order-tracking-clarification.md",
            "claude project/PST-001 - NNN - Story-checkout.md",
            "claude project/PST-003 - fernhouse-save-card-draft.md",
            "claude project/PST-004 - NNN - Story-order-tracking-clarification.md"}
    want |= {f"{skill_bundle}/002{n} - {stem}.md" for n, stem, _ in BUNDLE_FILES}
    want |= {f"{project_bundle}/NNN{n} - {stem}.md" for n, stem, _ in BUNDLE_FILES}
    got = files_under(out)
    t.check(got == want, f"collected set differs: missing {sorted(want - got)}, extra {sorted(got - want)}")
    for n, stem, h1 in BUNDLE_FILES:
        for rel in (f"{skill_bundle}/002{n} - {stem}.md", f"{project_bundle}/NNN{n} - {stem}.md"):
            path = os.path.join(out, rel)
            t.check(os.path.isfile(path) and read(path) == body(h1), f"{rel} does not hold its own block")
    refined = os.path.join(out, "skill/SST-003 - fernhouse-save-card-draft.md")
    t.check(os.path.isfile(refined) and read(refined) == body("Checkout - Save card"),
            "the refinement export was replaced by the edited attachment")
    t.fault("an attachment the runtime changed is skipped with one warning line",
            [line for line in proc.stdout.splitlines() if line.startswith("warning")] and
            all("context/fernhouse-save-card-draft.md" in line
                for line in proc.stdout.splitlines() if line.startswith("warning"))
            and not any("context" in p.split("/")[1:] for p in got), proc.stdout[-400:])

    dry = os.path.join(tmp, "collected-dry")
    dproc = py(os.path.join(HERE, "collect_exports.py"), run, dry, "--dry-run")
    t.check(dproc.returncode == 0 and not os.path.exists(dry) and dproc.stdout == proc.stdout,
            "the dry run wrote files or listed a different set")

    control = os.path.join(tmp, "collected-sonnet")
    cproc = py(ctx["sonnet_paths"]["collect_exports.py"], run, control)
    flat = files_under(control)
    t.check(cproc.returncode == 0 and flat and all(len(p.split("/")) == 2 for p in flat)
            and "skill/SST-004 - 002.1 - task-ios-order-status.md" in flat
            and "claude project/PST-004 - NNN.1 - task-ios-order-status.md" in flat
            and "warning" not in cproc.stdout,
            f"negative control: the Sonnet collector should flatten the same bundle, got {sorted(flat)[:6]}")

    # An export edited after collection survives the next collection, so a hand
    # edit is never undone silently, and --force restores the run's copy.
    edited = os.path.join(out, "skill/SST-001 - 001 - Story-checkout.md")
    write(edited, "edited by hand\n")
    kept = py(os.path.join(HERE, "collect_exports.py"), run, out)
    t.check(kept.returncode == 0 and read(edited) == "edited by hand\n"
            and any(line.startswith("warning skill SST-001 - 001 - Story-checkout.md")
                    for line in kept.stdout.splitlines()),
            "the collector overwrote an export edited after collection, or kept it without a warning")
    forced = py(os.path.join(HERE, "collect_exports.py"), run, out, "--force")
    t.check(forced.returncode == 0 and read(edited) == body("Checkout"),
            "--force did not restore the run's copy of an edited export")

    # A remeasure round is collected only on request.
    with_round = os.path.join(tmp, "run-with-round")
    shutil.copytree(run, with_round)
    shutil.copytree(os.path.join(run, "skill"), os.path.join(with_round, "remeasure-demo", "run-1", "skill"))
    plain, rounds = os.path.join(tmp, "collected-plain"), os.path.join(tmp, "collected-rounds")
    py(os.path.join(HERE, "collect_exports.py"), with_round, plain)
    py(os.path.join(HERE, "collect_exports.py"), with_round, rounds, "--rounds")
    t.check(not any("remeasure-demo" in p for p in files_under(plain))
            and any(p.startswith("skill/remeasure-demo/run-1/") for p in files_under(rounds)),
            "a remeasure round was collected without --rounds, or left out with it")


def make_check_run(root, engine="claude", model=MODEL, thinking="medium", streams=MODEL):
    scenarios = [{"id": "SST-001", "side": "skill", "slug": "demo", "turns": ["one", "two"]},
                 {"id": "PST-001", "side": "project", "slug": "demo", "turns": ["one"]}]
    write(os.path.join(root, "manifest.json"), json.dumps(
        {"engine": engine, "model": model, "thinking": thinking, "claude_version": "synthetic",
         "scenarios": scenarios}))
    write(os.path.join(root, "run-status.json"), "[]")
    for sc in scenarios:
        folder = os.path.join(root, "skill" if sc["side"] == "skill" else "claude project",
                              f"{sc['id']} - {sc['slug']}")
        write(os.path.join(folder, "meta.json"), json.dumps({"completed": True, "turns_run": len(sc["turns"])}))
        for n in range(1, len(sc["turns"]) + 1):
            write(os.path.join(root, "replies", f"{sc['id']}-turn{n}.txt"), "A reply.\n")
            write(os.path.join(folder, f"events-turn-{n}.jsonl"), "\n".join(json.dumps(e) for e in (
                {"type": "system", "model": streams},
                {"type": "assistant", "message": {"model": streams, "content": []}},
                {"type": "result", "modelUsage": {streams: {}}})) + "\n")
    return root


def test_check_run(t, ctx):
    tmp, script, old = ctx["tmp"], os.path.join(HERE, "check_run.py"), ctx["sonnet_paths"]["check_run.py"]
    clean = make_check_run(os.path.join(tmp, "check-clean"))
    proc = py(script, clean)
    t.check(proc.returncode == 0 and f"claude {MODEL} at effort medium" in proc.stdout,
            f"a clean run with no --model did not pass against {MODEL}: {proc.stdout.strip()}")
    planted = [("effort high in manifest.json", {"thinking": "high"}, "thinking is 'high'"),
               ("engine pi in manifest.json", {"engine": "pi"}, "engine is 'pi'"),
               ("model claude-sonnet-5 in manifest.json", {"model": "claude-sonnet-5"},
                "model is 'claude-sonnet-5'"),
               ("an event stream naming claude-sonnet-5", {"streams": "claude-sonnet-5"}, "not only " + MODEL)]
    for n, (label, fields, needle) in enumerate(planted, 1):
        run = make_check_run(os.path.join(tmp, f"check-fault-{n}"), **fields)
        proc = py(script, run)
        t.fault(label, proc.returncode == 1 and needle in proc.stdout, proc.stdout.strip()[-200:])
    high = os.path.join(tmp, "check-fault-1")
    t.check(py(script, "--effort", "high", high).returncode == 0,
            "--effort high before the folder was not read as the expected effort")
    sonnet_run = make_check_run(os.path.join(tmp, "check-sonnet"), model="claude-sonnet-5",
                                streams="claude-sonnet-5")
    t.check(py(script, sonnet_run, "--model", "claude-sonnet-5").returncode == 0,
            "--model after the folder was not read as the expected model")
    t.check(py(old, clean).returncode == 1,
            "negative control: the Sonnet check_run should reject the clean run, since it expects claude-sonnet-5")
    t.check(py(old, high, "--model", MODEL).returncode == 0,
            "negative control: the Sonnet check_run should pass effort high, since it never reads the effort")


def test_root_links(t, ctx):
    root = os.path.join(SYSTEM, PLAYBOOK, "manual-testing-playbook.md")
    if not t.check(os.path.isfile(root), f"no playbook root at {os.path.relpath(root, SYSTEM)}"):
        return
    links = []
    for a, b in LINK_TARGET_RE.findall(strip_code(read(root))):
        target = (a or b).strip()
        if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("#"):
            continue
        links.append(unquote(target.split("#", 1)[0]))
    dead = [x for x in links if not os.path.exists(os.path.join(os.path.dirname(root), x))]
    if dead and all("fixtures/companies" in x for x in dead):
        t.waits_on = "the company fixtures the root links to"
    t.check(links and not dead, f"{len(dead)} of {len(links)} relative links do not resolve: {dead[:5]}")


def test_parse_real(t, ctx):
    runner = ctx["runner"]
    waits = "the 46 rewritten scenario files and the company fixtures they attach"
    try:
        rows = runner.load_playbook(SYSTEM, KEY)
    except runner.PlaybookError as exc:
        t.waits_on = "the company fixtures the scenario files attach"
        t.check(False, f"{len(exc.problems)} attachment problem(s), first: {exc.problems[0]}")
        return
    by_id = {r["id"]: r for r in rows}
    ids = set(MANIFEST) | {"P" + i[1:] for i in MANIFEST}
    present = ids & set(by_id)
    if len(rows) != len(ids) or present != ids:
        t.waits_on = waits
        t.check(False, f"the playbook holds {len(rows)} scenario files and {len(present)} of the "
                       f"{len(ids)} manifest IDs, so the scenarios are not written yet")
        return
    waves = runner.load_waves(SYSTEM)
    t.check(sum(len(r["turns"]) for r in rows) == TOTAL_TURNS,
            f"{sum(len(r['turns']) for r in rows)} turns, not {TOTAL_TURNS}")
    scratch = os.path.join(ctx["tmp"], "real-context")
    for sid, (slug, group, company, turns, wave, kind, sources) in MANIFEST.items():
        pid = "P" + sid[1:]
        s, p = by_id[sid], by_id[pid]
        for row, side in ((s, "skill"), (p, "project")):
            rid = row["id"]
            t.check(row["side"] == side and row["group"] == f"{side}-{group}" and row["slug"] == slug,
                    f"{rid}: {row['side']}/{row['group']}/{row['slug']}, not {side}/{side}-{group}/{slug}")
            t.check(len(row["turns"]) == turns, f"{rid}: {len(row['turns'])} turns, not {turns}")
            t.check(waves.get(rid) == wave, f"{rid}: wave {waves.get(rid)}, not {wave}")
            names = [a["basename"] for a in row["attachments"]]
            t.check(names == [f"{company}-context.md"] + sources, f"{rid}: attachments {names}")
            base = "/".join(["AI Systems", "Product Owner", "benchmark", "fixtures", "companies", company])
            t.check(all(a["source"] == f"{base}/{a['basename']}" for a in row["attachments"]),
                    f"{rid}: an attachment lives outside {base}")
            missing = [n for n in names if f"context/{n}" not in (row["turns"] or [""])[0]]
            t.check(not missing, f"{rid}: Turn 1 does not name {missing}")
            text = read(row["file"])
            pattern = EXPORT_PATTERNS.get(kind, rf"export/{NUMBER} - {kind}-")
            t.check(re.search(pattern, text), f"{rid}: no export path matching {pattern}")
            t.check("PRD-" not in text, f"{rid}: holds the retired PRD- export word")
            shutil.rmtree(scratch, ignore_errors=True)
            os.makedirs(scratch)
            runner.stage_attachments(SYSTEM, scratch, row["attachments"])
            problems = runner.context_problems(scratch, row["attachments"])
            t.check(not problems, f"{rid}: staged attachments fail the check: {problems}")
        t.check(s["turns"] == p["turns"], f"{sid} and {pid} differ in their turns")
        t.check([(a["basename"], a["source"]) for a in s["attachments"]]
                == [(a["basename"], a["source"]) for a in p["attachments"]],
                f"{sid} and {pid} differ in their attachments")
    # One full sandbox per side proves the real packaging and the real attachments
    # pass isolation together.
    for rid, side in (("SST-004", "skill"), ("PST-004", "project")):
        box = os.path.join(ctx["tmp"], "real-sandbox", side)
        runner.build(SYSTEM, side, box, by_id[rid]["seed_export"], by_id[rid]["attachments"])
        problems = runner.prove_isolation(side, box, by_id[rid]["attachments"])
        t.check(not problems, f"{rid}: the real sandbox fails isolation: {problems}")


TESTS = [("parse-synthetic", test_parse_synthetic), ("isolation", test_isolation),
         ("staging-order", test_staging_order), ("collector", test_collector),
         ("check-run", test_check_run), ("root-links", test_root_links), ("parse-real", test_parse_real)]


def main(argv):
    keep = "--keep" in argv[1:]
    started = time.time()
    tmp = tempfile.mkdtemp(prefix="po-run-selftest-")
    results = []
    try:
        ctx = {"tmp": tmp, "runner_path": os.path.join(HERE, "playbook_runner.py")}
        missing = [s for s in SCRIPTS if not os.path.isfile(os.path.join(SONNET_RUN, s))]
        if missing:
            print(f"the Sonnet run folder lacks {missing}, so the negative controls cannot run", file=sys.stderr)
            return 1
        ctx["sonnet_paths"] = {}
        for script in SCRIPTS:
            copy = os.path.join(tmp, "sonnet", script)
            os.makedirs(os.path.dirname(copy), exist_ok=True)
            shutil.copyfile(os.path.join(SONNET_RUN, script), copy)
            ctx["sonnet_paths"][script] = copy
        ctx["runner"] = load_module("selftest_runner", ctx["runner_path"])
        ctx["sonnet_runner"] = load_module("selftest_sonnet_runner", ctx["sonnet_paths"]["playbook_runner.py"])
        ctx["po"] = make_po_system(os.path.join(tmp, "po"))
        ctx["deal"] = make_deal_system(os.path.join(tmp, "deal"))
        for name, fn in TESTS:
            t = Test(name)
            try:
                fn(t, ctx)
            except Exception as exc:  # a crash is a failed test, reported with its line
                where = traceback.extract_tb(exc.__traceback__)[-1]
                t.failures.append(f"raised {type(exc).__name__}: {exc} (line {where.lineno})")
            results.append(t)
    finally:
        if keep:
            print(f"temporary directory kept at {tmp}")
        else:
            shutil.rmtree(tmp, ignore_errors=True)
    for t in results:
        verdict = "PASS" if not t.failures else "FAIL"
        waits = f" [waits on {t.waits_on}]" if t.failures and t.waits_on else ""
        print(f"{verdict} {t.name}: {t.checks} checks, {len(t.caught)} planted faults caught{waits}")
        for label in t.caught:
            print(f"     caught: {label}")
        for failure in t.failures[:12]:
            print(f"     failed: {failure}")
        if len(t.failures) > 12:
            print(f"     ... and {len(t.failures) - 12} more")
    passed = sum(1 for t in results if not t.failures)
    print(f"selftest: {passed} of {len(results)} tests passed in {time.time() - started:.1f}s")
    return 0 if passed == len(results) and results else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
