#!/usr/bin/env python3
"""Check both engines against the scenario snapshots, and against each other.

  python3 tests/run_tests.py            compare with tests/expected/*.json
  python3 tests/run_tests.py --update   rewrite the snapshots from the JavaScript engine

Needs Node.js on the PATH for the JavaScript side.
"""
import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "engine"))
import aafdid as A  # noqa: E402

SCEN = sorted((ROOT / "tests" / "scenarios").iterdir())
EXP = ROOT / "tests" / "expected"
EXP.mkdir(exist_ok=True)

JS = r"""
const fs = require('fs'); const A = require(process.argv[1] + '/engine/aafdid.js');
const bundle = JSON.parse(fs.readFileSync(process.argv[1] + '/rules/aafdid-rules.json', 'utf8'));
const out = {};
for (const f of JSON.parse(process.argv[2])) {
  const input = A.parseInput(fs.readFileSync(f, 'utf8'));
  const r = A.evaluate(bundle, input);
  out[f] = { result: r, md: A.toMarkdown(r), block: A.toProfileBlock(bundle, input), checklist: A.toChecklist(r) };
}
process.stdout.write(JSON.stringify(out));
"""


def summary(r):
    return {
        "profile": r["profile"],
        "pathway": r["pathway"]["id"] if r["pathway"] else None,
        "focus_event": r["focus_event"]["id"] if r["focus_event"] else None,
        "counts": r["counts"],
        "derived": r["derived"],
        "questions_needed": [q["id"] for q in r["questions_needed"]],
        "currency_notes": [n["id"] for n in r["currency_notes"] if n["applies_here"]],
        "unrecognized": r["unrecognized"],
        "items": [[i["code"], i["status"], i["group"], i["type"]] for i in r["items"]],
    }


def main():
    update = "--update" in sys.argv
    files = [str(p) for p in SCEN]
    js = json.loads(subprocess.run(["node", "-e", JS, str(ROOT), json.dumps(files)], check=True, capture_output=True, text=True).stdout)
    bundle = A.load_bundle()
    failures = 0
    for f in files:
        inp = A.parse_input(Path(f).read_bytes().decode("utf-8", errors="replace"))
        py = A.evaluate(bundle, inp)
        name = Path(f).stem
        j = js[f]
        problems = []
        if py != j["result"]:
            problems.append("JSON result differs between engines")
        if A.to_markdown(py) != j["md"]:
            problems.append("Markdown differs between engines")
        if A.to_profile_block(bundle, inp) != j["block"]:
            problems.append("Profile block differs between engines")
        if A.to_checklist(py) != j["checklist"]:
            problems.append("Checklist differs between engines")
        snap = EXP / f"{name}.json"
        if update:
            snap.write_text(json.dumps(summary(j["result"]), indent=1, ensure_ascii=False) + "\n")
        elif not snap.exists():
            problems.append("no snapshot; run with --update")
        elif json.loads(snap.read_text()) != summary(j["result"]):
            problems.append("result differs from the snapshot")
        status = "ok" if not problems else "FAIL: " + "; ".join(problems)
        tag = "ok" if not problems else "FAIL"
        if problems:
            failures += 1
        c = j["result"]["counts"]
        print(f"{name:30s} {tag:4s}  req {c.get('required', 0):3d}  may {c.get('conditional', 0):3d}  review {c.get('review', 0):3d}  trig {c.get('triggered', 0):3d}  undet {c.get('undetermined', 0):3d}  n/a {c.get('not_applicable', 0):3d}")
        if problems:
            print("   " + status)
    print(f"\n{len(files) - failures} of {len(files)} scenarios passed" + (" (snapshots updated)" if update else ""))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
