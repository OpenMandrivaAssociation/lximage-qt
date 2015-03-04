%define debug_package %{nil}

Name:		lximage-qt
Version:	0.3.0
Release:	1
Source0:	http://lxqt.org/downloads/%{name}/%{version}/%{name}-%{version}.tar.xz
Summary:	Image viewer and screenshot tool for the LXQt desktop
Url:		http://lxqt.org/
License:	GPLv2+
Group:		Graphical desktop/KDE
BuildRequires:	cmake
BuildRequires:	pkgconfig(lxqt)
BuildRequires:	pkgconfig(libfm)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	qt5-linguist-tools
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(xfixes)

%description
Image viewer and screenshot tool for the LXQt desktop

%prep
%setup -q
%cmake -DUSE_QT5=ON

%build
%make -C build

%install
%makeinstall_std -C build

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-screenshot.desktop
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_datadir}/%{name}/translations/%{name}*.qm
