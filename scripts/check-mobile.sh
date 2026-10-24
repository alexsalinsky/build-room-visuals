#!/usr/bin/env bash
# check-mobile.sh - lists HTML pages that will render as a shrunken desktop page on phones:
# no <meta name="viewport"> and not marked <!-- desktop-only --> (fixed slide decks).
# Exit 1 if any are found. See CLAUDE.md "Mobile first".
set -uo pipefail
cd "$(dirname "$0")/.."
bad=0
while IFS= read -r f; do
  grep -q 'name="viewport"' "$f" && continue
  grep -q 'desktop-only' "$f" && continue
  echo "no viewport: $f"; bad=1
done < <(find . -name '*.html' -not -path './.git/*' -not -path '*_archived*' | sort)
exit $bad
