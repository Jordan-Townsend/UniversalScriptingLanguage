# USL v4.11.1 — rule implementation, semantic workers and schedule model

This separate addon preserves the published v4.10/v4.11 sources and archives.
It adds a real Brainfuck→USL frontend, a complete published JSON grammar and
rule inventory with parser/generator→USL processing, all607 source-discovery
workers, and executable conditional scheduling/resource/context equations.

Current joined coverage: **244 scoped original IDs; 362 without a scoped profile;
0 fully qualified standards; 0/21 completed entity tracks**. Scope includes
83 code/expression and161 category-processing profiles. JSON is a data format.
The base service still exposes its historical v4.10 registry; these additions
use the addon CLIs and explicit receipt/record joins.

All607 discovery workers start together. The latest run bound384 IDs to verified
reference bodies, indexed10,724 document sections, preserved all15/18 per-ID
steps/dimensions and hash-verified every factored join. These are structural
inventories, not complete semantic rules for all languages. The detailed
RULE_SET_PROGRESS.json distinguishes the JSON rule set and bounded Brainfuck
profile from the remaining unaudited/missing implementations.

Brainfuck:426 independent cases,849 fresh native executions and426 actual USL
executions. All256 byte inputs for increment are checked. The public ebfc2.0
compiler is pinned by commit and18 source hashes. Beef1.2 provides additional
native comparisons. Byte0xFF with EOF-zero/255 is explicitly rejected because
Beef treats0xFF as EOF; ebfc supports EOF-same. Tape/depth/resource and extension
limits are declared. Nontermination/resource exhaustion returns unknown/error.

JSON:30 published RFC8259 grammar productions,10 operative uppercase statements
and22 prose/interoperability rules are inventoried and mapped to implementation.
318 upstream cases plus612 independent vectors pass;1556 fresh native parsing
cases and626 actual generated-USL data translations were checked. Three upstream
cases exceed declared permitted resource limits and are recorded separately.
Two independent-review roundtrip counterexamples are fixed and retained as tests.
Full implementation proof and certification remain open. Published December2017
text is the exact target; an official errata5318 conflict is disclosed separately.

The context view is85.5% smaller by serialized bytes than the full per-ID record
file. Full records, failures and identities remain available. This does not change
service quotas and is not a measurement of model tokens or total engineering gain.

## Run in this environment

```bash
source /workspace/.onboarding/activate-usl.sh
cd /workspace/usl-planning-v4.11.1
python -m unittest -v test_planner test_semantics test_json_semantics test_semantic_records
python semantic_workers.py --source-root /workspace/usl-v4.10.0-clean-test --output fresh-semantic --fresh-brainfuck
python planner.py --source-root /workspace/usl-v4.10.0-clean-test --scoped-receipt fresh-semantic/brainfuck/qualification.json --output fresh-plan
python qualify_json.py --source-root /workspace/usl-v4.10.0-clean-test --output fresh-json
python qualify_json_intent.py --source-root /workspace/usl-v4.10.0-clean-test --output fresh-json
python context_pack.py --source-root /workspace/usl-v4.10.0-clean-test --ids json,brainfuck,usl --output focused-context.json
```

Linux x86-64 is the tested native host. Elsewhere install the extracted v4.10
runtime dependencies, set PYTHONPATH to its directory, and pass that directory
as --source-root. Install the public Beef1.2 interpreter and make/gcc. Restore
ebfc from its hash-pinned public sources with:

```bash
python restore_ebfc.py --destination providers/ebfc
python brainfuck_semantics.py --source-root /path/to/base --ebfc providers/ebfc/ebfc --output fresh-brainfuck
git clone https://github.com/nst/JSONTestSuite.git providers/JSONTestSuite
git -C providers/JSONTestSuite checkout 1ef36fa01286573e846ac449e8683f8833c5b26a
python qualify_json.py --source-root /path/to/base --suite providers/JSONTestSuite --output fresh-json
```

No native binaries or whole third-party reference bodies are shipped. Tests and
results do not substitute for proof of every possible program's intent.

## Execute your own data or program

```bash
python json_cli.py --source-root /path/to/base --input example.json --output roundtrip.json --emit-usl example.usl
python brainfuck_semantics.py --source-root /path/to/base --program example.b --input input.bin --emit-usl program.usl --run-output output.bin
```

JSON duplicate generation rejects by default; --duplicate-policy preserve opts
into the documented lossless preservation of duplicate input members.

## Rebuild the source discovery records

This requires the existing v4.11 preparation results/CAS and the private verified
reference cache. The downloadable v4.11 addon contains validated/preparation.json
and its objects. Pass --preparation explicitly outside the original workspace.

```bash
python semantic_records.py --source-root /path/to/base --preparation /path/to/v4.11/validated/preparation.json --private-cache /path/to/reference-cache --output new-records --fetch-missing
```

Cached bodies advertised by the input manifest must exist and match their hashes;
an empty cache cannot validate historical snapshot claims. The exported records
are independently readable without that cache. New sources are processed as data.

## Time estimate

Read results/REPORT.md and edit assumptions.json. All hour allocations are
unmeasured budget scenarios, not forecasts or probability ranges. Shared family
and IR work is factored once, prerequisites overlap, and engineering capacity is
kept separate from CPU/virtual-worker counts. Host/license waits, unresolved
research and full entity effort are unknown. The whole-project ETA stays null.

For example, the reference scenario assumes8352 remaining scoped-profile
engineering hours and553280 full pinned-profile hours. At20 effective engineering
lanes ×32 productive hours/week the hypothetical schedules are15.3weeks and
16.6years, excluding external waits. These are arithmetic consequences of assumed
budgets; we have no measured whole-standard completion rate to support a finish
date. Future unbuilt acceleration is not credited as guaranteed speedup.

The full objective remains the original all-language and entity goal. This
delivery closes concrete implementation/tests and retains the remaining work.
