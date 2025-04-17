
# Universal Scripting Language (USL)

The DNA of Logic.

USL is a symbolic, compressible, transpilable logic format that works across 605+ programming languages.

## Features

- Symbolic encoding (.usl)
- Compression (.uslb, .uslc)
- Quantum-ready encryption (.uslbq)
- Reverse transpilation
- Semantic token mapping
- Full CLI and GUI-ready runtime
- Packaged as .uslpack (logic runtime environment)

## Repository

https://github.com/jordantownsend/universalscriptinglanguage

## Quick Start

```bash
pip install ./tools/uslcli_install_package.zip

python tools/run_uslpack.py USL_Final_Standard.uslpack.zip python
python tools/reverse_transpile.py myscript.py --output logic_output.usl
python tools/usl_token_optimizer.py logic_output.usl --output logic_optimized.usl
python tools/usl_semantic_engine.py logic_optimized.usl
```

## Structure

- logic/: `.usl`, `.uslb`, `.uslc`, `.uslbq`
- transpiler/: Symbolic transpilers
- tools/: CLI utilities
- templates/: Registry-backed syntax
- docs/: Whitepapers, guides, benchmarks
- submissions/: IEEE, ISO, NIST, arXiv letters

## License

MIT and Apache 2.0 Dual Licensed  
Author: Jordan Townsend
