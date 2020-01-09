%define glib2_version 2.27.90

### Abstract ###

Name: libsoup
Version: 2.34.3
Release: 3%{?dist}
License: LGPLv2
Group: Development/Libraries
Summary: Soup, an HTTP library implementation
URL: http://live.gnome.org/LibSoup
#VCS: git:git://git.gnome.org/libsoup
Source: http://download.gnome.org/sources/libsoup/2.34/libsoup-%{version}.tar.bz2
Patch1: libsoup-trusted-cert.patch
Patch2: libsoup-not-ssl3.patch
Requires: glib-networking >= %{glib2_version}

### Build Dependencies ###

BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: glib-networking
BuildRequires: libxml2-devel
BuildRequires: sqlite-devel
BuildRequires: gnome-keyring-devel

%description
Libsoup is an HTTP library implementation in C. It was originally part
of a SOAP (Simple Object Access Protocol) implementation called Soup, but
the SOAP and non-SOAP parts have now been split into separate packages.

libsoup uses the Glib main loop and is designed to work well with GTK
applications. This enables GNOME applications to access HTTP servers
on the network in a completely asynchronous fashion, very similar to
the Gtk+ programming model (a synchronous operation mode is also
supported for those who want it).

%package devel
Summary: Header files for the Soup library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: glib2-devel >= %{glib2_version}
Requires: gnutls-devel
Requires: libxml2-devel

%description devel
Libsoup is an HTTP library implementation in C. This package allows
you to develop applications that use the libsoup library.

%prep
%setup -q

%patch1 -p1 -b .trust
%patch2 -p1 -b .not-ssl3

%build
%configure

# Omit unused direct shared library dependencies.
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.a

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README COPYING NEWS AUTHORS
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}-2.4
%{_includedir}/%{name}-gnome-2.4
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/html/%{name}-2.4

%changelog
* Mon Jan  5 2015  <danw@redhat.com> - 2.34.3-3
- Fix TLS negotiation; don't default to SSLv3 (rh#975457)

* Wed Jun 11 2014 Dan Winship <danw@redhat.com> - 2.34.3-2
- rebase to libsoup 2.34 (via f15 package) (rh#1101399)

* Thu Aug 30 2012 Dan Winship <danw@redhat.com> - 2.28.2-4
- Fix infinite retry of non-resposive conection (rh#746587)

* Wed Jun 27 2012 Dan Winship <danw@redhat.com> - 2.28.2-3
- Fix crash when cancelling during socket connection (rh#657622)

* Wed Jul 20 2011 Dan Winship <danw@redhat.com> - 2.28.2-2
- Patch for CVE-2011-2524

* Mon Jan  4 2010 Matthias Clasen <mclasen@redhat.com> - 2.28.2-1
- Update to 2.28.2

* Thu Nov 05 2009 Bastien Nocera <bnocera@redhat.com> 2.28.1-2
- Fix hangs when playing hi-def YouTube videos

* Mon Oct 19 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.1-1
- Update to 2.28.1

* Mon Sep 21 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Mon Sep  7 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.92-1
- Update to 2.27.92

* Mon Aug 24 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.91-1
- Update to 2.27.91

* Tue Aug 11 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.90-1
- Update to 2.27.90

* Tue Jul 28 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.5-1
- Update to 2.27.5

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Matthew Barnes <mbarnes@redhat.com> - 2.27.4-1
- Update to 2.27.4

* Wed Jun 17 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.2-1
- Update to 2.27.2

* Mon May 18 2009 Bastien Nocera <bnocera@redhat.com> 2.27.1-1
- Update to 2.27.1

* Mon Apr 13 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.1-1
- Update to 2.26.1
- See http://download.gnome.org/sources/libsoup/2.26/libsoup-2.26.1.changes

* Thu Apr  9 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.0.9-1
- Upate to 2.26.0.9

* Mon Mar 16 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Matthew Barnes <mbarnes@redhat.com> - 2.25.91-1
- Update to 2.25.91

* Mon Feb 02 2009 Matthew Barnes <mbarnes@redhat.com> - 2.25.5-1
- Update to 2.25.5

* Sun Jan 25 2009 Matthias Clasen  <mclasen@redhat.com> - 2.25.4-2
- Build against libproxy

* Mon Jan 05 2009 Matthew Barnes <mbarnes@redhat.com> - 2.25.4-1
- Update to 2.25.4

* Tue Dec 16 2008 Matthew Barnes <mbarnes@redhat.com> - 2.25.3-1
- Update to 2.25.3

* Mon Dec 01 2008 Matthew Barnes <mbarnes@redhat.com> - 2.25.2-1
- Update to 2.25.2

* Wed Nov 12 2008 Matthias Clasen  <mclasen@redhat.com> - 2.25.1-3
- Fix BuildRequires

* Fri Nov 07 2008 Matthew Barnes <mbarnes@redhat.com> - 2.25.1-1
- Update to 2.25.1

* Mon Oct 20 2008 Matthias Clasen  <mclasen@redhat.com> - 2.24.1-1
- Update to 2.24.1

* Wed Sep 24 2008 Matthias Clasen  <mclasen@redhat.com> - 2.24.0.1-1
- Update to 2.24.0.1

* Mon Sep 22 2008 Matthias Clasen  <mclasen@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Mon Sep  8 2008 Matthias Clasen  <mclasen@redhat.com> - 2.23.92-1
- Update to 2.23.92

* Mon Sep 01 2008 Matthew Barnes <mbarnes@redhat.com> - 2.23.91-1
- Update to 2.23.91

* Mon Aug 04 2008 Matthew Barnes <mbarnes@redhat.com> - 2.23.6-1
- Update to 2.23.6

* Wed Jul 30 2008 Matthew Barnes <mbarnes@redhat.com> - 2.23.1-6
- Omit unused direct shared library dependencies (RH bug #226046).

* Tue Jun 24 2008 Tomas Mraz <tmraz@redhat.com> - 2.23.1-5
- rebuild with new gnutls

* Sun Jun 22 2008 Matthew Barnes <mbarnes@redhat.com> - 2.23.1-4
- Remove unnecessary pkgconfig build requirement.

* Mon Jun 16 2008 Matthew Barnes <mbarnes@redhat.com> - 2.23.1-3
- Incorporate package review feedback (RH bug #226046).

* Sun May  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.1-2
- Fix source url

* Mon Apr 21 2008 Matthew Barnes <mbarnes@redhat.com> - 2.23.1-1
- Update to 2.23.1

* Mon Apr 07 2008 Matthew Barnes <mbarnes@redhat.com> - 2.4.1-1
- Update to 2.4.1

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.4.0-1
- Update to 2.4.0

* Mon Feb 25 2008 Matthew Barnes <mbarnes@redhat.com> - 2.3.4-1
- Update to 2.3.4

* Wed Feb 13 2008 Matthew Barnes <mbarnes@redhat.com> - 2.3.2-1
- Update to 2.3.2

* Mon Jan 28 2008 Matthew Barnes <mbarnes@redhat.com> - 2.3.0-1
- Update to 2.3.0
- Bump glib2 requirement to >= 2.15.3.
- Clean up some redundant dependencies.
- Remove patch for RH bug #327871 (fixed in glibc).

* Mon Nov 26 2007 Matthew Barnes <mbarnes@redhat.com> - 2.2.104-1
- Update to 2.2.104

* Sun Oct 28 2007 Jeremy Katz <katzj@redhat.com> - 2.2.103-1
- update to 2.2.103 to fix a rhythmbox crasher (#343561)

* Mon Oct 15 2007 Matthew Barnes <mbarnes@redhat.com> - 2.2.102-1
- Update to 2.2.102

* Thu Oct 11 2007 Matthew Barnes <mbarnes@redhat.com> - 2.2.101-2
- Add patch for RH bug #327871 (broken Rhythmbox build).
- Suspect this is really a glibc bug.

* Fri Oct 05 2007 Matthew Barnes <mbarnes@redhat.com> - 2.2.101-1
- Update to 2.2.101

* Wed Aug  8 2007 Matthias Clasen <mclasen@redhat.com> - 2.2.100-3
- Update the license field

* Sat Apr 21 2007 Matthias Clasen <mclasen@redhat.com> - 2.2.100-2
- Don't install INSTALL

* Mon Feb 12 2007 Matthew Barnes <mbarnes@redhat.com> - 2.2.100-1
- Update to 2.2.100

* Mon Jan 08 2007 Matthew Barnes <mbarnes@redhat.com> - 2.2.99-1
- Update to 2.2.99

* Mon Nov 21 2006 Matthew Barnes <mbarnes@redhat.com> - 2.2.98-1
- Update to 2.2.98
- Remove patch for RH bug #215919 (fixed upstream).

* Fri Nov 17 2006 Matthias Clasen <mclasen@redhat.com> - 2.2.97-2
- Avoid accidentally exported symbols (#215919)

* Mon Nov 06 2006 Matthew Barnes <mbarnes@redhat.com> - 2.2.97-1
- Update to 2.2.97
- Remove patch for Gnome.org bug #356809 (fixed upstream).

* Fri Nov 03 2006 Matthew Barnes <mbarnes@redhat.com> - 2.2.96-5
- Revised patch for Gnome.org bug #356809 to match upstream.

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 2.2.96-4
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Wed Sep 20 2006 Matthew Barnes <mbarnes@redhat.com> - 2.2.96-3.fc6
- Add patch for Gnome.org bug #356809 (lingering file on uninstall).

* Tue Aug 15 2006 Matthew Barnes <mbarnes@redhat.com> - 2.2.96-2.fc6
- Rebuild

* Tue Jul 25 2006 Matthew Barnes <mbarnes@redhat.com> - 2.2.96
- Update to 2.2.96
- Bump glib2 requirement to >= 2.6.

* Wed Jul 12 2006 Matthew Barnes <mbarnes@redhat.com> - 2.2.95.1-1
- Update to 2.2.95.1

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.2.94-3.1
- rebuild

* Wed Jun 14 2006 Tomas Mraz <tmraz@redhat.com> - 2.2.94-3
- rebuilt with new gnutls

* Tue Jun 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.2.94-1
- Update to 2.2.94

* Mon Apr 10 2006 Matthias Clasen <mclasen@redhat.com> - 2.2.92-2
- Update to 2.2.92

* Sat Mar  4 2006 Matthias Clasen <mclasen@redhat.com> - 2.2.91-1
- Update to 2.2.91

* Wed Feb 15 2006 Matthias Clasen <mclasen@redhat.com> - 2.2.7-2
- Remove excessive Requires for the -devel package

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.2.7-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.2.7-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Nov 29 2005 David Malcolm <dmalcolm@redhat.com> - 2.2.7-1
- 2.2.7
- Remove static library

* Tue Aug 23 2005 David Malcolm <dmalcolm@redhat.com> - 2.2.6.1-1
- 2.2.6.1

* Tue Aug  9 2005 David Malcolm <dmalcolm@redhat.com> - 2.2.5-1
- 2.2.5
- Removed gnome-bug-306877-soup-connection-ntlm.c.patch (#160071) as this is 
  now in upstream tarball

* Mon Aug  8 2005 Tomas Mraz <tmraz@redhat.com> - 2.2.3-5
- rebuild with new gnutls

* Tue Jun 14 2005 David Malcolm <dmalcolm@redhat.com> - 2.2.3-4
- add patch for NTLM domains (#160071)

* Sun Apr 24 2005 Florian La Roche <laroche@redhat.com>
- rebuild for new gnutls

* Thu Mar 17 2005 David Malcolm <dmalcolm@redhat.com> - 2.2.3-2
- explicitly enable gtk-doc support

* Thu Mar 17 2005 David Malcolm <dmalcolm@redhat.com> - 2.2.3-1
- 2.2.3

* Wed Mar  2 2005 David Malcolm <dmalcolm@redhat.com> - 2.2.2-3
- rebuild with GCC 4

* Wed Jan 26 2005 David Malcolm <dmalcolm@redhat.com> - 2.2.2-2
- actually uploaded the source this time

* Wed Jan 26 2005 David Malcolm <dmalcolm@redhat.com> - 2.2.2-1
- update from 2.2.1 to 2.2.2
- add explicit devel requirements on glib2-devel, pkgconfig, gtk-doc, gnutls-devel and libxml2-devel

* Tue Oct 12 2004 David Malcolm <dmalcolm@redhat.com> - 2.2.1-1
- update from 2.2.0 to 2.2.1

* Wed Oct  6 2004 David Malcolm <dmalcolm@redhat.com> - 2.2.0-3
- added requirement on libxml2 (#134700)

* Wed Sep 22 2004 David Malcolm <dmalcolm@redhat.com> - 2.2.0-2
- added requirement on gnutls, so that we build with SSL support
- fixed source download path

* Tue Aug 31 2004 David Malcolm <dmalcolm@redhat.com> - 2.2.0-1
- update from 2.1.13 to 2.2.0

* Mon Aug 16 2004 David Malcolm <dmalcolm@redhat.com> - 2.1.13-1
- 2.1.13

* Tue Jul 20 2004 David Malcolm <dmalcolm@redhat.com> - 2.1.12-1
- 2.1.12

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jun  7 2004 David Malcolm <dmalcolm@redhat.com> - 2.1.11-1
- 2.1.11

* Thu May 20 2004 David Malcolm <dmalcolm@redhat.com> - 2.1.10-2
- added missing md5 file

* Thu May 20 2004 David Malcolm <dmalcolmredhat.com> - 2.1.10-1
- 2.1.10

* Tue Apr 20 2004 David Malcolm <dmalcolm@redhat.com> - 2.1.9-1
- Update to 2.1.9; added gtk-doc to BuildRequires and the generated files to the devel package

* Wed Mar 10 2004 Jeremy Katz <katzj@redhat.com> - 2.1.8-1
- 2.1.8

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 17 2004 Jeremy Katz <katzj@redhat.com> - 2.1.7-1
- 2.1.7

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jan 26 2004 Jeremy Katz <katzj@redhat.com> 2.1.5-1
- 2.1.5

* Wed Jan 14 2004 Jeremy Katz <katzj@redhat.com> 2.1.4-0
- update to 2.1.4

* Sat Jan  3 2004 Jeremy Katz <katzj@redhat.com> 2.1.3-0
- update to 2.1.3

* Tue Sep 23 2003 Jeremy Katz <katzj@redhat.com> 1.99.26-2
- rebuild

* Fri Sep 19 2003 Jeremy Katz <katzj@redhat.com> 1.99.26-1
- 1.99.26

* Tue Jul 15 2003 Jeremy Katz <katzj@redhat.com> 1.99.23-3
- rebuild to pickup ppc64

* Mon Jun  9 2003 Jeremy Katz <katzj@redhat.com> 1.99.23-2
- rebuild 
- no openssl on ppc64 yet, excludearch

* Mon Jun  9 2003 Jeremy Katz <katzj@redhat.com> 1.99.23-1
- 1.99.23

* Wed Jun 5 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jun  5 2003 Jeremy Katz <katzj@redhat.com> 1.99.22-2
- rebuild

* Sun May 25 2003 Jeremy Katz <katzj@redhat.com> 1.99.22-1
- 1.99.22

* Tue May  6 2003 Jeremy Katz <katzj@redhat.com> 1.99.20-1
- 1.99.20

* Sun May  4 2003 Jeremy Katz <katzj@redhat.com> 1.99.17-3
- include ssl proxy so that ssl urls work properly (#90165, #90166)

* Wed Apr 16 2003 Jeremy Katz <katzj@redhat.com> 1.99.17-2
- forward port patch to use a union initializer to fix build on x86_64

* Wed Apr 16 2003 Jeremy Katz <katzj@redhat.com> 1.99.17-1
- rename package to libsoup
- update to 1.99.17
- don't obsolete soup for now, it's parallel installable

* Sun Apr  6 2003 Jeremy Katz <katzj@redhat.com> 0.7.11-1
- update to 0.7.11

* Wed Apr  2 2003 Matt Wilson <msw@redhat.com> 0.7.10-5
- added soup-0.7.10-64bit.patch to fix 64 bit platforms (#86347)

* Sat Feb 01 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- only runtime libs in normal rpm

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan 21 2003 Jeremy Katz <katzj@redhat.com> 
- update url (#82347)

* Tue Jan  7 2003 Nalin Dahyabhai <nalin@redhat.com> 0.7.10-2
- use pkgconfig's openssl configuration information, if it exists

* Fri Dec 13 2002 Jeremy Katz <katzj@redhat.com> 0.7.10-1
- update to 0.7.10

* Thu Dec 12 2002 Jeremy Katz <katzj@redhat.com> 0.7.9-4
- fix fpic patch
- soup-devel should require soup

* Thu Dec 12 2002 Jeremy Katz <katzj@redhat.com> 0.7.9-3
- better lib64 patch
- fix building of libwsdl-build to use libtool so that it gets built 
  with -fPIC as needed

* Tue Dec 10 2002 Jeremy Katz <katzj@redhat.com> 0.7.9-2
- change popt handling in configure slightly so that it will work on 
  multilib arches

* Tue Dec 10 2002 Jeremy Katz <katzj@redhat.com> 0.7.9-1
- update to 0.7.9, pulling the tarball out of Ximian packages

* Wed Oct 23 2002 Jeremy Katz <katzj@redhat.com> 0.7.4-3
- fix to not try to include non-existent doc files and remove all 
  unwanted files from the build
- include api docs 
- don't build the apache module

* Wed Sep 25 2002 Jeremy Katz <katzj@redhat.com> 0.7.4-2
- various specfile tweaks to include in Red Hat Linux
- include all the files

* Tue Jan 23 2001 Alex Graveley <alex@ximian.com>
- Inital RPM config.
