# Steps to qualify an exact language profile

Qualification belongs to an exact catalog ID, version, dialect, category,
implementation build, libraries and claimed platform. A complete standard is
larger than a set of keywords: name binding, evaluation order, types, effects,
numeric/text representations, libraries, concurrency and host interactions also
determine what a program means. Related languages can share implementation work;
each retains its own normative obligations and evidence.

1. **Select the authority and scope.** Choose the complete published standard,
   revision and errata policy, or an exact upstream implementation/manual when no
   formal standard exists. Audit the category and dialect. Identify required
   libraries, implementation-defined choices, platforms, devices and licenses.
   A candidate URL or downloaded document is preparation, not a completed audit.
2. **Audit every normative rule.** Read the complete authoritative material and
   enumerate its grammar, static/dynamic semantics, mandatory APIs, permitted
   choices and conformance requirements. Map each clause to an explicit rule
   record. An exclusion needs exact citations and independent review; unavailable
   tools and unfinished work stay blocked, rather than becoming not applicable.
3. **Prepare real compatible hosts.** Install or bind the actual pinned native
   compiler, interpreter, validator, renderer, database, proof kernel, simulator
   or device. Verify artifacts and dependencies. Retain exact licensed-host and
   unavailable-device prerequisites with an owner and next action.
4. **Implement the frontend and semantics.** Build the actual parser and AST,
   binding/type rules, values, evaluation, mutation, errors, effects, text/numbers
   and applicable concurrency model. Exercise every production, required rule,
   invalid-input class and interaction. A lexer or keyword list cannot do this.
5. **Complete libraries and interoperability.** Inventory and implement every
   mandatory standard-library contract. Verify host services, ABI/layout,
   marshalling, callbacks, garbage collection/lifetimes, errors and async
   cancellation. Installing a same-named package is insufficient evidence.
6. **Implement and compare translation.** Lower real source semantics through a
   typed/effect IR into generated executable or processable artifacts. Freshly
   compare native and generated values, errors, state, effects and allowed
   ordering. Record semantic translation and native embedding separately. Reject
   unsupported or uncertain behavior instead of silently approximating it.
7. **Verify the original intent.** Write independent preconditions,
   postconditions, permitted effects, error and termination/liveness contracts;
   test held-out cases. A proof requires an adequate explicit model and a checked
   artifact under stated assumptions. Exhaustive finite tests prove only that
   finite domain. Arbitrary natural-language intent and unrestricted program
   equivalence cannot be universally proved by tests, syntax knowledge or a solver
   query that omits relevant behavior. Retain unmodelled proof obligations.
8. **Close normative conformance coverage.** Run applicable upstream suites,
   independently authored acceptance tests, negative/boundary tests, differential
   tests, properties and fuzzing. Retain and minimize counterexamples. Reconcile
   every normative clause and mandatory API against implementation and evidence.
   Passing a sample or suite does not fill unmapped semantic gaps.
9. **Qualify platforms and measure cost.** Run relevant contracts on every
   claimed OS/architecture/device/host. Check capabilities, isolation and resource
   limits, keeping limits distinct from standard semantics. Measure cold/warm
   end-to-end CPU, wall time, memory, storage and real admitted parallel work.
   Counts of virtual actors are not additional hardware or engineering capacity.
10. **Review and release the exact build.** Obtain independent review, close
    mandatory blockers, reproduce the package from a clean extraction, run the
    affected regressions and verify hashes. Publish exact scope and limitations.
    Changed semantics, libraries or platforms invalidate dependent evidence until
    affected checks are completed again.

These steps are executable acceptance contracts in `gate_plans.py`: all 18
existing obligation dimensions retain all 48 original leaf IDs. Creating the
contracts creates no normative rule records, execution observations or automatic
qualifications. The all-ID runner must instantiate them against every catalog
entry, including USL and future additions, and preserve open obligations.

The 48 leaf IDs are **project obligations**, not 48 already-audited clauses from
every language standard. The exact normative audit determines what each selected
standard actually mandates. Translation, independent intent proof, performance
measurement, deployment isolation and release review are additional project
requirements; they must not be advertised as universal ISO or language-standard
requirements. Normative language conformance, whole-implementation coverage,
translation preservation, intent proof and project release qualification therefore
keep separate claims and evidence. Nothing here grants ISO approval or
certification by an external standards body.

## Category-specific results

| Category | What must actually be checked |
| --- | --- |
| Source programs | Parse/type/binding rules, original and generated execution, values/errors/state/effects/ordering |
| Grammars, schemas and interfaces | Validation, acceptance/rejection, parse/model structures, generated target code and matching runtime |
| Templates | Native rendering, contextual escaping/includes, embedded-language checking and effects |
| Configuration and builds | Resolved graph, isolated application state, effects, failure behavior and declared idempotence |
| Documents and formats | Declared byte/structure/render/roundtrip relation, encoding, order/duplicate and rejection contracts |
| Transcripts, logs and protocol messages | Record/message/session processing, field/state/encoding rules and malformed inputs; recorded commands are data |
| Queries | Exact schema/fixtures/collation/timezone, multisets or declared ordering, NULLs, errors, updates and transactions |
| Proofs and analysis | Elaboration, actual kernel/checker judgments, axioms, bounds, rejected proofs/countermodels and unknown results |
| Devices and simulation | Exact revision/target, compilation, simulation and actual device results as separate evidence |
| Assembly and IR | ISA/IR, encoding/relocations, verification/linking, registers/memory/traps and exact ABI |

An executable snippet inside a transcript or template needs its actual embedded
runtime; parsing recorded output does not prove that snippet ran. A format does
not acquire a fictitious standalone CPU execution requirement. All categories
retain every original dimension until a reviewed applicability decision or a
complete category contract resolves it.

## Claims that remain separate

- **Bounded profile validated:** only the declared constructs, inputs, limits and
  observed platforms have evidence. Missing mandatory features prevent full
  qualification.
- **Full standard qualified:** all applicable obligations of the selected complete
  normative standard and its conformance class are resolved for the exact build
  and claimed platform profile. Internal engineering qualification must not be
  advertised as an external certification scheme.
- **Whole implementation qualified:** where no formal standard exists, the
  complete pinned implementation/manual baseline is covered. This does not create
  a formal standard or an official certification.
- **Semantic translation qualified:** source-to-target semantics have the stated
  coverage and preservation evidence. Delegating the source to its own native
  host remains native embedding.
- **Intent property proved:** the specific independent formal contract holds
  under its explicit model, domain and trusted assumptions. Other intent and
  unmodelled properties remain open.

Family reuse and exact content-addressed artifacts can reduce repeated work.
Independent ready tasks can run concurrently under actual resource admission.
Execution observations and external effects must be freshly observed. Shared
code, a common family, virtual worker count or a proposed equation cannot transfer
an unproved guarantee to another ID or remove a mandatory gate.
