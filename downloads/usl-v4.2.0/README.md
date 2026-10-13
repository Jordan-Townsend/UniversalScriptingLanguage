# USL v4.2 development source download

Download [the full source ZIP](USL-UNIVERSAL-SYSTEMS-V4.2.0-FULL-SOURCE.zip?raw=true), [testing instructions](TESTING-V4.2.txt), and [the SHA-256 checksum](USL-UNIVERSAL-SYSTEMS-V4.2.0-FULL-SOURCE.zip.sha256).

The ZIP is 8,947,829 bytes and contains 753 files, including examples, reports, six recovered subsystem archives, and the original v4.1 source package.

SHA-256: `f59721784dd91625e4751d8c9276778a0f795e23c65e14e7969e2b5914e05d12`

This is a Linux-tested development source release. Recorded coverage is 71 of 606 catalog entries at tested-subset level, including 18 newly executed entries. The other 535 entries are unqualified, and no entry has full specification qualification. The 606-entry inventory includes programming languages, templates, configuration, and document formats.

Validation: 490 executed regression tests passed, 9 skipped; 45 native compiler cases; 72 new source-engine cases; a successful integrated 27-task USL workflow. Windows, live model inference, and physical-device integrations remain unqualified. See the included docs/V4.2_BUILD_STATUS.md for contracts and remaining work.

Extract the archive and follow TESTING-V4.2.txt. Native examples require the listed external runtimes and execute with your account permissions.
