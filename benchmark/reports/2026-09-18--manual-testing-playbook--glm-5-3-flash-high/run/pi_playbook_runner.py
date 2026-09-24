#!/usr/bin/env python3
"""Run one system's manual testing playbook through the Pi CLI, against both packagings.

Every scenario gets its own scratch tree and its own Pi session, built fresh from the
repository, so no scenario can see another's files and a two-turn scenario keeps its
state only inside its own chain. This is the Pi port of run_packaging.sh in the Claude
Project Sync Loop folder: the same builders, the same isolation proof and the same
retrieval line, so a result here compares with a result there on the packaging rather
than on the harness.

Usage:
  pi_playbook_runner.py --system <system dir> --out <run folder> [--ids ID,ID]
                        [--side skill|project|both] [--jobs N] [--dry-run]

The run folder lives under benchmark/reports/. It keeps everything a run produces,
and collect_exports.py beside this file copies the deliverables alone out to
export/benchmark/, which holds real artifact exports and nothing else.

Exit codes:
  0   every scenario ran, whatever its verdict will be
  1   one or more scenarios could not be run after retries
  2   isolation failed or the system is not where it was named
  64  usage
"""
import argparse
import concurrent.futures as cf
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
import uuid

MODEL = "llmgateway/glm-5.3-flash"
THINKING = "high"
TURN_TIMEOUT_S = 900
ATTEMPTS = 3

SKILL_TOOLS = ["read", "bash", "edit", "write", "ls", "grep", "find"]
# A claude.ai Project has no filesystem. Reading stays, because opening knowledge/ is how
# Project Knowledge retrieval is simulated in a terminal. Writing does not, because a
# Project given write tools can satisfy a delivery rule by saving a file, which the
# deployed runtime cannot do, and the reply under test is then one it would never give.
PROJECT_TOOLS = ["read", "ls", "grep", "find"]

# Verbatim from run_packaging.sh. A real Project hands its knowledge over from a
# retrieval index and a terminal does not, so without this line a Project scenario
# measures the runtime's retrieval habits rather than the packaging's rules.
RETRIEVAL_NOTE = """

Your Project knowledge documents are the markdown files in the knowledge/ directory
beside these instructions. Wherever these instructions point at a knowledge document for
detail, by any wording, open the matching file in knowledge/ and read it before acting on
that section. Use your file reading tools to do so."""

TEST_DIR_EXACT = "manual-testing-playbook"

# Premises a scenario names as an environment rather than an action. Running the file
# does not establish them and nothing reports it when they are missing, so they are
# declared here where the runner applies them.
PROFILES = {
    # SVC-003 needs web access genuinely absent. Pi has no web tools, but bash can reach
    # the network, so bash is withheld for this one scenario.
    ("deal-templates", "SVC-003"): {"drop_tools": ["bash"]},
    # SBD-002 proves numbering past an invalid high filename. A folder without the trap
    # cannot test whether the trap is ignored, and the run would be void, not a pass.
    ("deal-templates", "SBD-002"): {"seed_export": [
        *(f"{n:03d} - deal-product-fixture.md" for n in range(1, 7)),
        "007 - deal-product-existing.md",
        "999-not-a-deal.md",
    ]},
}

SYSTEM_KEYS = {
    "Product Owner": "product-owner",
    "Barter - Deal Templates": "deal-templates",
    "Barter - Copywriter": "copywriter",
}

LOG_LOCK = threading.Lock()


# ─── playbook ────────────────────────────────────────────────────────────────

def _cells(row):
    out, cur, tick, i = [], "", False, 0
    s = row.strip().strip("|")
    while i < len(s):
        c = s[i]
        if c == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            cur += "|"; i += 2; continue
        if c == "`":
            tick = not tick
        if c == "|" and not tick:
            out.append(cur.strip()); cur = ""
        else:
            cur += c
        i += 1
    out.append(cur.strip())
    return out


def _unwrap(x):
    x = x.strip()
    if x.startswith("`") and x.endswith("`") and x.count("`") == 2:
        return x[1:-1]
    return x


def load_playbook(system_dir, key):
    sk = next(d for d in os.listdir(system_dir) if d.startswith("sk-"))
    pb = os.path.join(system_dir, sk, TEST_DIR_EXACT)
    rows = []
    for group in sorted(os.listdir(pb)):
        gdir = os.path.join(pb, group)
        if not os.path.isdir(gdir):
            continue
        side = "skill" if group.startswith("skill-") else "project"
        for f in sorted(os.listdir(gdir)):
            if not f.endswith(".md"):
                continue
            t = open(os.path.join(gdir, f), encoding="utf-8").read()
            m = re.search(r'^title:\s*"?([A-Z]{2,4}-\d{3})', t, re.M)
            if not m:
                continue
            turns, lines = [], t.splitlines()
            for i, line in enumerate(lines):
                if re.match(r"^\|\s*Turn\s*\|", line):
                    j = i + 2
                    while j < len(lines) and lines[j].startswith("|"):
                        c = _cells(lines[j])
                        if c and re.fullmatch(r"\d+", c[0]):
                            turns.append(_unwrap(c[1]))
                        j += 1
                    break
            if not turns:
                pm = re.search(r"^- Prompt:\s*(.+)$", t, re.M)
                if pm:
                    turns = [_unwrap(pm.group(1))]
            sid = m.group(1)
            prof = PROFILES.get((key, sid), {})
            tools = [x for x in (SKILL_TOOLS if side == "skill" else PROJECT_TOOLS)
                     if x not in prof.get("drop_tools", [])]
            rows.append({
                "id": sid, "side": side, "group": group, "slug": f[:-3],
                "file": os.path.join(gdir, f), "turns": turns,
                "twin": ("P" if sid[0] == "S" else "S") + sid[1:],
                "tools": tools, "seed_export": prof.get("seed_export", []),
            })
    return rows


def load_waves(system_dir):
    """Wave number per scenario id, read from the root playbook's wave table.

    Ranges are written `SIR-001..SIR-004`. An id the table omits takes the wave of its
    group's lowest listed id, which is how PDP-004 lands beside PDP-001 to PDP-003."""
    sk = next(d for d in os.listdir(system_dir) if d.startswith("sk-"))
    text = open(os.path.join(system_dir, sk, TEST_DIR_EXACT, TEST_DIR_EXACT + ".md"),
                encoding="utf-8").read()
    waves = {}
    for line in text.splitlines():
        m = re.match(r"^\|\s*(\d+)\s*\|(.+?)\|", line)
        if not m:
            continue
        n, cell = int(m.group(1)), m.group(2)
        for a, b in re.findall(r"([A-Z]{3}-\d{3})\.\.([A-Z]{3}-\d{3})", cell):
            for k in range(int(a[4:]), int(b[4:]) + 1):
                waves.setdefault(f"{a[:3]}-{k:03d}", n)
        for sid in re.findall(r"[A-Z]{3}-\d{3}", cell):
            waves.setdefault(sid, n)
    return waves


# ─── sandbox ─────────────────────────────────────────────────────────────────

def build(system_dir, side, scratch, seed_export):
    shutil.rmtree(scratch, ignore_errors=True)
    os.makedirs(scratch)
    if side == "skill":
        subprocess.run(["rsync", "-aL", "--exclude", "benchmark", "--exclude", TEST_DIR_EXACT,
                        "--exclude", "export", "--exclude", "changelog",
                        system_dir.rstrip("/") + "/", scratch + "/"],
                       check=True, stderr=subprocess.DEVNULL)
        shutil.rmtree(os.path.join(scratch, "claude project"), ignore_errors=True)
        # The playbook's precondition is a writable export/ that exists before the run.
        os.makedirs(os.path.join(scratch, "export"), exist_ok=True)
        for name in seed_export:
            with open(os.path.join(scratch, "export", name), "w", encoding="utf-8") as fh:
                fh.write(f"# {name[:-3]}\n\nOperator numbering fixture. Not a deal.\n")
    else:
        subprocess.run(["rsync", "-aL", os.path.join(system_dir, "claude project") + "/",
                        scratch + "/"], check=True, stderr=subprocess.DEVNULL)
        for f in os.listdir(scratch):
            if f == "README.md" or "review" in f.lower():
                p = os.path.join(scratch, f)
                if os.path.isfile(p):
                    os.remove(p)


def prove_isolation(side, scratch):
    """A failure stops the run. A harness that warns and continues produces a run
    somebody will later treat as evidence."""
    problems = []
    names = {f for _, _, fs in os.walk(scratch) for f in fs}
    dirs = {d for _, ds, _ in os.walk(scratch) for d in ds}
    if side == "project":
        for f in ("SKILL.md", "AGENTS.md"):
            if f in names:
                problems.append(f"{f} is reachable from the Project runtime")
        if not os.path.isfile(os.path.join(scratch, "Custom Instructions.md")):
            problems.append("the Project runtime has no kernel")
        if any(d.startswith("sk-") for d in dirs):
            problems.append("a skill tree is reachable from the Project runtime")
    else:
        if any("testing-playbook" in d for d in dirs) or any("testing-playbook" in f for f in names):
            problems.append("the skill runtime can read its own playbook")
        if "benchmark" in dirs:
            problems.append("the skill runtime can read earlier benchmark replies")
        if not os.path.isfile(os.path.join(scratch, "AGENTS.md")):
            problems.append("the skill runtime has no override document")
        if "claude project" in dirs or "Custom Instructions.md" in names:
            problems.append("the Project packaging is reachable from the skill runtime")
    return problems


def snapshot(root):
    out = {}
    for dp, _, fs in os.walk(root):
        for f in fs:
            p = os.path.join(dp, f)
            try:
                out[os.path.relpath(p, root)] = hashlib.sha256(open(p, "rb").read()).hexdigest()
            except OSError:
                pass
    return out


def diff(before, after):
    return {
        "created": sorted(set(after) - set(before)),
        "modified": sorted(k for k in set(after) & set(before) if after[k] != before[k]),
        "deleted": sorted(set(before) - set(after)),
    }


# ─── one turn ────────────────────────────────────────────────────────────────

def seatbelt(scratch, session_dir, deny_roots):
    """A macOS sandbox profile that confines the runtime to its own tree.

    Isolation was first proved only by inspecting what each sandbox held, and that was
    not enough: every sandbox sat beside its siblings, so a runtime listed `..`, grepped
    every other scenario's files and read two sibling exports into its own deliverable.
    A check on contents cannot see a path out, so the path out is closed here instead.
    Everything under the deny roots is refused and then the scenario's own sandbox and
    session folder are allowed back, because the last matching rule wins."""
    q = lambda p: '"' + os.path.realpath(p).replace('"', '\\"') + '"'
    deny = " ".join(f"(subpath {q(r)})" for r in deny_roots if os.path.exists(r))
    # Resolving a path stats every folder above it, so a write to a new file inside the
    # sandbox failed while its ancestors were denied outright. The ancestors get metadata
    # only: a stat resolves the path, while listing or reading them stays refused.
    ancestors = set()
    for leaf in (scratch, session_dir):
        cur = os.path.dirname(os.path.realpath(leaf))
        while cur and cur != "/":
            ancestors.add(cur)
            cur = os.path.dirname(cur)
    meta = " ".join(f"(literal {q(a)})" for a in sorted(ancestors))
    return ("(version 1)(allow default)"
            f"(deny file-read* file-write* {deny})"
            f"(allow file-read-metadata {meta})"
            f"(allow file-read* file-write* (subpath {q(scratch)}) (subpath {q(session_dir)}))")


def run_turn(scratch, session_dir, session_id, system_prompt, tools, prompt, events_path, deny_roots):
    cmd = ["sandbox-exec", "-p", seatbelt(scratch, session_dir, deny_roots),
           "pi", "-p", "--offline", "--mode", "json",
           "--model", MODEL, "--thinking", THINKING,
           "--session-dir", session_dir, "--session-id", session_id,
           "--no-context-files", "--no-skills", "--no-extensions",
           "--no-prompt-templates", "--no-themes", "--no-approve",
           "--tools", ",".join(tools),
           "--system-prompt", system_prompt,
           "--", prompt]
    t0 = time.time()
    status = "ok"
    marks = {}
    timed_out = threading.Event()
    # stderr is written inside the session folder and copied out afterwards. Node checks
    # its inherited stdio at startup, and a stderr file inside a denied folder makes that
    # check fail under the sandbox, so the runtime aborts before it runs a single turn.
    err_path = os.path.join(session_dir, os.path.basename(events_path).replace(".jsonl", ".stderr.txt"))
    with open(events_path, "w", encoding="utf-8") as out, \
         open(err_path, "w", encoding="utf-8") as err:
        # stdin closed: a non-interactive pi left holding stdin waits forever with no
        # output, which reads as a slow model rather than a deadlock
        p = subprocess.Popen(cmd, cwd=scratch, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                             stderr=err, text=True, bufsize=1)
        timer = threading.Timer(TURN_TIMEOUT_S, lambda: (timed_out.set(), p.kill()))
        timer.start()
        # Pi stamps an assistant message when it starts, not when it ends, so a
        # one-message reply measured from those stamps reads as instant. Events are
        # stamped here on arrival instead, and the turn runs from agent_start to agent_end.
        for line in p.stdout:
            out.write(line)
            try:
                kind = json.loads(line).get("type")
            except ValueError:
                kind = None
            if kind and kind not in marks:
                marks[kind] = time.time() - t0
        rc = p.wait()
        timer.cancel()
    shutil.copyfile(err_path, events_path.replace(".jsonl", ".stderr.txt"))
    if timed_out.is_set():
        status = "timeout"
    r = parse_events(events_path, rc, status, time.time() - t0)
    if "agent_start" in marks and "agent_end" in marks:
        r["model_s"] = round(marks["agent_end"] - marks["agent_start"], 2)
        r["startup_s"] = round(marks["agent_start"], 2)
    return r


def parse_events(path, rc, status, wall):
    msgs = None
    for line in open(path, encoding="utf-8", errors="ignore"):
        try:
            e = json.loads(line)
        except ValueError:
            continue
        if e.get("type") == "agent_end":
            msgs = e.get("messages") or []
    r = {"rc": rc, "status": status, "wall_s": round(wall, 2), "reply": "", "transcript": [],
         "tool_calls": 0, "tools_used": [], "input_tokens": 0, "output_tokens": 0,
         "reasoning_tokens": 0, "cost_usd": 0.0, "model_s": None, "startup_s": None, "stop_reason": None,
         "response_models": []}
    if msgs is None:
        if status == "ok":
            r["status"] = "no-agent-end"
        return r
    last_text = ""
    for m in msgs:
        role = m.get("role")
        content = m.get("content") if isinstance(m.get("content"), list) else []
        if role == "assistant":
            u = m.get("usage") or {}
            r["input_tokens"] += u.get("input", 0) or 0
            r["output_tokens"] += u.get("output", 0) or 0
            r["reasoning_tokens"] += u.get("reasoning", 0) or 0
            r["cost_usd"] += ((u.get("cost") or {}).get("total", 0) or 0)
            if m.get("responseModel") and m["responseModel"] not in r["response_models"]:
                r["response_models"].append(m["responseModel"])
            r["stop_reason"] = m.get("stopReason")
            texts = []
            for b in content:
                if b.get("type") == "text":
                    texts.append(b.get("text", ""))
                    r["transcript"].append({"kind": "text", "text": b.get("text", "")})
                elif b.get("type") == "toolCall":
                    r["tool_calls"] += 1
                    r["tools_used"].append(b.get("name"))
                    r["transcript"].append({"kind": "call", "name": b.get("name"),
                                            "args": b.get("arguments")})
            if texts:
                last_text = "\n".join(texts)
        elif role == "toolResult":
            body = "".join(b.get("text", "") for b in content if b.get("type") == "text")
            r["transcript"].append({"kind": "result", "name": m.get("toolName"),
                                    "error": m.get("isError"), "text": body[:4000]})
    r["reply"] = last_text
    if r["stop_reason"] in ("error", "aborted"):
        r["status"] = f"stop-{r['stop_reason']}"
    elif not r["reply"].strip() and r["status"] == "ok":
        r["status"] = "empty-reply"
    return r


# ─── one scenario ────────────────────────────────────────────────────────────

def deny_roots(system_dir, harness_root):
    # every sandbox, the repository with its playbooks and earlier replies, and the
    # operator's own transcripts
    repo = os.path.dirname(os.path.dirname(os.path.realpath(system_dir)))
    return [harness_root, repo, os.path.expanduser("~/.claude"), "/private/tmp/claude-501"]


def side_dir(side):
    return "skill" if side == "skill" else "claude project"


def write_transcript(path, sc, n, prompt, r):
    lines = [f"# {sc['id']} turn {n} transcript", "", f"**User:** {prompt}", ""]
    for item in r["transcript"]:
        if item["kind"] == "text":
            lines += ["**Assistant:**", "", item["text"], ""]
        elif item["kind"] == "call":
            lines += [f"**Tool call:** `{item['name']}` `{json.dumps(item['args'], ensure_ascii=False)[:600]}`", ""]
        else:
            flag = " (error)" if item.get("error") else ""
            lines += [f"**Tool result{flag}:** `{item['name']}`", "", "```text", item["text"][:1500], "```", ""]
    open(path, "w", encoding="utf-8").write("\n".join(lines))


def run_scenario(system_dir, key, sc, out_root, harness_root):
    base = os.path.join(harness_root, key, sc["side"])
    scratch = os.path.join(base, sc["id"])
    sessions = os.path.join(base, ".sessions", sc["id"])
    dest = os.path.join(out_root, side_dir(sc["side"]), f"{sc['id']} - {sc['slug']}")
    failures = []
    for attempt in range(1, ATTEMPTS + 1):
        build(system_dir, sc["side"], scratch, sc["seed_export"])
        problems = prove_isolation(sc["side"], scratch)
        if problems:
            return {"id": sc["id"], "side": sc["side"], "status": "isolation-failed",
                    "problems": problems}
        shutil.rmtree(sessions, ignore_errors=True)
        os.makedirs(sessions)
        if sc["side"] == "skill":
            sp = open(os.path.join(scratch, "AGENTS.md"), encoding="utf-8").read()
        else:
            sp = open(os.path.join(scratch, "Custom Instructions.md"), encoding="utf-8").read() + RETRIEVAL_NOTE
        shutil.rmtree(dest, ignore_errors=True)
        os.makedirs(dest)
        session_id = f"{key}-{sc['id']}-{uuid.uuid4().hex[:8]}"
        before0 = before = snapshot(scratch)
        turns, ok = [], True
        for n, prompt in enumerate(sc["turns"], 1):
            ev = os.path.join(dest, f"events-turn-{n}.jsonl")
            r = run_turn(scratch, sessions, session_id, sp, sc["tools"], prompt, ev,
                         deny_roots(system_dir, harness_root))
            after = snapshot(scratch)
            r["ledger"] = diff(before, after)
            before = after
            r["turn"], r["input"] = n, prompt
            turns.append(r)
            with LOG_LOCK:
                with open(os.path.join(out_root, "run-log.jsonl"), "a", encoding="utf-8") as fh:
                    fh.write(json.dumps({k: v for k, v in r.items() if k not in ("reply", "transcript")}
                                        | {"id": sc["id"], "side": sc["side"], "attempt": attempt}) + "\n")
            if r["status"] != "ok":
                ok = False
                failures.append({"attempt": attempt, "turn": n, "status": r["status"], "rc": r["rc"]})
                break
        if ok:
            break
        # a failed attempt keeps its evidence beside the retry, never silently replaced
        keep = os.path.join(out_root, "failed-attempts", side_dir(sc["side"]), f"{sc['id']}-attempt-{attempt}")
        shutil.rmtree(keep, ignore_errors=True)
        shutil.copytree(dest, keep)
    final = snapshot(scratch)
    changed = diff(before0, final)
    for rel in changed["created"] + changed["modified"]:
        tgt = os.path.join(dest, "exports", rel)
        os.makedirs(os.path.dirname(tgt), exist_ok=True)
        shutil.copy2(os.path.join(scratch, rel), tgt)
    os.makedirs(os.path.join(out_root, "replies"), exist_ok=True)
    for r in turns:
        open(os.path.join(dest, f"turn-{r['turn']}.md"), "w", encoding="utf-8").write(r["reply"])
        open(os.path.join(out_root, "replies", f"{sc['id']}-turn{r['turn']}.txt"), "w",
             encoding="utf-8").write(r["reply"])
        write_transcript(os.path.join(dest, f"transcript-turn-{r['turn']}.md"), sc, r["turn"], r["input"], r)
    meta = {
        "id": sc["id"], "side": sc["side"], "scenario_file": sc["file"], "twin": sc["twin"],
        "model": MODEL, "thinking": THINKING, "tools": sc["tools"], "seed_export": sc["seed_export"],
        "session_id": session_id, "attempts": attempt, "failures": failures, "completed": ok,
        "turns_declared": len(sc["turns"]), "turns_run": len(turns),
        "net_file_changes": changed,
        "turns": [{k: v for k, v in r.items() if k not in ("reply", "transcript")} for r in turns],
    }
    json.dump(meta, open(os.path.join(dest, "meta.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    return {"id": sc["id"], "side": sc["side"], "status": "ok" if ok else "failed",
            "attempts": attempt, "turns_run": len(turns), "turns_declared": len(sc["turns"])}


# ─── main ────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--system", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--ids", default="")
    ap.add_argument("--side", default="both", choices=["skill", "project", "both"])
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--dry-run", action="store_true")
    try:
        a = ap.parse_args()
    except SystemExit:
        return 64
    system_dir = os.path.abspath(a.system)
    key = SYSTEM_KEYS.get(os.path.basename(system_dir.rstrip("/")))
    if not key or not os.path.isdir(system_dir):
        print(f"no known system at {system_dir}", file=sys.stderr)
        return 2
    rows = load_playbook(system_dir, key)
    full = list(rows)
    if a.side != "both":
        rows = [r for r in rows if r["side"] == a.side]
    if a.ids:
        want = set(a.ids.split(","))
        rows = [r for r in rows if r["id"] in want]
    os.makedirs(a.out, exist_ok=True)
    waves = load_waves(system_dir)
    for r in full:
        if r["id"] not in waves:
            same = [waves[x["id"]] for x in full if x["group"] == r["group"] and x["id"] in waves]
            waves[r["id"]] = min(same) if same else 99
        r["wave"] = waves[r["id"]]
    manifest = [{k: v for k, v in r.items()} for r in full]
    if a.dry_run:
        print(json.dumps([m for m in manifest if m["id"] in {r["id"] for r in rows}], indent=1, ensure_ascii=False))
        return 0
    json.dump({"model": MODEL, "thinking": THINKING, "pi_version":
               subprocess.run(["pi", "--version"], capture_output=True, text=True,
                              stdin=subprocess.DEVNULL).stdout.strip(),
               "scenarios": manifest},
              open(os.path.join(a.out, "manifest.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    harness_root = os.path.join(os.environ.get("TMPDIR", "/tmp"), "pi-playbook-bench")

    # The identity handovers gate each set, so they run first and alone.
    gates = [r for r in rows if r["id"].endswith("ID-001")]
    # The rest follow the skill set's wave order, and each Project scenario runs beside
    # its skill twin rather than in its own later wave. The waves group scenarios for a
    # hand run, where one operator works one runtime at a time. Here every scenario has
    # its own sandbox, so only the first wave is an ordering rule.
    rest = sorted((r for r in rows if r not in gates),
                  key=lambda r: (waves.get("S" + r["id"][1:], r["wave"]), r["id"][1:], r["side"] != "skill"))
    # Twins run side by side so both packagings of one scenario meet the same gateway
    # load, which is what keeps a speed ratio between them fair.
    order, seen = [], set()
    for r in rest:
        if r["id"] in seen:
            continue
        order.append(r); seen.add(r["id"])
        twin = next((x for x in rest if x["id"] == r["twin"] and x["side"] != r["side"]), None)
        if twin and twin["id"] not in seen:
            order.append(twin); seen.add(twin["id"])

    results = []
    with cf.ThreadPoolExecutor(max_workers=a.jobs) as ex:
        for batch in (gates, order):
            futs = {ex.submit(run_scenario, system_dir, key, r, a.out, harness_root): r for r in batch}
            for f in cf.as_completed(futs):
                res = f.result()
                results.append(res)
                print(json.dumps(res), flush=True)
                if res["status"] == "isolation-failed":
                    print("isolation failed, stopping", file=sys.stderr)
                    return 2
    status_path = os.path.join(a.out, "run-status.json")
    merged = {}
    if os.path.exists(status_path):
        merged = {(r["id"], r["side"]): r for r in json.load(open(status_path))}
    merged.update({(r["id"], r["side"]): r for r in results})
    json.dump(sorted(merged.values(), key=lambda r: (r["side"], r["id"])), open(status_path, "w"), indent=1)
    return 1 if any(r["status"] != "ok" for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
