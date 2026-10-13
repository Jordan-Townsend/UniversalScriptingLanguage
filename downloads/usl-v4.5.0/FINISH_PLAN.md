# Remaining work and execution plan for USL v4.5

Full606 semantic translation and the human-capability entity are unfinished. Current evidence:158 backend/format subsets,448 without such evidence,2 typed source-translation profiles,0 fully qualified standards. GLSL has compile/validation evidence without shader execution. All606 entries still need full qualification; the number of distinct standards is unresolved until alias/version/dialect audits finish.

The existing Python/JavaScript profiles preserve the explicitly supported integer/Unicode/list/function/branch/iteration/effect/error behavior. Full objects, closures, recursion, modules, floats, general libraries, async/concurrency, ABI/FFI and whole-program simulation proofs remain incomplete. The12 AST intent proofs cover bounded pure arithmetic, not arbitrary applications.

Primary families and their remaining shared engineering work:

| Family | Entries | Backend/format subsets | Without backend evidence | Shared next work |
|---|---:|---:|---:|---|
| Systems and native imperative | 35 | 14 | 21 | Reuse mature native frontends and exact numeric/layout/ownership models; qualify macros, undefined behavior and native ABI separately for each standard. |
| JVM and managed object languages | 12 | 4 | 8 | Reuse JVM bytecode/runtime integration, while implementing each source type system, modules, exceptions and Java library bindings. |
| .NET managed languages | 4 | 1 | 3 | Reuse the versioned CLR/IL/GC and .NET libraries; independently qualify C#/VB/F# source semantics, metadata, callbacks and async cancellation. |
| ML/Haskell and typed functional | 18 | 6 | 12 | Share typed functional IR machinery where justified; implement each type system, pattern matching, laziness/effects and runtime representation separately. |
| Lisp and related languages | 14 | 6 | 8 | Share reader/AST and closure infrastructure only for reviewed compatible profiles; preserve macros, evaluation order, numeric towers and dynamic binding. |
| BEAM languages | 3 | 2 | 1 | Use actual OTP/BEAM hosts and shared process/message transport; qualify each source grammar, pattern semantics, supervision and concurrency behavior. |
| Scripting and general application languages | 69 | 13 | 56 | Expand the real Python/JavaScript typed profiles with measured compatibility helpers; bind original runtimes for unsupported objects/modules/effects. |
| Array, numerical and statistical | 27 | 4 | 23 | Share typed array/storage and exact marshaling with explicit rounding/layout contracts; qualify every statistical function, toolbox and licensed runtime separately. |
| SQL and query languages | 26 | 5 | 21 | Use exact engine/dialect/schema versions; implement bindings, nulls, transactions and query effects, then compare complete results and state against native engines. |
| Templates and composite sources | 89 | 45 | 44 | Share host/template composition after audited escaping and context contracts; independently test render rules, embedded language semantics and injection boundaries. |
| Markup, documents and styles | 42 | 22 | 20 | Implement category-appropriate parse/validate/process/serialize behavior, Unicode and normalization; use exact document/style versions and independent roundtrip oracles. |
| Configuration, build and deployment | 50 | 8 | 42 | Use real build/configuration hosts and resolved dependency graphs; qualify evaluation, environment, command effects and cancellation, beyond accepting syntax. |
| Grammars, interfaces and schemas | 49 | 6 | 43 | Use mature generators/validators and shared schema IR where compatibility is reviewed; execute generated artifacts and qualify imports, diagnostics and resource behavior. |
| HDL, shaders and compute | 11 | 4 | 7 | Use real elaborators/simulators or shader compilers plus qualifying devices; preserve scheduling, precision, layout, linkage and target-specific execution semantics. |
| Assembly and intermediate representations | 14 | 2 | 12 | Use exact ISA/ABI/device profiles and actual assemblers/VMs; verify instruction effects, memory/layout and observable native behavior. |
| Shell and automation languages | 13 | 5 | 8 | Bind actual shell/automation hosts; preserve expansion, quoting, environment, process status, pipelines and external effects under explicit capabilities. |
| Logic, proof and verification | 20 | 2 | 18 | Use native proof/query engines and declared logic models; qualify unification, search, termination assumptions and trusted proof checkers. |
| BASIC and business procedural | 16 | 2 | 14 | Install genuine native tools where available; implement record/storage/control semantics, fixed/free dialects and exact proprietary host dependencies. |
| Stack and concatenative languages | 3 | 0 | 3 | Share a typed stack IR only with reviewed word/dictionary contracts; qualify stack effects, memory, numeric semantics and each native environment. |
| Esoteric languages | 4 | 0 | 4 | Implement each actual execution model with independently authored step traces and resource limits; resemblance or a keyword list cannot establish equivalence. |
| Domain-specific and classification pending | 45 | 3 | 42 | Resolve the actual domain/specification first, identify real upstream tools, and implement its category-appropriate contract; family classification remains provisional. |
| Transcripts, logs and protocol messages | 42 | 4 | 38 | Validate framing/prompts and replay pinned messages against the actual host; distinguish logs/diagnostics from executable programming-language sources. |

Exact implementation sequence:

1. **specifications** — Audit exact version, dialect, category, platform, licensing, normative chapters and complete library surface for every catalog ID. Resolve aliases without removing IDs. Reuse retrieved public sources and signed upstream source/doc archives; apply the saved network configuration before retrying denied references.

   Closure gate: Every entry has an audited versioned normative contract, explicit category-appropriate execution mode and chapter/feature obligations; unavailable hosts/licenses remain blocked.

2. **semantic ir** — Extend the typed/effect USL IR with float/integer policies, object/heap identity, mutation, closures and recursion, imports/modules, exceptions, ownership/lifetimes, IO effects, concurrency/async/cancellation and ABI contracts. Add explicit compatible runtime helpers where source semantics differ.

   Closure gate: Every accepted construct has a validated semantic representation and checked lowering; unsupported or uncertain semantics reject admission.

3. **family frontends** — Extend Python/JavaScript first; implement shared family infrastructure for native systems/LLVM/GCC, JVM, CLR, ML/Haskell, Lisp and BEAM, retaining each source grammar/type/runtime rules. Implement query/template/configuration/format/grammar/transcript IR and processing contracts by category.

   Closure gate: Actual source ASTs lower into typed USL semantics and genuine target translation; opaque native execution stays separately labelled.

4. **execution backends** — Add reviewed exact-version profiles for the448 entries without backend evidence; install available public upstream tools, real runtimes and libraries. Run programs, queries, renderers, format/schema processors, grammar generators and transcript hosts appropriately. Connect native macOS/Windows, licensed hosts and devices only when available.

   Closure gate: Fresh independent positive/negative/boundary/native cases pass with exact executable/dependency/platform identities; shaders require actual qualifying execution, not only compilation.

5. **libraries and interop** — Complete audited standard libraries and host APIs; qualify layout/marshaling, callbacks, GC/pinning and ownership, exceptions, shared memory, async and cancellation across actual native ABIs.

   Closure gate: Chapter/library coverage and independent source-target observable-state/effect/order/lifetime tests pass; JSON exchange cannot certify arbitrary native compatibility.

6. **intent and conformance** — Run authoritative suites, invalid/boundary/property/metamorphic/fuzz cases and native-versus-translated differential tests. Define original task intent contracts before generation; perform native typechecking, independent holdout acceptance and relevant AST/IR/SMT/model obligations. Independently review exact profile coverage.

   Closure gate: All applicable gates pass for the exact specification/profile. Unknown solver results, counterexamples, missing libraries, unmodelled effects and stale identities block promotion. Finite tests are not universal arbitrary-program proofs.

7. **entity learning and models** — Build grounded spatial/temporal/causal task planning and dialogue; working/episodic/semantic/procedural consolidation; general traceable study/hypothesis/independent experiment/skill acquisition; staged isolated candidate evaluation, unseen-task and restart/forgetting checks, promotion and rollback. Install actual pretrained models, train modality encoders on real paired datasets, use a new protected evaluation set and measure calibration/robustness/cost against baselines.

   Closure gate: Measured independent integrated tasks demonstrate each declared capability after restart; synthetic fixtures, generated speech and developmental image tests stay labelled; no general superiority/human claim without evidence.

8. **senses and subsystems** — Connect calibrated camera/microphone/speech, touch/force, position/joint, IMU/balance, temperature, chemical smell/taste and physical controllers with units, acquisition timestamps, frames and sync. Complete actual Shadow/Ollama, Swarm, Chrome, EmoVision, mesh/GPU and Ghostshell/Nexus task integration. Resolve missing intended client/model/worker protocols and assets.

   Closure gate: Actual device/model/controller tasks pass against independent calibrated references; desktop previews and software adapters are not live physical qualification.

9. **release qualification** — Rerun source-bound regressions and native/model/device/platform checks, package with manifests, validate clean extraction, publish authorized GitHub downloads and verify remote hashes. Update each of606 language records and21 entity tracks after every tranche.

   Closure gate: Every requested language and entity capability meets its exact gates. Until then overall_objective_complete remains false and no all-complete handoff is issued.

Family order: expand the already-tested Python/JavaScript source profiles; then native systems, JVM/CLR, typed functional/Lisp/BEAM; run query/template/format/schema branches in parallel where resources permit; complete numerical/business/logic/shell/assembly/HDL/domain-specific and transcript profiles using their real contracts. Keep platform/license/device dependencies explicit while independent code work continues.

Four exact classifications still need review: arrow (Arrow), flatline (Flatline), floscript (FloScript), rsl (RSL). Every classification still needs its normative standard/version audit.

Entity remainder: general grounded reasoning/planning/dialogue, durable consolidation, general verified self-study and skill transfer, measured neural learning/forgetting on fresh independent datasets, live calibrated senses/body control, real local model inference and functional subsystem protocols. The current demonstrated action is a bounded USL calculation, not physical embodiment. Existing desktop assets and TCP framing tests do not complete XR, multiplayer or EEG calibration.

External dependencies: apply/publish saved public-reference/dataset network settings; authorized macOS/Windows hosts; entitled SAP/ABAP, SAS, Stata, MATLAB and IDL runtimes; physical sensors/controllers and calibration; intended missing Ghostshell/nexus-earth sources/client/model/worker contracts. Codex can implement available software and tests; it cannot create absent host access, licenses or hardware.

Every tranche must pass source-bound regressions, real native/model tests, independent intent/conformance checks, clean-extraction validation and remote checksum verification before delivery. The ledger tracks15 dependent tasks and18 gate dimensions per catalog entry, plus21 entity tracks. Full standards stay unqualified until all relevant gates and independent review pass.

No all-complete continuation prompt or completion date is asserted while these implementation and dependency obligations remain.
