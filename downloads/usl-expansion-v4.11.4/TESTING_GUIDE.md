# Run fresh validation

Both Debian 13 and Ubuntu 26.04.1 LTS x86-64 passed the complete 30-profile
workflow: 14 root tests, 199 family tests and 4,862 fresh USL executions on each.
Ubuntu-specific setup also passed 19 tests. See PLATFORM_MATRIX.json for the
exact scope and validation/ for the full source, intent and native receipts.
The earlier 247 bounded profiles were retained, not freshly requalified here.

For Ubuntu, start with ubuntu/README.md. The tested target uses a real Ubuntu
26.04 container plus retained mounted toolchains and workspace dependencies.
The ZIP alone is insufficient for a clean Ubuntu machine. The retained CPython,
Node, Agda and other native prerequisites are not bundled; a standalone
source-only Ubuntu bootstrap remains unverified.

Use the retained cloud environment for the exact qualified Linux host builds.
Activate /workspace/.onboarding/activate-usl.sh. The runtime dependency is the
unmodified v4.10 USL source at /workspace/usl-v4.10.0-clean-test. Baseline status
comes from /workspace/usl-planning-v4.11.2, and the full607-ID requirements are
retained in /workspace/usl-qualification-v4.11.3. Dependency archives and their
SHA256 values are listed in DEPENDENCIES.json.

The complete cloud readiness command is:

```bash
bash /workspace/.onboarding/restore_expansion_v4114.sh
```

The root runner supports --source-root, --previous and --output. Run output
outside the extracted source tree. Providers must first be restored using the
family instructions below. Then:

```bash
python -m unittest test_coordinator -v
python coordinator.py --source-root /absolute/path/usl-v4.10.0 \
  --previous /absolute/path/usl-planning-v4.11.2 \
  --output /absolute/path/fresh-validation
```

The coordinator verifies registered source identities, completes each family
test suite, runs fresh native/USL/intent comparisons and joins all359 actors.
It fails if a family omits IDs, changes source during execution, fails its
tests, lacks actual native/USL counts or attempts to promote a full standard.
Read SUMMARY.json and each FAMILY_RECEIPTS.json entry; all native case counts
and physical process counts remain distinct. Historical247 bounded profiles
are retained without a new native execution claim for those old observations.

The family READMEs specify pinned native prerequisites and restoration recipes.
Small downloadable provider archives are checksum verified; Debian providers
also use the signed release/index chain. Preserve TLS/signature/hash checks.
Runners require the listed exact versions and refuse unsupported syntax or
domains. Installation and native syntax checks alone do not qualify a profile.
Host builds include Agda/Node, Ruby/Lua/R, Asymptote/OpenSCAD/Godot/Robot,
BibTeX/SWIG/gcc and selected system libraries/tools. This addon does not ship
native tool binaries. Ubuntu support is limited to the recorded retained-toolchain
workflow; other platforms and fresh Ubuntu installations are not qualified.

The .usl outputs and generated portable source artifacts are supplied. Source
archives omit native executables, compiled extension binaries, build objects
and native interface caches, whose identities remain in the detailed receipts.
Regenerate them through the tested provider/native workflow. Read each scope:
many source, library, interoperability, normative-conformance and proof gates
remain open even after a bounded profile validates.
