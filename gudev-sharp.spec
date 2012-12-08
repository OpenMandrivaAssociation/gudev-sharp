%define name gudev-sharp
%define version 0.1
%define git cd3e7df
%define release 5
%define api 1.0
%define udev 146

Summary: Mono bindings for the GUdev library
Name: %{name}
Version: %{version}
Release: %{release}
# http://github.com/mono/gudev-sharp/tarball/GUDEV_SHARP_0_1
Source0: %{name}-%{version}.tar.gz
License: LGPLv2+
Group: System/Libraries
Url: http://github.com/mono/gudev-sharp

BuildArch: noarch
BuildRequires: mono-devel
BuildRequires: gtk+2-devel
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: gtk-sharp2
BuildRequires: gtk-sharp2-devel
Requires: libgudev >= %udev

%description
This is a Mono binding for GUdev based on GTk#.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/Other

%description devel
This is a Mono binding for GUdev based on GTk#.

%prep
%setup -q -n mono-%name-%git
./autogen.sh

%build
./configure --prefix=%_prefix --libdir=%_prefix/lib
%make

%install
rm -rf %{buildroot}
%makeinstall_std pkgconfigdir=%_datadir/pkgconfig

%files
%doc AUTHORS
%_prefix/lib/mono/%name-%api
%_prefix/lib/mono/gac/%name

%files devel
%_datadir/pkgconfig/%name-%api.pc


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1-2mdv2011.0
+ Revision: 664961
- mass rebuild

  + Götz Waschk <waschk@mandriva.org>
    - update URL

* Fri Sep 10 2010 Götz Waschk <waschk@mandriva.org> 0.1-1mdv2011.0
+ Revision: 577096
- switch to 0.1 release

* Mon Aug 30 2010 Götz Waschk <waschk@mandriva.org> 0.1-0.20100713.1mdv2011.0
+ Revision: 574374
- import gudev-sharp

