<div align="center">

# LGL VM Curator

**One of the best QEMU/KVM VM managers around — now a `dnf install` away on Fedora and Bazzite.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Fedora](https://img.shields.io/badge/Fedora-COPR-blue?logo=fedora&logoColor=white)](https://copr.fedorainfracloud.org/coprs/linuxgamerlife/lgl-essentials/)

</div>

---

## Overview

[vm-curator](https://github.com/mroboff/vm-curator) is a fast, friendly Rust TUI for managing QEMU/KVM virtual machines — automatic VM discovery, a guided creation wizard, GPU and physical-disk passthrough, snapshots, disk resizing, and 130+ pre-configured OS profiles.

This repo packages it for Fedora and Bazzite via COPR, so it's easy to install without a manual `cargo build`. It currently tracks upstream **v1.5.0**.

All credit for vm-curator itself goes to [Mark Roboff](https://github.com/mroboff) — see the [upstream README](https://github.com/mroboff/vm-curator#readme) for full feature docs and usage, or the pinned copy in [UPSTREAM-README.md](UPSTREAM-README.md).

See [LGL-CHANGELOG.md](LGL-CHANGELOG.md) for what's changed in this packaging.

---

## Install

### Recommended — COPR

```bash
sudo dnf copr enable linuxgamerlife/lgl-essentials
sudo dnf install lgl-vm-curator
```

QEMU (`qemu-system-x86`, so the GTK/SDL/SPICE display and audio modules come with it), qemu-img, and libudev are pulled in automatically as package dependencies. UEFI firmware, swtpm, passt, samba, and virt-viewer are weak dependencies, which `dnf` installs by default unless you've disabled weak deps.

### Migrating from the old repository

Earlier builds came from a standalone `linuxgamerlife/lgl-vm-curator` COPR repository under the package name `vm-curator`. The package is now `lgl-vm-curator` and ships from `linuxgamerlife/lgl-essentials`. To switch over:

```bash
# 1. Enable the new repository
sudo dnf copr enable linuxgamerlife/lgl-essentials

# 2. Replace the old package with the renamed one
sudo dnf swap vm-curator lgl-vm-curator

# 3. Remove the old repository
sudo dnf copr remove linuxgamerlife/lgl-vm-curator
```

If you no longer want the package at all, remove it and drop the old repository (keep `lgl-essentials` enabled if you use other packages from it):

```bash
sudo dnf remove lgl-vm-curator vm-curator
sudo dnf copr remove linuxgamerlife/lgl-vm-curator
```

Only remove the shared repo too if nothing else comes from it:

```bash
sudo dnf copr remove linuxgamerlife/lgl-essentials
```

### Your settings and VMs are kept

Uninstalling, reinstalling, switching package names, or moving between versions never touches your data. The application always reads the same locations, regardless of which package, binary name, or repository supplied it:

- Settings: `~/.config/vm-curator/config.toml`
- Metadata and art overrides: `~/.config/vm-curator/metadata/`, `~/.config/vm-curator/ascii/`
- Managed networks: `~/.config/vm-curator/networks/`
- VM library: `~/vm-space` by default (or wherever `vm_library_path` points)
- Per-VM metadata: `vm-curator.toml` inside each VM's folder

These live in your home directory and are not owned by any RPM, so they survive upgrades, downgrades, and package removal. Every version of vm-curator — including upstream's official builds — uses this same configuration.

### Before you start

- **Enable virtualization in your BIOS/UEFI** — Intel VT-x or AMD-V must be turned on, or KVM acceleration won't be available and VMs will fail to start or run unusably slow.
- **Add your user to the `kvm` group** so `lgl-vm-curator` can access `/dev/kvm`:

  ```bash
  sudo usermod -aG kvm $USER
  ```

  Log out and back in for the group change to take effect.

---

## License

MIT — see [LICENSE](LICENSE) for details.

---

<div align="center">
Made for <a href="https://fedoraproject.org">Fedora</a> · by <a href="https://www.youtube.com/@linuxgamerlife">LinuxGamerLife</a>
</div>
