# All 606 catalog entries: families and remaining work

The build records native execution or format-processing subset evidence for **158 of 606 entries**; **448** lack that evidence. **0 full standards are qualified, so 606 entries still require full qualification.** These are separate counts, not a percentage of semantic completion.

Typed source translation has tested finite profiles for **2 source languages**. This does not qualify their entire standards or every generated application. A parser installation, native wrapper or passed scalar case cannot close the broader gates.

[Open the standalone searchable table](LANGUAGE_COMPLETION_TABLE.html) or [download the 606-row CSV](LANGUAGE_COMPLETION_TABLE.csv). The HTML works locally with no service or network dependency. It groups entries, filters names/aliases/status and shows each entry's remaining work, exact external dependencies and evidence references.

Each ID has one primary implementation family so the totals sum to 606. Tags retain overlap: F# also targets .NET; Clojure also uses the JVM; templates combine host and embedded languages. Families organize shared work and do not prove shared semantics. The catalog contains versions, duplicate descriptors, templates, documents and transcripts. The number of distinct standards remains unresolved until the version/dialect/alias identity audit finishes.

| Primary family | Entries | Native/format subsets | Typed source subsets | Full standards | Still need full qualification |
|---|---:|---:|---:|---:|---:|
| Systems and native imperative | 35 | 14 | 0 | 0 | 35 |
| JVM and managed object languages | 12 | 4 | 0 | 0 | 12 |
| .NET managed languages | 4 | 1 | 0 | 0 | 4 |
| ML/Haskell and typed functional | 18 | 6 | 0 | 0 | 18 |
| Lisp and related languages | 14 | 6 | 0 | 0 | 14 |
| BEAM languages | 3 | 2 | 0 | 0 | 3 |
| Scripting and general application languages | 69 | 13 | 2 | 0 | 69 |
| Array, numerical and statistical | 27 | 4 | 0 | 0 | 27 |
| SQL and query languages | 26 | 5 | 0 | 0 | 26 |
| Templates and composite sources | 89 | 45 | 0 | 0 | 89 |
| Markup, documents and styles | 42 | 22 | 0 | 0 | 42 |
| Configuration, build and deployment | 50 | 8 | 0 | 0 | 50 |
| Grammars, interfaces and schemas | 49 | 6 | 0 | 0 | 49 |
| HDL, shaders and compute | 11 | 4 | 0 | 0 | 11 |
| Assembly and intermediate representations | 14 | 2 | 0 | 0 | 14 |
| Shell and automation languages | 13 | 5 | 0 | 0 | 13 |
| Logic, proof and verification | 20 | 2 | 0 | 0 | 20 |
| BASIC and business procedural | 16 | 2 | 0 | 0 | 16 |
| Stack and concatenative languages | 3 | 0 | 0 | 0 | 3 |
| Esoteric languages | 4 | 0 | 0 | 0 | 4 |
| Domain-specific and classification pending | 45 | 3 | 0 | 0 | 45 |
| Transcripts, logs and protocol messages | 42 | 4 | 0 | 0 | 42 |

The shortest defensible path is to build reusable semantic components in tested tranches:

1. Audit exact standards and supported hosts first. Reuse mature upstream frontends, libraries and conformance suites; keep platform/license blockers separate from implementation work.
2. Expand the existing real Python/JavaScript typed translation with independent requirements and differential cases. Preserve concrete differences in numbers, Unicode, identity, exceptions and effects. Unsupported behavior must fail explicitly.
3. Build source frontends on shared versioned IR infrastructure by family: native/LLVM tooling, JVM, CLR, typed functional languages, Lisp and BEAM. A common backend can share engineering work; each source type system and standard still needs its own audit and tests.
4. Qualify query engines, template composition, configuration evaluation, formats, grammar generators and transcripts by their actual execution contracts. Do not invent conventional program execution for documents or logs.
5. Extend library coverage and real interoperability: ABI, marshaling, callbacks, GC/ownership, exceptions, state/effect ordering and cancellation. Compare complete observable behavior against the original hosts.
6. Run upstream chapter-traced conformance, independent holdouts, invalid/boundary/property/metamorphic/fuzz tests and relevant formal checks. Promote a versioned profile only after current evidence and independent review pass; preserve unfinished broader features.
7. Schedule executable USL worker sets on measured host resources, sharing exact immutable reports and reviewed compatible frontends. Re-run execution when relevant identities change. Native external effects cannot be collapsed or replayed from a cache.

Full working support still requires, for each exact standard/profile: complete relevant grammar and static/dynamic semantics, numeric/Unicode/data behavior, effects/concurrency, library/host surface, genuine translation or declared native route, independent intent acceptance, ABI/interoperability, authoritative conformance, resource/safety checks and actual claimed platforms. No credible calendar estimate follows from counting keywords or catalog rows.

Known external requirements include an entitled SAP ABAP host, macOS AppleScript runner, Windows AutoHotkey/AutoIt runners, and licensed SAS, Stata, MATLAB and NV5 IDL runtimes. A compatible open implementation can be qualified as its own explicit profile; it cannot automatically certify a proprietary language/toolbox or unavailable host.

**4 entries still need an exact family classification review.** Domain-specific entries retain concrete specification/backend tasks instead of being forced into a misleading family. Every row remains visible.

Shared work by primary family:

- **Systems and native imperative:** Reuse mature native frontends and exact numeric/layout/ownership models; qualify macros, undefined behavior and native ABI separately for each standard.
- **JVM and managed object languages:** Reuse JVM bytecode/runtime integration, while implementing each source type system, modules, exceptions and Java library bindings.
- **.NET managed languages:** Reuse the versioned CLR/IL/GC and .NET libraries; independently qualify C#/VB/F# source semantics, metadata, callbacks and async cancellation.
- **ML/Haskell and typed functional:** Share typed functional IR machinery where justified; implement each type system, pattern matching, laziness/effects and runtime representation separately.
- **Lisp and related languages:** Share reader/AST and closure infrastructure only for reviewed compatible profiles; preserve macros, evaluation order, numeric towers and dynamic binding.
- **BEAM languages:** Use actual OTP/BEAM hosts and shared process/message transport; qualify each source grammar, pattern semantics, supervision and concurrency behavior.
- **Scripting and general application languages:** Expand the real Python/JavaScript typed profiles with measured compatibility helpers; bind original runtimes for unsupported objects/modules/effects.
- **Array, numerical and statistical:** Share typed array/storage and exact marshaling with explicit rounding/layout contracts; qualify every statistical function, toolbox and licensed runtime separately.
- **SQL and query languages:** Use exact engine/dialect/schema versions; implement bindings, nulls, transactions and query effects, then compare complete results and state against native engines.
- **Templates and composite sources:** Share host/template composition after audited escaping and context contracts; independently test render rules, embedded language semantics and injection boundaries.
- **Markup, documents and styles:** Implement category-appropriate parse/validate/process/serialize behavior, Unicode and normalization; use exact document/style versions and independent roundtrip oracles.
- **Configuration, build and deployment:** Use real build/configuration hosts and resolved dependency graphs; qualify evaluation, environment, command effects and cancellation, beyond accepting syntax.
- **Grammars, interfaces and schemas:** Use mature generators/validators and shared schema IR where compatibility is reviewed; execute generated artifacts and qualify imports, diagnostics and resource behavior.
- **HDL, shaders and compute:** Use real elaborators/simulators or shader compilers plus qualifying devices; preserve scheduling, precision, layout, linkage and target-specific execution semantics.
- **Assembly and intermediate representations:** Use exact ISA/ABI/device profiles and actual assemblers/VMs; verify instruction effects, memory/layout and observable native behavior.
- **Shell and automation languages:** Bind actual shell/automation hosts; preserve expansion, quoting, environment, process status, pipelines and external effects under explicit capabilities.
- **Logic, proof and verification:** Use native proof/query engines and declared logic models; qualify unification, search, termination assumptions and trusted proof checkers.
- **BASIC and business procedural:** Install genuine native tools where available; implement record/storage/control semantics, fixed/free dialects and exact proprietary host dependencies.
- **Stack and concatenative languages:** Share a typed stack IR only with reviewed word/dictionary contracts; qualify stack effects, memory, numeric semantics and each native environment.
- **Esoteric languages:** Implement each actual execution model with independently authored step traces and resource limits; resemblance or a keyword list cannot establish equivalence.
- **Domain-specific and classification pending:** Resolve the actual domain/specification first, identify real upstream tools, and implement its category-appropriate contract; family classification remains provisional.
- **Transcripts, logs and protocol messages:** Validate framing/prompts and replay pinned messages against the actual host; distinguish logs/diagnostics from executable programming-language sources.

The continuation/handoff prompt for an all-complete build is withheld while these gates are unfinished. The machine ledger and this table provide the resumable state.

Evidence used to generate these counts:

- `test_results/v4.4.0_sweep/full_606_sweep.json` — SHA-256 `04689297b55bb116ce6416b2b678c16f8d20b58a7a2f09cb8312ca19e3eaaa32`.
- `test_results/v4.5.0_completion_ledger/current_native_evaluations.json` — SHA-256 `e085854cbfdadeaf4c9721d073f2e5e4bb86667f4c3bbe5be355634f83b2c244`.
- `test_results/v4.5.0_completion_ledger/state/ledger.json` — SHA-256 `4e9f2bd32207f536805ffb3098effbea641524ea7285ad46f43c0564c8d9ef38`.
- `test_results/v4.5.0_semantic_translation.json` — SHA-256 `76a5d0967c14fabc121a5e8f36ccb4653a87818c0185d2bf0ca2b84890a1df12`.
