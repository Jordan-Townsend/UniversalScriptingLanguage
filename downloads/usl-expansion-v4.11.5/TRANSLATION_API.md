# Translate your own source into executable USL

`translate.py` accepts user programs in the exact bounded profiles implemented
by this addon. It calls the real frontend in an isolated Python subprocess,
writes `generated.usl` plus `receipt.json`, and optionally executes the generated
code with the hash-pinned USL runtime. Original native programs, servers,
templates, shaders and system commands are never automatically executed by this
CLI. The separate release qualification runner performs native differential
tests on its authored fixtures.

```bash
source /workspace/.onboarding/activate-usl.sh
cd /workspace/usl-expansion-v4.11.5
python translate.py --list
python translate.py /tmp/request.json --output /tmp/my-translation --run-usl
```

The output directory must be new, its parent must already exist, and it must
sit outside this release, the pinned runtime and preceding source directories.
Existing files, directories and symlink output paths are rejected. This makes
repeat invocations fail without replacing previous results. Supply a different
output directory for the next request.

The default runtime is `/workspace/usl-v4.10.0-clean-test`. Elsewhere supply
`--source-root /path/to/extracted/v4.10/source`; its `usl_systems/language.py`
must have SHA256
`28572d10c70421c71777a4562bbdd075acf6077d5ea4c3b9ebca3278e6dc76cc`.
The authenticated runtime file is loaded directly; adjacent package startup
code is not executed. Python dependencies such as Lark and, for optional shader
proofs, Z3 still need to be installed. Native provider binaries are not required
for these pure parser/emitter requests.

Requests contain only `catalog_id`, `source`, optional `inputs` and optional
`expected`. Catalog IDs are explicit and case-sensitive. Unknown IDs, implicit
aliases such as `nim`, unsupported input fields and unsupported source fail
with a nonzero exit status. Use catalog ID `nimrod` for the selected modern Nim
profile. A missing adapter produces an explicit unavailable error. `--list`
reports source presence separately from qualification.

| IDs | `inputs` schema | Observed result with `--run-usl` |
|---|---|---|
| `icon`, `nimrod`, `vala` | omitted or `{}` | `observed.stdout`; no semantic result variable |
| `janet`, `newlisp` | omitted or `{}` | integer or Boolean `observed.result` |
| `cirru` | omitted or `{}` | nested syntax-tree list; no execution-language claim |
| `apacheconf`, `lighttpd`, `vcl`, `vclsnippets` | exactly `{"path":"/r"}` or `{"paths":["/r","/r/x"]}` | one `[status,Location-or-reason]` or an ordered list of them |
| `treetop`, `antlr-ruby`, `antlr-csharp` | `{"text":"ab"}` | Boolean complete-input recognition |
| `jasmin` | `{"argument":7}` | signed32 return value; selected arithmetic errors fail USL assertions |
| `glsl`, `hlsl` | `{"pairs":[[0,1],[4294967295,2]]}` | ordered uint32 results from the selected pure function |
| `vue`, `ng2`, `html+ng2` | `{"bindings":{"title":"Hello"}}` | HTML string from the strict template profile |

Frontends enforce their documented syntax and semantic bounds. In addition,
this CLI limits requests to 64 KiB, source to 16 KiB, JSON nesting to 20, input
lists to 512 elements, server paths to 64, shader inputs to 256 pairs, grammar
text to 128 characters, and exact numeric JSON values to integer magnitude 2^64.
It rejects floating point and duplicate keys. Each worker has a 25-second wall
deadline, 18-second soft CPU budget, 768 MiB address-space budget and 128 file
descriptors. Generated execution has 1,000,000 operations, 5 seconds and 120 call
depth. A source accepted for translation can still exceed execution limits.
These service limits are additional bounds, not a promise to run arbitrary
programs or all of a language's normative features.

An `expected` object may contain an exact `stdout` string and/or a JSON
`result`. It requires `--run-usl`. Comparisons preserve JSON types: integer 1
does not equal Boolean `true`. A mismatch exits1 and retains the generated
source, observed output and failed checks. This is one caller-provided test;
it creates no qualification and proves no original intent or general semantic
equivalence. A successful request also creates no language qualification.
Invalid requests/path failures exit 2. Adapter/runtime/expectation failures exit 1
with a receipt when they reach the isolated worker.

For example, put this exact JSON in `/tmp/request.json`:

```json
{"catalog_id":"nimrod","source":"var x = 2\necho x + 3\n","expected":{"stdout":"5\n"}}
```

The resulting `generated.usl` is a standalone program for the specified USL
runtime. Template inputs are embedded as a fixed lookup function, and all other
selected inputs are likewise explicit in generated code. No Python `eval`,
shell interpolation or caller-selected module path is used to handle source.

Additional requests:

```json
{"catalog_id":"janet","source":"(let [x 7] (* x 3))","expected":{"result":21}}
```

```json
{"catalog_id":"apacheconf","source":"Redirect 302 /r https://example.invalid/to\n","inputs":{"paths":["/r/x","/rx"]},"expected":{"result":[[302,"https://example.invalid/to/x"],[404,""]]}}
```

```json
{"catalog_id":"treetop","source":"grammar Probe\nrule start\n\"ab\"\nend\nend\n","inputs":{"text":"ab"},"expected":{"result":true}}
```

```json
{"catalog_id":"glsl","source":"#version 450\nuint evaluate(uint x,uint y){return x + y;}","inputs":{"pairs":[[4294967295,2],[7,3]]},"expected":{"result":[1,10]}}
```

For GLSL/HLSL only, add `--prove-ir` to independently invoke the solver-backed
check of the typed uint32 IR against the actual emitted function return AST.
A successful `unsat` result covers all 2^64 uint32 argument pairs under the
recorded semantic model and assumptions. The receipt retains solver input,
assumptions and exclusions. It does not prove parser correctness, interpreter
correctness, native compiler/Vulkan behavior, the caller's intended function,
or full-standard conformance. A finite expected-result check has the separate
scope described above.

Receipts include source/request/generated hashes, adapter source hashes,
runtime identity, optional observed results, operations and limited proof
evidence. They explicitly mark `full_standard_qualified`, `qualification_created`
and `native_original_executed` false. The release's all-ID backlog remains the
authority for outstanding language implementation and qualification work.
