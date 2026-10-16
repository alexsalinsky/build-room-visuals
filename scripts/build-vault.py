#!/usr/bin/env python3
"""Render the public Build Vault page (build-vault.html) from build-vault-src/.

Sources:
  build-vault-src/alex-builds.json    Alex's own builds, newest first. Add new ones here ("log a build").
  build-vault-src/member-builds.json  Member builds (seeded from the Google Sheet index) with flow + integrations.
  build-vault-src/template.html       Page shell; __BUILDS__ is replaced with the JSON.

Each build: title, what_it_does, why, builder, where, category, tools[], demo_url,
starter_prompt, integrations[] (what to connect, and why), flow[] ({role, eg}: generic
role box, brand examples under it).

Usage: python3 scripts/build-vault.py
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "build-vault-src"
REQUIRED = ("title", "what_it_does", "builder", "category", "flow", "integrations")


def load(name, section):
    rows = json.loads((SRC / name).read_text(encoding="utf-8"))
    for r in rows:
        r["section"] = section
        missing = [k for k in REQUIRED if not r.get(k)]
        if missing:
            sys.exit(f"{name}: '{r.get('title')}' is missing {', '.join(missing)}")
    return rows


def main():
    alex = sorted(load("alex-builds.json", "alex"), key=lambda r: r.get("logged") or "", reverse=True)
    builds = alex + load("member-builds.json", "member")
    text = json.dumps(builds, ensure_ascii=False)
    if "—" in text:
        sys.exit("Em dash found in build copy; house style bans it.")
    text = text.replace("</", "<\\/")
    page = (SRC / "template.html").read_text(encoding="utf-8").replace("__BUILDS__", text)
    (ROOT / "build-vault.html").write_text(page, encoding="utf-8")
    print(f"build-vault.html: {len(alex)} Alex builds + {len(builds) - len(alex)} member builds")


if __name__ == "__main__":
    main()
