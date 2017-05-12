#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE23B7E70B467F0BF (office@who-t.net)
#
Name     : libwacom
Version  : 0.25
Release  : 5
URL      : https://sourceforge.net/projects/linuxwacom/files/libwacom/libwacom-0.25.tar.bz2
Source0  : https://sourceforge.net/projects/linuxwacom/files/libwacom/libwacom-0.25.tar.bz2
Source99 : https://sourceforge.net/projects/linuxwacom/files/libwacom/libwacom-0.25.tar.bz2.sig
Summary  : Wacom model feature query library
Group    : Development/Tools
License  : HPND
Requires: libwacom-bin
Requires: libwacom-lib
Requires: libwacom-data
BuildRequires : doxygen
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libxml-2.0)

%description
libwacom is a library to identify wacom tablets and their model-specific
features. It provides easy access to information such as "is this a built-in
on-screen tablet", "what is the size of this model", etc.

%package bin
Summary: bin components for the libwacom package.
Group: Binaries
Requires: libwacom-data

%description bin
bin components for the libwacom package.


%package data
Summary: data components for the libwacom package.
Group: Data

%description data
data components for the libwacom package.


%package dev
Summary: dev components for the libwacom package.
Group: Development
Requires: libwacom-lib
Requires: libwacom-bin
Requires: libwacom-data
Provides: libwacom-devel

%description dev
dev components for the libwacom package.


%package lib
Summary: lib components for the libwacom package.
Group: Libraries
Requires: libwacom-data

%description lib
lib components for the libwacom package.


%prep
%setup -q -n libwacom-0.25

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1494598959
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1494598959
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/libwacom-list-local-devices

%files data
%defattr(-,root,root,-)
/usr/share/libwacom/bamboo-0fg-s-p.tablet
/usr/share/libwacom/bamboo-16fg-m-pt.tablet
/usr/share/libwacom/bamboo-16fg-s-p.tablet
/usr/share/libwacom/bamboo-16fg-s-pt.tablet
/usr/share/libwacom/bamboo-16fg-s-t.tablet
/usr/share/libwacom/bamboo-2fg-fun-m-pt.tablet
/usr/share/libwacom/bamboo-2fg-fun-s-pt.tablet
/usr/share/libwacom/bamboo-2fg-m-p.tablet
/usr/share/libwacom/bamboo-2fg-s-p.tablet
/usr/share/libwacom/bamboo-2fg-s-pt.tablet
/usr/share/libwacom/bamboo-2fg-s-t.tablet
/usr/share/libwacom/bamboo-4fg-fun-m.tablet
/usr/share/libwacom/bamboo-4fg-fun-s.tablet
/usr/share/libwacom/bamboo-4fg-s-pt.tablet
/usr/share/libwacom/bamboo-4fg-s-t.tablet
/usr/share/libwacom/bamboo-4fg-se-m-pt.tablet
/usr/share/libwacom/bamboo-4fg-se-s-pt.tablet
/usr/share/libwacom/bamboo-one.tablet
/usr/share/libwacom/cintiq-12wx.tablet
/usr/share/libwacom/cintiq-13hd.tablet
/usr/share/libwacom/cintiq-13hdt.tablet
/usr/share/libwacom/cintiq-20wsx.tablet
/usr/share/libwacom/cintiq-21ux.tablet
/usr/share/libwacom/cintiq-21ux2.tablet
/usr/share/libwacom/cintiq-22hd.tablet
/usr/share/libwacom/cintiq-22hdt.tablet
/usr/share/libwacom/cintiq-24hd-touch.tablet
/usr/share/libwacom/cintiq-24hd.tablet
/usr/share/libwacom/cintiq-27hd.tablet
/usr/share/libwacom/cintiq-27hdt.tablet
/usr/share/libwacom/cintiq-companion-2.tablet
/usr/share/libwacom/cintiq-companion-hybrid.tablet
/usr/share/libwacom/cintiq-companion.tablet
/usr/share/libwacom/cintiq-pro-13.tablet
/usr/share/libwacom/cintiq-pro-16.tablet
/usr/share/libwacom/dtf-720.tablet
/usr/share/libwacom/dth-2242.tablet
/usr/share/libwacom/dti-520.tablet
/usr/share/libwacom/dtk-1651.tablet
/usr/share/libwacom/dtk-2241.tablet
/usr/share/libwacom/dtu-1031.tablet
/usr/share/libwacom/dtu-1031x.tablet
/usr/share/libwacom/dtu-1141.tablet
/usr/share/libwacom/dtu-1631.tablet
/usr/share/libwacom/dtu-1931.tablet
/usr/share/libwacom/dtu-2231.tablet
/usr/share/libwacom/ek-remote.tablet
/usr/share/libwacom/generic.tablet
/usr/share/libwacom/graphire-usb.tablet
/usr/share/libwacom/graphire-wireless-8x6.tablet
/usr/share/libwacom/graphire3-4x5.tablet
/usr/share/libwacom/graphire3-6x8.tablet
/usr/share/libwacom/graphire4-4x5.tablet
/usr/share/libwacom/huion-h610-pro.tablet
/usr/share/libwacom/intuos-12x12.tablet
/usr/share/libwacom/intuos-12x18.tablet
/usr/share/libwacom/intuos-4x5.tablet
/usr/share/libwacom/intuos-6x8.tablet
/usr/share/libwacom/intuos-9x12.tablet
/usr/share/libwacom/intuos-m-p.tablet
/usr/share/libwacom/intuos-m-p2.tablet
/usr/share/libwacom/intuos-m-pt.tablet
/usr/share/libwacom/intuos-m-pt2.tablet
/usr/share/libwacom/intuos-pro-2-l.tablet
/usr/share/libwacom/intuos-pro-2-m.tablet
/usr/share/libwacom/intuos-pro-l.tablet
/usr/share/libwacom/intuos-pro-m.tablet
/usr/share/libwacom/intuos-pro-s.tablet
/usr/share/libwacom/intuos-s-p.tablet
/usr/share/libwacom/intuos-s-p2.tablet
/usr/share/libwacom/intuos-s-pt.tablet
/usr/share/libwacom/intuos-s-pt2.tablet
/usr/share/libwacom/intuos2-12x12.tablet
/usr/share/libwacom/intuos2-12x18.tablet
/usr/share/libwacom/intuos2-4x5.tablet
/usr/share/libwacom/intuos2-6x8.tablet
/usr/share/libwacom/intuos2-9x12.tablet
/usr/share/libwacom/intuos3-12x12.tablet
/usr/share/libwacom/intuos3-12x19.tablet
/usr/share/libwacom/intuos3-4x5.tablet
/usr/share/libwacom/intuos3-4x6.tablet
/usr/share/libwacom/intuos3-6x11.tablet
/usr/share/libwacom/intuos3-6x8.tablet
/usr/share/libwacom/intuos3-9x12.tablet
/usr/share/libwacom/intuos4-12x19.tablet
/usr/share/libwacom/intuos4-4x6.tablet
/usr/share/libwacom/intuos4-6x9-wl.tablet
/usr/share/libwacom/intuos4-6x9.tablet
/usr/share/libwacom/intuos4-8x13.tablet
/usr/share/libwacom/intuos5-m.tablet
/usr/share/libwacom/intuos5-s.tablet
/usr/share/libwacom/intuos5-touch-l.tablet
/usr/share/libwacom/intuos5-touch-m.tablet
/usr/share/libwacom/intuos5-touch-s.tablet
/usr/share/libwacom/isdv4-100.tablet
/usr/share/libwacom/isdv4-101.tablet
/usr/share/libwacom/isdv4-104.tablet
/usr/share/libwacom/isdv4-10d.tablet
/usr/share/libwacom/isdv4-10e.tablet
/usr/share/libwacom/isdv4-10f.tablet
/usr/share/libwacom/isdv4-114.tablet
/usr/share/libwacom/isdv4-116.tablet
/usr/share/libwacom/isdv4-117.tablet
/usr/share/libwacom/isdv4-124.tablet
/usr/share/libwacom/isdv4-12c.tablet
/usr/share/libwacom/isdv4-4004.tablet
/usr/share/libwacom/isdv4-4800.tablet
/usr/share/libwacom/isdv4-4814.tablet
/usr/share/libwacom/isdv4-5000.tablet
/usr/share/libwacom/isdv4-5002.tablet
/usr/share/libwacom/isdv4-5013.tablet
/usr/share/libwacom/isdv4-5014.tablet
/usr/share/libwacom/isdv4-503e.tablet
/usr/share/libwacom/isdv4-503f.tablet
/usr/share/libwacom/isdv4-5040.tablet
/usr/share/libwacom/isdv4-5044.tablet
/usr/share/libwacom/isdv4-5048.tablet
/usr/share/libwacom/isdv4-504a.tablet
/usr/share/libwacom/isdv4-90.tablet
/usr/share/libwacom/isdv4-93.tablet
/usr/share/libwacom/isdv4-e2.tablet
/usr/share/libwacom/isdv4-e3.tablet
/usr/share/libwacom/isdv4-e5.tablet
/usr/share/libwacom/isdv4-e6.tablet
/usr/share/libwacom/isdv4-ec.tablet
/usr/share/libwacom/isdv4-ed.tablet
/usr/share/libwacom/isdv4-ef.tablet
/usr/share/libwacom/layouts/bamboo-0fg-s-p.svg
/usr/share/libwacom/layouts/bamboo-16fg-m-pt.svg
/usr/share/libwacom/layouts/bamboo-16fg-s-pt.svg
/usr/share/libwacom/layouts/bamboo-16fg-s-t.svg
/usr/share/libwacom/layouts/bamboo-2fg-fun-m-pt.svg
/usr/share/libwacom/layouts/bamboo-2fg-fun-s-pt.svg
/usr/share/libwacom/layouts/bamboo-2fg-s-pt.svg
/usr/share/libwacom/layouts/bamboo-2fg-s-t.svg
/usr/share/libwacom/layouts/bamboo-4fg-fun-m-pt.svg
/usr/share/libwacom/layouts/bamboo-4fg-fun-s-pt.svg
/usr/share/libwacom/layouts/bamboo-4fg-s-pt.svg
/usr/share/libwacom/layouts/bamboo-4fg-s-t.svg
/usr/share/libwacom/layouts/bamboo-4fg-se-m-pt.svg
/usr/share/libwacom/layouts/bamboo-4fg-se-s-pt.svg
/usr/share/libwacom/layouts/cintiq-12wx.svg
/usr/share/libwacom/layouts/cintiq-13hd.svg
/usr/share/libwacom/layouts/cintiq-20wsx.svg
/usr/share/libwacom/layouts/cintiq-21ux.svg
/usr/share/libwacom/layouts/cintiq-21ux2.svg
/usr/share/libwacom/layouts/cintiq-22hd.svg
/usr/share/libwacom/layouts/cintiq-24hd.svg
/usr/share/libwacom/layouts/cintiq-companion-2.svg
/usr/share/libwacom/layouts/cintiq-companion-hybrid.svg
/usr/share/libwacom/layouts/cintiq-companion.svg
/usr/share/libwacom/layouts/dth-2242.svg
/usr/share/libwacom/layouts/dti-520.svg
/usr/share/libwacom/layouts/dtk-1651.svg
/usr/share/libwacom/layouts/dtu-1031.svg
/usr/share/libwacom/layouts/dtu-1141.svg
/usr/share/libwacom/layouts/ek-remote.svg
/usr/share/libwacom/layouts/graphire-wireless-8x6.svg
/usr/share/libwacom/layouts/graphire4-4x5.svg
/usr/share/libwacom/layouts/huion-h610-pro.svg
/usr/share/libwacom/layouts/intuos-m-p.svg
/usr/share/libwacom/layouts/intuos-m-p2.svg
/usr/share/libwacom/layouts/intuos-m-pt.svg
/usr/share/libwacom/layouts/intuos-m-pt2.svg
/usr/share/libwacom/layouts/intuos-pro-2-l.svg
/usr/share/libwacom/layouts/intuos-pro-2-m.svg
/usr/share/libwacom/layouts/intuos-pro-l.svg
/usr/share/libwacom/layouts/intuos-pro-m.svg
/usr/share/libwacom/layouts/intuos-pro-s.svg
/usr/share/libwacom/layouts/intuos-s-p.svg
/usr/share/libwacom/layouts/intuos-s-p2.svg
/usr/share/libwacom/layouts/intuos-s-pt.svg
/usr/share/libwacom/layouts/intuos-s-pt2.svg
/usr/share/libwacom/layouts/intuos3-12x12.svg
/usr/share/libwacom/layouts/intuos3-12x19.svg
/usr/share/libwacom/layouts/intuos3-4x5.svg
/usr/share/libwacom/layouts/intuos3-4x6.svg
/usr/share/libwacom/layouts/intuos3-6x11.svg
/usr/share/libwacom/layouts/intuos3-6x8.svg
/usr/share/libwacom/layouts/intuos3-9x12.svg
/usr/share/libwacom/layouts/intuos4-12x19.svg
/usr/share/libwacom/layouts/intuos4-4x6.svg
/usr/share/libwacom/layouts/intuos4-6x9-wl.svg
/usr/share/libwacom/layouts/intuos4-6x9.svg
/usr/share/libwacom/layouts/intuos4-8x13.svg
/usr/share/libwacom/layouts/intuos5-l.svg
/usr/share/libwacom/layouts/intuos5-m.svg
/usr/share/libwacom/layouts/intuos5-s.svg
/usr/share/libwacom/layouts/mobilestudio-pro-13.svg
/usr/share/libwacom/layouts/mobilestudio-pro-16.svg
/usr/share/libwacom/libwacom.stylus
/usr/share/libwacom/mobilestudio-pro-13.tablet
/usr/share/libwacom/mobilestudio-pro-16.tablet
/usr/share/libwacom/n-trig-pen.tablet
/usr/share/libwacom/one-by-wacom-m-p.tablet
/usr/share/libwacom/one-by-wacom-s-p.tablet
/usr/share/libwacom/serial-wacf004.tablet

%files dev
%defattr(-,root,root,-)
/usr/include/libwacom-1.0/libwacom/libwacom.h
/usr/lib64/libwacom.so
/usr/lib64/pkgconfig/libwacom.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libwacom.so.2
/usr/lib64/libwacom.so.2.5.3
