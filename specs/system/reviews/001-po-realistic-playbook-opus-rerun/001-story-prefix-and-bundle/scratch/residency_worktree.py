#!/usr/bin/env python3
"""Pre-commit signal only, never the gate. Runs residency_check.check_system over
the working-copy declaration, which the real gate refuses until it is committed."""
import sys, glob, os
from pathlib import Path
sys.dont_write_bytecode = True
root = Path(__file__).resolve().parents[4]
sl = Path(glob.glob(str(root / "AI Systems" / "z*Sync Loop"))[0])
ns = {"__file__": str(sl / "residency_check.py"), "__name__": "residency_check"}
exec(compile((sl / "residency_check.py").read_text("utf-8"), str(sl / "residency_check.py"), "exec"), ns)
print("gate refusal as expected:", (ns["DECLARATION_PROBLEM"] or "none")[-60:])
decl_ns = {"__file__": str(sl / "systems.py"), "__name__": "systems"}
sys.path.insert(0, str(sl))
exec(compile((sl / "systems.py").read_text("utf-8"), str(sl / "systems.py"), "exec"), decl_ns)
ns["SYSTEMS"] = decl_ns["SYSTEMS"]
system_id = sys.argv[1] if len(sys.argv) > 1 else "product-owner"
findings = ns["check_system"](system_id, decl_ns["SYSTEMS"][system_id])
for f in findings: print(f)
print(f"working-copy residency harness: {len(findings)} finding(s) for {system_id}")
sys.exit(1 if findings else 0)
