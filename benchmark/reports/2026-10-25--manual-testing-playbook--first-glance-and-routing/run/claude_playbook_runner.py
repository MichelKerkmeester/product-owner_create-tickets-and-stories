#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: CLAUDE CODE PLAYBOOK RUNNER
# ───────────────────────────────────────────────────────────────

"""Run Product Owner FigJam scenarios through the Claude Code CLI, skill side only.

The Claude Code port of oc2_playbook_runner.py beside it, for days the gateway that
OpenCode runs on is out of quota. The playbook loader, the sandbox builder, the
isolation proof, the scenario loop and the redaction are that runner's own, imported
rather than copied, so a result here differs from one there only in the harness.

Claude Code reads CLAUDE.md where OpenCode reads AGENTS.md, so each sandbox gains a
CLAUDE.md that imports its AGENTS.md. Only project settings load, which keeps the
operator's own instructions, settings and hooks out of every scenario, and the only
MCP server is Figma's hosted one, authenticated once under the name figma-remote.

Usage:
  claude_playbook_runner.py --system <system dir> --out <run folder> --ids ID,ID
                            [--jobs N] [--file-key KEY] [--new-file-ids ID,ID]

Exit codes:
  0   every scenario ran, whatever its verdict will be
  1   one or more scenarios could not be run after retries
  2   isolation failed or the system is not where it was named
  64  usage
"""
import argparse
import concurrent.futures as cf
import json
import os
import re
import subprocess
import sys
import threading
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import oc2_playbook_runner as base  # noqa: E402

# ───────────────────────────────────────────────────────────────
# 1. CONFIGURATION
# ───────────────────────────────────────────────────────────────

MODEL = "claude-sonnet-5-5"
THINKING = "high"
CLAUDE_BIN = "claude"
# The OAuth login is keyed to this server name, so the sandbox config repeats it exactly
FIGMA_MCP = {"mcpServers": {"figma-remote": {"type": "http", "url": "https://mcp.figma.com/mcp"}}}
# The skill runtime's tools in Claude Code's names. ToolSearch stays, because the Figma
# tools arrive deferred and cannot be called until it loads them.
SKILL_TOOLS = ["Read", "Bash", "Edit", "Write", "Glob", "Grep", "ToolSearch"]

base.MODEL = MODEL
base.THINKING = THINKING
_build = base.build


def project_dir_name(path):
    """The folder name Claude Code files a working directory's sessions and scratch under."""
    return re.sub(r"[^A-Za-z0-9]", "-", os.path.realpath(path))


# ───────────────────────────────────────────────────────────────
# 2. SANDBOX
# ───────────────────────────────────────────────────────────────

def build(system_dir, side, scratch, seed_export):
    """The OpenCode sandbox, with a CLAUDE.md in place of the OpenCode config."""
    _build(system_dir, side, scratch, seed_export)
    oc = os.path.join(scratch, "opencode.json")
    if os.path.exists(oc):
        os.remove(oc)
    with open(os.path.join(scratch, "CLAUDE.md"), "w", encoding="utf-8") as fh:
        fh.write("@AGENTS.md\n")
    json.dump(FIGMA_MCP, open(os.path.join(scratch, ".figma-mcp.json"), "w"), indent=1)


def seatbelt(scratch, session_dir, deny_roots):
    """The OpenCode runner's profile, with Claude Code's own per-project folders allowed back.

    Claude Code files each session under ~/.claude/projects and its tool output under the
    per-user temp folder, both named after the working directory. Every other project's
    transcripts stay refused, since they hold the playbooks and earlier replies."""
    q = lambda p: '"' + os.path.realpath(p).replace('"', '\\"') + '"'
    name = project_dir_name(scratch)
    own = [os.path.expanduser(f"~/.claude/projects/{name}"), f"/private/tmp/claude-{os.getuid()}/{name}"]
    for d in own:
        os.makedirs(d, exist_ok=True)
    profile = base.seatbelt(scratch, session_dir, deny_roots)
    # Startup creates the temp root with mkdir -p, which fails on a folder it cannot stat
    parents = " ".join(f"(literal {q(os.path.dirname(d))})" for d in own)
    return (profile + f"(allow file-read* {parents})"
            "(allow file-read* file-write* " + " ".join(f"(subpath {q(d)})" for d in own) + ")")


def deny_roots(system_dir, harness_root):
    """Every sandbox, the repository, every Claude Code transcript and every temp scratch."""
    repo = os.path.dirname(os.path.dirname(os.path.realpath(system_dir)))
    return [harness_root, repo, os.path.expanduser("~/.claude/projects"),
            f"/private/tmp/claude-{os.getuid()}"]


# ───────────────────────────────────────────────────────────────
# 3. ONE TURN
# ───────────────────────────────────────────────────────────────

def run_turn(scratch, session_dir, session_id, tools, prompt, events_path, deny_roots):
    """Run one Claude Code turn in the sandbox and return its parsed run record."""
    cmd = ["sandbox-exec", "-p", seatbelt(scratch, session_dir, deny_roots),
           CLAUDE_BIN, "-p", prompt, "--model", MODEL, "--effort", THINKING,
           "--output-format", "stream-json", "--verbose",
           "--setting-sources", "project", "--dangerously-skip-permissions",
           "--strict-mcp-config", "--mcp-config", os.path.join(scratch, ".figma-mcp.json"),
           "--tools", ",".join(SKILL_TOOLS)]
    if session_id:
        cmd += ["--resume", session_id]
    t0 = time.time()
    status = "ok"
    marks = []
    timed_out = threading.Event()
    err_path = events_path.replace(".jsonl", ".stderr.txt")
    with open(events_path, "w", encoding="utf-8") as out, \
         open(err_path, "w", encoding="utf-8") as err:
        p = subprocess.Popen(cmd, cwd=scratch, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                             stderr=err, text=True, bufsize=1, env=dict(os.environ, PWD=scratch))
        timer = threading.Timer(base.TURN_TIMEOUT_S, lambda: (timed_out.set(), p.kill()))
        timer.start()
        for line in p.stdout:
            out.write(line)
            marks.append(time.time() - t0)
        rc = p.wait()
        timer.cancel()
    if timed_out.is_set():
        status = "timeout"
    r = parse_events(events_path, rc, status, time.time() - t0)
    if marks:
        r["startup_s"] = round(marks[0], 2)
        r["model_s"] = round(marks[-1] - marks[0], 2)
    return r


def parse_events(path, rc, status, wall):
    """The run record parsed from one Claude Code stream-json event stream."""
    r = {"rc": rc, "status": status, "wall_s": round(wall, 2), "reply": "", "transcript": [],
         "tool_calls": 0, "tools_used": [], "input_tokens": 0, "output_tokens": 0,
         "reasoning_tokens": 0, "cost_usd": 0.0, "model_s": None, "startup_s": None, "stop_reason": None,
         "response_models": [MODEL], "session_id": None, "inner_calls": [], "mcp_servers": None}
    names, final, last_text = {}, None, ""
    for line in open(path, encoding="utf-8", errors="ignore"):
        try:
            e = json.loads(line)
        except ValueError:
            continue
        r["session_id"] = r["session_id"] or e.get("session_id") or None
        kind = e.get("type")
        if kind == "system" and e.get("subtype") == "init":
            r["mcp_servers"] = e.get("mcp_servers")
        elif kind == "assistant":
            texts = []
            for c in (e.get("message") or {}).get("content") or []:
                if c.get("type") == "text":
                    texts.append(c.get("text", ""))
                    r["transcript"].append({"kind": "text", "text": c.get("text", "")})
                elif c.get("type") == "tool_use":
                    names[c.get("id")] = c.get("name")
                    r["tool_calls"] += 1
                    r["tools_used"].append(c.get("name"))
                    if (c.get("name") or "").startswith("mcp__"):
                        r["inner_calls"].append(c.get("name"))
                    r["transcript"].append({"kind": "call", "name": c.get("name"), "args": c.get("input")})
            if texts:
                last_text = "\n".join(texts)
        elif kind == "user":
            for c in (e.get("message") or {}).get("content") or []:
                if isinstance(c, dict) and c.get("type") == "tool_result":
                    body = c.get("content")
                    if isinstance(body, list):
                        body = "\n".join(x.get("text", "") for x in body if isinstance(x, dict))
                    r["transcript"].append({"kind": "result", "name": names.get(c.get("tool_use_id")),
                                            "error": bool(c.get("is_error")), "text": str(body or "")[:4000]})
        elif kind == "result":
            final = e
    if final:
        u = final.get("usage") or {}
        r["input_tokens"] = (u.get("input_tokens", 0) or 0) + (u.get("cache_read_input_tokens", 0) or 0) \
            + (u.get("cache_creation_input_tokens", 0) or 0)
        r["output_tokens"] = u.get("output_tokens", 0) or 0
        r["reasoning_tokens"] = ((u.get("output_tokens_details") or {}).get("thinking_tokens", 0)) or 0
        r["cost_usd"] = final.get("total_cost_usd", 0) or 0
        r["stop_reason"] = final.get("stop_reason")
        r["reply"] = final.get("result") or last_text
        if final.get("is_error"):
            r["status"] = "error"
            r["errors"] = [final.get("subtype") or "error", str(final.get("result") or "")[:500]]
    else:
        r["reply"] = last_text
        if r["status"] == "ok":
            r["status"] = "error"
            r["errors"] = ["no result event"]
    if r["status"] == "ok" and r["stop_reason"] == "max_tokens":
        r["status"] = "stop-length"
    elif r["status"] == "ok" and not r["reply"].strip():
        r["status"] = "empty-reply"
    return r


# The scenario loop is the OpenCode runner's, so its turn and sandbox calls are pointed here
base.build = build
base.run_turn = run_turn
base.deny_roots = deny_roots


# ───────────────────────────────────────────────────────────────
# 4. MAIN
# ───────────────────────────────────────────────────────────────

def main():
    """Run the named scenarios and return the process exit status."""
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--system", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--ids", required=True)
    ap.add_argument("--jobs", type=int, default=3)
    ap.add_argument("--file-key", default="")
    ap.add_argument("--new-file-ids", default="")
    try:
        a = ap.parse_args()
    except SystemExit:
        return 64
    system_dir = os.path.abspath(a.system)
    key = base.SYSTEM_KEYS.get(os.path.basename(system_dir.rstrip("/")))
    if not key or not os.path.isdir(system_dir):
        print(f"no known system at {system_dir}", file=sys.stderr)
        return 2
    want = a.ids.split(",")
    rows = [r for r in base.load_playbook(system_dir, key) if r["id"] in want and r["side"] == "skill"]
    for r in rows:
        r["tools"] = SKILL_TOOLS
    os.makedirs(a.out, exist_ok=True)
    version = subprocess.run([CLAUDE_BIN, "--version"], capture_output=True, text=True,
                             stdin=subprocess.DEVNULL).stdout.strip()
    json.dump({"model": MODEL, "thinking": THINKING, "runtime": "claude-code", "runtime_version": version,
               # A run folder an OpenCode run already filled keeps that run's manifest
               "scenarios": rows}, open(os.path.join(a.out, "manifest-claude.json"), "w", encoding="utf-8"),
              indent=1, ensure_ascii=False)
    harness_root = os.path.join(os.environ.get("TMPDIR", "/tmp"), "claude-sonnet-playbook-bench")
    order = sorted(rows, key=lambda r: want.index(r["id"]))
    results = []
    with cf.ThreadPoolExecutor(max_workers=a.jobs) as ex:
        futs = {ex.submit(base.run_scenario, system_dir, key, r, a.out, harness_root,
                          base.pin_for(r, a)): r for r in order}
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
