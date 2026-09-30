#!/usr/bin/env python3
"""Build the published site: the web page plus files AI tools can read without JavaScript.

  python3 tools/build_site.py [OUT_DIR] [--base-url URL]

OUT_DIR (default _site) receives:
  index.html             the web navigator (web/index.html)
  aafdid-rules.json      the rules bundle, for tools that run code
  llms.txt               the guide for AI assistants: how to get a correct answer
  agent/*.md             the agent-pack knowledge files, as plain Markdown
  answers/index.md       the list of answer files
  answers/<pathway>/<key answer>/<event>.md
                         the engine's own result for each common profile, with every other
                         answer left unknown, plus what each open answer would change

The page draws its requirement lists with JavaScript, so a tool that reads it as text sees no
requirements. These files give such tools the same results the page shows, in plain text.
Nothing here is committed: the Pages workflow runs this script on every deploy.
"""
import itertools, json, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "engine"))
import aafdid as A  # noqa: E402

args = [a for a in sys.argv[1:] if not a.startswith("--")]
OUT = Path(args[0]) if args else ROOT / "_site"
BASE = "https://gfranistaken.github.io/aafdid-navigator"
if "--base-url" in sys.argv:
    BASE = sys.argv[sys.argv.index("--base-url") + 1].rstrip("/")

B = A.load_bundle()
META = B["meta"]
PW = {p["id"]: p for p in B["pathways"]}
Q = {q["id"]: q for q in B["questions"]["questions"]}
PLACE = {"required": "Required", "conditional": "May apply", "review": "Also review", "triggered": "Only if triggered, and only",
         "reference": "Reference rule", "needs_more": "Still needs another answer"}
STATUS_WORD = {"required": "Required", "conditional": "May apply", "review": "Also review", "triggered": "Only if triggered",
               "reference": "Reference rule", "undetermined": "Needs an answer", "not_applicable": "Not applicable"}

# The answer that splits each pathway's list the most. Every other answer stays unknown.
VARIANTS = {
    "mca": [(o["value"], {"mca_program_type": o["value"]}, o["label"]) for o in Q["mca_program_type"]["options"]],
    "mta": [(f"{p['value']}-{s['value']}", {"mta_path": p["value"], "mta_size": s["value"]}, f"{p['label']}, {s['label'].lower()}")
            for p in Q["mta_path"]["options"] for s in Q["mta_size"]["options"]],
    "uca": [(o["value"], {"uca_acat": o["value"]}, o["label"]) for o in Q["uca_acat"]["options"]],
    "swa": [("above_acat_ii", {"swa_above_acat_ii": True}, "above the ACAT II thresholds"),
            ("not_above_acat_ii", {"swa_above_acat_ii": False}, "at or below the ACAT II thresholds")],
    "dbs": [("all_programs", {}, "all business systems")],
    "aos": [(o["value"], {"svc_total_value": o["value"]}, f"total value {o['label'][0].lower() + o['label'][1:]}")
            for o in Q["svc_total_value"]["options"]],
}
VARIANT_FIELD = {"mca": "mca_program_type", "mta": "mta_path and mta_size", "uca": "uca_acat", "swa": "swa_above_acat_ii",
                 "dbs": "key answer", "aos": "svc_total_value"}


def key_answers(pid):
    """How a user's answer maps to the folder name, for llms.txt."""
    if pid == "mta":
        paths = "; ".join(f"`{o['value']}` = {o['label']}" for o in Q["mta_path"]["options"])
        sizes = "; ".join(f"`{o['value']}` = {o['label']}" for o in Q["mta_size"]["options"])
        return f"`<path>-<size>` (for example `rf-non_major`). Path: {paths}. Size: {sizes}."
    if pid == "swa":
        return "`above_acat_ii` = cost exceeds the ACAT II thresholds; `not_above_acat_ii` = at or below them."
    if pid == "dbs":
        return "always `all_programs` (the DBS list does not split by size)."
    field = {"mca": "mca_program_type", "uca": "uca_acat", "aos": "svc_total_value"}[pid]
    return "; ".join(f"`{o['value']}` = {o['label']}" for o in Q[field]["options"]) + "."


def events(pid):
    return [e for e in PW[pid]["events"] if not e.get("every")]


def values(qid):
    q = Q[qid]
    return [True, False] if q.get("type") == "boolean" else [o["value"] for o in q.get("options") or []]


def fmt(qid, v):
    return ("yes" if v else "no") if Q[qid].get("type") == "boolean" else f"`{v}`"


def describe(combos, fields):
    """Plain-English form of a set of answer combinations over fields, as an OR of AND clauses,
    factored field by field: "`a` is `x` and `b` is `y` or `z`; or `a` is `w`"."""
    opts = [values(f) for f in fields]

    def rec(cs, i):
        """Clauses (lists of (field, values)) covering exactly the combinations cs over fields[i:]."""
        if i == len(fields):
            return [[]]
        groups = {}
        for c in cs:
            groups.setdefault(c[0], set()).add(c[1:])
        rest_all = len(list(itertools.product(*opts[i + 1:])))
        merged = {}
        for v in opts[i]:
            if v in groups:
                sub = groups[v]
                key = "*" if len(sub) == rest_all else repr(sorted(sub, key=lambda c: [o.index(x) for o, x in zip(opts[i + 1:], c)]))
                merged.setdefault(key, ([], sub))[0].append(v)
        clauses = []
        for key, (vs, sub) in merged.items():
            head = [] if len(vs) == len(opts[i]) else [(fields[i], vs)]
            tails = [[]] if key == "*" else rec(sorted(sub, key=lambda c: [o.index(x) for o, x in zip(opts[i + 1:], c)]), i + 1)
            clauses += [head + t for t in tails]
        return clauses

    ordered = sorted(set(combos), key=lambda c: [o.index(x) for o, x in zip(opts, c)])
    if not ordered:
        return ""
    text = []
    for clause in rec(ordered, 0):
        text.append(" and ".join(f"`{f}` is " + " or ".join(fmt(f, v) for v in vs) for f, vs in clause) or "whatever the answers")
    return "; or ".join(text)


def when_text(it):
    return A.when_text(it) or "not tied to one event"


def settle_section(profile, result):
    """For each open item, what each answer (or pair of answers) makes of it, computed by the engine."""
    cache = {}

    def run(extra):
        key = json.dumps(extra, sort_keys=True)
        if key not in cache:
            cache[key] = {i["code"]: i for i in A.evaluate(B, dict(profile, **extra))["items"]}
        return cache[key]

    L = ["## Settle the open items", ""]
    qs = result["questions_needed"]
    L.append("Ask the user these questions, one at a time, and accept \"not sure\":")
    L.append("")
    for n, q in enumerate(qs, 1):
        qq = Q[q["id"]]
        opts = "yes or no" if qq.get("type") == "boolean" else "; ".join(f"`{o['value']}` = {o['label']}" for o in qq["options"])
        L.append(f"{n}. `{q['id']}`: {q['text']} Answers: {opts}. (Affects {q['affects']} item{'' if q['affects'] == 1 else 's'} below.)")
    L.append("")
    L.append("Then place each open item as shown. The results come from the navigator engine, not from reading the rules by hand.")
    L.append("")
    for it in result["items"]:
        if it["status"] != "undetermined":
            continue
        fields = it.get("missing") or []
        outcome = {}
        for combo in itertools.product(*[values(f) for f in fields]):
            got = run(dict(zip(fields, combo))).get(it["code"])
            st = got["status"] if got else "not_applicable"
            if st == "undetermined":
                st = "needs_more"
            outcome.setdefault(st, []).append(combo)
        lines = [f"{PLACE[st]} when {describe(outcome[st], fields)}" for st in PLACE if st in outcome]
        if "not_applicable" in outcome:
            lines.append("Not applicable otherwise")
        L.append(f"- **{it['code']}** {it['name'].rstrip('.')}. Due: {when_text(it).rstrip('.')}. " + ". ".join(lines) + ".")
    typed = [it for it in result["items"] if it.get("type_depends_on") and it["status"] != "not_applicable"]
    if typed:
        L.append("")
        L.append("Types (statutory or regulatory) that depend on an answer:")
        L.append("")
        for it in typed:
            f = it["type_depends_on"]
            by = {}
            for combo in itertools.product(*[values(x) for x in f]):
                got = run(dict(zip(f, combo))).get(it["code"])
                if got:
                    by.setdefault(A.TYPE_LABEL[got["type"]], []).append(combo)
            parts = [f"{t} when {describe(c, f)}" for t, c in by.items()]
            L.append(f"- **{it['code']}** {it['name'].rstrip('.')}: " + "; ".join(parts) + f". Until answered: {A.TYPE_LABEL[it['type']]}.")
    return L


def answer_file(pid, vkey, vprof, vlabel, ev):
    pw = PW[pid]
    profile = {"pathway": pid, **vprof}
    if ev:
        profile["event"] = ev["id"]
    res = A.evaluate(B, profile)
    ev_label = ev["name"] if ev else "all events"
    md = A.to_markdown(res, include_not_applicable=False).split("\n")
    md = md[1:]  # the engine's H1 is replaced by the title below
    if "## Questions that would settle more of the list" in md:  # the settle section below asks them, with their answers
        a = md.index("## Questions that would settle more of the list")
        b = next((i for i in range(a + 1, len(md)) if md[i].startswith("## ") or md[i].startswith("_")), len(md))
        md = md[:a] + md[b:]
    na = [i["code"] for i in res["items"] if i["status"] == "not_applicable"]
    L = [f"# AAFDID requirements: {pw['code']}, {vlabel}, {ev_label}", ""]
    L.append(f"This is the AAFDID Navigator engine's own result for the profile below, from rules {META['version']} "
             f"(AAFDID captured {META['capture_date']}, checked against the live AAFDID pages {META['checked_date']}). "
             "Every answer not shown is still unknown.")
    L += ["", "```", A.to_profile_block(B, profile), "```", ""]
    L.append("**For AI assistants.** Present these lists as they are. Keep the codes, names, types and due events exactly, "
             "and do not add or drop requirements. Then ask the questions under \"Settle the open items\" and place each open item as "
             f"that section says. If the program's pathway, {VARIANT_FIELD[pid]} or next event differs from the profile above, "
             f"use the matching file listed in {BASE}/answers/index.md instead of adjusting this one.")
    L += md[:-1]  # everything but the closing disclaimer line
    if res["questions_needed"]:
        L += settle_section(profile, res)
        L.append("")
    if na:
        L.append(f"## Not applicable to this profile ({len(na)})")
        L.append("")
        L.append("Do not list these: " + ", ".join(na) + ".")
        L.append("")
    L.append(md[-1])  # disclaimer
    return "\n".join(L).rstrip() + "\n"


def llms_txt(index_rows):
    ex = f"{BASE}/answers/mca/acat_ii/ms_b.md"
    L = ["# AAFDID Navigator", ""]
    L.append(f"> An unofficial guide to AAFDID, the Adaptive Acquisition Framework Document Identification tool. It works out which "
             f"information requirements apply to a Department of War acquisition program, when each is due, and whether each is "
             f"statutory or regulatory. Rules {META['version']}: AAFDID captured {META['capture_date']}, checked against the live AAFDID "
             f"pages {META['checked_date']}, {META['requirements']} requirement records across all six pathways.")
    L.append("")
    L.append("## Instructions for AI assistants")
    L.append("")
    L += [
        "1. Do not answer AAFDID questions from memory or from the web page (index.html). The page draws its requirement lists "
        "with JavaScript, so its text contains no requirements.",
        "2. There is no single \"AAFDID plan\": the list depends on the program. Before listing requirements, ask the user for:",
        "   - the pathway: `mca`, `mta`, `uca`, `swa`, `dbs` or `aos` (if they are unsure, use the pathway finder in the procedure file below)",
        "   - the pathway's key answer (listed below for each pathway)",
        "   - the next decision point or phase, or all events",
        f"3. Fetch the matching answer file: `{BASE}/answers/<pathway>/<key answer>/<event>.md`, for example {ex}. "
        f"Every file is listed in {BASE}/answers/index.md.",
        "4. Present the file's lists as they are, then ask the questions in its \"Settle the open items\" section and place each "
        "open item as that section says. Do not add requirements that are not in the file, and do not drop any.",
        "5. Keep requirement codes and names exactly as written, and end with the caveat at the bottom of the file.",
        "6. Ask for dollar ranges, never exact amounts. Do not ask for classified information, CUI or other sensitive details. "
        "Fetching these files sends nothing about the program except which file is requested.",
        "",
        "## Answer files",
        "",
        "The folder is the key answer and the file name is the next event. Use `all_events` when the user does not name one.",
        "",
    ]
    L += index_rows
    L += [
        "",
        "## Reference",
        "",
        f"- [Procedure]({BASE}/agent/00-procedure.md): the full method, output format and pathway finder",
        f"- [Intake questions]({BASE}/agent/01-intake.md): every question, its answers, and which requirements it affects",
    ]
    for f, label in (("10-mca.md", "MCA records"), ("11-mta.md", "MTA records"), ("12-uca.md", "UCA records, and the MCA entries UCA programs also review"),
                     ("13-swa.md", "SWA records"), ("14-dbs.md", "DBS records"), ("15-aos.md", "AoS records, and the services categories")):
        size = (ROOT / "agent" / "knowledge" / f).stat().st_size
        L.append(f"- [{label}]({BASE}/agent/{f}): about {round(size / 1000)}K characters")
    L += [
        f"- [Changes since AAFDID's tables]({BASE}/agent/20-changes-since-aafdid.md): later law and policy changes, attached to the records they affect",
        f"- [Rules bundle, JSON]({BASE}/aafdid-rules.json): machine-readable rules; tools that run code can use the engines in the repository",
        "- [Source repository](https://github.com/gfranistaken/aafdid-navigator): rules, engines, tests and the agent pack",
        "",
        "Not a secure system: this is an unofficial public website, not a U.S. Government system. " + META["disclaimer"].replace("Unofficial. ", ""),
        "",
    ]
    return "\n".join(L)


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "agent").mkdir(parents=True)
    shutil.copy(ROOT / "web" / "index.html", OUT / "index.html")
    shutil.copy(ROOT / "rules" / "aafdid-rules.json", OUT / "aafdid-rules.json")
    for f in sorted((ROOT / "agent" / "knowledge").glob("*.md")):
        shutil.copy(f, OUT / "agent" / f.name)
    shutil.copy(ROOT / "agent" / "AGENT_INSTRUCTIONS.md", OUT / "agent" / "AGENT_INSTRUCTIONS.md")

    listing, index_rows, biggest = [], [], (0, "")
    for pid in ("mca", "mta", "uca", "swa", "dbs", "aos"):
        evs = events(pid)
        ev_names = "; ".join(f"`{e['id']}` = {e['name']}" for e in evs) + "; `all_events` = every event"
        first = VARIANTS[pid][0][0]
        index_rows += [f"### `{pid}`: {PW[pid]['name']} ({PW[pid]['code']})", "",
                       f"- Key answer: {key_answers(pid)}",
                       f"- Next event: {ev_names}.",
                       f"- Example: {BASE}/answers/{pid}/{first}/{evs[0]['id']}.md", ""]
        listing += [f"## {PW[pid]['name']} ({PW[pid]['code']})", ""]
        for vkey, vprof, vlabel in VARIANTS[pid]:
            links = []
            for ev in evs + [None]:
                name = ev["id"] if ev else "all_events"
                path = OUT / "answers" / pid / vkey / f"{name}.md"
                path.parent.mkdir(parents=True, exist_ok=True)
                text = answer_file(pid, vkey, vprof, vlabel, ev)
                path.write_text(text, encoding="utf-8")
                biggest = max(biggest, (len(text), str(path.relative_to(OUT))))
                links.append(f"[{ev['short'] if ev else 'all events'}]({BASE}/answers/{pid}/{vkey}/{name}.md)")
            listing.append(f"- {vlabel[0].upper() + vlabel[1:]}: " + " · ".join(links))
        listing.append("")
    head = ["# AAFDID Navigator answer files", "",
            f"Each file is the navigator engine's result for one pathway, key answer and next event, with every other answer unknown "
            f"(rules {META['version']}). See {BASE}/llms.txt for how to use them.", ""]
    (OUT / "answers" / "index.md").write_text("\n".join(head + listing).rstrip() + "\n", encoding="utf-8")
    (OUT / "llms.txt").write_text(llms_txt(index_rows), encoding="utf-8")
    n = sum(1 for _ in (OUT / "answers").rglob("*.md")) - 1
    print(f"wrote {OUT}: {n} answer files (largest {biggest[1]}, {biggest[0]:,} characters), llms.txt, agent/, index.html, aafdid-rules.json")


if __name__ == "__main__":
    main()
