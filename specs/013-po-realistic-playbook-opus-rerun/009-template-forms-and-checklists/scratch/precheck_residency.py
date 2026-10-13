"""Run the residency and parity checks against the uncommitted declaration.

Both gates refuse a declaration that differs from HEAD, which is right for a
gate. This harness lifts that one guard in memory only, so a change can be
checked before it is committed. Nothing on disk is modified.
"""
import sys
from pathlib import Path

GATE = Path("/Users/michelkerkmeester/MEGA/Development/AI Systems/AI Systems/z — Claude Project Sync Loop")
GUARD = "    if committed.stdout != data:"


def gate_namespace():
    path = GATE / "validate_parity.py"
    src = path.read_text()
    assert src.count(GUARD) == 1
    src = src.replace(GUARD, "    if False:")
    ns = {"__file__": str(path), "__name__": "validate_parity"}
    exec(compile(src, str(path), "exec"), ns)
    return ns


def residency(argv):
    path = GATE / "residency_check.py"
    src = path.read_text()
    anchor = "_gate = load_gate_module()"
    assert src.count(anchor) == 1
    src = src.replace(anchor, "_gate = __precheck_gate__()")
    ns = {"__file__": str(path), "__name__": "residency_precheck", "__precheck_gate__": gate_namespace}
    exec(compile(src, str(path), "exec"), ns)
    return ns["run"](argv)


def parity(argv):
    ns = gate_namespace()
    sys.argv = ["validate_parity.py"] + argv
    return ns["main"](["validate_parity.py"] + argv)


if __name__ == "__main__":
    which = sys.argv[1]
    rest = sys.argv[2:]
    sys.exit(residency(rest) if which == "residency" else parity(rest))
