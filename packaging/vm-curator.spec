Name:           vm-curator
Version:        1.3.0
Release:        3%{?dist}
Summary:        TUI application to manage QEMU/KVM virtual machines

License:        MIT
URL:            https://github.com/linuxgamerlife/lgl-vm-curator
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  systemd-devel
BuildRequires:  desktop-file-utils
Requires:       qemu-system-x86-core
Requires:       qemu-img
Requires:       systemd-libs
Requires:       bash
Requires:       kitty

%description
vm-curator is a feature-rich TUI application for managing QEMU/KVM virtual
machines: automatic VM discovery, a 5-step creation wizard with 121
pre-configured OS profiles, snapshot management, USB passthrough, and 3D
graphics acceleration.

%prep
%autosetup

%build
cargo build --release --locked

%install
install -Dm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 README.md %{buildroot}%{_pkgdocdir}/README.md
install -Dm644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE
install -Dm644 packaging/lgl-vm-curator.desktop %{buildroot}%{_datadir}/applications/lgl-vm-curator.desktop
install -Dm644 packaging/lgl-vm-curator.png %{buildroot}%{_datadir}/pixmaps/lgl-vm-curator.png
desktop-file-validate %{buildroot}%{_datadir}/applications/lgl-vm-curator.desktop

%files
%{_bindir}/%{name}
%{_pkgdocdir}/README.md
%license LICENSE
%{_datadir}/applications/lgl-vm-curator.desktop
%{_datadir}/pixmaps/lgl-vm-curator.png

%post
echo ""
echo "vm-curator: make sure hardware virtualization (Intel VT-x / AMD-V) is enabled"
echo "in your BIOS/UEFI, and that your user is in the 'kvm' group:"
echo "  sudo usermod -aG kvm \$USER"
echo "then log out and back in for it to take effect."
echo ""

%changelog
* Fri Jul 31 2026 Linux Gamer Life <linuxgamerlife@users.noreply.github.com> - 1.3.0-3
- Add explicit systemd-libs Requires (provides libudev)
- Print a post-install reminder to enable BIOS virtualization and join
  the kvm group

* Fri Jul 31 2026 Linux Gamer Life <linuxgamerlife@users.noreply.github.com> - 1.3.0-2
- Package desktop file and icon, add kitty as a runtime dependency,
  switch SRPM build to a git-archive-based Makefile (no git tag needed)

* Fri Jul 31 2026 Linux Gamer Life <linuxgamerlife@users.noreply.github.com> - 1.3.0-1
- Initial COPR packaging
