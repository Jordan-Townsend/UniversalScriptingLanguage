# USL v4.11.5 downloads

Download USL-V4.11.5-19-PROFILES-PORTABLE-UBUNTU.zip and verify SHA256SUMS.
Start with PORTABLE_UBUNTU.md to run supported source-to-USL translations on
Ubuntu26.04 x86-64 using its own Python, two hash-pinned packages and the bundled
unmodified USL subset interpreter. This path needs no Codex Python/Node or
previous source release. TRANSLATION_API.md documents all19 strict profiles.

New IDs: icon, nimrod, vala, janet, newlisp, cirru, treetop, antlr-ruby,
antlr-csharp, jasmin, apacheconf, lighttpd, vcl, vclsnippets, glsl, hlsl,
vue, ng2, html+ng2. Cirru is a syntax-tree processing contract; grammars,
configuration and templates retain their category-specific contracts.

Coverage:296/606 original IDs have bounded profiles;310 do not. No full standard
or complete entity track qualifies. Historical277 profiles are retained without
a new requalification claim. ALL606_STATUS.csv and ALL329_PROGRESS.md show the
complete original catalog and starting backlog. Per-ID open obligations remain.

Debian13 and Ubuntu26.04.1 each passed70 root tests+95 family tests and2152 fresh
USL executions. Portable setup additionally passed19 public CLI tests under
Ubuntu native Python3.14.4, repeated against the extracted archive. The native
suite requires its separately retained native hosts/toolchains; the portable
command does not install or qualify every native ecosystem or full language.
No real GPU claim is made for CPU Vulkan execution. Review scope and assumptions
are in PLATFORM_MATRIX.json and the reports.

The immutable source ZIP contains source, tests, generated USL, pinned provider
restoration, public references and validation/debian.zip+ubuntu26.zip with full
portable fresh native/intent/USL evidence. Compiled artifacts are omitted with
hashes and rebuilt. Development family results are historical snapshots; final
joined validation ZIPs identify the authoritative build. CLEAN_NATIVE_EVIDENCE.zip
and the separate restore receipt attest the exact source archive without
circular archive/checksum references. Setup drafts still require user publication;
a new cloud task or fresh booted VM restoration is not established here.
