#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE23B7E70B467F0BF (office@who-t.net)
#
Name     : libwacom
Version  : 1.1
Release  : 18
URL      : https://github.com/linuxwacom/libwacom/releases/download/libwacom-1.1/libwacom-1.1.tar.bz2
Source0  : https://github.com/linuxwacom/libwacom/releases/download/libwacom-1.1/libwacom-1.1.tar.bz2
Source1 : https://github.com/linuxwacom/libwacom/releases/download/libwacom-1.1/libwacom-1.1.tar.bz2.sig
Summary  : Library to identify Wacom tablets and their features
Group    : Development/Tools
License  : HPND
Requires: libwacom-bin = %{version}-%{release}
Requires: libwacom-data = %{version}-%{release}
Requires: libwacom-lib = %{version}-%{release}
Requires: libwacom-license = %{version}-%{release}
Requires: libwacom-man = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : doxygen
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : itstool
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libxml-2.0)

%description
SVG images have a dual purpose, providing an accurate representation of the
tablets and also providing the size and location of the various controls on
the device that can be queried by various applications that may need it.

%package bin
Summary: bin components for the libwacom package.
Group: Binaries
Requires: libwacom-data = %{version}-%{release}
Requires: libwacom-license = %{version}-%{release}

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
Requires: libwacom-lib = %{version}-%{release}
Requires: libwacom-bin = %{version}-%{release}
Requires: libwacom-data = %{version}-%{release}
Provides: libwacom-devel = %{version}-%{release}
Requires: libwacom = %{version}-%{release}
Requires: libwacom = %{version}-%{release}

%description dev
dev components for the libwacom package.


%package lib
Summary: lib components for the libwacom package.
Group: Libraries
Requires: libwacom-data = %{version}-%{release}
Requires: libwacom-license = %{version}-%{release}

%description lib
lib components for the libwacom package.


%package license
Summary: license components for the libwacom package.
Group: Default

%description license
license components for the libwacom package.


%package man
Summary: man components for the libwacom package.
Group: Default

%description man
man components for the libwacom package.


%prep
%setup -q -n libwacom-1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568869490
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1568869490
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libwacom
cp COPYING %{buildroot}/usr/share/package-licenses/libwacom/COPYING
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/udev/rules.d/65-libwacom.rules

%files bin
%defattr(-,root,root,-)
/usr/bin/libwacom-list-local-devices

%files data
%defattr(-,root,root,-)
/usr/share/libwacom/bamboo-0fg-m-p-alt.tablet
/usr/share/libwacom/bamboo-0fg-s-p-alt.tablet
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
/usr/share/libwacom/bamboo-one-m-p.tablet
/usr/share/libwacom/bamboo-one.tablet
/usr/share/libwacom/bamboo-pad-wireless.tablet
/usr/share/libwacom/bamboo-pad.tablet
/usr/share/libwacom/cintiq-12wx.tablet
/usr/share/libwacom/cintiq-13hd.tablet
/usr/share/libwacom/cintiq-13hdt.tablet
/usr/share/libwacom/cintiq-16.tablet
/usr/share/libwacom/cintiq-20wsx.tablet
/usr/share/libwacom/cintiq-21ux.tablet
/usr/share/libwacom/cintiq-21ux2.tablet
/usr/share/libwacom/cintiq-22.tablet
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
/usr/share/libwacom/cintiq-pro-24-p.tablet
/usr/share/libwacom/cintiq-pro-24-pt.tablet
/usr/share/libwacom/cintiq-pro-32.tablet
/usr/share/libwacom/dell-canvas-27.tablet
/usr/share/libwacom/dtf-720.tablet
/usr/share/libwacom/dth-1152.tablet
/usr/share/libwacom/dth-2242.tablet
/usr/share/libwacom/dth-2452.tablet
/usr/share/libwacom/dti-520.tablet
/usr/share/libwacom/dtk-1651.tablet
/usr/share/libwacom/dtk-1660e.tablet
/usr/share/libwacom/dtk-2241.tablet
/usr/share/libwacom/dtk-2451.tablet
/usr/share/libwacom/dtu-1031.tablet
/usr/share/libwacom/dtu-1031x.tablet
/usr/share/libwacom/dtu-1141.tablet
/usr/share/libwacom/dtu-1141b.tablet
/usr/share/libwacom/dtu-1631.tablet
/usr/share/libwacom/dtu-1931.tablet
/usr/share/libwacom/dtu-2231.tablet
/usr/share/libwacom/ek-remote.tablet
/usr/share/libwacom/elan-2072.tablet
/usr/share/libwacom/elan-22e2.tablet
/usr/share/libwacom/elan-24db.tablet
/usr/share/libwacom/elan-2537.tablet
/usr/share/libwacom/elan-2627.tablet
/usr/share/libwacom/elan-264c.tablet
/usr/share/libwacom/elan-5515.tablet
/usr/share/libwacom/generic.tablet
/usr/share/libwacom/graphire-usb.tablet
/usr/share/libwacom/graphire-wireless-8x6.tablet
/usr/share/libwacom/graphire2-4x5.tablet
/usr/share/libwacom/graphire2-5x7.tablet
/usr/share/libwacom/graphire3-4x5.tablet
/usr/share/libwacom/graphire3-6x8.tablet
/usr/share/libwacom/graphire4-4x5.tablet
/usr/share/libwacom/graphire4-6x8.tablet
/usr/share/libwacom/huion-h420.tablet
/usr/share/libwacom/huion-h610-pro.tablet
/usr/share/libwacom/intuos-12x12.tablet
/usr/share/libwacom/intuos-12x18.tablet
/usr/share/libwacom/intuos-4x5.tablet
/usr/share/libwacom/intuos-6x8.tablet
/usr/share/libwacom/intuos-9x12.tablet
/usr/share/libwacom/intuos-m-p.tablet
/usr/share/libwacom/intuos-m-p2.tablet
/usr/share/libwacom/intuos-m-p3-wl.tablet
/usr/share/libwacom/intuos-m-p3.tablet
/usr/share/libwacom/intuos-m-pt.tablet
/usr/share/libwacom/intuos-m-pt2.tablet
/usr/share/libwacom/intuos-pro-2-l.tablet
/usr/share/libwacom/intuos-pro-2-m.tablet
/usr/share/libwacom/intuos-pro-2-s.tablet
/usr/share/libwacom/intuos-pro-l.tablet
/usr/share/libwacom/intuos-pro-m.tablet
/usr/share/libwacom/intuos-pro-s.tablet
/usr/share/libwacom/intuos-s-p.tablet
/usr/share/libwacom/intuos-s-p2.tablet
/usr/share/libwacom/intuos-s-p3-wl.tablet
/usr/share/libwacom/intuos-s-p3.tablet
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
/usr/share/libwacom/isdv4-2d1f-002e.tablet
/usr/share/libwacom/isdv4-4004.tablet
/usr/share/libwacom/isdv4-4800.tablet
/usr/share/libwacom/isdv4-4806.tablet
/usr/share/libwacom/isdv4-4807.tablet
/usr/share/libwacom/isdv4-4809.tablet
/usr/share/libwacom/isdv4-4814.tablet
/usr/share/libwacom/isdv4-481a.tablet
/usr/share/libwacom/isdv4-4822.tablet
/usr/share/libwacom/isdv4-4824.tablet
/usr/share/libwacom/isdv4-4831.tablet
/usr/share/libwacom/isdv4-4841.tablet
/usr/share/libwacom/isdv4-484c.tablet
/usr/share/libwacom/isdv4-485e.tablet
/usr/share/libwacom/isdv4-4865.tablet
/usr/share/libwacom/isdv4-486a.tablet
/usr/share/libwacom/isdv4-4870.tablet
/usr/share/libwacom/isdv4-488f.tablet
/usr/share/libwacom/isdv4-5000.tablet
/usr/share/libwacom/isdv4-5002.tablet
/usr/share/libwacom/isdv4-5010.tablet
/usr/share/libwacom/isdv4-5013.tablet
/usr/share/libwacom/isdv4-5014.tablet
/usr/share/libwacom/isdv4-502a.tablet
/usr/share/libwacom/isdv4-503e.tablet
/usr/share/libwacom/isdv4-503f.tablet
/usr/share/libwacom/isdv4-5040.tablet
/usr/share/libwacom/isdv4-5044.tablet
/usr/share/libwacom/isdv4-5048.tablet
/usr/share/libwacom/isdv4-504a.tablet
/usr/share/libwacom/isdv4-5090.tablet
/usr/share/libwacom/isdv4-5099.tablet
/usr/share/libwacom/isdv4-509d.tablet
/usr/share/libwacom/isdv4-50b4.tablet
/usr/share/libwacom/isdv4-50b6.tablet
/usr/share/libwacom/isdv4-50b8.tablet
/usr/share/libwacom/isdv4-50db.tablet
/usr/share/libwacom/isdv4-50e9.tablet
/usr/share/libwacom/isdv4-50f1.tablet
/usr/share/libwacom/isdv4-50f8.tablet
/usr/share/libwacom/isdv4-50fd.tablet
/usr/share/libwacom/isdv4-5110.tablet
/usr/share/libwacom/isdv4-5115.tablet
/usr/share/libwacom/isdv4-5122.tablet
/usr/share/libwacom/isdv4-5128.tablet
/usr/share/libwacom/isdv4-513b.tablet
/usr/share/libwacom/isdv4-5146.tablet
/usr/share/libwacom/isdv4-5150.tablet
/usr/share/libwacom/isdv4-5157.tablet
/usr/share/libwacom/isdv4-5158.tablet
/usr/share/libwacom/isdv4-515a.tablet
/usr/share/libwacom/isdv4-5169.tablet
/usr/share/libwacom/isdv4-516b.tablet
/usr/share/libwacom/isdv4-517d.tablet
/usr/share/libwacom/isdv4-90.tablet
/usr/share/libwacom/isdv4-93.tablet
/usr/share/libwacom/isdv4-e2.tablet
/usr/share/libwacom/isdv4-e3.tablet
/usr/share/libwacom/isdv4-e5.tablet
/usr/share/libwacom/isdv4-e6.tablet
/usr/share/libwacom/isdv4-ec.tablet
/usr/share/libwacom/isdv4-ed.tablet
/usr/share/libwacom/isdv4-ef.tablet
/usr/share/libwacom/layouts/bamboo-0fg-s-p-alt.svg
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
/usr/share/libwacom/layouts/bamboo-pad.svg
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
/usr/share/libwacom/layouts/dth-2452.svg
/usr/share/libwacom/layouts/dti-520.svg
/usr/share/libwacom/layouts/dtk-1651.svg
/usr/share/libwacom/layouts/dtk-2451.svg
/usr/share/libwacom/layouts/dtu-1031.svg
/usr/share/libwacom/layouts/dtu-1141.svg
/usr/share/libwacom/layouts/dtu-1141b.svg
/usr/share/libwacom/layouts/ek-remote.svg
/usr/share/libwacom/layouts/graphire-wireless-8x6.svg
/usr/share/libwacom/layouts/graphire4-4x5.svg
/usr/share/libwacom/layouts/graphire4-6x8.svg
/usr/share/libwacom/layouts/huion-h420.svg
/usr/share/libwacom/layouts/huion-h610-pro.svg
/usr/share/libwacom/layouts/intuos-m-p.svg
/usr/share/libwacom/layouts/intuos-m-p2.svg
/usr/share/libwacom/layouts/intuos-m-p3.svg
/usr/share/libwacom/layouts/intuos-m-pt.svg
/usr/share/libwacom/layouts/intuos-m-pt2.svg
/usr/share/libwacom/layouts/intuos-pro-2-l.svg
/usr/share/libwacom/layouts/intuos-pro-2-m.svg
/usr/share/libwacom/layouts/intuos-pro-2-s.svg
/usr/share/libwacom/layouts/intuos-pro-l.svg
/usr/share/libwacom/layouts/intuos-pro-m.svg
/usr/share/libwacom/layouts/intuos-pro-s.svg
/usr/share/libwacom/layouts/intuos-s-p.svg
/usr/share/libwacom/layouts/intuos-s-p2.svg
/usr/share/libwacom/layouts/intuos-s-p3.svg
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
/usr/share/libwacom/layouts/xp-pen-star03.svg
/usr/share/libwacom/libwacom.stylus
/usr/share/libwacom/mobilestudio-pro-13.tablet
/usr/share/libwacom/mobilestudio-pro-16.tablet
/usr/share/libwacom/n-trig-pen.tablet
/usr/share/libwacom/one-by-wacom-m-p.tablet
/usr/share/libwacom/one-by-wacom-m-p2.tablet
/usr/share/libwacom/one-by-wacom-s-p.tablet
/usr/share/libwacom/one-by-wacom-s-p2.tablet
/usr/share/libwacom/serial-wacf004.tablet
/usr/share/libwacom/xp-pen-star03.tablet

%files dev
%defattr(-,root,root,-)
/usr/include/libwacom-1.0/libwacom/libwacom.h
/usr/lib64/libwacom.so
/usr/lib64/pkgconfig/libwacom.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libwacom.so.2
/usr/lib64/libwacom.so.2.6.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libwacom/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/libwacom-list-local-devices.1
