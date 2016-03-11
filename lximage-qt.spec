%define debug_package %{nil}

Name:		lximage-qt
Version:	0.4.0
Release:	6
Source0:	http://lxqt.org/downloads/%{name}/%{version}/%{name}-%{version}.tar.xz
Summary:	Image viewer and screenshot tool for the LXQt desktop
Url:		http://lxqt.org/
License:	GPLv2+
Group:		Graphical desktop/KDE
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	pkgconfig(lxqt)
BuildRequires:	pkgconfig(libfm-qt5)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(x11)

%description
Image viewer and screenshot tool for the LXQt desktop

%prep
%setup -q
%cmake_qt5

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
