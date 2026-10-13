# USL workload follow-through bundle

This bundle contains the unchanged v4.5.0 full source plus a separate runnable
workload addon. The bundle label is v4.5.1; the underlying USL runtime remains
v4.5.0. It is a tested development snapshot, not full language or entity
completion.

Start with `ACTION_PLAN.md` and `DECISION_TREE.md`. `FINISH_PLAN.md` describes the
remaining language-family and entity obligations. `results/action_plan.json`
preserves all 606 catalog IDs and their outstanding gates.

The `.usl` supervisor actually runs native differential/intent checks, chooses a
measured workload route, searches six USL native targets, verifies factored and
incremental arithmetic, and losslessly collapses the evidence available before
the collapse step. Execution results are always fresh. Source/runtime/dependency
identities and artifact hashes protect the limited translation cache.

## Test the downloaded bundle

Verify the ZIP against its companion `.sha256` file, then extract it. Work from
the extracted source root, using Python 3.12 and an installed Node runtime with
BigInt support. Linux/POSIX is the qualified host. Core USL and this Python-to-JS
workload use the standard library. Native targets need genuine installed tools;
the source bundle does not contain compiler/runtime binaries.

```bash
python workload_followthrough/verify_files.py --root .
python -m usl_systems run examples/hello.usl
python workload_followthrough/run.py --source-root . --output followthrough-results --i-allow-execution
```

On the existing cloud machine, activate the installed tools first:

```bash
source /workspace/.onboarding/activate-usl.sh
```

For the addon regression tests, from the source root:

```bash
export USL_SOURCE_ROOT="$PWD"
cd workload_followthrough
python -m unittest test_workload
```

The measured success search tests Python, JavaScript, Ruby, PHP, C and C++.
Install available genuine tools using the base `NATIVE_RUNTIME_SETUP.md` and
`tools/setup_native_v45.py` instructions. Unavailable candidates remain recorded
as unavailable/failed; they do not become qualified by resembling another
language. Additional AI, sensor, catalog and platform features have their own
base dependency instructions and qualification status.

`--i-allow-execution` explicitly enables the trusted bundled native fixtures.
The runner has time/output/resource budgets; its native processes inherit the
host's access and are not an operating-system security sandbox.

## Read the measured results

`RESULTS.md` and `RESULTS_SUMMARY.json` summarize the final recorded run.
`results/results.json` contains all calibration trials, native observed outputs,
independent expected values, held-out results, costs, worker counts, candidate
attempts, arithmetic audit accounting and equation applicability. The serialized
codec frame and its exact CAS object are also included.

Strategies are selected before the held-out workload. Timing is host-specific;
the held-out comparison is one pair, preceded by three calibration trials per
route. The declared cost combines CPU seconds, wall seconds and cache bytes.
No physical-energy savings, universal speedup, full-program proof or general
neural superiority is asserted.

Current base status remains 158 backend/format subsets, 448 entries without
such evidence, two typed translation profiles and zero fully qualified
standards. All 606 catalog entries and the human-capability entity still need
their full qualification work.
