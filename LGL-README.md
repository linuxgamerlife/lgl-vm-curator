<div align="center">

# LGL VM Curator

**One of the best QEMU/KVM VM managers around — now a `dnf install` away on Fedora and Bazzite.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Fedora](https://img.shields.io/badge/Fedora-COPR-blue?logo=fedora&logoColor=white)](https://copr.fedorainfracloud.org/coprs/linuxgamerlife/lgl-vm-curator/)

</div>

---

## Overview

[vm-curator](https://github.com/mroboff/vm-curator) is a fast, friendly Rust TUI for managing QEMU/KVM virtual machines — automatic VM discovery, a guided creation wizard, GPU passthrough, snapshots, and 120+ pre-configured OS profiles.

This repo packages it for Fedora and Bazzite via COPR, so it's easy to install without a manual `cargo build`.

All credit for vm-curator itself goes to [Mark Roboff](https://github.com/mroboff) — see the [upstream README](https://github.com/mroboff/vm-curator#readme) for full feature docs and usage.

---

## Install

### Recommended — COPR

```bash
sudo dnf copr enable linuxgamerlife/lgl-vm-curator
sudo dnf install vm-curator
```

---

## License

MIT — see [LICENSE](LICENSE) for details.

---

<div align="center">
Made for <a href="https://fedoraproject.org">Fedora</a> · by <a href="https://www.youtube.com/@linuxgamerlife">LinuxGamerLife</a>
</div>
