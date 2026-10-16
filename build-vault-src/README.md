# Build Vault source

The public page `build-vault.html` is rendered from this folder:

    python3 scripts/build-vault.py

- `alex-builds.json`: Alex's own builds (tagged "Alex's build", shown first, newest `logged` date first).
- `member-builds.json`: member builds, seeded 2026-10-16 from the Google Sheet "Humans v Robots Member Builds (Index)", each with `flow` and `integrations` added.
- `template.html`: the page shell.

## Log a build

Add an object to `alex-builds.json` (or `member-builds.json`) with:
`title, what_it_does, why, builder, where, category, tools[], demo_url, logged (YYYY-MM-DD), starter_prompt`,
plus:

- `integrations`: what someone has to connect, each with what it's for, e.g. "Call recorder API key, to pull transcripts (Fathom)".
- `flow`: the main workflow as 3 to 6 generic role boxes, brand examples under each, e.g.
  `{"role": "Call recorder", "eg": "Fathom, Otter"}`. Roles never name a brand; swap the fillings, keep the boxes.

Then run the script and push. No em dashes (the script refuses them).

Note: the laptop renderer (my-work/scripts/build-vault.py) only writes the gated copy; don't copy its output over this page, or the flows and Alex's builds disappear.
