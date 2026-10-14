# USL v4.11.2: all-ID preparation and concurrent native tranches

All 362 initially uncovered original IDs now have distinct preparation records. The current join has **247/606 validated bounded profiles** (84 code/expression, 163 category-processing), **359 without a profile**, **0 full standards** and **0/21 completed entity tracks**. Every original ID and the extra USL host remain present. Preparation records are implementation plans; complete normative semantics remain open.

Start with `current-scope-results/CURRENT_SCOPE.md` and `CURRENT_SCOPE.json`. The full all607 ledger is `scope-all-results/ALL_IDS.json`; it preserves the initial244/362 snapshot. `joined-results/qualification-ledger.json` records the three new promotions with source/evidence identities. `NEXT_READY_WORK.json` enqueues all359 remaining actions without fixed-size rounds.

## Concurrent work completed

- All607 scoping actors ran actual `.usl` policy checks. Every initially uncovered ID has an authored host candidate, three specific semantic focus items, category-appropriate native/intent contracts, source locators where available, dependencies and all18 original obligation dimensions. Twelve catalog identity traps were recorded. Exact version/authority/library/ABI audits remain open.
- Forth: a real Gforth0.7.3 amd64 frontend emits persistent-stack USL. The scoped profile covers44 selected words, prior colon-definition calls, conditionals and begin/until/while loops. 866 independent intent/native cases and917 USL executions passed. Independent adversarial review added251 native cases and250 successful USL executions, and found/fixed lexer, dictionary/harness and comment-boundary bugs. The maximum **live** stack depth is64, including intermediates; call/control/operation/time limits are explicit. I/O, memory/addressing, return-stack words, exceptions and the remaining standard/library surface are outside this profile. `forth-results/generated/` contains the actual Forth and emitted `.usl` sources. `rule-inventory.json` binds44 rules and7 control locators to source bytes in the pinned Debian package; this is an implementation-source audit, not a whole-standard audit.
- ANTLR: the original IDs `antlr-python` and `antlr-cpp` now have a bounded ANTLR4.9.2 literal-choice grammar profile, real generated native parsers and a generated USL predicate. 5,676 fresh native cases and5,686 USL executions passed. All5,676 case actors started together across four native jobs. Two Z3 proofs relate the actual generated equality/OR AST to independent whole-input membership contracts for all symbolic strings; they exclude correctness of ANTLR, its runtimes, the USL interpreter and whole-language semantics.
- Scheduler: arbitrary positive integer requested lane counts use sparse materialization. Tests include10**100 requested lanes with only the ready work materialized. Resource admission and prerequisites determine actual execution concurrency. Virtual counts do not create hardware or external engineering capacity.

Only exact pure artifacts, input bodies and syntax trees are shared. Native observations and effects are fresh. Compatibility is checked per profile; family membership does not transfer qualifications. Forth and ANTLR run concurrently in `verify_release.py`.

## Run in this cloud workspace

```bash
source /workspace/.onboarding/activate-usl.sh
cd /workspace/usl-planning-v4.11.2
python verify_release.py --source-root /workspace/usl-v4.10.0-clean-test --output /tmp/usl-v4112-test
python qualification_ledger.py --source-root /workspace/usl-v4.10.0-clean-test --output joined-results
python integrate_scoping.py
python planner.py --source-root /workspace/usl-v4.10.0-clean-test --catalog joined-results/catalog.json --lanes 1 137 607 10926 1000000000000000000 --output results
python scope_all.py --source-root /workspace/usl-v4.10.0-clean-test --inspect teal
```

`bash /workspace/.onboarding/restore_planning_v4112.sh` restores pinned providers and runs the development readiness checks. It has been executed here. Saving setup instructions does not publish the environment; publication remains in environment settings.

## Test an extracted download elsewhere

The ZIP contains this addon and source/reports, without native binaries or third-party documentation bodies. Supply the extracted v4.10 runtime from the earlier base download. Linux x86-64 with a Debian13-compatible C++ runtime, Java, g++, binutils, Python3.12, dpkg-deb and the base USL dependencies (including Z3/Lark) is the tested platform. Install those host prerequisites, activate your Python environment and set `PYTHONPATH` to your extracted base directory.

```bash
python restore_forth.py --destination providers/forth
python restore_antlr.py --destination providers/antlr
python restore_antlr_java.py --destination providers/antlr-java --archives providers/debs
python qualify_forth.py --source-root /path/to/base --prefix providers/forth --output fresh-forth
python qualify_antlr.py --source-root /path/to/base --prefix providers/antlr --jars providers/antlr-java/usr/share/java --output fresh-antlr
```

These provider paths are explicit overrides. `verify_release.py` and the full regression suite use the configured cloud provider defaults; use the two qualification commands above with overrides elsewhere. Provider installation preserves TLS/hash verification. A different machine still requires its own fresh validation. No other operating system or fresh unrelated host is certified by these results.

`scope_all.py` uses exported structural reference inventories and the private body cache when present. Without that cache it reports unavailable bodies and keeps source retrieval open. The recovery pass retrieved candidates for127 of137 initially missing IDs. There are349 of359 current remaining IDs with candidate bodies;10 still lack one (basemake, bugs, comal, croc, gooddata-cl, minid, mql, openedge, tasm, vgl). These are retrieval candidates pending version/authority/applicability audit; a successful HTTP response does not finish a semantic rule set.

## Continue towards the full objective

The next stage can start for prepared entries while other entries retrieve sources or acquire hosts. For each ID: pin the correct specification/dialect/category; map every applicable clause and library/host contract; implement and lower the actual semantics; run fresh native and independent intent tests; retain counterexamples; and qualify only the exact supported profile after its conformance/review gates pass. No global wait is required before independent implementation starts.

The conditional effort model keeps all9,090 original generic steps and10,908 dimensions. Its hour budgets are assumptions, and the full-project ETA remains unknown. Fast preparation/test execution is not evidence of semantic engineering throughput. All21 entity tracks and device/model/platform dependencies remain visible in `results/ENTITY_TRACKS.json`.

The inherited Brainfuck, JSON and earlier semantic-record results are preserved v4.11.1 evidence. They are not claimed as newly executed language qualifications in this release. Original v4.10/v4.11.0/v4.11.1 releases remain separate and unchanged.
