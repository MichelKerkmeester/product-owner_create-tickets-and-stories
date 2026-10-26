#!/usr/bin/env python3
"""One turn on the Codex CLI or the Claude Code CLI, recorded the way the Devin runner records one.

The comparison grew from three Devin models to two more that Devin does not serve: GPT 6
Luna on Codex and Claude Opus 5.5 on Claude Code. Each turn here runs in the Devin
runner's own sandbox tree, inside the same seatbelt, with a config that holds only Figma's
hosted MCP server, and returns the record `devin_playbook_runner.parse_export` returns, so
`adaptive_compare.py` drives every model the same way.

A model id names its runtime: `codex:<model>:<effort>` or `claude:<model>:<effort>`.
"""
import json
import os
import re
import subprocess
import threading
import time

import devin_playbook_runner as dv

# The binary, because the operator's shell wraps codex in a function
CODEX_BIN = "/opt/homebrew/bin/codex"
CLAUDE_BIN = os.path.expanduser("~/.local/bin/claude")
# Holds only the ChatGPT login and a config that pre-approves the account's connected apps,
# so the operator's hooks, rules and voice file never reach a scenario. Codex reaches Figma
# through the Figma app on the ChatGPT account, served as `codex_apps`, whose tools are
# Figma's hosted MCP server under a `figma.` prefix. Without the approval line every
# `use_figma` call is refused, because `codex exec` cannot ask.
CODEX_HOME = os.path.join(os.environ.get("TMPDIR", "/tmp"), "codex-compare-home")
CODEX_CONFIG = """[apps._default]
default_tools_approval_mode = "approve"
destructive_enabled = true
open_world_enabled = true
"""
FIGMA_URL = "https://mcp.figma.com/mcp"
# The name the operator's Claude Code login for Figma is stored under, so the child reuses it
CLAUDE_FIGMA = "figma-remote"
URL = re.compile(r"https?://(?:www\.)?figma\.com/[^\s\"'<>)\]\\]+")
BOARD_ID = re.compile(r'boardId\\*"?\s*:\s*\\*"(\d+:\d+)')
HOME = os.path.expanduser("~")
# Claude Code keeps the operator's rules, skills and transcripts under ~/.claude. They stay
# denied, and only the session folders of this harness's own scenarios are allowed back.
CLAUDE_PRIVATE = ["CLAUDE.md", "projects", "transcripts", "history.jsonl", "skills", "agents",
                  "plans", "file-history", "sessions", "paste-cache", "plugins", "teams", "jobs"]


def runtime(model):
    """The runtime, model and effort a model id names, or None for a Devin model."""
    parts = model.split(":")
    return tuple(parts) if len(parts) == 3 and parts[0] in ("codex", "claude") else None


def seatbelt(scratch, session_dir, deny_roots, extra_allow=""):
    """The Devin runner's profile, with the runtime's own folders allowed back last."""
    base = dv.seatbelt(scratch, session_dir, deny_roots)
    return base + extra_allow


def record(rc, status, wall):
    return {"rc": rc, "status": status, "wall_s": round(wall, 2), "reply": "", "transcript": [],
            "tool_calls": 0, "tools_used": [], "input_tokens": 0, "output_tokens": 0,
            "cached_tokens": 0, "response_models": [], "session_id": None, "inner_calls": [],
            "composed": False, "boards": []}


def figma_call(r, tool, args, result):
    """Count one Figma call and read a composed board's id from its result."""
    tool = str(tool).split(".")[-1]
    r["inner_calls"].append(tool)
    if isinstance(args, str):
        try:
            args = json.loads(args)
        except ValueError:
            args = {"code": args}
    if tool == "use_figma":
        code = str((args or {}).get("code", ""))
        if "const MODEL" in code:
            r["composed"] = True
        r["boards"] += BOARD_ID.findall(str(result or ""))


def launch(cmd, scratch, session_dir, n, env, raw):
    """Run one turn's process with the runner's timeout, its stdout kept as the raw export."""
    t0 = time.time()
    timed_out = threading.Event()
    with open(raw, "w", encoding="utf-8") as out:
        p = subprocess.Popen(cmd, cwd=scratch, stdin=subprocess.DEVNULL, stdout=out,
                             stderr=open(os.path.join(session_dir, f"turn-{n}.stderr.txt"), "w"),
                             text=True, env=env)
        timer = threading.Timer(dv.TURN_TIMEOUT_S, lambda: (timed_out.set(), p.kill()))
        timer.start()
        rc = p.wait()
        timer.cancel()
    return rc, "timeout" if timed_out.is_set() else "ok", time.time() - t0


def redact_stream(text):
    """An event stream redacted without breaking its JSON lines.

    The Devin pattern `figma\.com/\S+` also takes an escaped quote or line break glued to a
    URL inside a JSON string, which left lines unparseable, so a stream uses the narrower
    URL pattern of `redact_run.py` before the rest of the Devin redaction. whoami also
    lists the account's plan keys, which neither names."""
    text = URL.sub("<figma-url>", text)
    text = dv.redact(text)
    return re.sub(r"\b(team|org|organization)::\d+", r"\1::<redacted>", text)


def finish(r, raw, dest, n):
    """Keep the redacted event stream beside the turn and settle the status."""
    text = redact_stream(open(raw, encoding="utf-8", errors="ignore").read())
    open(os.path.join(dest, f"export-turn-{n}.jsonl"), "w", encoding="utf-8").write(text)
    r["boards"] = list(dict.fromkeys(r["boards"]))
    if r["rc"] != 0 and r["status"] == "ok":
        r["status"] = "error"
    elif not r["reply"].strip() and r["status"] == "ok":
        r["status"] = "empty-reply"
    return r


def env_for(session_dir, scratch, **extra):
    tmp = os.path.join(session_dir, "tmp")
    os.makedirs(tmp, exist_ok=True)
    return dict(os.environ, PWD=scratch, TMPDIR=tmp, AI_SESSION_CHILD="1", **extra)


def codex_turn(spec, scratch, session_dir, session_id, prompt, n, dest, deny_roots):
    """One Codex turn. A later turn resumes the thread the first turn started."""
    _, model, effort = spec
    os.makedirs(CODEX_HOME, exist_ok=True)
    auth = os.path.join(CODEX_HOME, "auth.json")
    if not os.path.lexists(auth):
        os.symlink(os.path.join(HOME, ".codex", "auth.json"), auth)
    open(os.path.join(CODEX_HOME, "config.toml"), "w").write(CODEX_CONFIG)
    raw = os.path.join(session_dir, f"export-turn-{n}.jsonl")
    conf = ["-c", f'model="{model}"', "-c", f'model_reasoning_effort="{effort}"',
            "-c", 'service_tier="fast"',
            # Codex wraps each shell command in its own seatbelt, which macOS refuses inside the
            # runner's seatbelt with "sandbox_apply: Operation not permitted", so every command
            # failed and the first seven Luna runs never read the skill. The operator approved
            # turning Codex's sandbox off, leaving the runner's seatbelt to confine the child,
            # as it confined Devin in its dangerous permission mode.
            "--dangerously-bypass-approvals-and-sandbox", "--skip-git-repo-check", "--json"]
    sub = ["exec", "resume", session_id] if session_id else ["exec"]
    q = lambda p: '"' + os.path.realpath(p).replace('"', '\\"') + '"'
    allow = f"(allow file-read* file-write* (subpath {q(CODEX_HOME)}) (subpath {q(os.path.join(HOME, '.codex'))}))"
    cmd = ["sandbox-exec", "-p", seatbelt(scratch, session_dir, deny_roots, allow),
           CODEX_BIN, *sub, *conf, "--", prompt]
    rc, status, wall = launch(cmd, scratch, session_dir, n, env_for(session_dir, scratch, CODEX_HOME=CODEX_HOME), raw)
    r = record(rc, status, wall)
    r["response_models"] = [model]
    last = ""
    for line in open(raw, encoding="utf-8", errors="ignore"):
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        t = ev.get("type")
        if t == "thread.started":
            r["session_id"] = ev.get("thread_id")
        elif t == "turn.completed":
            u = ev.get("usage") or {}
            r["input_tokens"] += u.get("input_tokens", 0) or 0
            r["output_tokens"] += u.get("output_tokens", 0) or 0
            r["cached_tokens"] += u.get("cached_input_tokens", 0) or 0
        elif t == "item.completed":
            it = ev.get("item") or {}
            kind = it.get("type")
            if kind == "agent_message":
                last = it.get("text", "")
                r["transcript"].append({"kind": "text", "text": last})
            elif kind in ("mcp_tool_call", "command_execution", "file_change", "web_search"):
                name = it.get("tool") if kind == "mcp_tool_call" else kind
                args = it.get("arguments") if kind == "mcp_tool_call" else {
                    "command": it.get("command"), "changes": it.get("changes")}
                result = it.get("result") if kind == "mcp_tool_call" else it.get("aggregated_output")
                r["tool_calls"] += 1
                r["tools_used"].append(name)
                if kind == "mcp_tool_call":
                    if it.get("server") == "codex_apps" and str(it.get("tool", "")).startswith("figma."):
                        figma_call(r, it.get("tool"), it.get("arguments"), json.dumps(result))
                r["transcript"].append({"kind": "call", "name": name, "args": args})
                r["transcript"].append({"kind": "result", "name": name,
                                        "error": bool(it.get("error")) or it.get("status") == "failed",
                                        "text": str(it.get("error") or result or "")[:4000]})
    r["session_id"] = r["session_id"] or session_id
    r["reply"] = last
    return finish(r, raw, dest, n)


def claude_turn(spec, scratch, session_dir, session_id, prompt, n, dest, deny_roots, figma=True):
    """One Claude Code turn. The sandbox's AGENTS.md is appended to Claude Code's own system
    prompt, as Devin and Codex load it as the checkout's rule file."""
    _, model, effort = spec
    raw = os.path.join(session_dir, f"export-turn-{n}.jsonl")
    mcp = os.path.join(session_dir, "figma-mcp.json")
    # A scenario that needs no hosted Figma server, such as FJ-009, gets an empty server list, so the
    # child sees the route missing exactly as a user without the connector would.
    servers = {CLAUDE_FIGMA: {"type": "http", "url": FIGMA_URL}} if figma else {}
    json.dump({"mcpServers": servers}, open(mcp, "w"))
    claude_dir = os.path.join(HOME, ".claude")
    denied = deny_roots + [os.path.join(claude_dir, p) for p in CLAUDE_PRIVATE]
    # Claude Code files a session under ~/.claude/projects by its encoded working folder
    allow = ('(allow file-read* file-write* (regex #"^' + re.escape(os.path.join(claude_dir, "projects"))
             + '/[^/]*compare-bench"))')
    cmd = ["sandbox-exec", "-p", seatbelt(scratch, session_dir, denied, allow),
           CLAUDE_BIN, "-p", "--model", model, "--effort", effort, "--setting-sources", "",
           "--strict-mcp-config", "--mcp-config", mcp, "--permission-mode", "bypassPermissions",
           # Opus 5.5 low made new files past the pin naming the test file, first through
           # create_new_file and then through generate_diagram. With both withheld it drew
           # nothing and asked for a plan instead. The operator then allowed a new file in
           # the drafts of the Barter plan, so both are back and only generate_figma_design,
           # which makes a design file rather than a board, stays withheld.
           "--disallowedTools", f"mcp__{CLAUDE_FIGMA}__generate_figma_design",
           "--append-system-prompt-file", os.path.join(scratch, "AGENTS.md"),
           "--output-format", "stream-json", "--verbose"]
    if session_id:
        cmd += ["--resume", session_id]
    cmd += ["--", prompt]
    # Claude Code roots its own temp files at /tmp/claude-<uid>, which the seatbelt denies
    # because the operator's sessions keep theirs there
    env = env_for(session_dir, scratch, CLAUDE_CODE_TMPDIR=os.path.join(session_dir, "tmp"))
    rc, status, wall = launch(cmd, scratch, session_dir, n, env, raw)
    r = record(rc, status, wall)
    calls, last = {}, ""
    for line in open(raw, encoding="utf-8", errors="ignore"):
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        t = ev.get("type")
        if t == "system" and ev.get("subtype") == "init":
            r["session_id"] = ev.get("session_id")
        elif t == "assistant":
            msg = ev.get("message") or {}
            m = msg.get("model")
            if m and m not in r["response_models"]:
                r["response_models"].append(m)
            for b in msg.get("content") or []:
                if b.get("type") == "text" and b.get("text", "").strip():
                    r["transcript"].append({"kind": "text", "text": b["text"]})
                elif b.get("type") == "tool_use":
                    calls[b.get("id")] = b
                    r["tool_calls"] += 1
                    r["tools_used"].append(b.get("name"))
                    r["transcript"].append({"kind": "call", "name": b.get("name"), "args": b.get("input")})
        elif t == "user":
            for b in (ev.get("message") or {}).get("content") or []:
                if isinstance(b, dict) and b.get("type") == "tool_result":
                    call = calls.get(b.get("tool_use_id")) or {}
                    name = call.get("name", "")
                    text = json.dumps(b.get("content"))
                    if name.startswith(f"mcp__{CLAUDE_FIGMA}__"):
                        figma_call(r, name.split("__")[-1], call.get("input"), text)
                    r["transcript"].append({"kind": "result", "name": name, "error": bool(b.get("is_error")),
                                            "text": text[:4000]})
        elif t == "result":
            last = ev.get("result") or ""
            u = ev.get("usage") or {}
            r["input_tokens"] += (u.get("input_tokens", 0) or 0) + (u.get("cache_creation_input_tokens", 0) or 0)
            r["output_tokens"] += u.get("output_tokens", 0) or 0
            r["cached_tokens"] += u.get("cache_read_input_tokens", 0) or 0
            r["session_id"] = ev.get("session_id") or r["session_id"]
    r["session_id"] = r["session_id"] or session_id
    r["reply"] = last
    return finish(r, raw, dest, n)


def run_turn(spec, scratch, session_dir, session_id, prompt, n, dest, deny_roots, figma=True):
    """One turn on the runtime the model id names. A failed turn is retried as a whole
    attempt by the driver, as on Devin, because a turn may already have written a board.
    Only Claude Code runs without the hosted Figma server. Codex reaches it through the account's
    Figma app, and no way to switch that off for one run has been tried here."""
    if spec[0] == "codex":
        return codex_turn(spec, scratch, session_dir, session_id, prompt, n, dest, deny_roots)
    return claude_turn(spec, scratch, session_dir, session_id, prompt, n, dest, deny_roots, figma)
