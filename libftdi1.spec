#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x707F91A424F006F5 (opensource@intra2net.com)
#
Name     : libftdi1
Version  : 1.4
Release  : 5
URL      : https://www.intra2net.com/en/developer/libftdi/download/libftdi1-1.4.tar.bz2
Source0  : https://www.intra2net.com/en/developer/libftdi/download/libftdi1-1.4.tar.bz2
Source1  : https://www.intra2net.com/en/developer/libftdi/download/libftdi1-1.4.tar.bz2.sig
Summary  : Library to program and control the FTDI USB controller
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 LGPL-2.0
Requires: libftdi1-bin = %{version}-%{release}
Requires: libftdi1-lib = %{version}-%{release}
Requires: libftdi1-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : pkg-config
BuildRequires : pkgconfig(libconfuse)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : python3-dev

%description
--------------------------------------------------------------------
libftdi version 1.4
--------------------------------------------------------------------

%package bin
Summary: bin components for the libftdi1 package.
Group: Binaries
Requires: libftdi1-license = %{version}-%{release}

%description bin
bin components for the libftdi1 package.


%package dev
Summary: dev components for the libftdi1 package.
Group: Development
Requires: libftdi1-lib = %{version}-%{release}
Requires: libftdi1-bin = %{version}-%{release}
Provides: libftdi1-devel = %{version}-%{release}
Requires: libftdi1 = %{version}-%{release}

%description dev
dev components for the libftdi1 package.


%package doc
Summary: doc components for the libftdi1 package.
Group: Documentation

%description doc
doc components for the libftdi1 package.


%package lib
Summary: lib components for the libftdi1 package.
Group: Libraries
Requires: libftdi1-license = %{version}-%{release}

%description lib
lib components for the libftdi1 package.


%package license
Summary: license components for the libftdi1 package.
Group: Default

%description license
license components for the libftdi1 package.


%prep
%setup -q -n libftdi1-1.4
cd %{_builddir}/libftdi1-1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592623782
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1592623782
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libftdi1
cp %{_builddir}/libftdi1-1.4/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/libftdi1/ff3ed70db4739b3c6747c7f624fe2bad70802987
cp %{_builddir}/libftdi1-1.4/COPYING.GPL %{buildroot}/usr/share/package-licenses/libftdi1/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/libftdi1-1.4/COPYING.LIB %{buildroot}/usr/share/package-licenses/libftdi1/ba8966e2473a9969bdcab3dc82274c817cfd98a1
cp %{_builddir}/libftdi1-1.4/LICENSE %{buildroot}/usr/share/package-licenses/libftdi1/98a992741b157246d2b3f6ed077428ab02dfa860
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ftdi_eeprom
/usr/bin/libftdi1-config

%files dev
%defattr(-,root,root,-)
/usr/include/libftdi1/ftdi.h
/usr/include/libftdi1/ftdi.hpp
/usr/lib64/cmake/libftdi1/LibFTDI1Config.cmake
/usr/lib64/cmake/libftdi1/LibFTDI1ConfigVersion.cmake
/usr/lib64/cmake/libftdi1/UseLibFTDI1.cmake
/usr/lib64/libftdi1.so
/usr/lib64/libftdipp1.so
/usr/lib64/pkgconfig/libftdi1.pc
/usr/lib64/pkgconfig/libftdipp1.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libftdi1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libftdi1.so.2
/usr/lib64/libftdi1.so.2.4.0
/usr/lib64/libftdipp1.so.2.4.0
/usr/lib64/libftdipp1.so.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libftdi1/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/libftdi1/98a992741b157246d2b3f6ed077428ab02dfa860
/usr/share/package-licenses/libftdi1/ba8966e2473a9969bdcab3dc82274c817cfd98a1
/usr/share/package-licenses/libftdi1/ff3ed70db4739b3c6747c7f624fe2bad70802987
