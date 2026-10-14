# Ubuntu 26.04 LTS x86-64

This directory prepares an Ubuntu 26.04 container that uses the retained USL
workspace and exact CPython 3.12.14 / Node 24.19.0 toolchains. The image digest,
executable SHA256 values, and USL interpreter hash are pinned in
`TOOLCHAINS.json`. The operating-system check reads the container's actual
`/etc/os-release`; a Debian host or another Ubuntu release cannot satisfy it.

The validation scope is Ubuntu 26.04 userspace with mounted retained toolchains.
`PLATFORM_CHECK.json` records an actual successful Ubuntu26.04.1 / glibc2.43
OS, exact-toolchain and USL smoke execution in the retained Docker container.
That test mounted Python/Node and copied the hash-identical retained Godot
binary to `/usr/local/bin/godot`; the reusable launcher instead mounts Godot
read-only and exposes its same pinned binary through the supplied wrappers.
A fresh Ubuntu installation and all 359 native language profiles are not
qualified by this setup. Consult the root Ubuntu validation receipt for actual
native families tested and any remaining compatibility failures. The base image,
bootstrap, launcher and developer-container configuration do not by themselves
establish native equivalence or full language conformance.

## Prepare a fresh Ubuntu host

On an Ubuntu 26.04 amd64 host, Docker can be installed from Ubuntu's authenticated
package repositories:

```bash
. /etc/os-release
test "$ID" = ubuntu && test "$VERSION_ID" = 26.04
test "$(dpkg --print-architecture)" = amd64
sudo apt-get update
sudo apt-get install --no-install-recommends docker.io python3 ca-certificates
sudo systemctl enable --now docker
sudo docker version
```

Use `sudo docker` where the current account cannot access the daemon. The Python
launcher calls `docker` as the current user; run that launcher with `sudo` in
that case. An existing Docker Engine installation can also be used. No host
Debian repository or Debian package installation is required by these steps.

Transfer the retained workspace snapshot and runtime directory to the host,
preserving symlinks. The snapshot must contain:

- `usl-expansion-v4.11.4`, `usl-v4.10.0-clean-test`, and
  `usl-planning-v4.11.2`; retain `usl-qualification-v4.11.3` for the full audit.
- `.onboarding/activate-usl.sh`, its Python virtual environment and dependencies,
  native wrappers, matching native sysroot/data and authenticated provider cache.
- Retained Godot4.6.3 under a separate `/opt/godot` tree; its executable hash is
  pinned in `TOOLCHAINS.json`. It is mounted read-only and exposed through
  `ubuntu/bin/godot` and `godot4` wrappers.
- `codex-primary-runtime` under the separate runtime directory, including the
  complete Python installation, matching `Python.h`, and Node installation.

The source archive alone does not contain these native binaries. The previous
source archives are identified and hashed in `../DEPENDENCIES.json`; use each
family's documented pinned provider restoration for omitted local providers.
The exact retained CPython/Node binaries have no download substitute in this
workflow. Installing Ubuntu's default Python, Node or Agda packages does not
reproduce their pinned identities. A source-only bootstrap on a clean Ubuntu
host remains untested.

## Build and launch

`Dockerfile` pins the official Ubuntu image by digest. `bootstrap.sh` checks
Ubuntu 26.04/amd64 and installs compiler, TLS and observed native runtime prerequisites from
the image's authenticated Ubuntu repositories. It does not add Debian apt
sources. Ubuntu package updates can change their versions; exact apt versions
must be retained in the validation receipt when making a new platform claim.
The image and retained Python/Node inputs are pinned separately.
The recorded validation uses the actual digest-pinned Ubuntu base plus the
listed packages in the retained Docker container. The Dockerfile build itself
and a fresh Ubuntu host setup were not executed during that validation.

```bash
cd /path/to/retained/workspace/usl-expansion-v4.11.4
sudo docker build --platform linux/amd64 --tag usl-ubuntu26:retained ubuntu
sudo python3 ubuntu/launch.py \
  --workspace /path/to/retained/workspace \
  --runtime-root /path/to/retained/runtimes \
  --godot-root /path/to/retained/godot check
```

The launcher mounts the workspace at `/workspace` and the runtime directory
read-only at `/opt/codex/runtimes` and Godot read-only at `/opt/godot`, preserving absolute virtual-environment and
wrapper paths. It verifies Python, Node and Godot hashes before Docker runs and checks
Docker daemon access. Containers run with the invoking host UID/GID (including
the original sudo user), so generated workspace files retain host ownership;
`--user UID:GID` overrides this explicitly. Inside the container, `inside.sh` activates the retained
workspace, verifies OS/architecture and the running interpreter, checks Node's
version, verifies the original USL interpreter hash, and executes `6 * 7` in USL.
A successful JSON receipt proves these checks only.

Inspect the exact Docker argument array without launching a container:

```bash
python3 ubuntu/launch.py --print-command check
```

Run a command after the same platform checks:

```bash
sudo python3 ubuntu/launch.py --workspace /path/to/retained/workspace \
  --runtime-root /path/to/retained/runtimes \
  --godot-root /path/to/retained/godot --interactive -- bash
```

Within that shell, `python coordinator.py --source-root
/workspace/usl-v4.10.0-clean-test --previous /workspace/usl-planning-v4.11.2
--output /tmp/usl-ubuntu26-fresh` performs actual fresh family qualification after
native prerequisites have been restored. It must complete successfully before
its family/native counts can be claimed. Outputs belong outside the source tree.
`--image` selects a separately prepared image, such as an image containing the
native compatibility libraries verified by the root Ubuntu test run.

## Native prerequisites and compatibility

The Dockerfile installs the core toolchain prerequisites and native runtime
libraries discovered by actual Ubuntu loader checks, including OpenSCAD and
TeX Live/BibTeX. Retained providers still need their matching resources. Full
native family runs additionally require the following native providers and
runtime inputs. Keep the versions in each family README and provenance file;
Ubuntu package names below describe dependencies, not replacements for those
exact provider versions.

| Family | Required native inputs and Ubuntu dependency candidates |
|---|---|
| agda | Retained Agda 2.6.4.3 binary, matching builtins/JS runtime, Node; `libgmp10`, `libtinfo6`; pinned Python `z3-solver` |
| preprocessor | Retained Python packages including `tinycss2`, original preprocessing source, Node |
| templates | Compatible Ruby runtime (`ruby` and its runtime libraries), pinned Haml/Slim/Temple/Tilt/Thor gems; pinned MaskJS under Node |
| configuration | `make`, `ncurses-bin`, `libtinfo6`, `libyaml-0-2`; ICU **76** and OpenLDAP `libldap.so.2`; pinned DTC/Kconfig/genrb providers; `sqv`, `debian-archive-keyring`, `dpkg-deb` for authenticated archive restoration |
| native_languages | `build-essential`, `git`, `make`, `lua5.4`, compatible LPeg; retained R/tools data with its matching R runtime and libraries |
| grammar_native | `build-essential`, matching retained CPython headers, pinned regex/Parsimonious/SWIG/WebIDL providers; `texlive-binaries`, `texlive-base`; GnuPG and retained Debian archive keyring for authenticated provider restoration |
| all359 selected native profiles | Retained Asymptote 3.02, OpenSCAD 2021.01, Godot 4.6.3, Robot Framework 7.5, their matching resources/runtime libraries; graphics/font/Qt/audio libraries required even for some headless scalar runs |

Ubuntu 26.04 libraries may differ from the retained Debian host. In particular,
Ubuntu's default ICU major is not a substitute for `libicuuc.so.76` and
`libicudata.so.76`; the existing genrb provider needs ICU76. Library filenames,
loader paths, the BibTeX reference-style path, Lua module ABI, R resources and
Agda data must be checked in the actual container. The saved bootstrap does not
silently replace them with current distro versions. Provider restore scripts
retain TLS, signature and hash checks for their original exact artifacts.

The retained activation script currently adds a private native sysroot to the
library path. Those retained binaries/libraries remain part of the platform's
trusted dependencies. Using them inside Ubuntu does not claim they were rebuilt
from Ubuntu sources or that all host ABI combinations work.

## Developer container and regression tests

For a developer-container client, set `USL_WORKSPACE`, `USL_RUNTIME_ROOT` and `USL_GODOT_ROOT` on
the host to the retained directory paths, and select `ubuntu/devcontainer.json`.
It builds the same digest-pinned Dockerfile, mounts the same inputs, and runs
the actual platform check after startup. It requires the same preexisting
snapshot and Docker access; it does not install native family providers.

```bash
python3 -m unittest discover -s ubuntu -p test_ubuntu.py -v
bash -n ubuntu/bootstrap.sh ubuntu/inside.sh
```

Nineteen regression tests check OS/version/architecture rejection, actual pinned
toolchain identities, digest consistency, read-only runtime mounting and literal
command arguments. They do not start Docker, install packages, or stand in for
the separate native Ubuntu validation.


## Restore the private ICU76 ABI

The Ubuntu native configuration path uses the original exact ICU76 provider.
The public Debian archive keyring in `keys/` has a frozen hash in
`COMPAT_PROVIDERS.json`; it contains public signing certificates. No Debian apt
repository is added to Ubuntu. `bootstrap.sh` verifies the bundled public
keyring SHA256 and installs it at
`/usr/share/keyrings/debian-archive-keyring.pgp` for existing provider helpers.
Ubuntu’s separate archive keyring is preserved. For an existing development
container, run `bash ubuntu/install_keyring.sh` as root before the provider
restoration/regression suites. On the prepared host or in the Ubuntu development
container, restore the signed-index-pinned `libicu76` 76.1-4 archive:

```bash
python ubuntu/restore_compat.py
export USL_COMPAT_LIBDIR=/workspace/.onboarding/ubuntu26-compat/usr/lib/x86_64-linux-gnu
export LD_LIBRARY_PATH="$USL_COMPAT_LIBDIR${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
```

This requires `sqv`, `dpkg-deb`, TLS certificates and network access to
`deb.debian.org`. It verifies the frozen signed InRelease, authenticates the
package index and the exact package/version/size/SHA256 entry, and verifies the
9,722,072-byte archive before extracting approximately31MB into the private
prefix. System prefixes are rejected. The restore receipt records actual
library hashes and the restoration host; restoration on Debian does not count
as a native Ubuntu execution. `inside.sh` activates this private directory when
present. Configuration native children preserve inherited library paths and
include `USL_COMPAT_LIBDIR`; fresh result records hash the actual chosen library
files. Ubuntu ICU78 is not overwritten.
