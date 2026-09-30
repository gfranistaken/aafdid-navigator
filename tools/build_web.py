#!/usr/bin/env python3
"""Build the web navigator from web/template.html, inlining the rules bundle and the engine.

Writes two files with the same content:
  web/index.html     a complete HTML document, for GitHub Pages or opening from disk
  web/artifact.html  the same page as a fragment (no doctype, head or body tags), for hosts
                     that wrap pages in their own document skeleton, such as a claude.ai artifact

Both are self-contained. The only network requests are for Google Fonts, and the page
falls back to system fonts without them.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
tpl = (ROOT / "web" / "template.html").read_text(encoding="utf-8")
rules = (ROOT / "rules" / "aafdid-rules.json").read_text(encoding="utf-8").strip()
engine = (ROOT / "engine" / "aafdid.js").read_text(encoding="utf-8")

MARK = "<!--BODY-->"
if tpl.count(MARK) != 1:
    raise SystemExit("web/template.html needs exactly one " + MARK + " marker between the head part and the body part")
rules = rules.replace("</", "<\\/")
if "</script" in engine.lower():
    raise SystemExit("engine contains a closing script tag")
page = tpl.replace("__RULES_JSON__", rules).replace("/*__ENGINE__*/", engine)
head, body = page.split(MARK)

fragment = head.rstrip() + "\n" + body.lstrip()
document = (
    "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
    + head.strip() + "\n</head>\n<body>\n" + body.strip() + "\n</body>\n</html>\n"
)

for name, html in (("index.html", document), ("artifact.html", fragment)):
    out = ROOT / "web" / name
    out.write_text(html, encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)} ({len(html.encode('utf-8')) // 1024} KB)")
