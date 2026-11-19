#!/usr/bin/env python3
"""Held-out generalisation probe for the Product Owner router.

Routes every probe string through benchmark/router/route_contract.py and
reports the resolved intent, shape, source and confidence beside the intent a
reader would expect, so correctness can be judged rather than only counted.
The probe strings are deliberately absent from fixtures.json and
differential_corpus.json: once a probe becomes a fixture it stops measuring
generalisation and starts measuring memorisation. The guard strings are the
opposite, restating inputs the fixtures already pin so an excluded term or a
framing precedence that regresses fails in both places.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROUTER = HERE.parents[2] / "AI Systems" / "Product Owner" / "benchmark" / "router"
sys.path.insert(0, str(ROUTER))

import route_contract as rc  # noqa: E402


def run(rows, label):
    fallbacks = 0
    wrong = 0
    print(f"\n== {label} ==")
    for row in rows:
        obj = rc.route_request(row["input"])
        intent, shape, source = obj["intent"], obj["shape"], obj["source"]
        conf = obj["confidence"]
        is_fallback = source in ("fallback", "quick-fallback") or intent == "INTERACTIVE"
        ok = intent == row["expect_intent"] and shape == row["expect_shape"]
        if is_fallback and row["expect_intent"] != "INTERACTIVE":
            fallbacks += 1
        if not ok:
            wrong += 1
        mark = "ok " if ok else "MISS"
        conf_s = "-" if conf is None else f"{conf:.2f}"
        print(f"  {mark} {intent:<12} shape={str(shape):<6} src={source:<14} conf={conf_s}  {row['input']}")
    print(f"  -- {label}: {len(rows) - wrong}/{len(rows)} correct, {fallbacks} fallback")
    return len(rows), wrong, fallbacks


def main():
    data = json.loads((HERE / "probe-set.json").read_text(encoding="utf-8"))
    total, wrong, fallbacks = run(data["probes"], "probe set")
    g_total, g_wrong, _ = run(data["guards"], "guards")
    print(f"\nPROBE {total - wrong}/{total} correct, {fallbacks} fallback")
    print(f"GUARD {g_total - g_wrong}/{g_total} correct")
    return 0 if (wrong == 0 and g_wrong == 0) else 1


if __name__ == "__main__":
    sys.exit(main())
