# LGL VM Curator — Packaging Changelog

This tracks packaging-only changes for the Fedora/Bazzite COPR build. The application itself is unchanged from [upstream vm-curator v1.4.0](https://github.com/mroboff/vm-curator/blob/main/CHANGELOG.md) — see that changelog for feature history.

## v1.4.0-1

- Merged upstream `v1.3.0` → `v1.4.0` (Virtual Network Manager, physical disk passthrough as boot device, launch path fix) into this fork's `main`.
- No packaging changes — spec, `.copr/Makefile`, desktop entry, and icon are unchanged from `1.3.0-2`. Only the `Version`/`Release` fields and `%changelog` were bumped to match upstream.

## v1.3.0-2

(`1.3.0-1` never built successfully via `rpkg` — see below — so this is the first release that actually publishes.)

- Packaged an application-menu entry: `packaging/lgl-vm-curator.desktop` and `packaging/lgl-vm-curator.png`, installed to `/usr/share/applications/` and `/usr/share/pixmaps/`.
- Added `Requires: kitty`, since the desktop entry launches vm-curator inside it (`Exec=kitty -e lgl-vm-curator`).
- Added a `desktop-file-validate` build-time check so a malformed desktop entry fails the build instead of shipping broken.
- Moved the spec file to `packaging/vm-curator.spec`, later renamed to `packaging/lgl-vm-curator.spec`.
- Switched the SRPM build method from `rpkg` to a git-archive-based `.copr/Makefile`. `rpkg` tied the source archive to the `v1.3.0` git tag, which meant packaging-only changes couldn't be built without either reusing a stale tag or re-tagging a non-upstream change. The Makefile archives `HEAD` directly, so the tag stays a pure marker of the real upstream release.
- Installed `git` inside the `make_srpm` mock chroot, since that minimal build environment doesn't include it by default and the Makefile's `git archive` step needs it.
- Fixed a personal email address leaked into the RPM `%changelog`, replacing it with a GitHub noreply address.
- Added an explicit `Requires: systemd-libs` (provides `libudev`) for clarity, alongside RPM's auto-detected shared-library dependency.
- Added a `%post` install reminder to enable hardware virtualization (Intel VT-x / AMD-V) in the BIOS/UEFI and to join the `kvm` group (`sudo usermod -aG kvm $USER`) — without this, `/dev/kvm` exists but isn't accessible, and VMs fail at QEMU startup with a permission error.
- Installed the binary as `lgl-vm-curator` instead of `vm-curator`.

## v1.3.0-1

**Never published** — the `rpkg` SRPM build failed because `Source0` pointed at the `v1.3.0` git tag, and COPR rejected rebuilding against a tag it had already built once. Superseded by `1.3.0-2` before a working build ever completed.

- Initial COPR packaging: builds `vm-curator` from source via `cargo build --release --locked`, installs the binary, README, and LICENSE.
- Runtime dependencies: `qemu-system-x86-core`, `qemu-img`, `bash`.
