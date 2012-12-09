Name: x11-driver-video-dummy
Version: 0.3.6
Release: 2
Summary: The X.org dummy video driver
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-dummy-%{version}.tar.bz2

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
This is a dummy video driver for X.org.

%prep
%setup -qn xf86-video-dummy-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/dummy_drv.so



%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.3.6-1
+ Revision: 810713
- version update 0.3.6

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.3.5-1
+ Revision: 787222
- 0.3.5
- Build for x11-server 1.12

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.3.4-7
+ Revision: 748388
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.4-6
+ Revision: 703715
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.3.4-5
+ Revision: 683556
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.4-4
+ Revision: 671144
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 0.3.4-3mdv2011.0
+ Revision: 595731
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 0.3.4-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Thu Jul 22 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.3.4-1mdv2011.0
+ Revision: 557061
- New version: 0.3.4

* Tue Dec 01 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.3.3-1mdv2010.1
+ Revision: 472434
- New version: 0.3.3

* Fri Jul 03 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 0.3.2-1mdv2010.0
+ Revision: 391862
- update to version 0.3.2

* Mon Jan 26 2009 Thierry Vignaud <tv@mandriva.org> 0.3.1-1mdv2009.1
+ Revision: 333669
- new release
- fix group

  + Colin Guthrie <cguthrie@mandriva.org>
    - Rebuild for new xserver

* Sun Nov 30 2008 Adam Williamson <awilliamson@mandriva.org> 0.3.0-3mdv2009.1
+ Revision: 308215
- rebuild for new X server

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.3.0-2mdv2009.0
+ Revision: 265912
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.3.0-1mdv2009.0
+ Revision: 194209
- Update to version 0.3.0.

* Mon Feb 11 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.2.0-7mdv2008.1
+ Revision: 165534
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.2.0-6mdv2008.1
+ Revision: 156603
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.2.0-5mdv2008.1
+ Revision: 154861
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.2.0-4mdv2008.1
+ Revision: 98690
- minor spec cleanup
- build against new xserver (1.4)

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-3mdv2008.0
+ Revision: 75758
- rebuild

