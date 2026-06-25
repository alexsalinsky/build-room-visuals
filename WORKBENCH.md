# build-room-visuals workbench

## 2026-06-24 - LLM Builder BPs page: add "What is this?" before install

Follow-up pass on `llm-builder-bps.html`. Previous rewrite cut the "what / why" framing in the push to make the install path crystal clear. People landed on the page learning HOW to install without knowing WHAT they were installing.

**What changed:**
- Added new "What is this?" section ABOVE the install steps. One-sentence definition (standing rules for LLM-driven build sessions: file structure, doc discipline, decision logging, wrap rituals). 2-line "why it matters" (builds get messy, stacks drift, next Monday your AI has no context).
- Moved the four-doc preview up from "What's inside the file" (after install) to the new "What is this?" block (before install). Same content, better placement.
- Install steps still ONE path, button still prominent.

**Decisions:**
- [DECISION] Placed What/Why BEFORE install steps, not after. Install is the action; context is the prerequisite for taking that action.

**Files touched:** llm-builder-bps.html, WORKBENCH.md

---

## 2026-06-24 - LLM Builder BPs page rewrite: one path + skill-style MD

Rewrote `llm-builder-bps.html` and `llm-builder-bps/llm-builder-bps.md` so the resource has ONE clear use path and the MD teaches the LLM to apply the practices automatically (like Alex's `wrap` skill).

**What changed:**
- Killed Path A / Path B / Codex paths entirely. Replaced with single 3-step path: download MD, drop into LLM, tell it to install.
- HTML now leads with "How to use it" steps + prominent download button. Preview of the four-doc system stays as "what you're installing." Why-it-works kept.
- MD now opens with an "Install" block addressed to the assistant ("Best Practices installed. Active for every session."), then a "When to apply" trigger list (any build work, file modifications, decisions, wrap phrases), then a "How to stay applied" memory hint for context compression.
- Updated card description on `build-room-resources.html` + `index.html` to match the new "drop into your LLM and tell it to install" framing.

**Decisions:**
- [DECISION] Removed Path A/B/Codex entirely instead of light-editing. Alex was explicit: one path only, no "you could also" options. Optionality was the problem.
- [DECISION] MD opens addressed to the assistant, not the human. Matches the wrap-skill pattern Alex referenced. Human reads the HTML; the MD talks to the LLM.

**Still open:**
- None. Ship-ready.

**Files touched:** llm-builder-bps.html, llm-builder-bps/llm-builder-bps.md, build-room-resources.html, index.html, WORKBENCH.md

---

## 2026-06-23 - Credentials hygiene deck v2: fix tokens 404 + file-structure reframe

V2 pass on `credentials-hygiene-deck.html`. Real bugs on the live deck plus a content reframe.

Formatting bugs found and fixed:
- **Root cause of every "looks broken" symptom**: `_template/tokens.css` 404'd on GitHub Pages because Jekyll ignores underscore-prefixed dirs by default. Every `var(--br-*)` resolved to empty, so h1 fell back to 16px, `.floor` dark pill rendered transparent, etc. Inlined the tokens directly into the deck (matches the template's stated "portable if served outside the repo" intent).
- Em dash in `<title>` swapped for middle dot.
- Worked-example scene was overflowing the viewport (h2 colliding with section chip, bottom of `src/main.py` block cut off). Compacted code-block font and added explicit `margin-top` to clear the chip.
- Slide-wrap top padding bumped from 20px to 40px so chip + heading have breathing room across all 9 slides.

Reframe (the load-bearing ask): credential hygiene is a file-structure story. Built a reusable `tree()` function that renders the same project tree across multiple scenes with mode-based highlighting: yellow highlight on `.env` in "The Pattern", yellow on `.gitignore` in "Hide it from GitHub", strikethrough + dim on `.env` in "What git sees", **red danger background + 'PUSHED TO GITHUB' note on `.env` in the leak scene**, clean ok-green annotations in the close. Tree uses real monospace branch chars (├── │ └──), distinguishable from prose.

Also added a new scene 4: side-by-side `git status` before/after, with red `.env` showing as untracked on the "without" side and green `.gitignore` showing as untracked on the "with" side. The dimmed-out tree sits below to reinforce.

[DECISION] Deck went from 8 → 9 scenes (added the git-status before/after). Static reference page untouched per scope.

Verified all 9 scenes locally before pushing. Commit `e133cd2`. Live URL same: https://alexsalinsky.github.io/build-room-visuals/credentials-hygiene-deck.html.

## 2026-06-23 - Credentials hygiene: ported static page to teach-from deck

Shipped `credentials-hygiene-deck.html` as a Build Room style 8-scene click-through deck mirroring the static `credentials-hygiene.html` content. Scenes: title + floor rule, the .env pattern, .gitignore (order matters), edit-it-yourself (why keys leak into transcripts), Do/Don't grid, leak rotation (with the 3 provider links and rotation order warn box), worked example (3 files at root + Python loader), close. Used the standard deck scaffold (tokens.css, glassy floating HUD, swipe + arrow + click nav, 96px bottom padding on slide-wrap). No black-box treatment, no em dashes, no audience-participation prompts. Footer middle dot. Thesis line omitted (didn't land naturally in a setup deck).

[DECISION] Kept BOTH the static page and the deck. Static = reference (link from Skool, read once). Deck = teach-from for cohort sessions. Updated `index.html` and `build-room-resources.html` to show two cards: "(Deck)" and "(Reference)". Alex can flip to deck-only if he prefers later.

Wired into resource library (`index.html` + `build-room-resources.html`), live at https://alexsalinsky.github.io/build-room-visuals/credentials-hygiene-deck.html after push.

## 2026-06-22 - Scrub black-box treatment from F&F Mon kickoff deck

Applied the no-black-box rule to `facilitator/ff-mon-kickoff.html`. Slide 8 (Agreements) had three `background:#1a1a1a` cards holding real content (Presence, Teamwork, Positive Possibility). Rewrote to the standard light-airy bordered card pattern from `_template/components.html` (white background, 2px black border, dark heading, gray body). Content preserved verbatim. Slide 12 inspected: no black-box container present, just an agenda list and a "Let's go." punchline. No change needed there. Committed and pushed to origin/main for GitHub Pages.

[DECISION] Kept slide 12 untouched. The forever-rule diagnostic flags filler dressed up by dramatic containers; slide 12 has neither a container nor filler.
