#!/usr/bin/env python3
"""Turn a study-guide HTML snapshot (downloaded from its Claude artifact) into a site page.

Usage:
    python3 tools/import_guide.py <raw_snapshot.html> <module_folder>
    e.g. python3 tools/import_guide.py ~/Downloads/ee6049.html ee6049

What it does (idempotent — safe to run on an already-imported file):
  * adds <meta name="robots" content="noindex, nofollow"> to <head>
  * copies the page <title> into <head> (artifact pages keep it in <body>)
  * injects a small fixed "Study hub" link back to the site root
  * writes the result to <module_folder>/index.html

The guide's own content, scripts and styles are left untouched.
"""
import re
import sys
from pathlib import Path

MARK = "<!-- hub-injected -->"

HUB_LINK = MARK + """
<style id="hub-link-style">
.hub-link{position:fixed;right:14px;bottom:calc(14px + env(safe-area-inset-bottom,0px));z-index:60;
display:inline-flex;align-items:center;gap:6px;padding:7px 13px;border-radius:99px;
font:600 13px/1 system-ui,-apple-system,"Segoe UI",sans-serif;letter-spacing:.02em;text-decoration:none;
background:#0d1117;color:#f5b841;border:1px solid #f5b84166;box-shadow:0 4px 14px rgba(0,0,0,.25)}
.hub-link:hover{background:#f5b841;color:#0d1117}
.hub-link:focus-visible{outline:2px solid #2fd0c0;outline-offset:2px}
@media print{.hub-link{display:none}}
</style>
<a class="hub-link" href="../" aria-label="Back to the study hub">&larr; Study hub</a>
"""


def main(src: str, folder: str) -> None:
    html = Path(src).read_text(encoding="utf-8")

    if MARK not in html:
        title = re.search(r"<title>(.*?)</title>", html, re.S)
        head_extra = '<meta name="robots" content="noindex, nofollow">'
        if title and "<head>" in html and html.find("<title>") > html.find("</head>"):
            head_extra += f"<title>{title.group(1).strip()}</title>"
        m = re.search(r"<meta charset=[^>]*>", html)
        anchor = m.group(0) if m else "<head>"
        html = html.replace(anchor, anchor + head_extra, 1)
        idx = html.rfind("</body>")
        if idx == -1:
            html += HUB_LINK
        else:
            html = html[:idx] + HUB_LINK + html[idx:]

    out = Path(folder) / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
