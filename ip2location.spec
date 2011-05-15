%define	major 0
%define libname %mklibname ip2location %{major}
%define develname %mklibname ip2location -d

Summary:	IP2Location C Library
Name:		ip2location
Version:	4.0.2
Release:	%mkrel 1
Group:		System/Libraries
License:	GPLv2
URL:		http://www.ip2location.com/
Source0:	http://www.ip2location.com/download/C-IP2Location-%{version}.tar.gz
Patch0:		C-IP2Location-4.0.2-soname.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
IP2Location is a C library that enables the user to find the country, region,
city, coordinates, zip code, time zone, ISP, domain name, connection type,
area code and weather that any IP address or hostname originates from. It has
been optimized for speed and memory utilization. Developers can use the API to
query all IP2Location™ binary databases for applications written in C or
supporting static/dynamic library.

%package -n	%{libname}
Summary:	IP2Location C Library
Group:          System/Libraries

%description -n	%{libname}
IP2Location is a C library that enables the user to find the country, region,
city, coordinates, zip code, time zone, ISP, domain name, connection type,
area code and weather that any IP address or hostname originates from. It has
been optimized for speed and memory utilization. Developers can use the API to
query all IP2Location™ binary databases for applications written in C or
supporting static/dynamic library.

%package -n	%{develname}
Summary:	Static library and header files for the ip2location library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
IP2Location is a C library that enables the user to find the country, region,
city, coordinates, zip code, time zone, ISP, domain name, connection type,
area code and weather that any IP address or hostname originates from. It has
been optimized for speed and memory utilization. Developers can use the API to
query all IP2Location™ binary databases for applications written in C or
supporting static/dynamic library.

This package contains the development files for the ip2location library.

%prep

%setup -q -n C-IP2Location-%{version}
%patch0 -p0 -b .soname

chmod 644 AUTHORS ChangeLog IP2LOCATION_PRODUCTS_CATALOG.PDF LICENSE.TXT README

%build
autoreconf -fi

%configure2_5x
%make

%check
make check

%install
rm -rf %{buildroot}

%makeinstall_std

# cleanup
rm -f %{buildroot}%{_libdir}/*.*a

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog IP2LOCATION_PRODUCTS_CATALOG.PDF LICENSE.TXT README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so

