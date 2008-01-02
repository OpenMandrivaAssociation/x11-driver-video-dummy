Name: x11-driver-video-dummy
Version: 0.2.0
Release: %mkrel 5
Summary: The X.org dummy video driver
Group: Development/X11
URL: http://xorg.freedesktop.org
# Note local tag xf86-video-dummy-0.2.0@mandriva suggested on upstream
# Tag at git checkout 2aeec40b3d48705bc1de9da3f06deac365c25895
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-dummy xorg/drivers/xf86-video-dummy
# cd xorg/drivers/xf86-video/dummy
# git-archive --format=tar --prefix=xf86-video-dummy-0.2.0/ xf86-video-dummy-0.2.0@mandriva | bzip2 -9 > xf86-video-dummy-0.2.0.tar.bz2
########################################################################
Source0: xf86-video-dummy-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-video-dummy-0.2.0@mandriva..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.1.5-4mdk
BuildRequires: x11-util-modular
Conflicts: xorg-x11-server < 7.0

%description
This is a dummy video driver for X.org.

%prep
%setup -q -n xf86-video-dummy-%{version}

%patch1 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/drivers/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/dummy_drv.so
