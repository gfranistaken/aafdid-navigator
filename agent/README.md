# Agent pack

This folder turns any capable LLM into an AAFDID assistant. The assistant can do three things:

- Interview a program office for the answers it needs.
- Print the program profile.
- List the information requirements that apply, grouped by decision point, with the same codes the web navigator shows.

Everything in this folder except this README is generated from `rules/aafdid-rules.json` by `tools/build_agent.py`. Edit the rules, not the generated files.

## What to load

| File | Where it goes | Size |
| --- | --- | --- |
| `AGENT_INSTRUCTIONS.md` | The agent's instructions or system prompt | about 2.5K characters |
| `knowledge/00-procedure.md` | Knowledge | procedure, profile format, pathway finder, output format, worked example |
| `knowledge/01-intake.md` | Knowledge | intake questions per pathway |
| `knowledge/10-mca.md` | Knowledge | MCA records plus a lookup matrix by program type and event |
| `knowledge/11-mta.md` … `15-aos.md` | Knowledge | one file per pathway |
| `knowledge/20-changes-since-aafdid.md` | Knowledge | changes after AAFDID's tables were last updated |
| `knowledge-combined/aafdid-knowledge-all.md` | Knowledge, instead of the nine files | use it when the platform limits the number of files |
| `tests/agent-test-scenarios.md` | **Not** knowledge | use it to check the agent's answers |

Every requirement record names its pathway and carries its own condition, so a retrieved chunk still makes sense on its own. The conditions use the same field names as the profile block. For example:

```
- Condition code: `contract_cost_type = yes AND contract_value >= 20,000,000 AND contract_value < 100,000,000`
```

## Set up by platform

### GenAI.mil Agent Designer
1. Create an agent and paste `AGENT_INSTRUCTIONS.md` into its instructions.
2. Upload the nine files in `knowledge/`. If the file limit is lower than nine, upload `knowledge-combined/aafdid-knowledge-all.md` instead.
3. Send `TAILCHECK`. The agent must answer `TAIL-OK-AAFDID-NAV-1`. Any other answer means the instructions were cut off.
4. Run a few scenarios from `tests/agent-test-scenarios.md` in fresh chats and score them.

The limits on instruction length, file count and file size were not yet measured when this pack was built. The [aafdid-agent-probe](https://github.com/gfranistaken/aafdid-agent-probe) kit measures them. If the probe shows that retrieval loses records deep in a large file, use the per-pathway files rather than the combined one.

### Claude (Projects) or ChatGPT (custom GPT)
Paste `AGENT_INSTRUCTIONS.md` into the project or GPT instructions and upload the knowledge files. Then run the same checks.

### Agents that can run code
Deterministic answers are better than a model reading tables. Clone this repository and run the engine:

```
node engine/cli.js profile.txt              # Markdown report
node engine/cli.js profile.txt --json       # machine-readable result
python3 engine/aafdid.py profile.txt        # same result from Python
```

A profile can be the text block below or JSON with the same fields. Use the knowledge files to explain the results.

## The profile block

```
AAFDID PROFILE v1
program: F3 replacement power supply
pathway: mta
event: entrance
mta_path: rf
mta_size: non_major
contract_value: 20m_to_50m
contract_cost_type: no
```

The web navigator prints this block in step 5, and agents print it when you say `show profile`. Paste it into a new chat to resume.

## How to judge an agent's answer

A good answer has these properties:

- Every code in the scenario's Required, May-apply and Also-review lines appears.
- None of the codes in the Must-not-list line appear as required, may apply or also review.
- Unknown answers become "Needs an answer" with a question, never a silent exclusion.
- Input it cannot use (scenario 23) is named, not silently dropped or guessed.
- It ends with the unofficial-overview caveat.

When an agent keeps missing records, move more of the work into code (the engine) or split the knowledge further.
