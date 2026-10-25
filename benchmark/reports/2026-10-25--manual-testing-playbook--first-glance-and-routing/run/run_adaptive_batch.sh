#!/bin/bash
# Run several scenarios through adaptive_scenario.py, three at a time.
# Each scenario has its own sandbox and session folder, so parallel runs stay isolated.
# Usage: run_adaptive_batch.sh <system dir> <run folder> <file key> ID [ID ...]
set -u
SYS="$1"; OUT="$2"; KEY="$3"; shift 3
HERE="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$OUT"
printf '%s\n' "$@" | xargs -P 3 -I{} sh -c \
  'python3 "$0/adaptive_scenario.py" "$1" "$2" {} "$3" > "$2/{}.stdout.txt" 2>&1; echo "{} exit $?"' \
  "$HERE" "$SYS" "$OUT" "$KEY"
