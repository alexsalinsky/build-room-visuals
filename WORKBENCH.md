# build-room-visuals workbench

## 2026-06-23 - Credentials hygiene: ported static page to teach-from deck

Shipped `credentials-hygiene-deck.html` as a Build Room style 8-scene click-through deck mirroring the static `credentials-hygiene.html` content. Scenes: title + floor rule, the .env pattern, .gitignore (order matters), edit-it-yourself (why keys leak into transcripts), Do/Don't grid, leak rotation (with the 3 provider links and rotation order warn box), worked example (3 files at root + Python loader), close. Used the standard deck scaffold (tokens.css, glassy floating HUD, swipe + arrow + click nav, 96px bottom padding on slide-wrap). No black-box treatment, no em dashes, no audience-participation prompts. Footer middle dot. Thesis line omitted (didn't land naturally in a setup deck).

[DECISION] Kept BOTH the static page and the deck. Static = reference (link from Skool, read once). Deck = teach-from for cohort sessions. Updated `index.html` and `build-room-resources.html` to show two cards: "(Deck)" and "(Reference)". Alex can flip to deck-only if he prefers later.

Wired into resource library (`index.html` + `build-room-resources.html`), live at https://alexsalinsky.github.io/build-room-visuals/credentials-hygiene-deck.html after push.

## 2026-06-22 - Scrub black-box treatment from F&F Mon kickoff deck

Applied the no-black-box rule to `facilitator/ff-mon-kickoff.html`. Slide 8 (Agreements) had three `background:#1a1a1a` cards holding real content (Presence, Teamwork, Positive Possibility). Rewrote to the standard light-airy bordered card pattern from `_template/components.html` (white background, 2px black border, dark heading, gray body). Content preserved verbatim. Slide 12 inspected: no black-box container present, just an agenda list and a "Let's go." punchline. No change needed there. Committed and pushed to origin/main for GitHub Pages.

[DECISION] Kept slide 12 untouched. The forever-rule diagnostic flags filler dressed up by dramatic containers; slide 12 has neither a container nor filler.
