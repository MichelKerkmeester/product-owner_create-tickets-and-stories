#!/bin/bash
# Run the seven board-quality scenarios on three Devin models, one run at a time.
# Every run writes to one shared FigJam file, so runs never overlap. Each scenario
# runs on all three models back to back, and the model order rotates per scenario,
# so no model always meets the busiest page.
# Usage: run_compare.sh <system dir> <run folder> <file key> [ID ...]
set -u
SYS="$1"; OUT="$2"; KEY="$3"; shift 3
HERE="$(cd "$(dirname "$0")" && pwd)"
IDS=("$@")
[ ${#IDS[@]} -eq 0 ] && IDS=(FJ-022 FJ-023 FJ-024 FJ-025 FJ-026 FJ-027 FJ-028)
LABELS=(deepseek glm swe)
MODELS=(deepseek-v4-1-flash-1017-max glm-5-3-flash-max swe-2-max)
mkdir -p "$OUT/stdout"
i=0
for id in "${IDS[@]}"; do
  for k in 0 1 2; do
    j=$(( (i + k) % 3 ))
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
