# Testing the addon

The small addon archive contains runnable source and complete current evidence. The combined archive additionally includes the unchanged v4.10 source ZIP. Extract that nested ZIP separately; point `--source-root` at the directory containing `usl_systems/` and `RELEASE_MANIFEST.json`. Preserve the v4.10 manifest; this addon does not rewrite its registry or evidence.

On the already prepared cloud instance:

```bash
source /workspace/.onboarding/activate-usl.sh
cd /workspace/usl-preparation-v4.11.0
bash setup-providers.sh
python run.py --source-root /workspace/usl-v4.10.0-clean-test --mode test --i-allow-execution
python run.py --source-root /workspace/usl-v4.10.0-clean-test --mode all --output my-fresh-results --offline --i-allow-execution
```

The default continuously schedules all10,926 actors and admits actual executors from the live memory budget; it does not split workers into fixed-size rounds. Use `--workers N` only to request a smaller physical executor budget.

`--mode all` freshly verifies6,638 retained-skill cases, transfers the prepared skill, inventories607 IDs, qualifies60 exact IDs, benchmarks the preparation strategies and builds all607 table entries. Execution and host programs are fresh; original learning holdouts are not re-sealed. `--offline` retains reference provenance without claiming fresh URL availability. Omit it to attempt public HTTPS resolution; HTTP success still does not complete a specification audit. Working-directory output is separate from packaged evidence.

Other modes: `prepare`, `qualify`, `race`, `skills`, `transfer`, `tables`, `test`. `tables` requires the preparation and qualification files in the chosen output. Nonzero exit means a required assertion/check failed; incomplete full standards are reported separately from this batch's checks. The command never claims all606 are implemented.

Outside this cloud instance, install the v4.10 requirements and the real native hosts before testing. New provider restoration requires Debian13, signed trusted APT indexes, `dpkg-deb`, an existing Python environment and Node/npm. Packages and expected SHA-256 are in `providers/debian-packages.json`; npm's full integrity lock is in `providers/package-lock.json`; added Python version pins are in `providers/python.lock.txt`. Base hosts include GCC/G++, NASM, LLVM19, Java/Javac, Ruby, GDC, Objective-C GCC, Ragel6, PHP8.4 with tokenizer/ctype/iconv, nginx and Meson. Native tool binaries are not shipped. Current tests do not certify another OS/architecture.

Optional path overrides: `USL_V411_PROVIDERS`, `USL_LLVM_ROOT`, `USL_PHP_EXTENSION_DIR`, `USL_ENV_ACTIVATE`; retain other v4.10 activation/tool paths. Providers are separate from older releases. Never override HOME. No public service or external message is sent by this addon.

For a native function through the API, put the frozen base on PYTHONPATH and import `NativeFrontend,source_for` from `native_profiles`; supply an exact catalog ID, canonical source, function `transform`, a `usl.intent.integer.v1` bounded int32 contract, and independent invocation results. `verify('python')` or `verify('javascript')` proves the admitted source/emitted AST models and freshly executes native, generated target and USL. Unsupported source/effects fail closed. The proof does not verify the entire compiler/runtime or arbitrary natural-language intent.

SHA256SUMS.json identifies every packaged file except itself. The companion `.sha256` covers the entire archive. Verify before extraction; extract into a new directory. No installer or check is automatically executed on extraction. Current reports retain all per-ID source, contracts, native diagnostics, counterexamples and CAS records.
