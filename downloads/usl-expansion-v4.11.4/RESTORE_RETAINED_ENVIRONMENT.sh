#!/usr/bin/env bash
set -euo pipefail
source /workspace/.onboarding/activate-usl.sh
usl_expansion_root="${USL_EXPANSION_ROOT:-/workspace/usl-expansion-v4.11.4}"
cd "$usl_expansion_root"
python templates/restore.py > /tmp/usl-v4114-template-restore.log
python configuration/restore.py > /tmp/usl-v4114-configuration-restore.log
python grammar_native/restore.py > /tmp/usl-v4114-grammar-restore.log
python native_languages/provider_restore.py > /tmp/usl-v4114-native-restore.log
python verify.py --previous /workspace/usl-planning-v4.11.2 --source-root /workspace/usl-v4.10.0-clean-test --output /tmp/usl-v4114-readiness
