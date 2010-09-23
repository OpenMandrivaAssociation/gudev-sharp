%define name gudev-sharp
%define version 0.1
%define git cd3e7df
%define release %mkrel 1
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
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: mono-devel
BuildRequires: gtk+2-devel
BuildRequires: libgudev-devel >= %udev
BuildRequires: gtk-sharp2
BuildRequires: gtk-sharp2-devel
%if %mdvver >= 201100
Requires: libgudev >= %udev
%endif
#gw filter out deps from *.dll.config
%define _requires_exceptions ^lib.*0$

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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS
%_prefix/lib/mono/%name-%api
%_prefix/lib/mono/gac/%name

%files devel
%defattr(-,root,root)
%_datadir/pkgconfig/%name-%api.pc
