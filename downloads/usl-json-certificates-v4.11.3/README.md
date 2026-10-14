This tranche adds **checked translation certificates for concrete JSON data artifacts**, followed by fresh original/generated native processing and actual generated `.usl` execution. It is separate from the frozen v4.11.2 source and the all-607 qualification gate package.

A certificate establishes this limited claim: the actual generated USL has exactly one assignment to `document`, its expression contains only recursive List and Constant nodes, and its literal data exactly equals an independently supplied intended IR. Exact types, number lexemes, object member order, duplicate names, arrays and Unicode codepoints are preserved. Additional code, calls, effects, names, tuples and computed expressions are rejected even when they would produce an equal value.

`verify` reparses the actual source and repeats the structural derivation, domain checks, exact comparisons and all identity bindings. It does not accept a passed flag or a matching hash as sufficient evidence. The checker itself, the pinned translator, the runtime source and the assumed Constant/List runtime branches are identity-bound. Booleans and integers are distinct throughout certificate and data comparisons.

```python
from json_certificate import Checker

checker = Checker(input_root="/workspace/usl-planning-v4.11.2",
                  source_root="/workspace/usl-v4.10.0-clean-test")
source_ir = ["number", "1.00e+02"]
intended_ir = ["number", "1.00e+02"]  # Supply this independently.
generated = checker.dependencies()[0].emit_usl(source_ir)
certificate = checker.certify(source_ir, intended_ir, generated)
checker.verify(certificate, source_ir, intended_ir, generated)
```

The fresh run starts all **930 case actors** together: 612 independently authored fixtures and 318 pinned upstream JSONTestSuite cases. Two independent native jobs per phase are admitted using observed memory and descriptor limits. Each accepted case gets a freshly checked certificate, fresh `run_usl` execution and fresh native processing of its original and regenerated JSON. Four native host processes each process a group of independent inputs; process counts and per-input observations remain separate. No external execution observation is replayed from a cache.

The resulting 626 accepted cases use 597 distinct pure generated artifacts and certificates. Content-addressed storage avoids 29 duplicate artifact copies; it does not avoid or pretend to repeat native or USL execution. The 296 syntax/encoding rejections and eight disclosed profile-resource-limit outcomes remain separate. Resource-limited inputs are not called accepted or complete conformance evidence. Runtime depth means value-recursion depth with root at zero and maximum 40; it does not mean a maximum of 40 nested empty containers.

Run the fresh workflow:

```bash
source /workspace/.onboarding/activate-usl.sh
python -m unittest test_json_certificate -v
python run_certificates.py --output results
python verify_certificates.py --output results
```

Other hosts need Python 3.12 with the pinned v4.10 USL runtime and v4.11.2 JSON candidate source. Supply their locations with `--source-root` and `--input-root`. The complete original upstream corpus must be available at `--suite`, pinned to commit `1ef36fa01286573e846ac449e8683f8833c5b26a`. Native evidence uses a fresh isolated Python standard-library JSON host and records its executable/source identities. This package does not ship native binaries or modify earlier source packages.

`results/RESULTS.json` retains per-case original/generated observations, intent/source bindings, outcomes and native execution receipts. `CERTIFICATES.json` and `ARTIFACTS.json` hold exact content-addressed data. Read-only `verify_certificates.py` independently reconstructs the original fixture contracts and checks every stored concrete certificate, while explicitly reporting zero new native or USL executions. Rerun `run_certificates.py` to obtain fresh execution evidence.

The trusted base includes this small structural checker, Python AST parsing and exact literal semantics, the loaded functions corresponding to their pinned files, and the specified USL assignment/List/Constant behavior. An external intended IR is assumed to represent the desired contract. These assumptions are recorded in every certificate. This is translation validation for specific literal artifacts; it is not a formally verified implementation of Python or USL, and it does not prove the JSON parser, JSON generator, complete RFC8259 standard, arbitrary source programs or natural-language intent.

The accompanying RFC review treats the earlier **62 entries as candidate inventory records**: 30 grammar productions, 10 operative uppercase requirements and 22 prose/policy records. It keeps imported normative references, transport/media integration, parser/generator correctness and final review obligations visible. No new full standard is qualified; the total remains **zero**. This checker reduces one concrete translation-validation obligation and does not close an entire language gate.
