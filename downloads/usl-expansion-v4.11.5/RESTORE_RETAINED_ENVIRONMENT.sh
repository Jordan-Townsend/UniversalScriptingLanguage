#!/usr/bin/env bash
set -euo pipefail
source /workspace/.onboarding/activate-usl.sh
usl_expansion_root="${USL_EXPANSION_ROOT:-/workspace/usl-expansion-v4.11.5}"
usl_readiness_output="${USL_READINESS_OUTPUT:-/tmp/usl-v4115-readiness}"
cd "$usl_expansion_root"
python restore_java.py > /tmp/usl-v4115-java-restore.log
for usl_family in lisp native_code grammar_hosts server_config semantic_hosts web_templates; do
    python "$usl_family/restore.py" > "/tmp/usl-v4115-$usl_family-restore.log" 2>&1
done
python verify.py --previous /workspace/usl-expansion-v4.11.4 --source-root /workspace/usl-v4.10.0-clean-test --output "$usl_readiness_output"
