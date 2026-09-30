#!/usr/bin/env python3
"""Build web/index.html: the template with the rules bundle and the engine inlined.

The result is one self-contained page (no network calls except Google Fonts),
suitable for GitHub Pages, a claude.ai artifact, or opening from disk.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
tpl = (ROOT / "web" / "template.html").read_text(encoding="utf-8")
rules = (ROOT / "rules" / "aafdid-rules.json").read_text(encoding="utf-8").strip()
engine = (ROOT / "engine" / "aafdid.js").read_text(encoding="utf-8")

rules = rules.replace("</", "<\\/")
if "</script" in engine.lower():
    raise SystemExit("engine contains a closing script tag")
html = tpl.replace("__RULES_JSON__", rules).replace("/*__ENGINE__*/", engine)
out = ROOT / "web" / "index.html"
out.write_text(html, encoding="utf-8")
print(f"wrote {out.relative_to(ROOT)} ({len(html.encode('utf-8')) // 1024} KB)")
