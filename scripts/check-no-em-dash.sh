#!/usr/bin/env bash
#
# check-no-em-dash.sh - House-style lint gate.
#
# House style BANS the em dash character (U+2014) in all visible/human-readable
# copy. This script scans *.md, *.json, and *.js files and fails (exit 1) if any
# em dash remains in human-readable copy.
#
# SCOPE NOTE: *.html is intentionally NOT scanned here. HTML has richer excluded
# contexts (<script>/<style> blocks, <!-- comments -->, <code>/<pre> samples,
# attribute values) that need a proper classifying parser; that surface is owned
# by the BUIL-001 house-style pass, not this lightweight grep-based gate.
#
# EXCLUDED contexts (an em dash there is tolerated, kept verbatim):
#   - Markdown fenced code blocks (``` ... ```)
#   - Markdown inline code spans (`...`)
#   - files whose path contains "_archived"
#
# Dependencies: bash, grep, awk only (no package manager needed).
#
# Usage:
#   bash scripts/check-no-em-dash.sh          # scan repo from its root
#
# Wire as a git pre-commit hook (optional):
#   ln -s ../../scripts/check-no-em-dash.sh .git/hooks/pre-commit
#   chmod +x .git/hooks/pre-commit
#
# Exit codes: 0 = clean, 1 = offending em dash(es) found (file:line printed).

set -euo pipefail

# Resolve repo root as the parent of this script's directory.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT"

DASH=$(printf '\xe2\x80\x94')   # U+2014 EM DASH
found=0

# Collect candidate files, excluding archived-prefixed paths.
while IFS= read -r file; do
  case "$file" in
    *_archived*) continue ;;
  esac

  # Blank out excluded regions while preserving line numbers, then grep.
  # - Fenced code blocks: everything between ``` fences (fences included).
  # - Inline code spans: the text between backticks on a line.
  offenders=$(awk -v dash="$DASH" '
    BEGIN { infence = 0 }
    {
      line = $0
      # Toggle fenced-code state on lines that open/close a fence.
      if (line ~ /^[[:space:]]*```/) {
        infence = !infence
        next   # fence line itself is excluded
      }
      if (infence) { next }   # inside fenced block: excluded
      # Strip inline code spans (paired backticks) so em dashes inside them
      # are not counted.
      gsub(/`[^`]*`/, "", line)
      if (index(line, dash) > 0) {
        printf "%s:%d:%s\n", FILENAME, FNR, $0
      }
    }
  ' "$file") || true

  if [ -n "$offenders" ]; then
    echo "$offenders"
    found=1
  fi
done < <(find . -type f \( -name '*.md' -o -name '*.json' -o -name '*.js' \) -not -path '*/.git/*')

if [ "$found" -ne 0 ]; then
  echo ""
  echo "check-no-em-dash: em dash (U+2014) found in human-readable copy (see above)." >&2
  echo "Rewrite into a comma, period + new sentence, colon, or parentheses - never a hyphen or en dash." >&2
  exit 1
fi

echo "check-no-em-dash: OK - no em dashes in human-readable copy."
