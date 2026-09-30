#!/usr/bin/env python3
"""AAFDID Navigator engine 1.0.0, Python port of engine/aafdid.js.

Evaluates a program profile against rules/aafdid-rules.json. Standard library only.
Logic is three-valued: a condition is True, False, or None (unknown) when an answer is missing.
Unknown never becomes "not applicable"; it becomes "undetermined" with the question to ask.

  python3 engine/aafdid.py profile.txt             Markdown report
  python3 engine/aafdid.py profile.json --json     JSON result
  python3 engine/aafdid.py profile.txt --checklist Checklist
  python3 engine/aafdid.py profile.txt --block     Normalized profile block

License: MIT.
"""
import json, math, re, sys
from pathlib import Path

ENGINE_VERSION = "1.0.0"
STATUS_BY_KIND = {"event": "required", "recurring": "required", "contract": "required", "compliance": "required",
                  "conditional": "conditional", "triggered": "triggered", "reference": "reference"}
STATUS_ORDER = ["required", "conditional", "triggered", "undetermined", "reference", "not_applicable"]
UNORDERED_EVENTS = {"other"}
UNKNOWN_WORDS = ["unknown", "?", "n/a", "na", "tbd", "not sure", "none given", "unsure", "don't know", "dont know"]
GROUP_ORDER = ["at_focus", "by_event", "later", "ongoing", "as_required", "earlier", "conditional", "review",
               "triggered", "undetermined", "reference", "not_applicable"]


def load_bundle(path=None):
    path = Path(path) if path else Path(__file__).resolve().parent.parent / "rules" / "aafdid-rules.json"
    return json.loads(path.read_text(encoding="utf-8"))


def is_unknown(v):
    return v is None or v == ""


def test(c, p):
    if not c or c.get("const") is True:
        return True
    if c.get("const") is False:
        return False
    if "all" in c:
        unk = False
        for x in c["all"]:
            r = test(x, p)
            if r is False:
                return False
            if r is None:
                unk = True
        return None if unk else True
    if "any" in c:
        unk = False
        for x in c["any"]:
            r = test(x, p)
            if r is True:
                return True
            if r is None:
                unk = True
        return None if unk else False
    if "not" in c:
        r = test(c["not"], p)
        return None if r is None else (not r)
    v = p.get(c["field"])
    if is_unknown(v):
        return None
    if "eq" in c:
        return type(v) == type(c["eq"]) and v == c["eq"]
    if "ne" in c:
        return not (type(v) == type(c["ne"]) and v == c["ne"])
    if "in" in c:
        return any(type(v) == type(x) and v == x for x in c["in"])
    n = float(v)
    if "gte" in c:
        return n >= c["gte"]
    if "gt" in c:
        return n > c["gt"]
    if "lte" in c:
        return n <= c["lte"]
    if "lt" in c:
        return n < c["lt"]
    raise ValueError("Unknown condition: " + json.dumps(c))


def fields_of(c, acc=None):
    acc = [] if acc is None else acc
    if not isinstance(c, dict):
        return acc
    for k in ("all", "any"):
        for x in c.get(k, []):
            fields_of(x, acc)
    if "not" in c:
        fields_of(c["not"], acc)
    if "field" in c and c["field"] not in acc:
        acc.append(c["field"])
    return acc


def parse_money(v):
    if isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return v if math.isfinite(v) else None
    s = re.sub(r"[, $]", "", str(v).strip().lower())
    if not s:
        return None
    m = re.match(r"^(\d+(?:\.\d+)?)(k|thousand|m|mm|mil|million|b|bn|billion)?$", s)
    if not m:
        return None
    n = float(m.group(1))
    u = m.group(2) or ""
    if u in ("k", "thousand"):
        n *= 1e3
    elif u in ("m", "mm", "mil", "million"):
        n *= 1e6
    elif u in ("b", "bn", "billion"):
        n *= 1e9
    return int(math.floor(n + 0.5))


def parse_bool(v):
    if isinstance(v, bool):
        return v
    s = str(v).strip().lower()
    if s in ("yes", "y", "true", "t", "1"):
        return True
    if s in ("no", "n", "false", "f", "0"):
        return False
    return None


def pathway_by_id(bundle, pid):
    for p in bundle["pathways"]:
        if p["id"] == pid:
            return p
    return None


def question_by_id(bundle, qid):
    for q in bundle["questions"]["questions"]:
        if q["id"] == qid:
            return q
    return None


def normalize(bundle, inp):
    out = {}
    inp = inp or {}
    if inp.get("program"):
        out["program"] = str(inp["program"]).strip()
    for q in bundle["questions"]["questions"]:
        v = inp.get(q["id"])
        if is_unknown(v):
            continue
        if isinstance(v, str) and v.strip().lower() in UNKNOWN_WORDS:
            continue
        t = q.get("type")
        if t == "boolean":
            v = parse_bool(v)
        elif t == "money":
            v = parse_money(v)
        elif t == "choice":
            s = str(v).strip().lower()
            hit = None
            for o in q["options"]:
                if o["value"].lower() == s or o["label"].lower() == s:
                    hit = o["value"]
            v = hit
        elif t == "event":
            v = str(v).strip()
        if not is_unknown(v):
            out[q["id"]] = v
    if out.get("event"):
        pw = pathway_by_id(bundle, out.get("pathway"))
        ev = None
        if pw:
            s = out["event"].lower()
            for e in pw["events"]:
                if e["id"] == out["event"] or e["short"].lower() == s or e["name"].lower() == s:
                    ev = e["id"]
        if ev:
            out["event"] = ev
        else:
            del out["event"]
    return out


def visible_questions(bundle, profile):
    return [q for q in bundle["questions"]["questions"] if not q.get("show_if") or test(q["show_if"], profile) is True]


def fmt_num(n):
    return str(int(n)) if float(n).is_integer() else str(n)


def services_category(bundle, p):
    if p.get("pathway") != "aos":
        return None
    rows = {s["id"]: s for s in bundle.get("scat", [])}
    sid, note = None, ""
    t, a = p.get("svc_total_value"), p.get("svc_annual_value")
    if p.get("svc_special_interest") is True:
        sid = "special_interest"
    elif not is_unknown(t):
        if t >= 1e9 or (not is_unknown(a) and a > 3e8):
            sid = "I"
        elif t >= 2.5e8:
            sid = "II"
            if is_unknown(a) and t > 3e8:
                note = "S-CAT I instead if more than $300M falls in any one year."
        elif t >= 1e8:
            sid = "III"
        elif t >= 1e7:
            sid = "IV"
        else:
            sid = "V"
        if is_unknown(p.get("svc_special_interest")):
            note = (note + " " if note else "") + "Unless ASD(A) designates it Special Interest."
    if not sid:
        return {"id": None, "label": "Undetermined", "decision_authority": None, "note": "Enter the total estimated value.", "cite": bundle.get("scat_cite")}
    r = rows.get(sid, {})
    return {"id": sid, "label": r.get("label", sid), "rule": r.get("rule", ""), "decision_authority": r.get("decision_authority", ""), "note": note, "cite": bundle.get("scat_cite")}


def event_info(pw):
    idx, order = {}, 0
    for e in pw["events"]:
        if e["id"] in UNORDERED_EVENTS:
            idx[e["id"]] = None
        else:
            idx[e["id"]] = order
            order += 1
    return idx


def group_for(req, status, focus, idx):
    if status in ("not_applicable", "undetermined", "reference", "triggered", "conditional"):
        return status
    evs = [w["event"] for w in req.get("when") or []]
    ordered = [e for e in evs if idx.get(e) is not None]
    if not evs:
        return "ongoing"
    if not focus:
        return "by_event"
    if focus in evs:
        return "at_focus"
    if idx.get(focus) is None:
        return "by_event" if ordered else "as_required"
    if any(idx[e] > idx[focus] for e in ordered):
        return "later"
    if ordered:
        return "earlier"
    return "as_required"


def assess(bundle, req, profile, pw, focus, idx, override):
    r = test(req["applies_if"], profile)
    missing, reason = [], ""
    if r is True:
        status = STATUS_BY_KIND.get(req["kind"], "required")
    elif r is None:
        status = "undetermined"
        missing = [f for f in fields_of(req["applies_if"]) if is_unknown(profile.get(f))]
    else:
        c2 = test(req["conditional_if"], profile) if req.get("conditional_if") else False
        if c2 is True:
            status = "conditional"
        elif c2 is None:
            status = "undetermined"
            missing = [f for f in fields_of(req["conditional_if"]) if is_unknown(profile.get(f))]
        else:
            status = "not_applicable"
            reason = "Applies when: " + req["applies_when"]
    if override and status not in ("not_applicable", "undetermined"):
        status = override["status"]
    typ, type_depends = req["type"], []
    if req.get("type_rule"):
        tr = test(req["type_rule"]["if"], profile)
        if tr is True:
            typ = req["type_rule"]["then"]
        elif tr is False:
            typ = req["type_rule"]["else"]
        else:
            typ = "depends"
            type_depends = [f for f in fields_of(req["type_rule"]["if"]) if is_unknown(profile.get(f))]
    src_pw = pathway_by_id(bundle, req["pathways"][0]) if override else pw
    ev_map = {e["id"]: e for e in src_pw["events"]}
    when = []
    for w in req.get("when") or []:
        e = ev_map.get(w["event"], {"short": w["event"], "name": w["event"]})
        when.append({"event": w["event"], "short": e["short"], "name": e["name"], "submission": w["submission"]})
    if override:
        group = "undetermined" if status == "undetermined" else "review"
    else:
        group = group_for(req, status, focus, idx)
    item = {"code": req["code"], "id": req["id"], "name": req["name"], "status": status, "group": group,
            "type": typ, "type_text": req.get("type_text") or "", "source": req.get("source") or "",
            "approval": req.get("approval") or "", "when": when, "due_text": req.get("due_text") or "",
            "applies_when": req["applies_when"], "notes": req.get("notes") or "", "table": req["table_name"],
            "url": req["url"], "rule_basis": req.get("rule_basis") or "", "kind": req["kind"]}
    if req.get("procedure"):
        item["procedure"] = req["procedure"]
    if req.get("footnotes"):
        item["footnotes"] = req["footnotes"]
    if req.get("note_has_conditions"):
        item["note_has_conditions"] = True
    if req.get("currency"):
        item["currency"] = list(req["currency"])
    if type_depends:
        item["type_depends_on"] = type_depends
    if missing:
        item["missing"] = missing
    if reason:
        item["reason"] = reason
    if override:
        item["review_reason"] = override["reason"]
    if req.get("phase"):
        item["phase"] = req["phase"]
    return item


def evaluate(bundle, inp):
    profile = normalize(bundle, inp)
    meta = bundle["meta"]
    result = {"engine": "aafdid-navigator", "engine_version": ENGINE_VERSION, "rules_version": meta["version"],
              "aafdid_capture": meta["aafdid_capture"], "live_check": meta["live_check"], "profile": profile,
              "pathway": None, "focus_event": None, "derived": {}, "counts": {}, "items": [],
              "questions_needed": [], "currency_notes": [], "disclaimer": meta["disclaimer"]}
    pw = pathway_by_id(bundle, profile.get("pathway"))
    if not pw:
        result["questions_needed"].append({"id": "pathway", "text": question_by_id(bundle, "pathway")["text"], "affects": len(bundle["requirements"])})
        return result
    result["pathway"] = {"id": pw["id"], "code": pw["code"], "name": pw["name"], "instruction": pw["instruction"],
                         "decision_authority": pw["decision_authority"], "aafdid_url": pw["aafdid_url"], "notes": pw.get("notes", [])}
    idx = event_info(pw)
    focus = profile.get("event") if profile.get("event") in idx else None
    if focus:
        for e in pw["events"]:
            if e["id"] == focus:
                result["focus_event"] = {"id": e["id"], "short": e["short"], "name": e["name"]}
    items = [assess(bundle, req, profile, pw, focus, idx, None) for req in bundle["requirements"] if pw["id"] in req["pathways"]]
    ar = pw.get("also_review")
    if ar:
        mapped = dict(profile)
        mapped[ar["map_field"]["to"]] = profile.get(ar["map_field"]["from"])
        src_pw = pathway_by_id(bundle, ar["pathway"])
        for req in bundle["requirements"]:
            if ar["pathway"] not in req["pathways"] or req["table"] not in ar["tables"]:
                continue
            if is_unknown(mapped.get(ar["map_field"]["to"])):
                continue
            if test(req["applies_if"], mapped) is False:
                continue
            items.append(assess(bundle, req, mapped, src_pw, None, event_info(src_pw), {"status": ar["status"], "reason": ar["reason"]}))
    if pw["id"] == "aos":
        result["derived"]["services_category"] = services_category(bundle, profile)

    def first_event(it):
        best = 99
        for w in it["when"]:
            k = idx.get(w["event"])
            if k is not None and k < best:
                best = k
        return best
    items.sort(key=lambda it: (GROUP_ORDER.index(it["group"]), first_event(it), it["code"]))
    result["items"] = items
    for s in STATUS_ORDER:
        result["counts"][s] = 0
    for it in items:
        result["counts"][it["status"]] = result["counts"].get(it["status"], 0) + 1
    need = {}
    for it in items:
        for f in (it.get("missing") or []) + (it.get("type_depends_on") or []):
            need[f] = need.get(f, 0) + 1
    vis = visible_questions(bundle, profile)
    for q in vis:
        if need.get(q["id"]):
            result["questions_needed"].append({"id": q["id"], "text": q["text"], "affects": need[q["id"]]})
    used = set()
    for it in items:
        if it["status"] != "not_applicable":
            used.update(it.get("currency") or [])
    vis_ids = {v["id"] for v in vis}
    for n in bundle["currency"]["notes"]:
        at = n.get("attach") or {}
        event_hit = bool(focus) and focus in (at.get("events") or []) and pw["id"] in (at.get("pathways") or [pw["id"]])
        q_hit = any(q in vis_ids for q in (at.get("questions") or []))
        if n.get("banner") or n["id"] in used or event_hit or q_hit:
            result["currency_notes"].append({"id": n["id"], "date": n["date"], "title": n["title"], "text": n["text"],
                                             "sources": n["sources"], "applies_here": bool(n["id"] in used or event_hit or q_hit)})
    return result


BLOCK_HEADER = "AAFDID PROFILE v1"


def to_profile_block(bundle, inp):
    p = normalize(bundle, inp)
    lines = [BLOCK_HEADER]
    if p.get("program"):
        lines.append("program: " + p["program"])
    unknown = []
    for q in visible_questions(bundle, p):
        if is_unknown(p.get(q["id"])):
            if q["id"] != "event":
                unknown.append(q["id"])
            continue
        v = p[q["id"]]
        lines.append(q["id"] + ": " + (("yes" if v else "no") if q.get("type") == "boolean" else (fmt_num(v) if isinstance(v, (int, float)) else str(v))))
    if unknown:
        lines.append("unknown: " + ", ".join(unknown))
    return "\n".join(lines)


def parse_profile_block(text):
    out = {}
    for line in str(text or "").splitlines():
        m = re.match(r"^\s*[-*]?\s*([A-Za-z_]+)\s*:\s*(.*?)\s*$", line)
        if not m:
            continue
        k, v = m.group(1).lower(), m.group(2)
        if k == "unknown":
            continue
        out[k] = v
    return out


TYPE_LABEL = {"statutory": "Statutory", "regulatory": "Regulatory", "both": "Statutory and regulatory", "unspecified": "Not stated", "depends": "Depends on an answer"}
GROUP_TITLE = {
    "at_focus": "Due at the next event", "by_event": "Due by event", "later": "Due at later events", "ongoing": "Ongoing, contract-level and compliance items",
    "as_required": "As required", "earlier": "From earlier events (should already exist; check for updates)",
    "conditional": "May apply: check the condition", "review": "Also review: MCA entries AAFDID points UCA programs to",
    "triggered": "Only if triggered", "undetermined": "Needs an answer", "reference": "Reference rules", "not_applicable": "Not applicable"}


def esc(s):
    return re.sub(r"\s+", " ", str(s or "").replace("|", "\\|")).strip()


def when_text(it):
    if it.get("when"):
        return ", ".join(w["short"] + (" (update)" if w["submission"] == "update" else "") for w in it["when"])
    return it.get("due_text") or ""


def to_markdown(result, include_not_applicable=True):
    L = []
    if not result["pathway"]:
        return "\n".join(["# AAFDID requirements", "", "Pick a pathway first. Ask: " + result["questions_needed"][0]["text"]])
    p = result["pathway"]
    L.append("# AAFDID requirements: " + (result["profile"].get("program") or p["name"]))
    L.append("")
    L.append("- Pathway: " + p["name"] + " (" + p["code"] + "), " + p["instruction"])
    L.append("- Next event: " + (result["focus_event"]["name"] if result["focus_event"] else "not given; all events listed"))
    sc = result["derived"].get("services_category")
    if sc:
        L.append("- Services category: " + sc["label"] + ("; decision authority: " + sc["decision_authority"] if sc.get("decision_authority") else "") + (" (" + sc["note"] + ")" if sc.get("note") else ""))
    L.append("- Counts: " + ", ".join(str(result["counts"][s]) + " " + s.replace("_", " ", 1) for s in ["required", "conditional", "triggered", "undetermined", "not_applicable"]))
    L.append("- Rules " + result["rules_version"] + ": AAFDID capture " + result["aafdid_capture"].split(" ")[0] + ", checked live " + result["live_check"].split(":")[0])
    L.append("")
    groups = {}
    for it in result["items"]:
        groups.setdefault(it["group"], []).append(it)
    for g in ["at_focus", "by_event", "later", "ongoing", "as_required", "earlier", "conditional", "review", "triggered", "undetermined", "reference"]:
        lst = groups.get(g)
        if not lst:
            continue
        title = GROUP_TITLE[g]
        if g == "at_focus" and result["focus_event"]:
            title = "Due at " + result["focus_event"]["name"]
        L.append("## " + title + " (" + str(len(lst)) + ")")
        L.append("")
        if g == "undetermined":
            L.append("| Code | Requirement | Missing answer |")
            L.append("| --- | --- | --- |")
            for it in lst:
                L.append("| " + it["code"] + " | " + esc(it["name"]) + " | " + esc(", ".join(it.get("missing") or [])) + " |")
        elif g in ("conditional", "triggered", "review"):
            L.append("| Code | Requirement | Type | Condition or trigger | Source |")
            L.append("| --- | --- | --- | --- | --- |")
            for it in lst:
                cond = (it.get("due_text") or it["applies_when"]) if g == "triggered" else (when_text(it) if g == "review" else it["applies_when"])
                L.append("| " + it["code"] + " | " + esc(it["name"]) + " | " + TYPE_LABEL[it["type"]] + " | " + esc(cond) + " | " + esc(it["source"]) + " |")
        else:
            L.append("| Code | Requirement | Type | When | Approval | Source |")
            L.append("| --- | --- | --- | --- | --- | --- |")
            for it in lst:
                L.append("| " + it["code"] + " | " + esc(it["name"]) + " | " + TYPE_LABEL[it["type"]] + " | " + esc(when_text(it)) + " | " + esc(it.get("approval") or it.get("procedure") or "") + " | " + esc(it["source"]) + " |")
        L.append("")
    if result["questions_needed"]:
        L.append("## Questions that would settle the undetermined items")
        L.append("")
        for q in result["questions_needed"]:
            L.append("- " + q["text"] + " (" + q["id"] + "; affects " + str(q["affects"]) + ")")
        L.append("")
    cn = [n for n in result["currency_notes"] if n["applies_here"]]
    if cn:
        L.append("## Changes since AAFDID that affect this list")
        L.append("")
        for n in cn:
            L.append("- **" + n["title"] + "** (" + n["date"] + "). " + re.sub(r"\n+", " ", n["text"]) + " Source: " + "; ".join("[" + s["title"] + "](" + s["url"] + ")" for s in n["sources"]))
        L.append("")
    if include_not_applicable and groups.get("not_applicable"):
        L.append("## Not applicable (" + str(len(groups["not_applicable"])) + ")")
        L.append("")
        for it in groups["not_applicable"]:
            L.append("- " + it["code"] + " " + esc(it["name"]) + ". " + esc(it.get("reason")))
        L.append("")
    L.append("_" + result["disclaimer"] + "_")
    return "\n".join(L)


def to_checklist(result):
    if not result["pathway"]:
        return ""
    L = ["AAFDID checklist: " + (result["profile"].get("program") or result["pathway"]["name"])]
    for it in result["items"]:
        if it["status"] not in ("required", "conditional", "triggered"):
            continue
        tag = "" if it["status"] == "required" else " [" + ("may apply" if it["status"] == "conditional" else "if triggered") + "]"
        wt = when_text(it)
        L.append("- [ ] " + it["code"] + " " + it["name"] + tag + (" (" + wt + ")" if wt else ""))
    return "\n".join(L)


def main(argv):
    files = [a for a in argv if not a.startswith("--")]
    if not files:
        print(__doc__)
        return 2
    bundle = load_bundle()
    text = sys.stdin.read() if files[0] == "-" else Path(files[0]).read_text(encoding="utf-8")
    try:
        inp = json.loads(text)
    except ValueError:
        inp = parse_profile_block(text)
    result = evaluate(bundle, inp)
    if "--json" in argv:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    elif "--block" in argv:
        print(to_profile_block(bundle, inp))
    elif "--checklist" in argv:
        print(to_checklist(result))
    else:
        print(to_markdown(result))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
