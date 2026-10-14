# USL v4.11.4: 30 new bounded profiles and Ubuntu 26.04 validation

The fresh combined runs passed on Debian 13 and Ubuntu 26.04.1 LTS x86-64:
14 coordinator regressions, 199 family tests and 4,862 USL executions per host.
The seven family jobs validate 30 new bounded profiles. Coverage is now
277/606 original IDs; 329 still lack a bounded profile. Full-standard
qualifications and complete entity tracks remain zero.

Ubuntu validation uses a real digest-pinned Ubuntu container with the retained
workspace and native toolchains. This source download is an addon, not a
standalone installer: it excludes native binaries and the retained Python/Node
installation. A clean Ubuntu installation from source alone is not yet verified.
Read ubuntu/README.md and PLATFORM_MATRIX.json before reproducing that run.
The full fresh case evidence is in validation/debian and validation/ubuntu26;
native binaries and compiler caches are omitted and identified in the receipts.

This release adds actual source frontends, USL translations, native hosts and
independent intent checks to the retained247 bounded profiles. SUMMARY.json
records the exact new count after a fresh joined run; ALL359_PROGRESS.md retains
every original unimplemented ID, including those still needing implementation.
These are bounded language/processing profiles. Full-standard qualifications
and complete entity tracks remain zero. Preparation, installed tools and a
passed flag cannot replace semantic/native/conformance evidence.

The family implementations run concurrently using observed memory/descriptor
admission. All359 logical catalog actors start before release; actors share the
same exact family execution result where its tested profile applies. No actor
creates hardware or model tokens. Every external/native execution is fresh.
The USL coordinator independently checks the integer status join. The all359
audit preserves all6462 original dimension obligations and5385 ordered steps in
lossless factored objects, with each ID's exact references and dependencies.

Implemented families are kept in their own directories:

- agda: pure typed Nat/Bool expressions and Markdown literate Agda, original
  Agda-to-JavaScript compilation, actual USL and limited SMT preservation checks.
- preprocessor: Mozilla hash/percent control, macros and filters; selected CSS,
  JavaScript and namespace-aware XML processing contracts.
- templates: Haml, Slim and MaskJS nesting, bindings, escaping and selected
  conditional/loop constructs against native engines and independent HTML trees.
- configuration: selected make, ncurses, ICU, device-tree, Kconfig, OpenLDAP and
  isolated glibc record-processing contracts.
- native_languages: selected Wren, Berry and MoonScript typed statements plus
  R documentation processing.
- grammar_native: selected PEG recognition, BibTeX style execution, SWIG native
  bindings and WebIDL argument-conversion contracts.
- all359: the complete original backlog and selected Asymptote, OpenSCAD,
  GDScript and Robot Framework original/generated/intent tests.

Read each directory's README and exact receipt before relying on a feature.
Each record retains unsupported semantics, library/ABI/host requirements,
counterexamples, resource domain and full-standard/proof obligations. Exact
full versions, standards and normative dependency inventories still need audit.
An exhausted finite domain or a solver result retains its stated scope and
trusted assumptions. It does not prove arbitrary source or natural-language
intent. All other607-ID qualification obligations from v4.11.3 stay open.

```bash
source /workspace/.onboarding/activate-usl.sh
python -m unittest test_coordinator -v
python coordinator.py --source-root /workspace/usl-v4.10.0-clean-test \
  --output /tmp/usl-v4114-fresh
```

The root registry binds actual family source identities before jobs may count.
Fresh native and independent test receipts, not caller-supplied data, drive
the scoped join. Stored historical247 profiles are retained and explicitly not
freshly requalified by this new-family runner. Root progress records expose all
359 starting IDs; the reported remaining count excludes only newly validated
bounded profiles. It is separate from the full-standard completion count.

See TESTING_GUIDE.md for native provider restoration and portable dependency
paths. Source archives exclude native tool binaries and generated native caches;
they retain source, .usl artifacts, evidence, references and provenance. Preserve
all previous releases, main and user files. New work belongs in its own release
directory until reviewed, tested and packaged with fresh evidence.
