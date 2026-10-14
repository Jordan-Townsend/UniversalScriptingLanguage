# USL v4.11.3: full qualification requirements across the catalog

This addon applies the complete project qualification gate set to all607 current IDs:606 original IDs plus USL. It evaluates18 dimensions and48 preserved project requirement groups per ID (10,926 gates and29,136 groups). The exact normative clause count for all language standards remains unknown until their specifications are audited. These48 groups are requirements for our work, not an invented count of clauses in every standard.

Read `QUALIFICATION_STEPS.md` for the ten engineering steps and `results/ALL_ID_STATUS.md` for every ID. `ALL_ID_QUALIFICATION.json` retains every gate, dependency, evidence link and open leaf. `WORK_QUEUE.json` records10,926 tasks;607 initial acceptance checks can start at the identity gate, while independent source/tool/test preparation can proceed for all tasks.

## What this run completed

- All10,926 logical gate actors started before release;607 actual `.usl` policy executions independently matched the host closure calculation. There is no fixed-size round or actor cap. The local interpreter executes on one thread; these logical actors do not create additional hardware or reasoning agents.
-180 shared category/dimension contract artifacts serve10,926 requests, avoiding10,746 duplicate constructions. Only the contract text is shared. Each ID retains separate target bindings, normative clauses, applicability decisions, native/intent tests and final review. Total measured report-generation cost is retained in `RUN_COSTS.json`; it is not an implementation-throughput estimate.
- All223 files of the pinned v4.11.2 input snapshot were hash-checked. Five profiles received deep receipt/contract checks: Brainfuck, Forth, JSON and ANTLR Python/C++. Other historical bounded claims are preserved and clearly labelled. Past native outputs are historical evidence, not fresh executions in this audit.
- The JSON candidate contains62 enumerated records (30 grammar productions,10 uppercase requirements,22 prose obligations); independent contracts and available upstream source hashes were rechecked. Complete implementation proof, review and the relevant errata policy remain open.
-42 transcript/log/protocol entries now use a processing-category proposal. Exact per-ID category review remains required; families cannot settle language identity or applicability.
- A fresh USL host inventory records the real12 statement kinds,14 expression kinds,12 builtins and source locations. Its18 existing core tests pass. This does not supply a complete authoritative USL specification or qualify USL itself.
- The runner supports additional catalog IDs; independent tests exercised609 IDs using two explicitly synthetic extension fixtures. That tests registration/completeness, and does not claim two new language implementations.

The247 historical bounded original profiles remain unchanged. **Zero full standards and zero whole-implementation contracts are qualified.** The release has no complete-profile proof/certificate verifier. Raw `passed`, `verified`, solver or not-applicable flags cannot grant qualification; the host and executed `.usl` policy prevent that outcome. The clause-closure helper checks proposed structure only and executes no proof checker.

## Required steps

1. Select the exact standard/version, errata, dialect, category, libraries, implementation choices and platforms. Where no formal standard exists, select a reviewed versioned implementation contract and name that claim accurately.
2. Audit the full authoritative specification and inventory every applicable normative clause/API. Review and justify every not-applicable decision using source citations.
3. Provide compatible pinned native compilers/runtimes, processors, databases, proof kernels or devices, and record host/license dependencies.
4. Implement the real grammar, AST, binding/types, values, evaluation, errors, mutation, effects, text/numbers and applicable concurrency semantics.
5. Complete mandatory libraries, host APIs and interoperability/ABI, including ownership, callbacks, errors and cancellation.
6. Lower source semantics through the typed/effect IR and compare fresh native/generated results and observable effects. Native embedding remains a distinct route.
7. State independent intent contracts and verify them with suitable tests and checked proofs under explicit assumptions. Unrestricted program equivalence and arbitrary natural-language intent have no automatic universal verifier.
8. Close clause-to-code-to-test coverage using upstream, independent, invalid/boundary, differential, property and fuzz checks; repair every counterexample.
9. Validate all claimed platforms, resources/isolation and measured end-to-end costs. Distinguish standard conformance from additional project requirements.
10. Independently review the exact build, complete required proof/checker obligations, reproduce the release and rerun affected regressions before granting the exact qualification claim.

## Run

```bash
source /workspace/.onboarding/activate-usl.sh
cd /workspace/usl-qualification-v4.11.3
python full_qualification.py --source-root /workspace/usl-v4.10.0-clean-test --output fresh-gates
python usl_host_inventory.py --source-root /workspace/usl-v4.10.0-clean-test --output fresh-usl-host
python verify.py --source-root /workspace/usl-v4.10.0-clean-test --output /tmp/usl-v4113-check
```

The setup helper is `/workspace/.onboarding/restore_qualification_v4113.sh`. No new dependency installation or service is required beyond the retained v4.11.2 and v4.10 environment. Existing checkouts and old releases remain unchanged. Saved setup instructions require publication through environment settings; saving does not publish them.

The addon depends on the exact extracted v4.11.2 source ZIP with SHA256 `0ec8164764712255e29ea9a22f887e6629bcd21bf32d93d5974cccc4808f39ae` and the existing v4.10 runtime/dependencies. Use `--input-root /path/to/usl-planning-v4.11.2 --source-root /path/to/base` for standalone gate auditing. The regression harness uses the cloud's retained paths and JSONTestSuite fixtures. On another host, supply/restore those fixtures before claiming the same regression readiness. No native binaries or documentation bodies are bundled.

An additional-catalog JSON file is a list of entries with `catalog_id`, `category_candidate`, and optional `family`, `semantic_focus`, `host_candidate`, `external_dependencies`. Pass it with `--additional-catalog`. New entries retain all18 dimensions; no original ID is removed. Extensions cannot self-declare evidence, scope or qualification. The ten category names are exported in `gate_plans.CATEGORY_CONTRACTS`.

The full implementation, normative audit and formal-checker work remains open. The workload queue makes those gaps explicit; running the audit does not perform missing compiler, library or language-standard engineering. Completion ETA remains uncalibrated.
