# build-room-visuals: rules for every HTML page

These pages are public (GitHub Pages) and people open them on their phones.

## Mobile first (Alex, 2026-10-24)
Every new or edited page must read well on a phone:
- Start the file with `<!doctype html>`, `<html lang="en">`, `<meta charset="utf-8">` and
  `<meta name="viewport" content="width=device-width, initial-scale=1">`. Without the viewport tag
  phones show the shrunken desktop layout. This was the Build Vault bug.
- One column under 600px. Use `max-width` + `padding-inline` (16-20px), and no fixed widths wider than the screen.
- Long rows of chips/buttons/tabs: scroll sideways in one row on mobile (`flex-wrap:nowrap; overflow-x:auto`) instead of stacking.
- Body text at least 15px, tap targets at least 40px tall.
- Check it at 390px wide before pushing: `document.documentElement.scrollWidth` must equal the window width (no sideways scroll).
- Fixed 16:9 slide decks are exempt; mark them with `<!-- desktop-only: slide deck -->` near the top.
- Lint: `bash scripts/check-mobile.sh` lists pages that miss the viewport tag and aren't marked desktop-only.

## House style
- No em dashes (`bash scripts/check-no-em-dash.sh`).
- Brand is "Humans V Robots". Times for customers are "New York time".

## Build Vault
Rendered from `build-vault-src/` by `python3 scripts/build-vault.py`; see `build-vault-src/README.md`.
