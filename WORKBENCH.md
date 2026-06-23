# build-room-visuals workbench

## 2026-06-22 - Scrub black-box treatment from F&F Mon kickoff deck

Applied the no-black-box rule to `facilitator/ff-mon-kickoff.html`. Slide 8 (Agreements) had three `background:#1a1a1a` cards holding real content (Presence, Teamwork, Positive Possibility). Rewrote to the standard light-airy bordered card pattern from `_template/components.html` (white background, 2px black border, dark heading, gray body). Content preserved verbatim. Slide 12 inspected: no black-box container present, just an agenda list and a "Let's go." punchline. No change needed there. Committed and pushed to origin/main for GitHub Pages.

[DECISION] Kept slide 12 untouched. The forever-rule diagnostic flags filler dressed up by dramatic containers; slide 12 has neither a container nor filler.
