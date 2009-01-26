Name: x11-driver-video-dummy
Version: 0.3.1
Release: %mkrel 1
Summary: The X.org dummy video driver
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-dummy-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

%description
This is a dummy video driver for X.org.

%prep
%setup -q -n xf86-video-dummy-%{version}

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/dummy_drv.la
%{_libdir}/xorg/modules/drivers/dummy_drv.so
