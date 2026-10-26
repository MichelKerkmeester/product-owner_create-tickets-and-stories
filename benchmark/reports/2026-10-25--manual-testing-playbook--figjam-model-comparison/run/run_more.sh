#!/bin/bash
# Run the seven board-quality scenarios on GPT 6 Luna through Codex and Claude Opus 5.5
# through Claude Code, one run at a time, the same way run_compare.sh runs the Devin models.
# The two models alternate which goes first per scenario.
# Usage: run_more.sh <system dir> <run folder> <file key> [ID ...]
set -u
SYS="$1"; OUT="$2"; KEY="$3"; shift 3
HERE="$(cd "$(dirname "$0")" && pwd)"
IDS=("$@")
[ ${#IDS[@]} -eq 0 ] && IDS=(FJ-022 FJ-023 FJ-024 FJ-025 FJ-026 FJ-027 FJ-028)
LABELS=(luna opus-low)
MODELS=(codex:gpt-6-luna:max claude:claude-opus-5-5:low)
mkdir -p "$OUT/stdout"
i=0
for id in "${IDS[@]}"; do
  for k in 0 1; do
    j=$(( (i + k) % 2 ))
    label="${LABELS[$j]}"
    # A run that already finished keeps its result, so the batch resumes where it stopped
    if ls "$OUT/skill/$label/$id - "*/meta.json >/dev/null 2>&1; then
      echo "$id $label skipped, already run"
      continue
    fi
    echo "$id $label start $(date -u +%H:%M:%S)"
    python3 "$HERE/adaptive_compare.py" "$SYS" "$OUT" "$label" "${MODELS[$j]}" "$id" "$KEY" \
      > "$OUT/stdout/$id-$label.txt" 2>&1
    echo "$id $label exit $? $(date -u +%H:%M:%S)"
  done
  i=$(( i + 1 ))
done
