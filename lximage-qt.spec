Summary:	Image viewer and screenshot tool for the LXQt desktop
Name:		lximage-qt
Version:	2.0.1
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://lxqt.org/
Source0:	https://github.com/lxqt/lximage-qt/releases/download/%{version}/lximage-qt-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6SvgWidgets)
BuildRequires:	cmake(lxqt2-build-tools)
BuildRequires:	pkgconfig(lxqt)
BuildRequires:	pkgconfig(libfm-qt6) >= 0.12.0
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
%autopatch -p1
%cmake -DPULL_TRANSLATIONS=NO -G Ninja

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
%find_lang %{name} --with-qt --all-name

# SVGs are scalable...
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
mv %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/*.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
rmdir %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
rmdir %{buildroot}%{_datadir}/icons/hicolor/48x48

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/lximage-qt.metainfo.xml
%{_datadir}/icons/*/*/*/*
%dir %{_datadir}/lximage-qt/translations
