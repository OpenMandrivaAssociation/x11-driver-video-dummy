%define _disable_ld_no_undefined 1

Summary:	The X.org dummy video driver
Name:		x11-driver-video-dummy
Version:	0.3.6
Release:	5
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-dummy-%{version}.tar.bz2
Patch0:		remove_mibstore_h.patch

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
This is a dummy video driver for X.org.

%prep
%setup -qn xf86-video-dummy-%{version}
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/dummy_drv.so

