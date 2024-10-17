%define _disable_ld_no_undefined 1

Summary:	The X.org dummy video driver
Name:		x11-driver-video-dummy
Version:	0.4.1
Release:	1
Group:		System/X11
License:	MIT
Url:		https://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-dummy-%{version}.tar.xz

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
This is a dummy video driver for X.org.

%prep
%autosetup -n xf86-video-dummy-%{version} -p1

%build
%configure
%make_build

%install
%make_install

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/dummy_drv.so
