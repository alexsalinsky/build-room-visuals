#!/usr/bin/env python3
"""Render one Build Vault build as its own shareable page, with no links to the rest.

    python3 scripts/build-share-page.py "Feed blocker" feed-blocker

Reads the build from build-vault-src/alex-builds.json (or member-builds.json) by
original_name, writes b/<slug>.html. Re-run after editing the entry.
"""
import html, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
name, slug = sys.argv[1], sys.argv[2]
build = None
for src in ("alex-builds.json", "member-builds.json"):
    for b in json.loads((ROOT / "build-vault-src" / src).read_text(encoding="utf-8")):
        if b.get("original_name") == name:
            build = b
if not build:
    sys.exit(f"no build with original_name {name!r}")

e = lambda s: html.escape(s or "", quote=True)
demo = build.get("demo_url") or ""
repo = build.get("repo_url") or ""
# embed same-site HTML demos; anything else is just a button
embed = demo.startswith("https://alexsalinsky.github.io/build-room-visuals/") and demo.endswith(".html")
demo_src = "../" + demo.split("/build-room-visuals/", 1)[1] if embed else ""

buttons = []
if repo:
    buttons.append(f'<a class="btn primary" href="{e(repo)}">Get the code</a>')
if demo:
    buttons.append(f'<a class="btn ghost" href="{e(demo)}">Open the demo</a>')

flow = "".join(f'<li><b>{e(f["role"])}</b> <span class="eg">{e(f.get("eg"))}</span></li>' for f in build.get("flow", []))
integ = "".join(f"<li>{e(i)}</li>" for i in build.get("integrations", []))
tools = "".join(f"<span>{e(t)}</span>" for t in build.get("tools", []))
lede = build.get("summary") or build["what_it_does"].split(". ")[0] + "."
diagram_json = json.dumps(build["diagram"]).replace("</", "<\\/")
demo_block = f'<section class="demo"><iframe src="{e(demo_src)}" title="Demo" loading="lazy"></iframe></section>' if embed else ""
button_html = "".join(buttons)

page = f"""<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(build["original_name"].capitalize())}</title>
<meta name="description" content="{e(lede)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,800&family=Space+Grotesk:wght@400;500;700&display=swap">
<style>
:root{{--black:#0B0B0B;--volt:#C8FF3D;--paper:#FFFFFF;--muted:#4a4a44;--soft:#f2f2ee;
  --display:"Bricolage Grotesque",ui-sans-serif,system-ui,sans-serif;
  --body:"Space Grotesk",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;color-scheme:light}}
*{{box-sizing:border-box}}
body{{background:var(--paper);color:var(--black);font:16px/1.55 var(--body);margin:0}}
.band{{background:var(--black);color:var(--paper)}}
.inner{{max-width:920px;margin:0 auto;padding-inline:16px}}
.band .inner{{padding-block:26px 36px;display:flex;flex-direction:column;gap:18px}}
.lockup{{display:flex;align-items:center;gap:.28em;font:800 20px/1 var(--display);letter-spacing:-.03em}}
.lockup svg{{height:.9em;width:auto}}
.eyebrow{{font:700 13px var(--body);letter-spacing:.24em;text-transform:uppercase;color:#bdbdb4}}
h1{{font:800 clamp(32px,5.5vw,52px)/1.05 var(--display);letter-spacing:-.03em;margin:0;text-wrap:balance}}
.lede{{margin:0;max-width:62ch;font-size:18px;color:#e4e4dc}}
.buttons{{display:flex;flex-wrap:wrap;gap:10px}}
.btn{{font:700 15px var(--body);padding:10px 16px;min-height:44px;border:2px solid var(--volt);text-decoration:none;display:inline-flex;align-items:center}}
.btn.primary{{background:var(--volt);color:var(--black)}}
.btn.ghost{{background:transparent;color:var(--paper)}}
main.inner{{padding-block:28px 56px;display:flex;flex-direction:column;gap:30px}}
h2{{font:800 24px/1.1 var(--display);letter-spacing:-.02em;margin:0 0 10px}}
p{{margin:0}}
.demo{{border:2px solid var(--black);box-shadow:8px 8px 0 var(--volt)}}
.demo iframe{{display:block;width:100%;height:760px;border:0}}
.tags{{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}}
.tags span{{font:700 11px var(--body);letter-spacing:.12em;text-transform:uppercase;border:2px solid var(--black);padding:2px 7px}}
ul{{margin:0;padding-left:20px}} li{{margin:4px 0}}
.eg{{color:var(--muted)}} .eg::before{{content:" \\00b7  "}}
.diagram{{border:2px solid var(--black);padding:14px;overflow-x:auto;min-height:60px}}
.diagram svg{{max-width:100%!important;height:auto;display:block;margin:0 auto}}
.diagram .node rect,.diagram .node polygon{{stroke-width:2px!important}}
.diagram .start rect{{fill:#0B0B0B!important}}
.diagram .start .nodeLabel,.diagram .start .nodeLabel *{{color:#FFFFFF!important}}
.diagram .bucket rect{{fill:#C8FF3D!important}}
.diagram .nodeLabel,.diagram .edgeLabel{{font:500 13px/1.3 var(--body)!important;color:var(--black)}}
.diagram .eg{{font-size:12px}} .diagram .eg::before{{content:""}}
pre{{white-space:pre-wrap;background:var(--soft);border:2px solid var(--black);padding:14px;margin:10px 0 0;font:15px/1.5 var(--body)}}
.copy{{font:700 15px var(--body);padding:10px 14px;min-height:44px;border:2px solid var(--black);background:var(--black);color:var(--paper);cursor:pointer;margin-top:10px}}
footer{{border-top:2px solid var(--black);padding-top:16px;display:flex;flex-wrap:wrap;justify-content:space-between;gap:10px;color:var(--muted);font-size:14px}}
footer b{{color:var(--black)}}
@media (max-width:640px){{.demo iframe{{height:820px}}}}
</style>
<header class="band"><div class="inner">
  <div class="lockup" aria-label="Humans v Robots">HUMANS<svg viewBox="7 12 106 106" aria-hidden="true"><path d="M16 40 L60 104 L104 40" fill="none" stroke="#FFFFFF" stroke-width="16" stroke-linejoin="miter"/><circle cx="60" cy="30" r="18" fill="#C8FF3D"/></svg>ROBOTS</div>
  <span class="eyebrow">Build Vault</span>
  <h1>{e(build["title"])}</h1>
  <p class="lede">{e(lede)}</p>
  <div class="buttons">{button_html}</div>
</div></header>
<main class="inner">
  {f'<section class="demo"><iframe src="{e(demo_src)}" title="Demo" loading="lazy"></iframe></section>' if embed else ""}
  <section><h2>What it does</h2><p>{e(build["what_it_does"])}</p><div class="tags">{tools}</div></section>
  <section><h2>Why</h2><p>{e(build["why"])}</p></section>
  <section><h2>How it works</h2><div class="diagram" id="diagram"><ol>{flow}</ol></div></section>
  <section><h2>What you connect</h2><ul>{integ}</ul></section>
  <section><h2>Build your own</h2><p>Paste this into Claude Code or Codex. It builds the smallest version first, then you improve it.</p>
    <pre id="prompt">{e(build["starter_prompt"])}</pre><button class="copy" id="copy" type="button">Copy starter prompt</button></section>
  <footer><span>Built by {e(build["builder"])}.</span><span>Learn AI. Build Robots. <b>Stay Human.</b></span></footer>
</main>
<script type="application/json" id="src">{diagram_json}</script>
<script type="module">
document.getElementById('copy').onclick = async (ev) => {{
  const btn = ev.currentTarget;
  try {{ await navigator.clipboard.writeText(document.getElementById('prompt').textContent); btn.textContent = 'Copied'; }}
  catch {{ const r = document.createRange(); r.selectNodeContents(document.getElementById('prompt'));
    const s = getSelection(); s.removeAllRanges(); s.addRange(r); btn.textContent = 'Selected, press Ctrl+C'; }}
  setTimeout(() => btn.textContent = 'Copy starter prompt', 1800);
}};
try {{
  const {{default: m}} = await import('https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.esm.min.mjs');
  m.initialize({{startOnLoad:false, securityLevel:'loose', theme:'base',
    themeVariables:{{fontFamily:'Space Grotesk, sans-serif', fontSize:'14px', primaryColor:'#FFFFFF', primaryBorderColor:'#0B0B0B', primaryTextColor:'#0B0B0B', lineColor:'#0B0B0B', edgeLabelBackground:'#FFFFFF'}},
    flowchart:{{htmlLabels:true, curve:'basis', nodeSpacing:22, rankSpacing:30, padding:10}}}});
  const {{svg}} = await m.render('flow', JSON.parse(document.getElementById('src').textContent));
  document.getElementById('diagram').innerHTML = svg;
}} catch (err) {{ /* the plain list stays */ }}
</script>
</html>
"""
if "—" in page:
    sys.exit("em dash in output; fix the entry")
out = ROOT / "b" / f"{slug}.html"
out.parent.mkdir(exist_ok=True)
out.write_text(page, encoding="utf-8")
print("wrote", out.relative_to(ROOT))
