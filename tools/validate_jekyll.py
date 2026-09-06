"""
Simulates Jekyll's permalink resolution and _includes/nav.html rendering logic
without needing a real Ruby/Jekyll install (none is available in the Claude
session environment, and rubygems.org isn't on the network allowlist).

Run this after any change that touches front matter, _data/nav.yml, or
cross-page #anchor links, and before pushing. GitHub Pages still does the
authoritative real build on push -- this is a fast local sanity check to
catch mistakes before that build does.

Usage:  python3 tools/validate_jekyll.py   (run from the repo root)
Requires: pyyaml  (pip install pyyaml --break-system-packages)
"""
import re, sys, glob, yaml, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- Load nav.yml ---
with open(f"{ROOT}/_data/nav.yml") as f:
    nav = yaml.safe_load(f)

nav_urls = []
for group in nav:
    for item in group["items"]:
        nav_urls.append(item["url"])

# --- Find all content pages (files with front matter) ---
pages = {}
for path in glob.glob(f"{ROOT}/**/*.html", recursive=True):
    if "/_layouts/" in path or "/_includes/" in path:
        continue
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        fm_text = text[4:end]
        body = text[end+5:]
        fm = yaml.safe_load(fm_text)
        pages[path] = {"front_matter": fm, "body": body}

print(f"Found {len(pages)} Jekyll pages.\n")

errors = []

# --- Check required front matter fields ---
required = ["layout", "title", "permalink", "category"]
permalinks = {}
for path, data in pages.items():
    fm = data["front_matter"]
    for field in required:
        if field not in fm:
            errors.append(f"{path}: missing front matter field '{field}'")
    if "permalink" in fm:
        pl = fm["permalink"]
        if pl in permalinks:
            errors.append(f"Duplicate permalink '{pl}': {permalinks[pl]} and {path}")
        permalinks[pl] = path

print("Permalinks registered:")
for pl, path in sorted(permalinks.items()):
    print(f"  {pl:35s} -> {os.path.relpath(path, ROOT)}")
print()

# --- Check every nav.yml url resolves to a real permalink ---
for url in nav_urls:
    if url not in permalinks:
        errors.append(f"nav.yml references url '{url}' with no matching page permalink")

# --- Simulate current-page highlighting per page ---
print("Simulated 'current' nav highlight per page:")
for path, data in pages.items():
    pl = data["front_matter"].get("permalink")
    matches = [u for u in nav_urls if u == pl]
    label = os.path.relpath(path, ROOT)
    if len(matches) > 1:
        errors.append(f"{label}: multiple nav items would match permalink {pl}")
    print(f"  {label:35s} permalink={pl!s:32s} current_matches={len(matches)}")
print()

# --- Check known cross-page anchors resolve ---
# Add an entry here whenever a new #anchor cross-link is introduced.
anchor_checks = [
    ("items/index.html#abaculus", "items/index.html", "abaculus"),
    ("overview/epochs.html#sundering", "overview/epochs.html", "sundering"),
    ("geography/locations.html#heavens-oak", "geography/locations.html", "heavens-oak"),
    ("stories/index.html#guardians", "stories/index.html", "guardians"),
]
print("Cross-page anchor checks:")
for label, relpath, anchor_id in anchor_checks:
    full = f"{ROOT}/{relpath}"
    body = pages.get(full, {}).get("body", "")
    found = f'id="{anchor_id}"' in body
    print(f"  {label:35s} -> {'OK' if found else 'MISSING'}")
    if not found:
        errors.append(f"Anchor id='{anchor_id}' not found in {relpath}")
print()

# --- Report ---
if errors:
    print(f"FAILED with {len(errors)} error(s):")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
else:
    print("All checks passed.")
