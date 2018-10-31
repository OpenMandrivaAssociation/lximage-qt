%define debug_package %{nil}

Summary:	Image viewer and screenshot tool for the LXQt desktop
Name:		lximage-qt
Version:	0.7.0
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://lxqt.org/
Source0:	https://downloads.lxqt.org/downloads/lximage-qt/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	ninja
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(lxqt-build-tools)
BuildRequires:	pkgconfig(lxqt)
BuildRequires:	pkgconfig(libfm-qt) >= 0.12.0
BuildRequires:	pkgconfig(libfm-extra)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(libmenu-cache)

%description
Image viewer and screenshot tool for the LXQt desktop.

%prep
%setup -q
%apply_patches
%cmake_qt5 -DPULL_TRANSLATIONS=NO -G Ninja

%build
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja -C build

%install
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja_install -C build

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-screenshot.desktop
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
