#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v22
# autospec commit: d73a1e7
#
# Source0 file verified with key 0xE23B7E70B467F0BF (office@who-t.net)
#
Name     : libwacom
Version  : 2.12.2
Release  : 40
URL      : https://github.com/linuxwacom/libwacom/releases/download/libwacom-2.12.2/libwacom-2.12.2.tar.xz
Source0  : https://github.com/linuxwacom/libwacom/releases/download/libwacom-2.12.2/libwacom-2.12.2.tar.xz
Source1  : https://github.com/linuxwacom/libwacom/releases/download/libwacom-2.12.2/libwacom-2.12.2.tar.xz.sig
Source2  : E23B7E70B467F0BF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : HPND
Requires: libwacom-bin = %{version}-%{release}
Requires: libwacom-config = %{version}-%{release}
Requires: libwacom-data = %{version}-%{release}
Requires: libwacom-lib = %{version}-%{release}
Requires: libwacom-license = %{version}-%{release}
Requires: libwacom-man = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : gettext
BuildRequires : gnupg
BuildRequires : intltool
BuildRequires : itstool
BuildRequires : libevdev-dev
BuildRequires : libgudev-dev
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pypi-libevdev
BuildRequires : pypi-pytest
BuildRequires : pyudev
BuildRequires : valgrind
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Overview
libwacom is a library to identify graphics tablets and their model-specific
features. It provides easy access to information such as "is this a built-in
on-screen tablet", "what is the size of this model", etc.

%package bin
Summary: bin components for the libwacom package.
Group: Binaries
Requires: libwacom-data = %{version}-%{release}
Requires: libwacom-config = %{version}-%{release}
Requires: libwacom-license = %{version}-%{release}

%description bin
bin components for the libwacom package.


%package config
Summary: config components for the libwacom package.
Group: Default

%description config
config components for the libwacom package.


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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) E23B7E70B467F0BF' gpg.status
%setup -q -n libwacom-2.12.2
cd %{_builddir}/libwacom-2.12.2
pushd ..
cp -a libwacom-2.12.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1743198095
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs
cd ../buildavx2;
meson test -C builddir --print-errorlogs || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/libwacom
cp %{_builddir}/libwacom-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libwacom/8e668446f99b374135786b7ef7ee75ddfafbaef2 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/libwacom-list-devices
/V3/usr/bin/libwacom-list-local-devices
/usr/bin/libwacom-list-devices
/usr/bin/libwacom-list-local-devices
/usr/bin/libwacom-show-stylus
/usr/bin/libwacom-update-db

%files config
%defattr(-,root,root,-)
/usr/lib/udev/hwdb.d/65-libwacom.hwdb
/usr/lib/udev/rules.d/65-libwacom.rules

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
/usr/share/libwacom/chuwi-minibookx.tablet
/usr/share/libwacom/cintiq-12wx.tablet
/usr/share/libwacom/cintiq-13hd.tablet
/usr/share/libwacom/cintiq-13hdt.tablet
/usr/share/libwacom/cintiq-16-2.tablet
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
/usr/share/libwacom/cintiq-pro-16-2.tablet
/usr/share/libwacom/cintiq-pro-16.tablet
/usr/share/libwacom/cintiq-pro-17.tablet
/usr/share/libwacom/cintiq-pro-22.tablet
/usr/share/libwacom/cintiq-pro-24-p.tablet
/usr/share/libwacom/cintiq-pro-24-pt.tablet
/usr/share/libwacom/cintiq-pro-27.tablet
/usr/share/libwacom/cintiq-pro-32.tablet
/usr/share/libwacom/dell-canvas-27.tablet
/usr/share/libwacom/dtc-121.tablet
/usr/share/libwacom/dtf-720.tablet
/usr/share/libwacom/dth-1152.tablet
/usr/share/libwacom/dth-134.tablet
/usr/share/libwacom/dth-2242.tablet
/usr/share/libwacom/dth-2452.tablet
/usr/share/libwacom/dti-520.tablet
/usr/share/libwacom/dtk-1651.tablet
/usr/share/libwacom/dtk-1660e-2.tablet
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
/usr/share/libwacom/elan-0732.tablet
/usr/share/libwacom/elan-2072.tablet
/usr/share/libwacom/elan-22e2.tablet
/usr/share/libwacom/elan-22f7.tablet
/usr/share/libwacom/elan-24d8.tablet
/usr/share/libwacom/elan-24db.tablet
/usr/share/libwacom/elan-2513.tablet
/usr/share/libwacom/elan-2514-alt.tablet
/usr/share/libwacom/elan-2514-alt2.tablet
/usr/share/libwacom/elan-2514.tablet
/usr/share/libwacom/elan-2537.tablet
/usr/share/libwacom/elan-2627.tablet
/usr/share/libwacom/elan-2628.tablet
/usr/share/libwacom/elan-262b.tablet
/usr/share/libwacom/elan-264c.tablet
/usr/share/libwacom/elan-29a1.tablet
/usr/share/libwacom/elan-29b6.tablet
/usr/share/libwacom/elan-2a70.tablet
/usr/share/libwacom/elan-2ad9.tablet
/usr/share/libwacom/elan-2bb3.tablet
/usr/share/libwacom/elan-2bd6.tablet
/usr/share/libwacom/elan-2c1b.tablet
/usr/share/libwacom/elan-2d55.tablet
/usr/share/libwacom/elan-2fc2.tablet
/usr/share/libwacom/elan-425a.tablet
/usr/share/libwacom/elan-425b.tablet
/usr/share/libwacom/elan-5515.tablet
/usr/share/libwacom/gaomon-1060pro.tablet
/usr/share/libwacom/gaomon-1061pro.tablet
/usr/share/libwacom/gaomon-a1201.tablet
/usr/share/libwacom/gaomon-a5h.tablet
/usr/share/libwacom/gaomon-a5h_mt.tablet
/usr/share/libwacom/gaomon-a601.tablet
/usr/share/libwacom/gaomon-a801.tablet
/usr/share/libwacom/gaomon-d16-pro.tablet
/usr/share/libwacom/gaomon-d22s.tablet
/usr/share/libwacom/gaomon-g12.tablet
/usr/share/libwacom/gaomon-g12gd.tablet
/usr/share/libwacom/gaomon-g13.tablet
/usr/share/libwacom/gaomon-g13gd.tablet
/usr/share/libwacom/gaomon-g16.tablet
/usr/share/libwacom/gaomon-g16gd.tablet
/usr/share/libwacom/gaomon-g22.tablet
/usr/share/libwacom/gaomon-gm116hd.tablet
/usr/share/libwacom/gaomon-gm116hdtp.tablet
/usr/share/libwacom/gaomon-gm156hd.tablet
/usr/share/libwacom/gaomon-gm156hdtp.tablet
/usr/share/libwacom/gaomon-gm185.tablet
/usr/share/libwacom/gaomon-gm220hd.tablet
/usr/share/libwacom/gaomon-gm24.tablet
/usr/share/libwacom/gaomon-gm24tp.tablet
/usr/share/libwacom/gaomon-gt-1106.tablet
/usr/share/libwacom/gaomon-gt116h.tablet
/usr/share/libwacom/gaomon-jr156.tablet
/usr/share/libwacom/gaomon-m0610-pro.tablet
/usr/share/libwacom/gaomon-m10.tablet
/usr/share/libwacom/gaomon-m106k-pro.tablet
/usr/share/libwacom/gaomon-m106k.tablet
/usr/share/libwacom/gaomon-m10k-2018.tablet
/usr/share/libwacom/gaomon-m10k-pro.tablet
/usr/share/libwacom/gaomon-m1220.tablet
/usr/share/libwacom/gaomon-m1230.tablet
/usr/share/libwacom/gaomon-m6.tablet
/usr/share/libwacom/gaomon-m62022.tablet
/usr/share/libwacom/gaomon-m7.tablet
/usr/share/libwacom/gaomon-m8.tablet
/usr/share/libwacom/gaomon-pd1161.tablet
/usr/share/libwacom/gaomon-pd1161gd.tablet
/usr/share/libwacom/gaomon-pd1220.tablet
/usr/share/libwacom/gaomon-pd1220gd.tablet
/usr/share/libwacom/gaomon-pd1320.tablet
/usr/share/libwacom/gaomon-pd1320gd.tablet
/usr/share/libwacom/gaomon-pd1560.tablet
/usr/share/libwacom/gaomon-pd1561.tablet
/usr/share/libwacom/gaomon-pd1561gd.tablet
/usr/share/libwacom/gaomon-pd156pro.tablet
/usr/share/libwacom/gaomon-pd156progd.tablet
/usr/share/libwacom/gaomon-pd1610.tablet
/usr/share/libwacom/gaomon-pd1611.tablet
/usr/share/libwacom/gaomon-pd1620.tablet
/usr/share/libwacom/gaomon-pd1621.tablet
/usr/share/libwacom/gaomon-pd2200.tablet
/usr/share/libwacom/gaomon-pd2400.tablet
/usr/share/libwacom/gaomon-pd2401.tablet
/usr/share/libwacom/gaomon-s56k.tablet
/usr/share/libwacom/gaomon-s620.tablet
/usr/share/libwacom/gaomon-s630.tablet
/usr/share/libwacom/gaomon-s830.tablet
/usr/share/libwacom/gaomon-sn540-m5.tablet
/usr/share/libwacom/gaomon-sp1603.tablet
/usr/share/libwacom/gaomon-t01.tablet
/usr/share/libwacom/gaomon-t02.tablet
/usr/share/libwacom/gaomon-tm156w.tablet
/usr/share/libwacom/gaomon-u16-tp4k.tablet
/usr/share/libwacom/gaomon-u164k.tablet
/usr/share/libwacom/gaomon-wh850.tablet
/usr/share/libwacom/gaomon-wh851.tablet
/usr/share/libwacom/generic.tablet
/usr/share/libwacom/graphire-usb.tablet
/usr/share/libwacom/graphire-wireless-8x6.tablet
/usr/share/libwacom/graphire2-4x5.tablet
/usr/share/libwacom/graphire2-5x7.tablet
/usr/share/libwacom/graphire3-4x5.tablet
/usr/share/libwacom/graphire3-6x8.tablet
/usr/share/libwacom/graphire4-4x5.tablet
/usr/share/libwacom/graphire4-6x8.tablet
/usr/share/libwacom/hp-pro-tablet-408.tablet
/usr/share/libwacom/huion-420.tablet
/usr/share/libwacom/huion-gc610-710.tablet
/usr/share/libwacom/huion-h1060p.tablet
/usr/share/libwacom/huion-h420.tablet
/usr/share/libwacom/huion-h610-pro.tablet
/usr/share/libwacom/huion-h640p.tablet
/usr/share/libwacom/huion-h950p-igg.tablet
/usr/share/libwacom/huion-h950p.tablet
/usr/share/libwacom/huion-hc16.tablet
/usr/share/libwacom/huion-hs610.tablet
/usr/share/libwacom/huion-hs611.tablet
/usr/share/libwacom/huion-hs64.tablet
/usr/share/libwacom/huion-hs95.tablet
/usr/share/libwacom/huion-hst640.tablet
/usr/share/libwacom/huion-inspiroy-2-l---h1061p.tablet
/usr/share/libwacom/huion-inspiroy-2-m---h951p.tablet
/usr/share/libwacom/huion-inspiroy-2-s---h641p.tablet
/usr/share/libwacom/huion-inspiroy-dial-2.tablet
/usr/share/libwacom/huion-inspiroy-dial-q620m.tablet
/usr/share/libwacom/huion-inspiroy-g10t.tablet
/usr/share/libwacom/huion-inspiroy-giano.tablet
/usr/share/libwacom/huion-inspiroy-h1161.tablet
/usr/share/libwacom/huion-inspiroy-h420x.tablet
/usr/share/libwacom/huion-inspiroy-h430p.tablet
/usr/share/libwacom/huion-inspiroy-h580x.tablet
/usr/share/libwacom/huion-inspiroy-h610x.tablet
/usr/share/libwacom/huion-inspiroy-ink-h320m.tablet
/usr/share/libwacom/huion-inspiroy-keydial-kd200.tablet
/usr/share/libwacom/huion-inspiroy-q11k-v2.tablet
/usr/share/libwacom/huion-inspiroy-q11k.tablet
/usr/share/libwacom/huion-inspiroy-q620m.tablet
/usr/share/libwacom/huion-inspiroy-wh1409-v2.tablet
/usr/share/libwacom/huion-kamvas-12-gs1161.tablet
/usr/share/libwacom/huion-kamvas-13.tablet
/usr/share/libwacom/huion-kamvas-16-gs1562.tablet
/usr/share/libwacom/huion-kamvas-162019.tablet
/usr/share/libwacom/huion-kamvas-19.tablet
/usr/share/libwacom/huion-kamvas-20-gs1901.tablet
/usr/share/libwacom/huion-kamvas-22-gs2201.tablet
/usr/share/libwacom/huion-kamvas-22-gs2202.tablet
/usr/share/libwacom/huion-kamvas-24-gs2401.tablet
/usr/share/libwacom/huion-kamvas-24-plus-gs2402.tablet
/usr/share/libwacom/huion-kamvas-gt-156-2021.tablet
/usr/share/libwacom/huion-kamvas-gt-156hd-v2.tablet
/usr/share/libwacom/huion-kamvas-gt-191-v2.tablet
/usr/share/libwacom/huion-kamvas-gt-191.tablet
/usr/share/libwacom/huion-kamvas-gt-220-v2.tablet
/usr/share/libwacom/huion-kamvas-gt-221-pro.tablet
/usr/share/libwacom/huion-kamvas-pro-12-gt-116.tablet
/usr/share/libwacom/huion-kamvas-pro-13-gt1302.tablet
/usr/share/libwacom/huion-kamvas-pro-13.tablet
/usr/share/libwacom/huion-kamvas-pro-16-gt-156.tablet
/usr/share/libwacom/huion-kamvas-pro-16-gt1561.tablet
/usr/share/libwacom/huion-kamvas-pro-16-gt1602.tablet
/usr/share/libwacom/huion-kamvas-pro-16-plus-gt1562.tablet
/usr/share/libwacom/huion-kamvas-pro-20-gt-192.tablet
/usr/share/libwacom/huion-kamvas-pro-20-gt1901.tablet
/usr/share/libwacom/huion-kamvas-pro-22-gt-221.tablet
/usr/share/libwacom/huion-kamvas-pro-24-gt2401.tablet
/usr/share/libwacom/huion-kamvas-pro-24.tablet
/usr/share/libwacom/huion-kamvas-pro-studio-22.tablet
/usr/share/libwacom/huion-kamvas-rds-220.tablet
/usr/share/libwacom/huion-kizuna-hs952.tablet
/usr/share/libwacom/huion-mini-keydial-kd100.tablet
/usr/share/libwacom/huion-new-1060-plus.tablet
/usr/share/libwacom/huion-note-x10.tablet
/usr/share/libwacom/huion-rds-160.tablet
/usr/share/libwacom/huion-rte-100.tablet
/usr/share/libwacom/huion-rtm-500.tablet
/usr/share/libwacom/huion-rtp-700.tablet
/usr/share/libwacom/huion-rts-300.tablet
/usr/share/libwacom/huion-wh1409.tablet
/usr/share/libwacom/ingenic-6161.tablet
/usr/share/libwacom/intuos-12x12.tablet
/usr/share/libwacom/intuos-12x18.tablet
/usr/share/libwacom/intuos-4x5.tablet
/usr/share/libwacom/intuos-6x8.tablet
/usr/share/libwacom/intuos-9x12.tablet
/usr/share/libwacom/intuos-m-p.tablet
/usr/share/libwacom/intuos-m-p2.tablet
/usr/share/libwacom/intuos-m-p3-android.tablet
/usr/share/libwacom/intuos-m-p3-wl-android.tablet
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
/usr/share/libwacom/intuos-s-p3-android.tablet
/usr/share/libwacom/intuos-s-p3-wl-android.tablet
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
/usr/share/libwacom/isdv4-016c.tablet
/usr/share/libwacom/isdv4-100.tablet
/usr/share/libwacom/isdv4-101.tablet
/usr/share/libwacom/isdv4-104.tablet
/usr/share/libwacom/isdv4-10d.tablet
/usr/share/libwacom/isdv4-10e.tablet
/usr/share/libwacom/isdv4-10f.tablet
/usr/share/libwacom/isdv4-114.tablet
/usr/share/libwacom/isdv4-116.tablet
/usr/share/libwacom/isdv4-117.tablet
/usr/share/libwacom/isdv4-121a.tablet
/usr/share/libwacom/isdv4-124.tablet
/usr/share/libwacom/isdv4-12c.tablet
/usr/share/libwacom/isdv4-149.tablet
/usr/share/libwacom/isdv4-2d1f-001e.tablet
/usr/share/libwacom/isdv4-2d1f-002c.tablet
/usr/share/libwacom/isdv4-2d1f-002e.tablet
/usr/share/libwacom/isdv4-2d1f-0040.tablet
/usr/share/libwacom/isdv4-2d1f-0066.tablet
/usr/share/libwacom/isdv4-2d1f-0095.tablet
/usr/share/libwacom/isdv4-2d1f-0114.tablet
/usr/share/libwacom/isdv4-2d1f-0136.tablet
/usr/share/libwacom/isdv4-2d1f-0163.tablet
/usr/share/libwacom/isdv4-2d1f-524c.tablet
/usr/share/libwacom/isdv4-4004.tablet
/usr/share/libwacom/isdv4-4800.tablet
/usr/share/libwacom/isdv4-4804.tablet
/usr/share/libwacom/isdv4-4806.tablet
/usr/share/libwacom/isdv4-4807.tablet
/usr/share/libwacom/isdv4-4809.tablet
/usr/share/libwacom/isdv4-4814.tablet
/usr/share/libwacom/isdv4-481a.tablet
/usr/share/libwacom/isdv4-4822.tablet
/usr/share/libwacom/isdv4-4824.tablet
/usr/share/libwacom/isdv4-4831.tablet
/usr/share/libwacom/isdv4-4834.tablet
/usr/share/libwacom/isdv4-4838.tablet
/usr/share/libwacom/isdv4-4841.tablet
/usr/share/libwacom/isdv4-484c.tablet
/usr/share/libwacom/isdv4-484d.tablet
/usr/share/libwacom/isdv4-484e.tablet
/usr/share/libwacom/isdv4-4851.tablet
/usr/share/libwacom/isdv4-485e.tablet
/usr/share/libwacom/isdv4-4865.tablet
/usr/share/libwacom/isdv4-486a.tablet
/usr/share/libwacom/isdv4-4870.tablet
/usr/share/libwacom/isdv4-4875.tablet
/usr/share/libwacom/isdv4-488f.tablet
/usr/share/libwacom/isdv4-4898.tablet
/usr/share/libwacom/isdv4-48b7.tablet
/usr/share/libwacom/isdv4-48c9.tablet
/usr/share/libwacom/isdv4-48ca.tablet
/usr/share/libwacom/isdv4-48ce.tablet
/usr/share/libwacom/isdv4-48d6.tablet
/usr/share/libwacom/isdv4-48eb.tablet
/usr/share/libwacom/isdv4-48ec.tablet
/usr/share/libwacom/isdv4-48ed.tablet
/usr/share/libwacom/isdv4-48ee.tablet
/usr/share/libwacom/isdv4-48f6.tablet
/usr/share/libwacom/isdv4-490a.tablet
/usr/share/libwacom/isdv4-490b.tablet
/usr/share/libwacom/isdv4-4957.tablet
/usr/share/libwacom/isdv4-495f.tablet
/usr/share/libwacom/isdv4-496c.tablet
/usr/share/libwacom/isdv4-4988.tablet
/usr/share/libwacom/isdv4-4995.tablet
/usr/share/libwacom/isdv4-49a3.tablet
/usr/share/libwacom/isdv4-49c8.tablet
/usr/share/libwacom/isdv4-5000.tablet
/usr/share/libwacom/isdv4-5002.tablet
/usr/share/libwacom/isdv4-5010.tablet
/usr/share/libwacom/isdv4-5013.tablet
/usr/share/libwacom/isdv4-5014.tablet
/usr/share/libwacom/isdv4-5019.tablet
/usr/share/libwacom/isdv4-502a.tablet
/usr/share/libwacom/isdv4-503e.tablet
/usr/share/libwacom/isdv4-503f.tablet
/usr/share/libwacom/isdv4-5040.tablet
/usr/share/libwacom/isdv4-5044.tablet
/usr/share/libwacom/isdv4-5048.tablet
/usr/share/libwacom/isdv4-504a.tablet
/usr/share/libwacom/isdv4-504c.tablet
/usr/share/libwacom/isdv4-5072.tablet
/usr/share/libwacom/isdv4-5090.tablet
/usr/share/libwacom/isdv4-5093.tablet
/usr/share/libwacom/isdv4-5099.tablet
/usr/share/libwacom/isdv4-509d.tablet
/usr/share/libwacom/isdv4-509f.tablet
/usr/share/libwacom/isdv4-50a0.tablet
/usr/share/libwacom/isdv4-50a9.tablet
/usr/share/libwacom/isdv4-50b4.tablet
/usr/share/libwacom/isdv4-50b6.tablet
/usr/share/libwacom/isdv4-50b8.tablet
/usr/share/libwacom/isdv4-50db.tablet
/usr/share/libwacom/isdv4-50e9.tablet
/usr/share/libwacom/isdv4-50ef.tablet
/usr/share/libwacom/isdv4-50f1.tablet
/usr/share/libwacom/isdv4-50f8.tablet
/usr/share/libwacom/isdv4-50fd.tablet
/usr/share/libwacom/isdv4-50fe.tablet
/usr/share/libwacom/isdv4-5110.tablet
/usr/share/libwacom/isdv4-5115.tablet
/usr/share/libwacom/isdv4-511a.tablet
/usr/share/libwacom/isdv4-5122.tablet
/usr/share/libwacom/isdv4-5128.tablet
/usr/share/libwacom/isdv4-513b.tablet
/usr/share/libwacom/isdv4-5144.tablet
/usr/share/libwacom/isdv4-5146.tablet
/usr/share/libwacom/isdv4-5147.tablet
/usr/share/libwacom/isdv4-5148.tablet
/usr/share/libwacom/isdv4-5150.tablet
/usr/share/libwacom/isdv4-5155.tablet
/usr/share/libwacom/isdv4-5157.tablet
/usr/share/libwacom/isdv4-5158.tablet
/usr/share/libwacom/isdv4-5159.tablet
/usr/share/libwacom/isdv4-515a.tablet
/usr/share/libwacom/isdv4-5169.tablet
/usr/share/libwacom/isdv4-516b.tablet
/usr/share/libwacom/isdv4-517d.tablet
/usr/share/libwacom/isdv4-5196.tablet
/usr/share/libwacom/isdv4-51a0.tablet
/usr/share/libwacom/isdv4-51af.tablet
/usr/share/libwacom/isdv4-51b0.tablet
/usr/share/libwacom/isdv4-51b1.tablet
/usr/share/libwacom/isdv4-51b2.tablet
/usr/share/libwacom/isdv4-51b3.tablet
/usr/share/libwacom/isdv4-51b6.tablet
/usr/share/libwacom/isdv4-51b7.tablet
/usr/share/libwacom/isdv4-51b8.tablet
/usr/share/libwacom/isdv4-51b9.tablet
/usr/share/libwacom/isdv4-51ba.tablet
/usr/share/libwacom/isdv4-51bb.tablet
/usr/share/libwacom/isdv4-51bc.tablet
/usr/share/libwacom/isdv4-51bd.tablet
/usr/share/libwacom/isdv4-51be.tablet
/usr/share/libwacom/isdv4-51bf.tablet
/usr/share/libwacom/isdv4-51c4.tablet
/usr/share/libwacom/isdv4-51c7.tablet
/usr/share/libwacom/isdv4-51d0.tablet
/usr/share/libwacom/isdv4-51e2.tablet
/usr/share/libwacom/isdv4-51e9.tablet
/usr/share/libwacom/isdv4-51ef.tablet
/usr/share/libwacom/isdv4-51f5.tablet
/usr/share/libwacom/isdv4-51f6.tablet
/usr/share/libwacom/isdv4-51f9.tablet
/usr/share/libwacom/isdv4-5202.tablet
/usr/share/libwacom/isdv4-5204.tablet
/usr/share/libwacom/isdv4-5215.tablet
/usr/share/libwacom/isdv4-5216.tablet
/usr/share/libwacom/isdv4-5218.tablet
/usr/share/libwacom/isdv4-521c.tablet
/usr/share/libwacom/isdv4-521f.tablet
/usr/share/libwacom/isdv4-5220.tablet
/usr/share/libwacom/isdv4-5221.tablet
/usr/share/libwacom/isdv4-5222.tablet
/usr/share/libwacom/isdv4-5229.tablet
/usr/share/libwacom/isdv4-523a.tablet
/usr/share/libwacom/isdv4-523e.tablet
/usr/share/libwacom/isdv4-5256.tablet
/usr/share/libwacom/isdv4-526c.tablet
/usr/share/libwacom/isdv4-5276.tablet
/usr/share/libwacom/isdv4-5277.tablet
/usr/share/libwacom/isdv4-5278.tablet
/usr/share/libwacom/isdv4-5279.tablet
/usr/share/libwacom/isdv4-527a.tablet
/usr/share/libwacom/isdv4-527e.tablet
/usr/share/libwacom/isdv4-527f.tablet
/usr/share/libwacom/isdv4-5285.tablet
/usr/share/libwacom/isdv4-5286.tablet
/usr/share/libwacom/isdv4-528e.tablet
/usr/share/libwacom/isdv4-52a2.tablet
/usr/share/libwacom/isdv4-52b0.tablet
/usr/share/libwacom/isdv4-52d3.tablet
/usr/share/libwacom/isdv4-52d5.tablet
/usr/share/libwacom/isdv4-5309.tablet
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
/usr/share/libwacom/layouts/cintiq-pro-16-2.svg
/usr/share/libwacom/layouts/cintiq-pro-17.svg
/usr/share/libwacom/layouts/cintiq-pro-22.svg
/usr/share/libwacom/layouts/cintiq-pro-27.svg
/usr/share/libwacom/layouts/dth-2242.svg
/usr/share/libwacom/layouts/dth-2452.svg
/usr/share/libwacom/layouts/dti-520.svg
/usr/share/libwacom/layouts/dtk-1651.svg
/usr/share/libwacom/layouts/dtk-2451.svg
/usr/share/libwacom/layouts/dtu-1031.svg
/usr/share/libwacom/layouts/dtu-1141.svg
/usr/share/libwacom/layouts/dtu-1141b.svg
/usr/share/libwacom/layouts/ek-remote.svg
/usr/share/libwacom/layouts/gaomon-1060pro.svg
/usr/share/libwacom/layouts/gaomon-1061pro.svg
/usr/share/libwacom/layouts/gaomon-a1201.svg
/usr/share/libwacom/layouts/gaomon-a5h.svg
/usr/share/libwacom/layouts/gaomon-a5h_mt.svg
/usr/share/libwacom/layouts/gaomon-a601.svg
/usr/share/libwacom/layouts/gaomon-a801.svg
/usr/share/libwacom/layouts/gaomon-d16-pro.svg
/usr/share/libwacom/layouts/gaomon-g12.svg
/usr/share/libwacom/layouts/gaomon-g12gd.svg
/usr/share/libwacom/layouts/gaomon-g13.svg
/usr/share/libwacom/layouts/gaomon-g13gd.svg
/usr/share/libwacom/layouts/gaomon-g16.svg
/usr/share/libwacom/layouts/gaomon-g16gd.svg
/usr/share/libwacom/layouts/gaomon-g22.svg
/usr/share/libwacom/layouts/gaomon-gm116hd.svg
/usr/share/libwacom/layouts/gaomon-gm116hdtp.svg
/usr/share/libwacom/layouts/gaomon-gm156hd.svg
/usr/share/libwacom/layouts/gaomon-gm156hdtp.svg
/usr/share/libwacom/layouts/gaomon-gt-1106.svg
/usr/share/libwacom/layouts/gaomon-gt116h.svg
/usr/share/libwacom/layouts/gaomon-m0610-pro.svg
/usr/share/libwacom/layouts/gaomon-m10.svg
/usr/share/libwacom/layouts/gaomon-m106k-pro.svg
/usr/share/libwacom/layouts/gaomon-m106k.svg
/usr/share/libwacom/layouts/gaomon-m10k-2018.svg
/usr/share/libwacom/layouts/gaomon-m10k-pro.svg
/usr/share/libwacom/layouts/gaomon-m1220.svg
/usr/share/libwacom/layouts/gaomon-m1230.svg
/usr/share/libwacom/layouts/gaomon-m6.svg
/usr/share/libwacom/layouts/gaomon-m62022.svg
/usr/share/libwacom/layouts/gaomon-m7.svg
/usr/share/libwacom/layouts/gaomon-m8.svg
/usr/share/libwacom/layouts/gaomon-pd1161.svg
/usr/share/libwacom/layouts/gaomon-pd1161gd.svg
/usr/share/libwacom/layouts/gaomon-pd1560.svg
/usr/share/libwacom/layouts/gaomon-pd1561.svg
/usr/share/libwacom/layouts/gaomon-pd1561gd.svg
/usr/share/libwacom/layouts/gaomon-pd156pro.svg
/usr/share/libwacom/layouts/gaomon-pd156progd.svg
/usr/share/libwacom/layouts/gaomon-pd1610.svg
/usr/share/libwacom/layouts/gaomon-pd1611.svg
/usr/share/libwacom/layouts/gaomon-pd2200.svg
/usr/share/libwacom/layouts/gaomon-s620.svg
/usr/share/libwacom/layouts/gaomon-s630.svg
/usr/share/libwacom/layouts/gaomon-s830.svg
/usr/share/libwacom/layouts/gaomon-sn540-m5.svg
/usr/share/libwacom/layouts/gaomon-sp1603.svg
/usr/share/libwacom/layouts/gaomon-t01.svg
/usr/share/libwacom/layouts/gaomon-t02.svg
/usr/share/libwacom/layouts/gaomon-wh850.svg
/usr/share/libwacom/layouts/gaomon-wh851.svg
/usr/share/libwacom/layouts/graphire-wireless-8x6.svg
/usr/share/libwacom/layouts/graphire4-4x5.svg
/usr/share/libwacom/layouts/graphire4-6x8.svg
/usr/share/libwacom/layouts/huion-gc610-710.svg
/usr/share/libwacom/layouts/huion-h1060p.svg
/usr/share/libwacom/layouts/huion-h420.svg
/usr/share/libwacom/layouts/huion-h610-pro.svg
/usr/share/libwacom/layouts/huion-h640p.svg
/usr/share/libwacom/layouts/huion-h950p-igg.svg
/usr/share/libwacom/layouts/huion-h950p.svg
/usr/share/libwacom/layouts/huion-hc16.svg
/usr/share/libwacom/layouts/huion-hs610.svg
/usr/share/libwacom/layouts/huion-hs611.svg
/usr/share/libwacom/layouts/huion-hs64.svg
/usr/share/libwacom/layouts/huion-hs95.svg
/usr/share/libwacom/layouts/huion-hst640.svg
/usr/share/libwacom/layouts/huion-inspiroy-2-l---h1061p.svg
/usr/share/libwacom/layouts/huion-inspiroy-2-m---h951p.svg
/usr/share/libwacom/layouts/huion-inspiroy-2-s---h641p.svg
/usr/share/libwacom/layouts/huion-inspiroy-dial-2.svg
/usr/share/libwacom/layouts/huion-inspiroy-dial-q620m.svg
/usr/share/libwacom/layouts/huion-inspiroy-g10t.svg
/usr/share/libwacom/layouts/huion-inspiroy-giano.svg
/usr/share/libwacom/layouts/huion-inspiroy-h1161.svg
/usr/share/libwacom/layouts/huion-inspiroy-h430p.svg
/usr/share/libwacom/layouts/huion-inspiroy-h580x.svg
/usr/share/libwacom/layouts/huion-inspiroy-h610x.svg
/usr/share/libwacom/layouts/huion-inspiroy-ink-h320m.svg
/usr/share/libwacom/layouts/huion-inspiroy-keydial-kd200.svg
/usr/share/libwacom/layouts/huion-inspiroy-q11k-v2.svg
/usr/share/libwacom/layouts/huion-inspiroy-q11k.svg
/usr/share/libwacom/layouts/huion-inspiroy-q620m.svg
/usr/share/libwacom/layouts/huion-inspiroy-wh1409-v2.svg
/usr/share/libwacom/layouts/huion-kamvas-12-gs1161.svg
/usr/share/libwacom/layouts/huion-kamvas-13.svg
/usr/share/libwacom/layouts/huion-kamvas-16-gs1562.svg
/usr/share/libwacom/layouts/huion-kamvas-162019.svg
/usr/share/libwacom/layouts/huion-kamvas-gt-156-2021.svg
/usr/share/libwacom/layouts/huion-kamvas-gt-156hd-v2.svg
/usr/share/libwacom/layouts/huion-kamvas-gt-221-pro.svg
/usr/share/libwacom/layouts/huion-kamvas-pro-12-gt-116.svg
/usr/share/libwacom/layouts/huion-kamvas-pro-13-gt1302.svg
/usr/share/libwacom/layouts/huion-kamvas-pro-13.svg
/usr/share/libwacom/layouts/huion-kamvas-pro-16-gt-156.svg
/usr/share/libwacom/layouts/huion-kamvas-pro-16-gt1602.svg
/usr/share/libwacom/layouts/huion-kamvas-pro-20-gt-192.svg
/usr/share/libwacom/layouts/huion-kamvas-pro-20-gt1901.svg
/usr/share/libwacom/layouts/huion-kamvas-pro-22-gt-221.svg
/usr/share/libwacom/layouts/huion-kamvas-pro-24.svg
/usr/share/libwacom/layouts/huion-kamvas-pro-studio-22.svg
/usr/share/libwacom/layouts/huion-mini-keydial-kd100.svg
/usr/share/libwacom/layouts/huion-new-1060-plus.svg
/usr/share/libwacom/layouts/huion-rds-160.svg
/usr/share/libwacom/layouts/huion-rte-100.svg
/usr/share/libwacom/layouts/huion-rtm-500.svg
/usr/share/libwacom/layouts/huion-rtp-700.svg
/usr/share/libwacom/layouts/huion-rts-300.svg
/usr/share/libwacom/layouts/huion-wh1409.svg
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
/usr/share/libwacom/layouts/movink.svg
/usr/share/libwacom/layouts/xp-pen-artist10s.svg
/usr/share/libwacom/layouts/xp-pen-artist12.svg
/usr/share/libwacom/layouts/xp-pen-artist13-3-pro.svg
/usr/share/libwacom/layouts/xp-pen-deco-l.svg
/usr/share/libwacom/layouts/xp-pen-deco-mini4.svg
/usr/share/libwacom/layouts/xp-pen-deco-mw.svg
/usr/share/libwacom/layouts/xp-pen-deco-pro-s-m-sw-mw.svg
/usr/share/libwacom/layouts/xp-pen-deco01-v2.svg
/usr/share/libwacom/layouts/xp-pen-star03.svg
/usr/share/libwacom/lenovo-ideapad-duet.tablet
/usr/share/libwacom/letsketch-wp9620.tablet
/usr/share/libwacom/libwacom.stylus
/usr/share/libwacom/mobilestudio-pro-13-2.tablet
/usr/share/libwacom/mobilestudio-pro-13.tablet
/usr/share/libwacom/mobilestudio-pro-16-2.tablet
/usr/share/libwacom/mobilestudio-pro-16-3.tablet
/usr/share/libwacom/mobilestudio-pro-16.tablet
/usr/share/libwacom/movink.tablet
/usr/share/libwacom/n-trig-pen.tablet
/usr/share/libwacom/one-by-wacom-m-p.tablet
/usr/share/libwacom/one-by-wacom-m-p2.tablet
/usr/share/libwacom/one-by-wacom-s-p.tablet
/usr/share/libwacom/one-by-wacom-s-p2.tablet
/usr/share/libwacom/serial-wacf004.tablet
/usr/share/libwacom/surface-go-2.tablet
/usr/share/libwacom/surface-go.tablet
/usr/share/libwacom/volito-4x5.tablet
/usr/share/libwacom/wacom-hid-49a0-pen.tablet
/usr/share/libwacom/wacom-hid-52EB-pen.tablet
/usr/share/libwacom/wacom-hid-52fa-pen.tablet
/usr/share/libwacom/wacom-hid-5334-pen.tablet
/usr/share/libwacom/wacom-hid-5362.tablet
/usr/share/libwacom/wacom-one-12.tablet
/usr/share/libwacom/wacom-one-13.tablet
/usr/share/libwacom/wacom-one-pen-m.tablet
/usr/share/libwacom/wacom-one-pen-s.tablet
/usr/share/libwacom/wacom-one.tablet
/usr/share/libwacom/waltop-slim-tablet-12-1.tablet
/usr/share/libwacom/xp-pen-artist10s.tablet
/usr/share/libwacom/xp-pen-artist12.tablet
/usr/share/libwacom/xp-pen-artist13-3-pro.tablet
/usr/share/libwacom/xp-pen-deco-l.tablet
/usr/share/libwacom/xp-pen-deco-mini4.tablet
/usr/share/libwacom/xp-pen-deco-mini7.tablet
/usr/share/libwacom/xp-pen-deco-mw.tablet
/usr/share/libwacom/xp-pen-deco-pro-mw.tablet
/usr/share/libwacom/xp-pen-deco-pro-sw.tablet
/usr/share/libwacom/xp-pen-deco01-v2.tablet
/usr/share/libwacom/xp-pen-g430.tablet
/usr/share/libwacom/xp-pen-g430s.tablet
/usr/share/libwacom/xp-pen-g640.tablet
/usr/share/libwacom/xp-pen-star03.tablet

%files dev
%defattr(-,root,root,-)
/usr/include/libwacom-1.0/libwacom/libwacom.h
/usr/lib64/libwacom.so
/usr/lib64/pkgconfig/libwacom.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libwacom.so.9.0.0
/usr/lib64/libwacom.so.9
/usr/lib64/libwacom.so.9.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libwacom/8e668446f99b374135786b7ef7ee75ddfafbaef2

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/libwacom-list-devices.1
/usr/share/man/man1/libwacom-list-local-devices.1
