#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x707F91A424F006F5 (opensource@intra2net.com)
#
Name     : libftdi1
Version  : 1.4
Release  : 4
URL      : https://www.intra2net.com/en/developer/libftdi/download/libftdi1-1.4.tar.bz2
Source0  : https://www.intra2net.com/en/developer/libftdi/download/libftdi1-1.4.tar.bz2
Source99 : https://www.intra2net.com/en/developer/libftdi/download/libftdi1-1.4.tar.bz2.sig
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
* How to cross compile libftdi-1.x for Windows? *
1 - Prepare a pkg-config wrapper according to
https://www.flameeyes.eu/autotools-mythbuster/pkgconfig/cross-compiling.html ,
additionally export PKG_CONFIG_ALLOW_SYSTEM_CFLAGS and
PKG_CONFIG_ALLOW_SYSTEM_LIBS.
2 - Write a CMake toolchain file according to
http://www.vtk.org/Wiki/CmakeMingw . Change the path to your future sysroot.
3 - Get libusb sources (either by cloning the git repo or by downloading a
tarball). Unpack, autogen.sh (when building from git), and configure like this:
./configure --build=`./config.guess` --host=i686-w64-mingw32 \
--prefix=/usr --with-sysroot=$HOME/i686-w64-mingw32-root/
4 - run
make install DESTDIR=$HOME/i686-w64-mingw32-root/
5 - go to libftdi-1.x source directory and run
cmake -DCMAKE_TOOLCHAIN_FILE=~/Toolchain-mingw.cmake \
-DCMAKE_INSTALL_PREFIX="/usr" \
-DPKG_CONFIG_EXECUTABLE=`which i686-w64-mingw32-pkg-config`
6 - run
make install DESTDIR=$HOME/i686-w64-mingw32-root/

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

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552062817
mkdir -p clr-build
pushd clr-build
export LDFLAGS="${LDFLAGS} -fno-lto"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1552062817
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libftdi1
cp COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/libftdi1/COPYING-CMAKE-SCRIPTS
cp COPYING.GPL %{buildroot}/usr/share/package-licenses/libftdi1/COPYING.GPL
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/libftdi1/COPYING.LIB
cp LICENSE %{buildroot}/usr/share/package-licenses/libftdi1/LICENSE
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
/usr/share/package-licenses/libftdi1/COPYING-CMAKE-SCRIPTS
/usr/share/package-licenses/libftdi1/COPYING.GPL
/usr/share/package-licenses/libftdi1/COPYING.LIB
/usr/share/package-licenses/libftdi1/LICENSE
