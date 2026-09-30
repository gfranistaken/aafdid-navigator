#!/usr/bin/env python3
"""Build the agent pack in agent/ from rules/aafdid-rules.json.

agent/AGENT_INSTRUCTIONS.md       paste into the agent's instructions field
agent/knowledge/*.md              upload as knowledge files (one per pathway, plus procedure and intake)
agent/tests/agent-test-scenarios.md   do not upload; use it to check the agent's answers

Every requirement record names its pathway and carries its own condition, so a
retrieved chunk still makes sense on its own.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "engine"))
import aafdid as A  # noqa: E402

B = json.loads((ROOT / "rules" / "aafdid-rules.json").read_text(encoding="utf-8"))
AG = ROOT / "agent"
KN = AG / "knowledge"
TS = AG / "tests"
KN.mkdir(parents=True, exist_ok=True)
TS.mkdir(parents=True, exist_ok=True)

PW = {p["id"]: p for p in B["pathways"]}
Q = {q["id"]: q for q in B["questions"]["questions"]}
CUR = {n["id"]: n for n in B["currency"]["notes"]}
META = B["meta"]
DISCLAIMER = "Unofficial. AAFDID is an overview: comply with its tabular notes and the full text of each cited source."
APB_CODE = next(r["code"] for r in B["requirements"] if r["name"] == "ACQUISITION PROGRAM BASELINE (APB)")
CITE_EXAMPLE = f"{APB_CODE} ACQUISITION PROGRAM BASELINE (APB)"
EVERY_EVENTS = [(p, e) for p in B["pathways"] for e in p["events"] if e.get("every")]
GATE_WORD = {"dote_oversight": "DOT&E oversight only", "it_type": "IT only", "mission_critical_it": "mission-critical IT only"}
STATUS_WORD = {"event": "Required", "recurring": "Required (recurring)", "contract": "Required (contract-level)",
               "compliance": "Required (compliance action)", "conditional": "May apply", "triggered": "Only if triggered",
               "reference": "Reference rule"}
TYPE_WORD = {"statutory": "Statutory", "regulatory": "Regulatory", "both": "Statutory and regulatory", "unspecified": "Not stated"}


def cond_code(c):
    """Readable, exact form of a condition."""
    if "const" in c:
        return "always (every program on this pathway)"
    if "all" in c:
        return " AND ".join(wrap(cond_code(x)) for x in c["all"])
    if "any" in c:
        return " OR ".join(wrap(cond_code(x)) for x in c["any"])
    if "not" in c:
        return "NOT " + wrap(cond_code(c["not"]))
    f = c["field"]
    if "eq" in c:
        v = c["eq"]
        return f"{f} = {'yes' if v is True else 'no' if v is False else v}"
    if "in" in c:
        return f"{f} is one of {{{', '.join(c['in'])}}}"
    for op, sym in (("gte", ">="), ("gt", ">"), ("lte", "<="), ("lt", "<")):
        if op in c:
            return f"{f} {sym} {c[op]:,}"
    raise ValueError(c)


def wrap(s):
    return f"({s})" if (" AND " in s or " OR " in s) else s


def when_line(r, pw):
    if r.get("when"):
        ev = {e["id"]: e for e in PW[r["pathways"][0]]["events"]}
        return "; ".join(f"{ev[w['event']]['name']} ({w['submission']})" for w in r["when"])
    return r.get("due_text") or "Not tied to one event"


def record(r, pw_id):
    pw = PW[pw_id]
    L = [f"### {r['code']} · {r['name']}", ""]
    L.append(f"- Pathway: {pw['code']} ({pw['name']}). Table: {r['table_name']}.")
    L.append(f"- Status when the condition holds: {STATUS_WORD[r['kind']]}.")
    L.append(f"- Applies when: {r['applies_when']}")
    L.append(f"- Condition code: `{cond_code(r['applies_if'])}`")
    if r.get("conditional_if"):
        L.append(f"- May apply instead when: `{cond_code(r['conditional_if'])}`")
    L.append(f"- When due: {when_line(r, pw)}")
    if r.get("type_rule"):
        tr = r["type_rule"]
        unk = tr.get("unknown")
        unk_txt = (f" If that is unknown: {TYPE_WORD[unk]}." if unk and unk != "depends" else " If that is unknown, the type depends on the answer.")
        aaf = f" AAFDID TYPE: {r['type_text']}" if r.get("type_text") else ""
        if tr.get("events"):
            evn = {e["id"]: e["name"] for e in PW[r["pathways"][0]]["events"]}
            at = ", ".join(evn[e] for e in tr["events"])
            L.append(f"- Type by event: if `{cond_code(tr['if'])}`, {TYPE_WORD[tr['then']]} at {at}, and {TYPE_WORD[tr['else']]} at its other events. "
                     f"Otherwise {TYPE_WORD[tr['else']]}.{unk_txt}{aaf}")
        else:
            L.append(f"- Type: {TYPE_WORD[tr['then']]} if `{cond_code(tr['if'])}`, otherwise {TYPE_WORD[tr['else']]}.{unk_txt}{aaf}")
    else:
        L.append(f"- Type: {TYPE_WORD[r['type']]}." + (f" AAFDID TYPE: {r['type_text']}" if r.get("type_text") else ""))
    if r.get("approval"):
        L.append(f"- Approval: {r['approval']}")
    if r.get("procedure"):
        L.append(f"- Procedure: {r['procedure']}")
    if r.get("source"):
        L.append(f"- Source: {r['source']}")
    if r.get("notes"):
        L.append(f"- AAFDID note: {r['notes']}")
    for f in r.get("footnotes") or []:
        L.append(f"- Footnote: {f}")
    if r.get("tool_note"):
        L.append(f"- Tool note: {r['tool_note']}")
    for c in r.get("currency") or []:
        L.append(f"- Changed since AAFDID ({CUR[c]['title']}): see 20-changes-since-aafdid.md, note {c}.")
    L.append(f"- Page: {r['url']}")
    L.append("")
    return "\n".join(L)


def mca_matrix(reqs):
    ev = [e for e in PW["mca"]["events"]]
    head = "| Code | Requirement | MDAP | MAIS | II | III | " + " | ".join(e["short"] for e in ev) + " |"
    sep = "| --- | --- | " + " | ".join(["---"] * (4 + len(ev))) + " |"
    rows = [head, sep]
    for r in reqs:
        if r["table"] != "ms":
            continue
        c = r["applies_if"]
        parts = c.get("all") or [c]
        typed = [pt for pt in parts if pt.get("field") == "mca_program_type"]
        types = set(typed[0]["in"]) if typed else {"mdap", "mais", "acat_ii", "acat_iii"}
        gates = [GATE_WORD.get(pt.get("field"), pt.get("field")) for pt in parts if pt.get("field") and pt.get("field") != "mca_program_type"]
        marks = ["●" if t in types else "" for t in ("mdap", "mais", "acat_ii", "acat_iii")]
        w = {x["event"]: ("I" if x["submission"] == "initial" else "U") for x in r["when"]}
        cells = [w.get(e["id"], "") for e in ev]
        name = r["name"].replace("|", "/")
        extra = "".join(f" ({g})" for g in gates)
        rows.append(f"| {r['code']} | {name}{extra} | " + " | ".join(marks) + " | " + " | ".join(cells) + " |")
    return "\n".join(rows)


def pathway_file(pid, num):
    pw = PW[pid]
    reqs = [r for r in B["requirements"] if pid in r["pathways"]]
    L = [f"# {pw['code']} requirements: {pw['name']}", ""]
    L.append(f"Knowledge file {num} of the AAFDID Navigator agent pack, rules {META['version']}. Every record below belongs to the {pw['code']} pathway only.")
    L.append("")
    L.append(f"- Governing instruction: {pw['instruction']}")
    L.append(f"- Summary: {pw['summary']}")
    L.append(f"- Decision authority: {pw['decision_authority']}")
    L.append(f"- Events, in order: " + "; ".join(f"`{e['id']}` = {e['name']}" + (" (not a next event)" if e.get("every") else "")
                                             for e in pw["events"]))
    for n in pw.get("notes") or []:
        L.append(f"- Note: {n}")
    L.append(f"- AAFDID page: {pw['aafdid_url']}")
    L.append("")
    if pid == "uca":
        ar = pw["also_review"]
        L.append("## Also review MCA entries")
        L.append("")
        tabs = " and ".join(f"`{t}`" for t in ar["tables"])
        L.append(f"{ar['reason']}")
        L.append("")
        L.append(f"For a UCA program, go through the MCA records in 10-mca.md from tables {tabs} (codes MCA-M.. and MCA-X..):")
        L.append("")
        L.append(f"1. If `uca_acat` is unknown, list none of them. Ask the ACAT question first, because it decides which MCA entries apply.")
        L.append(f"2. Otherwise test each record's Condition code with `{ar['map_field']['to']}` set to the program's `{ar['map_field']['from']}` value (`acat_ii` stays `acat_ii`; `acat_iii` stays `acat_iii`) and every other field from the profile.")
        L.append("3. False: leave the record out. MDAP-only rows always drop out this way.")
        L.append("4. Unknown: list it under Needs an answer, naming the missing field (for example `dote_oversight`).")
        L.append("5. True: list it under \"Also review: MCA entries AAFDID points UCA programs to\", with status Also review, its MCA code, and its MCA events.")
        L.append("")
    if pid == "aos":
        L.append("## Services category (S-CAT)")
        L.append("")
        L.append("| S-CAT | Rule | Decision authority |")
        L.append("| --- | --- | --- |")
        for s in B["scat"]:
            L.append(f"| {s['label']} | {s['rule']} | {s['decision_authority']} |")
        L.append("")
        L.append(f"Source: {B['scat_cite']}. Special Interest overrides the dollar category.")
        L.append("")
    if pid == "mca":
        L.append("## Lookup matrix: Milestone and Phase Information Requirements")
        L.append("")
        L.append("● = applies to that program type. I = initial submission at that event; U = update. Read the program type column and the next-event column together. A row marked (DOT&E oversight only) also needs `dote_oversight` = yes; the record's Condition code is the full rule.")
        L.append("")
        L.append(mca_matrix(reqs))
        L.append("")
    tables = []
    for r in reqs:
        if r["table_name"] not in tables and r["table"] != "evm":
            tables.append(r["table_name"])
    for r in reqs:
        if r["table_name"] not in tables:
            tables.append(r["table_name"])
    for t in tables:
        L.append(f"## {t}")
        L.append("")
        for r in reqs:
            if r["table_name"] == t:
                L.append(record(r, pid))
    return "\n".join(L).rstrip() + "\n"


def intake_file():
    L = ["# Intake questions", "", "Knowledge file 01 of the AAFDID Navigator agent pack.", ""]
    L.append(B["questions"]["intro"])
    L.append("")
    L.append("Ask the questions for the program's pathway in the order below, one per message. Always offer \"not sure\". Record each answer under its field name using the value in the left column of its options table.")
    L.append("")
    for pid in ["mca", "mta", "uca", "swa", "dbs", "aos"]:
        pw = PW[pid]
        prof = {"pathway": pid}
        qs = [q for q in A.visible_questions(B, prof)]
        L.append(f"## {pw['code']}: {pw['name']}")
        L.append("")
        for i, q in enumerate(qs, 1):
            L.append(f"{i}. `{q['id']}`: {q['text']}")
            if q["id"] == "pathway":
                L.append(f"   - Answer `{pid}` for this section.")
            elif q["id"] == "event":
                L.append("   - Values: " + "; ".join(f"`{e['id']}` = {e['name']}" + (f" (also: {', '.join(e['aliases'])})" if e.get("aliases") else "")
                                             for e in pw["events"] if not e.get("every")) + ". Leave blank to list every event.")
            elif q.get("type") == "boolean":
                L.append("   - Values: `yes`, `no`, or leave blank if not sure.")
            elif q.get("type") == "money":
                L.append("   - Values (ranges): " + "; ".join(f"`{o['value']}` = {o['label']}" for o in q["options"]))
                L.append("   - Ask for the range, never the exact amount. If the user gives an amount anyway, record the range it falls in.")
            else:
                L.append("   - Values: " + "; ".join(f"`{o['value']}` = {o['label']}" + (f" (also: {', '.join(o['aliases'])})" if o.get("aliases") else "") for o in q["options"]))
                for o in q["options"]:
                    if o.get("help"):
                        L.append(f"     - `{o['value']}`: {o['help']}")
            L.append(f"   - Why it matters: {q['why']}")
            if q.get("gates"):
                g = [c for c in q["gates"] if any(pid in r["pathways"] and r["code"] == c for r in B["requirements"])]
                if g:
                    L.append(f"   - Affects: {', '.join(g)}")
                ar = pw.get("also_review")
                if ar:
                    rv = [c for c in q["gates"] if c not in g]
                    if rv:
                        L.append(f"   - Also affects these MCA entries to review (12-uca.md): {', '.join(rv)}")
        L.append("")
    return "\n".join(L).rstrip() + "\n"


def procedure_file():
    f = B["finder"]
    L = ["# How to work: AAFDID Navigator procedure", "", "Knowledge file 00 of the AAFDID Navigator agent pack. Read this first.", ""]
    L += [
        "## What this is",
        "",
        f"A rule base for finding which AAFDID information requirements apply to a DoW acquisition program. It has {META['requirements']} records across six pathways.",
        f"- AAFDID capture: {META['aafdid_capture']}.",
        f"- Live check: {META['live_check']}.",
        f"- Acquisition of Services: {META['aos_source']}.",
        "",
        "## Program profile block",
        "",
        "The profile is the program's answers. Read it when pasted, and print it exactly like this when asked:",
        "",
        "```",
        "AAFDID PROFILE v1",
        "program: <name>",
        "pathway: <mca|mta|uca|swa|dbs|aos>",
        "event: <the next event's id from the pathway file, or omit>",
        "<field>: <value>",
        "unknown: <comma-separated fields not answered yet>",
        "```",
        "",
        "Only fields asked for the pathway appear (see 01-intake.md). Booleans are `yes` or `no`. Dollar fields hold a range id, such as `contract_value: 20m_to_50m`, never an amount.",
        "",
        "When reading a pasted profile, match values to the options in 01-intake.md, including the listed synonyms (\"ACAT IC\" is `mdap`; \"Milestone B\" is `ms_b`). If a field is not an intake field for the pathway, or a value matches no option, say which ones you could not use and treat those fields as unknown.",
        "",
        "## Pathway finder",
        "",
        f"{f['intro']} Ask in this order and stop at the first yes.",
        "",
    ]
    for i, s in enumerate(f["steps"], 1):
        yes = PW[s["yes"]["result"]]["code"]
        no = s["no"].get("result")
        L.append(f"{i}. {s['text']} Yes: {yes}." + (f" No: {PW[no]['code']}." if no else " No: next question."))
        L.append(f"   - {s['help']} ({s['cite']})")
    L += [
        "",
        "## Procedure for \"which requirements apply?\"",
        "",
        "1. Confirm the pathway. If the profile has none, run the pathway finder.",
        "2. Note the next event (`event`). If it is missing, list requirements by event instead of splitting them.",
        "3. Open the pathway's knowledge file. Use only records whose Pathway line names that pathway. The one exception is UCA, which also reviews some MCA rows (see 12-uca.md).",
        "4. For each record, test its Condition code against the profile. `always` holds for every program on the pathway. A field the profile does not answer is unknown. `AND` is false if any part is false, and unknown if any part is unknown. `OR` is true if any part is true, and unknown if any part is unknown.",
        "   Dollar answers are ranges (01-intake.md lists them), cut at the thresholds the rules use. Compare using the amounts inside the range: `contract_value >= 20,000,000` is true for `20m_to_50m` and false for `under_20m`, and `contract_value > 50,000,000` is false for `20m_to_50m`.",
        "5. Assign a status:",
        "   - The condition holds: use the record's \"Status when the condition holds\". Required, May apply, Only if triggered, or Reference rule.",
        "   - The condition is false but the \"May apply instead when\" code holds: May apply.",
        "   - The condition, or the \"May apply instead when\" code, is unknown: Needs an answer. Name only the fields that keep it unknown (skip parts of an `OR` that are already false), and ask their questions from 01-intake.md.",
        "   - Otherwise: Not applicable. Give the Applies-when text as the reason.",
        "6. Work out the type. If the record gives a type rule (Statutory if ..., otherwise ...), apply it to the profile. If its field is unknown, use the type the record gives for that case, or say the type depends on that answer, and ask the question. A \"Type by event\" rule gives each event its own type: show it beside each event (for example `MS B (update, statutory)`), and give the record the type at the next event when it is due there, otherwise Statutory and regulatory if its events differ.",
        "7. Group the Required items when a next event is given:",
        "   - Due at the next event: the When-due line includes the next event."
        + "".join(f" {p['code']} records due at \"{e['name'].split(' (')[0]}\" are due at every decision point, so they always go here." for p, e in EVERY_EVENTS),
        "   - Due at later events: it includes an event after the next one.",
        "   - Ongoing: no event, such as recurring reports, contract-level items and compliance actions.",
        "   - As required: its only events are AAFDID's \"Other\" column, not a numbered decision point.",
        "   - From earlier events: all its numbered events come before the next one (it may also be due at Other). It should already exist; check for updates.",
        "   Without a next event, list Required items under Due by event (with their events) and Ongoing.",
        "   When the next event is Other, list the items due at Other first (Due at Other), then the rest under Due by event.",
        "8. Then list, in this order: May apply, Also review (UCA only, see 12-uca.md), Only if triggered, Needs an answer, Reference rules, then Not applicable.",
        "9. After the lists, add the questions that would settle more of the list: the ones behind Needs-an-answer items, types that depend on an answer, and for UCA the ACAT question.",
        "10. Then add the \"Changed since AAFDID\" notes attached to listed records, and the notes in 20-changes-since-aafdid.md that change the answer. Then Not applicable, then the caveat below.",
        "",
        "## Output format",
        "",
        "Use this layout. Code, name, type, when, approval and source come from the record.",
        "",
        "```",
        "# AAFDID requirements: <program name>",
        "- Pathway: <name> (<code>), <instruction>",
        "- Next event: <event name, or 'not given; all events listed'>",
        "- Counts: <n> required, <n> may apply, <n> also review, <n> triggered, <n> need an answer, <n> not applicable",
        "  (leave out \"also review\" when there are none)",
        "",
        "## Due at <event name> (<n>)",
        "| Code | Requirement | Type | When | Approval | Source |",
        "...",
        "## Due by event (<n>)  (when no next event is given, or the next event is Other)",
        "## Due at later events (<n>)",
        "## Ongoing, contract-level and compliance items (<n>)",
        "## As required (<n>)",
        "## From earlier events (<n>)",
        "## May apply: check the condition (<n>)",
        "| Code | Requirement | Type | Condition | Source |",
        "## Also review: MCA entries AAFDID points UCA programs to (<n>)  (UCA only)",
        "## Only if triggered (<n>)",
        "## Needs an answer (<n>)",
        "| Code | Requirement | Missing answer |",
        "## Reference rules (<n>)",
        "## Questions that would settle more of the list",
        "## Changes since AAFDID that affect this list",
        "## Not applicable (<n>)  (list codes and reasons; may be shortened if asked)",
        "",
        DISCLAIMER,
        "```",
        "",
        "## Tailoring",
        "",
        "- Statutory requirements stay unless the statute itself allows a waiver (AAFDID MCA overview).",
        "- The decision authority can tailor regulatory requirements. Record the decisions in writing, usually in the ADM or the approved acquisition strategy.",
        "- Items marked \"Part of Acquisition Strategy\" belong inside the strategy, not in separate documents.",
        "- Never call a statutory item tailorable, and never invent a waiver authority.",
        "",
        "## Rules that prevent wrong answers",
        "",
        "- Never add a requirement that is not a record in the knowledge files. If the user asks about one, say it is not in the AAFDID knowledge files.",
        "- Never treat unknown as no. Unknown means Needs an answer.",
        "- Keep dollar thresholds as written, with their dollar basis. Do not convert them.",
        f"- Cite by code and name, for example `{CITE_EXAMPLE}`.",
        "- Record codes belong to this rules release. Record ids in the JSON (`rules/aafdid-rules.json`) stay stable across releases.",
        "",
        "## Worked example",
        "",
    ]
    ex = json.loads((ROOT / "tests" / "scenarios" / "01-mta-rf-nonmajor-f3.json").read_text())
    res = A.evaluate(B, ex)
    L.append("Profile:")
    L.append("")
    L.append("```")
    L.append(A.to_profile_block(B, ex))
    L.append("```")
    L.append("")
    L.append("Correct result (the not-applicable list is left out):")
    L.append("")
    L.append(A.to_markdown(res, include_not_applicable=False))
    L.append("")
    return "\n".join(L).rstrip() + "\n"


def changes_file():
    L = ["# Changes since AAFDID's tables", "", "Knowledge file 20 of the AAFDID Navigator agent pack.", "", B["currency"]["aafdid_status"], ""]
    for n in B["currency"]["notes"]:
        L.append(f"## {n['id']}: {n['title']} ({n['date']})")
        L.append("")
        L.append(n["text"])
        L.append("")
        for s in n["sources"]:
            L.append(f"- Source: {s['title']}: {s['url']}")
        at = n.get("attach") or {}
        codes = sorted({r["code"] for r in B["requirements"] if n["id"] in (r.get("currency") or [])})
        if codes:
            L.append(f"- Attached to: {', '.join(codes)}")
        if at.get("questions"):
            L.append(f"- Also matters for the intake questions: {', '.join(at['questions'])}")
        L.append("")
    return "\n".join(L).rstrip() + "\n"


def instructions_file():
    files = ["00-procedure.md", "01-intake.md", "10-mca.md", "11-mta.md", "12-uca.md", "13-swa.md", "14-dbs.md", "15-aos.md", "20-changes-since-aafdid.md"]
    return f"""# AAFDID Navigator agent

You help DoW program offices find which AAFDID information requirements apply to a program, and when each is due. Use only the knowledge files. Never invent a requirement, citation, threshold, approval authority or waiver.

## Knowledge files
- 00-procedure.md: how to work, the profile block, the pathway finder and the output format. Follow it exactly.
- 01-intake.md: the intake questions for each pathway.
- 10-mca.md, 11-mta.md, 12-uca.md, 13-swa.md, 14-dbs.md, 15-aos.md: one file per pathway. Each record names its pathway. Use only records from the program's pathway. UCA also reviews some MCA rows, as 12-uca.md explains.
- 20-changes-since-aafdid.md: changes made after AAFDID's tables were last updated.

## Conversation
1. If the user pastes a block starting "AAFDID PROFILE v1", adopt it as the program profile. Name any field or value you can't match to 01-intake.md and treat it as unknown.
2. If the user says "start intake", or asks for requirements without a profile, ask the intake questions for their pathway from 01-intake.md. Ask one question per message, in order, and always allow "not sure". Ask for dollar ranges, never exact amounts. If they don't know the pathway, run the pathway finder first.
3. When the user says "show profile", print the profile block exactly as 00-procedure.md shows it, and nothing else.
4. When asked which requirements apply, follow the procedure in 00-procedure.md and use its output format.

## Rules
- Test each record's Condition code against the profile. A missing answer is unknown. List that record under "Needs an answer" with the question that settles it. Never guess, and never treat unknown as no.
- Keep AAFDID's own words for names, types, sources, approval authorities and notes. Quote notes when asked for detail.
- Statutory items cannot be tailored unless the statute allows a waiver. The decision authority may tailor regulatory items. If the source does not state something, say "source does not state".
- Cite each requirement by code and name, for example "{CITE_EXAMPLE}".
- Point out every "Changed since AAFDID" note that is attached to a listed record.
- End every requirements answer with: "{DISCLAIMER}"
- If a question is outside the knowledge files, say "Not in the AAFDID knowledge files" and name the source to check.

## Check
If the user types exactly TAILCHECK, reply exactly: TAIL-OK-AAFDID-NAV-1
"""


def tests_file():
    L = ["# Agent test scenarios", "",
         "Use these to check an agent built from this pack. **Do not upload this file as knowledge.**",
         "",
         "For each scenario:",
         "",
         "1. Start a new chat.",
         "2. Paste the profile block.",
         "3. Ask: \"Which requirements apply?\"",
         "4. Score the answer. It should list every code in the Required, May-apply and Also-review lines, and none of the codes in the Must-not-list line.",
         "",
         "For a fuller comparison, run the same profile through the web navigator or the engine: `node engine/cli.js <profile>`.",
         "",
         "Also check that `TAILCHECK` returns `TAIL-OK-AAFDID-NAV-1` exactly. If it doesn't, the instructions were cut off.",
         ""]
    engine_only = {"28-bom-odd-json"}  # JSON-encoding quirks that only the engines see
    for f in sorted((ROOT / "tests" / "scenarios").iterdir()):
        if f.stem in engine_only:
            continue
        inp = A.parse_input(f.read_bytes().decode("utf-8", errors="replace"))
        res = A.evaluate(B, inp)
        if not res["pathway"]:
            continue
        by = {}
        for it in res["items"]:
            by.setdefault(it["status"], []).append(it["code"])
        L.append(f"## {f.stem}")
        L.append("")
        L.append("```")
        if res["unrecognized"]:
            # Give the agent the raw answers, so the test checks that it flags what it cannot use.
            L.append(A.BLOCK_HEADER)
            L += [f"{k}: {A.format_value({'type': 'boolean'} if isinstance(v, bool) else {}, v)}" for k, v in inp.items()]
        else:
            L.append(A.to_profile_block(B, inp))
        L.append("```")
        L.append("")
        if res["focus_event"]:
            at = [it["code"] for it in res["items"] if it["group"] == "at_focus"]
            L.append(f"- Due at {res['focus_event']['name']} ({len(at)}): {', '.join(at) or 'none'}")
        for st, word in (("required", "Required"), ("conditional", "May apply"), ("review", "Also review"), ("triggered", "Only if triggered"), ("undetermined", "Needs an answer")):
            if st == "review" and not by.get(st):
                continue
            codes = by.get(st, [])
            L.append(f"- {word} ({len(codes)}): {', '.join(codes) if codes else 'none'}")
        if res["questions_needed"]:
            L.append(f"- Questions to ask: {', '.join(q['id'] for q in res['questions_needed'])}")
        na = by.get("not_applicable", [])
        L.append(f"- Must not list as required, may apply or also review ({len(na)}): {', '.join(na) if na else 'none'}")
        if res["unrecognized"]:
            L.append("- The agent should say it could not use: " + "; ".join(f"{u['field']} = {u['value']} ({u['reason']})" for u in res["unrecognized"]))
        sc = res["derived"].get("services_category")
        if sc:
            L.append(f"- Services category: {sc['label']}; decision authority: {sc['decision_authority']}")
        L.append("")
    return "\n".join(L).rstrip() + "\n"


files = {
    KN / "00-procedure.md": procedure_file(),
    KN / "01-intake.md": intake_file(),
    KN / "10-mca.md": pathway_file("mca", "10"),
    KN / "11-mta.md": pathway_file("mta", "11"),
    KN / "12-uca.md": pathway_file("uca", "12"),
    KN / "13-swa.md": pathway_file("swa", "13"),
    KN / "14-dbs.md": pathway_file("dbs", "14"),
    KN / "15-aos.md": pathway_file("aos", "15"),
    KN / "20-changes-since-aafdid.md": changes_file(),
    AG / "AGENT_INSTRUCTIONS.md": instructions_file(),
    TS / "agent-test-scenarios.md": tests_file(),
}
CO = AG / "knowledge-combined"
CO.mkdir(parents=True, exist_ok=True)
combined = "\n\n---\n\n".join(text for p, text in files.items() if p.parent == KN)
files[CO / "aafdid-knowledge-all.md"] = ("# AAFDID Navigator knowledge, all files combined\n\n"
    "Use this single file when a platform limits the number of knowledge files. It is the nine files in agent/knowledge joined in order.\n\n---\n\n" + combined)
for p, text in files.items():
    p.write_text(text, encoding="utf-8")
    print(f"{p.relative_to(ROOT)}: {len(text):,} chars")
