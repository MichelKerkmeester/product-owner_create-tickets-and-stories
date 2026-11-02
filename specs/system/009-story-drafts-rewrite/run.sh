#!/usr/bin/env bash
# Rewrite every draft as a full Story with DeepSeek V4 Flash at max thinking on
# the llmgateway provider. Three lanes run at once because each rewrite is
# several minutes and the folders are independent. The prompt is what a person
# would type, routed through the agent router.
ROOT="/Users/michelkerkmeester/MEGA/Development/AI Systems/AI Systems"
OUT="$(dirname "$0")"; R="$OUT/results.tsv"
printf "lane\tseconds\texit\tfile\n" > "$R"
lane() {
  local lane="$1"; shift
  local n=0
  for f in "$@"; do
    n=$((n+1)); local log="$OUT/lane$lane-$n.txt"
    local s e secs rc
    s=$(perl -MTime::HiRes=time -e 'print time')
    ( cd "$ROOT" && pi -p --provider llmgateway --model deepseek-v4-flash:max -- \
      "/agent-router product owner \$story rewrite the story draft at \"$f\" as a full Story in the current house format, using that draft and the context.md beside it if there is one as the only source. Overwrite that exact file path with the finished Story, do not write a numbered export. The screenshots in that folder get embedded in ClickUp later, so the Story must not reference any of them." \
      < /dev/null ) > "$log" 2>&1
    rc=$?
    e=$(perl -MTime::HiRes=time -e 'print time')
    secs=$(perl -e "printf '%.1f', $e-$s")
    printf "%s\t%s\t%s\t%s\n" "$lane" "$secs" "$rc" "$f" >> "$R"
    echo "[lane$lane #$n] ${secs}s exit=$rc $(basename "$f")"
  done
}
ALL=(); while IFS= read -r line; do [ -n "$line" ] && ALL+=("$line"); done < "$OUT/files.txt"
A=(); B=(); C=()
for i in "${!ALL[@]}"; do case $((i % 3)) in 0) A+=("${ALL[$i]}");; 1) B+=("${ALL[$i]}");; 2) C+=("${ALL[$i]}");; esac; done
lane 1 "${A[@]}" & lane 2 "${B[@]}" & lane 3 "${C[@]}" &
wait
echo complete
