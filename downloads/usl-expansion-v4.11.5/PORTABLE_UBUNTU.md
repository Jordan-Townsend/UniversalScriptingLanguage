# Run the selected translation profiles on Ubuntu26

This path uses Ubuntu's Python and public hash-pinned packages. It does not need
the Codex Python/Node installation, previous source archives or native language
toolchains. The archive includes the unmodified v4.10 budgeted USL subset
interpreter; its SHA256 and original source archive are in
bundled_runtime/PROVENANCE.json. Other USL subsystems are separate dependencies.

On Ubuntu26.04 LTS x86-64:

```bash
sudo apt-get update
sudo apt-get install --no-install-recommends python3 python3-venv ca-certificates
cd /path/to/extracted/usl-expansion-v4.11.5
python3 setup_portable.py --venv /tmp/usl-python-env
/tmp/usl-python-env/bin/python portable_checks.py
```

Use a new virtual-environment path; the installer preserves existing directories.
Lark1.3.1 and Z3-solver5.1.0.0 are installed from exact wheel hashes with TLS
verification enabled. The Z3 wheel is for Linux x86-64/glibc2.27 or newer.
Corporate or cloud TLS inspection needs its authorized CA configured in the
system trust store; do not disable certificate checks.

Write request.json:

```json
{"catalog_id":"nimrod","source":"var x = 2\necho x + 3\n","expected":{"stdout":"5\n"}}
```

Then generate and execute USL:

```bash
/tmp/usl-python-env/bin/python translate.py request.json \
  --source-root bundled_runtime --output /tmp/usl-result --run-usl
```

The output directory must be new. It contains generated.usl and receipt.json.
Read TRANSLATION_API.md for each input schema, optional shader IR proof checking,
all19 supported IDs, unsupported syntax and resource limits. Each frontend
supports a bounded profile. Caller expected-output comparisons are scoped tests;
they do not prove arbitrary intent or qualify a full language standard.

The portable installation and all19 public CLI tests were run using Ubuntu
26.04.1's native Python3.14.4 in a fresh virtual environment. The test command
cleared LD_LIBRARY_PATH and PYTHONPATH and used /usr/bin:/bin as PATH. The shared
container also held the native-test workspace; the portable tests used the
bundled runtime and the two installed packages. This is not a fresh booted VM
qualification or a complete native ecosystem installer. Native compilers,
framework SSR engines, CPU Vulkan drivers and the broader conformance suites
still require TESTING_GUIDE.md's separate workflow.
