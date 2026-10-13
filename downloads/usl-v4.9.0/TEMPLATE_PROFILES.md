# v4.9 typed template processing profiles

Forty-four exact original catalog IDs now translate a declared finite template profile
into executable `.usl`. The implementation reads actual upstream ASTs or native
compiler tokens, lowers literal text and direct integer output nodes into a typed
template IR, and emits a USL function made only from string constants, bounded
integer parameters, `str`, and concatenation. Generated targets contain no
foreign source envelope or `engine_run` call.

This is a category-appropriate template processing profile. It does not qualify
full template standards, arbitrary embedded source programs, modules, libraries,
arithmetic expressions, loops, conditionals, filters, escaping directives,
includes, IO, object lookup, or native execution of JavaScript/Python host programs.
Genshi markup admits simple named XML tags without attributes or namespaces and
uses the genuine upstream text serializer for entity escaping. SQL host processing
admits two literal integer `SELECT` projections in a fresh in-memory SQLite
database. Rendering a JavaScript/Python template validates the resulting program's
syntax; it does not execute that resulting program.

The profile takes one or two explicitly named signed32 integer bindings. Every
binding must have a declared inclusive finite range; the Cartesian product is
capped at 4,096 contexts and 524,288 rendered UTF-8 bytes. Reserved `usl` harness
names and Cheetah compiler locals `trans` and `write` are rejected. Independent
intent specifies ordered literal/substitution segments, and independently authored
cases specify exact expected output strings. Boolean values, strings, missing or
extra context keys, and out-of-range integers fail admission.

## Exact IDs and actual engine

| Actual engine | Exact catalog IDs |
|---|---|
| Django | `django`, `css+django`, `html+django`, `javascript+django`, `xml+django` |
| Jinja2 | `sql+jinja`, `yaml+jinja` |
| Cheetah | `cheetah`, `html+cheetah`, `javascript+cheetah`, `xml+cheetah` |
| Mako | `mako`, `css+mako`, `html+mako`, `javascript+mako`, `js+mako`, `xml+mako` |
| UL4 | `ul4`, `css+ul4`, `html+ul4`, `js+ul4`, `py+ul4`, `xml+ul4` |
| Native Ruby ERB/Ripper | `erb`, `rhtml`, `css+ruby`, `javascript+ruby`, `xml+ruby` |
| Native PHP tokenizer/render | `css+php`, `html+php`, `javascript+php`, `xml+php` |
| Genshi text | `genshitext`, `css+genshitext`, `js+genshitext` |
| Genshi markup | `genshi`, `html+genshi` |
| Python Liquid | `liquid` |
| Native Node Handlebars 4.7.8 | `handlebars`, `html+handlebars` |

Each exact ID receives its own fresh original rendering, finite-domain comparison,
malformed native syntax test, host-category validation and runtime identity.
Related IDs share implementation code; qualification is not transferred across IDs.
Catalog names that list more than one engine are qualified only with the actual
engine shown above and its observed installed version.

## Validation and measured work reuse

`test_results/v4.9.0_semantic_templates.json` records all forty exact profiles.
The 19-by-19 qualification domain contains 361 contexts for each original ID:

- 14,440 fresh original native renders and 14,440 actual generated USL executions
  cover every declared context. Both must equal the independently specified intent.
- Three additional independently authored cases per ID produce 120 fresh native
  original renders, 120 actual USL executions and per-case host validation.
- Each ID also receives an actual upstream malformed syntax rejection. Together,
  the original-domain batches, independent-case programs and syntax probes use
  200 bounded original/negative worker programs. Runtime identity probes and
  host-parser subprocesses are additional real costs, not replayed observations.
- Exact upstream AST→typed IR→emitted USL AST structural identity is checked before
  the finite executions. Source, intent, expected cases, bounds, parser/runtime
  identities and typed IR are guarded against mutation.

The batch renderer compiles each admitted pure template once inside one fresh
bounded native worker and renders all 361 contexts there. This is reuse of a pure
compiled artifact; every output is newly observed. Up to two real qualification
processes run concurrently. No test output or external side effect is replayed.
The measured forty-profile qualifier finished in about 25.46 seconds on this
machine. That timing includes observed runtime identity checks and qualification
work; it is not a universal speedup guarantee.

Native render observations and all-domain USL results remain individually visible
in the report. `test_results/v4.9.0_template_counterexamples.json` preserves the
initial detected PHP repeated-binding and HTML parser-doctype counterexamples.
Those candidates were repaired and all forty profiles requalified freshly.

Host processors are lxml for XML/HTML, tinycss2 for CSS, Node's native syntax checker
for JavaScript, CPython AST for Python, SQLite for the finite SQL projection
profile and PyYAML safe loading for a flat integer map. The recorded provider
identities include actual installed source/native files and distribution records;
full platform/library/toolchain closures remain unqualified. POSIX process groups,
deadlines and bounded output are used. They are not an OS security sandbox.

## Run and API

```bash
source /workspace/.onboarding/activate-usl.sh
python -m tools.qualify_semantic_templates --workers 2 \
  --output test_results/v4.9.0_semantic_templates.json
python -m unittest discover -s tests -p 'test_v49_templates.py' -v
```

`usl_systems.semantic_templates` exports `LANGUAGES`,
`dependency_identity(language=None)`, `TemplateFrontend(language, source,
contract, cases)`, and `qualify_one(language)`. A frontend provides `lower()`,
`translate()` and `verify()`. Reports use `profile_kind='template_processing'`
and `full_standard_qualified=False`; this profile must be counted separately from
closed-source or function-fragment source translation profiles.

`examples/v49_templates/index.json` links all forty original templates, independent
intent contracts, cases and executable generated `.usl` examples. The latter
render the authored negative/positive case and print its result.

Python dependencies were already installed by the reusable cloud setup. The new
native Handlebars dependency is installed under the workspace and does not ship
native binaries. Its exact package and transitive lock are included as
`examples/v49_templates/node-package.json` and `node-package-lock.json`. Restore it
on another compatible host with:

```bash
mkdir -p /workspace/.onboarding/template-v49-node
cp examples/v49_templates/node-package.json \
  /workspace/.onboarding/template-v49-node/package.json
cp examples/v49_templates/node-package-lock.json \
  /workspace/.onboarding/template-v49-node/package-lock.json
npm ci --prefix /workspace/.onboarding/template-v49-node \
  --cache /workspace/.onboarding/template-v49-node/cache \
  --ignore-scripts --no-audit --no-fund
```

Set `USL_TEMPLATE_NODE_ROOT` to a different restored dependency directory when
needed. The Handlebars lock SHA-256 is
`95b0aedf96d486feb6fa47d07c3ace8bea7d3dad7c7d7f460b59126beb98ccc9`.
