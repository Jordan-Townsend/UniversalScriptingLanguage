# USL v4.11.4 downloads

Download `USL-V4.11.4-30-PROFILES-UBUNTU26.zip` and verify it against
`SHA256SUMS`. The ZIP contains source, tests, generated .usl artifacts, provenance
and full fresh Debian/Ubuntu case evidence. Native binaries are omitted.

This addon adds 30 bounded profiles: 277/606 original catalog IDs now have a
bounded profile; 329 do not. No full standard or complete entity track qualifies.
`ALL606_STATUS.csv` and `ALL359_PROGRESS.md` expose the remaining work.

Read `TESTING_GUIDE.md`, `DEPENDENCIES.json` and `UBUNTU26_GUIDE.md` first.
Ubuntu26.04.1 LTS x86-64 passed 14 coordinator tests, 199 family tests and
4,862 fresh USL executions, plus 19 Ubuntu setup tests. The same family suite
also passed on Debian13. Historical247 profiles were retained without a new
requalification claim. Native work uses different units by family and is not
summed into a misleading process count.

Ubuntu validation used the retained toolchains mounted into an actual Ubuntu
container. The source ZIP alone does not install a complete environment on a
fresh Ubuntu machine; the retained workspace/Python/Node/native prerequisites
are required. A standalone source-only Ubuntu installation remains unverified.
See `PLATFORM_MATRIX.json` for exact scope, `UBUNTU26-INSTALLED-PACKAGES.tsv` for
observed OS packages and `UBUNTU26-RESTART-CHECK.json` for the service restart
and USL smoke check. `UBUNTU26-BOOTSTRAP.log` records the actual Ubuntu bootstrap.

The clean-extraction receipt is separate from the immutable archive so it can
identify the exact tested ZIP without circular checksums. Source identities are
in `MANIFEST.json`; full runtime/case identities are inside the archive.

New scoped IDs: agda, literate-agda, mozhashpreproc, mozpercentpreproc, css+mozpreproc, javascript+mozpreproc, xul+mozpreproc, haml, slim, mask, basemake, termcap, terminfo, resourcebundle, devicetree, kconfig, ldapconf, unixconfig, wren, berry, moonscript, rd, peg, bst, swig, webidl, asymptote, openscad, gdscript, robotframework.
