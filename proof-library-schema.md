# Proof Library: Schema

Last updated: 2026-07-23

Single source of truth for the structure of `proof-library.json`. The static page at `proof-library.html` reads this JSON client-side. Anything that writes to the JSON (skills, workers, manual edits) MUST conform to the entry shape below.

This is the data layer for a future content-generation pipeline. Honest gaps (status=raw, null URLs) are more useful than fabricated entries.

---

## Entry shape

Each entry is a JSON object with these fields. Required unless marked optional.

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | string (kebab-case slug) | yes | Globally unique. Convention: `<cohort>-s<N>-<builder-slug>-<short-tag>` for wins, `<cohort>-<short-tag>` for everything else, e.g. `rpa-s2-david-zoom-downloader`, `nc17-thesis-line`. |
| `type` | enum | yes | One of: `clip`, `win`, `testimonial`, `lesson`, `screenshot`, `published`, `quote`. |
| `cohort` | enum | yes | One of: `rpa`, `ginger-rpa`, `dbalp`, `ff-mon`, `ff-thu`, `nc17`, `hvr2`, `dcmex`, `none`, `cross-cohort`, or a **consulting engagement slug** (see below). |
| `title` | string (one line) | yes | Short and concrete. The card headline. |
| `source_url` | string OR null | yes | Where this came from. Transcript file path (relative repo path is OK), Skool post URL, LinkedIn URL, Fathom URL. Null if unverified. |
| `media_url` | string OR null | yes | YouTube unlisted, Drive, direct file. Null if no media uploaded yet. Use TODO marker in `notes` when waiting on upload. |
| `thumbnail` | string OR null | yes | Path under `build-room-visuals/assets/proof/` or absolute URL. Null if none. |
| `quote` | string OR null | yes | The actual text. Markdown allowed. Null when the entry is purely a media reference (e.g. screenshot, video clip with no transcript line). |
| `attribution` | string OR null | yes | Person + cohort, e.g. "Kate (DBALP cohort)". Null for cross-cohort or facilitator-only entries. |
| `timestamp` | string OR null | yes | `HH:MM:SS` or `MM:SS` in the source transcript or video. Null if not applicable. |
| `tags` | array of strings | yes | Free-form. Examples: `first-brick`, `thesis`, `breakthrough`, `pivot`, `peer-teaching`, `live-demo`, `mid-session-extension`, `recovery`. Empty array allowed. |
| `status` | enum | yes | One of: `raw`, `cleared-for-public`, `live`, `featured`, `redacted`. Default is `raw`. See lifecycle below. |
| `date_captured` | string (YYYY-MM-DD) | yes | Date this entry was added to the library. Shown on each card as "Added: YYYY-MM-DD" and available as a sort option in the UI (default sort is Date added, newest first). |
| `date_cleared` | string OR null | yes | Date status moved past `raw`. Null until that happens. |
| `notes` | string | optional | Internal-use free-form. TODO markers, permission asks pending, sensitivity flags. |
| `do_not_share` | boolean | optional | Builder asked that this work not circulate. When `true`, the entry is excluded from every derived view at every tier (proof-library.html render, Build Vault internal and public) and is off-limits to content, outreach, and lookup skills. Absence means false. |
| `consent_note` | string | optional | Plain-language record of what the builder said about sharing and when, so future sessions don't rediscover the preference from transcripts. Can exist without `do_not_share` (e.g. "OK internally, never public"). |

---

## Field detail

### `id`

Globally unique kebab-case slug. Convention by type:

- **win**: `<cohort>-s<N>-<builder-slug>-<short-tag>`, e.g. `dbalp-s3-kate-missive-live`
- **clip**: `<cohort>-<short-tag>` or `<source>-<short-tag>`, e.g. `nc17-thesis-line`, `dbalp-s3-kate-applause`
- **published**: `<platform>-<slug-from-url>`, e.g. `linkedin-how-to-get-your-team-to-actually-use-ai`
- **testimonial** / **quote**: `<cohort>-<speaker-slug>-<short-tag>`, e.g. `ff-mon-ruben-on-purpose-on-track`
- **lesson**: `<cohort>-s<N>-<concept-slug>`, e.g. `cross-cohort-burn-the-thread`
- **screenshot**: `<cohort>-s<N>-<builder-slug>-screenshot-<N>`

If a builder appears multiple times in one session, append a discriminator: `-1`, `-2`, or a concept-tag.

### `type`

| Value | Use for |
|---|---|
| `clip` | Audio / video moment, transcript-grounded. Marketing-ready or near-ready. |
| `win` | Per-builder, per-session breakthrough from a debrief wins post. The primary debrief artifact. |
| `testimonial` | A participant said something quotable about the program. Permission status matters. |
| `lesson` | A teaching / framework / heuristic surfaced live in a session (cross-cohort value). |
| `screenshot` | Image-only proof: a dashboard, sidebar, deck, working tool. |
| `published` | Already shipped publicly (LinkedIn newsletter, podcast episode, talk recording). |
| `quote` | A noteworthy thing someone said that doesn't fit `testimonial` (e.g. a sponsor's offhand line, a builder's own framing of their work). |

### `cohort`

Use `cross-cohort` when the entry applies to multiple cohorts or to The Build Room as a whole (e.g. the thesis line). Use `none` for things outside any cohort context (e.g. Alex's own published article).

**Consulting engagements** (Centaur Digital, and any future direct-consulting client) use the client slug from `clients/` as the cohort value, e.g. `centaur`. `ginger-rpa` set the precedent for client-named values.

These proofs come from consulting work, not from people learning to build with AI, so they need to be separable from cohort proof. Two rules:

- Every consulting entry carries the `consulting` tag. That is the filter for "proof from client work."
- Every consulting entry also carries a **domain tag** naming what kind of proof it is: `founder-dependency`, `delegation`, `ops-systems`, `performance-reviews`, `engagement-outcome`. Add new ones as needed; these are not AI-building tags and shouldn't be forced into `first-brick` / `ship` / `deploy` vocabulary.

**Consent is different for consulting clients.** The blanket clip clearance covers Build Room cohort calls, NOT paying consulting clients. Consulting entries default to `raw` and stay there until the client says yes in writing. Anything containing performance commentary about a named employee never leaves local working files at all, regardless of status (see `feedback-client-facing-artifacts-no-perf`).

### `status`: lifecycle

| Value | Meaning |
|---|---|
| `raw` | Default. Captured but no permission asked, no public clearance, no media uploaded. Library shows but does not surface for promo. |
| `cleared-for-public` | Permission granted (testimonial form, explicit text consent, builder posted it themselves). Ready for repurposing. |
| `live` | Currently in active use somewhere public (LinkedIn post, Skool homepage, landing page). |
| `featured` | Flagged as a top-of-funnel hero asset. The handful of strongest proofs. |
| `redacted` | Previously surfaced but pulled. Keep the record; explain why in `notes`. |

Promote conservatively. The default is `raw`. Only mark `cleared-for-public` if there's already explicit evidence Alex shared it publicly (e.g. a live LinkedIn post URL).

### `source_url`

Honest gaps over fabrication. If you can't verify a URL, set null. Acceptable values:

- Relative repo paths (`brain/the-build-room/cohorts/.../s2-wins-post-2026-06-23.md`)
- Absolute URLs (Fathom, Skool, LinkedIn, YouTube)
- `null`

### `media_url` and `thumbnail`

Both nullable. As of 2026-07-16, cut clips upload to the Drive "Clips" folder (inside the Build Room master folder, anyone-with-link viewer) and `media_url` gets the Drive `/file/d/<id>/view` link. The library page embeds Drive links as `/preview` iframes, and relative `.mp4` paths (repo-hosted files) as native video. When a media upload is pending, set `media_url: null` and add `"TODO: upload <type> to <destination>"` to `notes`.

### `local_path` (optional)

For clip entries, the path to the archived clean cut on Alex's machine (usually under `brain/the-build-room/recordings/clips/<cohort>/`). Set when `media_url` points at Drive so the local master is still traceable.

`thumbnail`, when set, should be a path under `build-room-visuals/assets/proof/` (relative) for repo-tracked images, or an absolute URL.

### `do_not_share` and `consent_note`

Consent protection above and beyond `status`. `status` tracks public clearance; `do_not_share` tracks a builder's request that the work not circulate at all, even internally. The `confidentiality-requested` tag remains the lightweight signal; `do_not_share: true` is the enforcement flag renderers and skills must obey. First use: Ruben's debt-project entries (2026-07-23, Alex confirmed his sensitivity).

Note: `proof-library.json` itself is fetchable from public GitHub Pages. `do_not_share` hides an entry from every rendered view, but the raw entry text stays in the public JSON. If an entry's content itself is sensitive, also slim the entry (trim `quote`/`notes` down to non-sensitive stubs) or keep the detail only in cohort docs.

### `tags`

Free-form, but reuse existing tags when they fit. Live working set:

`first-brick`, `thesis`, `breakthrough`, `pivot`, `peer-teaching`, `live-demo`, `mid-session-extension`, `recovery`, `scope-lock`, `tooling`, `vision`, `urgency`, `framework`, `cohort-promise`, `objection-handling`, `humor`, `story`, `recognition`.

Consulting-engagement tags: `consulting` (required on every consulting entry), plus one or more of `founder-dependency`, `delegation`, `ops-systems`, `performance-reviews`, `engagement-outcome`.

Don't invent a tag if an existing one works.

**Workflow tag:** `awaiting-review` marks a cut clip Alex has not yet approved. The library page has a "Ready for review" filter for it. Remove the tag when Alex approves the clip; that is the moment it becomes shareable to the marketing loop.

---

## What NOT to put in the library

- Quotes you can't trace to a transcript line or a written source
- Builder last names + identifying detail in any `cleared-for-public` entry without evidence the builder posted it themselves
- Internal facilitator-only diagnostics (those belong in facilitator recap docs)
- Media speculation (don't claim a video exists if it hasn't been recorded)

---

## Mutation rules

- Append-only by default. Promote `status` upward as evidence arrives.
- `id` is immutable once set. If wrong, mark old entry `redacted` and add a new one.
- Schema changes happen here first, then the JSON, then the HTML.
- Skills that write to the JSON (e.g. `build-room-debrief`) must conform to this schema. Drift gets caught at HTML render time (cards will show empty fields).

---

Alex Salinsky · The Build Room
