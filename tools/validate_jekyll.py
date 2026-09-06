"""
Simulates Jekyll's permalink resolution and _includes/nav.html rendering logic
without needing a real Ruby/Jekyll install (none is available in the Claude
session environment, and rubygems.org isn't on the network allowlist).

Also builds a directed link graph from every page's actual href="..." content
(page -> pages/anchors it links to), and checks:
  - every internal link resolves to a real page
  - every #anchor link resolves to a real id="..." on the target page
  - every page is reachable from either _data/nav.yml or another page's body
    content (an "unreachable" page has no way for a reader to ever find its
    URL, even though the file exists and Jekyll would build it fine)

This replaces manually grepping the repo for stale links before deleting or
renaming a page -- run this instead and read the "Link graph" and
"Reachability check" sections.

Run this after any change that touches front matter, _data/nav.yml, or
internal links -- especially before deleting or renaming a page -- and
before pushing. GitHub Pages still does the authoritative real build on
push; this is a fast local sanity check to catch mistakes before that
build does.

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

# --- Extract every internal link from every page's body, build a directed
#     graph (page -> pages/anchors it links to), and validate each edge ---
href_re = re.compile(r'href="([^"]+)"')
id_re_cache = {}

def anchor_exists(target_path, anchor_id):
    if target_path not in id_re_cache:
        body = pages.get(target_path, {}).get("body", "")
        id_re_cache[target_path] = set(re.findall(r'id="([^"]+)"', body))
    return anchor_id in id_re_cache[target_path]

graph = {}          # permalink -> sorted list of permalinks it links to
incoming = set()    # every permalink that receives at least one link
link_errors = []

for path, data in pages.items():
    src_permalink = data["front_matter"].get("permalink")
    src_dir = os.path.dirname(path)
    targets = set()
    for href in href_re.findall(data["body"]):
        if href.startswith(("http://", "https://", "mailto:")):
            continue
        page_part, _, anchor_part = href.partition("#")
        if page_part == "":
            # Same-page anchor, e.g. href="#top" -- nothing to resolve.
            continue
        resolved = os.path.normpath(os.path.join(src_dir, page_part))
        resolved_permalink = "/" + os.path.relpath(resolved, ROOT).replace(os.sep, "/")
        if resolved_permalink not in permalinks:
            link_errors.append(
                f"{os.path.relpath(path, ROOT)}: links to '{href}' -> "
                f"'{resolved_permalink}' which doesn't match any page's permalink"
            )
            continue
        if anchor_part and not anchor_exists(permalinks[resolved_permalink], anchor_part):
            link_errors.append(
                f"{os.path.relpath(path, ROOT)}: links to '{href}' but "
                f"id=\"{anchor_part}\" doesn't exist on {os.path.relpath(permalinks[resolved_permalink], ROOT)}"
            )
        targets.add(resolved_permalink)
        incoming.add(resolved_permalink)
    graph[src_permalink] = sorted(targets)

print("Link graph (page -> pages it links to):")
for pl, path in sorted(permalinks.items()):
    targets = graph.get(pl, [])
    print(f"  {os.path.relpath(path, ROOT):35s} -> {len(targets)} link(s)")
print()

# --- Reachability: every page should be reachable from nav.yml or from
#     another page's body content. A page reachable by neither is a genuine
#     dead page -- no visible way for a reader to ever find its URL. ---
reachable = set(nav_urls) | incoming
print("Reachability check (nav.yml link OR incoming content link):")
unreachable = []
for pl, path in sorted(permalinks.items()):
    label = os.path.relpath(path, ROOT)
    is_reachable = pl in reachable
    print(f"  {label:35s} {'reachable' if is_reachable else 'UNREACHABLE'}")
    if not is_reachable:
        unreachable.append(label)
print()

errors.extend(link_errors)
if unreachable:
    errors.append(f"Unreachable pages (no nav link, no incoming content link): {', '.join(unreachable)}")

# --- Report ---
if errors:
    print(f"FAILED with {len(errors)} error(s):")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
else:
    print("All checks passed.")
