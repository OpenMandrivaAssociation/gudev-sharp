%define git	cd3e7df
%define api	1.0
%define udev	146

Summary:	Mono bindings for the GUdev library
Name:		gudev-sharp
Version:	0.1
Release:	9
# http://github.com/mono/gudev-sharp/tarball/GUDEV_SHARP_0_1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://github.com/mono/gudev-sharp
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(gapi-2.0)
BuildRequires:	pkgconfig(gtk-sharp-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(mono)
Requires:	libgudev >= %{udev}

%description
This is a Mono binding for GUdev based on GTk#.

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Group:		Development/Other

%description devel
This is a Mono binding for GUdev based on GTk#.

%prep
%setup -qn mono-%{name}-%git
./autogen.sh

%build
./configure --prefix=%{_prefix} --libdir=%{_prefix}/lib
%make

%install
%makeinstall_std pkgconfigdir=%{_datadir}/pkgconfig

%files
%doc AUTHORS
%{_prefix}/lib/mono/%{name}-%{api}
%{_prefix}/lib/mono/gac/%{name}

%files devel
%{_datadir}/pkgconfig/%{name}-%{api}.pc

