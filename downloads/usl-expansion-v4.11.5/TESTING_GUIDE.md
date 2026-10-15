# Fresh validation

For supported user programs without the retained cloud toolchains, start with
PORTABLE_UBUNTU.md. It installs a separate Python environment and runs all19
public adapter tests against the bundled, unmodified USL interpreter. The
instructions below run the broader native differential workflow.

Preserve v4.11.4 and all earlier releases. Source the retained environment:

```bash
source /workspace/.onboarding/activate-usl.sh
cd /workspace/usl-expansion-v4.11.5
```

Read each family README and restore its pinned providers. The cloud helper
`bash /workspace/.onboarding/restore_expansion_v4115.sh` restores providers and
runs this workflow; its clean-extraction receipt is delivered separately from
the immutable source archive.

```bash
python -m unittest discover -v
python verify.py --previous /workspace/usl-expansion-v4.11.4 \
  --source-root /workspace/usl-v4.10.0-clean-test \
  --output /tmp/usl-v4115-fresh
```

Output must be outside the addon, runtime and previous release. The runner
checks source identities, completes all family regression suites, executes new
native/generated/independent-intent comparisons and joins all329 starting IDs.
Read the exact records in FAMILY_RECEIPTS.json. Native units differ between
families and must not be summed as physical process counts. Execution evidence
is never served from a cache. Failed jobs cancel and reap their process groups.

For the already prepared Ubuntu26.04 container:

```bash
docker start usl-ubuntu26-v4114
docker exec --user 1000:1000 usl-ubuntu26-v4114 \
  bash /workspace/usl-expansion-v4.11.5/ubuntu_run.sh \
  python verify.py --output /tmp/usl-v4115-ubuntu26-fresh
```

This requires the actual retained container, native prerequisites and mounted
workspace/toolchains; Docker process state must be restarted after restoration.
For recreation prerequisites see v4.11.4's ubuntu/README.md. The source ZIP alone
does not bootstrap a fresh Ubuntu machine. An absent container or external
runtime mount is not repaired by merely running this shell helper.

The platform matrix records actual completed tests. It does not qualify
untested operating systems, alternate tool versions, standalone installations
or real GPU hardware. A CPU Vulkan shader run is CPU execution through the
declared driver, distinct from an actual GPU device claim.
