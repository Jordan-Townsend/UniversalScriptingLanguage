# Test the concrete JSON translation tranche

This addon needs Python 3.12, Git, the unmodified v4.11.2 addon and the v4.10
USL runtime. It introduces no third-party Python dependencies. Download and
verify the two source archives listed in DEPENDENCIES.json. Extract the v4.10
archive into its own directory; its files do not have an enclosing directory.
The v4.11.2 archive has an enclosing usl-planning-v4.11.2 directory. Preserve
both releases. This addon does not include those sources or native binaries.

Obtain the public upstream corpus in a separate checkout:

```bash
git clone https://github.com/nst/JSONTestSuite.git JSONTestSuite
git -C JSONTestSuite checkout --detach 1ef36fa01286573e846ac449e8683f8833c5b26a
```

From this addon's extracted directory, run one complete verification, supplying
your own absolute paths. Its output must be outside this addon:

```bash
python3.12 verify_release.py \
  --input-root /absolute/path/usl-planning-v4.11.2 \
  --source-root /absolute/path/usl-v4.10.0 \
  --suite /absolute/path/JSONTestSuite \
  --output /absolute/path/json-verification
```

This runs 17 checker/review tests, starts all 930 logical case actors, performs
fresh native processing and generated USL executions, checks the stored concrete
certificates, and reproduces the RFC review against hash-pinned source text. It
retrieves that public RFC over HTTPS unless --rfc-text supplies a local copy.
The corpus and all essential candidate/runtime/oracle source hashes are checked.
Successful output includes 626 accepted concrete translation cases, 296 syntax
or encoding rejections, eight distinct resource refusals and zero qualified
full standards. Failures terminate verification; inspect the named log.

In this cloud environment the tested shortcut is:

```bash
bash /workspace/.onboarding/restore_json_certificates_v4113.sh
```

Read-only certificate checking can be run separately:

```bash
python3.12 verify_certificates.py \
  --input-root /absolute/path/usl-planning-v4.11.2 \
  --source-root /absolute/path/usl-v4.10.0 \
  --suite /absolute/path/JSONTestSuite --output results
```

That command performs no fresh native or USL execution. Its rechecked historical
observations retain their original scope. The full verifier above is the route
for fresh observations. Neither finite tests nor concrete literal certificates
establish arbitrary program correctness or complete RFC8259 qualification.

For direct unit-test discovery outside the cloud, set USL_CERTIFICATE_INPUT_ROOT
and USL_CERTIFICATE_SOURCE_ROOT to your extracted dependency paths. The full
verifier supplies these environment settings to its test subprocess itself.
